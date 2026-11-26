# Independent mathematical audit

## correctness

PASS

The frozen result is mathematically sound: for N≥2, the free maximum transform at s=1/2 contracts by 1−δ, the killed regeneration operator preserves the exponential supersolution, and nonexplosion permits the monotone infinite-cycle limit. From any positive start the reflection-killed heat kernel is strictly positive between positive points, so one surviving reset can reach a position with the bound strictly below one. A chosen particle can hit before the first alarm, so escape is never certain at finite positive parameters. The no-reset survival tail obtained by independence and reflection is of order t^(−N/2), with the mean criterion N>2; N=1 resetting is inert. As r decreases to zero, survival is bounded by the probability that the first alarm precedes the a.s. finite free hit; as r increases to infinity, the capture bound vanishes. For the repaired quantitative finding, the designated-particle first-cycle event also gives the lower bound e^(−y), y=x√(r/D). Independent Gaussian mean and difference give the conditional transform; integrating erfc by Tonelli and rationalizing yields 2/[2+s(√(2−s²)−s)] for every s∈(0,1). Thus the required contraction gap Δ(s)>0 holds on the entire interval and Δ(s)≥s(1−s)/3. The iteration works for each choice of s; choosing s=1−1/(y+2) gives the explicit 6eN(y+2)e^(−y) upper bound. Together these bounds force the sharp logarithmic rate; the proof never assumes independence of the maximum and the killing indicator within a cycle. Independent original transform quadratures agree (max absolute discrepancy below 7×10⁻¹⁴, replay `python3 /workspace/audit_checks/frozen_reconstruction.py`). The corrected package includes its own new bounded checker and `python3 /workspace/repairs/5/checker.py` passed six transform quadratures, sampled contraction bounds and rational prefactor checks. The proof, not the checker, certifies the logarithmic rate; no exact asymptotic prefactor is asserted.

## originality

PASS

This PASS is for the substantive quantitative repair only. The original headline claim of nonzero escape at every positive reset rate (and infinite unconditional mean there) fails independent originality assessment: it is a direct v=0 corollary of the distinct inward-drift threshold record under the exact same reset and killing rules. This is demonstrated coverage, not a claim about which same-day record appeared first or a mathematical error in the frozen theorem. The repair under /workspace/repairs/5 removes the qualitative assertion as a novelty claim and makes the sharp large-distance capture exponent and an explicit polynomial-prefactor upper bound the finding. The inspected threshold proof gives existence of a nonsharp exponential bound at some small positive trial exponent. That existence statement does not determine a sharp exponent. The repaired conclusion requires the full transform contraction interval and matching lower bound, neither furnished by that theorem or its inspected proof. The original half-rate explicit bound is retained as a corollary, not as a substitute novelty claim for the old finding.

## value

PASS

Unlike the already covered qualitative statement of positive escape, the repair determines how rare capture is as the starting distance increases, a natural observable of this first-hit problem. The explicit upper and lower bounds compare the infinite sequence of risky cycles to just one initial cycle: the latter sets the exact exponential scale and unlimited further cycles can change the probability by at most a linear distance factor in the proved envelope. This is a sharp rate, not merely a new arbitrary trial constant. It applies to every fixed N≥2 and all positive r,D without confinement, but does not identify a precise prefactor or simulate an infinite horizon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
