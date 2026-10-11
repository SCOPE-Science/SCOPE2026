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

FAIL

The identity \(\langle uy\rangle=\beta\langle u^2\rangle\) and the storage/energy balance are correct. However \(\langle G(x)\rangle=0\) as stated is not valid under the record's identity-level assumptions. Its proof uses that \(\dot\theta=\omega\ne0\) forces the phase marginal to be Haar and hence \(\langle\sin\theta\rangle=0\). When \(\omega=0\), a compact invariant equilibrium may have fixed phase \(\theta_0\) and satisfy \(G(x)=A\sin\theta_0\), so the asserted zero mean need not hold. Because the final claim explicitly says only \(de\ne0\) is needed for the identities, the submitted theorem is false on its stated domain. A repair by adding \(\omega\ne0\) would fix correctness, but the surviving mathematical content does not pass originality/value below.

## originality

FAIL

After the needed \(\omega\ne0\) restriction, the core mean-power law is mechanically implied by the standard storage identity for the stable first-order filter \(\dot u=y-\beta u\): stationarity of \(u^2/2\) gives input-output power \(\langle uy\rangle=\beta\langle u^2\rangle\). The remaining nonlinear balance is the routine source-system energy multiplication/cancellation, and \(\langle G(x)\rangle=0\) follows by averaging once the rotating phase has zero sine mean. The defining paper supplies exactly the controller state equation and cardiac oscillator. Under the implication-level rule, the source-specific repackaging does not survive as an original theorem.

## value

FAIL

Quantifying controller power in the published cardiac example is motivated, but the claimed exact law is the elementary storage balance of a first-order stable filter, while the source-specific energy identity is obtained by one direct multiplication and cancellation. Once the incorrect frequency scope is repaired, the result does not expose a new boundary, nontrivial invariant, or structural obstruction beyond standard passivity bookkeeping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
