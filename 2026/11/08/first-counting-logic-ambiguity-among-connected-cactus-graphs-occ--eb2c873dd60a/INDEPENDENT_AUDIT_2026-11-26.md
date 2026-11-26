# Independent mathematical audit

## correctness

PASS

A connected cactus has a tree of vertex/block incidences. Pruning an end block leaves a smaller cactus, or a singleton when there is only one block; edge and cycle augmentations are exactly the inverse operations and preserve the cactus condition. In the canonical rooted encoding an edge has one child and a cycle's rooted cyclic order is preserved up to reversal. Sorting branch encodings and minimizing over all roots therefore gives precisely one code per isomorphism type, including for one-vertex cacti. With a global palette the old color embedded in the new key makes the union partition refine monotonically; a step with unchanged class count is stable. Comparing histograms then gives exactly C²-equivalence. Separate standard-library enumeration and exact color refinement reproduced the cactus counts (1,1,2,4,9,23,63,188,596,1979,6804,24118), no collisions through order 11, and only two doubletons at order 12, giving 24,116 classes including 24,114 singletons. It emitted the exact four frozen graph6 strings. The two distinct representatives per class are nonisomorphic; the first pair also has different multiset of block sizes. These are pairs within connected cacti, not a test for partners outside the class. The frozen script only asserts the expected number of collisions conditional on finding any, but its output and the unconditional independent census both show the two at order 12.

## originality

PASS

The established statement is the minimum order and exact doubleton census when both graphs are connected cacti. Global nonidentification and leafless bicyclic doubleton classifications give genuinely close earlier examples with one cactus, but not two. Known cactus totals and general color-refinement theory are prerequisites, not this census. The exact catalogue match is the record under review, not a distinct antecedent.

## value

PASS

Connected cacti provide an elementary extension of trees in which cycles may change what counting logic can distinguish. Knowing the first order at which two members of the class agree on all C² sentences is useful separately from global nonidentification; the prior six-vertex cactus with a non-cactus twin shows why those questions differ. The sharp cutoff and two explicit, structurally different types of collisions give exact benchmarks for structural extensions of tree identification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
