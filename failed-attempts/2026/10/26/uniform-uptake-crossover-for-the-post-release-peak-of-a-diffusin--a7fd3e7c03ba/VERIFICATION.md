---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a>0 the kernel h(s)=s^(−p)exp(−a/s−ks) vanishes at 0, and the sign of a−ps−ks² gives a unique mode m≤a/p. The release-phase derivative is proportional to h(t)>0. After release the derivative is proportional to h(T+δ)−h(δ); it is positive when both arguments lie before m and negative when both lie after m. On the intermediate interval the first term strictly decreases and the second strictly increases; endpoint signs give a unique crossing and global peak with δ<m<T+δ. The logarithmic equality at the peak gives a/δ−a/(T+δ)=p log(1+T/δ)+kT. For z=a/(pδ)>1 and B=log(pT/a)+kT/p, its exact rearrangement is z−log z=B+E, with 0<E≤2a/(pT). The large branch has z>B; evaluating x−log x at x=B+log B underestimates B by log(1+log B/B). For B≥2, the derivative is at least 1/2 throughout the comparison interval, so 0<z−(B+log B)≤2 log B/B+4a/(pT), uniform even for arbitrarily large k(T). This proves the displayed lag and all three scaling regimes. The derivative at the crossing also gives the stated strict duration trends. The supplied finite-grid script and metadata were inspected, not executed; uniformity follows from the analytic inequality, not the grid.

## originality

FAIL

The closest separately indexed drift-release result has an exactly equivalent kernel for every nonnegative loss and gives the same exact scalar root equation. It does not print the claimed all-loss error term, but that error term follows mechanically by bounding two terms already visible in its equation and using the standard large-branch inverse. The different observable does not change the timing problem. Both files are dated October 26; this is a statement of coverage and implication, not an assertion of intra-day priority.

## value

FAIL

The crossover is a natural physical observable and the uniform estimate is valid. Its additional precision here is a direct bound on the already available identical peak equation followed by a textbook inversion; the change of observable does not yield a new mathematical regime. No independently useful unknown fact beyond that implication was demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
