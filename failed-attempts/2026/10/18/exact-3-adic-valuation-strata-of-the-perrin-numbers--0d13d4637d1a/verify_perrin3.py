"""Exact finite cross-checks for the Perrin 3-adic residue theorem."""
M=((0,1,0),(0,0,1),(1,1,0))
B=((2,4,3),(3,5,4),(4,7,5))
v=(3,0,2)

def mv(A,x):
    return tuple(sum(A[i][j]*x[j] for j in range(3)) for i in range(3))

def mm(A,C):
    return tuple(tuple(sum(A[i][h]*C[h][j] for h in range(3)) for j in range(3)) for i in range(3))

def mpow(A,n):
    Z=((1,0,0),(0,1,0),(0,0,1))
    while n:
        if n&1: Z=mm(Z,A)
        A=mm(A,A); n//=2
    return Z

def check():
    assert mpow(M,13)==tuple(tuple((1 if i==j else 0)+3*B[i][j] for j in range(3)) for i in range(3))
    vals=[3,0,2]
    for i in range(3,3500): vals.append(vals[i-2]+vals[i-3])
    assert [x%3 for x in vals[:13]]==[0,0,2,0,2,2,2,1,1,0,2,1,2]
    for a,bb in ((0,12),(1,17),(3,29),(9,158)):
        assert mv(B,mv(mpow(M,a),v))[0]==bb
    for k in range(1,6):
        p=3**k
        period=13*3**(k-1)
        assert period<len(vals)
        roots=[n for n in range(period) if vals[n]%p==0]
        assert len(roots)==(4 if k==1 else 3), (k, roots)
        if k>=2:
            assert set(n%13 for n in roots)=={1,3,9}
    for a in (1,3,9):
        for m in range(1,5):
            mod=3**m
            roots=[t for t in range(mod) if vals[a+13*t]%(3*mod)==0]
            assert len(roots)==1,(a,m,roots)
    # independent recurrence and matrix powering comparisons
    for n in range(200):
        assert mv(mpow(M,n),v)[0]==vals[n]
    print('VERIFY_OK: M^13, residue base, 3-adic root uniqueness, all periods k<=5, matrix/recurrence equivalence')
if __name__=='__main__':check()
