---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Execute `python3 verify.py` from the extracted directory with any standard Python 3 installation. The script has no third-party dependencies and generates the entire normalized projective plane, all curve-smooth rational points, the Gauss-image line coefficients, all noncollinear triples of prospective projective-triangle vertices, and four quadratic-character patterns for each triple.

The expected final marker is `SIX_OPTIMAL_TANGENT_COVERS_VERIFIED 6 S3_ORBIT 6 TRIPLES 59640 NONCOLLINEAR 55129`. It tests each accepted cover against all 133 rational points, yielding incidence multiplicities \(1^{90}2^{15}3^{25}7^3\). It independently verifies that the six coordinate permutations of one cover give exactly all six covers.

The enumeration certifies every **finite** calculation but does not itself prove that all minimum blocking sets must be projective triangles. That reduction uses the explicitly cited theorems of Blokhuis–Brouwer–Wilbrink and Lovász–Schrijver. Geometric irreducibility and the smooth rational-point description come from the cited Asgarli–Ghioca paper; the rational tangent gradient formula follows by differentiation and is checked by modular arithmetic. Independent mathematical audit has not been performed.
