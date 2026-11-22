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

# Reproducible checks

The attached `verify_latin.py` enumerates the \(3\times3\) Latin squares by independent row permutations and column checks, then enumerates all candidate query supports of sizes zero through four. It computes the 270-by-216 mod-two edge–triangle boundary matrix and eliminates it using integer XOR operations. It additionally enumerates the 576 order-four Latin squares and checks every one of the 25,920 compatible three-query supports.

The attached `verify_latin.cpp` generates the order-three Latin squares instead as coordinate isotopes of the cyclic addition table, deduplicates them, and independently builds Boolean traces, facets, and the mod-two boundary matrix. It uses exact `std::bitset` row reductions.

Commands from the directory containing the two files:

```sh
python3 verify_latin.py
g++ -std=c++17 -O2 verify_latin.cpp -o verify_latin
./verify_latin
```

The expected assertions are 12 order-three Latin squares, 576 order-four Latin squares, face vector \((1,27,270,216,0)\), 108 maximal pairs, 216 maximal triangles, boundary rank 133, reduced Betti ranks \((111,83)\), and 25,920 compatible and shattered order-four triples. Both programs were executed from their actual delivery contents before the present report was prepared.

The all-order statement is deductive and uses the published partial Latin completion theorem; the finite verifiers do not purport to certify infinitely many cases. The computation does not establish integral homology, homotopy type, or independent mathematical validation.
