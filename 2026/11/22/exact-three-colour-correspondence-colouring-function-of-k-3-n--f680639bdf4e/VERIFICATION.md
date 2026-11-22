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

# Verification of the exact three-fold DP colour function

The stand-alone `verify.cpp` program generates all 36 ordered pairs of permutations of three symbols, fixes one identity pair and traverses all weakly increasing remaining tuples. For each candidate it evaluates the exact 27-assignment integer product count, records a minimum, and checks the explicit attaining cover by direct independent-transversal enumeration. It verifies the six proposed leaf types block all 27 left-colour triples. The separately written `verify.py` program carries out the same finite search using an independent implementation.

Run `g++ -std=c++17 -O2 verify.cpp -o verify && ./verify` and `python3 verify.py`. Both emit `VERIFY_OK` after checking minima `24,18,14,6,5,0` at right-shore lengths one through six. The exact numbers of normalized cases examined by each program are `1,36,666,8436,82251,658008`. The C++ program additionally tests all six witnesses directly and the symbolic obstruction's finite residue-condition premise.

The computations are exhaustive over n<=6 because the label normalization is mathematically complete; they do not prove the unbounded n>=6 case, which follows independently from the six-type cyclic-shift argument in RESULT.md. This is a reproducible finite-plus-symbolic proof, not an independent external audit. An earlier unindexed published exact table remains a possible originality limitation.
