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

# Verification record

Run `python3 verify.py` in the directory containing `verify.py` and `checks.json`. The script has no third-party dependencies. Its JSON stdout is exactly the supplied `checks.json` when run with Python 3 on the same files. The complete script verifies all seven distinct distance-three edges, the seven maximal cliques, the two possible triangle witnesses for every remaining edge, absence of nested closed neighborhoods, all 128 optional-incidence subsets, connectivity and graph cycle rank for each of the 29 valid subsets, and all 14 dihedral automorphisms of the distinguished seven-vertex graph. A repeat run of this exact package was successful.

These checks exhaust the **finite combinatorial enumeration**, not arbitrary topologies. The unrestricted topological lower bound and equality rigidity are supplied by the written proof in `RESULT.md`; McCord's standard theorem supplies the asserted weak equivalence. The previously established edge clique cover number of the seven-antihole is explicitly credited. Independent mathematical validation and comprehensive historical priority verification have not been carried out.
