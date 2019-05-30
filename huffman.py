from __future__ import print_function, absolute_import

from heapqo import Heap
from collections import Counter

__all__ = ["Node", "Leaf", "Tree", "codebook"]


class Node(object):
    def __init__(self, left, right):
        self.parent = None
        left.parent = right.parent = self

        self.left = left
        self.right = right

        self.weight = left.weight + right.weight

    def __repr__(self):
        return "<Node with weight {}>".format(self.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class Leaf(Node):
    def __init__(self, symbol, weight):
        self.parent = None
        self.symbol = symbol
        self.weight = weight

    def __repr__(self):
        return "{} {} {}".format(
            self.symbol, self.code, self.weight
        )

    @property
    def code(self):
        code = ""
        n = self
        while n.parent is not None:
            codebit = "0" if n is n.parent.left else "1"
            code = codebit + code
            n = n.parent
        return code


class Tree(object):
    def __init__(self, symbolweights):
        leaves = [Leaf(*sw) for sw in symbolweights]
        heap = Heap(leaves[:])
        while len(heap) >= 2:
            heap.push(Node(heap.pop(), heap.pop()))

        self.root = heap.pop()
        self.codebook = {l.symbol: l.code for l in leaves}
        self.leaves = leaves
    def printar(self):
        print('{:5} | {:5} | {:5}'.format('Letra', 'Code', 'Freq'))
        for l in self.leaves:
            print('{:5} | {:5} | {:3}'.format(l.symbol, l.code, l.weight))


def codebook(symbolweights):
    return Tree(symbolweights).codebook

def print_codebook(symbolweights):
    return Tree(symbolweights).printar()

texto = 'The huffman code is boring'
texto_bin = ""

dicionario = codebook(Counter(texto).items())

print_codebook(Counter(texto).items())


for letra in texto:
    texto_bin += dicionario[letra]

print("\n{} ({} bits)".format(texto_bin, len(texto_bin)))