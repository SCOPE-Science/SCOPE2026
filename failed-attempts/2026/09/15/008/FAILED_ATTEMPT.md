# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Tamagawa-refined Bloch-Kato divisibility for the prime-conductor-277 paramodular abelian surface via the GSp(4) Euler system
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20183
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** Euler systems and Selmer complexes

## Problem

Let A/Q be the paramodular abelian surface of prime conductor 277 with End_Q(A)=Z (LMFDB genus-2 curve 277.a.277.1), assumed of analytic rank 0, i.e. L(A,1) != 0. Let p>=5 be a prime of good ordinary reduction for A with p not dividing 277, such that the residual spin representation is absolutely irreducible and p-distinguished, the p-adic spin representation admits a Klingen-ordinary refinement through a Hida family, and the standard big-image/local-vanishing hypotheses of the Loeffler-Skinner-Zerbes Euler-system machinery hold. With Omega_A the real period, Tam(A/Q)=prod_v c_v the Tamagawa product including c_277, and #Sha(A/Q)_an = L(A,1)*#A(Q)_tors*#A^vee(Q)_tors/(Omega_A*Tam(A/Q)), prove via the Loeffler-Skinner-Zerbes GSp(4) Euler system with the local Tamagawa ideal at ell=277 made explicit the finite exact divisibility v_p(#Sha(A/Q)) <= v_p(#Sha(A/Q)_an).

## Attempted claim

Let A/Q be the paramodular abelian surface of prime conductor 277 with End_Q(A)=Z (LMFDB genus-2 curve 277.a.277.1), assumed of analytic rank 0, i.e. L(A,1) != 0. Let p>=5 be a prime of good ordinary reduction for A with p not dividing 277, such that the residual spin representation is absolutely irreducible and p-distinguished, the p-adic spin representation admits a Klingen-ordinary refinement through a Hida family, and the standard big-image/local-vanishing hypotheses of the Loeffler-Skinner-Zerbes Euler-system machinery hold. With Omega_A the real period, Tam(A/Q)=prod_v c_v the Tamagawa product including c_277, and #Sha(A/Q)_an = L(A,1)*#A(Q)_tors*#A^vee(Q)_tors/(Omega_A*Tam(A/Q)), prove via the Loeffler-Skinner-Zerbes GSp(4) Euler system with the local Tamagawa ideal at ell=277 made explicit the finite exact divisibility v_p(#Sha(A/Q)) <= v_p(#Sha(A/Q)_an).

## Research outcome

Proved the Tamagawa-refined Bloch-Kato divisibility for the 277 paramodular surface under the stated hypotheses, with c_277=1 computed explicitly.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route: conditional proof checked against admitted target. Lemma c_277=1 is correct and cross-checked via LMFDB Tamagawa 1 plus I_{1-0-0} nodal geometry; torsion Z/15Z and p>=7 p-unit bookkeeping and p=5 reducibility remark are correct; point counts are consistency evidence only. Essential divisibility inference FAILS: draft asserts optimally-normalised automorphic period equals Neron period Omega_A up to p-unit, but LZ 2110.13102 Remark 8.2.3 explicitly states this comparison is not obvious/unknown, so Thm 8.2.4 yields only automorphic-period Iwasawa divisibility, not the stated v_p(#Sha)<=v_p(#Sha_an) with Neron period. Odd-twist nonvanishing hypothesis (4) is claimed automatic from L(A,1)!=0 plus End=Z, without proof, and no admissible p is shown to satisfy deformability/big-image, leaving possibly empty antecedent. value: Even taken as conditional TARGET statement, result adds no independently retrievable fact: the only unconditional computations (c_277=1, torsion 15, Tam=1, point-count divisibility by 15) are already in the LMFDB 277.a.277.1 tables, hence known-database recomputation plus certification which the STANDARD says do not create value. The headline conditional inequality is unproved due to the period-comparison gap, assumes odd-twist/deformability/big-image with no verified admissible prime exhibited, and therefore does not materially advance BSD/Bloch-Kato for the first paramodular surface beyond quoting the general LZ theorem with a label substitution.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: The result is conditional on the target's own hypotheses (good ordinary reduction, Klingen-ordinary Hida deformability, residual irreducibility and p-distinguishedness, big-image and local-vanishing conditions, odd-twist nonvanishing, L(A,1)!=0) which are assumed, not proved, for any specific prime p; the quoted LSZ Euler system, LZ explicit reciprocity law, and LZ BSD-descent theorems are used as black boxes with exact references rather than re-proved; the point counts and LMFDB numerics are c…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
