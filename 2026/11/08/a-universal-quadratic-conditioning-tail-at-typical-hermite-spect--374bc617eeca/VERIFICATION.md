---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For n≥1, f_n(0)=ξ_n is independent of the Wirtinger derivatives with squared magnitudes (n+1)X and nY. A zero is intensity-Palm selected, so the Kac–Rice mark is weighted by |U²−V²|, with E=(a²+b²)/(a+b); this is correctly distinguished from point conditioning. The singular values U+V and |U−V| give K=(U+V)/|U−V|. Changing to t=V/U yields density 4a²b² t|1−t²|/[E(b+at²)^3]; splitting t at one and substituting t↦1/t gives the displayed antiderivative, tail coefficient 32a²b²/[(a²+b²)(a+b)²], layer-cake moment threshold r<2, and the n→∞ survival 4k²/(k²+1)². Independent exact-rational antiderivative and k=100 checks n=1,2,5 approach the stated coefficients. No anisotropic scaling invariance claimed.

## originality

PASS

The specified local Palm mark is not mere conditioning on F_n(z)=0. Published Hermite-spectrogram first/two-point and charged-zero formulas provide the underlying derivative laws but no exact intensity-size-biased Jacobian singular-value ratio survival, sharp k^{-2} coefficient, moment cutoff and universal high-order distribution in the inspected sections. This is a best-of-knowledge distinction, not absolute priority.

## value

PASS

Numerical conditioning of a typical white-noise Hermite spectrogram zero is a naturally important local inverse/detection observable; almost-sure nondegeneracy does not quantify unstable near-degenerate zeros. Exact power-law tails, finite mean/infinite variance, and a full high-order limit provide a meaningful family-wise quantitative risk law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
