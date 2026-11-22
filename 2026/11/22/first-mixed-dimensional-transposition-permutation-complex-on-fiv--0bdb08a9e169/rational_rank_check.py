"""Independent direct rational boundary-rank check for the five-letter case.

Execute: python3 rational_rank_check.py
Uses only the Python standard library and does not import the Morse checker.
"""
from itertools import combinations
from fractions import Fraction


def words(n=5):
    all_words = [set() for _ in range(n)]
    for i,j in combinations(range(n),2):
        perm = list(range(1,n+1))
        perm[i],perm[j] = perm[j],perm[i]
        for mask in range(1,1<<n):
            word=tuple(perm[t] for t in range(n) if (mask>>t)&1)
            all_words[len(word)-1].add(word)
    return [sorted(layer) for layer in all_words]


def rank_over_q(matrix):
    a = [[Fraction(z) for z in row] for row in matrix]
    m = len(a)
    n = len(a[0]) if m else 0
    pivot_row = 0
    for col in range(n):
        j = next((i for i in range(pivot_row,m) if a[i][col]),None)
        if j is None:
            continue
        a[pivot_row],a[j] = a[j],a[pivot_row]
        pivot=a[pivot_row][col]
        a[pivot_row]=[z/pivot for z in a[pivot_row]]
        for i in range(pivot_row+1,m):
            if a[i][col]:
                c=a[i][col]
                a[i]=[z-c*w for z,w in zip(a[i],a[pivot_row])]
        pivot_row+=1
        if pivot_row==m:
            break
    return pivot_row


def main():
    sets = words()
    expected=[4,16,30,10]
    assert [len(layer) for layer in sets]==[5,20,48,41,10]
    for degree in range(1,5):
        lower, upper=sets[degree-1],sets[degree]
        address={word:i for i,word in enumerate(lower)}
        mat=[[0]*len(upper) for _ in lower]
        for j,word in enumerate(upper):
            for k in range(len(word)):
                mat[address[word[:k]+word[k+1:]]][j]=1 if k%2==0 else -1
        got=rank_over_q(mat)
        assert got==expected[degree-1],(degree,got)
        print('boundary',degree,'rank',got,'size',len(lower),'x',len(upper))
    print('all exact rational boundary-rank checks passed')


if __name__=='__main__':
    main()
