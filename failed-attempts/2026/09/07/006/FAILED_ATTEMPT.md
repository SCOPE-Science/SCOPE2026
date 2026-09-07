# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Closing or tightening A(16,6,7) in [109,122] via branch-and-bound with Delsarte LP certificates and canonical isomorph rejection
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1
- **Disposition:** NO_RESULT
- **Domain:** Combinatorics
- **Method:** branch-and-bound integer programming with isomorph rejection

## Problem

Determine the exact value of A(16,6,7), the maximum size of a binary code of length n=16, constant weight w=7 and minimum Hamming distance d=6 (intersection <=4). Current Brouwer-type sandwich is 109 <= A(16,6,7) <= 122 over universe C(16,7)=11440. Within a 2-hour bounded search, run branch-and-bound integer programming (maximum independent set on Johnson conflict graph where x_i+x_j<=1 if |supp(i) cap supp(j)|>=5) with Delsarte LP (Johnson-scheme Krawtchouk LP) upper-bound pruning at each node and canonical augmentation / isomorph rejection under S_16 (fix c1=0b1111111000000000, branch c2 by intersection type t=0..4). Success is an exact value with explicit optimal code and machine-checkable optimality certificate; predefined fallback is a tightened sandwich by >=1 on either side with rerunnable certificate.

## Attempted claim

Determine exact A(16,6,7) in [109,122] by exhaustive branch-and-bound with Delsarte LP pruning and canonical isomorph rejection; primary hypothesis to test is optimality of the Golay-derived 109-code, i.e. prove A(16,6,7)=109, or otherwise exhibit the true optimum (e.g. 110-122) with explicit optimal code list (16-bit vectors weight 7, pairwise distance >=6) and a complete optimality certificate (branch tree + per-node LP/Johnson bounds covering all S_16 orbits).

## Research outcome

No tightening of 109<=A(16,6,7)<=122 achieved in 2h. Johnson 122 recomputed exactly conditional on cited A(15,6,7)=69; plain Delsarte LP rigorously proved to be 3146/5=629.2 (dual certificate, hence useless vs Johnson); Golay G24 construction verified (weight distribution, distance 8) but naive puncture/shorten fails to recover 109; best new explicit code has size 77 (verified 2926 pairs), below known 109; parallel ARW stalls at 75-77 with pool analysis explaining hardness. Upper <=121 and lower >=110 both remain open in this lane.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['Upper bound unchanged at 122: plain Delsarte LP optimum proved 629.2 (far weaker than Johnson), so per-node Delsarte pruning cannot beat Johnson; SDP (Schrijver/Polak) not implemented in 2h pure-Python budget; depth-bounded branch-and-bound would cover negligible fraction of the 5 c2 orbits (10620 compatible nodes) and was not pursued to a certificate.', 'Lower bound not improved: best explicit code has size 77 (2926 pairs verified), below known 109; hence no Brouwer-table tightening on either side. 110-code not found; 109-code not reproduced from scratch (naive Golay puncture/shorten yields only 33-45 greedy subsets within 704-pools).', 'A(15,6,7)=69 used as cited exact input for Johnson 122 (Ostergard 2010); not re-derived. No originality claim on 109-122 interval itself.', 'Heuristic search is stochastic (ARW tabu, fixed seeds) and plateaued at 75-77 across 8 seeds x80k iterations; LNS pool analysis shows small-k neighborhoods (k<=10) contain 0-1 extra vertices beyond removed set, explaining stall. Larger-k exact LNS and SDP remain future work requiring C implementation and longer budget.', 'No exhaustive optimality certificate; no DRAFT.md per NO_RESULT spec.']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['Upper bound unchanged at 122: plain Delsarte LP optimum proved 629.2 (far weaker than Johnson), so per-node Delsarte pruning cannot beat Johnson; SDP (Schrijver/Polak) not implemented in 2h pure-Python budget; depth-bounded branch-and-bound would cover negligible fraction of the 5 c2 orbits (10620 compatible nodes) and was not pursued to a certificate.', 'Lower bound not improved: best explicit code has size 77 (2926 pairs verified), below known 109; hence no Brouwer-table tightening on eithe…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
