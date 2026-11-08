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

# Verification and limits

The included `verify.py` uses only the standard Python library. It constructs the vertex set of \(KG(n,2)\) from the two-element subsets of \([n]\), constructs every adjacency independently using disjointness, enumerates every candidate subset for \(n=4,5,6,7\), and tests induced degrees, plus maximality by attempted addition of each missing vertex. It compares the entire resulting coefficient vectors to both claimed polynomials. The exact number of examined subsets is
\[
2^{\binom42}+2^{\binom52}+2^{\binom62}+2^{\binom72}=2,131,008.
\]
There are 2,823 dissociation sets and 74 inclusion-maximal dissociation sets over these four orders. The output expected after an ordinary run is:

```text
VERIFY_OK full_orders=4..7 subsets=2131008 dissociation_sets=2823 maximal_sets=74 polynomials=PASS structural_families=PASS generated_orders=8..12 generated_maximal_sets=1281
```

Additionally, for \(n=8,9,10,11,12\), the verifier independently builds every proposed complete-star and four-support maximal set, tests it against the graph's adjacency, and checks that its count is \(\binom n4+n\). This last check is **not** an exhaustive search of all subsets for those orders. All finite checks agree with the proof; the infinite statement is established by the structural dichotomy and maximality arguments in `RESULT.md`, not by extrapolation. There is no external mathematical certification or independent audit.
