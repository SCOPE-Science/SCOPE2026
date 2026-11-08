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

# Exact verification

`check.py` is a standalone Python 3 standard-library script. Run `python3 check.py` to recompute the eleven exact hexadecimal triangular values and their weight \(26\), test the repunit identities on bounded inputs, and check the full eleven-consecutive construction for triangular weights \(H=t(t+1)/2\) with \(13\le t\le26\). The proof's two exact identities and no-carry inequalities cover all admissible integers beyond those test inputs.

The proof does not rely on probabilistic tests or finite extrapolation. The listed seed is completely reproducible from integer multiplication, and no inaccessible external software, downloaded data or other result is needed to replay it.

No independent mathematical review has been performed, and no claim concerning arbitrary-length runs, least starting index or novelty beyond the inspected literature is certified.
