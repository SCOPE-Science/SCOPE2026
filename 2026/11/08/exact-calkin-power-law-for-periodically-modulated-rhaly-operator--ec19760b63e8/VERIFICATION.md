---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: Periodic zero-mean partial sums are uniformly bounded, so summation by parts bounds Σ_{j=k}^n d_j/j=O(1/k) and Σ_{j>=M}e_j/j²=O(M^-2). Thus CD_dC and C*D_eC are Hilbert–Schmidt. The Cesàro weakly null harmonic packets give essential norm 2; its commutator C*C-CC* is Hilbert–Schmidt, so its Calkin image a is normal. With b=pi(D_c), aba=ma² and a*b*ba=mu a*a imply (ba)^p=m^(p-1)ba^p and ||ba^p||=sqrt(mu)2^p. The zero-mean square-zero and numerical-radius conclusions follow by C*-algebra calculus, with p=1 interpreted separately at m=0. A finite independent check tested periodic cancellation entrywise for multiple patterns; the proof is infinite-dimensional.

## originality

PASS

PASS (best knowledge): the relevant earlier periodic Rhaly Gram theorem computes the trace-class Gram averaging and first essential norm, and Sang gives Toeplitz-algebra membership, but neither establishes the full complex-periodic all-power essential norm or square-zero Calkin behavior. The additional mean m controls powers, while the earlier Gram result involves only mu. General earlier power-calculus coverage is a residual risk.

## value

PASS

PASS: the contrast of identical positive Gram operators with sharply different essential spectral radii is a motivated operator-theoretic distinction. The exact two-moment, all-power law and noncompact square-zero Calkin example are reusable structural facts and are not a generic restatement of Gram compactness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
