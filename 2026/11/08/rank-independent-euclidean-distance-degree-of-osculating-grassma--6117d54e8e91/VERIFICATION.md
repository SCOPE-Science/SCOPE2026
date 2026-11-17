---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

In Bombieri-scaled Sym^d(C²), the osculating r-space of the rational normal curve is transported from a coordinate flag by the conformal-orthogonal symmetric power M_d(t). Its projection matrix P_d,r(t)=M_d(t)P0M_d(−t)/(1+t²)^d embeds a smooth rational parameter curve away from isotropic t=±i and is regular at infinity. Under the complexified rotation character z, the projector has Laurent weights −d..d. Both extreme weights are nonzero for every 1<=r<=d by sum_{j<r}(−1)^j binom(d,j)=(−1)^(r−1)binom(d−1,r−1), and for generic unrestricted symmetric data both corresponding trace coefficients remain nonzero. The derivative of the trace objective has exactly two poles of order d+1; genus-zero differential divisor degree −2 yields 2d zeros counted with multiplicity. Immersion and basepoint-free characteristic-zero Bertini ensure generic simple, nonpole critical points; thereby ED degree exactly 2d. The metric and data hypotheses are essential. Independently computed symbolic exact projection/derivative degrees for five d,r samples (d=2,3,4, including rank>1), matching 2d; finite tests are not universal proof.

## originality

PASS

Full Resultary comparison with the earlier rank-one rational-normal curve shows a different embedding and metric: its monomial v=(1,t,...,t^d) with unweighted Euclidean form has Gram Σt^(2j), ED degree 4d−2 and GD degree 3d−2, whereas current Bombieri-apolar metric gives (1+t²)^d and all higher osculating ranks with ED 2d. Scroll-ruling curves and osculating binary-form varieties are different objects. Friedman–Hoşten–Rosana introduces ED/GD theory and Schubert/matroid/product model calculations but no accessible explicit same-rank osculating-flag computation. Originality is best-of-knowledge; the most relevant Friedman full text was not lawfully accessible despite OA and authorized institutional attempt.

## value

PASS

The exact ED degree of a natural osculating-flag curve embedded in a projection Grassmannian is a motivated algebraic-optimization invariant. The constant 2d across every osculating rank is a non-obvious rigidity consequence of a specific metric and extreme-weight cancellation; it is useful as a natural complete family, without needing a general downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
