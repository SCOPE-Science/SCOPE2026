# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Arithmeticity of the first compact Coxeter 4-cube
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1548
- **Disposition:** AUDIT_1_REJECT
- **Domain:** compact hyperbolic Coxeter 4-polytopes
- **Method:** Gram-matrix cyclic products and Galois signatures via PARI/GP

## Problem

Let C0 be one explicit compact hyperbolic Coxeter 4-cube with 8 facets from the Ma-Zheng complete classification (the first diagram in the 12-cube Jacquemet-Tschantz/Ma-Zheng list with all dihedral angles pi/m), with Coxeter Gram matrix G0 and Vinberg field k0=Q(cyclic products of 2G0). Prove or disprove that the reflection group of C0 is arithmetic over k0 by the Vinberg criterion. A complete answer must either certify arithmeticity via exact Gram-matrix computation (field degree, cyclic-product integrality, and signature conditions with PARI/GP certificate), or prove it is properly quasi-arithmetic or non-arithmetic by exhibiting the exact failing Vinberg invariant (a non-integral cyclic product, a wrong Galois-conjugate signature, or a non-isomorphic Vinberg form) with certificate.

## Attempted claim

Let C0 be one explicit compact hyperbolic Coxeter 4-cube with 8 facets from the Ma-Zheng complete classification (the first diagram in the 12-cube Jacquemet-Tschantz/Ma-Zheng list with all dihedral angles pi/m), with Coxeter Gram matrix G0 and Vinberg field k0=Q(cyclic products of 2G0). Prove or disprove that the reflection group of C0 is arithmetic over k0 by the Vinberg criterion. A complete answer must either certify arithmeticity via exact Gram-matrix computation (field degree, cyclic-product integrality, and signature conditions with PARI/GP certificate), or prove it is properly quasi-arithmetic or non-arithmetic by exhibiting the exact failing Vinberg invariant (a non-integral cyclic product, a wrong Galois-conjugate signature, or a non-isomorphic Vinberg form) with certificate.

## Research outcome

Disproved arithmeticity of the first compact Coxeter 4-cube: k0=Q(sqrt13), failing invariant 4c^2=(10+2sqrt13)/3 of norm 16/3; conjugate form PSD so properly quasi-arithmetic.

## Why this attempt failed

Failed axes: originality.

originality: ADMISSION_DEFECT: Jacquemet-Tschantz (2018), Remark 9, verified in the published PDF, already records this exact graph Sigma_1^{2,2,3} as non-arithmetic via Vinberg's arithmeticity criterion, so the TARGET verdict itself was published before Admission. Fused retrieval (20 results, all providers ok) found the JT/MZ classifications and no per-cube certificate, but verdict-level coverage suffices since a prior source need not state the headline verbatim. The new explicit failing product 4c^2 of norm 16/3 is a recomputation/certificate of that known verdict, an explicit originality failure mode. Originality failure is never repairable.

## Conditions for a legitimate retry

state a substantive result not covered by the identified prior work; address the recorded limitation: PARI/GP was unavailable on this host so exact certificates were produced with sympy (exact algebraic arithmetic) instead; the conjugate-signature certificate uses an exact integer discriminant/product/sum argument rather than a PARI nfcert. The Gram-matrix solid-edge placement was reconstructed from the published figures (JT Fig.1, MZ Fig.34) and validated internally (signature (4,1), 16/16 elliptic vertices, dotted lengths matching JT Table 4 and MZ Table 17), but not byte-compared against the…

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
