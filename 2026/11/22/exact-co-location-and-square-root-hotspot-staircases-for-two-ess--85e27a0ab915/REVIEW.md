# Scientific review: Two-essential-resource Monod hotspot allocation

## Correctness — PASS

The objective and feasible set are explicit: equal normalized carbon and nutrient budgets over any finite number of identical independent patches. The proof uses an exact nonnegative square decomposition, proving both the dual-to-single resource reduction and forced co-location for **all** maximizers. A factorized derivative rules out asymmetric positive scalar maximizers; all support patterns are compared by an exact adjacent-score threshold \(T^2=k(k+1)\). Endpoint and tie cases are covered. A standalone checker passed 60,282 supplementary assertions, mostly exact rational. Finite grids are not treated as exhaustive proofs of continuous domains.

## Originality — PASS on inspected evidence

The primary 2024 soil heterogeneity paper directly motivates two-substrate Monod kinetics but tests and simulates spatial glucose treatments rather than freely optimizing both resources. A 2020 experimental study varied one, two, and four glucose-feeding compartments without jointly allocating carbon and nutrient. Generic sigmoidal resource allocation is well established; the present exact co-location and radical support-switch law are not asserted to pioneer that field. Closely related mathematical records on Hill inhibitor dosage and Holling-III prey placement have single budget constraints and different response laws. The 1970 Vicentini report on S-shaped allocation was only accessible as an abstract; general historical coverage of the scalar stage remains a specific, genuine priority risk. Not all older literature has been exhaustively searched.

## Value — PASS

This complete allocation theorem isolates a sharp conflict between the need to **co-locate** essential substrates at low supply and **spread** them after local saturation. All support changes, exact transition ties, and all optimizing placement patterns are classified for arbitrary patch counts, and the contrast with the one-resource concavity theorem explains the importance of complementarity. The result is a controlled mathematical benchmark, not an experimentally calibrated microbial application guideline.

## Closest literature and limits

Endress et al., *Soil Biology and Biochemistry* (2024), doi:10.1016/j.soilbio.2024.109509; Shi et al. (2021), doi:10.1016/j.soilbio.2020.108068; Vicentini (1970), repository abstract; Udell–Boyd (2015), author PDF. Limits include equal normalized budgets, identical independent patches, static initial uptake, and no dynamic transport. Independent external verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
