# Scientific review: complete generating-subset spectra of cyclic Brandt semigroups

## Correctness — PASS

The exact domain is finite \(n\ge2\), cyclic order \(m\ge1\), and nonzero (zero-omitting) **unordered** subsets. The main proof shows: (i) strong directed support plus full closed-walk gain group is equivalent to generating the Brandt semigroup; (ii) for each divisor subgroup the potential equations uniquely describe its permitted labeled graphs; and (iii) divisor Möbius inversion selects precisely the full-group case. The directed cut inclusion–exclusion proves the explicit strong-graph formula. The first nonzero coefficient follows from Hamiltonian cycles and Euler's totient identity. All coefficients were independently enumerated via multiplication closure at four small parameter pairs and by exhaustive lifted-state reachability for \(n=3,m=2\); the general proof does not depend on those experiments.

## Originality — PASS under inspected comparisons

Gray and Ruškuc (2005, available public online 2007) §9, Corollary 9.4, and Gray (arXiv:1307.8280, 2013) §2, Corollary 9, recover only the minimum generating-set cardinality, not the complete subset-size polynomial. The related Brandt power-semigroup study addresses nilpotency indices of subsets as semigroup elements, not which subsets generate the Brandt semigroup. The exact all-size gain-subgroup refinement is not implied by the numerical minimum-rank statement alone. Classical strong-digraph reliability and graph-potential methods are explicitly credited as constituents, not independently claimed. Search limitations leave a nonzero risk of earlier equivalent counting formulas in gain-graph and completely zero-simple semigroup literature.

## Value — PASS

Generation reliability by subset size is a natural intrinsic invariant of finite semigroups. A complete formula for unbounded index number and arbitrary cyclic group order determines all cardinality strata and contrasts the trivial-group strong-digraph case with the genuinely arithmetic cyclic-gain obstruction. The Hamiltonian/totient coefficient gives a sharp, interpretable minimal-generator multiplicity rather than merely reproducing the known minimum size. Its use of a divisor transform gives a reusable way to count generation by group-valued edge walks.

## Limitations and sources

The result does not cover arbitrary nonabelian groups, conjugacy classes of generating subsets, or polynomial-time evaluation of the explicit inclusion–exclusion. The 1987 Gomes–Howie original and some general gain-graph literature were not inspected in full. Sources: Gray and Ruškuc, https://doi.org/10.1080/00927870500276676; Gray, https://arxiv.org/abs/1307.8280. Computational source is the attached standalone `CHECKER.py`.

Self-review: passed. Independent audit: not yet performed.
