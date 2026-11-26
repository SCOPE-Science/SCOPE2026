"""Independent numerical checks for two projective-plane distance-kernel families.
Scientific output only; finite checks are not proofs of universal assertions.
Run: python checker.py
"""
import math
import numpy as np


def incidence_prime(q):
    """PG(2,q), q prime, normalized homogeneous points and lines."""
    pset = []
    for x in range(q):
        for y in range(q):
            pset.append((1,x,y))
    for z in range(q):
        pset.append((0,1,z))
    pset.append((0,0,1))
    a = np.array(pset,dtype=int)
    b = ((a[:,None,:]*a[None,:,:]).sum(axis=2)%q==0).astype(float)
    v=q*q+q+1
    assert len(pset)==v
    assert np.all(b.sum(axis=0)==q+1) and np.all(b.sum(axis=1)==q+1)
    assert np.all(b@b.T == q*np.eye(v)+np.ones((v,v)))
    return b


def powered_distance(B,p):
    v=B.shape[0]
    A=(np.ones((v,v))-np.eye(v))*2**p
    C=B+(1-B)*3**p
    return np.block([[A,C],[C.T,A]])


def predicted_eig(v,k,lam,p):
    s=math.sqrt(k-lam)
    d=2**p
    r=3**p-1
    # mean-zero: two sectors +/- with multiplicity v-1, constant odd sector
    return np.sort(np.r_[np.repeat(-d+r*s,v-1),
                            np.repeat(-d-r*s,v-1),
                            (v-1)*d-k-(v-k)*3**p])


def beta_spectral(q):
    lo,hi=0.,1.
    for _ in range(80):
        p=(lo+hi)/2
        if (3**p-1)*math.sqrt(q)<2**p:lo=p
        else:hi=p
    return (lo+hi)/2


def beta_complement(q):
    if q==2:return beta_spectral(q)
    lo,hi=0.,1/q
    for _ in range(80):
        p=(lo+hi)/2
        f=q*(q+1)*2**p-q*q-(q+1)*3**p
        if f<0:lo=p
        else:hi=p
    return (lo+hi)/2


def run():
    count=0
    for q in (2,3,5,7):
        B=incidence_prime(q)
        v=B.shape[0]
        for kind,C in [('incidence',B),('nonincidence',1-B)]:
            k=int(C.sum(axis=0)[0])
            lam=int(round((C@C.T)[0,1]))
            root=beta_spectral(q) if kind=='incidence' else beta_complement(q)
            print(f'q={q:2}, {kind:12}, n={2*v:3}, beta={root:.12g}, k={k}, lambda={lam}')
            J=np.ones((2*v,2*v))/(2*v)
            P=np.eye(2*v)-J
            for p in (0.,root*.2,root*.8,root,root+.04):
                D=powered_distance(C,p)
                raw=np.linalg.eigvalsh(-0.5*P@D@P)
                direct=np.delete(raw,np.argmin(np.abs(raw)))
                # remove the constant-vector zero eigenvalue, not the least eigenvalue
                from_spectrum=-.5*predicted_eig(v,k,lam,p)[::-1]
                assert np.max(np.abs(np.sort(direct)-np.sort(from_spectrum)))<2e-10
                if p < root-1e-8:
                    assert direct.min()>-2e-9
                if p > root+1e-8:
                    assert direct.min() < -1e-5
                count+=1
            if kind=='incidence' or q==2:
                assert abs((-2**root+(3**root-1)*math.sqrt(q)))<1e-10
            else:
                assert abs(q*(q+1)*2**root-q*q-(q+1)*3**root)<1e-10
                assert root<1/q<beta_spectral(q)
    print('PASSED',count,'distinct centered-spectrum numerical checks, projective plane orders 2,3,5,7')

if __name__=='__main__':run()
