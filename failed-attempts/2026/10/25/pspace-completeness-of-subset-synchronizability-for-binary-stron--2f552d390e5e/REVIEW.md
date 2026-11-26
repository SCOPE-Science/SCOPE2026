# Independent mathematical audit

## correctness

PASS

The stated decision theorem is correct. In the implicit subset graph a shortest path to a singleton uses at most 2^|Q|−1 transitions; the current subset and an |Q|-bit counter suffice for nondeterministic polynomial space. Empty input subsets never reach a singleton and singletons accept the empty word. For hardness, the frozen two-copy synopsis omits the uniformity issue in Vorel v4 Lemma 4, where the distinguished index is chosen in reference to a reset target. It is not a self-contained uniform reduction as written. The cited Vorel v1 provides a uniform alternative: Lemma 5 maps the unrestricted instance to a transitive instance in both directions using 4|Q|+2 states and |X|+2c letters for c strongly connected components, and Lemma 2 uses a complete binary pointer automaton with |Q||X| states and preserves synchronization and strong connectivity. In the latter construction the pointer stays common to the entire current subset; reading only the applied letters decodes any binary witness, and original letters can all be simulated from the reset pointer. Thus the exact many-one conclusion does not depend on the abbreviated later reduction. No computational certificate is required.

## originality

FAIL

The complete finding is already Theorem 10 of Vorel arXiv:1403.3972v1 and Theorem 4 of v4. There is no new parameter restriction, complexity conclusion or independently new reduction in the frozen record.

## value

FAIL

The published restricted complexity theorem is useful, but the submitted finding is a short restatement of it with a less complete hardness synopsis, not a new theorem, independently useful exact invariant, or stronger analysis. The elementary space bound and summary of the cited reductions do not add a mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
