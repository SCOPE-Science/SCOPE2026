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

Run `python3 verify.py` using the Python standard library. The program prints `DERANGEMENT_VERIFY_OK` after all checks. It constructs all matrices in \(\operatorname{GL}_r(2)\) for \(1\le r\le4\), checks the exact kernel-dimension mixture against Gaussian binomial inversion, and independently checks all \(8\) quandle automorphisms at rank one and all \(6144\) quandle automorphisms at rank two against the entire multiplication table, including their fixed-point histograms. It confirms the rank-two distribution \((2769,2048,768,492,54,12,1)\) indexed by \((0,1,2,4,8,12,16)\).

The exact symbolic proofs in `RESULT.md`, not the finite checker, justify every rank and the asymptotic limit. Computation does not certify bibliographic priority, independence, or any external review. The full text of Hou's 2011 article was unavailable; its abstract was inspected as a relevant stronger automorphism-classification source.
