# Self-review

## Correctness — PASS

The domain is every prime power \(q=6s+1\); the counted objects are exact-index-six permutation-polynomial functions vanishing at zero, modulo quasi-multiplicative equivalence. Fan's published Theorem 4.5 bounds degree by five and period by twelve. The exact modular fixed-point calculation uses Fan's Lemma 4.1 and Burnside/Möbius formula, and checks six **prime** interpolation arguments for each residue class. Every residue polynomial is therefore rigorously determined by six evaluations; this is not a finite-experiment extrapolation. An independent direct-orbit check matches three small fields. Dirichlet's theorem supplies infinitely many admissible primes in each residue class, and comparison of the residue-six, residue-twelve and residue-four constituent polynomials proves sharpness of the period. The bundled standard-library checker passed its exhaustive finite tasks. The general degree bound is a cited, rather than independently reproved, premise.

## Originality — PASS with stated residual risk

The closest primary paper is Fan, arXiv:2611.16944v1, which gives the general algorithm and the **upper bound** twelve, but not the six explicit index-six formulas or the exact minimal period. In particular, index-four formulas in Fan show that the universal even-index bound need not be sharp, so exact period twelve at index six is not an immediate logical consequence of the general bound. The general algorithm makes the computation possible, and novelty is **not** claimed for that method. Garg et al., arXiv:2503.20982v3, consider selected low-term quadratic-extension classes instead of the full index-six function. Indexed equivalent-formulation, broader-coverage, table and implication searches did not locate a containing result. An unindexed independent calculation may nevertheless exist.

## Mathematical value — PASS

The smallest squarefree composite index is a natural next unresolved closed-form case after Fan's prime-index and index-four evaluations. The exact formula identifies all six arithmetic phases and proves that the bound \(2\ell\) on the quasi-polynomial period is genuinely attained at this index; it distinguishes three-adic and two-adic divisibility regimes in a way the general degree/period theorem leaves undetermined. This is a complete, motivated exact invariant rather than an arbitrary finite-field census or a routine isolated substitution.

## Scope and limitations

The proof assumes Fan's classification and quasi-polynomiality theorem. All interpolation counts are finite exact-arithmetic certificates, not independent proof of the source theorem. The calculation covers only zero-constant, exact-index-six classes; it does not claim all polynomial functions of index at most six or classes with nonzero constant term. Primary literature inspected includes the complete counting sections of Fan and the relevant equivalence section of Garg et al. Residual risk: possible unindexed earlier derivation of the same explicit period and formulas.

Self-review: passed. Independent audit: not yet performed.
