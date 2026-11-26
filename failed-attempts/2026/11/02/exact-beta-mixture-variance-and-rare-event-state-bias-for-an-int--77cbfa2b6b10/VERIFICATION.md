---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Positive mean drift gives a finite conditional variance in the backward stationary convolution by the ergodic theorem. Coupling two stationary versions with the same initial environment (which has a unique marginal) and the same future noises makes their position difference contract almost surely, proving uniqueness; the variance process contracts by the squared multiplier. The variance is strictly greater than D/a almost surely. In the variance transport equations the opposite fluxes are proportional to (v-c)^eta (v+d)^(-xi) and vanish at both endpoints. The resulting nonnegative integrable densities solve the invariant equations; alternatively any constant nonzero total flux would force nonintegrable plus density at c or minus density at infinity. The change to Y gives precisely the two beta shapes. Their beta-endpoint survivals give the displayed variance coefficients, and the common independent Gaussian factor gives the claimed two-sided coefficient: v^theta P(V>v|S=s) is bounded, allowing domination by a multiple of |Z|^(2 theta). The moment statement is for nonnegative p, including logarithmic divergence at equality. The relative state coefficients are a:b in plus/minus share reversed, i.e. the minus-to-plus ratio is a/b, giving the stated share. The explicit example gives K_V=8/(3 pi) and hence the stated K_X. A separate finite diagnostic at (a,b,u,w,D)=(1.5,0.7,0.9,4.62,0.8) matched second and fourth joint moments to within 4.4e-15. To reproduce, start at the invariant environmental masses and solve (Q^T-2r diag(a,-b))M_r=-2r(2r-1)D M_(r-1) at r=1,2, where Q is the environment generator and M_r stores the joint order-2r moments. Compare to beta integrals of (2r-1)!! v(y)^r. The variance survival computed by the beta integrals at threshold 10^4 gave a repulsive share 0.6817909 against limit 0.6818182. This diagnostic is not a proof. The frozen verification prose names check.py but the supporting script is standalone_check.py; the packaged expected output is not an independent run.

## originality

FAIL

The earlier Resultary record 93bb1b2e24d1 states and proves the same joint state-conditional variance laws in beta-prime coordinates, the same position mixture, and the identical explicit tail coefficient and moment cutoff. The highlighted extreme-state share follows directly from those already stated joint laws and identical Gaussian multiplication in each state. Nothing material in the frozen finding survives that comparison as a distinct contribution.

## value

FAIL

An evaluated state-resolved stationary law and tail amplitude are valuable observables, but the earlier result already resolves them for precisely this family. Taking the ratio of its two state coefficients highlights a physical interpretation, but is a mechanical normalization, not a further scientific contribution in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
