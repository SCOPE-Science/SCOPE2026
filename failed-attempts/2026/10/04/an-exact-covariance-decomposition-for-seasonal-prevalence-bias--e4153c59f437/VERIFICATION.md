---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

At each strictly positive period-omega solution, divide Sdot=bK-beta_bar(t)IS-bS by S and integrate Sdot/S over a full period to obtain <beta_bar I>=bK<1/S>-b. Since beta=<beta_bar>>0, split <beta_bar I>=beta<I>+Cov(beta_bar,I), and subtract beta I*=bK/S*-b at each chosen positive averaged equilibrium. This proves the exact first formula and iff condition. Likewise the infected logarithmic derivative gives <beta_bar S>+<lambda_bar R>=alpha+b, and subtraction of beta S*+lambda R*=alpha+b proves companion. Continuity and strict positivity justify all divisions and integration; no uniqueness/equilibrium existence/sign claim is smuggled in. The source verify.py uses exact rationals but tests only algebra; independent actual seasonal positive 1-periodic numerical solution at (b,K,alpha,beta,lambda)=(0.2,1,0.3,1.1,0.2), beta_bar=1.1(1+0.4 sin2pi t), lambda_bar=0.2(1+0.3 cos2pi t) gave meanI-I*=-0.00015141406637547705 versus formula -0.0001514140655416743 (absolute discrepancy 8.34e-13), companion residual 2.51e-12. This is corroboration only, not an unrestricted proof.

## originality

PASS

Best-of-knowledge narrow explicit formula originality only, not novelty of the SIRI model, positivity, covariance definition or averaging of logarithmic derivatives. The 2026 same-model source supplies the ODE and numerical mean-versus-averaged comparisons but the publisher-indexed material retrieved did not explicitly give the two displayed identities. General reproduction-number threshold papers and a published oscillatory SI mean-variance shell do not assert or imply the same model-specific closed form as a stated result. However, the result is a direct routine mathematical consequence of already published source equations; this significantly weakens its scientific value. Full same mathematical model primary text was inaccessible, so any stronger prior occurrence is retained as a material risk; O is not a novelty certification.

## value

FAIL

The object (seasonal SIRI prevalence versus an averaged equilibrium) is motivated by a real numerical comparison, but the submitted mathematical addition is only the standard periodic identity integral_0^omega Sdot/S dt=0 followed by the definition Cov(X,Y)=<XY>-<X><Y> and subtraction of the already published equilibrium relation; the second boxed formula repeats the identical logarithmic-derivative manipulation for I. The stated iff equality condition merely rearranges the first identity. It yields no independently checkable parameter condition, nontrivial bound/sign, structural classification, boundary example, new dynamical consequence or computed natural invariant not mechanically implied by the published equations. To evaluate the rhs one needs the same full periodic orbit data from which <I> is already directly computed; no useful prediction or reduction is established. Thus this is a textbook balance-equation re-expression rather than a motivated nonroutine mathematical finding; correctness and a specific motivating paper do not suffice to establish scientific value. Rejection is about this final mathematical claim, not about primary-text access or verification effort.

The dated certificate retains the supplied scientific assessment, sources and limitations.
