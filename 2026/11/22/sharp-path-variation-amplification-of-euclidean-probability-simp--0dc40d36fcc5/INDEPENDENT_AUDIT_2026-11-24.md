# Independent mathematical audit

## correctness

PASS

The threshold projection is invariant under common translation. Its active-set derivative J_F subtracts the active mean on F and vanishes elsewhere; each F occurs on a strict open cell. Segment integration gives the maximum of the local norms, and a one-jump step attains each local norm because the path-difference map identifies the quotient by constants with an l1 space. At a cut with a,b active positions on the two sides, the output is −b/(a+b) and a/(a+b) on those respective positions. The middle edge splits additively by sign. Appending a zero toward the cut on each side gives max transition count min(2a,2z+1) on a side with a ones and z zeros, attained by alternating runs. In the deficit formula, for a=b each side deficit is nonnegative and vanishes only for u,v in {−1,0}; this gives n=4a−2,4a−1,4a. If b>a and b≤3a, the minimum v-term is at v=−1 (possibly tied when b=3a) and the integer numerator of the deficit is at least d(2d−1) for d=b−a. Equality at one requires d=1,u=0,v=−1, hence n=2(a+b)−1; if b>3a the integer numerator is at least b²−ab+2a(a−1)>1. All larger numerators give a deficit at least 1/(a+b)>1/(n+1). The residue-specific selectors realize the claimed maxima, including n=2. Strict slack gives distinct arbitrarily close attaining inputs, and scalar clipping gives only the separate one-input variation bound. Positive mass scales out. Independent exact replay in branches/db9cfbef-f580-405f-ba1d-713faf127430/independent_check.py checked 851,867 active-support/cut cases through n=15, 72 boundary counts, and all integer maxima and strict witnesses through n=100. The universal result is analytical, not an extrapolation.

## originality

PASS

Pass for the all-dimensional closed evaluation with its mod-4 defect. The earlier connected-graph theorem already supplies an exact finite maximum and nearby-pair attainment for this very path, as well as the positive-mass and one-input statements. Those are not new here. What remained to evaluate was the path-specific constrained boundary maximum uniformly in dimension; the exact integer gap is not a mechanical graph substitution or finite re-tabulation.

## value

PASS

The exact closed expression makes the stability loss for ordered coordinates available without an exponential search over supports and cuts. It isolates an arithmetic obstruction with feasible attaining configurations and exposes strict pairwise expansion already at n=3 despite pointwise variation diminution. This value concerns the path evaluation, not the pre-existing general graph formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
