# Mathematical audit — 2026-10-01

## Final claim

K2P single-triangle four-leaf network has dimension at least 13

## Correctness — PASS

PASS. The corrected K2P Fourier parameterization was reconstructed independently with the root-edge exponent rc=g4. At the stated rational point, the full Jacobian has rank 13 and the specified 13 by 13 minor is exactly 160576479/4194304, so the network variety has dimension at least 13. The displayed-tree exponent matrix has rank 10. Thus the admitted target value 7 is indeed false.

## Originality — FAIL

FAIL. A stronger dimension statement is already mechanically implied by Gross-Krone-Martin. Their 2024 Table 1 reports deficiency 1 for the K2P 3-sunlet; with three K2P orbit classes this gives affine dimension 10. Their general cut-edge toric-fiber-product formula then glues that 3-sunlet to the 3-claw forming the four-leaf single-triangle skeleton, giving dimension 10+7-3=14. Hence the audited lower bound 13 and the disproof of dimension 7 are strict corollaries of published results.

## Scientific value — PASS

PASS. Dimensions of K2P models on triangle networks are directly relevant to phylogenetic identifiability, so an exact or certified dimension result on this natural quarnet would be worthwhile if not already implied. The rejection is solely originality: prior work gives the stronger exact dimension 14.

## Sources inspected

- E. Gross, R. Krone, S. Martin, Dimensions of Level-1 Group-Based Phylogenetic Networks — https://doi.org/10.1007/s11538-024-01314-z: STRONGER_PRIOR_COVERAGE. Primary full text: toric-fiber-product dimension formula, K2P model definition, and Table 1 showing deficiency 1 for the n=3 K2P sunlet.
- S. Cox, E. Gross, S. Martin, Group-based phylogenetic models on 3-sunlet networks — https://doi.org/10.1007/s11538-025-01506-1: CONTEXT_AND_MODEL_NORMALIZATION. Primary full text on 3-sunlet dimensions and explicit discussion that K2P is a nontrivial automorphism-orbit model distinct from the general V4/K3P model.

## Residual risks

- The committed certificate proves only a lower bound 13, while prior theory gives the stronger exact value 14 for the same contracted single-triangle skeleton.
- Scientific rejection is not a correctness failure; the numerical certificate remains valid evidence.

## Disposition

**failed**
