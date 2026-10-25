---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For k>=3,n>=2,N=kn, the centered pair-incidence features w_e(M)=1_{e co-block}-p have constant diagonal squared norm m-mu and span the unique (N-2,2) irreducible image: the standard (N-1,1) component vanishes because every vertex has exactly k-1 same-block neighbours. Schur scalar and trace d=N(N-3)/2 yield P(M,M′)=d(S-mu)/(|H|(m-mu)), and transitivity plus symmetry give both exact sharp endpoint norms. Counting labeled intersection tables gives the stated probability polynomial. For fixed k, each factorial-moment pattern with one chosen pair in each of r reference blocks contributes lambda^r; every other fixed component pattern has at least one extra co-location constraint and total O_k,r(1/n). Bounded second moments imply UI of centered absolute deviations. Poisson recursion then gives the displayed coefficient; subsequent k->infinity Gaussian limit is valid only after fixed-k n->infinity. Independently enumerated all partitions for (n,k)=(2,3),(2,4),(3,3),(4,2),(4,3), reproducing exact norm fractions 9/5,24/7,243/70,80/21,11178/1925. Direct full projector idempotence, trace and absolute row sums checked for the four cases with <=280 partitions. The original paper arXiv:2201.02887 Proposition 22 has a printed normalization issue: for (n,k)=(2,3), its displayed diagonal is 6/5 and trace 12 although rank d=9. The audited Gram formula has trace 9 and squares to itself. This printed defect is not used as proof of novelty.

## originality

FAIL

A decisive exact reduction was absent from the submitted comparison. The intersection table A of independent uniformly random partitions has precisely the distribution of the edge-count table of a degree-k bipartite configuration model with n vertices on each side: both give probability ((k!)**(2n)/((kn)!))/prod(A_ij!). Hence S=sum_ij binom(A_ij,2) is exactly the multiple-edge statistic Mbar of Angel--van der Hofstad--Holmgren (2019), Theorem 1.10, which already gives the Poisson law with even a quantitative total-variation error O_k(1/n) and mean mu. Filmus--Lindzey (2022), Section 9, independently established the same (kn-2,2) pair-overlap spherical-projector structure, though the displayed normalization in Proposition 22 has a trace discrepancy. Correcting that scalar by the routine diagonal trace, taking absolute row sums and applying the elementary Poisson centered first absolute moment directly produces the submitted fixed-k norm limit and the subsequent Gaussian iterated constant. The final claim is thus a short corollary of combined published general results, not an original independent theorem under the stipulated implication-based priority standard. Existing work also gives the zero-overlap special event. This rejects scientific originality without questioning the correctness of the result.

## value

PASS

The operator is a canonical multiplicity-one harmonic Fourier projection, and its sharp L1/L-infinity amplification coefficient is a mathematically motivated natural quantitative invariant. A corrected trace normalization and explicit limiting constant can be useful when applying existing hypermatching spectral theory. The exact fixed-block-size formula has a genuine interpretation independent of complexity claims or a joint-limit theorem. This gives mathematical utility even though the central claimed asymptotic lacks scientific originality because it is directly implied by earlier general results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
