# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Log-overlap sharpness for the BMV cubic saddle via triple flat-rectangle necessity and null-ruling packet cluster
- **Round:** 2026-09-07-first-light-01
- **Lane:** 618
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Harmonic Analysis
- **Method:** polynomial partitioning with Guth-Katz incidence bounds and bilinear-to-linear restriction induction, via null-frame flatness classification and wave-packet extremal witness

## Problem

Let phi_BMV be the Buschenhenke-Muller-Vargas cubic perturbation phase in R^3 with extension operator E_BMV and l2 decoupling constant D(delta) over (phi,A delta)-flat rectangles in the sense of Guth-Maldague-Oh. Prove overlap/log-loss is necessary at this named cell: exhibit a null-ruling wave-packet cluster forcing D(delta_j) >= c log(delta_j^{-1})^{1/2} along a sequence delta_j -> 0, via an explicit triple of overlapping maximal flat rectangles through one frequency point with a computed energy ratio. This is the lower-bound (extremal-witness) branch of the lane, not an upper-bound epsilon-removal.

## Attempted claim

Let phi_BMV, E_BMV, and D(delta) be as above with GMO (phi,A delta)-flat rectangles. There exist an absolute c > 0 and a sequence delta_j -> 0 with N_j ~ j explicitly overlapping maximal flat rectangles through one frequency point, and explicit null-ruling wave-packet clusters f_j with one packet per rectangle, such that D(delta_j) >= ||E_BMV f_j||_{L^4} / (sum_S ||E_BMV f_{j,S}||_{L^4}^2)^{1/2} >= c log(delta_j^{-1})^{1/2}, proving the GMO logarithmic overlap and epsilon-loss are qualitatively necessary at the BMV cell; the j=3 instance is the fallback triple with ratio >= sqrt(3/2).

## Research outcome

Proved a committed-scale BMV triple overlap-necessity witness (three (phi,0.01)-flat rectangles through (1/2,1/2) with sympy-exact junction/maximality ledger and 3-packet L^4 ratio sqrt(3) >= sqrt(3/2)) plus quantitative no-go obstructions blocking both the full log-growth target extension and the literal c3^2-scale fallback (fan rigidity, large-ball washout curve, literal-scale infeasibility).

## Why this attempt failed

Failed axes: correctness, value.

correctness: Replayed verify_triple.py exit 0: S1 UB 0.00702, S2 UB 0.00669, S3 UB 0.00947 <=0.01 confirmed (S2 cancellation dx+0.5dy=sqrt(5)/2 dB verified analytically; random-pair search sups 0.0065/0.0024/0.0090 consistent). Junction witness pairs sympy-exact 0.044960/0.012223/0.010849 >0.01 confirmed. Small-ball grid ratio 1.7320 on B_0.05/B_0.02 confirmed. BUT three essential inferences fail: (1) Overlap>=3 forcing is false as stated. Pi tail packets are pairwise disjoint, each Pi subset Si hence (phi,0.01)-flat, so {P1,P2,P3} is itself a disjoint flat cover of P1uP2uP3 with overlap 1. Junction pairs (e.g. (0,0.5) and wpt(-0.10,0)) lie outside Pi, so they prove Si-unions non-flat, not that Pi cannot be disjointly covered. Any union of crossing strips can be partitioned into small flat squares with overlap 1. (2) Ratio scale mismatch: decoupling constant D(delta) requires ball radius delta^-1=200 for delta=0.005; ratio proved only at r<=0.05 where ANY 3 disjoint packets give sqrt(3) by coherence (trivial, mechanically implied). At required scale the report's own MC shows decay to 0.9765<sqrt(3/2). So no decoupling lower bound proved. (3) Fan-rigidity logic fallacy: Sec6a infers non-flatness from general-pair UPPER bound exceeding budget (0.016-0.039>0.01); UB>budget proves nothing (S2 itself has loose UB 0.0393 yet is flat, per T1rot off=0 row). Only endpair lower bounds count, and they pass (flat) for off 0-15deg. Hence 'no transverse fan exists' not proved. (4) Maximality overclaimed: only listed dilations checked, not all; 'maximal' unproved. Large-ball 'washout proof' is seed-7 Monte Carlo (n=60000 in huge oscillatory ball), i.e. experimental evidence, not proof, yet presented as killing TARGET leg. Honest limitations are stated but headline inferences still asserted. value: EMERGENT_FINDING judged under ordinary full value standard with no presumption. Strongest headline (committed-scale triple + sqrt(3) on B_0.05) is not independently worth retrieving: (a) Scale delta*=0.005, A0=2, H=0.007, a=0.10/b=0.004 etc. are arbitrary committed numbers, admitted NOT the literature-pinned c3^2=1/9, GMO A0, theta0=33.08deg, B_9 (S1-S3 separation 14.04deg<33.08deg). (b) Flatness of three sufficiently small crossing strips through a point follows from continuity (D=dx dy+uy dy^2+dy^3/3 ->0 as diameter->0); the tight UBs are replayable arithmetic, not a new obstruction. (c) Ratio sqrt(3) on B<=0.05 is mechanically implied for any N=3 disjoint packets on a sufficiently small ball (coherence), not a decoupling gain; the decoupling-scale ratio fails by the report's own washout curve. (d) Negative companions (rigidity/washout/literal-no-go) are failure logs from fallacious UB reasoning and seed-7 MC, not citable obstructions; they close off only the authors' own shape family/route, explicitly 'not for all shapes/f'. Hence textbook continuity + trivial small-ball coherence + arbitrary-scope enumeration + unexplained numbers, even though correct at committe…

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: ['Committed scale delta_star=0.005, A0=2 differ from literal fallback pins delta=c3^2=1/9, GMO A0, theta0=33.08deg, B_9: S1-S3 separation is 14.04deg < 33.08deg; literal criterion provably unsatisfiable for this shape family but not for all conceivable shapes.', 'Ratio proved only on committed small balls B<=0.05; large-ball transfer disproved for this packet family (washout through threshold), not universally.', 'Full TARGET log lower bound neither proved nor disproved in general; only the nul…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
