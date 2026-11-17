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

The q-fold root-of-unity sum makes off-residue Fourier Gram entries exactly zero; within each residue N_r the substitution beta=q alpha gives a single symmetric interval Gram. Analytic exterior powers of the Fourier synthesis operator have unique leading Taylor multi-index {0,...,j}, so division of consecutive wedge norms yields eigenvalue c_{r,j} beta^(2j+1). The factor from the monic Legendre polynomial is 2^(2j)/((2j+1)(j!)^2 binom(2j,j)^2 pi), and W_{r,j} is the moment-determinant ratio. Positivity, largest-residue conditioning, and exact collision-free tightness follow. Independent 3-node high-precision Legendre constant checks passed; they cannot replace the all-fixed-mask analytic proof.

## originality

PASS

The indexed literature covers clustered Vandermonde exponents and general Fourier concentration, but the inspected Batenkov 2019/2020 original Theorems 2.2–2.3 only give order estimates and cluster-count multiplicities. The arithmetic decomposition and exact all-level determinant constants on arbitrary finite sparse masks remain best-of-knowledge distinct.

## value

PASS

A natural observation/reconstruction problem for Fourier masks: complete hierarchy and sharp constants predict exactly which frequency collisions degrade reconstruction. Exact finite-mask constants and perfect-frame criterion have independent design value beyond order bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
