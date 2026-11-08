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

The mathematical argument is contained in `RESULT.md`. Run `python3 verify_symbolic.py` to reproduce exact affine-interval identities for the full unbounded range \(k\ge2\). It establishes five residue-slice tables, proves strict modular separation of the three possible categories of triple involving periodic terms, and verifies a complete disjoint partition of the base interval. The run's actual output is in `symbolic_check.txt`.

Run `python3 verify_greedy.py` for a separately programmed direct greedy comparison. It independently compares the candidate with the greedy recurrence through \(12h\) for all \(k=2,\ldots,400\), through \(100h\) for eight parameters, and checks the explicit base complement against literal three-distinct-term sums for eleven parameters. Actual output is in `greedy_check.txt`. These finite checks are corroborating evidence only; the infinite proof uses the affine calculation.

The Python programs require only the standard library. The code works directly with integer arithmetic; it does not rely on randomization, external files, a proprietary solver, or a mathematical oracle. No independent mathematical audit has been carried out.
