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

From this directory, execute:

```sh
g++ -O2 -std=c++17 verify_dodecahedron.cpp -o check_dodecahedron
./check_dodecahedron
python3 verify_dodecahedron.py
```

Both programs run solely from the displayed \(GP(10,2)\) edge formula. The C++ program checks the 295 maximal independent sets by enumeration of all \(2^{20}\) vertex subsets. The Python program builds the same family by an independent complement-clique recursion. Both verify the complete support shattering polynomial, all facet sizes and exact mod-two boundary ranks. The Python program separately counts the ten pairwise-distance-three tetrahedra and checks these are precisely the size-four facets.

Expected face vector by support size zero through six: \((1,20,160,660,1470,1572,310)\). Expected facet counts by sizes four through six: \((10,672,310)\). Expected ranks of augmented boundaries in face cardinalities one through six: \((1,19,141,519,941,305)\). Reduced mod-two Betti numbers in simplicial dimensions three, four, five: \((10,326,5)\).

Both implementations were compiled or executed on the extracted source content, with exact assertions passing. The verification is a finite mathematical computation, not an independent professional or institutional audit. No integral homology, homotopy equivalence, or absolute novelty is certified.
