"""Exact finite-moment checks for alternating free/Ornstein-Uhlenbeck renewal switching.
Uses only Python's standard library. Run: python check.py
"""
from fractions import Fraction as Q
from math import comb, factorial


def moments(atoms, n):
    """Atoms are (nonnegative rational value, rational probability) pairs."""
    assert sum((p for _, p in atoms), Q(0)) == 1
    assert all(p >= 0 for _, p in atoms)
    return [sum((p * x**k for x, p in atoms), Q(0)) for k in range(n+1)]


def forward(b, a, n, r=Q(1), q=Q(1)):
    """b: release duration moments; a: exp(-lambda * confined duration) moments."""
    assert len(b) >= n+2 and len(a) >= n+1
    H = [Q(1)]
    F = [Q(1)]
    v = [Q(1)]
    for m in range(1, n+1):
        T = sum((Q(comb(m,j))*r**(m-j)*b[m-j]*H[j] for j in range(m)), Q(0))
        hm = a[m]*T/(1-a[m])
        H.append(hm)
        fm = sum((Q(comb(m,j))*r**(m-j)*b[m-j+1]*H[j] / Q(m-j+1) for j in range(m+1)), Q(0))/b[1]
        F.append(fm)
        vm = sum((Q(comb(m,j))*q**(m-j)*F[j] for j in range(m+1)), Q(0))
        v.append(vm)
    return H, F, v


def invert_confined(b, F, n, r=Q(1)):
    H = [Q(1)]
    a = [Q(1)]
    for m in range(1, n+1):
        correction = sum((Q(comb(m,j))*r**(m-j)*b[m-j+1]*H[j]/Q(m-j+1)/b[1] for j in range(m)), Q(0))
        hm = F[m] - correction
        H.append(hm)
        T = sum((Q(comb(m,j))*r**(m-j)*b[m-j]*H[j] for j in range(m)), Q(0))
        a.append(hm/(hm+T))
    return H, a


def invert_released(a, F, mean_b, n, r=Q(1)):
    b=[Q(1), mean_b]
    H=[Q(1)]
    for m in range(1, n+1):
        T=sum((Q(comb(m,j))*r**(m-j)*b[m-j]*H[j] for j in range(m)),Q(0))
        hm=a[m]*T/(1-a[m])
        H.append(hm)
        rest=sum((Q(comb(m,j))*r**(m-j)*b[m-j+1]*H[j]/Q(m-j+1)/mean_b for j in range(1,m+1)),Q(0))
        b.append((F[m]-rest)*Q(m+1)*mean_b/r**m)
    return b,H


def kernel(mat):
    """A nonzero exact rational vector in the nullspace of a wide matrix."""
    A=[[Q(x) for x in row] for row in mat]
    rows=len(A); cols=len(A[0]); piv=[]; rr=0
    for cc in range(cols):
        good=next((k for k in range(rr, rows) if A[k][cc]),None)
        if good is None:continue
        A[rr],A[good]=A[good],A[rr]
        t=A[rr][cc]; A[rr]=[x/t for x in A[rr]]
        for k in range(rows):
            if k!=rr and A[k][cc]:
                t=A[k][cc];A[k]=[A[k][j]-t*A[rr][j] for j in range(cols)]
        piv.append(cc);rr+=1
        if rr==rows: break
    free=next(c for c in range(cols) if c not in piv)
    x=[Q(0)]*cols;x[free]=Q(1)
    for row,c in enumerate(piv):x[c]=-A[row][free]
    assert any(x)
    assert all(sum((Q(t)*v for t,v in zip(row,x)),Q(0))==0 for row in mat)
    return x


