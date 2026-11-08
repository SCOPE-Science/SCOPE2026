# Scientific review

## Correctness

**PASS.** The result applies to all finite unweighted trees with two distinct marked vertices. Directed-edge arrival and the initial unremembered step are separately handled. The branch-excursion induction establishes the critical expected return \(2b_v-1\), the child-arrival system has an explicit finite solution, and successive upward passages yield the claimed identity. The standard simple-walk recursion gives the comparison baseline. The equality characterization follows from strictly positive intermediate path terms. Separate exact-linear-system computations replayed for 4,202 cases from the packaged script. No finite test is presented as an infinite proof.

## Originality

**PASS, qualified for priority.** The general inequality against simple random walk is **already proved**, in stronger graph-wide form, by Altisen et al. (2012), Corollary 9, using the same rule; it is not claimed as new. Their Proposition 14 gives facts about paths rather than the present arbitrary-tree quantitative formula. Fasino et al. (2021), specifically their second-order hitting-system treatment, and Matsuo et al. (2022 advance publication) do not give the exact target-rooted subtree-speedup identity or its equality characterization in their inspected portions. Searches of published mathematical records and relevant earlier claims did not surface an implication or exact table recovering the formula. No search proves exhaustive historical novelty; unknown earlier or equivalent derivations remain a residual risk.

## Value

**PASS.** The literature's global speedup order does not say how large the improvement is at a particular source-target pair. The new explicit formula answers that natural quantitative question for all tree topologies, exposes the contribution of branches along the path, distinguishes exact equality from strict improvement, and permits direct comparisons without solving the directed-edge Markov system. It has substantive structural content beyond a small numerical example, while requiring no extension to general graphs to be useful.

## Closest sources and limitations

Altisen, Devismes, Gerbaud and Lafourcade, *Comparisons of mean hitting times for tabu random walks on finite graphs* (2012), Corollary 9; Fasino, Tonetto and Tudisco, *Hitting times for second-order random walks* (2021), sections on second-order hit formulas and no-dangling-edge model; Matsuo, Kawagishi and Ohsaki, *On the mean first passage time and mean cover time of a non-backtracking random walk on graphs* (2022 advance), sections on regular and configuration-model graphs. The theorem has not been extended to weighted trees, cycle-bearing graphs, or other leaf rules. Independent priority checking and mathematical auditing have not been performed.

Self-review: passed. Independent audit: not yet performed.
