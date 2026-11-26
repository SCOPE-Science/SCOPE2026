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

The images of any two distinct domain points determine the orientation and offset. Distances to those two points then determine every other image. Each sign has one support of length n and two at each shorter positive length; adding the n² singletons and the empty map separately to the at-least-two restrictions gives 6·2^n−n²−4n−5. All partial identities commute, giving exactly 4^n ordered idempotent pairs. A support of size less than 3n/4 provides at most 2^(3n/4) restrictions per affine type, so short maps or rank ≤1 contribute pair probability O(n·2^(−n/4)). For two long types f,g, choose g nonidentity. The intersection of the image of its support with the admissible support of f has size ≥n/2, losing at most one source to a fixed point. From the remaining arrows x→g(x), take a vertex-disjoint set of size ≥(n/2−1)/3: translations give paths and reflections give two-cycles. At each selected arrow, x∈B, g(x)∈A, x∉A forces the two product domains to differ. These events are independent, each of probability at least 1/8 without conditioning on rank (including x outside the support of f). Conditioning on both ranks ≥2 costs at most a factor of four for n≥8, and the estimate is uniform across long types. This proves the quantitative bound. Both exponential bases and the normalization correction are absorbed by O(0.99^n); the positive limit implies conditional concentration. An independently written enumeration found 31, 204, 1089, 5104, 21021, 81210 commuting pairs for n=2,…,7, confirming the frozen finite data only; the supplied script was inspected, not executed.

## originality

FAIL

The distinct indexed record 2523a33ab907 already documents the headline statement on the exact same full monoid: the limit 1/36 with exponential convergence and conditional dominance of pairs of partial identities. This is statement-level coverage, not a finding about priority between records on the same date. Its exact mixed commuting count is additional. The frozen two-term error estimate gives a somewhat better explicit nonoptimal base than the example bound in 2523a33ab907 (about 0.978 versus 0.986, before polynomial factors); the headline O(0.99^n) already follows from that record. The modest quantitative improvement comes from the support cutoff and localized domain witnesses in the same affine-representative framework; it identifies neither a sharp rate nor a new asymptotic term and does not support a standalone valuable repair.

## value

PASS

As a mathematical question the full-monoid law is substantive: reflections are not a negligible exceptional family, and their interaction with arbitrary partial domains is not addressed by counting elements or by translation-only models. The proof identifies a mechanism forcing almost all commuting pairs to come from two partial identities. This value of the main result does not make it distinct from the overlapping record or make the change to the nonoptimal bound a valuable separate finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
