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

For a symmetric path kernel under the return-excluded convention, the pseudoinverse resistances sum to n times the trace and edge i separates i(n−i) unordered pairs. Thus nK is the strictly convex reciprocal sum with only the interior capacity inequalities (which also bound endpoint transitions). The alternating candidate is feasible and saturates every interior inequality. The incidence transpose system for normalized dual multipliers has the stated alternating-prefix solution; equal unit total mass on each parity gives its closing zero. Direct polynomial summation gives the four displayed factorizations: for n=2r, both relevant numerators are positive on 1≤k≤r−1 and vanish for the last odd-index multiplier k=r; for n=2r+1 the even-index numerator is positive for k<r and the odd-index numerator for k≤r. This includes n=3. Stationarity turns the reciprocal tangent remainder into precisely the displayed weighted holding cost plus the positive quadratic-over-linear remainder; both vanish only at the candidate. Evaluating the parity sums gives the two values and rationalizing the even-order excess gives 3/[2(n²−1+sqrt(n⁴−2n²−8))], strictly positive and asymptotic to 3/(4n²). The matching SLEM theorem uses exactly the same path feasibility. Fresh tests solved the multiplier incidence system directly and used the exact matrix resolvent and a nonconstant feasible vector for each n=3,...,12. Those checks corroborate, but do not prove, the all-order formulas.

## originality

PASS

The exact locally constrained path design, parity comparison, and strictly positive interior-capacity loss certificate are not established by the inspected SLEM, resistance-budget, general SDP or spider results. Credit the existing resistance representation and the general Kemeny design problem; neither is part of the distinct claim.

## value

PASS

Paths are a basic benchmark for designing uniform-stationary walks. The result exactly resolves when optimal expected stationary-target search uses the same kernel as optimal spectral mixing. The strict parity-dependent divergence and all-local-capacity rigidity are structural; the excess certificate makes the benchmark quantitative. Its small absolute even-order gain is not presented as a practical speedup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
