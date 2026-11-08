# Scientific review

## Correctness (C): PASS

The claim is the all-positive-integer-moment product and its sharp near-one Tauberian tail, with a previously established CRP functional limit used explicitly as a premise. The cited logarithmic-time functional convergence gives a stationary tandem with independent exponential stage rates \(1,\ldots,k\). The total service law is the maximum of \(k\) unit exponentials (Rényi representation), so its survival integral is \(\phi_k\). For any ordered observation times, a marked-Poisson void probability splits into the initial empty-state mass and independent non-overlapping arrival intervals. Ordering the \(s\) sample-time coordinates and changing to successive ratios produces the product moment formula exactly, including the Jacobian and \((s-1)!\) factor. A first-order expansion at ratio one, with a second-order beta-moment bound, proves \(q_j=1-\theta/j+O(j^{-2})\). The positive infinite product, integer-to-real Mellin interpolation, and the Laplace--Stieltjes Tauberian theorem give the stated sharp constant and exponent. The \(k=1\) variance is a direct calculation. All domain and boundary assumptions are explicit. Running the standalone checker yielded 101 exact/symbolic/numeric assertions, but the proof is not based on finite experiments.

## Originality (O): PASS, with historical-priority qualification

Gnedin and Stark (2022 first public preprint; 2023 publication), *Random Permutations and Queues*, explicitly study the same chronological small-cycle occupation and prove lack of almost-sure convergence; Theorem 6 supplies the logarithmic-time functional limit. Their paper's Section 3 leaves nonvanishing variance to the reader and their Sections 8 and 10 supply queue representations, but the accessible full text does not present an all-order product of occupation-fraction moments or sharp high-fraction asymptotics. Galganov and Ilienko (2025), *Scaling limit for small blocks in the Chinese restaurant process*, prove a strictly broader point-measure limit, recover the count functional limit in Section 4.2, and derive other block-characteristic laws. This work does not claim to improve those convergence theorems: it adds an explicit distributional invariant and a quantitative near-one endpoint universality result through nontrivial void-set factorization and Tauberian analysis. Da Silva, Jamshidpey and Tavaré (2020) consider static conditioned Ewens derangements rather than chronological occupation. Searches for alternative idle-time/discounted-occupation formulations and relevant indexed research records found no matching endpoint constant or factorization. Because a general point-process theorem could be specialized, and queueing literature is large, an unlocated equivalent calculation remains a genuine priority risk; it is not treated as independent certification.

## Value (V): PASS

The chronological derangement fraction is the central fluctuating statistic motivating the 2022 work. Earlier results describe its absence of an almost-sure limit and the underlying limiting process, but leave numerical and distributional properties poorly explicit. A one-dimensional product formula for every moment determines its entire limiting law; the sharp power and positive constant at the endpoint specify the probability of extremely long predominantly derangement epochs. Independence of the endpoint exponent from the small-cycle exclusion cutoff is a structural universality statement, not a routine normalization or unmotivated finite enumeration. The uniform-permutation special case yields the exact nonzero limiting variance \(e^{-2}(e-2)\), sharpening the motivating variance observation.

## Closest literature and residual limitations

- Gnedin--Stark, arXiv:2209.12781, especially Sections 3, 5, 8 and 10: known chronological nonconvergence, stationary tandem and functional limit; no explicit matching product/tail located.
- Galganov--Ilienko, arXiv:2502.05578, especially Section 4.2: broader limiting process result; no matching endpoint asymptotic located.
- Da Silva--Jamshidpey--Tavaré, arXiv:2006.04840, Sections 1--3: static derangement law, not the growing-process occupation fraction.

The result fixes \(k\) and \(\theta\) while \(n\) tends to infinity. The endpoint limit is subsequently taken in the limiting variable. It does not provide finite-\(n\) rates, growing-\(k\) limits, or an independently verified priority classification.

Self-review: passed. Independent audit: not yet performed.
