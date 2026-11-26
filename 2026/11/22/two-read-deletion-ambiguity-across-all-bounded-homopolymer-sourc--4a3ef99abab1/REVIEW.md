# Independent mathematical audit

## correctness

PASS

Cai et al. Proposition 9 gives exactly two distinct common deletion outputs precisely for opposite alternating phases, with the block forced by the first and last disagreements. For either endpoint of the block, one phase extends the adjacent context run if its symbol is in the selected pair; thus the only forbidden contexts are those whose adjacent run has length r in either of the two symbols. A fixed terminal symbol and run length r contribute z^r/(1−(q−1)S_r); subtracting twice this from the all-context series gives H. Since L≥2 the interfaces cannot coalesce, and multiplying by the two independent contexts and one unordered choice of symbols gives the bivariate count with no overcounting. The unique smallest-modulus pole is simple for H and double for the edge series: equality in the triangle inequality forces all summands, including z and z², to align with the positive real axis. The fixed-span/total coefficient ratio gives the stated geometric law; differentiating in u gives convergence of the mean to (2−R)/(1−R). Comparing the double-pole edge asymptotic to the single-pole vertex asymptotic gives the stated linear mean degree constant. The frozen scripts were inspected, not executed: the direct one checks total edges and observed edge structure, not individual expected span counts. A separate enumeration tested span counts at 42 parameter/length points, including 69,18,3 for spans 2,3,4 at q=3,r=2,n=4. Replay: /workspace/branches/8394f34b-b488-4f62-8bd9-33c79cb55a7c/independent_bounded_check.py and bounded_enumeration.txt in the same directory. The finite test is corroboration only.

## originality

PASS

Credit is for the finite run-cap r≥2 enumerator and its run-cap-dependent consequences, not the Type-A characterization, the unrestricted count or its geometric limit. The inspected matches do not cover the required finite-cap boundary compatibility.

## value

PASS

The two-read exclusion graph is a natural reconstruction object; enforcing a maximum run length changes both the finite adjacency counts and their asymptotics. An exact all-length, all-span formula quantifies how localized ambiguity is for a uniformly sampled edge and provides an exact linear mean-degree benchmark beyond the unconstrained case. It does not solve an independence-number problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
