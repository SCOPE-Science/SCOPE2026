---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On K_m square K_n the orthogonal constant/contrast tensor decomposition gives L^+ on the three contrast blocks with eigenvalues 1/m, 1/n and 1/(m+n). The transfer-current covariance can also be obtained from the two-edge coefficient of the reduced Matrix–Tree determinant after adding rank-one incidence perturbations: distinct edges contribute −K(e,f)² and the shared edge contributes K(e,e)−K(e,e)². Thus the covariance is p minus the sum of all squared currents, including the squared shared-edge current. To check that sum independently, put d_i=e_0−e_i in the first coordinate and f_j=e_0−e_j in the second. First-coordinate edges at the two marks have tensor incidences d_i⊗e_0 and d_k⊗e_1, pairing to (1+δ_ik)/[m(m+n)]. Mixed edges pair by their coordinate dot products on the double-contrast block; only the cases with the shared edge are nonzero and yield −1/(m+n). Second-coordinate incidences pair by their second-coordinate dot product times η=(n+1)/[n(m+n)]. Their sum of squared dot products is 4+3(n−2), and p=2η. This gives exactly the three contributions to S and the numerator N in the proof. As an independent sign check, set t=n(n+1)/2 and divide the numerator by m²: N/m²=2n(m−t)+n+2−n²(m−2)/m². For m≤t−1 and n≥3 this is at most 2−n<0; for n=2 the only allowed below-threshold case m=2 gives zero. For m≥t the last term subtracted is less than n²/m≤2n/(n+1)<2, so the value is positive. At n→∞ with m/n²→c>0, (N/m²)/n³→2c−1 and (m+n)²/n⁴→c²; the quotient yields the claimed n³-scaled limit, also at c=1/2. Swapping coordinates exchanges the marked edge direction.

## originality

PASS

Transfer currents and general formulas for joint UST degrees are known. The distinct contribution is an evaluated two-vertex covariance and exact integer aspect-ratio transition in the rectangular rook family. The strongest general comparators require evaluating graph- and pair-dependent currents or track only aggregate coordinate degrees. The closest indexed rook result gives only a marginal, and the indexed adjacent-degree results on hypercubes do not vary m,n. No inspected comparator states or gives without further graph-specific calculation the evaluated covariance and sign threshold. This judgment is limited to inspected evidence.

## value

PASS

In a natural vertex-transitive graph family, two adjacent degree sums share a Bernoulli edge but also accumulate negative cross-edge covariances. The competition makes their sign unclear from classical negative association. The exact triangular-number transition, including the sole zero and behavior near the critical m≈n²/2 window, tells a researcher when the shared-edge mechanism wins rather than just exhibiting a positive example or giving a general algorithm for each parameter pair. The contribution is an evaluated and structurally informative boundary, not the transfer-current method itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
