"""Exact finite-field checks of nilpotent-step additive convolution and its Fourier spectrum.

Run: python3 check.py
Uses only the Python standard library. Finite checks corroborate, but do not
replace, the all-dimensional proof or establish asymptotic convergence.
"""
from collections import Counter
from itertools import product
from math import prod

class Field:
    def __init__(self, q):
        if q not in (2, 3, 4, 5):
            raise ValueError('supported exact-check fields: 2,3,4,5')
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q
    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q
    def sub(self, a, b):
        return self.add(a, self.neg(b))
    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        z = 0
        while b:
            if b & 1:
                z ^= a
            b >>= 1
            a <<= 1
            if a & 4:
                a ^= 7  # alpha^2 + alpha + 1 = 0
        return z

def dot(f, x, y):
    z=0
    for a,b in zip(x,y):
        z=f.add(z,f.mul(a,b))
    return z

def vecs(f,n):
    return list(product(range(f.q),repeat=n))

def rank(f,m):
    a=[list(row) for row in m]
    d=len(a); n=len(a[0]); r=0
    for j in range(n):
        piv=next((i for i in range(r,d) if a[i][j]),None)
        if piv is None: continue
        a[piv],a[r]=a[r],a[piv]
        scale=next(z for z in range(1,f.q) if f.mul(z,a[r][j])==1)
        a[r]=[f.mul(scale,x) for x in a[r]]
        for i in range(d):
            if i==r or a[i][j]==0: continue
            z=a[i][j]
            a[i]=[f.sub(a[i][k],f.mul(z,a[r][k])) for k in range(n)]
        r+=1
        if r==d: break
    return r

def matvec(f,b,v,n):
    return tuple(dot(f,b[i*n:(i+1)*n],v) for i in range(n))

def reps_projective(f,n):
    out=[]
    for v in vecs(f,n):
        if not any(v):continue
        first=next(x for x in v if x)
        inv=next(x for x in range(1,f.q) if f.mul(x,first)==1)
        w=tuple(f.mul(inv,x) for x in v)
        if w not in out:out.append(w)
    return out

def eigenline_count(f,b,n,lines):
    z=0; dims=[]
    for a in range(f.q):
        c=[]
        for i in range(n):
            c.append([f.sub(b[i*n+j], a if i==j else 0) for j in range(n)])
        dims.append(n-rank(f,c))
    for v in lines:
        w=matvec(f,b,v,n)
        if any(w==tuple(f.mul(a,x) for x in v) for a in range(f.q)):
            z+=1
    assert z==sum((f.q**d-1)//(f.q-1) for d in dims)
    return z,max(dims)

def flatten(X):return tuple(x for row in X for x in row)

def steps(f,n):
    out=set()
    for v in vecs(f,n):
        if not any(v): continue
        for u in vecs(f,n):
            if not any(u) or dot(f,v,u):continue
            out.add(tuple(f.mul(v[i],u[j]) for i in range(n) for j in range(n)))
    return out

def group(f,n):
    # A traceless matrix is determined by all entries except the last diagonal.
    arr=[]
    for c in product(range(f.q),repeat=n*n-1):
        a=list(c)
        tr=0
        for i in range(n-1):tr=f.add(tr,a[i*n+i])
        a.append(f.neg(tr))
        arr.append(tuple(a))
    return arr

def cgroup(f,n):
    return list(product(range(f.q),repeat=n*n-1))

def addtuple(f,a,b):return tuple(f.add(x,y) for x,y in zip(a,b))

def main_check(q,n,do_conv=True):
    f=Field(q);lines=reps_projective(f,n)
    S=steps(f,n)
    P=(q**n-1)//(q-1)
    k=(q**(n-1)-1)*P
    assert len(S)==k
    frequencies=[(0,)+tuple(v) for v in product(range(q),repeat=n*n-1)]
    spectral_numerators=[]
    eigmax=Counter()
    for B in frequencies:
        e,r=eigenline_count(f,B,n,lines)
        formula=q**(n-1)*e-P
        freqcounts=Counter()
        for X in S:
            tr=0
            for i in range(n):
                for j in range(n):tr=f.add(tr,f.mul(B[i*n+j],X[j*n+i]))
            freqcounts[tr]+=1
        assert len({freqcounts[a] for a in range(1,q)})==1
        assert freqcounts[0]-freqcounts[1]==formula
        spectral_numerators.append(formula)
        eigmax[r]+=1
    assert spectral_numerators.count(k)==1
    if n>2:
        expected=P*prod(q**n-q**j for j in range(1))
        assert eigmax[n-1]==expected,(q,n,eigmax[n-1],expected)
    if do_conv:
        H=cgroup(f,n); N=len(H)
        sx=[tuple(X[:-1]) for X in S]
        origin=(0,)*(n*n-1)
        counts={origin:1}
        for t in range(1,4):
            nxt=Counter()
            for x,v in counts.items():
                for s in sx:nxt[addtuple(f,x,s)]+=v
            counts=nxt
            lhs=N*sum(v*v for v in counts.values())-k**(2*t)
            rhs=sum(a**(2*t) for a in spectral_numerators if a!=k)
            assert lhs==rhs,(q,n,t,lhs,rhs)
    print('EXACT_SPECTRAL_CONVOLUTION_PASS q=%d n=%d generators=%d Fourier_classes=%d'%(q,n,k,len(frequencies)))

if __name__=='__main__':
    for q,n in ((2,2),(2,3),(3,2),(4,2),(5,2)):
        main_check(q,n)
    print('NILPOTENT_WALK_EXACT_CHECKS_PASS')
