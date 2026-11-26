---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

With counting input and probability output, character orthogonality produces the unscaled pair-sum energy. When the first pair sum s is nonzero, s³−3s ab determines ab from the cubic sum, hence determines the unordered pair even over nonprime fields. When s=0, evenness puts each antipodal pair into a fiber labeled by 2h(t), and isolated origin separates the diagonal (0,0). The trivial energy is 2S²−∑|f|⁴; the exceptional correction is four times the off-diagonal product sum for each block because there are two ordered representatives per nonzero antipodal pair. On a block of size n with pair masses s_i and total W, equal magnitudes within pairs and aligned products give the bound W²−(3/2)∑s_i²≤(1−3/(2n))W². Strictness within an occupied pair follows from the strictly increasing quadratic in its product magnitude on the nonnegative domain (unless the pair has zero mass); Cauchy–Schwarz forces all pair masses equal at positive W. For M≥2 the maximal coefficient is positive, so the strict sum-of-squares comparison forces precisely one nonzero block, of size M, with no origin mass. For M=1 there are no distinct-pair collisions and the ℓ⁴ term is minimized only by uniform positive magnitude on all q points. Cyclicity gives kernel size 2gcd(m,(q−1)/2) for t↦t^(2m). The numbers on the monomial line are fourth powers as explicitly scoped in the record, not literal operator norms. The supplied verifier was read, not executed. The recorded finite tests cover 81 maps and 648 seeded Gaussian-integer inputs. An independent exact pair-sum check reproduced 5/2 and the perturbed 29/18 in resonant examples over q=7 and q=13, including unequal sizes [3,2,1], and 25/13 for singleton blocks over q=13.

## originality

FAIL

The exact one-block variational problem and its complete extremizers already appear in the conic-erasure result 6b59f93aeabe. This covers every relevant block size over the same field: the split conic has (q−1)/2 antipodal pairs, so retain exactly n complete pairs. The conic's pair-sum identity equals the frozen block's identity on paired coefficients; subtracting 2W² from the known sharp energy gives exactly the frozen local bound and all equality cases. Relabeling by h creates several copies but no cross-block correction, since s³−3s ab resolves all collisions for s≠0 and h labels the s=0 blocks. With c*=1−3/(2M)>0 the remaining optimization is the elementary comparison ∑c_n W_n²≤c*∑W_n²≤c*(∑W_n)², with equality only in one largest block. Isolating the origin is a hypothesis that makes this direct comparison possible. The M=1 alternative is the usual collision-free quartic identity plus Cauchy–Schwarz, and the monomial specialization is the ordinary cyclic-group fiber count. No premise is that the antecedent already prints the identical multiblock theorem; the adverse conclusion rests on the direct reduction and scalar maximization, not keywords, publication dates, or inaccessible sources.

## value

FAIL

Sharp extension norms and their equality cases are natural invariants, but this particular exact law is mechanically transferable from the known conic optimization. The h-coordinate partitions an already understood collision into independent copies, and the only new global step puts a quadratic mass on the largest positive coefficient. The monomial values give applications of this rule and elementary kernel counts, not an additional nontrivial invariant. No surviving distinct valuable remainder was identified for a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
