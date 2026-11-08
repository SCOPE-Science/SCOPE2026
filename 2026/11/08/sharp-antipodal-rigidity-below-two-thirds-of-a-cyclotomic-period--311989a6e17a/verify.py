#!/usr/bin/env python3
"""Exact finite checks for a short nonnegative cyclotomic-cone theorem.
The general theorem depends on the algebraic proof in RESULT.md, not on finite enumeration.
"""

def trim(v):
    v=list(v)
    while len(v)>1 and v[-1]==0:
        v.pop()
    return v


def divide_monic(f,g):
    f=trim(f);g=trim(g)
    if g[-1]!=1: raise ValueError('monic divisor required')
    q=[0]*max(1,len(f)-len(g)+1)
    while len(f)>=len(g):
        j=len(f)-len(g);c=f[-1];q[j]=c
        for k,ck in enumerate(g):f[j+k]-=c*ck
        f=trim(f)
        if f==[0]:break
    return trim(q),trim(f)


def cyclotomic(n):
    cur=[-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n%d==0:
            cur,rem=divide_monic(cur,cyclotomic_cached(d))
            assert rem==[0]
    return trim(cur)

_CACHE={1:[-1,1]}
def cyclotomic_cached(n):
    if n not in _CACHE:_CACHE[n]=cyclotomic(n)
    return _CACHE[n]


def poly_from_exponents(E):
    r=[0]*(max(E)+1) if E else [0]
    for e in E:r[e]+=1
    return r


def residue_monomials(P,degree):
    d=len(P)-1; r=[1]+[0]*(d-1)
    for j in range(degree+1):
        yield list(r)
        h=r[-1];r=[0]+r[:-1]
        for i in range(d):r[i]-=h*P[i]


def check():
    phi=cyclotomic_cached(30)
    expected=[1,1,0,-1,-1,-1,0,1,1]
    assert phi==expected,(phi,expected)
    rem=list(residue_monomials(phi,20))
    weights=[2*z[5]+z[6]+z[7] for z in rem]
    assert weights==([0]*5+[2,1,1,1,2,2,1,1,1,2]+[0]*5+[-2]),weights
    print('EXACT_DUAL_CERTIFICATE_OK',weights[:20])

    # Independently scan all binary coefficient choices in the full 20-position window.
    # Use Gray-code updates in the 8-dimensional integer remainder space.
    v=[0]*8;prev=0;zeros=1
    for counter in range(1,1<<20):
        mask=counter^(counter>>1)
        changed=mask^prev; j=changed.bit_length()-1
        sign=1 if mask & changed else -1
        r=rem[j]
        for i in range(8):v[i]+=sign*r[i]
        if not any(v):
            zeros+=1
            assert all(not(mask>>j&1) for j in range(5,15)),mask
            assert all(((mask>>j)&1)==((mask>>(j+15))&1) for j in range(5)),mask
        prev=mask
    assert zeros==32,zeros
    print('BINARY_WINDOW_EXHAUSTIVE_OK masks=',1<<20,'divisible_including_zero=',zeros)

    # Verify the standard and the non-polygonal six-term witnesses at the phase boundary.
    asymmetric=(0,1,7,13,19,20)
    assert divide_monic(poly_from_exponents(asymmetric),phi)[1]==[0]
    for a in range(1,6):
        t=1<<(a-1);N=30*t
        phiN=cyclotomic_cached(N)
        lift=[0]*(8*t+1)
        for j,c in enumerate(phi):lift[t*j]=c
        assert trim(lift)==phiN,(N,phiN,trim(lift))
        for exps in ((0,10*t,20*t),tuple(t*j for j in asymmetric)):
            f=poly_from_exponents(exps)
            assert divide_monic(f,phiN)[1]==[0],(a,exps)
            assert max(exps)-min(exps)==20*t
            assert any((e+15*t) not in exps for e in exps if e < 5*t) or 10*t in exps
        A=[(i*i+7*i+3)%3 for i in range(5*t)]
        A[0]=A[-1]=1
        f=[0]*(20*t)
        for i,c in enumerate(A):
            f[i]+=c;f[i+15*t]+=c
        assert divide_monic(trim(f),phiN)[1]==[0],a
        assert len(trim(f))-1==20*t-1
        print('DYADIC_LIFT_OK a=',a,'n=',N,'sharp_diameter=',20*t)
    print('VERIFY_OK exact=true finite_checks_do_not_replace_proof=true')

if __name__=='__main__':check()
