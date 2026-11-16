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
# Reproducible verification
Run `python3 c4_check.py` with Python 3. The code directly sums four-cycle sign products for all \(2^{3n}\) edge signings in each dimension \(2\le n\le5\), independently constructs the four-cell multinomial distribution, and verifies agreement for **every** coefficient. It checks zero and second moments through \(n=8\), and the predicted zero-free dimensions through \(n=22\). The expected terminal marker is `ALL_C4_CHECKS_PASS`. The symbolic argument in RESULT.md, rather than the finite checker, proves the result for every integer \(n\ge2\).
