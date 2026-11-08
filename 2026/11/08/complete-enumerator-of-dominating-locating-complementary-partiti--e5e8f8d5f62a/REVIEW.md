# Scientific review

## Correctness — PASS

The finite simple base graph may be disconnected or contain isolates; the attached private clique has size at least two. Two omitted private vertices would have identical selected-neighbor signatures, and no omitted vertex in a hub-plus-clique cluster would leave private selected vertices undominated by its complement. This forces the three exclusive cluster types. In the only type with two omitted vertices, the omitted hub is separated from its omitted private vertex exactly by a selected neighboring hub. Different clusters have nonempty private signatures, ensuring cross-cluster separation. Thus the classification is both necessary and sufficient. Counting these types establishes the entire enumerator. The extremal identity \(\max_A|N_H(A)\setminus A|=n-\gamma(H)\) follows by the dominating-set completion \(A\cup(V(H)\setminus N_H[A])\) and equality at a minimum dominating set. The source-defined original adjacency test reproduces polynomial coefficients on finite instances; it is corroboration, not an infinite proof.

## Originality — PASS, with residual priority risk

The closest 2026 full-text study (DOI `10.37236/14049`) proves existence and construction for every isolate-free graph, with an example for the one-leaf corona. It does not give an exact enumerator, clique-corona classification for attachment size at least two, or an equality recovering the domination number of an arbitrary base graph. The 2025 locating-dominating partition paper (`arxiv:2506.12933`) asks for two locating-dominating classes on certain twin-free classes; here the attached cliques introduce twins and the complementary class is only dominating. The 2014 corona paper (DOI `10.12988/ams.2014.43205`) handles locating *total* domination, not this mixed-role enumeration; its additional internal adjacency requirement is not automatic for the present counted sets. Targeted mathematical-record and literature searches found no statement implying the full formula. Search incompleteness and possible unrecognized equivalent formulations prevent independent priority certification.

## Mathematical value — PASS

The result resolves the full cardinality distribution of a recently studied complementary domination-partition problem for a natural, arbitrarily complicated family of corona graphs. Unlike mere existence, the classification reconstructs every admissible partition, counts minimizers, and exactly encodes the ordinary domination number of the arbitrary base graph in the least exponent. This establishes a nontrivial link between a mixed locating-domination enumeration and classical domination without requiring structural restrictions such as connectivity, chordality, or bounded order.

## Limits and closest literature

The lower bound on private clique size is essential to the proof. The formula does not promise efficient evaluation for arbitrary input base graphs. Closest inspected sources: Chakraborty et al. (2026), DOI `10.37236/14049`, entire 12-page paper including the corona example and proof; Foucaud et al. (2025), arXiv:`2506.12933`, full available preprint; and Omamalin et al. (2014), DOI `10.12988/ams.2014.43205`, its relevant full-text corona results. Historical priority remains provisional; independent external audit remains unperformed.

Self-review: passed. Independent audit: not yet performed.
