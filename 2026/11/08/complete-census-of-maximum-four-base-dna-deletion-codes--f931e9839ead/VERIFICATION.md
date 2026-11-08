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

The codebook model is specified in `RESULT.md`. All scripts and data in this package are self-contained apart from a standard C++17 compiler and Python 3; neither needs an optimization solver or network access.

```
c++ -std=c++17 -O2 census.cpp -o census
./census > reconstructed_codebooks.tsv
python3 verify.py reconstructed_codebooks.tsv symmetry_representatives.tsv
python3 verify.py maximum_codebooks.tsv symmetry_representatives.tsv
```

Observed: `ORBIT_CANDIDATES=120; SIZE_12_SETS=0; MAXIMUM_CODEBOOKS=44` and two `INDEPENDENT_VERIFICATION_OK 44 maxima; 9 symmetry classes; compulsory pairs AAAA,CCCC` lines. The C++ recursion's candidate-set invariant and color upper bound make the search exhaustive. The Python script separately constructs the deletion graph and enumerates maximal cliques using a different search algorithm, then tests exact set equality with the 44-row certificate.

The eleven entries on each codebook line are the canonical lexicographically smaller words in the reverse-complement pairs. Expanding each entry with its reverse complement gives all 22 labeled strands. The optional representative file reports all nine group orbits. A published 22-strand example appears among the 44 certified codebooks.

These checks prove the finite enumerative assertion only within the mathematical model. They do not prove literature priority, biological suitability, or any statement about larger blocklengths. Independent scientific review was not performed.
