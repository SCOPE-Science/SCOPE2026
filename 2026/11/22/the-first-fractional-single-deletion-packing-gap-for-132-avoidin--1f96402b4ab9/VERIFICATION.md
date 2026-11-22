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

The standalone `verify.py` checker was run from its actual directory with the included `LP_CERTIFICATE.json` and printed `VERIFY_OK`. For each source length \(1\le n\le6\), it independently generates all \(132\)-avoiding permutations by Catalan decomposition and by filtering all permutations; computes every rank-standardized deletion set; and executes exhaustive compatibility-graph clique branch-and-bound with a proved proper-color bound. It checks a concrete thirteen-word code and exact rational primal/dual linear-programming certificates. For length six it enumerates 132 sources, 42 distinct observation words, and 50,809 search nodes, attaining exact integer optimum 13 and exact fractional optimum \(4434/308=2217/154\).

A supplementary mixed-integer optimizer returned integer optimum 13 on the 132-source, 1,995-conflict-edge formulation. This is corroboration, not needed for the complete finite proof. The checker does not claim a general-\(n\) theorem, exhaustive literature coverage, or independent mathematical validation.
