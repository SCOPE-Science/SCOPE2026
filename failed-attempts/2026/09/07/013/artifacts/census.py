"""Exact-rational census for 4x4 bimatrix games + fast integer N22 counter."""
from fractions import Fraction
import itertools

def det_fraction(M):
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    det = Fraction(1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if A[r][col] != 0:
                piv = r
                break
        if piv is None:
            return Fraction(0)
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            det = -det
        det *= A[col][col]
        for r in range(col+1, n):
            if A[r][col] != 0:
                f = A[r][col]/A[col][col]
                for c in range(col, n):
                    A[r][c] -= f*A[col][c]
    return det

def solve_fraction(M, b):
    n = len(M)
    A = [[Fraction(M[r][c]) for c in range(n)] for r in range(n)]
    B = [Fraction(x) for x in b]
    det = Fraction(1)
    for col in range(n):
        piv = None
        for r in range(col, n):
            if A[r][col] != 0:
                piv = r
                break
        if piv is None:
            return Fraction(0), None
        if piv != col:
            A[col], A[piv] = A[piv], A[col]
            B[col], B[piv] = B[piv], B[col]
            det = -det
        det *= A[col][col]
        for r in range(col+1, n):
            if A[r][col] != 0:
                f = A[r][col]/A[col][col]
                for c in range(col, n):
                    A[r][c] -= f*A[col][c]
                B[r] -= f*B[col]
    if det == 0:
        return det, None
    z = [Fraction(0)]*n
    for r in range(n-1, -1, -1):
        s = B[r] - sum(A[r][c]*z[c] for c in range(r+1, n))
        z[r] = s/A[r][r]
    return det, z

def census(A, B):
    eqs = []
    n = 4
    rows = list(range(n)); cols = list(range(n))
    for i in rows:
        for j in cols:
            v = Fraction(A[i][j]); w = Fraction(B[i][j])
            ok = True
            srow = {}; scol = {}
            for ip in rows:
                if ip == i: continue
                s = v - Fraction(A[ip][j])
                srow[ip] = s
                if s <= 0: ok = False
            for jp in cols:
                if jp == j: continue
                s = w - Fraction(B[i][jp])
                scol[jp] = s
                if s <= 0: ok = False
            if ok:
                eqs.append(dict(I=[i],J=[j],k=1,x=[Fraction(1)],y=[Fraction(1)],
                                v=v,w=w,srow=srow,scol=scol,
                                detM=Fraction(1),detN=Fraction(1)))
    for k in [2,3,4]:
        for I in itertools.combinations(rows,k):
            for J in itertools.combinations(cols,k):
                AIJ = [[A[i][j] for j in J] for i in I]
                BIJ = [[B[i][j] for j in J] for i in I]
                M = [[Fraction(0)]*(k+1) for _ in range(k+1)]
                for r in range(k):
                    for c in range(k):
                        M[r][c]=Fraction(AIJ[r][c])
                    M[r][k]=Fraction(-1)
                for c in range(k):
                    M[k][c]=Fraction(1)
                M[k][k]=Fraction(0)
                b = [Fraction(0)]*k+[Fraction(1)]
                detM, zM = solve_fraction(M,b)
                if detM==0 or zM is None: continue
                y = zM[:k]; v = zM[k]
                if any(t<=0 for t in y): continue
                N = [[Fraction(0)]*(k+1) for _ in range(k+1)]
                for r in range(k):
                    for c in range(k):
                        N[r][c]=Fraction(BIJ[c][r])
                    N[r][k]=Fraction(-1)
                for c in range(k):
                    N[k][c]=Fraction(1)
                N[k][k]=Fraction(0)
                detN, zN = solve_fraction(N,b)
                if detN==0 or zN is None: continue
                x = zN[:k]; w = zN[k]
                if any(t<=0 for t in x): continue
                ok=True
                srow={}; scol={}
                for ip in rows:
                    if ip in I: continue
                    u = sum(Fraction(A[ip][J[c]])*y[c] for c in range(k))
                    s = v-u
                    srow[ip]=s
                    if s<=0: ok=False
                for jp in cols:
                    if jp in J: continue
                    u = sum(x[r]*Fraction(B[I[r]][jp]) for r in range(k))
                    s = w-u
                    scol[jp]=s
                    if s<=0: ok=False
                if ok:
                    eqs.append(dict(I=list(I),J=list(J),k=k,x=x,y=y,v=v,w=w,
                                    srow=srow,scol=scol,detM=detM,detN=detN))
    return eqs

def count_N22_fast(A, B):
    c=0
    for i1 in range(4):
        for i2 in range(i1+1,4):
            for j1 in range(4):
                for j2 in range(j1+1,4):
                    a11=A[i1][j1];a12=A[i1][j2];a21=A[i2][j1];a22=A[i2][j2]
                    b11=B[i1][j1];b12=B[i1][j2];b21=B[i2][j1];b22=B[i2][j2]
                    DA=a11-a12-a21+a22
                    if DA==0: continue
                    nA=a22-a12; nA2=a11-a21
                    if nA*DA<=0 or nA2*DA<=0: continue
                    DB=b11-b12-b21+b22
                    if DB==0: continue
                    nB=b22-b21; nB2=b11-b12
                    if nB*DB<=0 or nB2*DB<=0: continue
                    ok=True
                    v_num=a11*nA+a12*nA2
                    for ip in range(4):
                        if ip==i1 or ip==i2: continue
                        u_num=A[ip][j1]*nA+A[ip][j2]*nA2
                        if (v_num-u_num)*DA<=0:
                            ok=False;break
                    if not ok: continue
                    w_num=b11*nB+b21*nB2
                    for jp in range(4):
                        if jp==j1 or jp==j2: continue
                        u_num=B[i1][jp]*nB+B[i2][jp]*nB2
                        if (w_num-u_num)*DB<=0:
                            ok=False;break
                    if ok: c+=1
    return c
