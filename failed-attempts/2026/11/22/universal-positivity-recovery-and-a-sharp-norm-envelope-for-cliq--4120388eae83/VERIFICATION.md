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

The constant mode, apex contrast (N−1,−1,…,−1), base block-average contrasts, and block-internal zero-sum spaces are mutually orthogonal and span the coordinates; applying L gives eigenvalues 0,N,1,p_i+1. For A=e^(−at) and C=e^(−ct), the resulting cross-block entry is D=((N−1)+C−NA)/(N(N−1)), realized because there are two or more cliques. The diagonal is positive, the apex entry is (1−C)/N, and each within-block off-diagonal entry exceeds D for t>0 under strict increase. Therefore D determines entrywise nonnegativity. Its derivative has sign Na−c e^(−(c−a)t), hence positive for positive t if c≤Na, and otherwise changes from negative to positive just once at t_*. Since D(0)=0 and D(∞)=1/N, there is just one positive root in the latter case. Row sums are one and H is symmetric. The absolute row sum is one plus twice negative mass. There are N−2 other base vertices per base row, all entries ≥D, with at least one strictly greater than D in a nonsingleton row. This gives the envelope, exactly the stated equality cases while D<0, and the maximum at t_* for an extremizing partition. Nonnegative times give norm one for all partitions and cannot change the peak comparison. For ψ(x)=x^α, a=1, c=N+δ; removing the root t=0 from the scalar equation gives T=2δ/[N(N−1)]+O_N(δ²), while the minimum of D is −δ²/[2N²(N−1)²]+O_N(δ³). With δ=N log(N) ε+O_N(ε²) these give the coefficients. The positive root increases with c and approaches log[N/(N−1)] by the exponential equation. These conclusions apply to the stated unweighted clique-cones, with strict increase needed only for the strict partition comparison.

## originality

FAIL

The earlier heterogeneous-windmill record c55885b0d081 gives the exact three off-diagonal entry classes on the identical graphs. Although its positivity theorem assumes convexity, its explicit entry identities are obtained by spectral projectors before that hypothesis is used and hold unchanged for the sampled nonconvex filter. Substitution of exp(−tψ(x)) plus monotonicity makes its already displayed cross-block entry the sign test, and counts the number of entries equal to that minimum in a row. One derivative gives the unique recovery root and peak; attaining the sharp bound is precisely attaining the entrywise lower bound at every other base coordinate of one row. The older star/multipartite fractional result separately gives the extremizing fractional kernel and its asymptotics. The combined phase and envelope are a direct corollary even where no earlier title announces them for all increasing ψ.

## value

FAIL

The positivity horizon and transient norms are natural and the formulas could be useful as a consolidated example. As a distinct finding, however, the stated topology invariance and sharp singleton envelope reduce directly to the already computed cross- and within-clique coordinates, a single scalar derivative, and counting equal minimum entries; the fractional extremal specialization is already the star. The frozen claim does not supply a further independently useful unknown invariant or nonroutine structural step beyond that prior exact table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
