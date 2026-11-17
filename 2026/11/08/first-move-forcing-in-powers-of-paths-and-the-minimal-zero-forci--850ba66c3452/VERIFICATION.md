---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

PASS: Let a blue vertex v have exactly one white neighbor w. After v forces w the whole closed neighborhood N[v] is blue, a contiguous interval [max(1,v-k),min(n,v+k)] in P_n^k. From its right edge an appropriate vertex k-1 positions behind the frontier forces the next right vertex, and symmetrically from the left; extra initially blue vertices do not disrupt completion. Conversely any proper blue set with no legal first force is stalled. Thus every ZF set contains an oriented-edge trigger {v}∪(N(v)\{w}), and its inclusion-minimal sets are precisely the minimal such triggers. For squares, boundary degrees give four size-two sets, one/two size-three sets and three independent interior four-vertex pattern families of n-7 for n>=8, with explicit n=3..7 boundaries. Independent ordinary forcing simulation tested 16,324 initial masks over path powers k=1..4 and the complete minimal-trigger antichains of path squares n=3..14, exactly reproducing the submitted polynomial. Finite tests corroborate the general interval proof.

## originality

PASS

PASS (qualified): Nazari–Karimi Radpoor and later zero-forcing graph-power results establish the *minimum* Z(P_n^k)=k. The complete November 2, 2026 published Resultary theorem explicitly classifies exactly 2k minimum seeds on path powers (and optimum cycle seeds), but does not classify *all inclusion-minimal* configurations or when an arbitrary nonminimum set forces at time zero. Brimkov–Carlson's full original minimal-ZF paper treats general bounds and examples, not this path-power local first-move iff global-forcing law or P_n² exact minimal polynomial. Thus the stated all-power structural lemma and square minimal-set census remain separate from earlier minimum-set classifications.

## value

PASS

PASS: It is a structural conversion from iterative propagation to a single local trigger for an entire natural infinite graph family, with bounded-size local witnesses. The square polynomial exactly enumerates all inclusion-minimal labelled seeds, including sizes 3 and 4 not determined by the classical minimum number 2. Its eventual count 3n-15 is a natural complete classification, not an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
