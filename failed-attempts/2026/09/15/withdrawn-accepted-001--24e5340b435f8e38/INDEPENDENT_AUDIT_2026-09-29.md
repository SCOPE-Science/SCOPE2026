# Independent audit — 2026/09/15/001

**Date:** 2026-09-29  
**Disposition:** **FAILED**  
**Audited tree:** `641d58614b35acbb121566b1b35cb89daa37a1bd` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**PASS_WITH_MINOR_CAVEAT** — The numerical implication is correct from the 3D shrinker classification and the entropy values: nu(R^3)=0, nu(S^2xR)=log 2-1, so the Gaussian is 1-log 2≈0.30685 away; a nontrivial free cylinder quotient lowers entropy by at least log 2. The discussion of nontrivial smooth Gaussian quotients is unnecessary because an orthogonal finite group fixes the potential minimum, but including them as hypothetical farther competitors does not invalidate the 0.2 implication.

## Originality

**FAIL** — Once the standard 3D classification and elementary finite-cover entropy shift are accepted, every epsilon < 1-log 2 gives the claimed cylinder gap. The choice 0.2 is arbitrary and no new rigidity mechanism, classification, invariant, or computation is introduced.

## Value

**FAIL** — The record is a short numerical corollary of a complete known classification. It does not materially advance the cylinder-rigidity problem beyond repackaging the classified entropy values, so it falls below the scientific-value threshold for a validated finding even though the implication itself is correct.

## Literature/evidence checked

- [Cao–Zhou, On complete gradient shrinking Ricci solitons](https://doi.org/10.4310/jdg/1287580963): Standard shrinker background/classification references.
- [Li–Wang, Rigidity of the round cylinders in Ricci shrinkers](https://arxiv.org/abs/2108.03622): Cylinder rigidity under pointed-Gromov–Hausdorff closeness, not entropy closeness.

## Limitations of this audit

Literature comparisons are claim-specific and do not constitute an exhaustive priority proof. GitHub was read only. Computations described as independent were reconstructed from stated finite data or supplied artifacts; no inaccessible paper is claimed as read.
