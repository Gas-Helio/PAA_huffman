def lcs(s1: str, s2: str):
    # rows -> s1 , cols -> s2
    rows = len(s1) + 1
    cols = len(s2) + 1

    # row0 and col0 will be 0 as they will signify null strings
    dp_array = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):

            # if the chars match, go for left-top diagonal value + 1
            if s1[i - 1] == s2[j - 1]:
                dp_array[i][j] = dp_array[i - 1][j - 1] + 1
            # otherwise get max of top or left
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], dp_array[i][j - 1])

    # length of longest common sub-sequence
    # return dp_array[rows-1][cols-1]

    # store the common sequence (will be stored in reverse)
    sub_sequence = []

    i = rows - 1
    j = cols - 1

    # find the lcs
    while i > 0 and j > 0:
        # if top is not equal, that means present char was used
        if dp_array[i][j] != dp_array[i - 1][j]:
            sub_sequence.append(s1[i - 1])
            i -= 1
            j -= 1
        # not used
        else:
            i -= 1
    
    # return length of lcs, list of char containing the lcs elements
    for i in range (rows):
        for j in range(cols):
            print('|'+str(dp_array[i][j])+'|',end="")
        print() 
    return dp_array[rows - 1][cols - 1], sub_sequence[::-1]

# main
if __name__ == "__main__":
    s1 = '10010101'
    s2 = '010110110'
    #s1 = 'universidade'
    #s2 = 'escola'

    max_lcs, sequence = lcs(s1, s2)

    print("Length of longest common sub-sequence")
    print(max_lcs)
    print("Longest commmon sub-sequence")
    print(''.join(sequence))