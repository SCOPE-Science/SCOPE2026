---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Independently obtained the coefficient by the periodic diagonal gauge x=e^{TH}v in phase time. The gauged generator is T(A0+T[A0,H]+T²[[A0,H],H]/2+O(T³)). The period mean of [A0,H] vanishes. In the normalized periodic profile the order-T term is constant and the next solvability condition makes it zero along with the linear exponent term. Pairing the order-T³ solvability condition with q kills A0−λ0I, leaving exactly the stated edge sum; [[A0,H],H]_{ij}=L_{ij}(H_j−H_i)² off diagonal. Bounded coefficients give a convergent fundamental-matrix power series, and the simple eigenvalue of the analytic desingularized monodromy fixes the branch at zero, justifying the differentiated remainder. Connectivity forces common H at zero energy; the resulting common scalar forcing factors out exactly at every period. Equality and differences of forcing must be understood a.e. (values at individual discontinuities are immaterial, as in the definition of H). In a separate exact directed three-cycle example with durations 1/4 and 3/4 and rates (1,2,4) and −(1,2,4)/3, the common zero-mean primitive factor has variance 1/192 and the coefficient is 7/576. This is an exact coefficient check, not a direct monodromy simulation. The frozen reported 36 assertions were inspected, not rerun.

## originality

FAIL

A distinct current indexed finding proves the same high-frequency directed-edge Dirichlet formula, strictness criterion and local derivative under equal or broader network assumptions. The two-patch case is an immediate patch-splitting reduction. This is established present coverage, not a finding that the indexed record predates the frozen one or an attribution of provenance. The earlier primary papers inspected do not establish the general new coefficient by themselves.

## value

PASS

The formula itself is useful: it identifies and computes the leading effect in a directed finite network, characterizes the flat case, and supplies strict fast-period monotonicity without asserting global behavior. This is a structural result for general seasonal waveforms, not just a numerical illustration. Scientific usefulness does not overcome documented equivalent coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
