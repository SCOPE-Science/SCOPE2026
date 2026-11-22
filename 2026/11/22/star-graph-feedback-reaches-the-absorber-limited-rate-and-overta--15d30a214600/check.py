"""Finite matrix checks for the star-graph pair-absorption spectrum.

The formulas are proved analytically in RESULT.md.  These finite checks are
independent numerical diagnostics, not substitutes for an all-size proof.
"""
import math
import itertools
import numpy as np


def pair_generator(n, strength):
    """Equation K=-Delta_pair/2+strength*I_edge on K_{1,n-1}."""
    assert n >= 2 and strength > 0
    pairs=list(itertools.combinations(range(n),2))
    where={p:i for i,p in enumerate(pairs)}
    K=np.zeros((len(pairs),len(pairs)))
    edges=[(0,j) for j in range(1,n)]
    for p in pairs:
        a=where[p]
        if p in edges: K[a,a]+=strength
        for u,v in edges:
            for old,new in [(u,v),(v,u)]:
                if old in p and new not in p:
                    q=tuple(sorted(new if z==old else z for z in p))
                    b=where[q]
                    K[a,a]+=.5
                    K[a,b]-=.5
    assert np.max(abs(K-K.T)) < 1e-12
    return K


def predicted(n, strength):
    m=n-1
    if m==1: return [strength]
    A=strength+(m-1)/2
    disc0=math.sqrt((A-1)**2+2*(m-1))
    base=[(A+1-disc0)/2,(A+1+disc0)/2]
    if m==2:return sorted(base+[A])
    disc1=math.sqrt((A-1)**2+(m-2))
    base += [(A+1-disc1)/2]*(m-1)
    base += [(A+1+disc1)/2]*(m-1)
    base += [1]*(m*(m-3)//2)
    return sorted(base)


def star_gap(n, strength=1):
    m=n-1
    if m==1: return strength
    S=strength+n/2
    return 2*strength/(S+math.sqrt(S*S-4*strength))


def main():
    tests=0
    for n in range(2,17):
        for strength in (.1,.35,1.0):
            exact=np.linalg.eigvalsh(pair_generator(n,strength))
            expected=np.array(predicted(n,strength))
            assert len(exact)==len(expected), (n,strength)
            assert np.max(abs(exact-expected))<1e-10,(n,strength,np.max(abs(exact-expected)))
            assert abs(exact[0]-star_gap(n,strength))<1e-10,(n,strength)
            tests+=1
    for n in range(3,101):
        star=star_gap(n)
        cycle=2*(1-math.cos(math.pi/n))
        sign=(star>cycle+1e-10) - (star<cycle-1e-10)
        assert sign == (-1 if n<=5 else 0 if n==6 else 1),(n,star,cycle)
        assert star <= 2/n+1e-12
        tests+=1
    for n in (100,1000,10000):
        assert abs((n*star_gap(n))-2)<.05
        tests+=1
    print(f"PASS: {tests} numerical spectrum, comparison, and bound checks")
    print(f"n=6: gap={star_gap(6):.15f}; cycle={2*(1-math.cos(math.pi/6)):.15f}")
    print(f"n=7: gap={star_gap(7):.15f}; cycle={2*(1-math.cos(math.pi/7)):.15f}")

if __name__=='__main__':main()


def quantum_operator_check():
    """Independently compare Kraus adjoint action with pair-walk closure."""
    for n in (3,4,5):
        d=2**n
        eye=np.eye(d,dtype=complex)
        basis=np.arange(d)
        pairs=list(itertools.combinations(range(n),2))
        def sw(a,b):
            out=np.zeros((d,d),dtype=complex)
            for k in basis:
                ba=(k>>a)&1;bb=(k>>b)&1
                l=k if ba==bb else k ^ (1<<a) ^ (1<<b)
                out[l,k]=1
            return out
        pr={p:(eye-sw(*p))/2 for p in pairs}
        z0=np.diag([1 if ((k>>0)&1)==0 else -1 for k in basis])
        for strength in (.1,.5,1.):
            phi=math.asin(math.sqrt(strength))
            V=math.cos(phi)*eye + 1j*math.sin(phi)*z0
            events=[]
            for e in [(0,i) for i in range(1,n)]:
                p=pr[e]
                events.append((eye-p,V@p))
            K=pair_generator(n,strength)
            for i,p in enumerate(pairs):
                O=pr[p]
                lhs=np.zeros_like(O)
                for k0,k1 in events:
                    lhs += k0.conj().T @ O @ k0 + k1.conj().T @ O @ k1 - O
                rhs=-sum(K[i,j]*pr[q] for j,q in enumerate(pairs))
                err=np.max(abs(lhs-rhs))
                assert err<1e-10,(n,strength,p,err)
    print('PASS: direct Kraus-operator closure checks for n=3,4,5 and three feedback strengths')

if __name__=='__main__':
    quantum_operator_check()
