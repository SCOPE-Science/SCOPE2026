# Self-review

## Correctness (PASS)
The precise source alphabet, length boundaries, exactly-one operation, and distinct-descendant interpretation are defined in RESULT.md. The derivative transformation is bijective over the additive group \(\mathbb Z_q\), and one duplication inserts precisely \(k\) zero entries. Confusability is equivalent to transferring exactly \(k\) zeros between two zero runs, not to an arbitrary change in two coordinates. On quotient vectors of integers the transfer is one unit. The proposed modular coloring strictly changes along every such edge, and a word with no available donor is isolated. Each active component has at most \(n-2k+1\) runs, so a single global palette works. The explicit clique of \(n-2k+1\) sources provides the matching lower bound; the no-edge case handles \(n\le2k\). Both embedded independent scripts passed. The proof is universal; finite scripts alone are not presented as certificates of a universal statement.

## Originality (PASS, with residual priority risk)
The 2016 Jain–Farnoud–Schwartz–Bruck source supplies the derivative/zero-run framework, not this exact global coloring and matching clique in the accessible inspected material. The closest published exact-edge-count result for the same graph counts edges rather than chromatic number, and the 2015 simplicial rook graphs concern a strictly different adjacency relation. Searches for colorings, equivalent vector-composition formulations, larger-coverage results, and exact databases/tables did not identify a statement implying the present one. The full text of the 2010 Dolecek–Anantharam source was not obtained; it remains a priority risk, as do unindexed works. These limits are disclosed, not treated as proof of absolute novelty.

## Value (PASS)
The problem asks for the smallest number of disjoint single-duplication-correcting codebooks covering every possible source word, not an artificial finite parameter slice. This all-parameter sharp decomposition, with an efficiently computable coloring and a matching obstruction, is an exact invariant of a canonical zero-error confusability graph. It can be used directly for codebook assignment and provides a global graph parameter not determined by average degree or the previous edge-count theorem. The result does not claim optimal size of any individual code.

## Closest literature and limitations
See the four referenced works in RESULT.md. The 2016 reduction is prior art; the 2026 edge enumeration does not imply a chromatic value. Earlier repetition coding and unindexed equivalent arguments remain possible historical overlap. No human or independent expert has reviewed this package.

Self-review: passed. Independent audit: not yet performed.
