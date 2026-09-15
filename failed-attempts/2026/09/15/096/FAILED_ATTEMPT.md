# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Supersingular Honda-Tate realization for K3 surfaces over finite fields with Artin-invariant control
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20318
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** crystalline cohomology and Tate-class analysis

## Problem

Let q=p^a and sigma_0 in {1,...,10}. Prove a finite-exact two-sided supersingular Honda-Tate statement: (i) [necessity, unconditional via known Tate] if X/F_q is a (supersingular, i.e. infinite-height / rho=22 geometrically) K3 surface of geometric Artin invariant sigma_0, then L(X/F_q,T)=prod_{i=1}^{22}(1-zeta_i T) with zeta_i roots of unity satisfies the crystalline discriminant condition disc NS(X_{bar F_q})=-p^{2 sigma_0} with the Frobenius action on H^2_crys / discriminant group prescribed by Ogus' theory, plus the Artin-Tate formula constraint on L(1), hence #X(F_q)=1+q^2+q*m with m in Z cap [-22,22] restricted accordingly; (ii) [sufficiency, conditional on potential semi-stability (star) as in Taelman] conversely every root-of-unity Weil polynomial satisfying those crystalline/Tate necessary conditions for the given (q,sigma_0) occurs as L(X'/F_{q^n},T) for some n>=1 and some supersingular K3 surface X'/F_{q^n} of Artin invariant sigma_0, with explicit control of the field of full rho=22 definition. In particular determine exactly which integers m occur as (#X(F_q)-1-q^2)/q for supersingular X/F_q of invariant sigma_0. This is finite-exact (fixed q, exact L), not a q->infinity asymptotic; only (ii) is conditional on (star).

## Attempted claim

Let q=p^a and sigma_0 in {1,...,10}. Prove a finite-exact two-sided supersingular Honda-Tate statement: (i) [necessity, unconditional via known Tate] if X/F_q is a (supersingular, i.e. infinite-height / rho=22 geometrically) K3 surface of geometric Artin invariant sigma_0, then L(X/F_q,T)=prod_{i=1}^{22}(1-zeta_i T) with zeta_i roots of unity satisfies the crystalline discriminant condition disc NS(X_{bar F_q})=-p^{2 sigma_0} with the Frobenius action on H^2_crys / discriminant group prescribed by Ogus' theory, plus the Artin-Tate formula constraint on L(1), hence #X(F_q)=1+q^2+q*m with m in Z cap [-22,22] restricted accordingly; (ii) [sufficiency, conditional on potential semi-stability (star) as in Taelman] conversely every root-of-unity Weil polynomial satisfying those crystalline/Tate necessary conditions for the given (q,sigma_0) occurs as L(X'/F_{q^n},T) for some n>=1 and some supersingular K3 surface X'/F_{q^n} of Artin invariant sigma_0, with explicit control of the field of full rho=22 definition. In particular determine exactly which integers m occur as (#X(F_q)-1-q^2)/q for supersingular X/F_q of invariant sigma_0. This is finite-exact (fixed q, exact L), not a q->infinity asymptotic; only (ii) is conditional on (star).

## Research outcome

Proved the finite-exact two-sided supersingular Honda-Tate statement: unconditional necessity with crystalline and Artin-Tate restrictions and exact endpoint theorems, plus conditional sufficiency via (star)/Taelman with field control, and a finite enumeration deciding the exact m-set.

## Why this attempt failed

Failed axes: correctness, value.

correctness: TARGET route; reran enumerate_m.py/witness_m.py confirming 60280 multisets, 43 orbit types, unconstrained m=[-22,22] and endpoint B values (B=1 for m=22, B=2^22 for m=-22) and qB-square checks. N(1) root-of-unity shape, N(2) disc=-p^{2sigma0} and weak bound aN even and >=2sigma0 via base-change, and N(3) necessity qB/|D| square with endpoint necessity are essentially correct modulo thin (Sq) p-part citation. BUT Theorem S sufficiency is invalid: it invokes Taelman's conditional machine for all-roots-of-unity (supersingular) data while Taelman Thm1/Thm2 explicitly assume not supersingular (verified full-text), so hypothesis fails; Ogus sigma0-matching and discriminant-group prescription is asserted without finite-index lattice proof; Sec.6 admits 0<r<22 sublattice-index verification unevaluated, so Corollary M exact equality for M(q,sigma0) is overclaimed (only r=0,22 evaluated; witnesses are numeric not surfaces). Endpoint iff relies on unproved sufficiency (only => proved). Lemma C shows literal target (same P_q over F_{q^n}, n>1) impossible by Weil weight q^n!=q: ADMISSION_DEFECT normalization error. value: Correctly proved part (necessity plus 60280-multiset combinatorics plus endpoint necessity a-even) is mechanical recombination of cited Tate/Ogus/Artin-Tate black boxes and elementary phi(d)<=22 enumeration, with no new lemma, boundary, or downstream use; r=0 numeric qB-square witnesses are not geometric realizations. Claimed valuable exact set M(q,sigma0) is not decided (0<r<22 missing, sufficiency invalid, iff unproved). Literal target is impossible for n>1 by weight (Lemma C), so negative resolution is a cheap normalization/type error: ADMISSION_DEFECT; per STANDARD such literal falsity still fails value. No independently retrievable exact invariant is established as stated, though narrow exact data could in principle be valuable if proved.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; supply independent motivation and a materially stronger contribution; address the recorded limitation: Theorem S sufficiency is conditional on potential semistability (star) and inherits the characteristic and level hypotheses of Taelman's construction, as permitted by the target; only part (ii) uses (star) while part (i) is unconditional. The p-part of Brauer squareness is used via the crystalline refinement; prime-to-p squareness is unconditional via Tate pairings. For 0<r<22 the Artin-Tate square test is given as an exact finite sublattice-index criterion with complete evaluation for r in {0,…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
