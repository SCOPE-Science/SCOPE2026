---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Acyclic orientations give the distinct vertices (strict maximizing directions realize exactly the sign orientations with a topological order); opposite orientations give opposite points, so the mean is zero. A cycle exists precisely when two complete terminal paths are coherent in opposite directions. The two admissible sign cubes, one excluding each coherent direction, overlap on the all-mixed arrays, giving the stated N. For distinct edges on one path, the same-sign product sums are +2 on coherent words and -2 on mixed words, with completion weights T_i and 2T_i-U_i. Across paths, the mixed-word single-edge sign sum is zero and only the two same-direction coherent pairs contribute, with T_ij completions each. Thus alpha_i=2(U_i-T_i)/N and beta_ij=2T_ij/N. Multiplication by the incidence blocks sends each all-ones vector to e_s-e_t, producing the stated formula with factor 1/4. For three equal paths the terminal coefficient in 4 Cov is 6/N; taking 2 times the trace gives the exact separation and the 12 ell*4^(-ell) leading excess. I also exposed vertices with every strict coordinate ordering, deduplicated the resulting doubled vertex coordinates and verified the full integer moment matrix for (2,2,3), (2,3,4), (2,2,2,3) and (3,3,3) with python3 /workspace/checks/theta.py. The check is finite; the sign calculation proves the full domain. The frozen checker was inspected but not executed.

## originality

PASS

There is exact prior overlap at K_{2,r}, the all-length-two boundary explicitly omitted from the new claim. The strongest inspected statements for longer/general theta arms give orientation or local flip counts, not this coordinate covariance or a theorem implying its terminal coefficient. The checked covariance results concern different families or sampling laws. No equivalent was located in the bounded search.

## value

PASS

The entire uniform vertex covariance is a natural geometric invariant, and the theorem treats overlapping cycles, including arbitrary unequal subdivisions. The covariance is not an enumeration of a size or trace: all nonlocal coordinate correlations reduce to the terminal pair. In fact writing A_i=D_i+1, the terminal numerator in 4 Cov has a strictly positive contribution from monomials supported on at most r-3 arms, with coefficient 2(r-|S|)(r-|S|-2) on the monomial indexed by S. This illustrates that the correction is genuinely nonzero and allows a weighted-Laplacian interpretation with a terminal edge. This information is not supplied by a cactus decomposition or by the known orientation count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
