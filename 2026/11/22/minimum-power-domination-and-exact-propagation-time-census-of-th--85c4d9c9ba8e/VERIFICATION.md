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

Two independent full-set checkers are included: `census_pentagons.cpp` generates the pentagon–pentagram graph, and `census_fano.cpp` generates the Fano-plane/triple graph. Each applies the standard synchronous propagation rule to every six-subset; both also exhaust the five-subsets (and the first checks all smaller cardinalities). Each reproduces the eight count cells in `COUNTS.tsv`; neither samples or prunes six-sets.

Commands:

```sh
g++ -O3 -std=c++17 census_pentagons.cpp -o a
./a > a.out
g++ -O3 -std=c++17 census_fano.cpp -o b
./b > b.out
diff -u a.out b.out
```

The table contains \(2{,}329{,}950\) successful six-subsets out of \(15{,}890{,}700\), and every five-subset fails. This certificate is finite and computational, not a formal proof in a theorem prover. The exact induced-edge and round histograms apply only to the stated graph and convention.
