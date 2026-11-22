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

Execute `python3 verify.py` with a standard Python 3 installation; no external packages, network, or data are required. The script independently builds each blowup graph, enumerates all nonempty faces from graph adjacency and common-neighbor counts, constructs its maximal facets, calculates mod-two simplicial homology with exact binary elimination, and compares the predicted weighted-incidence graph's component and cycle counts. It exhausts connected labeled graphs without a four-cycle through five vertices under unit weights, tests selected heterogeneous variants, and includes the Petersen, Heawood and heterogeneous cycle graphs. The recorded successful run checks 339 graph instances and 1,481 filtration stages. A four-cycle negative control distinguishes the asserted scope.

The checker does not verify the abstract functorial nerve lemma or compute integral Smith normal forms; those statements are justified by the elementary-cover proof and the fact that the model is a graph. Finite rank agreement alone does not establish the general theorem or persistence-map naturality. No independent scientific audit has been performed.
