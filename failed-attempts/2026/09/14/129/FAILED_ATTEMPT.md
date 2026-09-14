# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Finite-time blowup embedding for the focusing energy-supercritical NLS on a generic irrational torus via Euclidean profiles
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20137
- **Disposition:** AUDIT_1_REJECT
- **Domain:** Partial Differential Equations
- **Method:** profile decomposition and long-time Strichartz estimate techniques

## Problem

Let T^4_alpha=R^4/(alpha_1 Z x alpha_2 Z x alpha_3 Z x alpha_4 Z) with generic Diophantine alpha in the full-measure set for which long-time Strichartz estimates hold, Delta_alpha the associated Laplacian, and consider the focusing quintic (s_c=3/2, energy-supercritical) (i d_t + Delta_alpha)u = -|u|^4 u, u(0)=u_0 in H^{3/2}(T^4_alpha). Assume the critical local well-posedness of Kwak-Kwon and Wang et al. Prove or disprove the following finite-exact statement via irrational profile decomposition and long-time Strichartz techniques: there exist Euclidean focusing quintic finite-time blowup data v_0 in H^{3/2}(R^4) with maximal time 0<T*<infinity and rescaled periodized truncations u_{0,N}=Phi_N(v_0) concentrating at scale N^{-1} << min alpha_i whose maximal solutions u_N on T^4_alpha satisfy T*_{alpha,N}<infinity and T*_{alpha,N} -> T* with nonlinear Euclidean-profile approximation valid up to T* modulo errors controlled only by the Diophantine constants of alpha. In particular establish (or refute by torus arrest) the nonlinear Euclidean-profile embedding lemma on T^4_alpha up to Euclidean blowup time. T*<infinity with critical-norm blowup is required; infinite-time norm growth or conditional bounds assuming an a priori critical bound do not suffice.

## Attempted claim

Let T^4_alpha=R^4/(alpha_1 Z x alpha_2 Z x alpha_3 Z x alpha_4 Z) with generic Diophantine alpha in the full-measure set for which long-time Strichartz estimates hold, Delta_alpha the associated Laplacian, and consider the focusing quintic (s_c=3/2, energy-supercritical) (i d_t + Delta_alpha)u = -|u|^4 u, u(0)=u_0 in H^{3/2}(T^4_alpha). Assume the critical local well-posedness of Kwak-Kwon and Wang et al. Prove or disprove the following finite-exact statement via irrational profile decomposition and long-time Strichartz techniques: there exist Euclidean focusing quintic finite-time blowup data v_0 in H^{3/2}(R^4) with maximal time 0<T*<infinity and rescaled periodized truncations u_{0,N}=Phi_N(v_0) concentrating at scale N^{-1} << min alpha_i whose maximal solutions u_N on T^4_alpha satisfy T*_{alpha,N}<infinity and T*_{alpha,N} -> T* with nonlinear Euclidean-profile approximation valid up to T* modulo errors controlled only by the Diophantine constants of alpha. In particular establish (or refute by torus arrest) the nonlinear Euclidean-profile embedding lemma on T^4_alpha up to Euclidean blowup time. T*<infinity with critical-norm blowup is required; infinite-time norm growth or conditional bounds assuming an a priori critical bound do not suffice.

## Research outcome

Disproved the target as stated: explicit virial blowup data plus exact critical scaling (T*/N^2->0) and endpoint Strichartz divergence rule out O(1) torus-blowup-time convergence with Diophantine-uniform profile approximation up to T*.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: the negative resolution exposes only the target's missing N^{-2} time normalization, i.e. a type/normalization error of exactly the kind Admission should have ruled out. The DRAFT concedes the defect is the missing rescaling, claims no torus arrest, and leaves the substantive corrected shrinking-window embedding (T*_{alpha,N} ~ T*/N^2) unproved. The established content is textbook Glassey virial plus a routine scaling substitution with no new theorem, lemma, witness, census, or motivated exact invariant a future researcher would need. Per the TARGET route policy, a literally-false verdict via a cheap normalization defect still FAILs value.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: The assumed H^{3/2} critical local well-posedness of Kwak-Kwon and Wang et al. is taken as a black box per the target and is not re-proved. The corrected rescaled embedding (T*_{alpha,N} ~ T*/N^2 on shrinking windows) is identified as a different claim and is not proved here. No torus-arrest/global-existence alternative is claimed. Euclidean blowup is exhibited for one explicit Schwartz family (A^4>108) rather than a full classification; irrational-torus Strichartz inputs are needed only to sta…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
