# Scientific review of the source–sink covariance extremum

## Correctness (C): PASS
For a fixed tree, indicators of source and sink status share orientation data only at the same or adjacent vertices. The four cases (identical, adjacent, distinct nonadjacent, and reversed edge) reconstruct the exact covariance formula. Completing squares gives a nonnegative edge-energy identity. Leaf counting proves the path upper bound; for three leaves the unique degree-three vertex contributes an exact degree penalty and three unavoidable edge energies. All equality cases are determined, including the impossibility of equality before seven vertices. The included standard-library checker independently enumerates all orientations of every labelled tree through six vertices, all Prüfer-coded trees through seven vertices for the structural bound, and equality constructions through fifty vertices. These finite tests do not substitute for the all-order argument.

## Originality (O): PASS, subject to historical priority
The closest primary literature is Hwang et al., *Acyclic orientation polynomials* (2019, arXiv:1910.10920), where sections 2–5 concern exact sink-set enumeration and related chromatic-symmetric-function identities. Those formulas record sink marginal behavior but not the joint source–sink moment or a sharp all-tree covariance inequality. Conte et al. (2018, DOI:10.1016/j.dam.2017.08.002) analyze algorithms to enumerate orientations with designated sources and do not derive the stated covariance extremum. Gebhard and Sagan (1999/2000, arXiv:math/9907078) concern counting orientations with a unique sink. Relevant mathematical-record searches for the covariance, source–sink duality, tree stability and the sharp constant did not identify a statement covering the new inequality. A past undiscovered equivalent remains possible, and the Conte publisher page was not fully retrievable in a later access attempt. No independence of validation is claimed.

## Value (V): PASS
The observable is the joint fluctuation of two natural orientation counts, not an arbitrary graph-polynomial coefficient. The path maximizer and strictly positive *order-independent* gap distinguish a global graph-shape effect; an exact family of second-best trees realizes the same sharp \(13/64\) loss at every order \(n\ge7\). The gap and equality family are not obtained simply from known one-sided sink counting. The sign reversal \(C(P_n)=(n-4)/16\) also makes source–sink dependence visible: zero on the four-vertex path and positive on longer paths, whereas strongly branched trees can have negative covariance.

## Scientific limits
Fixed finite simple trees, unbiased independent edge orientations, and one covariance statistic only. Open-ended priority searches cannot rule out all historical equivalences; external validation remains to be performed.

Self-review: passed. Independent audit: not yet performed.
