---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Fourier isolation of differences splits Hermitian lifting into a real diagonal block W0 and doubled real blocks Wd for d>0. Completing Gaussian squares produces generalized Vandermonde matrices with distinct positive nodes and distinct integer exponents; Rolle induction gives rank min(r,m_d). Pair multiplicities yield the exact full rank, unique-difference extremizer, and consecutive-set formula. For trace-one recovery r=n-1, the remaining one-dimensional diagonal kernel is killed precisely when the augmented W0/trace determinant is nonzero. Two symmetric centers for {-1,0,1} give the claimed cosh resonance. All quantifiers are continuous time, arbitrary distinct centers and finite integer S; no nonlinear all-signal inference is made.

## originality

PASS

PASS on inspected sources: the two-frequency-bin phase retrieval papers concern identification of rank-one signals, whereas the new rank and kernel are for *all* Hermitian matrices and all integer spectra. The arbitrary multiplicity formula is not implied by a pure-state uniqueness theorem. A three-tone filtered example and finite Gabor orbit ranks are narrower or different operators.

## value

PASS

PASS: the multiplicity-counting invariant yields exact missing degrees of mixed-state tomography and sharp necessary/sufficient channel thresholds, including an exceptional trace-one filter configuration. The choice of spectrum matters quantitatively, creating a useful structural distinction between Sidon and consecutive frequencies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
