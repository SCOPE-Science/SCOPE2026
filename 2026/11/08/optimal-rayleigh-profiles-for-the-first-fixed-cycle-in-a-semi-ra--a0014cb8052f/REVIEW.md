# Scientific review

## Correctness — PASS
The exposure lemma is proved componentwise, separating cyclic components, small trees with a non-exposed central vertex, and large trees. Every successful new cycle necessarily uses the newest edge, giving the exact exposure hazard. The path-template strategy yields the matching hazard to additive \(O(1/n)\) per step in expectation, hence \(O_{\ell,L}(n^{-1/2})\) in the survival function. The accompanying checker passed 134,418 finite exact/combinatorial and numerical assertions, including all simple graphs on at most six vertices; these do not constitute an infinite proof.

## Originality — PASS (best-knowledge, provisional priority)
Ben-Eliezer et al. (arXiv:1805.02259), Behague et al. (arXiv:2105.07034), and Gao–Koerts (doi:10.1002/jgt.23202) provide threshold-scale results rather than the exact length-dependent Rayleigh constant. Akhmejanova–Kupavskii (arXiv:2610.33854) analyze local graph properties with limited partner choice but do not state this family profile. The documented \(\ell=3\) special case is covered and explicitly excluded from the novelty claim; the new content is the all-length structural extremal argument and sharp optimal strategy. A broader unlocated result may subsume this proof; novelty is not certified by an unsuccessful search.

## Value — PASS
Cycle appearance is a canonical local-property hitting-time benchmark. The constant changes systematically with the cycle length, and a sharp componentwise extremal graph theorem explains why long path templates, rather than arbitrary forest structures, optimize the hazard. The same strategy attains the entire compact-window probability profile, not just an order-of-magnitude threshold.

## Risk and scope
The target length is fixed, endpoint choice unrestricted, and success refers to a non-induced cycle. Independent historical-priority verification and mathematical audit remain outstanding.

Self-review: passed. Independent audit: not yet performed.
