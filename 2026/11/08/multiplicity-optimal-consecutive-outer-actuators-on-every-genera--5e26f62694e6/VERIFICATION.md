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

# Reproducibility

The accompanying `verify_gp.py` requires only the Python standard library. Run `python3 verify_gp.py` after extracting the files without modification. It builds each unweighted generalized Petersen Laplacian directly from its edge list. Every displayed full modular rank is a valid finite certificate of full real Kalman rank because the relevant matrices have integer entries. The modulus is the prime \(1000003\).

The same verifier checks the exact resultant for \(\operatorname{GP}(11,2)\) by computing a determinant in the quotient ring \(\mathbb Z[t]/(t^5+t^4-4t^3-3t^2+3t+1)\), all with integer polynomial arithmetic, and tests the mod-two derivative and \(R(0),R(2)\). Those operations verify the explicit arithmetic illustration. Other numerical spectral coincidences printed in exploratory tests are **not** exact proofs. A deficient modular rank cannot certify a real rank deficiency. General controllability and the universal actuator-count statement are established by the proof rather than finite enumeration.

Scientific boundaries: unweighted, finite graphs with \(n\ge5,2\le k<n/2\), one independent control channel per selected vertex. No external independent audit or stronger certification is claimed.
