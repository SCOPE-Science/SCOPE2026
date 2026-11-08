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

Run `python3 verify.py` with an ordinary Python 3 interpreter; only the Python standard library is required. The script builds finite absorbing generators from occupancy transitions without using the closed product recursion and solves the rational linear systems. It tests \(b=1,\ldots,8\), five rational transform arguments per size (including \(s=0\)), and the independent exact mean-hitting-time systems. Expected output: `VERIFY_OK 48 exact generator/product/mean assertions`.

The test is finite and does not establish the infinite-population weak limit. The result's proof derives the gamma identity from the first-step recursions and proves the convergence of the two-sided near-zero Laplace transforms by gamma-ratio asymptotics. No external expert or formal independent certificate was obtained.
