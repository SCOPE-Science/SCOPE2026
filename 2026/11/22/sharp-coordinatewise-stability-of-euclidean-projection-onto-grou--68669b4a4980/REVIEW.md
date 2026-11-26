# Independent mathematical audit

## correctness

PASS

The main formula is correct. The frozen Finding's unqualified singleton specialization 2−2/m is false for m=1: the interval projector is the identity locally and has Lipschitz coefficient 1. The corrected result gives the right exception and describes sorting as an available method, not a necessary computational step. On a strict exterior cell, clipping gives k_i t_i=∑_{j∈S_i} y_ij−λ and H=∑_{h active}1/k_h. A clipped row has positive in-group absolute sum 1−1/(k_iH) and negative cross-group absolute sum (r−1)/(k_iH) for r active groups. One active group gives zero clipped rows; identity and inactive rows have norms one and zero. The largest exterior row for r≥3 minimizes k_iH by k_i=1 and taking all coordinates clipped in the other r−1 active groups, which can be the largest groups. The cap-budget solution is affine in each strict sign and clipping cell; continuity extends the segment bound to arbitrary inputs. At chosen equal positive caps and λ>0, the extremal clip pattern satisfies strict inequalities. Perturbations of initially zero coordinates do not spoil the open affine neighborhood: those outputs are either zero by inactivity or unchanged by clipping. A signed finite perturbation attains the row norm, and interior pairs cover m≤2. Homogeneous sizes give a strictly increasing prefix function, with the stated value at m−1.

## originality

PASS

Prior work already solves the same mixed-norm Euclidean projection problem, and the numerical singleton-block coefficient is covered by known cross-polytope thresholding and centering formulas. The supported distinction is the exact global coordinate maximum-norm modulus for nontrivial general block-size patterns, its nonexpansivity boundary, and finite attaining pairs for the optimizing patterns. The result does not claim a new norm, new projector or a new singleton coefficient.

## value

PASS

Coordinatewise error is a natural sensitivity measure for a projection implemented by clipping individual coordinates. A sharp coefficient, a block-count nonexpansivity criterion, and an actual finite witness say more than Euclidean firm nonexpansivity. Unequal block sizes and the possibility of selecting a strict prefix matter, and the equal-size formula shows that block structure can substantially amplify coordinate errors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
