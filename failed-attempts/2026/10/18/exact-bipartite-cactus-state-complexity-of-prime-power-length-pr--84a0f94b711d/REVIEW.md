# Independent mathematical audit

## correctness

PASS

After restricting to one letter, any accepted length N at least the number of states has a run containing a simple directed cycle. Repeating it advances the length by the LCM P of the usable simple-cycle lengths, so within each residue modulo P acceptance, once attained above the threshold, persists. This proves eventual periodicity by P in both directions. The exact length predicate has least period m, hence m divides P. A prime power dividing a finite LCM must divide an individual length c, forcing at least c distinct states. When the underlying simple graph is bipartite and c is at least m ≥ 4, c is even (each step of that cycle changes color). Formal loops do not affect this inference. Counters on cycles of lengths m and lcm(m,2) attain the unrestricted and graph-restricted bounds; the latter cycle is itself a cactus. Non-full-period subsets are exactly those invariant under the order-p subgroup, giving 2^(p^(k−1)) such sets, and the 2m singleton/complement exclusions are distinct primitive sets.

## originality

FAIL

The exact formulas are a direct corollary of the published original-graph SCC period decomposition for unary NFAs, followed by prime-power divisibility, the even-cycle lower bound and residue-counter constructions. This is stronger prior coverage than either a language-equivalent Chrobak normal-form construction or the published bipartite-cactus existence theorem. The indexed thresholded-residue record alone is not an equivalent result. The count is the usual primitive binary period count at a prime power, with singleton/complement exclusions.

## value

FAIL

The parity overhead is a natural question and the elementary proof usefully illustrates period extraction, but the audited prime-power minima and mask count follow immediately from the stronger known period theorem, standard cyclic counter and elementary primitive-mask count. No independent invariant or unresolved case remains in this claim; it does not settle overhead for composite periods with more than one prime divisor or general regular languages.

The dated certificate retains the supplied scientific assessment, sources and limitations.
