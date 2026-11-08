"""Finite exact checks for complete trapping on anisotropic circular ladders.
Only integer arithmetic is used for dynamical rank; trigonometric evaluation
chooses the spectral-branch collisions, not the dynamical rank.
"""
from fractions import Fraction
from math import cos, pi, gcd, prod
from itertools import combinations
import numpy as np

P=1_000_003

def phi(n):
    return sum(gcd(n,x)==1 for x in range(1,n+1))

def theoretical(n,r):
    c=[cos(2*pi*j/n) for j in range(n//2+1)]
    m=[1 if j==0 or (n%2==0 and j==n//2) else 2 for j in range(n//2+1)]
    counts=[m[j]+m[l] for j in range(len(c)) for l in range(j+1,len(c)) if abs(c[j]-c[l]-float(r))<1e-9]
    return max([2]+counts)

def adjacency(n,ratio):
    K=ratio.numerator;J=ratio.denominator
    size=2*n
    # Sparse adjacency update list; index=2*angle+layer.
    return [[(2*((a-1)%n)+b,J), (2*((a+1)%n)+b,J), (2*a+1-b,K)] for a in range(n) for b in range(2)]

def rank_mod(matrix,p=P):
    piv={}
    for vec in matrix:
        v=[e%p for e in vec]
        for j in sorted(piv):
            b=piv[j]
            factor=v[j]
            if factor:
                for t in range(j,len(v)):
                    v[t]=(v[t]-factor*b[t])%p
        j=next((j for j,w in enumerate(v) if w),None)
        if j is None: continue
        mult=pow(v[j],-1,p)
        piv[j]=[(w*mult)%p for w in v]
    return len(piv)

def observability_rank(n,ratio,traps):
    # [P,PA,...,PA^{2n-1}], using transpose Krylov columns A^j e_t.
    N=2*n
    adj=adjacency(n,ratio)
    cols=[]
    for t in traps:
        v=[int(i==t) for i in range(N)]
        for _ in range(N):
            cols.append(v)
            w=[0]*N
            for i,edges in enumerate(adj):
                for k,weight in edges:
                    w[i]+=weight*v[k]
            v=[x%P for x in w]
    return rank_mod(cols)

def traps_witness(k):
    if k==2: return (0,2)
    if k==3: return (0,2,1)
    if k==4: return (0,2,1,3)
    raise ValueError(k)

def spectral_rank_all(n, ratio, traps):
    # Analytically known real Fourier basis, compared independently with row restriction.
    N=2*n
    vectors=[]
    energies=[]
    for j in range(n//2+1):
        x=np.arange(n)
        basis=[np.cos(2*np.pi*j*x/n)]
        if j!=0 and not (n%2==0 and j==n//2):
            basis.append(np.sin(2*np.pi*j*x/n))
        for sign in (1,-1):
            for mode in basis:
                vectors.append(np.stack([mode, sign*mode],axis=1).reshape(N))
                energies.append(2*np.cos(2*np.pi*j/n)+sign*ratio)
    groups=[]
    for a,e in enumerate(energies):
        for g in groups:
            if abs(energies[g[0]]-e)<1e-8:
                g.append(a);break
        else: groups.append([a])
    arr=np.array(vectors)
    for group in groups:
        M=arr[group,:][:,traps].T
        if np.linalg.matrix_rank(M,tol=1e-7)!=len(group):return False
    return True

def main():
    checked=0
    sample=[Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(7,5),Fraction(11,7),Fraction(5,4),Fraction(4,3)]
    found={2:0,3:0,4:0}
    for n in range(3,19):
        for ratio in sample:
            k=theoretical(n,ratio)
            observed=observability_rank(n,ratio,traps_witness(k))
            assert observed==2*n,(n,ratio,k,observed)
            found[k]+=1
            checked+=1
            # All proper prefix-trap sets of the 4-witness fail when they have fewer than max multiplicity.
            if k>2:
                insufficient=traps_witness(k)[:-1]
                assert observability_rank(n,ratio,insufficient)<2*n,(n,ratio,k)
                checked+=1
    generic=Fraction(11,7)
    pair_checks=0
    for n in range(3,13):
        if theoretical(n,generic)!=2: continue
        count=0
        for i,j in combinations(range(2*n),2):
            full=observability_rank(n,generic,[i,j])==2*n
            angular=(j//2-i//2)%n
            expected=gcd(n//gcd(n,2),angular)==1
            assert full==expected,(n,i,j,full,expected)
            count+=full;pair_checks+=1
        expected_total=2*n*gcd(n,2)*phi(n//gcd(n,2))
        assert count==expected_total,(n,count,expected_total)
    spectral_checks=0
    spectral_counts={2:0,3:0,4:0}
    for n in range(3,29):
        c=[cos(2*pi*j/n) for j in range(n//2+1)]
        samples=[float(Fraction(11,7))]
        samples += [c[j]-c[l] for j in range(len(c)) for l in range(j+1,len(c))]
        for ratio in samples:
            k=theoretical(n,ratio)
            assert spectral_rank_all(n,ratio,traps_witness(k)),(n,ratio,k)
            if k>2:assert not spectral_rank_all(n,ratio,traps_witness(k)[:-1]),(n,ratio,k)
            spectral_counts[k]+=1;spectral_checks+=1
    print('VERIFY_OK',{'rank_witness_and_lower':checked,'generic_pairs':pair_checks,'spectral_resonance_cases':spectral_checks,'categories':found,'spectral_types':spectral_counts})

if __name__=='__main__': main()
