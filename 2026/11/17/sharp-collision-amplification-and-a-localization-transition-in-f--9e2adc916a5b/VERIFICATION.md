---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The specified C1 two-piece quadratic spline has dimension six and interpolation equations at 0, epsilon, 1, R and two matching conditions at (1+epsilon)/2. Recomputing the exact 6x6 determinant gives epsilon(R-1)(epsilon-1)[-R epsilon-3R+epsilon^2+2epsilon+1]/4, nonzero on 0<epsilon<1<R. Divide the colliding interpolation difference by epsilon, pass to the invertible confluent matrix and obtain the operator-norm limit epsilon I_epsilon -> (y2-y1) g_R with left quadratic t-(4R-1)t^2/(3R-1) and right quadratic (t-1)(t-R)/(3R-1). Its two competing absolute extrema occur at (3R-1)/(2(4R-1)) and (R+1)/2. Their heights give the stated sharp norm coefficient and cross uniquely at R=2+sqrt(3). Uniform convergence of all four Lagrange basis functions gives uniform convergence of Lebesgue functions and correct maximizer localization, including the two-point tie. Independent symbolic determinant and exact rational R=3/2,2,4,6 checks corroborate the algebra. This is fixed-R, epsilon->0 only; no uniform-in-R inference.

## originality

PASS

Greene establishes the scheme and cubic smooth-data convergence, with Powell cited for qualitative instability; neither the accessible statement nor any inspected distinct interpolation result supplies the exact rank-one collision operator, sharp R-dependent coefficient or unique localization phase threshold. The proof derives a nontrivial equality comparison rather than an immediate normalization of the known qualitative blowup. Historical priority remains bounded by inaccessible original chapters and current preprint full text.

## value

PASS

PASS: The minimal four-site not-a-knot spline is a canonical boundary case of even-degree spline interpolation. A sharp collision blowup coefficient and the exact geometric switch in the norming location quantify a meaningful failure mode of smooth-data stable-looking schemes under arbitrary noisy nodal data. The fixed-four-node exact instability and phase threshold are mathematically informative rather than simply restating the known nonuniform boundedness observation; the fixed-R restriction is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
