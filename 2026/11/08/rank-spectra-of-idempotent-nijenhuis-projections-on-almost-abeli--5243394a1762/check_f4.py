"""Direct exhaustive check over the genuine four-element extension field.
Field is GF(2)[u]/(u*u+u+1), represented by bit masks 0..3.
Tests the original torsion and idempotency conditions, not a classified family."""
from collections import Counter
from itertools import product


def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return z

M=[[mul(i,j) for j in range(4)] for i in range(4)]
Q=range(4)
V=list(product(Q,repeat=3))
B=[(1,0,0),(0,1,0),(0,0,1)]


def dot(a,b):
    v=0
    for x,y in zip(a,b):v^=M[x][y]
    return v


def rank3(columns):
    rows=[[columns[j][i] for j in range(3)] for i in range(3)]
    count=0
    for c in range(3):
        pivot=next((j for j in range(count,3) if rows[j][c]),None)
        if pivot is None:continue
        rows[count],rows[pivot]=rows[pivot],rows[count]
        inv={1:1,2:3,3:2}[rows[count][c]]
        rows[count]=[M[inv][u] for u in rows[count]]
        for j in range(3):
            if j!=count:
                fact=rows[j][c]
                if fact:rows[j]=[u^M[fact][v] for u,v in zip(rows[j],rows[count])]
        count+=1
    return count


def enumerate_original(A):
    pairs=[]
    for i in range(3):
        for j in range(i+1,3):pairs.append((i,j))
    def bracket(x,y):
        Ax=(M[A[0][0]][x[1]]^M[A[0][1]][x[2]],M[A[1][0]][x[1]]^M[A[1][1]][x[2]])
        Ay=(M[A[0][0]][y[1]]^M[A[0][1]][y[2]],M[A[1][0]][y[1]]^M[A[1][1]][y[2]])
        return (0, M[x[0]][Ay[0]]^M[y[0]][Ax[0]], M[x[0]][Ay[1]]^M[y[0]][Ax[1]])
    br0={(i,j):bracket(B[i],B[j]) for i,j in pairs}
    C=Counter()
    for columns in product(V,repeat=3):
        def apply(v):return tuple(dot(v,[columns[j][i] for j in range(3)]) for i in range(3))
        if any(apply(columns[j])!=columns[j] for j in range(3)):continue
        for i,j in pairs:
            lhs=bracket(columns[i],columns[j])
            v=bracket(columns[i],B[j]);w=bracket(B[i],columns[j]);z=apply(br0[i,j])
            inner=tuple(v[h]^w[h]^z[h] for h in range(3))
            if lhs!=apply(inner):break
        else:C[rank3(columns)]+=1
    return dict(C)


def main():
    cases=[
       ('scalar',((1,0),(0,1)),{0:1,1:336,2:336,3:1}),
       ('Jordan',((1,1),(0,1)),{0:1,1:80,2:80,3:1}),
       ('irreducible',((0,1),(2,1)),{0:1,1:16,2:16,3:1}),
       ('distinct split',((1,0),(0,2)),{0:1,1:144,2:144,3:1}),
    ]
    # x*x+x+u is irreducible over GF(4), since a^2+a only takes 0 or 1.
    for label,A,pred in cases:
        got=enumerate_original(A)
        assert got==pred,(label,got,pred)
        print(f'{label} GF(4) rank spectrum {got}; total {sum(got.values())}; PASS')
    print('ALMOST_ABELIAN_NIJENHUIS_GF4_EXTENSION_OK')


if __name__=='__main__':main()
