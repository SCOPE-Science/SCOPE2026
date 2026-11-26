---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS

The local inequalities are precisely the synchronous open-neighbor fixed-point rule with ties retained; at n=3 the horizontal neighbors are distinct. The pair-state overlap recovers the full cyclic column string with its specified starting index, so closed walks count labelled configurations via tr(T^n), without a rotation quotient. A fresh exact reproduction gives 110 transitions, SCC sizes 20 and 44 singletons, and characteristic polynomial X^46(X−1)^5(X+1)^2pqr as claimed. This finite certificate works for the trace at every n, independently of diagonalizability. A separate vertex-neighbor enumeration agrees at n=3–6 (8, 36, 78, 146). Exact strict Schur reductions for q and r at radius 2 and the derivative and product for p give a simple leading rho, bracketed by 2.2055 and 2.2056, with all other eigenvalues below 2 in modulus. An independently constructed comparison matrix for the triangular cross-section confirms a simple eigenvalue 3 and all other moduli below 2, establishing the ratio with leading constant 1. Replay: python3 /workspace/branches/0b0f1035-a9a8-416f-b4ac-dd28dadabeb9/reproduce.py; output is reproduce.log in that directory. The frozen verify.py and VERIFICATION.md were inspected, not executed. The invalid or unavailable cited triangular-report link does not affect the comparison, which has a readable prior statement and a direct exact reproduction.

## originality

PASS

The transfer-matrix method and the triangle-cross-section growth base are prior inputs. The supported distinct contribution is the exact spectrum and closed trace counts for the path cross-section, with the consequent comparison upon closing its two end rows. No priority is claimed for the triangular count or for the method.

## value

PASS

Closing the path inside each column is a natural, uniform edge modification with the same number of sites and a fixed update convention. The exact count and spectral gap quantify a strict entropy increase for that comparison, despite the changed local degree/tie constraints. The result is an all-length enumeration, not a handful of tested lengths or an unsupported universal monotonicity claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
