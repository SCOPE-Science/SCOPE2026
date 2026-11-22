"""Independent coefficient-level verification of irreducible sextic Richelot counts.
Usage: python3 check_richelot.py   (Python 3 standard library only).
Enumerates all monic degree-six polynomials in F_p[x] for p=3,5 and all
PGL2(F_p) involutions, then tests binary-sextic invariance coefficient-wise.
This is a finite-field check; the all-q proof is symbolic and independent.
"""
from itertools import product
from math import comb

def trim(f):
    while len(f)>1 and f[-1]==0: f.pop()
    return f

def rem(a,b,p):
    a=trim(a[:]); b=trim(b[:]); inv=pow(b[-1],-1,p)
    while len(a)>=len(b) and any(a):
        coeff=a[-1]*inv%p
        offset=len(a)-len(b)
        for j,v in enumerate(b): a[offset+j]=(a[offset+j]-coeff*v)%p
        trim(a)
    return a

def gcd(a,b,p):
    while any(b): a,b=b,rem(a,b,p)
    return a

def mul_mod(a,b,f,p):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=(c[i+j]+x*y)%p
    return rem(c,f,p)

def powx_mod(exponent,f,p):
    r=[1]; a=[0,1]
    while exponent:
        if exponent&1:r=mul_mod(r,a,f,p)
        exponent>>=1
        if exponent:a=mul_mod(a,a,f,p)
    return r

def is_irred(f,p):
    x=[0,1]
    def sub_x(a):
        b=a[:]
        if len(b)<2:b += [0]*(2-len(b))
        b[1]=(b[1]-1)%p
        return trim(b)
    return len(gcd(f,sub_x(powx_mod(p**2,f,p)),p))==1 and len(gcd(f,sub_x(powx_mod(p**3,f,p)),p))==1 and powx_mod(p**6,f,p)==x

def poly_mul(a,b,p):
    v=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):v[i+j]=(v[i+j]+x*y)%p
    return v

def pow_linear(a,b,n,p):
    return [comb(n,i)*pow(a,i,p)*pow(b,n-i,p)%p for i in range(n+1)]

def involutions(p):
    ans=[]; seen=set()
    for a,b,c in product(range(p),repeat=3):
        d=(-a)%p
        det=(a*d-b*c)%p
        if det==0: continue
        vec=(a,b,c,d)
        v=next(x for x in vec if x)
        key=tuple(x*pow(v,-1,p)%p for x in vec)
        if key in seen: continue
        seen.add(key)
        split=pow((-det)%p,(p-1)//2,p)==1
        # precompute action on homogeneous monomials x^i z^(6-i)
        mat=[]
        for i in range(7):
            mat.append(poly_mul(pow_linear(a,b,i,p),pow_linear(c,d,6-i,p),p))
        ans.append((key,split,mat))
    assert len(ans)==p*p
    assert sum(1 for _,sp,_ in ans if sp)==p*(p+1)//2
    return ans

def verify(p):
    invols=involutions(p)
    hist={0:0,1:0,2:0}; splits=[0,0]
    for coeff in product(range(p),repeat=6):
        f=list(coeff)+[1]
        if not is_irred(f,p):continue
        hits=[]
        for key,split,mat in invols:
            transformed=[sum(f[i]*mat[i][j] for i in range(7))%p for j in range(7)]
            scale=transformed[-1]
            if scale and transformed==[(scale*t)%p for t in f]:hits.append((key,split))
        assert len(hits)<=1,(p,f,hits)
        hist[len(hits)]=hist.get(len(hits),0)+1
        if hits:splits[0 if hits[0][1] else 1]+=1
    n_all=(p**6-p**3-p**2+p)//6
    n_deg=p**3*(p*p-1)//6
    exp_split=p*p*(p-1)*(p+1)**2//12
    exp_nonsplit=p*p*(p-1)**2*(p+1)//12
    print(f'p={p}: total={sum(hist.values())}, no_decomposition={hist[0]}, decomposed={hist[1]}, split={splits[0]}, nonsplit={splits[1]}')
    assert sum(hist.values())==n_all
    assert hist[1]==n_deg
    assert splits==[exp_split,exp_nonsplit]

if __name__=='__main__':
    verify(3)
    verify(5)
    print('All independent coefficient-level tests passed.')
