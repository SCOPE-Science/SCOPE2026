# Self-review

## Correctness — PASS

For the ternary directed Kautz graph of admissible length-\(n\) words, the two children of any admissible length-\(n-1\) prefix have identical positive-radius predecessors, yielding a lower bound of one sensor per sibling pair, \(3\cdot2^{n-2}\). The orientation test selects exactly one extension per prefix. The decoding proof separates incoming predecessor layers and treats odd and even \(n\) separately: at odd lengths the two radius-two sensors have a unique repeated suffix of length \(n-2\); at even lengths the selected radius-two sensors form a suffix pair and the radius-one pair is either present, with a unique ordered overlap, or absent, uniquely fixing the next orientation. A selected sibling is not a predecessor of its other sibling, since the only possible length-two overlap would be an alternating word excluded by the code. Thus every vertex has a nonempty unique signature and decodes in linear time. The proof handles all \(n\ge3\), and identical full radius-two balls preclude identification at \(n=1,2\). `VERIFY.py` separately reconstructs graph balls, signatures and decoder and checks every vertex through \(n=11\). Finite testing is corroboration, not an infinite proof.

## Originality — PASS with residual historical-priority risk

Boutin, Goliber and Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842 (first publicly posted 2014-12-18), examine the larger *unrestricted* de Bruijn graph; their sharp code sizes there do not entail this result for the proper-adjacency Kautz subgraph. The 2007 and 2009 Kautz work of Araki concerns tuple domination and twin domination, without the required pairwise separation of all reporting signatures. A known radius-one Kautz identification formula concerns a different radius and is not itself an optimal radius-two construction. Searches against the mathematical finding index, known prior claims, the source article and Kautz aliases found no result that subsumes the present exact half-size optimum plus constructive decoder. An unindexed theorem, or unexamined details in the 2007 paper (abstract accessible), could affect priority.

## Value — PASS

A two-step sensor that identifies an unknown node from directed reachability observations is a natural network localization invariant. The theorem gives a sharp all-length minimum cost, an explicit optimal distributed sensor selection condition depending on only two local word transitions, and an exact \(O(n)\) reconstruction from at most five reporting sensors. Radius-two localization does not follow merely from the analogous radius-one bound. This is a structural solution for an infinite family, not a small numerical improvement or arbitrary finite slice.

## Literature and limitations

[1] D. Boutin, V. H. Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, https://arxiv.org/abs/1412.5842; inspected full text, especially lower bound and Theorem 3.6. The distinction is the forbidden-adjacent-equality constraint in the Kautz network.

[2] T. Araki, *On the k-tuple domination of de Bruijn and Kautz digraphs*, Information Processing Letters 104 (2007), 86–90, DOI:10.1016/j.ipl.2007.05.010; abstract examined but complete text unavailable.

[3] T. Araki, *Connected k-tuple twin domination in de Bruijn and Kautz digraphs*, Discrete Mathematics 309 (2009), 6229–6234, DOI:10.1016/j.disc.2009.05.031; relevant openly accessible article material examined.

The result applies only to incoming-radius-two signatures in the directed ternary no-repeat shift, with \(n\ge3\). It neither classifies all optimal codes nor resolves historical priority against inaccessible literature. All-length validity rests on the proof, not finite tests.

Self-review: passed. Independent audit: not yet performed.
