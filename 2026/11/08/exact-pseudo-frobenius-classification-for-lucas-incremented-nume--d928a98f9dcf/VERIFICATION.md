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

The Python verifier independently constructs numerical-semigroup Apéry sets with Dijkstra and checks each claimed pseudo-Frobenius element and absence of all others for \(3\le a\le17\). It separately generates candidate canonical digit sets from compositions into \(2\) and \(3\), confirms the exact type formula, and checks the two exceptional residues. Finite checks are a diagnostic for the symbolic proof, not its substitute.

Scientific limitations: arbitrary \(a\ge3\) is proved symbolically; no independent audit has been performed.
