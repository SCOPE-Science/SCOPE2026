# Independent mathematical audit

## correctness

PASS

In the stated Gaussian normalization, angular orthogonality makes the Toeplitz operator diagonal on monomials, and polar integration gives the Gamma(k+d,1) expectation with multiplicity binomial(k+d−1,d−1). The derivative bound with c=β−η√(β²+ω²)>0 and the one-exponential coupling prove strict ordering. On [k/2,3k/2], the signed first Taylor moment is d and the second moment about k is k+d+d²; outside, gamma Chernoff bounds and Cauchy–Schwarz give exponentially small relevant tail terms. This proves λ_k=a0(k)+O(k^(−β−1)) and compactness. The derivative lower bound permits a fixed index shift in either direction, so the last degree with eigenvalue strictly above t is r(t)+O(1), including at threshold equality. Inverting the strictly decreasing scalar symbol yields r=t^(−1/β)H−1. For H the upper endpoint occurs at phase −ω log((1+η)^(1/β)); the lower occurs at π−ω log((1−η)^(1/β)); the range follows by continuity (these phase formulas resolve the endpoint order in the proof). Summing multiplicities gives the counting law, and at a jump the two one-sided errors of any continuous approximant cannot both be smaller than half the multiplicity; t^(−(d−1)/β) is comparable to that multiplicity. This covers d=1, where jumps have size one. From eigenvalues and multiplicities one gets the stated strong/weak Schatten cutoff. At q=d/β, the leading summand m_k λ_k^q is (1+η cos(ω log k))^q/((d−1)!k) with summable O(k^(−2)) error; the derivative of the smooth leading summand is O(k^(−2)), so a sum–integral comparison followed by translation-period averaging gives the critical logarithmic mean. The rank through degree K grows like K^d/d!, and a partial next block contributes O(K^(−1)); the factor 1/d therefore applies to the ordinary log-mean over every rank, proving the stated value for normalized Dixmier traces. Replay: python3 /workspace/branches/frozen_math_reproductions.py 3 (SciPy). Centered-variable quadrature, an independent inversion in the phase variable, and strict-threshold counts for three admissible tuples in d=1,2,4 agree with the bounds (largest sampled scaled count error <1.88); this does not test all dimensions or calculate the Dixmier limit numerically. The uploaded checker was inspected, not run.

## originality

PASS

There are substantial prior analogues for individual parts, including the joint oscillating Weyl coefficient and measurable trace in a Bergman example. The distinct supported result is their explicit realization for this fixed standard Gaussian Fock Toeplitz family in every complex dimension, with an exact profile and multiplicity-optimal remainder. Radial diagonalization itself, failure of a scalar Weyl coefficient in general, and the abstract period-averaging mechanism are not assigned independent novelty.

## value

PASS

This symbol family separates two spectral properties in a fixed canonical space: the normalized counting function fills a nontrivial explicit interval while the critical normalized singular-value mean still converges. The optimal error against continuous counts uses the dimension-dependent jump size rather than just a coarse leading term. The all-dimensional relation among modulation, exact profile, and trace is useful beyond a one-off counterexample; no necessity of the amplitude constraint or arbitrary nonradial extension is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
