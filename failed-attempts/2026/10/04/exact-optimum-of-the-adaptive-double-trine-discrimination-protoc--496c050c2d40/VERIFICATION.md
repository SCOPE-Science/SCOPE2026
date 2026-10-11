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

The source branch probabilities and postmeasurement states reconstruct the submitted scalar error function. With the normalized branch posteriors, \(Q=P_0+P_1\) and the retained-state overlap \(c=(1-p)/(2(2+p))\), the Helstrom expression reduces to the displayed \(E(p)\). Independent symbolic differentiation gives \((S')^2-4(Q')^2S=(p-1)((18+11\sqrt3)p-(14+9\sqrt3))/216\). The unsquared derivative condition rejects \(p=1\), and the remaining root is \(p_*=(45-8\sqrt3)/39\); direct substitution gives the stated exact minimum and positive gap. Thus the mathematical exactification is correct.

## originality

FAIL

The exact radicals are not printed in the 2013 source, but the final claim is mechanically implied by that source. Chitambar--Hsieh publish the same one-parameter protocol, the exact conditional probabilities and postmeasurement states, the exact Helstrom objective, and the same numerical minimum \(6.47\times10^{-2}\), with \(p=1\) identified as the one-way endpoint. The audited contribution then consists of differentiating this published one-variable analytic function and simplifying its already reported optimum to radicals. Under implication-based originality, a closed-form exactification of a source-supplied scalar objective and source-reported optimum is covered even when the source did not print the radical.

## value

FAIL

An exact calibration is convenient, but the source already establishes the operational two-way advantage, supplies the full scalar objective, and reports the same optimum numerically. Turning that published one-dimensional numerical optimum into radicals is a routine exactification rather than a separately motivated mathematical gap under the common value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
