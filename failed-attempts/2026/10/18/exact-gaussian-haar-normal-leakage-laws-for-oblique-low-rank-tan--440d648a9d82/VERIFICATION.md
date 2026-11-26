---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

FAIL

The universally defined Haar factor in RESULT.md lines 29–35 omits the admissible case ell=r and d=r+1: it is not full, not in the finite partial range, and fails the written condition r<=ell<=r+1<d. Step 4 repeats this restriction. This is an undefined branch of the claimed law, not a counterexample to the other displayed values. In the missing case the true value is infinity: for d=2,r=ell=1 and U=e_1, Haar gives A=tan(theta) for a uniform row angle modulo pi, whose square has infinite integral. More generally, conditioning on G in the Haar-frame trace identity gives (d-ell) tr[(G^T G)^(-1)] for all partial Haar counts; each inverse-Wishart diagonal is the reciprocal of a chi-square with ell-r+1 degrees of freedom by projecting one independent Gaussian column off the others, hence a divergent mean here. The correct partial-Haar infinite range requires ell<d and ell<=r+1, with neither restriction implying the other. Full Haar remains identically zero. I checked the remaining algebra: with C the normal coordinate block, squared leakage equals ||AC||^2+||CB^T||^2+||ACB^T||^2; independence and isotropy give the stated finite law, while an infinite one-sided contribution suffices on every fixed C!=0. The three bounds are simultaneously attained with C an outer product of top right singular vectors. The bundled CHECK.py factor helper orders the branches correctly but its listed cases do not test partial Haar with ell=r=d-1; the finite samples cannot establish the boundary.

## originality

FAIL

Epperly–Webber already give both exact one-sided factors for arbitrary rank, not just the Gaussian or rank-one case. The stated finite two-sided mean is a direct product of their two known identities applied to the normal coordinates of Carrel–Grigori's projector. The realized supremum is the elementary top eigenvalue of the same tensor-product Gram, minus one. The cited inverse-moment mechanism also gives the moment boundary by the standard reciprocal-Wishart test. This decision is about directly implied scientific content, not a claim that the exact two-sided wording appears in the source.

## value

FAIL

Normal contamination is relevant to sketch-based low-rank integration, but the central quantitative claim is a direct conditioning/tensor product of exact known least-squares means for the known projector. The realized bound likewise reduces immediately to the norm of two stacked matrices, with a rank-one tensor maximizer. Correcting the missing Haar branch would make a sound exposition, but would not supply an independent valuable result; no repaired finding is proposed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
