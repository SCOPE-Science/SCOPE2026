---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Correct global convex automorphism averaging and 2x2 Fourier block B(ell) for each cycle Laplacian eigenvalue; scalar bound minimized at a=(z+2)/(2D), b=z(z+1)/D, z=sqrt2 sin(pi/m). Negative modes bounded via lambda_-(4), and zero Fourier block does not dominate, proving exact SLEM 2(z+1)/D for all m>=3 (no noninvariant uniqueness assertion). Independent eigenspectrum for m=3,4,5,9,20 matches to numerical precision, m=4 gives 4/5. However the exact theorem is previously published verbatim in Oct26 and follows from a broader Nov8 corona theorem.

## originality

FAIL

Oct26 published complete all-m sunlet optimizer with identical weights and full graph class; Nov8 independently supplies strictly broader vertex/edge-transitive leaf-corona optimum which specializes exactly to all sunlets. Neither proof reformulation nor restated asymptotic is a distinct new result.

## value

FAIL

Identical complete sunlet classification published Oct26; more general leaf-corona theorem published Nov8. This record rederives an already established exact optimum and asymptotics without an additional independently motivated mathematical fact. Correctness and reproducibility do not restore separate value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
