# Independent mathematical audit

## correctness

PASS

Independent analytical reconstruction: reflect labels to reduce moments to the rare event with conditional probability (x−1+r)_+, whose first and second moments are r²/2 and r³/3. Thus v=r²/2−r⁴/4 and c=r³/3−r⁴/4, giving a=v−2c>0. The diagonal, incident and disjoint edge cases give Cov(Z)=aI+c BᵀB and hence the claimed polynomial in Q=BBᵀ. The positive square root of (aI+2cQ)² gives the inverse; the kernel is the space of vectors alternating on each component. At τ=2 absence is almost sure. For empirical PSD matrices with shifted roots A,B≥aI, solve A X+X B=4c(S−T) by the integral of e^(−sA)4c(S−T)e^(−sB), giving the stated 1/a Lipschitz bound for the inverse even without commutation. For h as in the proof the Hoeffding failure sum is 2(n²+n)e^(−2mh²)≤δ, the first-moment product error is ≤2Δ²h, and 3nΔ²h<a/2 follows from the strict bound. This verifies the all-graph theorem and finite-sample guarantee; the supplied finite script was inspected, not executed. Replay: RESULT.md lines 31–77 with these moment and Sylvester computations.

## originality

FAIL

An October 18 Resultary record already gives the exact threshold-one quadratic law, principal-root recovery, bipartite kernel and stable rounding from repeated degree-only observations via the same incidence and Sylvester steps. The all-interior-threshold coefficients and explicit probability bound are not literally supplied there. They are, however, a direct substitution of the new two scalar moments into the existing incidence inversion, with routine concentration; the purported central quadratic-reconstruction mechanism is covered. No claim of publication priority is made.

## value

FAIL

The already established degree-only inversion is mathematically useful. The distinct remainder is the elementary moment update under a threshold shift and a conservative sufficient sample count from entrywise Hoeffding plus the established square-root perturbation argument. The record gives no nonroutine new stability regime, sharp recovery rate, or unknown-threshold inference. There is no independently valuable surviving claim here to repair under the stated standard; this does not dispute the validity of the formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
