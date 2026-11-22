---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

**Proof review.** The classification uses the exact sequence \(1\to1+\mathfrak m\to R^\times\to\mathbb F_q^\times\to1\), where the kernel is elementary abelian of exponent \(p\), and the unique prime-to-\(p\) complement in each residue-unit lift. The exceptional case is reduced to the verified power identity \(f_{1+w,a}^p(x)=x+pa\); the binomial coefficient vanishes on the radical for odd \(p\). Each case gives the exact disjoint-cycle structure and map multiplicity; their sum is \(q^3(q-1)\). The isomorphism conclusion uses the standard two-type classification of length-two commutative chain rings at fixed odd \(q\).

**Executable independent small-case checks.** Execute `python3 verify_chain_affine.py`. The script constructs actual finite rings, enumerates all affine permutation maps with invertible multiplier, computes the disjoint-cycle decomposition as point permutations and compares with the formulas. Checks cover \(\mathbb Z/9\mathbb Z\), \(\mathbb F_3[\varepsilon]/(\varepsilon^2)\), \(\mathbb Z/25\mathbb Z\), \(\mathbb F_5[\varepsilon]/(\varepsilon^2)\), \(\mathrm{GR}(9,2)\), and \(\mathbb F_9[\varepsilon]/(\varepsilon^2)\), with affine group sizes \(54\), \(500\), and \(5832\) for each pair. All six comparisons passed and produced `LENGTH_TWO_AFFINE_CYCLE_CENSUS_VERIFIED`.

**Limits.** The finite checker does not certify the infinite statement, prove novelty, or provide independent scientific validation. The theorem excludes \(p=2\). The recorded publication comparisons distinguish already known prime-cyclic cases from the new uniform nonprime-residue-field statement; earlier equivalent accounts cannot be excluded absolutely.
