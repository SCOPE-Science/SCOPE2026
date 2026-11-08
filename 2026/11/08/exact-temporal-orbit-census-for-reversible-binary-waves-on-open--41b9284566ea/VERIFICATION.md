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

# Reproducibility and proof limits

The theorem is proved for all integers \(n\ge2\), \(t\ge1\) by (1) the exact characteristic polynomial, (2) geometric multiplicity one, (3) a cyclic-module kernel degree identity, and (4) root multiplicities in characteristic two. These are algebraic steps; no finite experiment certifies the infinite range by itself.

Included `direct_matrix_check.py` constructs the update matrix over binary vectors and checks the predicted nullity of \(M_n^t-I\) for 1,116 pairs (all \(n=2,\ldots,32\) and \(t=1,\ldots,2(n+1)\)). It additionally checks that the matrix has order exactly \(2(n+1)\) for all 31 lengths. The output is in `direct_matrix_check.txt`.

Included `orbit_enumeration_check.py` directly classifies every labelled paired-row state, without the matrix nullity implementation, for each \(n=2,\ldots,8\), totaling 87,376 configurations over seven sizes. It checks 33 fixed-point and primitive-orbit divisor cases using independent trajectory classification. The output is in `orbit_enumeration_check.txt`.

Both programs use only the Python standard library. Neither requires network access or external datasets. Their captured output is supplied as scientific corroboration; independent auditing remains unperformed.
