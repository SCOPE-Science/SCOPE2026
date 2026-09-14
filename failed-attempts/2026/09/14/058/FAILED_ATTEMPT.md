# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Exceptional-zero correction to the inert supersingular Heegner Kolyvagin system
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20026
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Arithmetic Geometry
- **Method:** Euler system norm-relation descent

## Problem

Let E/Q be a semistable non-CM elliptic curve of conductor N, let p>=5 be a good supersingular prime, and let K be an imaginary quadratic field with (D_K,Np)=1 such that every prime dividing N splits in K. Assume p is inert in K, E[p] is absolutely irreducible as a G_K-module, the residual ramification condition at the split primes dividing N holds, and the signed Lambda-adic Heegner class kappa_1^sharp is not Lambda-torsion. Let T=T_pE tensor Lambda^iota, let gamma generate Gamma=Gal(K_infty/K), and put X=gamma-1. With I_sharp=char_Lambda(Sel^sharp(K,T)/Lambda*kappa_1^sharp) and J_sharp=char_Lambda((Sel^sharp(K_infty,E[p^infinity])^vee)_tors), compute explicitly the exceptional quotient E_sharp=I_sharp*J_sharp^{-1} as a fractional ideal of Lambda tensor Q_p: determine its X-adic order and every remaining local/Tamagawa factor, and prove the resulting corrected characteristic-ideal identity. In particular, decide whether E_sharp=(X) up to a unit, and state the exact finite-level consequence for the classical Heegner-point Kolyvagin system and the rank-one p-converse.

## Attempted claim

Let E/Q be a semistable non-CM elliptic curve of conductor N, let p>=5 be a good supersingular prime, and let K be an imaginary quadratic field with (D_K,Np)=1 such that every prime dividing N splits in K. Assume p is inert in K, E[p] is absolutely irreducible as a G_K-module, the residual ramification condition at the split primes dividing N holds, and the signed Lambda-adic Heegner class kappa_1^sharp is not Lambda-torsion. Let T=T_pE tensor Lambda^iota, let gamma generate Gamma=Gal(K_infty/K), and put X=gamma-1. With I_sharp=char_Lambda(Sel^sharp(K,T)/Lambda*kappa_1^sharp) and J_sharp=char_Lambda((Sel^sharp(K_infty,E[p^infinity])^vee)_tors), compute explicitly the exceptional quotient E_sharp=I_sharp*J_sharp^{-1} as a fractional ideal of Lambda tensor Q_p: determine its X-adic order and every remaining local/Tamagawa factor, and prove the resulting corrected characteristic-ideal identity. In particular, decide whether E_sharp=(X) up to a unit, and state the exact finite-level consequence for the classical Heegner-point Kolyvagin system and the rank-one p-converse.

## Research outcome

Proved the exceptional-zero correction: E_sharp=(X) up to a unit in Lambda tensor Q_p (X-adic order 1, all Tamagawa factors units), giving the corrected signed Heegner Kolyvagin identity and the rank-one p-converse.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: claim requires exact equality E_sharp=(X)u in Lambda_Qp plus descent. Symbolic checks replicate (Phi1(0)=p, Phi1'(0)=p(p-1)/2, C(0)^2=-pI, (p-1)/4 unit) and script passes. But DRAFT derives equality from a one-sided Mazur-Rubin/Howard Kolyvagin divisibility written as equation (KS), with no opposite inclusion, primitivity, or analytic BSD/reciprocity argument. The bridge from Phi1 calculus to Col^sharp comparison determinant L_p=(X) (cokernel length 1, order neither 0 nor >=2) is asserted, not proved; inert Wach/BKO Coleman identification is quoted. L_aux unit and exact control descent are asserted without proof. Equality therefore does not follow; at most one divisibility plus a formal derivative computation is shown.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Equality is proved in Lambda tensor Q_p, i.e. up to p-power factors and units; integral mu-invariants and exact p-powers at bad primes are not determined. The proof applies the signed Kolyvagin-system formalism (core rank 1, nontriviality, control) under the full stated hypotheses and makes no claim for p=2,3, ordinary p, p split in K, or non-semistable E.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
