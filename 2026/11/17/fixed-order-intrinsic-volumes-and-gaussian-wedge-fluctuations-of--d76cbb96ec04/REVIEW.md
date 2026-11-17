# Scientific review of the fixed-index White Whale intrinsic-volume law

## Correctness

PASS. The intrinsic-volume-to-random-wedge identity uses the established zonotope formula with correct Steiner normalization and exactly accounts for repeated and zero Boolean columns. The Bernoulli row Gram expectation is \((I+\mathbf1\mathbf1^{\mathsf T})/4\), with inverse \(4(I-\mathbf1\mathbf1^{\mathsf T}/(k+1))\). The binomial fourth moment yields \(\operatorname{Var}(U)=2k/(k+1)\), giving the Gaussian variance \(k/(2\cdot4^k)\) and relative expectation correction \(-k^3/[4(k+1)d]\). Concentration away from the singular determinant boundary makes Taylor expansion valid, and expectation of the third and fourth terms is \(O_k(d^{-2})\). The accompanying reproducibility checks establish fifteen finite exact-method comparisons and ten finite-order moment identities. Those finite checks do not replace the proof.

## Originality

PASS, with historical-priority uncertainty. The principal 2022 White Whale source addresses vertex and edge counts, not this fixed-order Euclidean metric asymptotic. Joós--Lángi and Breiding--Bürgisser--Lerario--Mathis prove the general wedge-based intrinsic-volume formula, which subsumes the starting exact reduction; that reduction is not claimed as original. The new claim is the joint all-fixed-order explicit Gaussian fluctuation and sharp relative \(1/d\) coefficient, including the limiting intrinsic-volume ratios. Semantic searches covering random Boolean Gram determinants, resonance zonotopes, aliases, broader coverage, and exact tables found no direct statement of those constants. Unindexed equivalent formulae and the routine general delta-method framework are remaining priority risks; the discrete moment evaluation and second-order coefficient are not stated in the inspected primary works.

## Mathematical value

PASS. The White Whale is a canonical zonotope with exponentially many generators and extremely large vertex counts, so exact fixed-order Euclidean intrinsic-volume behavior is a natural invariant independent of its hard vertex enumeration. The result gives every fixed-index coefficient a uniform-in-d asymptotic template, a sharp relative correction, a nondegenerate Gaussian law for the contributing parallelotope sizes, and an explicit nonorthogonality hierarchy \(\sqrt{k+1}/2^{k/2}\). The two-dimensional limit \(\sqrt3/2\) is a geometrically interpretable persistent angular correlation, not an arbitrary parameter slice or a restatement of the general sum formula. The theorem does not assert anything for growing index.

## Closest prior literature and limits

- Deza--Hao--Pournin (arXiv:2205.13309): same canonical object, different combinatorial invariants.
- Joós--Lángi (arXiv:2206.03204): general zonotope Steiner formula, credited as inherited.
- Breiding--Bürgisser--Lerario--Mathis (arXiv:2109.14996): general random-wedge/zonoid framework, without the specific second-order Boolean constants.
- Previously published White Whale width and incenter claims: distinct invariants; no implication to the present asymptotic beyond general geometric background.

Fixed-order asymptotics only, finite checks not infinite proofs, and unindexed equivalent Bernoulli determinant calculations remain possible.

Self-review: passed. Independent audit: not yet performed.
