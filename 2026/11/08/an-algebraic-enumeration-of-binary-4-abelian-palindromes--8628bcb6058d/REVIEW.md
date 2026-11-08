# Scientific review

## Correctness: PASS

The assertion is all-length and has two independent mathematical components. First, boundary conservation for contiguous factor counts reduces four-abelian equivalence under reversal to a mirrored three-letter boundary and one remaining independent antisymmetric four-factor difference. Second, an eight-state weighted de Bruijn matrix has exactly the stated determinant and reversal-trace rational function, whose Laurent constant term yields the algebraic generating function. The subdominant denominator polynomial has no root inside the half-radius disk; the square-root transfer gives the asymptotic. These implications are reconstructed in RESULT.md and their finite matrix identities are checked symbolically in verify.py. Exhaustive enumeration through length sixteen independently agrees. Computational checks do not substitute for the proof of the infinite statement.

## Originality: PASS (qualified)

Karhumäki and Puzynina (2014) analyze rich and poor classes of k-abelian palindromes, rather than the ambient enumeration of all binary 4-abelian palindromes. Cassaigne, Karhumäki and Puzynina's accessible full 2016 presentation contains general equivalence definitions, the \((4,2)\) poorness case, constructions and open factor-richness questions; no exact algebraic total-count generating function or square-root asymptotic is given in that inspected material. Searches for reversed 4-gram balance, the derived series, and the exact numerical sequence did not locate a dominating identity in indexed sources or published research records. The 2014 chapter is subscription-only in its full form; a related 2018 journal publication likewise could not be read in full. This is a genuine historical-priority risk, not evidence of a proved uniqueness claim. Results on substring counts and on palindromic duplications do not imply this exact enumerator.

## Value: PASS

This counts all length-n words satisfying the first binary k-abelian reversal condition that is not decided solely by endpoint symbols, and determines an exact singularity and asymptotic probability. It exposes a one-dimensional internal balance obstruction after boundary reflection, converting a priori several local constraints into a single global statistic. That is a natural complete enumeration of a defined finite language, not an arbitrary small-parameter census or a recomputation of a published table.

## Limitations

The characterization is binary and at level four only. It does not answer the separate extremal problem of how many distinct k-abelian palindromic factors can occur within one given word. Complete priority against inaccessible full publications cannot be guaranteed. No external audit or independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
