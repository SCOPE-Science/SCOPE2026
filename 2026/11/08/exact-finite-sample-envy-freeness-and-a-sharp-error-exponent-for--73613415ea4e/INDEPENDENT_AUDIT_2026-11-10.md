# Independent mathematical audit

## correctness

PASS

For a good, first-agent signed own-minus-other value Z has density 1+z on (−1,0) and z on (0,1). The two agents’ total signed gains sum to Σ|X_g−Y_g|>0 almost surely, so simultaneous envy is impossible and symmetry gives F_m=2P(ΣZ_g>0)−1. The MGF M(t)=((t−1)e^t+t+e^(−t))/t² (M(0)=1) is positive and strictly convex. Its m-th power expansion into e^{(r−u)t}/t^{2m−s−j} inverts by the bilateral Laplace formula, yielding exactly the displayed rational multinomial sum, with F1=0. Unique θ<0 with M′(θ)=0 exists by convexity; tilting at θ makes a compactly supported, nonlattice, bounded-density mean-zero law with variance σ²=M″(θ)/M(θ). Fourier local CLT plus a uniform O(m^−1/2) density bound justifies dominated convergence of the tilted half-line integral and the exact prefactor 2/(|θ|σ√2π). This is a proof of all m and the limit, independent of simulations.

## originality

PASS

Theorem 2 in Dickerson et al. 2014 proves eventual envy-freeness of a utilitarian-maximizing assignment under broad iid assumptions, explicitly including uniform draws, but does not give finite exact probabilities or the sharp one-sided large-deviation constant. Other inspected fair division work studies EF existence, groups, asymmetric samples or online welfare; no known exact formula covering the complete final claim was found.

## value

PASS

The exact finite-m welfare/fairness compatibility probability is a natural reliability statistic in canonical two-agent allocation. The analytic saddlepoint rate and exact prefactor quantify rare envy failure sharply, substantially strengthening qualitative high-probability results; the fixed two-agent uniform model is intrinsically motivated, not an arbitrary tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
