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

# Verification

Run `python3 check.py` using the included standalone file in the same directory as RESULT.md. This executes exact integer inequalities and exhaustive vertex-pair enumeration for every integer order 3 through 10, both adjacent-swap layer orders, then 4,800 fixed-seed large-order comparisons and sharpness witnesses through order 201. No third-party package is needed.

Expected output:

```text
ZIGZAG_BRUHAT_DIAMETER_PASS local_cases=80 exhaustive_n=3..10 orientations=2 vertex_pairs=348500 random_pairs=4800
```

Mathematical proof is in RESULT.md: Bruhat subword characterization, exact two-coordinate bounds, four parity/orientation cases, equality classification and exclusion of nonvertex maximizers. Finite tests are corroboration, not an infinite certificate or evidence for historical priority.

This is a self-review only. No independent mathematical validation or independent audit has been performed.
