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

The standalone `verify.py` uses only the Python standard library. It exhausts the four reduced order-four Latin squares (all others are isotopic after relabeling), calculates the two intercalate types, checks the 28-vertex marked graph, and reconstructs all 27 Smith valuations at primes two and three for every reduced Latin square. Exact determinants independently verify their completeness and exclude all other primes. The success marker in `verification_output.txt` is from this package's own executable program. The algebraic-geometric interpretation also invokes the usual theorem identifying split, regular, unit-thickness semistable Jacobian component groups with graph degree-class groups. Neither an arbitrary weighted smoothing nor the full plane divisor is covered. Independent mathematical audit not performed.
