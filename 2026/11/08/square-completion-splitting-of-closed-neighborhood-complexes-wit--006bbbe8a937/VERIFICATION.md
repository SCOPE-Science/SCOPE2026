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
# Computational reproducibility

Run `python3 verify.py` with a standard Python 3 interpreter; its exact captured output is included as `verify_output.txt`. The program creates the closed-neighborhood simplices, executes the proposed free-face collapse, verifies that each face has exactly one proper remaining coface (including all higher-dimensional cofaces), then independently rebuilds the graph with tetrahedral square boundaries and compares exact face sets. It also checks uniqueness of square diagonals and reduced mod-two homology for named examples. Results include all 606 eligible pseudorandom test graphs, 334 correctly rejected inputs, and exact checks on eleven named graph families/parameters, including the Grötzsch graph.

The test result is `ALL_VERIFY_OK`. Klein grids of sizes five-by-five and six-by-five have reduced mod-two Betti numbers \((2,26)\) and \((2,31)\) in dimensions one and two, respectively. Field calculations alone cannot establish integral torsion; that part follows from the Klein bottle's standard fundamental polygon proof in `RESULT.md`. Random testing and other finite examples are corroboration only. The universal homotopy statement relies on the explicit theorem proof and standard CW-cell attachment facts. Independent mathematical validation was not performed.
