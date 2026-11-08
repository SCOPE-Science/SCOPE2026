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

# Verification and reproducibility

Run `python3 verify.py` in the same directory as this document; no nonstandard Python packages are required. The verifier directly builds vertices of \(K_2\square K_b\square K_n\), computes pairwise Hamming distances, and enumerates exact-distance-two independent sets without relying on the combinatorial decomposition. It separately evaluates the published polynomial by integer polynomial arithmetic and compares the full coefficient arrays.

Checked dimension pairs are \((2,2),(2,3),(2,4),(3,3),(3,4),(4,4),(3,5),(5,3),(4,5),(5,4),(2,6)\). In addition, the literal total-visibility definition is tested against all \(256\) vertex subsets of \(K_2\square K_2\square K_2\) and all \(4096\) subsets of \(K_2\square K_2\square K_3\), using shortest paths in the induced remaining-vertex search, retaining both requested endpoints. The code checks the proposed highest-degree coefficients independently for all parameter pairs in the enumerated list.

Recorded output ends in `VERIFY_OK profiles 11 full_literal_subsets 4352 classification_and_polynomial=PASS unrestricted_proof_not_replaced_by_finite_check`. These checks are finite corroboration, not a proof for arbitrary parameters. The unrestricted claim follows from the distance-two lemma, layer classification, and elementary case enumeration in RESULT.md. Independent mathematical audit has not been performed.
