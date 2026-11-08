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

The proof of the unrestricted theorem is in `RESULT.md`, using affine-span dependence, explicit linear-functional separation of an independent support, a linear-subspace positive-branch induction, and exact ordered-tuple counting.

`verify_affine_flats.py` uses only the Python standard library. To replay locally, run `python3 verify_affine_flats.py`. Its output was captured in `verification_output.txt`. It directly enumerates the concepts and point traces and independently tests affine rank by elimination; the small cases also compute exact Littlestone dimension by recursion. The \(q=4\) case uses explicit arithmetic in \(\mathbb F_2[u]/(u^2+u+1)\). In cases with more than 27 points the script limits higher-cardinality support enumeration and explicitly labels which Littlestone dimensions it did not compute. The finite checks are corroboration, not an infinite proof.

The cited 2022 paper gives a pre-existing affine-subspace online dimension in a different setting. The numerical combinatorial count can also be expressed as an established affine-matroid rank count. The narrow relationship between fixed-rank membership shattering and affine-matroid independence is the claimed interpretation. An independent audit has not been performed.
