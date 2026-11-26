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

The largest permutation symbol has an increasing suffix after it (otherwise its neighbors form a triangle with it). If this suffix has length one the insertion is I1. If it has length at least two, no prefix symbol can exceed its last symbol, since that would create a four-cycle involving two suffix vertices and the maximum. Thus the last symbol is the second largest, and removing it and relabelling the maximum inverts I2. This verifies the unique encoding; the graph also determines the order of each pair of values. The insertions attach a leaf at the corresponding active endpoint, up to relabelling. With all inactive vertices required covered, I1 sends 01 to {00,11} and 11 to {10}, and I2 interchanges the roles of the two endpoints, sending 10 to {00,11} and 11 to {01}. Thus the even-stage state {00,11} survives exactly the complementary disjoint pairs. Repeating an insertion attaches to the nonleaf and adds one leaf; switching attaches to the active leaf and extends the internal spine without changing the leaf count. Consequently L=2 plus the adjacent equalities and diameter is n-L+1 for n>=3. Pair orientation differences (conditioned) or usual bit differences (unconditioned) give independent fair indicators by an invertible binary transform. The leaf-resolved count, strict decrease up to the zero cutoff, and both diameter laws follow; the conditional mean and variance are 3m/2 and (m-2)/4, giving the asymptotic Gaussian limit for m>=3. Odd order is impossible and n=2 is the single matched edge.

## originality

PASS

The distinct result is the perfect-matching filter and resulting conditional finite laws and change in typical diameter for the uniform tree-permutation ensemble. The encoding, caterpillar geometry and unconditional distributions are credited to Acan and Hitczenko. The strongest distinct indexed matching comparator is for a different ensemble and does not establish this filter or diameter shift.

## value

PASS

Perfect matching is a natural global constraint with nontrivial consequences in this random caterpillar model: it forbids equalities within every disjoint insertion pair, lowering the number of leaves and changing diameter at linear scale from about n/2 to 3n/4. The local word criterion and leaf-resolved probabilities explain the mechanism and quantify the conditional bias beyond the already known unconditioned binomial law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
