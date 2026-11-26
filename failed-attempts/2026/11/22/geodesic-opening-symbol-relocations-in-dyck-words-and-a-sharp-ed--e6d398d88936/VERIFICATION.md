---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At fixed semilength a legal Dyck gap vector has nonnegative integer coordinates, total n and all prefix sums at least their prefix lengths. Each opening relocation changes one unit between coordinates, decreasing the positive surplus relative to the target by at most one. Any matching of all surplus to deficit units yields a legal path by doing all leftward transfers first: those only raise prefixes, and thereafter each prefix's excess over the target equals the count of outstanding rightward transfers crossing it. Donors are never overdrawn. The shared first opening gives distance at most n−1, attained by mountain versus alternating; since U_n is a subgraph of R_n, the upper bound carries over, and one arbitrary relocation cannot increase binary runs by more than two, giving a matching lower bound for that pair. For n=1 both are singletons. My independent replay constructs edges by shared same-symbol deletion traces (rather than enumerating insertion slots); BFS exhausts all 203455 ordered pairs in each graph for 1≤n≤7 and confirms the opening metric and both diameters. The universal claim is proved analytically, not by the finite test. Replay: python3 /workspace/checks/2.py. The informal frozen slogan's 'any two' is scoped by the theorem to equal semilength.

## originality

FAIL

The central exact opening-only metric is covered by a direct discrete-polymatroid base-exchange specialization. This is a demonstrated implication, not a judgment from a title, an inaccessible source, or the mistaken ordinary Catalan-matroid encoding. With that metric the two sharp diameters are immediate from the first gap and the mountain/alternating witness, using the elementary run-count or unchanged-subsequence bound for either-symbol moves. No separately substantial unexplained remainder in the frozen claim was identified. This does not assert that a previous paper printed the identical Dyck wording.

## value

FAIL

Dyck routing is a natural setting and the proof is a useful elementary illustration. However the exact opening metric is mechanically available from established augmentation/exchange for a single suffix chain. The worst-case diameters then use the mandatory first up step and one elementary extremal pair. The frozen claim does not isolate a separate independently useful structural theorem or unknown invariant beyond these routine deductions. The correct two-phase proof is not, as stated, a substantively different result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
