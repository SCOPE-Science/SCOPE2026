---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The frozen statement is for unlabeled packings as concepts on the 56-element spread universe. An independent exact-cover search using the nonzero binary vectors reconstructed 35 lines, 56 spreads and 240 packings: at either cover level selecting a block through the least remaining element enumerates every cover. Reproduction recovered compatible counts 56,840,4200,7560,5040 for k=1,…,5, with multiplicities 30,6,2, then 6720 single and 840 double completions, then all single. This supplies all trace estimates: for a four-set the three-positive pattern always fails if both triple completions contain the fourth spread and always exists if only one does. For each pair or singleton inside a compatible four-set, a union bound on completions involving forbidden spreads is smaller than the number of completions of the required positives, and the all-negative trace exists since 4·30<240. The same argument works on smaller compatible supports. Incompatibility loses the all-positive pattern. A shattered five-set would have a shattered four-subset whose unique completion already contains the fifth spread, which is impossible. Each compatible triple extends to a unique-completion quartet by taking a spread present in only one of its two completions, giving purity. The independent enumeration also compared direct trace masks on all compatible supports through k=5 and traversed the linear group action, recovering order 20160 and the orbit sizes 3360,3360 and 840. Replay: /workspace/branches/c833c554-25e5-4075-bddf-16a10a351f4c/reproduce.py and reproduction.log; supplied verify.py, symmetry.py and verify_fano.py were inspected, not executed. The finite result is exhaustive on this space, with no inference for other field sizes.

## originality

PASS

Credit the packing universe, its two packing orbits, the labelled Fano encoding, and the reported prior overlap count. The supported distinct claim concerns the complete eight-label packing trace complex, including its unique-completion criterion and exact orbit decomposition on supports, not the census of packings. The nearest other trace result has substantial related incidence structure but uses a different concept family and does not determine these traces by relabeling or parameter substitution.

## value

PASS

A natural incidence concept class receives a complete local characterization, not just a numerical VC dimension. The criterion tells exactly when positive constraints force a forbidden spread, explains purity, and identifies two geometric facet types tied to distinct packing types. This makes the result a useful exact benchmark for trace questions on packing designs rather than a recomputation of the known packing census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
