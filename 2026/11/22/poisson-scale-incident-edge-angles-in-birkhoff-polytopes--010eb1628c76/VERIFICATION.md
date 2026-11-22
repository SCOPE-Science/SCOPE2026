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

# Reproduction and boundaries

Run `python3 check_birkhoff_angles.py` using Python 3.10+ with only the standard library. The script enumerates all nonidentity single-cycle permutations for four small orders, computes pairwise Frobenius products directly and through trace identities, checks exact conditional factorial-moment identities over every available fixed-set conditioning, and reports deterministic Monte Carlo sanity checks for the asymptotic triple. The expected final marker is `BIRKHOFF_LOCAL_ANGLE_EXACT_PASS`.

The exact small-order counts are: \(n=3\): 5 neighbors, 25 ordered pairs; \(n=4\): 20, 400; \(n=5\): 84, 7,056; \(n=6\): 409, 167,281. These computations independently check finite implications of the proof and the specified metric; they cannot establish a limit theorem. The proof of the all-orders result is the moment argument in RESULT.md, especially the fact that a proper subset of edges of one directed cycle is a disjoint union of paths.

No extra packages, downloaded corpora, externally maintained files, hidden dependencies, or private datasets are required. The only scientific sources cited are public primary papers. The resulting argument has not undergone independent audit.
