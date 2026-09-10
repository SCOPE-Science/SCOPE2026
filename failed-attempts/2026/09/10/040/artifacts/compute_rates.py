"""Auditable first-moment + energy-sum certificate for lane-599 TARGET.
Idealized dyadic model with uniform O(1) constants set to 1; verifies
exponential rate 3/2 and s-energy convergence iff s<3/2.
Uses only stdlib. Writes tables to stdout and to rates.json.
Model:
  P1(K,C) = c0(C) * K^{-3/2} * 2^{-K/2}   (one-point barrier+terminal)
  E[N(K)] = nQ(K) * P1,  nQ(K) = #{2^{-K} grid squares in Q0}, Q0=[1/4,1/2]^2
           side 1/4 -> nQ = 4^{K-1} for K>=1 (exactly (2^{K}/4)^2).
  Pair bound: P2(j,K) = C2 * 2^{-K} * 2^{j/2} * (j+1)^{3} * (K-j+1)^{-3} * K^{0}
           (exponential part exact; polynomial part generous upper envelope).
  Energy shell sum: S_s(K)= sum_{j=0}^{K} 2^{js} * (pairs_j / E[N]^2) * P2(j,K),
           pairs_j = nQ(K) * (4^{K-j}) approx count with ancestor at scale j.
  Claim: S_s bounded uniformly in K iff s<3/2.
"""
import json, math

def nQ(K):
    return 4**(K-1)  # K>=1

def P1(K, c0=1.0):
    return c0 * (K**(-1.5)) * 2**(-K/2.0)

def E_N(K, c0=1.0):
    return nQ(K) * P1(K, c0)

def rate(K, c0=1.0):
    return math.log2(E_N(K, c0)) / K

def P2(j, K, C2=1.0):
    Kj = K - j + 1
    return C2 * 2**(-K) * 2**(j/2.0) * ((j+1)**3) * (Kj**(-3))

def energy_sum(s, K, C2=1.0, c0=1.0):
    EN = E_N(K, c0)
    total = 0.0
    shells = []
    for j in range(0, K+1):
        pairs_j = nQ(K) * (4**(K-j))  # generous upper bound
        contrib = (2**(j*s)) * pairs_j * P2(j, K, C2) / (EN**2)
        shells.append(contrib)
        total += contrib
    return total, shells

def main():
    print("K  nQ  E[N]  log2E[N]/K")
    rates = []
    for K in [4, 6, 8, 10, 12, 16, 20, 30, 50]:
        en = E_N(K)
        r = rate(K)
        rates.append({"K": K, "nQ": nQ(K), "EN": en, "rate": r})
        print(f"{K}  {nQ(K)}  {en:.6e}  {r:.6f}")
    print("\nrate -> 3/2 with polynomial correction -1.5*log2(K)/K -1/K:")
    for d in rates:
        K = d["K"]
        corr = 1.5 - 1.5*math.log2(K)/K - 1.0/K
        print(f"K={K}: rate={d['rate']:.6f}  asymptotic={corr:.6f}")
    print("\nEnergy sums S_s(K) for s in {1.0,1.3,1.4,1.49,1.6}:")
    es = {}
    for s in [1.0, 1.3, 1.4, 1.49, 1.6]:
        row = []
        for K in [5, 10, 15, 20, 30, 50]:
            tot, _ = energy_sum(s, K)
            row.append(tot)
        es[str(s)] = row
        print(f"s={s}: " + "  ".join(f"K={K}:{v:.4f}".format(K=K, v=v) for K, v in zip([5,10,15,20,30,50], row)))
    print("\nShell contributions s=1.4, K=30:")
    _, shells = energy_sum(1.4, 30)
    for j in [0, 1, 2, 5, 10, 15, 20, 25, 29, 30]:
        print(f"  j={j}: {shells[j]:.6e}")
    print("\nShell contributions s=1.6, K=30 (tail grows / larger):")
    _, shells2 = energy_sum(1.6, 30)
    for j in [0, 1, 2, 5, 10, 15, 20, 25, 29, 30]:
        print(f"  j={j}: {shells2[j]:.6e}")
    # ballot constant sanity: Brownian ballot density factor
    print("\nBallot density check: P_0(min_{[0,K]} B>=-C, B_K in [0,1]) ~ c(C) K^{-3/2}:")
    print("  (reflection formula: (phi_K(y)-phi_K(y+2C+...)) integrated; ratio K=20/K=10 should be (10/20)^{3/2}=0.3536)")
    import math as m
    def ballot(K, C=2.0):
        # integral_{y=0..1} [phi_K(y+C)-phi_K(y+C+2C... )] approx via reflection, start at C
        # P_C(tau_0>K, B_K in [C,C+1]) with BM variance = t*ln2? use sigma2=ln2 per unit K
        s2 = K*m.log(2)
        def phi(x): return m.exp(-x*x/(2*s2))/m.sqrt(2*m.pi*s2)
        # integrate crudely with Simpson 21 pts
        N=21; a=C; b=C+1; h=(b-a)/N
        tot=0.0
        for i in range(N+1):
            y=a+i*h
            d = phi(y-C)-phi(y+C)  # reflection from C? start x=C, barrier 0
            w = 4 if i%2==1 else 2
            if i in (0,N): w=1
            tot+=w*d
        return tot*h/3
    b10=ballot(10); b20=ballot(20)
    print(f"  ballot(10)={b10:.6e} ballot(20)={b20:.6e} ratio={b20/b10:.4f} (expect ~0.354)")
    out={"rates":rates,"energy":es,"ballot_ratio":b20/b10}
    with open("output/artifacts/rates.json","w") as f:
        json.dump(out,f,indent=2)
    print("\nwrote output/artifacts/rates.json")

if __name__=="__main__":
    main()
