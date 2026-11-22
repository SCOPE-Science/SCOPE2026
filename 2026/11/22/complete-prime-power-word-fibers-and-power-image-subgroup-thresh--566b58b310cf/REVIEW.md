# Scientific review

## Correctness — PASS

For the semidirect-product group with regular cyclic top action, the identity \((v,i)^{p^b}=(\sum_{r=0}^{p^b-1}T^{ri}v,p^bi)\) is checked directly. The characteristic-\(p\) polynomial identity and the single-Jordan-block structure of \(T-I\) determine kernel and image of every such sum. Counting top-coordinate lifts yields all prescribed-root fibers, including the exceptional identity fiber. Summing the disjoint top fibers yields the exact image count; unequal coset sizes force the non-subgroup threshold, and dividing by group order proves the convergent lacunary limiting series. Independent direct multiplication checks passed 22 small finite cases (captured in `check_power.out`); they are not treated as a proof of the unbounded family.

## Originality — PASS, qualified

Riedl (2009) establishes the cyclic regular wreath-group setting and standard Hall power identity but addresses automorphisms, not all-root fibers or the power-image filtration. Riedl (2014) treats upper central series; only an abstract/publisher preview was accessible, leaving a documented overlap risk. Kundu–Mondal (2020) develops prime-power and conjugacy-class enumeration in symmetric-top wreath groups, not the cyclic-top all-target fiber census. The established rank-one norm calculation for \(C_p\wr C_p\) is recognized as a special case, and so is not counted as new. Relevant published power-fiber results in radical-square-zero quiver unit groups have structurally different multiplication. Targeted mathematical-record searches and claim-level comparisons found no result implying the full all-depth formula; a prior implicit or unindexed derivation remains possible.

## Value — PASS

Power-word images are natural group-theoretic invariants. The all-target fiber formulas supply complete enumeration for a growing family of nonabelian finite \(p\)-groups, while the sharp failure and eventual restoration of subgroup closure gives a structural distinction invisible from element-order counts. The lacunary density series gives a quantitative limiting hierarchy at fixed prime, coefficient-field size, and power depth. This is an infinite natural family, not a selection of arbitrary small cases.

## Scope and independent validation

The base is elementary abelian of characteristic \(p\), the top action is one regular cycle, and only prime-power exponents are asserted. Earlier literature may include implicit equivalents, especially the inaccessible 2014 full text. The included checker supports finite cases only.

Self-review: passed. Independent audit: not yet performed.
