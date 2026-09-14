# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Localization of the Ma–Schwede perfectoid test ideal
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20041
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Commutative Algebra
- **Method:** perfectoid big Cohen-Macaulay algebras and test-ideal comparison

## Problem

Let (A,m) be a complete Noetherian regular local ring of mixed characteristic (0,p), let a be an ideal of A, and let t>=0. For every prime Q containing (p,a), is the exact equality tau(A,a^t) times the Q A_Q-adic completion of A_Q = tau(the Q A_Q-adic completion of A_Q,(a times that completion)^t), with both test ideals defined by the Ma–Schwede perfectoid construction using compatible p-power-root data?

## Attempted claim

Let (A,m) be a complete Noetherian regular local ring of mixed characteristic (0,p), let a be an ideal of A, and let t>=0. For every prime Q containing (p,a), is the exact equality tau(A,a^t) times the Q A_Q-adic completion of A_Q = tau(the Q A_Q-adic completion of A_Q,(a times that completion)^t), with both test ideals defined by the Ma–Schwede perfectoid construction using compatible p-power-root data?

## Research outcome

Proved completion-of-localization for fixed-data Ma-Schwede perfectoid test ideals via exact finite-tower Hom base change plus a retraction lemma and MS stabilization, with SNC confirmation and a verified computational model.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET route: finite-level S-linear base-change I_e(u)S=I_part=I_full and SNC formula transport are sound and the toy retraction script reproduces, but the essential bridge in DRAFT Sec.5 that tau([f]^t)=J(t+epsilon0) and tau(S,[fS]^t)=J^S for general nonprincipal a is asserted not proved. It cites MS Cor.2.7/Lemmas 5.2-5.5 plus Noetherian stabilization, yet those MS results concern stabilization of diamond submodules 0_[k,k] and blowup comparison, not identification of A_infty almost-annihilators with finite Hom-evaluation ideals I_e, and the almost-vs-honest p^{1/p^infty} torsion and completion/colimit passage plus construction of S_infty extending transported [fS] are missing. Principal/SNC detail from MS Cor.3.10/Ex.8.1 does not imply the general case. Hence the headline equality is not established; computation is only a model check, not a proof.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: The proved equality is for the fixed compatible-data ideals tau([f]^t) named by the target; the all-compatible-roots variant tau(a^t) contains it by MS (†) but equality of the (†) inclusions is MS Question 9.1 (open) and not claimed. The general nonprincipal Hom-identification step follows the Ma-Schwede machine (Corollary 2.7, Lemmas 5.2-5.5) with principal/SNC cases fully detailed in MS; degenerate inputs (a=0, t<0) are outside MS scope. The argument bypasses rather than solves perfectoid bas…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
