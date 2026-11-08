#!/usr/bin/env python3
"""Independent finite checks for the random shifted regular-crosspolytope section theorem.
Uses only the Python standard library. Checks never substitute for the proof.
"""
from itertools import combinations, product
from math import comb, erf, erfc, exp, sqrt, pi
from random import Random

rng = Random(20261104)

def polynomial_face_count(d, p, j):
    r=j+2
    all_faces=(2**r)*comb(d,r)
    positive=comb(p,r) if p>=r else 0
    negative=sum(comb(p,a)*comb(d-p,r-a)*(2**(r-a))
                 for a in range(max(0,r-(d-p)), min(r,p)+1))
    return all_faces-positive-negative

def actual_face_count(u, h, j):
    d=len(u)
    # Enumerate the actual faces: signed coordinate choices on r distinct axes.
    r=j+2
    count=0
    shift=h*u[-1]
    for axes in combinations(range(d),r):
        for signs in product((-1,1),repeat=r):
            signed_heights=[signs[t]*u[i]-shift for t,i in enumerate(axes)]
            if min(signed_heights)<0<max(signed_heights):count+=1
    return count

def frame_parameter(u,h):
    t=h*abs(u[-1]);return 1+sum(abs(v)>t for v in u[:-1])

def test_face_vectors():
    tests=0
    for d in range(3,9):
        for h in (0.02,0.23,0.63,0.997):
            for rep in range(21):
                u=[rng.gauss(0,1) for _ in range(d)]
                p=frame_parameter(u,h)
                for j in range(d-1):
                    actual=actual_face_count(u,h,j)
                    predicted=polynomial_face_count(d,p,j)
                    assert actual==predicted,(d,h,j,p,actual,predicted)
                    tests+=1
                assert polynomial_face_count(d,p,0)==p*(2*d-p-1)
    return tests

def check_limit_rank_symmetry():
    # At h=1, the number of the other absolute Gaussian coordinates
    # exceeding |G_d| is an exchangeable rank: each rank occurs equally.
    # Exhaustively enumerate all rank orders at small dimensions, no sampling.
    from itertools import permutations
    checks=0
    for d in range(3,8):
        counts=[0]*d
        for order in permutations(range(d)):
            # order is ascending list of coordinate indices
            rank=order.index(d-1)
            k=d-1-rank
            counts[k]+=1
        assert counts == [__import__('math').factorial(d-1)]*d
        checks+=d
    return checks

def check_boundary_probability():
    # Near h=1, exact rank law yields P(V=v_k) =1/d except top=2/d.
    for d in range(3,12):
        groups={}
        for k in range(d):
            val=(k+1)*(2*d-2-k)
            groups.setdefault(val,0)
            groups[val]+=1
        assert len(groups)==d-1 and sorted(groups.values())==[1]*(d-2)+[2]
    return 9

def check_gaussian_mixture():
    # Numerically integrate the conditional binomial formula, then compare
    # with an independently sampled direct Gaussian-normal construction.
    checks=0
    from math import factorial
    for d,h in ((4,0.6),(6,0.91)):
        a=0.0;b=11.0;nsteps=6000;delta=(b-a)/nsteps
        probs=[]
        for k in range(d):
            def integrand(t):
                q=erfc(h*t/sqrt(2))
                return sqrt(2/pi)*exp(-t*t/2)*comb(d-1,k)*(q**k)*((1-q)**(d-1-k))
            approx=(integrand(a)+integrand(b)+4*sum(integrand(a+(2*j+1)*delta) for j in range(nsteps//2))+2*sum(integrand(a+2*j*delta) for j in range(1,nsteps//2)))*delta/3
            probs.append(approx)
        assert abs(sum(probs)-1)<1.e-9
        counts=[0]*d
        nn=80000
        for _ in range(nn):
            values=[abs(rng.gauss(0,1)) for i in range(d)]
            k=sum(v>h*values[-1] for v in values[:-1])
            counts[k]+=1
        for k in range(d):
            assert abs(counts[k]/nn-probs[k])<0.013,(d,h,k,counts[k]/nn,probs[k])
            checks+=1
    return checks

def check_full_top_face_vector_tie():
    checks=0
    for d in range(3,14):
        for j in range(d-1):
            assert polynomial_face_count(d,d-1,j)==polynomial_face_count(d,d,j)
            checks+=1
    return checks

def main():
    checks=test_face_vectors()+check_limit_rank_symmetry()+check_boundary_probability()+check_gaussian_mixture()+check_full_top_face_vector_tie()
    print('PASS',checks,'supplementary tests; direct face enumeration, exact ranks, independent Gaussian mixture integration, numerical samples')

if __name__=='__main__': main()
