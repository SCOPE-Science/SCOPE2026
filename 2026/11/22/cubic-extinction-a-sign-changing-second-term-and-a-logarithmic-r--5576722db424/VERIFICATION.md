---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The coincidence is genuine: positive equilibria obey x=1−y and the reduced equation (m(γ+y)−α)(1−y)−βy(γ+y)=0. At α=mγ the constant term vanishes and the linear coefficient is m−βγ, so at β=m/γ the equation has a double root at zero with nonzero quadratic term. In coordinates v=y and w=x+y−1 the exact increment is δmv²[γw−(γ+1)v]/[γ(γ+v)(1−v+w)] and the transverse update is W=(1−δ(1−v+w))w+(V−v). On |w|<ηv the increment is strictly negative, of order v³ with bounds on both sides, and V/v≥1−Cv². Since |1−δ|<1, shrinking the wedge gives |W|<ηV, V>0 and 1−V+W>0. Thus v descends to zero; division by v gives transverse contraction and w/v→0. Reciprocal-square increments then tend to 2A. Division by v³ gives a uniformly contractive recurrence with limiting forcing −A and fixed point −κ, where κ=A/δ. Once w=O(v³), the error w+κv³ obeys a stable recurrence with forcing O(v⁴). Dividing by V⁴ preserves eventual contraction since V/v→1, so w=−κv³+O(v⁴). This yields scalar coefficients A, B=A(γ−1)/γ and C=A(1−1/γ+1/γ²+m/γ) with a negative sign in the map. Expanding the reciprocal square gives increment 2A+2Bv+(2C+3A²)v²+O(v³). First summation gives v=(2An)^(−1/2)+O(n^(−1)); the next gives v^(−2)=2An+[4B/√(2A)]√n+O(log n). Inverting yields coefficient −B/(2A²) and the claimed sign and remainder. At γ=1, B=0 and v²−1/(2An)=O(log n/n²), so subtracting the harmonic increment leaves a summable error, including O(v³). This gives an actual finite orbit-dependent clock remainder, with log coefficient (2C+3A²)/(2A)=1+m+3δm.

## originality

PASS

The exact model and generic cubic slowing are not new. The compared exact-model paper excludes this slice in its transcritical theorem. The distinct result is the quantitative extinction law for positive Euler orbits on this slice, with model-specific transverse locking, sign change, and finite discrete clock at γ=1. A different plankton map already has a substantial two-term extinction result. The cited continuous cusp is close background; its exact source passage could not be independently retrieved and is not relied on to prove noncoverage.

## value

PASS

The slice is dictated by coincident thresholds, not chosen to fit a computation. It resolves the local positive dynamics where the ordinary quadratic transcritical coefficient vanishes. The explicit two-term rate reveals a sign change invisible to leading-order cubic slowing; at the cancellation point the finite renormalized inverse-square clock distinguishes discrete-step effects. Transverse locking puts the asymptotic in the population variables for an open wedge, not only on a formal invariant curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
