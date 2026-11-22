#!/usr/bin/env python3
"""Integer matrix checks for the parity-nullity proof on binary hypercubes.

Only standard Python is required.  The infinite-dimensional part is proved
symbolically in RESULT.md; this checks small nontrivial instances exactly.
"""


def clifford(m):
    assert m >= 1
    a = 4*m-3
    c = [5-4*m] + [4]*(m-1)
    assert sum(x*x for x in c) == a*a and all(c)
    N = 1 << m
    K = [[0]*N for _ in range(N)]
    for z in range(N):
        for j in range(m):
            parity = (z & ((1 << j)-1)).bit_count() % 2
            w = z ^ (1 << j)
            K[z][w] = (-1 if parity else 1)*c[j]
    assert all(K[i][j] == K[j][i] for i in range(N) for j in range(N))
    for i in range(N):
        for j in range(N):
            assert sum(K[i][k]*K[k][j] for k in range(N)) == (a*a if i == j else 0)
    return a, K


def mod_rank(M,p=1000003):
    a = [[v%p for v in row] for row in M]
    n=len(a);h=0
    for j in range(len(a[0])):
        pivot=next((k for k in range(h,n) if a[k][j]),None)
        if pivot is None: continue
        a[h],a[pivot]=a[pivot],a[h]
        inv=pow(a[h][j],p-2,p)
        for k in range(h+1,n):
            if a[k][j]:
                mult=a[k][j]*inv%p
                for l in range(j,len(a[0])):
                    a[k][l]=(a[k][l]-mult*a[h][l])%p
        h+=1
        if h==n:break
    return h


def main():
    for d in range(2,7):
        m=d-1; a,K=clifford(m)
        n=1<<d; h=1<<m
        M=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i<h)==(j<h):
                    M[i][j]=K[i%h][j%h]
                elif (i%h)==(j%h):
                    M[i][j]=a
                assert (M[i][j]!=0) == ((i^j).bit_count()==1)
        assert all(M[i][j]==M[j][i] for i in range(n) for j in range(n))
        E=[v for v in range(n) if v.bit_count()%2==0]
        O=[v for v in range(n) if v.bit_count()%2==1]
        B=[[M[i][j] for j in O] for i in E]
        r=mod_rank(B)
        assert r==n//4,(d,r)
        assert mod_rank(M)==n//2
        print(f'd={d}: vertices={n}, matrix_rank={n//2}, each_parity_kernel_dim={n//4}')
    print('MATRIX_CERTIFICATE_PASS')

if __name__=='__main__':main()
