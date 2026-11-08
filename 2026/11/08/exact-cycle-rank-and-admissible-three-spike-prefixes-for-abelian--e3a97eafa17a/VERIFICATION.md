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

# Verification and reproducibility

Run `python3 checker.py` from the extracted package directory; no external dependencies are required. Its deterministic union-find construction works on the original bipartite graph rather than the proof's contracted graph. At preparation it reported `CHECKS_OK triples=13750; forests_extended=6635; larger_random=1000`. It compares every \(0\le a<22\), \(1\le b-a\le25\), \(1\le c-b\le25\), as well as 1,000 seeded larger triples. It checks one forest-preserving new-support edge-sum at \(2c+1\) whenever the predicted core is acyclic.

The code only tests finitely many instances. The general mathematical proof uses matching contraction, permutation cycles modulo the sum of two step sizes, component counting, and indefinitely repeatable leaf attachments. The infinite-word consequence invokes the published incidence-forest characterization, not a numerical experiment. Independent external mathematical validation was not performed.
