---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For the precise character chi(2)=exp(2πi/10) in the real harmonic EITFF(11,11,3), the square-affine action partitions all 330 four-subsets into six size-55 orbits. Gram matrix for each representative is similar to a 12×12 cyclotomic matrix; the inspected certificate.py builds Q(zeta_55) entries and uses Faddeev–LeVerrier to check the complete degree-12 characteristic coefficients against the three polynomials in spectra.json, including exactly one simple zero for 12 columns in dimension 11. Positivity of the 11×11 sum of projections plus nonzero degree-one coefficient gives full span; exact quadratic-field Sturm checks isolate each least eigenvalue. Independent recomputation of orbit multiplicities and numerical eigenvalue roots gave class populations 165/110/55 and least roots ≈0.0389554/0.0849397/0.1859598. The numerical check is corroboration; the exact field and Sturm certificate algorithms were inspected for their mathematical soundness, not independently run.

## originality

PASS

Best-of-knowledge original exact spectral classification and optimal lower frame bound for the specific real eleven-plane EITFF. Construction is prior art, not claimed. The published finite-fusion rank/spectrum results identified treat different 7-, 9- or 13-plane objects; no implication carries their coefficients and exact orbit types to this 11-plane object.

## value

PASS

The specific Fickus–Iverson–Jasper–Mixon real 11-plane EITFF is a natural nontrivial fusion frame. Exact erasure-reconstruction stability of all four-subspace selections and the complete orbit-stratified sharp lower bound are meaningful intrinsic geometric invariants not furnished by pairwise coherence alone, with precise extremizers. This is a motivated complete finite classification rather than an arbitrary small random computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
