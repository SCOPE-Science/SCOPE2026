---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The analytic descent proof is independent of finite experiments. Every odd input at least \(29\) reaches a strictly smaller odd integer within at most three steps; the decreasing stopping-time construction forces entry into the explicit 13-state graph.

The exact inverse-totient argument has a proven finite scope: \(\varphi(n)\ge\sqrt{n/2}\) ensures that every positive solution of \(\varphi(n)=m\) for \(m\le30\) has \(n\le1800\). The bundled `verify.py` uses integer arithmetic to exhaust this **entire** range and verify all 10 preimage lists, including the empty lists at targets \(0\) and \(26\). The exhaustive computation provides the finite component of the proof, rather than merely sampling candidate solutions.

The checker also independently evaluates the 13 small odd states via gcd counting, exhausts the proposed strict descent on odd integers through \(99999\), and checks the basin assertions for every positive start through \(100000\). Its actual successful output is embedded as `verify_output.txt`. Those larger bounds are regression checks only and are not used to infer the all-integers theorem.

The mathematical claim concerns exactly \(n\mapsto\varphi(n)+3\). It does not classify other shifts or provide closed-form preperiod lengths. Self-review passed; independent audit is not performed.
