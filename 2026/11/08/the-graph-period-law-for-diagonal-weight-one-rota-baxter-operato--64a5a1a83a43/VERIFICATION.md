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

# Verification of the graph-period law

The attached `verify.py` is standalone Python using only the standard library. Execute `python3 verify.py` from the directory containing this file.

It enumerates **all** directed graphs with up to three labeled vertices and at least one edge, filters them by strong connectivity, and computes the gcd of edge-level discrepancies to obtain their period. For each graph, it exhaustively checks every diagonal coefficient assignment in the fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_8\). The binary extension fields are represented by polynomial bases with the irreducible moduli `0b111` and `0b1011`, respectively. All arithmetic and assertions are exact.

For each tested assignment, the code evaluates the weight-one coefficient equation on every graph edge and compares the exact solution count with \(1+\gcd(2^d-1,q-1)\). The finite tests comprise 894 graph/field configurations, 5,118 total tested directed edges across configurations, and 156,329 exact operator assignments. An independent simple-cycle enumerator also cross-checks the graph-period algorithm, and the directed three-cycle gains one reverse edge over \(\mathbb F_8\), collapsing eight diagonal operators to two. The final 256 assignments evaluate the actual weighted multiplication coefficients in a non-monomial perfect four-dimensional example over \(\mathbb F_4\) and check that precisely four diagonal solutions, including two nonconstant ones, occur.

Actual recorded output (`verification_output.txt`):

```
VERIFY_OK configurations=894 tested_directed_edges=5118 maps=156329 dense_perfect_example=4
SIMPLE_CYCLE_CASES [(1, 4, 1, 2), (1, 8, 1, 2), (2, 4, 2, 4), (2, 8, 2, 2), (3, 4, 3, 2), (3, 8, 3, 8)]
EDGE_COLLAPSE_GF8 [(3, 8), (1, 2)]
```

**Logical status:** finite enumeration is not an infinite theorem. The complete claim follows instead from the coefficient-equation reduction, the squaring conjugacy, the closed-walk period argument, and construction of every root-of-unity solution as given in `RESULT.md`. The checker does not test off-diagonal operators or all fields and dimensions.
