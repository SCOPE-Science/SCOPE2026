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

Direct exponentiation of the two invariant Hamiltonian blocks gives the two X-state concurrence candidates. Their dependence on \(\nu(D)=\sqrt{g^2+D^2}\) is monotone, so each has at most one crossing. Solving the two equality conditions gives the stated piecewise \(D_-\) and \(D_+\). Independent evaluation on the source benchmark across several temperatures reproduced the strict ordering around \(D_c\) whenever the left branch exists and the convergence of both endpoints toward \(D_c\). The exact identities comparing the inverse-hyperbolic arguments with \(z+a\) establish the all-parameter straddling; the finite evaluations are only supplementary.

## originality

FAIL

The direct 2008/2010 Gürkan--Pashaev paper implication-covers the final claim. It prints the undercritical and overcritical finite-temperature concurrence branches, defines the same critical coupling \(D_c\), and explicitly states that at positive temperature entanglement vanishes on an interval containing \(D_c\) that grows with temperature. The audited \(D_-\) and \(D_+\) formulas are obtained by setting the two printed monotone numerators to zero and applying \(\operatorname{arcosh}\) and \(\operatorname{arsinh}\). The straddling of \(D_c\) follows from elementary hyperbolic identities. Under the required implication standard, lack of printed endpoint notation does not make this original.

## value

FAIL

Closed endpoint formulas can be convenient, but here they are obtained by elementary monotone inversion of two concurrence numerators already printed in a source that also states the resulting zero-concurrence interval and its location around \(D_c\). This is a routine algebraic repackaging rather than a motivated new mathematical gap under the audit's value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
