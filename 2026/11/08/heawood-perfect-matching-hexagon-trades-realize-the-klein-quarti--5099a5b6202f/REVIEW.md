# Review of the Heawood perfect-matching hexagon-trade correspondence

## Correctness — PASS

The claim specifies exactly the Fano incidence relation, matching and six-cycle flip criterion, and embedded facial rotation. Exhaustive matching enumeration is performed independently by local incidence choices and by all seven-point bijections. In both programs, 24 perfect matchings and 28 six-cycles appear; a six-cycle flip is legal exactly when a matching contains three alternate edges. The 84-edge graph is connected, with constant distance layers \((1,7,14,2)\) and the complete neighbor intersection counts of \(\{7,4,1;1,2,7\}\). The cycle-disjointness model independently computes all 24 distinct induced Coxeter heptagons and tests the common-two-path criterion across all 276 matching pairs. Two different facial constructions independently give \(3K_1\sqcup3C_7\). The identification as the named Klein quartic graph uses the previously established uniqueness of the distance-regular graph having that array. Independent scientific validation is not claimed.

## Originality — PASS, qualified

Ye–Zhang (arXiv:0908.1506v1) studies Pfaffian toroidal polyhexes with the Heawood graph. Dejter (arXiv:1002.1960v1) already supplies the 28-hexagon Coxeter model, 24 Coxeter heptagons, Klein graph and path-based heptagon geometry; none are presented as independently new. The additional matching-to-heptagon assignment and exact equivalence of matching-hexagon flips to common-two-path adjacency are not stated in the inspected relevant constructions. Tratnik–Ye (arXiv:1710.00761v1) provides general surface resonance theory; its cubical-component theorem assumes a proper subset of faces and does not cover this seven-out-of-seven system. Liang–Zhang (arXiv:2609.19766v1) covers general toroidal polyhex facial connectivity and trivial matchings but does not provide the explicit Heawood \(3C_7+3K_1\) calculation or its all-hexagon counterpart. Specific database-result checks did not identify a stronger calculation of this matching correspondence. Residual originality risk: the correspondence might be implicit in a different Fano/Klein construction or appear under an unindexed synonym; priority is qualified, not absolute.

## Value — PASS

Perfect-matching resonance ordinarily uses only embedding faces, whereas alternating-cycle trades admit nonfacial exchanges. The smallest cubic girth-six toroidal incidence graph supplies a canonical, symmetry-rich test of the distinction: seven facial hexagons leave six components, but permitting the 21 essential ones connects everything in at most three moves. The new explicit matching-to-Coxeter bijection explains the symmetry through the existing Klein geometry and allows shortest-path questions in one context to be translated into Coxeter heptagon adjacency. The insight is structural, not an arbitrary partial census; it makes no claim of a theorem for an infinite family.

## Closest sources and limitations

The dominant nearby construction is Dejter's Coxeter-to-Klein seven-cycle model (2010). The strongest general coverage of facial resonance is the later surface theory of Tratnik–Ye and Liang–Zhang. Verified conclusions are finite and specific to the stated torus rotation; the graph-name and distance-array classification is prior knowledge. The two supplied programs are same-package mathematical checks, not an external validation.

Self-review: passed. Independent audit: not yet performed.
