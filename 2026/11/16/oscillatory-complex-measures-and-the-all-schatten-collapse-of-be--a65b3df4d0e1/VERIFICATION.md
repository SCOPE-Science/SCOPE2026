---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For alpha>-1 and 0<s<1/2 on H², the Bergman power kernel expands into the exact lower-triangular matrix T_{nk}=m_n(s)(alpha+2)_{n-k}/(n-k)!. Boundary chirp moments transform via v=(1-t)^(-1) and contour rotation through pi/4. At v~e^{ipi/4}sqrt(n), the unique saddle gives m_n=√pi n^{-s/2-1/4}exp(-√(2n))exp(i[√(2n)+1/2+pi(1/8-s/4)])(1+O_s(n^-1/2)). Independent mpmath rotated-ray integrations at n=30,100,300 gave ratios approximately (0.916+0.080i),(0.956+0.045i),(0.975+0.027i), consistent with the O(n^-1/2) correction; a finite check is not the saddle proof. Row norms decay stretched-exponentially times a power, so rank-one row sums converge in every Schatten quasi-ideal S_p, p>0. Trace-norm finite compressions preserve determinant ∏(1-zm_n) and nonzero spectrum. Trace ∑m_n=(-i)^(s-1)Gamma(1-s,-i) uses summation remainder of bounded variation O(N^-s), avoiding unjustified absolute Fubini. For positive total variation, coefficients asymptotically n^(alpha+1-s), not square-summable, so it fails H² on constant 1. No claim uniform at s endpoints.

## originality

PASS

Blasco–Pennanen arxiv:2609.21657 studies precisely Bergman-kernel Cesaro operators but imposes *positive* inducing measures in its main theorems; Blasco–Mas 2025 likewise uses positive measures. Older complex-measure Cesaro works with Cauchy kernel do not directly entail the higher Bergman-power all-Schatten boundary chirp. The published related oscillatory Fock and radial Bergman Toeplitz findings concern different operators. Exact stretched exponential moment asymptotics, full S_p range, determinant and trace are not dominated by the inspected results.

## value

PASS

The example separates oscillatory complex measure regularization from any bound on its total-variation operator: variation is unbounded whereas every Schatten p-class holds. The precise nonselfadjoint spectrum, determinant and trace across all Bergman exponents are independently useful exact information for operator-ideal and Cesaro theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
