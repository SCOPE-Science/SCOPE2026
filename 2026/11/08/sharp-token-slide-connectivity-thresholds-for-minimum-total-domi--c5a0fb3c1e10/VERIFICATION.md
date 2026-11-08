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

The proof in `RESULT.md` establishes the theorem for every integer \(m,n\ge3\). The two runnable Python scripts independently test finite instances and the legal slide templates. Execute `python3 direct_check.py` and `python3 matching_check.py` from this directory; compare their standard output with `direct_check.out` and `matching_check.out`.

`direct_check.py` constructs the original categorical-product adjacency relation, proves the tested minimum is three by checking all pairs, enumerates every triple and tests open total domination at each vertex, then independently creates both reconfiguration graphs. `matching_check.py` bypasses graph domination and generates all three-edge partial bipartite matchings, builds simultaneous-free-endpoint moves, enumerates components, and checks the finite template certificates. The programs require only the Python standard library.

Important limits: verification through finite \((m,n)\) values is not a proof of the parameter-uniform claim; the infinite proof uses the three explicit transposition templates, whose legal intermediate states are separately checked. The original numerical total domination number belongs to prior work. These checks have not undergone independent external audit.
