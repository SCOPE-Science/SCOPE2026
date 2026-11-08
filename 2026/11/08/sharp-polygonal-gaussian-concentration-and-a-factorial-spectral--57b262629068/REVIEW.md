# Scientific review: regular-polygon Gaussian localization

## Correctness — PASS

The proof fixes the normalization of the Gaussian STFT and Fock monomials. The exact area-normalized radial endpoint gives both the vacuum integral and a second-order boundary displacement. The equal-area disk operator has a strictly positive top spectral gap, and the polygon operator converges to it in norm through a symmetric-difference estimate. Cyclic rotation kills every vacuum-to-monomial coupling below degree \(N\). A uniform short-interval asymptotic gives the degree-\(N\) coefficient, while factorial tails suppress all higher permitted degrees. The Schur-complement resolvent converges on that high-degree vector to scalar multiplication by \((1-e^{-A})^{-1}\), proving the sharp gain and eigenfunction coefficient. Exact symbolic integration and high-precision quadrature corroborate the expansion; neither substitutes for the infinite-dimensional argument. No estimates are claimed uniformly in area.

## Originality — PASS, provisional

Nicola–Tilli (2022) proves global disk extremality and the Gaussian equality case. Gómez–Guerra–Ramos–Tilli (2024, first circulated 2023) proves sharp stability order and second variations in the signal, rather than the explicit regular-polygon spectral expansion. Existing fixed-profile smooth shape-Hessian formulas do not directly imply this result for a nonsmooth sequence whose first angular frequency increases with \(N\). No examined source establishes the sharp factorial gain and leading eigenvector correction. The strongest unresolved priority risk is an earlier Toeplitz approximation or high-symmetry perturbation theorem that includes this special family; the bibliographic search is not an exhaustive novelty proof.

## Mathematical value — PASS

An area-matched regular polygon is a canonical implementable approximation to the globally optimal disk mask. The result identifies a sharp fourth-order concentration penalty and a *different*, factorial scale for the improvement obtained by optimizing the signal itself. This separates geometric approximation loss from signal adaptation, and explains the high angular mode selected by discrete rotational symmetry. It is more than a generic stability estimate or a routine reparametrization: the factorial law needs a selection rule and a resolvent calculation beyond any fixed-order shape expansion.

## Closest literature and limitations

The closest primary sources are DOI 10.1007/s00222-022-01119-8 and DOI 10.1007/s00222-024-01248-2. The theorem treats fixed positive area and large polygon order only; it does not classify the entire spectrum, provide a uniform area-dependent threshold, or establish independent historical priority. The attached numerical checker is limited to finitely many tests.

Self-review: passed. Independent audit: not yet performed.
