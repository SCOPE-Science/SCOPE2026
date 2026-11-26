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

Each translation gives a modulation ONB, hence the full frame is p-tight and the least retained eigenvalue is p minus the largest deleted Gram eigenvalue. For a unit Rayleigh vector, the off-diagonal bound uses (sum |z_i|)^2−1 <= 4. Equality first forces all five moduli equal and nonzero, then all pair magnitudes equal to p^−1/2 and all phases align after diagonal rephasing. For distinct slopes, completing the square gives normalized Gauss phases epsilon_p chi(u_j−u_i) times omega to the power −(v_j−v_i)^2/[4(u_j−u_i)]. The cyclic exponent on three points is governed by d_1 d_2 (s_1−s_2)^2/(d_1+d_2), so it vanishes exactly for collinear triples. For p=3 mod 4 a phase ±i cannot be a p-th root; for p=1 mod 4 the alignment condition is exactly collinearity and positive triple signs. Fixing one slope gauge proves the equivalence to at most two disjoint cliques. Independent exact enumeration fixed one slope to 0 by translation, built square residues directly, and constrained the other six edge signs by their four signs at the anchor. It found no solution at 5,13,17 and witnesses at all nine eligible primes 29 through 101 (e.g. a distinct p=29 witness 0,1,3,5,6). For p>=109 a Paley triangle exists via its adjacent-pair intersection number; expanding three common-nonneighbor indicators gives (p−3−tau)/8. Points in the triangle contribute zero and the pair character sums each equal −1. Hasse gives |tau|<=2 sqrt(p) and the Paley least adjacency eigenvalue gives the Hoffman bound alpha<=sqrt(p). Since p−3>10 sqrt(p), the common nonneighbors contain an edge, giving the required K3 plus K2 graph. Finally rank <=5 and p>=29 leave the largest surviving frame eigenvalue equal to p, with condition number given by the square root of the eigenvalue ratio as stated.

## originality

PASS

The general five-column coherence inequality and the phase switching criterion are not new. The all-prime threshold and Alltop-specific complete equality characterization are distinct from the inspected strongest comparisons. An earlier Paley-41 record actually provides the identical five-slope witness at that prime; this is credited as prior finite-instance coverage, not as evidence against the threshold as a whole.

## value

PASS

The sharpness question is meaningful for deterministic robust frames: it specifies exactly when the readily usable coherence guarantee is the true worst-case guarantee. The arithmetic cutoff, complete collinearity/sign description and exact optimum condition number in the saturating regime replace numerical case checks with an all-prime mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
