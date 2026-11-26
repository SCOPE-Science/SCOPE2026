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

Final repaired RESULT.md: the rank reduction now requires an i.i.d. sample with independent continuous coordinates, or a uniform pairing permutation directly. The frozen assumptions said independent pairs without explicitly requiring common margins, which is insufficient as written: if all X_j,Y_j are independent Uniform(2j,2j+1), then both rank orders agree deterministically and Q_{1,1}=0, contradicting the proposed mean on that sampling interpretation. Exchangeability of each continuous common-margin sample plus independence of the two samples gives exactly the required uniform pairing. The uniform-permutation theorem and formulas are unchanged. Independently rederived their exact computation: group ordered signed positions by the equality partition of row indices; permutation images are uniform injective labels and contribute denominator (n)_m for m blocks. Compute the injective character sum by adding the last label unrestricted (multiplying by n times its order-divisibility indicator) and subtracting each possible collision by merging its weight with the relevant previous weight. This recursion avoids the frozen coarsening code. Grouping by the multiset of block positive/negative occupancies has total frequencies 2, 15, 203 at degrees 2, 4, 6. Exact symbolic reduction of the alternate recurrence verifies the mean, variance and all three centered moments and differences (replay: /workspace/branches/independent-replays/audit_rank_exact_recurrence.py); at n=9 it gives 1591/768, 525/256, 20871/8960. Signed multiplicities cannot exceed three in absolute value, so only exact character order three adds nonzero frequencies to the zero-sum block filter for odd n. The negative K₁−K₀ and the positive-coefficient numerator of K₂−K₀ at n=9+t prove strict distinction when the classes occur, and leading terms give the limit. Frozen checker read, not executed. Reproducing the alternate exact sums certifies the symbolic identities, not any assertion for nonuniform permutations. Only RESULT.md changes; the supplied uniform-permutation checker and its scientific reproducibility notes still apply.

## originality

PASS

For the repaired scope, the finite-sample degree-six Fourier-energy calculation and its three strict arithmetic classes were not found in the strongest related findings inspected. Neither the standard rank-null reduction, the general equality-partition method, nor the first two moments alone is credited as the distinct contribution. Specifying the i.i.d. rank-null hypothesis does not change the exact theorem compared.

## value

PASS

Fourier energies of a rank pairing are natural distribution-free null components. Equality of means and variances does not make these modes interchangeable at finite sample sizes: the first differing centered moment separates exactly three frequency types when 3 divides n, with strict ordering in opposite directions for one versus two resonant slots relative to the generic case. This exact calibration fact can matter when selecting or comparing modes. It does not establish power or an omnibus null law. The repaired rank hypothesis preserves that application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
