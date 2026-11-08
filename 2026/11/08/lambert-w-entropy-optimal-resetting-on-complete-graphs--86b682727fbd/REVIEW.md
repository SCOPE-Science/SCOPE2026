# Scientific review

## Correctness — PASS

The specified transition kernel distinguishes observed destinations from unobserved reset decisions. Detailed balance gives explicit stationary masses, and direct row-entropy evaluation gives the exact formula. The all-size improvement follows from the small-reset singular term and a support bound; the asymptotic maximizer follows from a global positivity localization, uniform expansion on the localized scale, and strict concavity of the limiting optimization function. The uniform error tends to zero, and strong concavity forces every maximizing sequence to lie at the Lambert-\(W\) scale. A separately constructed transition-matrix checker passed 126 parameter cases. Finite calculations are supporting evidence rather than substitutes for the proof.

## Originality — PASS (qualified)

The 2022 primary resetting-entropy article gives a general transition matrix and stationary-resolvent formula but reports a regular-network entropy optimum based on keeping ordinary and reset arrivals distinct. Its general machinery can yield the finite clique entropy expression after explicit specialization, so that expression **alone** is not claimed as the original contribution. The substantive new comparison is the vanishing all-maximizer scale \(W(m)/m^2\) and gain \((W(m)^2/2+W(m))/m^3\), neither given or implied as an immediate corollary by its regular-network optimizer. The 2021 weighted-walk survey gives the standard entropy formula, and the 2023 centrality-reset paper addresses first-passage times instead. Semantic research-index searches and literature searches found no equivalent asymptotic. Absence of a matching record is not a proof of historical priority.

## Value — PASS

The correction changes the qualitative design scale: on large cliques, entropy-optimal resets vanish faster than \(1/m\), and the possible entropy gain shrinks as \((\log m)^2/m^3\). The theorem supplies both a structural explanation (merging of indistinguishable paths to the reset vertex) and a quantitative asymptotic rule for a natural infinite graph family, rather than only an isolated numerical counterexample.

## Closest literature and residual limits

Wang–Chen (2022), arXiv:2208.05665, sections II–IV, is the closest source. Riascos–Mateos (2021), Section 3.4, supplies the general entropy-rate formula. Zelenkovski et al. (2023), Section 2, explicitly describe overlapping reset and ordinary-step destinations but study first-passage objectives. An unrelated-looking 2025 density-dependent reset/local-time large-deviation paper on complete graphs could not be fully inspected and was not classified as noncovering; a previously unlocated entropy optimization could affect historical priority. The theorem does not establish finite-\(m\) uniqueness or the same scaling for other graph families.

Self-review: passed. Independent audit: not yet performed.
