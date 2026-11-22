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

# Reproducibility and scope of verification

Run `python3 verify.py` in the directory containing the bundled `nonproduct_cycle.json`. The program uses only Python 3's standard library, enumerates all 15,120 degree-three generators, applies the reduced Świątkowski differential, and obtains exact rank 14,991 modulo three. It builds every simple four-, six- and eight-cycle of the graph and all pairwise-disjoint cycle triples, verifying the counts 152, 576, 240 and 144. It verifies each geometric product's full signed integral boundary and computes exact rational rank 128 using fraction-free elimination. The 1,475-term integer witness has zero signed boundary and a nonzero exact rational remainder; its independent mod-three check is supplementary, not a substitute. Successful output is `Q4_THREE_PARTICLE_NONPRODUCT_H3_OK`.

The comparison with the actual topological configuration space depends on the published reduced Świątkowski comparison theorem. The calculation determines free ranks in degree three and the rational non-toric obstruction, not all quotient-lattice elementary divisors or the lower homology groups. No external independent audit is recorded.
