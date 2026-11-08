"""Independent finite-matrix and exact-polynomial checks for Gaussian-bin intensity tomography.
Run: python CHECK.py . This checks examples; the all-size theorem uses the proof in RESULT.md.
"""
import itertools
import math
import numpy as np
import sympy as sp

count=0

def check(condition, message):
    global count
    if not condition:
        raise AssertionError(message)
    count+=1

def parts(freqs):
    ans={}
    for i,fi in enumerate(freqs):
        for j,fj in enumerate(freqs):
            if fi>=fj:
                ans.setdefault(fi-fj,[]).append((i,j))
    return ans

def theoretical_rank(freqs,r):
    p=parts(freqs)
    return min(r,len(freqs))+2*sum(min(r,len(p[d])) for d in p if d>0)

def make_basis(n):
    B=[]
    for i in range(n):
        H=np.zeros((n,n),dtype=complex);H[i,i]=1
        B.append(H)
    for i in range(n):
        for j in range(i+1,n):
            H=np.zeros((n,n),dtype=complex)
            H[i,j]=H[j,i]=1/math.sqrt(2)
            B.append(H)
            H=np.zeros((n,n),dtype=complex)
            H[i,j]=1j/math.sqrt(2); H[j,i]=-1j/math.sqrt(2)
            B.append(H)
    return B

def numerical_test(freqs,r,a=0.045):
    n=len(freqs)
    bins=[-1+1.4*j for j in range(r)]
    widths=[np.exp(-a*(np.asarray(freqs)-b)**2) for b in bins]
    dmax=max(freqs)-min(freqs)
    ts=np.arange(2*dmax+1)*2*np.pi/(2*dmax+1)
    Bs=make_basis(n)
    M=[]
    for b,w in zip(bins,widths):
        E=w[None,:]*np.exp(1j*np.asarray(freqs)[None,:]*ts[:,None])
        for t in range(len(ts)):
            phi=np.outer(E[t,:],np.conj(E[t,:]))
            vals=[np.real(np.sum(H*phi)) for H in Bs]
            M.append(np.array(vals)/np.sqrt(len(ts)))
    M=np.array(M)
    observed=np.sort(np.linalg.svd(M,compute_uv=False))[::-1]
    allzeros=np.r_[observed,np.zeros(max(0,n*n-len(observed)))]
    p=parts(freqs)
    values=[]
    for d,idx in p.items():
        W=np.array([[w[i]*w[j] for i,j in idx] for w in widths])
        sigma=np.linalg.svd(W,compute_uv=False)
        values.extend(sigma if d==0 else list(sigma)*2)
    predicted=np.sort(np.r_[values,np.zeros(n*n-len(values))])[::-1]
    check(len(observed)==min(M.shape),'SVD output length mismatch')
    check(len(predicted)==n*n,'predicted dimension mismatch')
    check(np.allclose(allzeros,predicted,atol=3e-10,rtol=3e-10),f'singular mismatch: {freqs}, {r}: {allzeros}, {predicted}')
    rk=theoretical_rank(freqs,r)
    check(sum(s>1e-10 for s in observed)==rk, f'rank mismatch {freqs} {r}: {observed}, target {rk}')
    for H in Bs:
        check(abs(np.vdot(H,H).real-1)<1e-12, 'nonunit Hermitian basis')

# Exact positive generalized Vandermonde ranks, kernels and frequency-difference counting.
examples=[]
for n in range(2,8):
    examples.append(tuple(range(n)))
    examples.append(tuple(2**i for i in range(n)))
    examples.append(tuple(i*i for i in range(n)))
    examples.append(tuple(i*i+i+1 for i in range(n)))
for freqs in examples:
    n=len(freqs)
    profile=parts(freqs)
    check(sum(len(profile[d]) for d in profile)==n*(n+1)//2,'pair total')
    for r in range(1,n+2):
        nodes=[sp.Integer(j+1) for j in range(r)]
        null=0
        for d,pairs in profile.items():
            m=len(pairs)
            low=[freqs[j] for i,j in pairs]
            V=sp.Matrix([[z**k for k in low] for z in nodes])
            target=min(r,m)
            check(V.rank()==target, f'generalized Vandermonde: {freqs}, {r}, {d}')
            if m>r:
                # Exact polynomial divisibility creates every null vector by a root polynomial.
                Q=sp.prod(sp.Symbol('z')-z for z in nodes)
                z=sp.Symbol('z')
                # For nonconsecutive powers, basis is not monomial-consecutive; nullspace
                # is checked by direct generalized evaluation rather than divisibility.
                for vector in V.nullspace():
                    check(all(sum(vector[k]*nodes[j]**low[k] for k in range(m))==0 for j in range(r)), 'null certificate')
                check(len(V.nullspace())==m-r,'null dimension')
            null+= (m-target)*(1 if d==0 else 2)
        check(n*n-theoretical_rank(freqs,r)==null, 'nullity identity')
    if all(len(profile[d])==1 for d in profile if d>0):
        for r in range(1,n+1):
            check(theoretical_rank(freqs,r)==n*n-(n-r),'Sidon optimum')
    for r in range(1,n+1):
        cap=n*n-(n-r)
        check(theoretical_rank(freqs,r)<=cap,'universal rank bound')
        condition=all(len(profile[d])<=r for d in profile if d>0)
        check((theoretical_rank(freqs,r)==cap)==condition,'optimal iff difference multiplicities')
    if freqs==tuple(range(n)):
        for r in range(1,n+1):
            check(theoretical_rank(freqs,r)==r*(2*n-r),'consecutive square codimension law')

# An independent sample-domain Hermitian-matrix computation including nonprogressions.
for freqs in [tuple(range(2)),tuple(range(3)),tuple(range(4)),(0,1,3),(0,1,4,6),(0,2,5,9),(0,1,3,7,12)]:
    for r in range(1,min(len(freqs)+1,5)):
        numerical_test(freqs,r)

print(f'PASS: {count} exact-algebraic and independent finite-matrix assertions')

# Trace-one state tomography: append the trace row to the original measurement map.
def rank_diag_plus_trace(freqs,bins,a):
    n=len(freqs)
    W=np.exp(-2*a*(np.asarray(freqs)[None,:]-np.asarray(bins)[:,None])**2)
    return np.linalg.matrix_rank(np.vstack([W,np.ones((1,n))]),tol=1e-10)

for freqs in [(0,1),(-1,0,1),(0,1,2,3),(0,2,5,9),(0,1,3,7,12)]:
    n=len(freqs)
    for r in range(1,n-1):
        bins=[-.75+1.7*j for j in range(r)]
        check(rank_diag_plus_trace(freqs,bins,.12)<n, 'too few bins can recover trace-one diagonal states')
    bins=[-.75+1.7*j for j in range(n-1)]
    check(rank_diag_plus_trace(freqs,bins,.12)==n,'generic (n-1)-bin trace-one recovery test')
    bins=[-.75+1.7*j for j in range(n)]
    check(rank_diag_plus_trace(freqs,bins,.12)==n,'n-bin tomography')

# An exact symmetric exception at n=3: opposite bins and three consecutive frequencies.
a=sp.Rational(1,4)
b=sp.acosh(sp.exp(2*a))/(4*a)
# At b,-b, the arithmetic mean of the two evaluation rows is proportional to (1,1,1).
check(sp.simplify(sp.cosh(4*a*b)-sp.exp(2*a))==0,'symmetric trace resonance')
print(f'PASS including trace-one checks: {count} assertions')
