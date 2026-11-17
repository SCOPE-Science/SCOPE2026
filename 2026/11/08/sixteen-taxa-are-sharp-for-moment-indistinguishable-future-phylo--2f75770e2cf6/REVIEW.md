# Revised scientific scope and evaluation

## Correctness

The final claim is the exact full-distribution generating-polynomial swap identity and its quantitative third-moment consequences, not the previously claimed first nonidentifiability threshold. Equation (4) of RESULT.md follows by conditioning on simultaneous extinction of the two daughter subtrees. Multiplication verifies equation (1) symbolically, and differentiating at z=1 verifies equality of the first two moments and the exact third moment gap. The four-leaf explicit polynomial is checked by the assigned `checker.py` with exact bivariate arithmetic and by its independent enumeration of 2^16 survival masks; those checks are finite and are not a substitute for the general algebra.

## Originality

Earlier October 18 and 26 published fixed-size rarefaction theorems prove the same sharp sixteen-leaf first collision, unique witness, and extension to larger leaf counts. Conditioning independent Bernoulli survival on the surviving leaf count gives a uniform fixed-size rarefaction sample, so equality of the entire fixed-k mean and second-moment sequences is equivalent (by Bernstein-basis independence) to equality of the full parameter-dependent extinction moments. That earlier complete result is decisively covering and explicitly disclaimed. The surviving candidate is the distinct full **generating-polynomial identity** q^(2s) z(1-z)(F_U-F_V)^2 for arbitrary two equal-size rooted subtrees, with a strict third-moment square law and the complete polynomial score-five separation. The inspected sharp rarefaction papers contain the two-moment interchange but not the exact full-distribution polynomial identity. The general extinction-distribution recursion of Faller–Pardi–Steel is prior foundational machinery, and unindexed algebraic equivalents remain a best-of-knowledge risk.

## Value

The full-distribution factorization is an exact structural lemma on a natural phylogenetic diversity law, giving both an obstruction to first-two-moment inference and a computable strict third-moment witness uniformly in extinction probability. Unlike the already known sixteen-leaf enumeration, it applies to arbitrary equal-size subtree pairs, gives the entire distribution difference, and controls all higher-moment comparisons. It is a motivated, reusable algebraic identity rather than a new name for the covered finite cutoff. No empirical detectability claim is made.

## Scientific limits

Unlabelled nonplane rooted binary shapes, all edges unit length, no stem, homogeneous independent leaf extinction, equal sizes of the two swapped subtrees. Formula (2) can vanish at parameters for which the incoming-edge means agree; only the explicit C/D witness is separated for every interior q. The published earlier census is not asserted to be independently rediscovered or new. Published work is cited in RESULT.md. No external expert attestation is claimed.
