---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the specified forward cycle, the first row is q_j(s)=(1+2 exp(-ds) cos(s-2πj/3))/3. For d≥√3 the negative fractional power is irreducible Metzler, giving strict positivity at t>0. For 0<d<√3 an entry can be negative only on its arc cos(s-2πj/3)<-1/2. The viable arcs, rather than the full overlapping negative-cosine lobes, have cells (2πn/3,2π(n+1)/3) and component (n+2) mod 3. The damped negative cosine has its maximum at γ_n-arctan d; the log peak decreases in d with derivative -(γ_n-arctan d). The strict peak inequality gives the ceiling, correctly excluding a tangency. The first arc starts with equality at s=0 and has positive derivative of the damped negative cosine there. For the last nonpositive time, the largest eligible index with weak peak inequality is floor[(3/(2π))(B(d)-π/3)]; its peak is within O(1) of log(2)/d, which is also an upper bound for the last root. Rescaling gives both asserted constants. At d=0 the row is a permutation at s∈(2π/3)Z and otherwise has exactly one negative entry. Row sum one then gives the norm formula. An independent high-precision solve of H_1(d)=0 gave d=0.228903469804774575 and α_1=2.570230659003062518. Replay: frozen RESULT.md, Proof, with the cell restriction above. The bundled verify.py was inspected, not executed; its finite tests are supplementary.

## originality

FAIL

The broader indexed three-state circulant staircase contains the advertised central classification: exact time test, count, endpoint equations, threshold ladder and divergent count. Specialization is exact under δ=3^(α/2)cos(πα/6), ω=3^(α/2)sin(πα/6), with transposition to accommodate the directed-cycle convention. This is demonstrated statement coverage, not a claim about which of the two same-day records came first. The record-specific labels, last-time asymptotic and α=3 boundary are direct consequences of the already explicit kernel and cells; they do not restore originality to the frozen central claim.

## value

FAIL

The sharp sign-time staircase is a useful quantitative phenomenon, but it is already supplied in a broader exact classification. In the frozen record the fractional path amounts to a parameter substitution; the component labels, zero-damping permutation endpoint and last-time estimate are immediate from the explicit kernel and bounded-width final cell. No separately motivated, substantive unaddressed invariant survives as a valuable repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