def run():
    checks=0
    # Independent exact moments and inverse checks for numerous atomic laws.
    for B in [[(Q(1),Q(1))],[(Q(1),Q(1,2)),(Q(2),Q(1,2))],[(Q(1,2),Q(1,4)),(Q(2),Q(3,4))]]:
        for A in [[(Q(1,2),Q(1))],[(Q(1,2),Q(1,4)),(Q(1,4),Q(1,2)),(Q(1,8),Q(1,4))],[(Q(1,3),Q(2,3)),(Q(1,9),Q(1,3))]]:
            n=6
            b=moments(B,n+1);a=moments(A,n)
            H,F,v=forward(b,a,n)
            Hr,ar=invert_confined(b,F,n)
            br,Hb=invert_released(a,F,b[1],n)
            for k in range(n+1):
                assert Hr[k]==H[k];checks+=1
                assert ar[k]==a[k];checks+=1
                assert Hb[k]==H[k];checks+=1
                assert br[k]==b[k];checks+=1
                assert v[k]==sum((Q(comb(k,j))*F[j] for j in range(k+1)), Q(0));checks+=1
            assert br[n+1]==b[n+1];checks+=1
    # Explicit fixed-mean on-clock alias: weights at C=j*log(2), j=1..4.
    base=[Q(1,4)]*4
    direction=[Q(-1,2),Q(2),Q(-5,2),Q(1)]
    e=Q(1,20)
    pp=[base[j]+e*direction[j] for j in range(4)]
    qq=[base[j]-e*direction[j] for j in range(4)]
    assert all(x>0 for x in pp+qq)
    assert sum(pp)==sum(qq)==1;checks+=1
    assert sum((Q(j+1)*pp[j] for j in range(4)),Q(0))==sum((Q(j+1)*qq[j] for j in range(4)),Q(0));checks+=1
    atoms1=[(Q(1,2)**(j+1),pp[j]) for j in range(4)]
    atoms2=[(Q(1,2)**(j+1),qq[j]) for j in range(4)]
    aa1=moments(atoms1,4);aa2=moments(atoms2,4)
    assert aa1[1]==aa2[1] and aa1[2]!=aa2[2];checks+=1
    b=moments([(Q(1),Q(1))],5)
    h1,f1,v1=forward(b,aa1,4);h2,f2,v2=forward(b,aa2,4)
    assert f1[1]==f2[1] and f1[2]!=f2[2];checks+=1
    assert v1[1]==v2[1] and v1[2]!=v2[2];checks+=1
    print('EXPLICIT_ALIAS', 'same E[X^2|off]=',v1[1], 'distinct E[X^4|off]=',3*v1[2],3*v2[2])
    # All finite K: construct equal dwell means and first K exponential moments, while laws differ.
    for K in range(1,9):
        js=list(range(1,K+4))
        mat=[[Q(1) for j in js],[Q(j) for j in js]]
        mat += [[Q(1,2)**(j*m) for j in js] for m in range(1,K+1)]
        vec=kernel(mat)
        assert any(v!=0 for v in vec);checks+=1
        base=Q(1,len(js))
        eps=base/(2*max(abs(v) for v in vec))
        p=[base+eps*v for v in vec];t=[base-eps*v for v in vec]
        assert min(p+t)>0;checks+=1
        pa=moments([(Q(1,2)**j,p[i]) for i,j in enumerate(js)],K+1)
        ta=moments([(Q(1,2)**j,t[i]) for i,j in enumerate(js)],K+1)
        assert pa[:K+1]==ta[:K+1];checks+=1
        assert sum((p[i]*js[i] for i in range(len(js))),Q(0))==sum((t[i]*js[i] for i in range(len(js))),Q(0));checks+=1
        FF=forward(moments([(Q(1),Q(1))],K+2),pa,K)[1]
        GG=forward(moments([(Q(1),Q(1))],K+2),ta,K)[1]
        assert FF==GG;checks+=1
    # Strict Chebyshev evaluation: these (K+2) functions are linearly independent at
    # any (K+2) distinct confined times; check the rational grid as a finite witness.
    for K in range(1,9):
        js=list(range(1,K+3))
        matrix=[[Q(1) for j in js],[Q(j) for j in js]]
        matrix += [[Q(1,2)**(m*j) for j in js] for m in range(1,K+1)]
        d=Q(1)
        for t in range(len(js)):
            k=next(i for i in range(t,len(js)) if matrix[i][t]!=0)
            if k!=t:
                matrix[t],matrix[k]=matrix[k],matrix[t];d=-d
            p=matrix[t][t];d*=p
            for i in range(t+1,len(js)):
                scale=matrix[i][t]/p
                matrix[i]=[matrix[i][j]-scale*matrix[t][j] for j in range(len(js))]
        assert d!=0;checks+=1
    print('PASS',checks,'exact rational and constructive checks')

if __name__=='__main__':run()
