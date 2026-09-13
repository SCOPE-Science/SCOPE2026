# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Stable-Jacobian-only smooth conjugacy for complex T^3 pair
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1698
- **Disposition:** AUDIT_1_REJECT
- **Domain:** smooth dynamics Anosov rigidity
- **Method:** Livsic cohomology matching functions quadrilateral holonomy

## Problem

Fix a hyperbolic automorphism L:T^3->T^3 with one real and a pair of non-real complex conjugate eigenvalues. Consider C-infinity Anosov diffeomorphisms f,g on T^3 homotopic to L and C^1-close enough to L that the Franks-Manning topological conjugacy h homotopic to the identity with h∘f=g∘h exists, and assume the one-dimensional stable Jacobian periodic data match: for every periodic point p=f^n(p), log|det(Df^n(p)|E^s_f(p))| equals log|det(Dg^n(h(p))|E^s_g(h(p)))| with no assumption of full or unstable Jacobian matching and no very-non-algebraic genericity hypothesis. Either prove h is then necessarily a C-infinity diffeomorphism, via Livsic cohomology for the stable Jacobian cocycle and Franks-Manning matching functions, or construct an explicit pair f,g satisfying all the above closeness, homotopy, Anosov, and matched stable-Jacobian hypotheses for which h is Holder but not C^1, with full proofs of the Anosov property, periodic-data matching, and failure of C^1 regularity. A complete answer is a rigorous proof of exactly one side.

## Attempted claim

Fix a hyperbolic automorphism L:T^3->T^3 with one real and a pair of non-real complex conjugate eigenvalues. Consider C-infinity Anosov diffeomorphisms f,g on T^3 homotopic to L and C^1-close enough to L that the Franks-Manning topological conjugacy h homotopic to the identity with h∘f=g∘h exists, and assume the one-dimensional stable Jacobian periodic data match: for every periodic point p=f^n(p), log|det(Df^n(p)|E^s_f(p))| equals log|det(Dg^n(h(p))|E^s_g(h(p)))| with no assumption of full or unstable Jacobian matching and no very-non-algebraic genericity hypothesis. Either prove h is then necessarily a C-infinity diffeomorphism, via Livsic cohomology for the stable Jacobian cocycle and Franks-Manning matching functions, or construct an explicit pair f,g satisfying all the above closeness, homotopy, Anosov, and matched stable-Jacobian hypotheses for which h is Holder but not C^1, with full proofs of the Anosov property, periodic-data matching, and failure of C^1 regularity. A complete answer is a rigorous proof of exactly one side.

## Research outcome

Proved the TARGET rigidity side: stable-Jacobian-only periodic-data matching forces the Franks-Manning conjugacy to be C-infinity for C^1-close Anosov pairs on T^3 with a complex unstable pair, via Livsic transfer, matching functions, and quadrilateral conformal holonomy, with three passing computational artifacts.

## Why this attempt failed

Failed axes: correctness.

correctness: TARGET side-A proof is not rigorous. Step 2 rho identity (2) is false as stated: Livsic coboundary gives rho_f = rho_g*(P(x)/P(y)), not equality; telescoping argument omits surviving -u(y)+u(x) term and confuses coboundary rho with matching. Step 1 leafwise C-infinity bootstrap is circular because phi|Ws = a_f^s - a_g^s o h is only Holder (h only Holder a priori), so phi is not C^r along contracting foliation. Step 3 conformal bootstrap is hand-waving: no proof that h|Wu is quasiregular/ACL with bounded dilatation, no Beltrami estimate from (3), single matching function insufficient for inverse-function-theorem, Weyl/Ahlfors-Bers invoked without Sobolev regularity. Step 4 Journe hypotheses (uniform C^r along both foliations) never established. Artifacts verify only linear-model telescoping and O(|u||s|) quad bound, not nonlinear rigidity.

## Conditions for a legitimate retry

repair the decisive proof or computational defect and recheck the full claim; address the recorded limitation: Steps 3-4 of the DRAFT invoke heavy published machinery (Livsic C^r leafwise bootstrap of de la Llave-Marco-Moriyon type, Ahlfors-Bers/Weyl lemma for weak conformality implying smoothness, Journe lemma gluing) as cited inputs rather than re-proving them in-lane; the in-lane original contribution is the stable-only plus complex-pair assembly with quantitative quadrilateral verification on an explicit L. The proof requires the 1D stable bundle to be C^1 (standard for codimension-2 Anosov maps on…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
