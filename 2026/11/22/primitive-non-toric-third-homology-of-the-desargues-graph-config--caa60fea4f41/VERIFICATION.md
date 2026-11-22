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

The exact certificate comprises `desargues_certificate.json` and the standard-library Python program `VERIFY.py`. Both files are supplied in this record. Run `python3 VERIFY.py` from the directory containing the files.

Checked against the actual packaged files: the degree-three and degree-two reduced chain groups have ranks 9,120 and 22,800; the prescribed 9,099 columns are independent modulo three; the full degree-three boundary has mod-two rank 9,094; and each of twenty-one integral chains has zero boundary and a distinct unit free coordinate. Exhaustive simple-cycle search produces 1,456 cycles and exactly twenty disjoint triples, each of three hexagons. All twenty product torus chains close integrally, and a specified 20-by-20 coefficient minor has exact determinant +1.

The topological chain-model comparison is a published theorem, not independently reproved. The finite calculation determines the stated third homology and primitive torus quotient. The universal coefficient theorem determines the two-torsion subgroup in second homology, but not the exponents of larger two-primary cyclic summands. No external mathematical audit or publication-priority certification is asserted.
