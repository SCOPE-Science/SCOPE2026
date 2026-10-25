---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditioned on the source-exact premises expressly included in the finding (38-dimensional integral symplectic S with chi=p²hh*, h irreducible, K=ker p(S) rational dimension two, L integral isotropic), all steps are sound: independent exact polynomial factorization confirms h irreducible, h != reciprocal h*, and gcd(h,h*)=gcd(h,p)=1. A common unit-circle root for real h would also be a root of h*; impossible. L is primitive as K intersection integral lattice; unimodular alternating symplectic basis extension gives free rank 34 quotient L^perp/L with integral symplectic induced form. By symplectic duality the two removed 2D factors both have chi p; quotient chi=hh*. Reciprocal degree 34 with no unit-circle roots gives stable/unstable real dimensions 17 each. p-primary 4D with dim ker p=2 forces one Q[t]/p² block, one Jordan block at each ±i; periodic rational vectors exactly K. B=R^{-1}Q is conjugate to A=QR^{-1} by R^{-1}. Exact SymPy verifies arithmetic but not original genus-19 38x38 matrix or full primary Appendix; all source-level premises are separately flagged as external.

## originality

FAIL

Although the exact named quotient theorem is not visible in accessible abstracts or distinct SCOPE/Resultary findings, the submission expressly takes from the October 1 Baykur--Stipsicz--Szabo source the entire degree-38 polynomial p^2*h*h* with h irreducible, dim ker p(S)=2, and its primitive isotropic integral lattice. These published source-specific facts mechanically imply every asserted new conclusion by standard symplectic linear algebra: h != h* forces coprimality and absence of unit roots; quotient by the isotropic kernel removes two p factors; the remaining reciprocal degree-34 polynomial yields 17+17 hyperbolicity; dim ker p=2 forces a single Q[t]/(p^2) block. This is a covered direct corollary of the source calculations, despite not necessarily being worded there as a separate Anosov quotient theorem. Full source inspection was blocked, so the source-to-claim implication is documented with its reliance on the submission’s exact attributions.

## value

FAIL

The quotient L^perp/L is a natural object, and structural Anosov dynamics is a mathematically relevant description; however the submitted exact statement is obtained entirely by standard symplectic reduction and rational-canonical/Jordan deductions from the previous authors’ specific characteristic polynomial and two-dimensional isotropic kernel. Its 34-dimensional rank, 17+17 split and p² primary module are forced immediately by that known data, with no independently new invariant, nonstandard lemma, meaningful boundary, fresh classification or added computation. As a standalone claim it is a restatement of textbook consequences of already-reported source computations, not an independently useful unknown precise fact. This is a value judgment about the submitted contribution, not about the broader mathematical importance of the Baykur–Stipsicz–Szabó construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
