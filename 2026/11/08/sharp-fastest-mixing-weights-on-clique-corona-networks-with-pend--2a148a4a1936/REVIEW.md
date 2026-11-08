# Scientific review

## Correctness — PASS
The full feasible set reduces by convex symmetry averaging to two edge weights, but global optimality is not inferred from symmetry alone: the transverse two-by-two block has an explicit positive Rayleigh vector whose quotient is a constant lower bound for every feasible invariant matrix. A feasible construction attains it. The remaining eigenvalues are bounded explicitly, including the potentially negative cluster-uniform mode when \(q\ge2\) and the \(q=1\) endpoint. The equality cases establish uniqueness only inside the invariant class. The attached symbolic and full-matrix verifier passed; no finite experiment is used as an infinite proof.

## Originality — PASS on inspected evidence
The 2004 FMMC paper gives the SDP and a four-vertex-path case, while the 2007 symmetry paper gives the group-averaging method and different exact examples. Both were checked in accessible full text and neither displayed the all-parameter \(K_m\circ\overline{K_q}\) formula, the fixed Rayleigh certificate, or the sharp ordering transition \(q=m-1\). Dedicated web and mathematical-record searches using graph aliases, spectral formulas, and consensus terminology found no stronger exact result covering the claim. This is a qualified best-knowledge originality judgment, not proof of absence from all literature. The published path case and generic symmetry method are explicitly credited.

## Mathematical value — PASS
The exact finite-dimensional graph-design problem is natural: dense core communication competes with degree-one pendant bottlenecks. The solution gives a globally sharp two-parameter spectral mixing rate, the unique invariant optimal design, mandatory zero core holding, a distinct core/leaf edge-weight transition, and fixed-parameter asymptotics. These are useful exact design facts rather than an unmotivated isolated computation.

## Closest literature and residual limits
Boyd–Diaconis–Xiao (2004), Boyd–Diaconis–Parrilo–Xiao (2007/2009), and Olesker-Taylor–Zanetti (2021/2024) are the most pertinent frameworks. The last was compared via its accessible abstract, not asserted to have been fully inspected. No specialist literature search guarantees uniqueness of the result; a future human literature audit may find earlier equivalent coverage. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
