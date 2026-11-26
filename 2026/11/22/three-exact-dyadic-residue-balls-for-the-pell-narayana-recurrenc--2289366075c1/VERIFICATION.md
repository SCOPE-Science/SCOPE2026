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

The companion matrix advances (P_n,P_{n+1},P_{n+2}) by one index. Exact recomputation gives entry valuations at least 1,2,4 for K^h−I at h=3,6,24, and the four rows of first and second Mahler coefficient valuations are (1,5),(3,5),(9,13),(9,15). For a row with matrix divisibility exponent s and first coefficient valuation d, uniform convergence follows from v2(c_j)≥sj and the integral binomial basis. Vandermonde and i·binom(t−u,i)=(t−u)binom(t−u−1,i−1) give the binomial difference bound v2(t−u)−floor(log2 j). The j=2 valuations exceed d+1. For j≥3, floor(log2 j)≤j−2 proves the required sj≥d+1+floor(log2 j) in each row (check at j=3 with this stronger linear bound, then slopes s≥1). Thus the linear term determines the exact difference valuation. The normalized maps induce injections of Z/2^k into itself and hence bijections for all k. With continuity and compactness this proves the four full branch disks, including the two complementary 512-disks centered at 258 and 2. For containment, the two nonzero classes mod 3 are odd, n=6t lies in 8Z2, and n=6t+3 has constant 2 modulo 256 since its next three coefficients are 256,29184,3330304 and all later ones are divisible by 4^4. Nonnegative parameter lifts of any finite residue yield infinitely many indices. The even disks collide only at k=1; from k=2 onward all three projections are disjoint, giving the stated cardinalities and Haar measure 161/256. The all-level argument does not depend on the finite recurrence period test.

## originality

PASS

The closest primary work has exactly the same recurrence and seeds, and gives prime-power periods, but not the residues within the periods. The closest prior three-disk theorem concerns a different, second-order recurrence, and analogous Narayana-cows results concern coefficient 1 rather than 2. The supported distinct claim is the exact image and its containment and surjectivity, not the period theorem or the standard Mahler machinery.

## value

PASS

For the natural Pell–Narayana recurrence, periods leave open a different arithmetic question: which target values are achievable to arbitrary dyadic precision. The answer isolates a particularly thin even disk at level 256, distinguishes infinitely many hits from unattained residues, and supplies an exact density and all finite-precision counts. The isometric-subsection method also explains how the thin disk is filled, rather than extrapolating it from a finite scan.

The dated certificate retains the supplied scientific assessment, sources and limitations.
