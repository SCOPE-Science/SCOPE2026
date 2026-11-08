# Self-review

## Correctness — PASS

The local rule is explicitly defined over the binary field for every cyclic ring length at least two. Recovering the leftmost input bit from a target symbol produces the stated sixteen-state reverse transition. Exact enumeration of the four rank-eight image sets proves the eight restricted bijections. Closed walks of the reverse-state skew product correspond bijectively to cyclic predecessors; a separate direct enumeration verifies this relationship for every target on lengths two through thirteen. The two explicit sheet permutations generate all \(40320\) permutations, and root loops of lengths six and thirty-five force aperiodicity. Strong connectivity follows from base reachability and full group generation, so the normalized adjacency is primitive and Perron–Frobenius convergence applies with an exponential spectral gap. Fixed-point enumeration gives the stated nine fractions. No finite sample is substituted for the infinite-size proof.

## Originality — PASS within inspected literature

The motivating 2026 preprint already gives the rule and its open, locally eventually onto and eight-to-one properties; these are not new here. The 2017 work by Mariot and collaborators provides preimage-period and multiplicity algorithms using de Bruijn graphs, not an explicit all-ring asymptotic image/fiber histogram for this particular recent nonlinear rule. The nearest related work on individual homogeneous/alternating cyclic targets supplies pointwise predecessor counts; those do not imply the limiting frequency of each possible predecessor multiplicity, the full symmetric-group monodromy or exponential convergence. The converse also does not give exact predecessor counts for chosen target words. Equivalence, stronger-coverage, precomputed-table and implication searches found no full statement in the material inspected. Historical priority is not independently certified; an unlocated specialized finite-to-one-cover result remains a residual risk.

## Value — PASS

A generic eight-to-one property on bi-infinite configurations gives neither the image fraction nor the ambiguity distribution among finite periodic target words. These are canonical invariants of finite-volume symbolic dynamics and determine how often a uniformly sampled periodic output has no input or has any of the eight possible fiber sizes. The exact symmetric-group law explains a nontrivial positive limiting excluded-output fraction and supplies an analytically proved exponential approximation for all large ring lengths. This is a structural result, not a tiny finite calculation or an arbitrary slice. It does not claim to resolve temporal dynamics or the entire finite-length histogram.

## Closest literature and limitations

Haugland et al., *Locally eventually onto cellular automata*, arXiv:2610.33131v1, Appendix B; Mariot et al., *Computing the Periods of Preimages in Surjective Cellular Automata*, DOI:10.1007/s11047-016-9586-x. A finite-state computation certifies a special transition system but gives no general theorem for arbitrary cellular automata. Historical priority remains provisional, and no independent audit has been undertaken.

Self-review: passed. Independent audit: not yet performed.
