---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exact source band condition expands at \(k=n\pi+x/(n\pi)\) as \(R=6-8/x^2+(n\pi)^{-2}(-8x^2+88/3+16/x-16/x^2)+O(n^{-4})\). Solving \(R=\pm2\) by the implicit expansion at \(x=\pm1,\pm\sqrt2\) gives exactly the four quoted energy-edge coefficients. A fresh symbolic reconstruction in this audit independently reproduced all four coefficients. The published wide-band family remains a positive momentum distance from \(n\pi\), hence exits every fixed recentered energy window. The frozen numerical bisection verifier was also read and is corroborative only.

## originality

FAIL

The primary source already gives the exact scalar band condition for half flux and itself performs the same local substitution \(k=n\pi+\delta\), obtaining \(\delta=\pm 2\sqrt2((n\pi)\sqrt{6-\Theta_2})^{-1}+O(n^{-3})\), with band edges at \(\Theta_2=\pm2\). That published formula already implies the claimed Hausdorff-limit edges \(\pm2\) and \(\pm2\sqrt2\) after squaring. The only added content is the next Taylor coefficient of the same exact one-variable dispersion relation. Under the required implication-based originality bar, this is a routine higher-order expansion of a stronger published exact formula rather than an independent scientific result.

## value

FAIL

The recentered cluster picture is a useful visualization, but scientifically the submitted addition is only a routine next-order Taylor extraction from the published exact one-variable dispersion relation, after the source has already performed the leading local expansion and identified the edge parameters. The extra four \((n\pi)^{-2}\) coefficients do not supply a new structural mechanism, boundary, classification, or independently motivated invariant under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
