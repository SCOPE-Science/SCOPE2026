# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** WLP failure for an explicit non-monomial (3,3,4) complete intersection over F2 by direct multiplication rank
- **Round:** 2026-09-07-first-light-01
- **Lane:** 246
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** direct Macaulay-matrix rank of multiplication by ell with syzygy-splitting cross-check

## Problem

Decide WLP for the explicitly committed non-monomial complete intersection A=F2[x,y,z]/I with f1=x^3+y^2*z+y*z^2, f2=y^3+x^2*z+x*z^2, f3=z^4+x*y^3+x^3*y and linear form ell=x+y+z: verify (f1,f2,f3) is a regular sequence, construct monomial bases of A_3 and A_4, and determine by exact F2 linear algebra whether xell:A_3->A_4 has maximal rank, cross-checked by the splitting type of Syz(f1,f2,f3).

## Attempted claim

For A=F2[x,y,z]/(f1,f2,f3) with f1=x^3+y^2*z+y*z^2, f2=y^3+x^2*z+x*z^2, f3=z^4+x*y^3+x^3*y, the multiplication map xell:A_3->A_4 with ell=x+y+z fails maximal rank over F2 (explicit rank deficiency with logged witness), so this non-monomial type-(3,3,4) complete intersection fails WLP in characteristic 2.

## Research outcome

Char-2 WLP failure for an explicit non-monomial (3,3,4) complete intersection. The as-written admitted triple (f3 without x^4) is NOT a CI (Hilbert tail 2, non-Artinian); with the disclosed minimal repair f3'=f3+x^4, A'=F2[x,y,z]/(f1,f2,f3') is a CI with Hilbert (1,3,6,8,8,6,3,1,0), and x(x+y+z):A'3->A'4 has rank 7<8 (det 0) with hand-checkable kernel identity (x+y+z)(y^2z+xy^2+x^2z+x^2y)=y*f1+x*f2, while xx:A'3->A'4 is an isomorphism. Verified by stdlib-only exact F2 linear algebra replayer.

## Why this attempt failed

Failed axes: correctness, value.

correctness: Machine facts partially verify but headline inference is false. Re-ran inputs/artifacts/verify.py: VERIFY_OK, Hilbert [1,3,6,8,8,6,3,1,0], rank(x:A3->A4)=8 det 1, rank(x+y+z:A3->A4)=7 det 0, kernel [0,1,0,0,1,1,1,0]. Hand identity independently re-expanded and holds over F2: (x+y+z)*k = y*f1+x*f2 with k=y^2z+xy^2+x^2z+x^2y, and k not in {0,f1,f2,f1+f2}=I_3, so x_ell has nontrivial kernel conditional on (a). Full-degree recomputation from same Macaulay code confirms DRAFT 3(c): x,y,x+z,y+z have full rank in every degree 0..7, while z,x+y,x+y+z fail somewhere. By the standard existential definition of WLP (Harima et al.: there EXISTS ell with maximal rank in every degree), existence of x as a strong Lefschetz element PROVES A' HAS WLP (indeed SLP for x). This directly contradicts Theorem (b)'s 'Hence A' fails WLP' and the target_claim's 'so this CI fails WLP'. What is proved is only that ell=x+y+z is a non-Lefschetz element, not WLP failure. Second independent defect: admitted triple f3 without x^4 is not a CI; recomputed Hilbert tail [1,3,6,8,8,6,3,2,2,2,...] for d=0..11, non-Artinian, so admitted headline is false for admitted object. DRAFT discloses repair f3'=f3+x^4 but headline remains false under correct definition. value: The admitted headline (first non-monomial mixed-type CI WLP failure showing monomial classification does not extend) is false, and its true correction has no independent retrieval value. Corrected statement is: A' HAS WLP (witness x) and x+y+z is one non-Lefschetz element. An ell-specific non-maximal rank in an algebra that has WLP is not a boundary-changing extremal witness, does not test Li-Zanello/Brenner-Kaid stability (those concern existential WLP), and is not the motivated invariant. Repaired object is post-hoc arbitrary: DRAFT lists three working one-term fixes (f3+x^4, f3+y^4, f3+x^2y^2) with x^4 chosen; it breaks the admitted x/y symmetry and was motivated only to restore Artinianity after computation, failing the 'motivated before computation' standard. No determinantal locus formula or concentration lemma (admitted fallback) is delivered. Certification of one 8x8 rank for one bad form of one ad-hoc point while a good form exists is an unexplained enumeration; certification alone does not rescue it.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Verdict is for the repaired ideal (f1,f2,f3+x^4), not the as-written non-Artinian triple (deviation disclosed in DRAFT). Char 2 only; no Q-side claim (Harima et al. give WLP in char 0). Ell-specific failure (x is Lefschetz). Syzygy-splitting cross-check replaced by full-profile Lefschetz contrast. No determinantal-locus closed form claimed.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
