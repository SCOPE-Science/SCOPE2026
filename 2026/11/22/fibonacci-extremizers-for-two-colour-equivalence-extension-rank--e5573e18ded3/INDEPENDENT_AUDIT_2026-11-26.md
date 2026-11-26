# Independent mathematical audit

## correctness

PASS

The theorem and proof survive unchanged. Induction on remaining depth separates a marked position into the per-colour capacities of its marked classes and the rank of the unused union: an existing-class move spends one unit of one capacity, and a new-class move uses a witness inside the unused union. For the one-colour projection, consecutive fresh-class requests require distinct capacities at least t,t-1,...,1; conversely, taking the largest free class on each fresh request meets those bounds even when some intermediate moves go to marked classes. Applying this to each named colour gives the sharp size lower bound and forces both staircases at equality. The first red and blue requests force the unique classes carrying each maximum t and require the other colour at least t-1. A shared maximum leaves a level-(t-1) host. For distinct maxima the classes must be (t,t-1) and (t-1,t); a second red fresh-class request after red must use the latter, leaving a level-(t-2) host. Both branches suffice by the separation lemma, are disjoint, and are uniquely peeled; t=0 and t=1 give 1 and 2. The lower bound at t+1 rules out larger rank. The frozen finite checker did not implement its stated full marked-profile sweep: line 72 tests r+b>0 (b the total blue capacity), not whether red or blue was actually selected. For example, the empty selection in a blue singleton is wrongly marked. The replacement evaluates the direct game with separate marked/free lists and classifies by actual selection; its fresh execution reproduces 573 host types, 24,963 profile visits and 199,704 depth comparisons, and the complete staircase-coupling census through t=5. The replacement log is the actual new output.

## originality

PASS

The uncoloured staircase law and the general rank definition are available premises. The distinct surviving claim is the classification of compatible couplings of the two forced staircases and its Fibonacci count. The same marginals can fail rank t, so the uncoloured theorem does not imply this classification.

## value

PASS

The equality classification answers which pairs of individually optimal resources can coexist in a single minimum universal-extension host. This is a natural structural problem not answered by the sharp numerical lower bound; the unique peeling rule and exact named-colour isomorphism census are mathematically useful beyond a finite count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
