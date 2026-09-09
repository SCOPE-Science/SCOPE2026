"""Galois-orbit checks: O2 generic transitivity bound (in-lane computation).

O2 (BJST Lemma 5.20, dim pi(S)=1 case): orbit of translate P+H' under
Gal(K(lam)-bar/K(lam)) has cardinality >= N/(2[K:Q]).
We verify the NUMERICAL content actually used: N/(2[K:Q]) vs N^{1/12}
crossover, i.e. the orbit bound beats the PW exponent 1/12 for all N>=2
once [K:Q] is fixed (k=1: N/2 >= N^{1/12} iff N^{11/12}>=2, true for N>=3).
Also verify phi-flavoured transitivity count: # exact-order-N torsion
sections over generic base = psi(N) := N^2 prod_{p|N}(1-1/p^2)... we only
need existence of >= N conjugates; check N/(2d) >= 1 for N>=2d.
"""
import math

def check_O2_crossover(dmax=20, Nmax=5000):
    worst = None
    for d in range(1, dmax+1):
        for N in range(2, Nmax+1):
            if N/(2*d) < N**(1/12) and N > 4*d**2:
                worst = (d, N); break
    return {"no_counterexample_beyond_4d^2": worst is None, "witness": worst}

def check_O2_nontrivial(dmax=20, Nmax=200):
    bad = [(d,N) for d in range(1,dmax+1) for N in range(2,Nmax+1)
           if N >= 2*d and N/(2*d) < 1]
    return {"bad": bad[:5], "count": len(bad)}

if __name__ == "__main__":
    print(check_O2_crossover())
    print(check_O2_nontrivial())
    print("O1 (Gao Thm 5.11, theta=11/12): [K(P):K]>=c N^{11/12} quoted; "
          "11/12 > 1/12, comparison T0 from c1 T^{11/12} <= C0 T^{1/12}.")
    print("CM spot table (Heegner-Stark, context only):",
          {3:1, 4:1, 7:1, 43:1, 163:1, 15:2, 40:2})
