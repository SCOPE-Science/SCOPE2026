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

The proof is symbolic and applies to arbitrary finite transitive source actions; the standalone verifier tests two nonabelian cases independently. It enumerates the complete six-element permutation group for the three-source test, all assignments of nine target colors, and all their equivariance equations. It also constructs the full twenty-four-element permutation group, the two twelve-element ordered-pair orbits, and the fixed-source labels for each orbit stabilizer. It checks that the predicted nonempty cell counts are seven and eight respectively.

Run `python3 verify_nonabelian_hom.py`. The included `verification_output.txt` records its actual output. These finite checks cannot prove the theorem for arbitrary groups or target sets; that scope is covered by the explicit normalization and support-map proof. No independent audit has been performed.
