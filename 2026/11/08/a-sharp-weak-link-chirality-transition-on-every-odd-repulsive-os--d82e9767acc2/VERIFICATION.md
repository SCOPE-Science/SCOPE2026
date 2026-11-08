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
# Reproducibility and verification

Run `python verify.py` in a directory containing the same embedded `verify.py`. The standard script requires `scipy`. It deterministically seeds 30 independent numerical local-optimization starts per parameter, over 9 positive relative weak-link weights and 4 odd ring sizes \(n=3,5,7,9\), for 1,080 tests. The special size-three case is only a consistency check, not an extension of the claimed new range. The script also evaluates the explicit candidate phase energy and asserts agreement with the root formula. This self-review executed successfully, reporting `VERIFY_OK odd_sizes=4 weight_cases=36 multistart_cases=1080 worst_negative_gap=0`.

Universal optimality is established by the analytic simplex reduction and cosine inequalities, not by finite random sampling; any numerical multistart test could miss non-global competitors. The asymptotic current/energy constants follow from Taylor expansion and the strict inverse-branch monotonicity and have not been independently audited. No external scientific review or independent validation was performed.
