# Scientific review: sparse third-order phase fingerprints

## Correctness

PASS. Phase words split bijectively into the displayed zero-first and one-first families. Each pattern count is calculated by choosing the final one and counting preceding zeros (or pairs of zeros). The sole possible second-order ambiguities satisfy an explicit linear Diophantine equation with exactly \(\gcd(a,b)-1\) solutions; at every such pair, subtracting the exact `001` formulas gives \(bm s(a-s)/2>0\). The single four-run counterexample is certified by comparing all fourteen scattered counts up to length three, and multiplicativity of truncated subsequence generating series propagates it through repetitions. All quantified boundaries are included. The verifier's finite checks are not substituted for the proof.

## Originality

PASS under the inspected evidence, with residual bibliographic risk. The closest primary literature is Poovanandran–Simpson–Teh (arXiv:2110.14858), which averages over rotations; Rigo–Stipulanti–Whiteland (arXiv:2201.04603), which studies general binomial complexities; and Vivion (arXiv:2509.11172), which proves second-order injectivity for different classes. Those inspected statements do not imply the sparse two-counter, gcd-sensitive threshold and quantitative third-order collision gap for all two-run periodic words. Searches for binomial equivalence of conjugates, three-binomial cyclic phase recovery, sparse `01`/`001` signatures, and related reconstruction found no decisive covering source. Previously established second-order gcd collisions are acknowledged as background rather than counted as the new contribution. The surviving risk is unindexed or differently named special-case work.

## Mathematical value

PASS. The question is a natural constrained scattered-subsequence reconstruction problem: how little order-sensitive information determines the cut position in a periodic circular binary signal? The answer is uniform in repetition count and both run lengths, exhibits an exact arithmetic obstruction at second order and an explicit optimal next order, supplies a two-coordinate fingerprint instead of the full third-order deck, and shows by a primitive four-run example that the rigidity is structurally special. These features are mathematically more substantive than simply incrementing a previously computed complexity parameter.

## Limitations

The theorem concerns complete-period observation windows and one zero-run plus one one-run per circular period. Third-order collisions at other lengths and for four-run periods are not classified. The source comparison is not an exhaustive guarantee against unpublished or unindexed equivalent statements. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
