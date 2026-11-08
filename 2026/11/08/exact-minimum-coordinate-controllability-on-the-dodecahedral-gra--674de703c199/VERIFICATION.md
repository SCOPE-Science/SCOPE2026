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

# Reproducibility

Execute `python3 verify.py` from the directory containing the file. Only Python 3 standard-library facilities are used.

The certificate reconstructs all 30 dodecahedral edges in a documented 20-vertex indexing, checks five independent exact adjacency eigenvectors of eigenvalue one, and verifies the integer polynomial identity for the antipodal involution. It builds the 120-element automorphism closure from three explicit graph automorphisms and its 60-element action on ten antipodal classes. Its eight computed orbits exhaust exactly 252 quotient five-subsets; five representative integer controllability matrices have rank twenty modulo eleven. For the three failed types it verifies displayed exact integral eigenvector obstructions. A second check independently constructs six adjacency eigenspaces over the field of eleven elements and verifies the PBH condition for every one of the 252 quotient five-subsets.

A successful run prints the eight orbit summaries and a concluding `PBH_FINITE_FIELD_ALL_252_OK ORBIT_CERTIFIED_8 MINIMUM_LEADERS_5 OPTIMAL_SETS_4224` line. These checks are exact and exhaustive for this finite graph; they do not prove any assertion for other graphs or yield an external independent review.
