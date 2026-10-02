#!/usr/bin/env python3
"""Exact finite checks for the coloring-channel/trace-monoid correspondence.

Only Python standard library is used.  The script:
  * builds the signed independence polynomial mu_P(z)=I_P(-z),
  * derives trace counts from 1/mu_P(z),
  * independently enumerates coloring-channel outputs for small n,
  * verifies several nontrivial channel families and cycles,
  * checks the closed-form cycle growth constant.
"""
from itertools import product, combinations
from math import cos, pi, log, sqrt


def pairs_graph(q, channels):
    edges=set()
    for ch in channels:
        ch=sorted(ch)
        for a,b in combinations(ch,2):
            edges.add((a,b))
    return edges


def signed_independence_coeffs(q, edges):
    # coeff[k] = (-1)^k * (# independent sets of size k in the pairs graph)
    coeff=[0]*(q+1)
    for mask in range(1<<q):
        verts=[v for v in range(q) if mask>>v & 1]
        independent=all((min(a,b),max(a,b)) not in edges for a,b in combinations(verts,2))
        if independent:
            k=len(verts)
            coeff[k]+=(-1)**k
    while len(coeff)>1 and coeff[-1]==0:
        coeff.pop()
    return coeff


def trace_counts(mu, N):
    # If G(z)=sum a_n z^n=1/mu(z), then convolution mu*a = 1.
    a=[0]*(N+1)
    a[0]=1
    for n in range(1,N+1):
        a[n]=-sum(mu[k]*a[n-k] for k in range(1,min(n,len(mu)-1)+1))
    return a


def output_count(q, channels, n):
    outs=set()
    for w in product(range(q), repeat=n):
        tup=tuple(tuple(x for x in w if x in ch) for ch in channels)
        outs.add(tup)
    return len(outs)


def check_family(name,q,channels,N=5):
    used=set().union(*map(set,channels)) if channels else set()
    assert len(used)==q, f"{name}: exact finite trace equality here assumes all letters used"
    edges=pairs_graph(q,channels)
    mu=signed_independence_coeffs(q,edges)
    a=trace_counts(mu,N)
    observed=[output_count(q,channels,n) for n in range(N+1)]
    assert observed==a, (name,mu,observed,a)
    print(f"{name}: mu={mu}; counts={a}")


def cycle_channels(t):
    return [{i,(i+1)%t} for i in range(t)]


def eval_poly(coeff,z):
    return sum(c*(z**i) for i,c in enumerate(coeff))



def check_unused_letter_example():
    # C4 on visible symbols 0,1,2,3, with symbol 4 completely unused.
    # A length-n input can hide any number of 4s, so distinct outputs are the
    # union of visible trace sets of lengths 0..n.
    q=5
    channels=cycle_channels(4)
    full_mu=signed_independence_coeffs(q,pairs_graph(q,channels))
    visible_mu=signed_independence_coeffs(4,pairs_graph(4,channels))
    visible=trace_counts(visible_mu,4)
    expected=[]
    total=0
    for x in visible:
        total+=x
        expected.append(total)
    observed=[output_count(q,channels,n) for n in range(5)]
    assert observed==expected, (observed,expected)
    # The unused vertex is isolated in the pairs graph, hence contributes (1-z).
    assert full_mu==[1,-5,6,-2], full_mu
    print(f"C4 + one unused symbol: mu_full={full_mu}; counts={observed}")


def main():
    check_family("C4",4,cycle_channels(4),N=6)
    check_family("overlapping triples",4,[{0,1,2},{0,2,3}],N=5)
    check_family("disjoint pair channels",4,[{0,1},{2,3}],N=5)
    check_family("mixed singleton/pair",4,[{0},{1},{2,3}],N=5)
    check_unused_letter_example()

    print("\nCycles:")
    for t in range(3,8):
        edges=pairs_graph(t,cycle_channels(t))
        mu=signed_independence_coeffs(t,edges)
        r=1/(4*cos(pi/(2*t))**2)
        lam=1/r
        residual=eval_poly(mu,r)
        counts=trace_counts(mu,5)
        observed=[output_count(t,cycle_channels(t),n) for n in range(6)]
        assert observed==counts
        assert abs(residual)<1e-10, (t,mu,r,residual)
        print(f"C_{t}: mu={mu}; lambda={lam:.12f}; counts={counts}")

    lam4=2+sqrt(2)
    cap4=log(lam4,4)
    assert abs(lam4-(4*cos(pi/8)**2))<1e-12
    print(f"\nC4 exact growth constant = 2+sqrt(2) = {lam4:.12f}")
    print(f"C4 base-4 capacity = log_4(2+sqrt(2)) = {cap4:.12f}")

if __name__=="__main__":
    main()
