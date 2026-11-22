"""Independent finite checks for directed-triangle-free two-type counts.
Uses only Python standard library. No external input or dependencies.
"""
from itertools import product
from fractions import Fraction

ALPHABET = (-1, 0, 1) # -1: old -> new; 0: absent; +1: new -> old
TRANSITION = ((4,2,1,1),(0,4,0,2),(0,0,3,2),(0,0,0,4))

def no_c3(words, adjacent):
    # Orient old i -> j if i<j. Check all directed triangles explicitly.
    n = len(words[0]); mat = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(i+1,n):
            mat[i][j]=1; mat[j][i]=-1
    for x in (0,1):
        for i,state in enumerate(words[x]):
            mat[n+x][i]=state
            mat[i][n+x]=-state
    mat[n][n+1]=adjacent; mat[n+1][n]=-adjacent
    for a in range(n+2):
        for b in range(a+1,n+2):
            for c in range(b+1,n+2):
                if mat[a][b]==mat[b][c]==mat[c][a] and mat[a][b]!=0:
                    return False
    return True

def valid_one(word):
    return not any(word[i]==1 and word[j]==-1 for i in range(len(word)) for j in range(i+1,len(word)))

def formula(n):
    one=(n+2)*2**(n-1) if n else 1
    arrow=(n*(n+9)*4**n//8+3**n) if n else 1
    # n*(n+9)*4**n/8 integer when n>=1
    total=one**2+2*arrow
    return one,arrow,total

def matrix_arrow(n):
    vec=[1,0,0,0]
    for _ in range(n):
        vec=[sum(vec[j]*TRANSITION[j][k] for j in range(4)) for k in range(4)]
    return sum(vec)

def brute(n):
    words=list(product(ALPHABET,repeat=n))
    valid=[w for w in words if valid_one(w)]
    counts={-1:0,0:0,1:0}
    for x in valid:
        for y in valid:
            for adjacent in (-1,0,1):
                if no_c3((x,y),adjacent):
                    counts[adjacent]+=1
    return len(valid), counts

for n in range(6):
    unary,arc,total=formula(n)
    one, counts=brute(n)
    assert one==unary,(n,one,unary)
    assert counts[1]==counts[-1]==arc,(n,counts,arc)
    assert counts[0]==unary*unary,(n,counts[0],unary)
    assert sum(counts.values())==total
    assert matrix_arrow(n)==arc
    print(f'n={n} unary={unary} each_arc={arc} no_edge={unary*unary} all={total} OK')
for n in range(6,101):
    unary,arc,total=formula(n)
    assert arc==matrix_arrow(n)
    assert Fraction(2*arc,total)>Fraction(1,2)
    assert Fraction(2*arc,total)<Fraction(2*formula(n-1)[1],formula(n-1)[2])
print('MATRIX_EXACT_TO_100; STRICT_ARC_DECAY_CHECKED_TO_100; ALL_TESTS_PASS')
