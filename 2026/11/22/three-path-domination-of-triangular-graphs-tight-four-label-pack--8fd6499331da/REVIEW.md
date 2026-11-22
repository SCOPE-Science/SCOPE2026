# Review: three-path domination on triangular graphs

## Correctness
**PASS.** The elementary edge-incidence criterion converts domination of \(J(n,2)\) into coverage of all but at most one original complete-graph label. A three-vertex path uses at most four labels, giving a sharp lower bound. Construction with four-blocks and one padded final path attains the bound for every \(n\ge3\). At \(n=4k+1\), the exact equality case forces disjoint four-label supports and precisely one unused label; all possible three-edge root trees are \(K_{1,3}\) and \(P_4\). Counting paths *as subgraphs with a specified middle* gives 12+12 choices per four-block, hence \((4k+1)!/k!\). The 119 legal replacements per path and connectivity via a unique spare label are fully proved. Independent direct and block-based programs pass the documented finite cross-checks. Risk: no machine proof of the unlimited-order combinatorial argument, and no independent mathematical validation.

## Originality
**PASS, provisional historical priority.** The 2024 foundational article develops three-path domination and solves paths/cycles, not \(J(n,2)\). Closest recorded triangular-graph results concern ordinary total domination, paired domination, and liar's vertex-edge domination, all with distinct constraints. Their stated results cannot recover the complete family of edge-defined three-path collections, its 24 path objects per four-label block or its whole-path exchange graph. Exact searched aliases included '3-path domination line graph complete graph', 'P3 domination triangular graph', 'four-label tree packing' and corresponding research records. The three relevant published result texts were read directly. Risk: an unindexed equivalent or much broader older theorem might imply portions; negative searches alone are not a novelty proof.

## Mathematical value
**PASS.** This is an exact infinite-family minimization and optimiser classification for a recently introduced nontrivial domination invariant, with a distinguished tight residue class. The capacity-equality case rigidly packs the ground labels into four-vertex rooted-tree supports; the factorial optimum count and regular connected exchange graph quantify both multiplicity and the mobility of complete three-path guard assignments. These are not just the previously known scalar path/cycle values.

## Limitations and closest literature
The scalar minimum is proved for all \(n\ge3\), but the enumeration and exchange theorem hold only for \(n=4k+1\). The count distinguishes subgraph paths that have the same three vertices but different middle choices. Comparison sources include Ibrahim–Jackson–King (2024), the previously published paired- and total-domination results on triangular graphs, and a different liar's vertex-edge invariant. First-public motivating date: 2024-06-30. Historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
