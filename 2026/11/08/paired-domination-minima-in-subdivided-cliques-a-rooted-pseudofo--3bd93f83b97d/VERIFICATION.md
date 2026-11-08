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

The proof reduces every minimum paired dominating set of the once-subdivided complete graph to a nontrivial rooted tree together with unicyclic components. The finite verification script `artifacts/verify.py` constructs incidence graphs directly, tests domination and matches all eligible selected original/subdivision vertex sets for \(2\le n\le7\). It compares exact perfect-matching multiplicities with \(2^c\) and matches the component-count generating polynomial coefficient-by-coefficient. The resulting initial distributions are \(A_2(y)=2\), \(A_3(y)=9\), \(A_4(y)=64\), \(A_5(y)=625+20y\), \(A_6(y)=7776+630y\), and \(A_7(y)=117649+16289y\).

The recurrence checks extend through \(n=30\). These are finite tests; they are not exhaustive verification for all \(n\). The general proof uses a vertex-cover obstruction, perfect-matching feasibility in incidence graphs, a component-edge count, and labelled tree and unicyclic graph enumeration.

No independent mathematical audit has been performed.
