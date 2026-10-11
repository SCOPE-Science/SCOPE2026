---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a binary prior \(\Pr(U=1)=q\), Bob's click channel has conditional probabilities \(0\) and \(a_pt\), so its mutual information is exactly \(h_2(qa_pt)-q h_2(a_pt)\). If \(\omega_1\preceq c\omega_0\), then every mixture \(\omega_s\) is the image of a Bernoulli coin of bias \(r_s^{(c)}\) under one fixed preparation channel, giving the stated \(J_c(q,t)\) upper bound by data processing. Averaging the two erasure branches and subtracting from Bob's information gives the displayed achievable private-information rate. A fresh high-precision evaluation at \(p=1/2,q=39/200,t=4/299\) gave \(0.0002101139266\ldots\), more than \(1.104\) times \(3\ln 2/10927\). The repository's exact rational-interval verifier independently certifies the sign.

## originality

FAIL

The assigned theorem keeps the source channel pair, states, measurement, environmental domination constants, and coding theorem, and changes only the binary input prior while retaining the exact mutual-information expressions instead of the source's coarser numerical bounds. The private-information achievability theorem already optimizes over input ensembles/priors. Thus the arbitrary-prior formula is a routine one-parameter evaluation of the published construction, and the \(0.0002101\) certificate is a numerical tuning of a previously established achievable architecture rather than a new scientific mechanism.

## value

FAIL

A reproducible ten-percent improvement to one already-positive lower-bound certificate is useful numerically, but here it comes from routine prior tuning and retaining exact elementary information expressions, with no optimality, new channel, new coding mechanism, or structural boundary. Under the shared value bar this is too narrow a numerical gain to constitute an independent mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
