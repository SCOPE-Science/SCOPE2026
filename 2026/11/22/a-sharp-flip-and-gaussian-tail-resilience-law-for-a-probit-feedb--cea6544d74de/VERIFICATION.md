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

# Verification of the probit-feedback theorem

The analytic verification is contained in the \(\texttt{RESULT.md}\) proof, not in a numerical enumeration. The critical facts are the exact conjugacy to \(G_a(z)=z-a(\Phi(z)-1/2)\), the strictly decreasing integral \(g(u)/u=\int_0^1\varphi(su)\,ds\), and the strictly increasing integral \(g(u)/(u\varphi(u))=\int_0^1e^{u^2(1-s^2)/2}\,ds\). These yield exact existence and uniqueness of the primitive two-cycle and of the superattracting gain for all positive real parameters. The linear/cubic boundary and Gaussian-tail constants follow by symbolic Taylor expansion and Mills' ratio.

Run the included standalone test file with `python check_probit.py`. The checker uses only the Python standard library, brackets positive roots numerically, tests the reflection return equation at seven gains, locates the only positive stationary-multiplier zero by a sign bracket, checks the finite-hitting exception, and compares the critical coefficient and Gaussian large-gain ratios. The reported run completed with exit status zero and a `PASS` message.

Computational tests do not prove universal quantifiers, exclude all other cycles, or replace the uniqueness arguments. The statement proves the exact number of primitive two-cycles but does not exclude possible higher-period or chaotic dynamics in the supercritical regime; it proves local rather than global attraction there. No independent mathematical audit has been performed.
