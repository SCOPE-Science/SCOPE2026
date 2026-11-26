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

For a=−c<0, cK<1 gives leading-term domination on the unit circle in Q itself. At cK=1, equality in the triangle inequality for a unit root forces all geometric monomials to have the same phase (in particular those of powers zero and one), hence z=1. This root is simple since Q'(1)≥1; continuity from the interior puts all others strictly inside. If cK>1, Q(1)<0 and Q(x)→+∞ for x→+∞, giving an unstable root. At a=0 all roots are zero. For a>0 use the exact identity (z−p)Q=z^{n+1}+(a−p)z^n−ap^n, whose extra root p is strictly inside. Unit-circle leading-term domination holds throughout the claimed open positive interval: for a≤p, p−a+ap^n<1, while for a≥p, a−p+ap^n<1 is exactly a<(1+p)/(1+p^n). At upper equality z=−1 is a root for odd n, and equality in |z+a−p|≥1−(a−p) forces that sole unit root. Differentiation of the trinomial at −1 gives z'(a_+)=−(1+p^n)/(1+n a_+p^n), since its z derivative is −1−n a_+p^n. The nonzero latter derivative proves simplicity. For a>a_+, Q(−1)>0 and odd monic Q(x)→−∞ as x→−∞. For the specified Leslie model equilibrium cancels F G(X*) to 1/K; the Jacobian first row is constant −a by log differentiation of G. The lower inequality then follows from X*>0 and the upper is exactly (1+gamma B)X*<B. This proves all linear assertions; in particular it does not decide nonlinear flip nondegeneracy or stability at criticality.

## originality

FAIL

There is a genuinely matching older mathematical criterion, even though the cited population paper did not itself give the all-p spectral proof. The classical trinomial root-count theorem of Bohl (1908), stated as Theorems 3.1–3.2 in Theobald–de Wolff, applies with exponents (s+t,t)=(n+1,n), coefficients (a−p,−ap^n), and radius one. In the decisive positive stable regime, Theorem 3.1 requires just 1>|a−p|+ap^n. This holds automatically for 0<a≤p and is exactly a<a_+ for a≥p. The threshold is sharp by the prior candidate Q(−1)=0 and the sign for larger a. The negative half is the classical coefficient-domination test on Q, sharpened immediately by evaluating Q(1). Thus the reported new stability interval is a direct specialization of existing root-location criteria plus real endpoint signs. Simplicity, slope and recruitment inequalities are immediate boundary/algebraic consequences, not independently surviving new results. This is not a rejection for inaccurate mathematics or inaccessible literature.

## value

FAIL

The application explains a meaningful stability boundary in the Leslie model, and the short derivation could be useful exposition. But the published model already supplies the candidate flip threshold, the mathematical classification is a trinomial root-location specialization, and the exact slope and recruitment division are routine differentiation and rearrangement of that boundary. There is no separate nonroutine residual scientific claim to repair, such as a nonlinear bifurcation theorem or a new classification outside the classical criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
