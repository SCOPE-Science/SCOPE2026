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
# Reproduction

Use Python 3.9 or later. Run `python3 verify_cyclic_switches.py` from this directory. It requires only the standard library. The archived output is `verification_output.txt`; the final line must read `CYCLIC_SWITCH_CHECKS_PASS supports=23200`.

The checker performs direct enumeration of every \(n\)-bit cyclic word for \(3\le n\le11\), every feasible even \(k\), and every coordinate support, testing shattering independently of the proof's gap argument. It also directly checks the completion-polynomial coefficient for every support of size at most three, and runs a memoized exact Littlestone recursion through \(n=10\) for \(k=2\). The separate `depth4_certificate.json` contains an explicit 16-leaf, four-level adaptive tree on five cycle vertices. Read each node's `position` as a one-based coordinate query and its `zero` and `one` branches as the resulting bits; every leaf is a concrete feasible word consistent with its path. Its leaves and node choices were checked against all paths when generated.

The exact general statements are justified by the all-parameter proof in `RESULT.md`, not by these finite checks. This package does not constitute independent validation or a historical originality certificate.
