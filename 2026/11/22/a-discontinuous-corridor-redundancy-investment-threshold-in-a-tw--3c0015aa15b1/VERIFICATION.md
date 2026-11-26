---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Applies to the corrected complete RESULT.md in repairs/3, not the frozen local-threshold wording. The frozen Finding says the balanced allocation becomes a strict local optimum 'at B=2√2'; this is false if inclusive and directly contradicted by its reduced derivative. At S=B/2=√2, 1−2t(S−t)=2(t−S/2)^2, so the derivative of log failure is positive to the left and negative to the right; arbitrarily small balanced transfers then improve success. The repair explicitly excludes equality and makes the derivative’s antisymmetry precise. Rechecked the repaired claim: internal balancing is strict at positive route totals because route success is ab/(1+a+b+ab) and other-route failure is positive. In the balanced family the log-failure derivative has sign (S−2t)[1−2t(S−t)]; when S>√2 both off-center roots are strict failure maxima and the center is a strict failure minimum. The latter lifts to a strict success maximum on the full simplex because changing route totals reduces the best achievable success locally, and any nonzero within-route imbalance strictly reduces success at unchanged totals. Only the center and concentrated endpoints can win globally. Their success difference (balanced minus concentrated) is S²(2S³+S²−8S−8)/((1+S)²(S+2)^4). The cubic has one positive root by Descartes plus the endpoint signs, and is negative at √2; independent bisection gives B_*≈4.357355625886. The endpoint-only max-path proxy follows from the strict increase of p(v/2)^2 in the route budget v. At B=4 the success values are 4/9 and 7/16 (concentrated and balanced); at B=5 they are 25/49 and 3425/6561. All frozen supporting files were inspected including the exact-arithmetic checker, not executed. It does not test the irrational local boundary; the exact sign identity does. The correction leaves the global claim and the open local/global disagreement interval intact. No correlated-passage or ecological field claim is proved.

## originality

PASS

Re-evaluated for the corrected statement. Independent-path reliability and balancing within one fixed route are not claimed new. The prior statements inspected give the proxy, reliability evaluation, different investment laws, or different design variables and connectivity criteria, not the rational-law cubic crossing and separate strict local boundary. Priority remains evidence-qualified.

## value

PASS

The repaired theorem exactly separates a meaningful single-route proxy from the true independent-route event. It identifies where local maximization may wrongly favor diversification before the global switch, and distinguishes a degenerate stationary allocation at the onset from an actual strict local optimum. This is a natural benchmark for objective selection and solver interpretation, not validation of habitat restoration recommendations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
