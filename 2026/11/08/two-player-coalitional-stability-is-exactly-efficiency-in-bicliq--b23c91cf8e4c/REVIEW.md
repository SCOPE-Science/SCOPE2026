# Scientific assessment

## Correctness — PASS

For all integer parameters \(a,b\ge1\) and \(q\ge2\), the proof explicitly derives each best-response condition from opposite-part color frequencies. The support dichotomy exhausts pure Nash profiles. In the balanced branch, updating the two frequency vectors establishes that strictly profitable two-player recoloring exists exactly for cross-part pairs of different original colors, with the swap uniquely feasible. Every proper coloring gives each agent maximum possible utility, excluding all strong improvements. The Stirling-surjection formula counts labeled disjoint-support colorings without double-counting, and a multinomial counts the distinct central branch. The proof treats the smallest sides, divisibility and every color count. The standalone program checked 58,547 profiles and 45 parameter instances, including all unilateral deviations, all possible two-player joint recolorings on Nash profiles, exact counting and welfare. Finiteness of tests is not presented as an infinite proof.

## Originality — PASS, subject to literature priority uncertainty

The closest original Max \(k\)-Cut paper, Carosi et al., arXiv:1810.09278, treats the same game and develops general sufficient coalitional-stability results. Its inspected main results and appendix do not show **the reverse implication** that every \(2\)-strong biclique profile is a maximum cut, nor classify all biclique Nash profiles, exact color-swap improvements or the labeled census. The full accessible 2020 and 2024 optimal-coloring literature concerns the forward direction (optimal implies some bounded coalition stability), not this biclique converse. A 2026 counterexample on a non-biclique network refutes a general strong-stability conjecture but does not cover the present infinite family. Searches of mathematical records by complete-bipartite/biclique/max-cut/anti-coordination/coalesced colors and exact claims found no equivalent result. This is a best-knowledge literature determination, not a proof of universal novelty; unindexed results remain a residual risk.

## Value — PASS

The paper's central problem is to understand whether social optimality is compatible with coalitional resistance. This theorem identifies an infinite, natural network family for which the two properties coincide, and remarkably a coalition of only two suffices to rule out every inefficient Nash profile, while all unilateral equilibria may be inefficient exactly at a clean divisibility threshold. The unique improving pair mechanism, closed equilibrium counts and exact price of anarchy provide structural, reproducible information not captured by general forward stability bounds. The object and invariant are motivated independently of the finite computational experiments.

## Closest comparisons and limitations

The theorem is confined to unweighted complete bipartite interaction graphs, labeled common-color strategy sets and pure strategies. Theoretical proof—not enumeration—establishes the statements for arbitrary positive part sizes. The comparison to Carosi et al. (2018), Gourvès–Monnot (2010), Garuglieri et al. (2020/2024), Madeo et al. (2022) and Gogoi (2026) is documented in the structured originality assessment. No exhaustive indexing or publication-priority certification is asserted.

Self-review: passed. Independent audit: not yet performed.
