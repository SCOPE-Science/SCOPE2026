# Independent mathematical audit

## correctness

PASS

Under the outgoing attack convention each weak component of a total map is a directed cycle with in-trees. Leaf-to-root induction forces all off-cycle labels in every complete (hence preferred) extension. An IN child forces its cycle parent OUT; the remaining free runs then alternate and a blocked cycle has one stable and one preferred assignment, coinciding even for a blocked self-loop. An unblocked even cycle has two alternating preferred/stable assignments; on an unblocked odd cycle any accepted cycle vertex would force alternating predecessors for defense, incompatible with conflict-freeness. Its only preferred component assignment omits the cycle and is not stable. Components factor, including the empty mapping whose sole extension is empty. Labelled trees give R=z exp(R) and U=z exp(R−U); when decorating a cycle vertex, R and U include that vertex and count all and free decorations respectively. The log contribution of blocked cycles is −log(1−R)+log(1−U); the marked unblocked even cycles contribute −(y/2) log(1−U²). Exponentiation yields the claimed EGF. For transfer, R has the square-root branch at 1/e; strict triangle inequality for its all-positive coefficients and continuation by the implicit equation exclude other circle singularities. On that closed convergence disk, the nonnegative free-tree coefficients bound |U| by U(1/e)=w<1. The local inverse U exp(U)=R has nonzero derivative there, so the numerator factors in the fixed-k and y=1 extractions are analytic in the square-root variable on a dented neighborhood. Their values at 1/e multiply the leading inverse square-root term. This yields the unconditional masses and the normalized conditional Poisson law. Independent direct tests over every map and vertex subset through n=6 confirmed family equality iff existence and the multiplicity histogram, including at n=6 the counts {0:20565,1:19836,2:5700,4:540,8:15}; an exact formal expansion through n=8 matched both displayed sequences. Replay: python3 /workspace/branches/747001a5-321b-478e-adf5-e9fad4fd69f4/independent_check.py. The replay corroborates the bounded data; it is not an all-order certificate.

## originality

PASS

The accepted contribution is the labelled multiplicity census and its asymptotic identification for a uniform total one-out attack map. Existing parity characterizations, classical functional-digraph decompositions, agreement criteria, and an earlier one-in partial-pointer model give substantial tools and analogous statements. The numerical family of limiting mass functions is already present in that earlier model after p=1−w; it is not a new probability law. The prior theorem concerns a different random variable on a different finite ensemble and does not identify this model's law or give the exact EGF. The distinction rests on branching children that can force cycle vertices, not terminology alone.

## value

PASS

The uniform labelled total mapping is a natural sparse model that permits arbitrary competition from incoming attacks despite fixing one outgoing attack per vertex. An exact bivariate census distinguishes preferred–stable agreement, uniqueness, multiple stable outcomes, and nonexistence, quantifying the otherwise unseen effect of tree blockage. It is materially different from an existence threshold, a cycle parity observation, or an arbitrary sequence of small counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
