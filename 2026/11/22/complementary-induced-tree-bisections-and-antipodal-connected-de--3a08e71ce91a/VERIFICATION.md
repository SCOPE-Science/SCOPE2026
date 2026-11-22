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

# Reproducibility and verification

The proof's nonstandard finite steps are wholly specified by the embedded programs; no external datasets, packages or network services are needed. `verify_fano.py` uses Python 3 with only its standard library, and `verify_hamilton.cpp` uses C++17 integer bitmasks.

Run:

```
python3 verify_fano.py
c++ -std=c++17 -O2 verify_hamilton.cpp -o verify_hamilton
./verify_hamilton
```

**Independent graph encodings.** The Python checker derives incidence from nonzero three-bit vectors and their dot products. The C++ checker builds a fourteen-cycle with seven alternating LCF chords. The Python checker verifies the complete vertex isomorphism, rather than assuming the representations agree.

**Finite coverage.** The Python checker enumerates all seven-subsets of fourteen vertices (3,432 total), rejects insufficient smaller connected feedback sets, evaluates exact induced edge/component counts, enumerates 336 incidence automorphisms, builds all 770 swap neighborhoods and performs 770 complete breadth-first distance searches. The C++ checker enumerates all 16,384 masks and independently computes all swap neighborhoods and all 770 shortest-path tables. Both calculate cardinalities and distances using exact integers, without optimization solvers, random trials, approximate tolerances or search timeouts.

Expected results from both: ordinary minimum feedback sets of cardinality four (70); connected minimum feedback sets of cardinality seven (770); 385 complement pairs; degree multiplicities \((16:378),(18:56),(20:336)\); 6,888 exchange edges; radius and diameter seven; exchange-distance counts \((1:6888),(2:39312),(3:97524),(4:104412),(5:40656),(6:6888),(7:385)\); 5,460 pairs one move beyond the Johnson lower bound. Python also verifies orbit sizes \((42,56,168,168,336)\) for the complete 336-automorphism group.

The elementary cubic lower bound is proved in the mathematical result. Executed exhaustive checks establish only this one finite graph's counts, not a theorem for all cubic graphs. The verifiers are independent implementations, not an independent external scientific audit.
