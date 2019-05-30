parent = dict()


def make_set(vertice):
    parent[vertice] = vertice


# returns first element of set, which includes 'vertice'
def find_set(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find_set(parent[vertice])
    return parent[vertice]


# joins two sets: set, which includes 'vertice1' and set, which
# includes 'vertice2'
def union(u, v, edges):
    ancestor1 = find_set(u)
    ancestor2 = find_set(v)
    # if u and v are not connected by a path
    if ancestor1 != ancestor2:
        for edge in edges:
            parent[ancestor1] = ancestor2


def kruskal(graph):
    mst = set()
    # puts all the vertices in seperate sets
    for vertice in graph['V']:
        make_set(vertice)

    edges = list(graph['E'])
    # sorts edges in ascending order
    edges.sort()
    for edge in edges:
        weight, u, v = edge
        # checks if current edge do not close cycle
        if find_set(u) != find_set(v):
            mst.add(edge)
            union(u, v, edges)

    return mst


# input graph
graph = {
    'V': ['1', '2', '3', '4', '5', '6', '7', '8'],
    'E': set([
            (240, '1', '2'),
            (210, '1', '3'),
            (340, '1', '4'),
            (280, '1', '5'),
            (200, '1', '6'),
            (345, '1', '7'),
            (120, '1', '8'),
            (265, '2', '3'),
            (175, '2', '4'),
            (215, '2', '5'),
            (180, '2', '6'),
            (185, '2', '7'),
            (155, '2', '8'),
            (260, '3', '4'),
            (115, '3', '5'),
            (350, '3', '6'),
            (435, '3', '7'),
            (195, '3', '8'),
            (160, '4', '5'),
            (330, '4', '6'),
            (295, '4', '7'),
            (230, '4', '8'),
            (360, '5', '6'),
            (400, '5', '7'),
            (170, '5', '8'),
            (175, '6', '7'),
            (205, '6', '8'),
            (305, '7', '8'),
    ])
}

mst = kruskal(graph)
print("Minimal Spanning Tree:")
print(mst)
mst_weight = 0
for edge in mst:
    weight, u, v = edge
    mst_weight += weight

print("Cost: ")
print(mst_weight)

#https://github.com/nbistrickis/kruskal/blob/master/kruskal.py
