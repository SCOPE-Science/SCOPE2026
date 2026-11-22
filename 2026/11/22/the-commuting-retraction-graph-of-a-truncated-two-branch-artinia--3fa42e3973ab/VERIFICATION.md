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

# Verification

Run `python verify.py` in a directory containing this file and `verify.py`. It enumerates all unital algebra homomorphisms via images of \(x,y\) in the maximal ideal, enforcing the original relations \(x^2=xy=y^N=0\), and tests composition-idempotence on both generators.

The script independently generates both asserted normal-form families, compares the complete sets, computes exact linear image ranks, enumerates every unordered pair of distinct nontrivial retractions to test composition commutation, verifies degree at most one and the number of edges/isolates, and checks the ordered commuting-pair expression including augmentation and identity. It uses elementary prime fields and the independently implemented \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\). Tested pairs \((q,N)\) are \((2,3),(3,3),(4,3),(5,3),(2,4),(3,4),(2,5),(2,6)\).

`verification_output.txt` contains the captured successful run, concluding `TRUNCATED_BRANCH_RETRACTION_GRAPH_VERIFIED`.

The finite enumeration does not prove the field-uniform or dimension-uniform conclusions; the proof of those claims is in `RESULT.md`. The results do not certify any unpublished priorities or provide an independent audit.
