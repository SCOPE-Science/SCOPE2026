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

The arithmetic census is checked by two exact finite computations. Execute `python3 verify_orbits.py` and `python3 verify_direct.py` from the supplied files' directory. Both programs require only Python's standard library.

`verify_orbits.py` reconstructs the complete 240 classes from the seven classical degree patterns; checks exceptional-class intersection equations, the 240-by-240 pair distribution, and all 22 eight-point cycle partitions; and counts invariant triples by their Frobenius orbit decompositions.

`verify_direct.py` independently obtains the same 240 classes by solving bounded integral exceptional-class equations, constructs all disjoint triples explicitly, and tests 22 Frobenius permutations on all 60,480 triple sets directly. The programs compare against a full explicit table and assert the sharp \((5,3)\) versus \((7,1)\) pair/triple distinction.

A finite case enumeration proves a statement about all 22 possible octad cycle partitions because every Frobenius action on eight geometric points has one of these cycle types. It does not establish that every type is realized over any fixed finite field, nor does it replace the classical classification of the 240 geometric exceptional curves. Independent external verification has not been performed.
