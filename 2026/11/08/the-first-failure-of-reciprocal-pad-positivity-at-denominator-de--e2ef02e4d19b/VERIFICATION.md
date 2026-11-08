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

## Exact certificate and replication

In the directory containing the embedded files run `python3 verify.py`. The file `root_centers.json` contains 330 pairs of integer coordinates, defining rational complex centers at resolution 1/1000000000. The checker uses only `Fraction`, integer arithmetic, `math.isqrt`, and exact comparisons; it does not call any numerical root finder. It proves one root in each of the 330 disjoint radius-1/1000000 disks via a strict Rouché inequality. From the root and derivative enclosures it proves positive-pole dominance for every index at least 300, with a uniform residue-error ratio strictly below 17/50. Exactly 19,734 finite positive recurrence signs are checked, together with the negative witness at numerator degree 66 and coefficient index 38. A successful execution emits `VERIFY_OK`.

The certificate is fully reproducible from these two files without external packages. It does not certify other denominator degrees or all numerator degrees greater than 66. An independent mathematical audit has not been performed.
