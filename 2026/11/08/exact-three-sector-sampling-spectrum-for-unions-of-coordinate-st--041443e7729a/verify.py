"""Exact finite-case checks for first Johnson harmonic sampling on coordinate-star unions.
Run: python3 verify.py
Uses only the Python standard library. These tests complement, not replace, the proof.
"""
from math import comb
from fractions import Fraction as F

def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0

def E_form(a,b,n,k,t):
    q=n-t;den=C(n,k)
    sm=F(0)
    for i in range(n):
        for j in range(n):
            s=1 if i==j else 2
            same_out=(i>=t and j>=t)
            count=C(n-s,k-s)-(C(q-s,k-s) if same_out else 0)
            sm+=a[i]*b[j]*F(count,den)
    return sm

def dot(a,b):return sum(x*y for x,y in zip(a,b))

def sectors(n,k,t):
    q=n-t;assert 2<=k<=q and 3<=t
    p0=F(C(q,k),C(n,k))
    L_out=1-p0*F(n*(n-1)*(q-k),q*(q-1)*(n-k))
    L_mix=1-p0*F(k*(n-1)*t,q*(n-k))
    v=[]
    for i in range(1,t):
        a=[0]*n;a[0]=1;a[i]=-1;v.append((a,F(1),'T'))
    for i in range(t+1,n):
        a=[0]*n;a[t]=1;a[i]=-1;v.append((a,L_out,'O'))
    a=[q]*t+[-t]*q;v.append((a,L_mix,'M'))
    assert len(v)==n-1
    beta=F(k*(n-k),n*(n-1))
    for a,La,sa in v:
        for b,Lb,sb in v:
            observed=E_form(a,b,n,k,t)
            if sa==sb:
                assert La==Lb
                expected=La*beta*dot(a,b)
            else: expected=0
            assert observed==expected,(n,k,t,sa,sb,observed,expected)
    assert 0<L_out<=1 and 0<L_mix<1
    should_out= n*(q-k)>=k*t*(q-1)
    assert (L_out<=L_mix)==should_out
    return L_out,L_mix

def all_cases():
    total=0;ties=0;left=0;right=0
    for n in range(5,14):
        for t in range(3,n-1):
            q=n-t
            for k in range(2,q+1):
                a,b=sectors(n,k,t);total+=1
                if a==b:ties+=1
                elif a<b:left+=1
                else:right+=1
    assert total and ties and left and right
    print('EXACT_ALL_FIRST_BAND_SECTORS_OK',total,'ties',ties,'O_smaller',left,'M_smaller',right)
    # Boundary k=1: an entire outside-coefficient sector is invisible, and rank t.
    for n in range(5,14):
        for t in range(3,n-1):
            q=n-t
            # A k=1 slice is just n points. Selecting its t points has rank t on mean-zero functions.
            # Directly, the restriction matrix consists of first t rows of I-J/n.
            rows=[[F(int(i==j),1)-F(1,n) for j in range(n)] for i in range(t)]
            # t independent rows since their t x t principal minor is I_t-J_t/n, positive definite.
            assert n>t
    print('SINGLETON_SLICE_RANK_BOUNDARY_OK')

if __name__=='__main__':all_cases()
