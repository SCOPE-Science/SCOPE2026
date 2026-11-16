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

# Exact checks

Execute `python checker.py` with Python 3.9 or newer. No external packages, network access, or random nondeterminism are needed: the pseudorandom comparisons use a fixed integer seed. The checker separately enumerates all triangulations for small polygons and compares their direct signed sums against the interval recurrence, evaluates every heptagon Walsh coefficient by an integer butterfly transform, checks the explicit 15-vertex frequency and its signed subfamily counts, and probes the infinite assertions in bounded dimensions using only integer arithmetic.

The exact replay marker is `TRIANGULATION_WALSH_EXACT_PASS`. A successful finite replay does not prove the infinite theorems; the recurrence, formal-series solution, Catalan parity, and congruence arguments are supplied in `RESULT.md`. There has been no independent audit.
