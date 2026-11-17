---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Verified Fourier factorization I=L²sinc²(Lt/2)[3+2cos(ut)+2cos(vt)+2cos((u+v)t)]. Independent SymPy expansions checked P2=2A, P4=2A², P6=2A³+3Q²(A+Q), A=u²+uv+v²,Q=uv; checked I=-2L²P2-3L⁴/2 and I^(6)=-2L²P6-5L⁴P4-2L⁶P2-9L⁸/28. Strict monotonic Q∈(0,A/3] yields inversion and realization criterion; fixed-A variation proves minimal order six. Square-root branch at u=v yields sharp inverse 1/2; compactness excludes vanishing widths/gaps. Actual CHECK.py inspected with 27 generated tests, 164 reported assertions; analytic proof supplies continuum.

## originality

PASS

Equal-width full-intensity homometry theorem establishes uniqueness for three starts but not a minimal local derivative jet or its sharp inverse Hölder exponent. Related general three-interval Fourier phase retrieval is a different model; best-of-knowledge jet classification survives.

## value

PASS

Sharp minimal finite jet for a natural geometrically constrained phase-retrieval inverse problem, with explicit reconstruction and optimal symmetry-degenerate stability exponent; meaningful measurement-complexity and stability boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
