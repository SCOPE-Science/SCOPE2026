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

# Finite verification

The attached `verify_p_first.py` and `verify_q_first.cpp` reconstruct the two thirteen-point designs from the precise starter triples and Pasch trade. They first verify the Steiner axioms, notably exactly one occurrence for each of the 78 unordered point pairs. They use the necessary-and-sufficient domination predicate from `RESULT.md` and exhaust all candidate nine-vertex sets with five, six or seven point vertices.

`verify_p_first.py` enumerates point subsets before choosing block subsets, whereas `verify_q_first.cpp` independently chooses block subsets first and tests each eligible point subset. Each computes the 39-bit encoding of every candidate and the one-for-one-replacement graph. Both programs must agree exactly on all 1,456 cyclic states and all 1,511 switched states. In addition to matching cardinality, their complete sorted state lists were compared as sets and showed no mismatch. The Python program emits SHA-256 identifiers for canonically sorted state masks; these checksums are included in `RESULT.md`.

Run the two programs as follows:

```sh
python3 verify_p_first.py
g++ -std=c++17 -O2 verify_q_first.cpp -o verify_q_first
./verify_q_first | grep -v '^@'
```

The C++ program additionally checks that **no** eight-vertex solution of the only possible point/block profile can dominate. The symbolic proof excludes all other profiles and establishes the bound independently. The two programs independently find the exact state counts, canonical-status distributions, undirected exchange-edge totals, and component-size multiplicities reported in `RESULT.md`. The C++ program's `@` lines list its complete state encodings for an optional cross-implementation comparison.

**Limits.** This is an exhaustive finite certificate for two explicit 39-vertex graphs, not a black-box test of arbitrary Steiner systems. The numerical claims should not be inferred outside the stated domain. An independent scholarly review has not been performed.
