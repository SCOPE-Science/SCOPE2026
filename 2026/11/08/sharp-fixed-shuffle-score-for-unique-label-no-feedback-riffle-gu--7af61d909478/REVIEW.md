# Review of the unique-label riffle guessing theorem

## Correctness — PASS

The objective is a maximum-weight perfect matching in the exact GSR position-marginal matrix. The source mixture formula gives the correct means and variances of each component. For labels away from multiples of the packet width, different components have disjoint ranges of attainable mean locations, separated by a linear-in-deck-size gap. A uniform lattice local central limit theorem identifies column peaks with the stated Gaussian density. Endpoint and boundary columns are controlled using a binomial mode bound, ensuring their total is negligible as the boundary width tends to zero. The interleaved permutation gives a matching lower Riemann sum, and the linear-variance integral evaluates to the claimed coefficient. The endpoint cases with zero variance at one side have integrable square-root singularities. A standalone checker passes 61 grouped exact-rational and finite matching tests. Remaining correctness risk: the proof invokes standard uniform Fourier local-limit estimates rather than reproducing their full analytic expansions; hypotheses and the characteristic-function control needed for their use are stated in the proof.

## Originality — PASS (historical priority provisional)

Krityakierne and Thanatipanonda (2025) provide the binomial-mixture representation for each card-position marginal, but explicitly allow repeated guesses and optimize positions separately. Their November 3, 2026 sequel states and proves a repeated-guess leading score and an exact row-wise maximizing strategy; neither theorem optimizes a one-to-one assignment. Kuba and Panholzer (2024) analyze the distribution of the unrestricted one-shuffle score, with a twice-repeated local guessing pattern. The new result combines column capacities and a block-interleaved permutation to determine the restricted optimum's leading coefficient. Full relevant sections of the primary works were inspected. Searches for a no-repeat or unique-label riffle guessing theorem produced no directly covering source. Risks are historical equivalent statements in older assignment or matching theory and the fact that a failure to locate a paper cannot establish priority.

## Mathematical value — PASS

A natural rule for sequentially naming cards is to use each label exactly once. That rule couples all decisions, unlike the established independent row maxima, and the coefficient is quantitatively different already at one riffle shuffle: \(\sqrt{2/\pi}\) instead of \(2/\sqrt\pi\). The theorem gives the sharp leading constant for every fixed number of GSR shuffles and an explicit asymptotically optimal, readily implemented permutation. It characterizes a meaningful constraint transition rather than a small finite improvement. It makes no claim about finite optimal permutations or growing numbers of shuffles.

Self-review: passed. Independent audit: not yet performed.
