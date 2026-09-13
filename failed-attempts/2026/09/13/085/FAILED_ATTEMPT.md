# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Foliation cones of Whitehead (0,1),(7,1)
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1660
- **Disposition:** AUDIT_1_REJECT
- **Domain:** 3-manifold topology / Thurston norm / sutured Floer / depth-one foliations
- **Method:** Gabai hierarchy depth-one construction or sutured Floer polytope obstruction (Altman)

## Problem

Let W be the Whitehead link exterior and let Y3 be the closed filling with slopes (0,1) on the first cusp and (7,1) on the second cusp. Verify that Y3 is closed, orientable, hyperbolic with b1=1 and nontrivial H_2, compute the Thurston norm ball and its fibered faces, and note Y3 is not a rational homology sphere so Santoro Whitehead rational-sphere classification and Dunfield rational-sphere tables do not decide it. Decide with proof the foliation-cone decomposition of Y3 in the sense of Altman: either construct a taut depth-one foliation spanning a non-fibered face, or compute the sutured Floer polytope to prove no non-fibered face carries Z and only fibered cones occur; either proven decomposition for this single named Y3 counts as complete.

## Attempted claim

Let W be the Whitehead link exterior and let Y3 be the closed filling with slopes (0,1) on the first cusp and (7,1) on the second cusp. Verify that Y3 is closed, orientable, hyperbolic with b1=1 and nontrivial H_2, compute the Thurston norm ball and its fibered faces, and note Y3 is not a rational homology sphere so Santoro Whitehead rational-sphere classification and Dunfield rational-sphere tables do not decide it. Decide with proof the foliation-cone decomposition of Y3 in the sense of Altman: either construct a taut depth-one foliation spanning a non-fibered face, or compute the sutured Floer polytope to prove no non-fibered face carries Z and only fibered cones occur; either proven decomposition for this single named Y3 counts as complete.

## Research outcome

Y3 decided: reducible with essential nonseparating sphere, not hyperbolic, Thurston norm identically zero, no taut foliations so the foliation-cone decomposition is empty.

## Why this attempt failed

Failed axes: correctness.

correctness: H1=Z+Z/7, closed/orientable, b1=1/H2=Z are correct, and Lemmas 2-3 follow conditionally from a sphere. But Lemma 1 is invalid: the twice-punctured-disk inner boundaries are meridians of K1, not longitudes, and a (7,1) filling disk bounds the (7,1) curve, not a meridian; intersection number one is confused with bounding. Capping two meridian boundaries in a (7,1) solid torus gives an annulus, so A union its cap is a torus, not a sphere. Existence of the twice-punctured disk is also asserted from the picture without a diagram or zero-intersection exclusion. Hence no essential sphere, no vanishing norm, and no empty-cone conclusion are proved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The twice-punctured longitude disk is asserted from the classical Whitehead clasp picture (standard diagram fact) rather than machine-verified normal surface enumeration; the prime-summand identification beyond H_1(Q)=Z/7 is left partial since the foliation conclusion does not need it; computational hyperbolicity failure (60+ retriangulations) is corroborating evidence only, with the proof carried by the topological sphere construction.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
