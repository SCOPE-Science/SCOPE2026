# Scientific review: complete type-\(A\) root-polytope surface law

## Correctness — PASS

The claim is for every integer \(n\ge3\) in the induced Euclidean metric of \(H_n\). The proof classifies every facet by a two-level linear functional; the actual facet is an orthogonal product \(\Delta_{s-1}\times\Delta_{n-s-1}\), whose Gram determinant gives the asserted individual area. Counting subsets supplies the exact size-biased distribution. The hypergeometric tilt is an algebraic identity. The explicit total-variation bound follows from \(1-(1-u)^{3/2}\le3u/2\) and the exact hypergeometric variance, and the classical hypergeometric central limit theorem gives the Gaussian scale. Facet-cone volume summation and Vandermonde's identity establish volume. A fourth-moment estimate justifies the claimed \(O(n^{-2})\) remainders. The parity correction to the inradius starts at order \(n^{-2}\), so the first-order tangency constant is stable. Actual Euclidean convex-hull calculations reconstructed every facet at \(n=3,4,5,6\) and corroborated volume; the finite checker is not used as an infinite proof.

## Originality — PASS, with residual priority uncertainty

Higashitani–Jochemko–Michałek (2018, arXiv:1807.07678 §3.1, especially Corollary 3.3) establishes the subset facet labels but not the Euclidean area-weighted law. D'Alì–Delucchi–Michałek (2019, arXiv:1910.05193, sections 2–4) develops related volumes and combinatorics, but not surface-weighted cut-size fluctuations or the tangency deficit. Chen–Davis–Korchevskaia (2021, arXiv:2107.12315, §4) characterizes facet subgraphs, not the asserted metric distribution. Closest published related published-finding corpus records deal respectively with continuous interior covariance of the **same** complete-graph root polytope and facet areas of **tree** root crosspolytopes. The former does not imply a boundary-area probability law; the latter has a different facet metric and neither supplies a complete-graph hypergeometric area law. The earlier exact volume is credited and is not claimed as novel. No covering result was found in the inspected material or targeted published-finding corpus checks; that is not a proof of historical uniqueness. The most significant residual risk is an unindexed classical equivalent under type-\(A\) root bodies or centered \(\ell_1\) sections.

## Mathematical value — PASS

This identifies the entire area-weighted facet-size spectrum of a canonical high-dimensional polytope rather than an arbitrary numerical slice. The hypergeometric size bias yields a concrete geometric distinction: choosing a facet by surface area cuts the asymptotic subset-size variance in half relative to choosing uniformly among facets, even though both favor balanced subsets. The exact surface area and sharp \(1/(4n)\) deficit from the tangential bound quantify the bulk boundary geometry and explain why an exponentially faceted body becomes asymptotically surface-tangent without being exactly tangential. The full phenomenon is not determined by the previously known volume or face count alone. It is a finite/infinite family metric invariant; no downstream theorem or universality outside this family is asserted.

## Limitations and risks

No independent audit or computer-formalized proof was performed. Missing historical synonyms could hide an earlier equivalent surface calculation, and one should not generalize the limiting law to other coordinate embeddings. The explicit total-variation estimate is not itself a Berry–Esseen estimate for convergence to the normal law.

Self-review: passed. Independent audit: not yet performed.
