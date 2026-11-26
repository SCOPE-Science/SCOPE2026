# Independent mathematical audit

## correctness

PASS

Reflection splits the four-site Laplacian into blocks [[1,−1],[−1,1]] and [[1,−1],[−1,3]]. The endpoint projector entries are 1/4, −q/4, 1/4, −p/4 in eigenvalue order 0,a,2,c, verifying the four-exponential formula. Ordinary heat is strictly positive by connectivity, and the positive stable subordination measure gives strict positivity for 0<α<1. As a function of α, (L^α)_{14}=(2^α−qa^α−pc^α)/4 has exactly the two simple zeros 1 and 2 by the three-exponential Rolle bound and the identities qa=pc=1 and qa²+pc²=4. It is negative for α>2 (the c^α term dominates), hence positive between the zeros. At 2 the first time derivative vanishes and (L^4)_{14}=−6 gives negative quadratic onset. The four-exponential Rolle bound in time leaves at most two positive zeros counting multiplicity after the origin, or one at α=2. For 1<α<2 the opposite initial and final signs require an odd total crossing multiplicity and leave only one simple root. Above 2 the negative witness t=2^(−α) follows from q exp(−(a/2)^α)≥1/2+3√2/4>1+exp(−1), forcing two simple positive zeros between initial and final positivity. In the Taylor expansions at (1,0) and (2,0), ∂_α(L^α)_{14} is log(2)/4 and [4log(2)−a log(a)−c log(c)]/4 respectively; the latter is strictly negative by convexity of x log x. Since (L^3)_{14}=−1, the sign brackets at t=u√(α−1) or t=u(α−2) give the two stated constants. Section 5 of python /workspace/review_reproduction.py independently checks the parity blocks and normalized roots on two small parameter offsets. These are corroboration only; neither the proof nor the diagnostics classify matrix-wide positivity or arbitrary paths.

## originality

FAIL

A distinct indexed four-path result already contains the complete endpoint sign classification, including precisely the two-crossing regime and the exponent-two transition, in a stronger all-entry theorem. A second distinct record explicitly gives the first onset for this same endpoint. The remaining exponent-two slope is a direct implicit derivative of the first comparator's displayed function and nonzero quadratic term. The shared UTC date does not settle historical priority; the failure is demonstrated coverage or direct implication, not a priority allegation.

## value

FAIL

The endpoint is a natural probe, and the reentrant phase portrait is scientifically meaningful. But that portrait and its first onset are already covered in the inspected results. The remaining linear slope adds only an implicit differentiation to known, explicit Taylor data for the same endpoint. It does not constitute a distinct nonmechanical exact invariant worth a narrowed repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
