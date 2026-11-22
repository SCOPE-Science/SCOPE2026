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

# Reproducing the finite Desargues classification

The graph is defined by two copies of the ten two-subsets of \([5]\), adjacent precisely for disjoint pairs on opposite shores. Indices \(0,\ldots,9\) and \(10,\ldots,19\) use lexicographically ordered pairs \(01,02,03,04,12,13,14,23,24,34\). This construction is internal to both programs: there are no graph-data downloads or random inputs.

Run these standalone source files in the same directory:

```sh
g++ -std=c++17 -O3 desargues_enum.cpp -o desargues_enum
./desargues_enum > direct_counts.txt
python3 desargues_verify.py
```

The first three output lines of the C++ program must be:

```text
all 1 20 190 1080 3985 9784 15910 16600 10390 3460 564 60 5 0 0 0 0 0 0 0 0
maximal 0 0 0 0 0 0 0 0 65 540 234 0 5 0 0 0 0 0 0 0 0
maximal_count 844
```

The C++ output then lists the \(844\) maximal bitmasks, one per line. The Python program independently prints the identical face/facet histograms, exactly twelve natural \(S_5\times C_2\) orbits with representatives and orbit sizes, `UNIQUE_EXTENSION_11_TO_12 60`, and `PASS`.

The representative table `ORBIT_REPS.tsv` records all twelve orbit representatives, orbit sizes, shore sizes and induced-edge counts. In particular the five size-twelve facets are the two-shore copies of the six pairs in \(\binom{[5]\setminus\{a\}}2\), for each \(a\in[5]\). Each eleven-vertex dissociation set is contained in exactly one such facet.

**Why the programs are exhaustive:** the C++ checker iterates over every twenty-bit mask and directly tests all selected vertices for induced degree at most one, then tests every possible one-bit extension. The Python checker instead builds a membership Boolean table by induction on the least selected bit and uses that table to decide maximality. Since dissociation is hereditary, a valid set has a valid proper extension exactly when it has a valid one-bit extension. Both implementations have finite upper bounds fixed by the twenty-vertex graph. The orbit action uses all \(5!\) label permutations and both shore flips, acting by graph automorphisms. Orbit representatives from all \(844\) facets are therefore exhaustive under this explicitly stated group.

**Unproved limits:** these computations prove nothing about graphs of larger order or arbitrary \(H(n,k)\); absolute priority over inaccessible historical publications is not a mathematical consequence of the enumeration.
