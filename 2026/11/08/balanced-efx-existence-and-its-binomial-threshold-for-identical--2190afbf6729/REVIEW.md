# Scientific review

## Correctness

**PASS.** Formula (1) is derived from a complete pairwise EFX test: removing a low item is the strongest test whenever the target bundle contains one, and removing a high item is the test for all-high target bundles. For \(H>2L\), integrality forces all non-all-high bundles to have one common high count, while an all-high bundle can coexist with them only in the top layer. Balanced constructions prove sufficiency. Multinomial enumeration establishes formula (2), and the binomial CLT, Chernoff bounds and the local CLT give (3)--(5). The exact checker tests 34,080 count profiles, 936 existence parameters, 312 count formulas and 38 independent labeled-allocation cases. Tests are finite evidence, not the reason for the general theorem.

## Originality

**PASS, qualified.** The closest balanced-allocation work proves existence of EF1 plus constrained fPO, not EFX; an unconstrained EFX result for two item types does not imply the same after exact cardinality constraints are imposed. Searches for balanced EFX with identical bivalued valuations, a high/low contrast threshold, modular high-good counts and probabilistic phase transitions did not reveal the particular classification or Gaussian window. Related unpublished/unindexed formulations remain an originality risk.

## Mathematical value

**PASS.** Exact cardinality balancing is motivated by equal team drafts and course-seat assignments, while EFX is the strong deletion-robust fairness requirement. The theorem completely classifies feasibility in a natural homogeneous bivalued domain, gives exact labeled allocation counts in the failing contrast regime, and identifies a sharp probabilistic phase transition (including arithmetic resonances) despite unconditional EF1. The contrast \(H=2L\) and high-good density \((r-1)/r\) are intrinsic to the EFX inequalities, not arbitrary numerical cutoffs.

## Closest literature and limitations

Kawase--Mahara (arXiv:2603.05956) and Cookson--Shah--Verma (arXiv:2608.06325): balanced EF1/fPO. Gorantla--Marwaha--Velusamy (arXiv:2202.05186): unconstrained two-type EFX. Davidiuk et al. (arXiv:2601.03438): unconstrained two-type EFX/PO. The present finding is restricted to identical positive two-value additive preferences, exact equal bundle sizes, and fixed bundle size in the asymptotic model. No independent expert validation was performed.

Self-review: passed. Independent audit: not yet performed.
