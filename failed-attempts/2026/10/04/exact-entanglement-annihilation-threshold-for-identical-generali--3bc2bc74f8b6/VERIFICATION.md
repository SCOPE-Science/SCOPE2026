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

The algebraic threshold is correct. For the generalized amplitude-damping channel with thermal parameter \(n\), the singlet partial-transpose boundary reduces to \(2(1+\sqrt2)n(1-n)\gamma^2+\gamma-1=0\). Independently comparing the positive root with the finite-temperature damping variable in Filippov--Frizen--Kolobova gives exactly their published entanglement-annihilation boundary after identifying \(\gamma=1-e^{-2\Gamma t}\) and \(n(1-n)=w(1-w)\). The diagonal-filter reduction to a unital channel is also consistent with the explicit nonunital-to-unital decomposition in that paper. Thus the final equivalence is mathematically valid, but it is not new.

## originality

FAIL

A decisive prior source already gives the same exact entanglement-annihilation boundary for two identical finite-temperature generalized amplitude-damping channels. Filippov--Frizen--Kolobova derive the corresponding unital reduction and state in their Eq. (49) that the tensor-square channel is entanglement annihilating exactly beyond the displayed finite-temperature threshold. After the elementary substitution \(\gamma=1-e^{-2\Gamma t}\), their inequality is precisely the quadratic boundary in the audited claim. The later singlet statement adds only the direct PPT calculation showing that one Bell state meets that already-published boundary. The 2025 paper's numerical conjecture therefore does not restore priority over the 2018 exact theorem.

## value

FAIL

The singlet calculation is a useful consistency check, but the scientifically substantive object is the exact entanglement-annihilation boundary, which was already derived for the same generalized amplitude-damping family in 2018. Identifying that an elementary singlet PPT boundary happens to equal the published threshold is not a separate structural gap under the audit value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
