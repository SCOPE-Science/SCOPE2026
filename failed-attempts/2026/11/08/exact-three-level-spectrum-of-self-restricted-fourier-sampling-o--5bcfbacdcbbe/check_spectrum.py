"""Independent finite tests for restricted additive Fourier sampling on GL(2,q).

Only field sizes 2, 3, 4 and 5 are enumerated. The general theorem
rests on the symbolic representation-theoretic proof, not these tests.
"""
import itertools
import numpy as np


def finite_field(q):
    if q != 4:
        add = np.array([[(a+b) % q for b in range(q)] for a in range(q)], dtype=int)
        mul = np.array([[(a*b) % q for b in range(q)] for a in range(q)], dtype=int)
        phase = np.exp(2j*np.pi*np.arange(q)/q)
        return add, mul, phase
    # GF(4) = F_2[x]/(x^2+x+1); integers encode polynomial coefficients.
    add = np.array([[a ^ b for b in range(4)] for a in range(4)], dtype=int)
    def product(a, b):
        value = 0
        for j in range(2):
            if (b >> j) & 1:
                value ^= a << j
        if value & 4:
            value ^= 7
        return value
    mul = np.array([[product(a,b) for b in range(4)] for a in range(4)], dtype=int)
    trace = [add[a, mul[a,a]] for a in range(4)]
    assert trace == [0,0,1,1]
    phase = np.array([(-1) ** t for t in trace], dtype=complex)
    return add, mul, phase


def rank2(x, add, mul):
    a,b,c,d = x
    char = 2 if len(add)==4 else len(add)
    minus = lambda t: next(s for s in range(len(add)) if add[t,s]==0)
    det = add[mul[a,d], minus(mul[b,c])]
    if det != 0:
        return 2
    return 0 if not any(x) else 1


def check(q):
    add,mul,phase = finite_field(q)
    mats = np.array(list(itertools.product(range(q),repeat=4)),dtype=int)
    ranks = np.array([rank2(x,add,mul) for x in mats])
    group=mats[ranks==2]
    n=len(group)
    assert n==(q*q-1)*(q*q-q)
    # Evaluate all additive pairings in the matrix space using field tables.
    pairing=np.zeros((q**4, n),dtype=np.int32)
    for t in range(4):
        pairing=add[pairing,mul[mats[:,t,None],group[None,:,t]]]
    K=phase[pairing].sum(axis=1)
    predicted=np.where(ranks==0,n,np.where(ranks==1,-q*(q-1),q))
    assert np.allclose(K,predicted,atol=1e-8)
    assert abs(K[0]-n)<1e-8
    # All invertible-matrix rows and columns: compute their actual complex Gram.
    index=np.flatnonzero(ranks==2)
    H=phase[pairing[index,:]]
    B=H@H.conj().T
    # Predicted Hermitian Gram depends only on rank of matrix differences.
    rdist=np.empty((n,n),dtype=np.int8)
    for i,x in enumerate(group):
        dif=np.array([[add[x[j], next(s for s in range(q) if add[y[j],s]==0)] for j in range(4)] for y in group])
        rdist[i]=[rank2(z,add,mul) for z in dif]
    exact=np.where(rdist==0,n,np.where(rdist==1,-q*(q-1),q))
    assert np.allclose(B,exact,atol=1e-7)
    predicted_levels={q*q:1+q*q, q**3:(q-2)*(q+1)**2,
                      q**4:n-(1+q*q)-(q-2)*(q+1)**2}
    ev=np.linalg.eigvalsh(B)
    for v,m in predicted_levels.items():
        near=int(np.sum(np.abs(ev-v)<1e-6))
        assert near==m, (q,v,near,m)
    assert sum(predicted_levels.values())==n
    # Independent singular-value comparison, and no omitted near-zero singularity.
    sv=np.linalg.svd(H,compute_uv=False)
    assert abs(sv[-1]-q)<1e-6
    assert abs(sv[0]-q*q)<1e-6
    print('q=%d, |GL_2|=%d, Gram spectrum=%s, condition=%g, direct Fourier check PASS' %
          (q,n,sorted(predicted_levels.items()),sv[0]/sv[-1]))


if __name__=='__main__':
    for q in [2,3,4,5]:
        check(q)
    print('GL2_RESTRICTED_FOURIER_SPECTRUM_PASS')
