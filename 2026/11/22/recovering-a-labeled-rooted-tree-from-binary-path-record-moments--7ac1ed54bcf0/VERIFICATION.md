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

The proof uses independent relative insertion ranks for records on a single path, a two-dimensional exact integral for incomparable vertices, and Hoeffding's inequality with a union bound for all empirical moments.

`python3 verify.py` runs using only the Python standard library. It checks exact rational population formulas and reconstruction through exhaustive rooted labeled trees of sizes 2–5, 24 seeded size-6 instances with all label orders, and 1,060 seeded instances on sizes 2–54 with symbolic moments. The observed output was `PASS: 630088 exact assertions, including every rooted labeled tree with root 0, n<=5; seeded n=6 and larger tests`.

The numerical finite check is not a substitute for the proof for arbitrary size or an independent expert review. The replication bound is sufficient but not asserted optimal. The classical antecedent on random tree records is credited; historical priority of the inverse result is qualified.
