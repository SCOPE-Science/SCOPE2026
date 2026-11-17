"""Exact branch matrices and independent interval-preimage checks for open zigzag maps."""
import math
import numpy as np


def metallic(m):
    return ((m+math.sqrt(m*m+4))/2 if m%2==0 else
            (m+1+math.sqrt((m+1)**2-4))/2)


def transition(m,j):
    L=metallic(m)
    allowed=[i for i in range(m+1) if i!=j]
    A=np.zeros((m,m), dtype=np.int64)
    length=np.array([1/L if i<m else (L-m)/L for i in allowed])
    for a,i in enumerate(allowed):
        for b,k in enumerate(allowed):
            # For i<m the branch covers [0,1]; for i=m only the last part.
            A[a,b]=int(i<m or (k==0 if m%2==0 else k>=1))
    return L,A,length


def direct_survivors(m,j,n):
    L=metallic(m)
    e=1/L
    E=[(0,j*e),((j+1)*e,1)]
    E=[(a,b) for a,b in E if b-a>1e-12]
    K=E
    for _ in range(1,n):
        new=[]
        for i in range(m+1):
            u=i/L;v=min((i+1)/L,1.)
            fu=abs(L*u-2*round(L*u/2))
            fv=abs(L*v-2*round(L*v/2))
            # At mesh endpoints nearest even integer maps correctly.
            for a,b in K:
                yl=max(a,min(fu,fv));yr=min(b,max(fu,fv))
                if yr<=yl+1e-13:continue
                x1=u+(yl-fu)*(v-u)/(fv-fu)
                x2=u+(yr-fu)*(v-u)/(fv-fu)
                low,high=min(x1,x2),max(x1,x2)
                for p,q in E:
                    low2=max(low,p);high2=min(high,q)
                    if high2>low2+1e-13:new.append((low2,high2))
        K=new
    return sum(b-a for a,b in K)

count=0
for m in range(2,9):
    L=metallic(m)
    expected=(L*L-m*L-1 if m%2==0 else L*L-(m+1)*L+1)
    assert abs(expected)<1e-10
    for j in range(m):
        lam,A,length=transition(m,j)
        assert len(length)==m
        pred=(m-1 if j==0 and m%2==0 else m if j==0 else
              (m-1+math.sqrt((m-1)**2+4))/2 if m%2==0 else
              (m+math.sqrt(m*m-4))/2)
        rho=max(abs(z) for z in np.linalg.eigvals(A))
        assert abs(rho-pred)<1e-9,(m,j,rho,pred)
        assert rho<L
        if m<=5:
            for n in range(1,5):
                Sn=float(np.ones(m)@np.linalg.matrix_power(A,n-1)@length)/L**(n-1)
                direct=direct_survivors(m,j,n)
                assert abs(Sn-direct)<1e-9,(m,j,n,Sn,direct)
                count+=1
    for n in range(2,8):
        s=[]
        for j in range(m):
            _,A,l=transition(m,j)
            s.append(float(np.ones(m)@np.linalg.matrix_power(A,n-1)@l)/L**(n-1))
        assert max(s[1:])-min(s[1:])<1e-10
        assert (s[0]<min(s[1:])) if m%2==0 else (s[0]>max(s[1:]))
    print(f'm={m} slope={L:.12f} spectral/horizon checks passed')
print(f'VERIFY_OK cases={count} escape_spectra=all_m_2_to_8 finite_order=all_n_2_to_7')
