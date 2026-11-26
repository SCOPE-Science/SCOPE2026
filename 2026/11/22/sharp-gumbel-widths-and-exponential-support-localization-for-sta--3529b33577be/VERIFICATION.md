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

The increasing prefix of v_j is emitted by the stack up to its last entry before the 1; the next larger entry (or the final flush) emits the 1 followed by that last entry. This gives v_(j−1). The translated differences have norm √(j(j+1)) and pairwise dot product zero (the j initial ones cancel the −j term against any later vector). Isotropic Gaussian scores are thus independent normals with the stated scales and with the origin also available. For k=n−j and bounded s=t_n²k/n, Mills' formula gives the tail ratio e^(−s)(1+o(1)) uniformly; the step size in s is t_n²/n. The inequality 1/a²−1≥2(k−1/2)/n follows from a=√(j(j+1))/n≤(j+1/2)/n and supplies a summable geometric majorant for the remaining layer. The total normal tail tends to e^(−x) since nφ(u)/u³ tends to e^(−x) with the stated c_n. On bounded marked rectangles the sum of rare-event probabilities converges to the product intensity; the total squared probabilities vanish since the maximal term is O(t_n²/n). The two sign bins are disjoint at one index, yielding independent Poisson limits via the same product expansion. One can truncate below a fixed low height and above a fixed large location and remove the cutoffs using the Gumbel lower tail and the geometric bound. The independent Exp(1) location marks then follow by the factorized intensities. The origin is negligible (probability 2^(−(n−1)) for each sign). Finally the chi-square radius has relative fluctuations O_P(n^(−1/2)), negligible at the t_n/√n spherical width scale, and does not change the indices.

## originality

PASS

Credit the stack-sorting simplex family and standard Gaussian extreme-value tools. The supported contribution is the joint canonical-metric width and marked support limit with its extra log-log shift, not the general use of a Poisson extreme process or a sum of two Gumbels. The strongest available same-object angle result and the closest width and rank-localization results do not give this joint law on available statements.

## value

PASS

The canonical permutation embedding is motivated independently of numerical enumeration and answers a different question from lattice equivalence. The result gives an exact subleading width correction and identifies which iterates expose the simplex in each sign. The coupled law distinguishes a localized boundary population from an iid estimate and gives more geometric information than a leading-order width alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
