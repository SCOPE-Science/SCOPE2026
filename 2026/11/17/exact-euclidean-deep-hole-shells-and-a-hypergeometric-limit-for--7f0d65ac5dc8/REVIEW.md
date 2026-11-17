# Mathematical review: hypersimplex-to-panhandle distance spectrum

## Correctness

PASS. The source's polytope description is independently verified from the cited primary Definition 4.1/Proposition 4.4. For each excluded hypersimplex vertex, the given projection has tail sum one, head sum \(r-1\), and coordinates in the unit cube. The displayed supporting-normal inequality holds against every point of the target polytope and proves unique nearest-point optimality. Rational residual norms give exact squared distances. Monotonicity gives every maximal vertex. The strict convex-combination variance identity rules out nonvertex farthest points. The hypergeometric central limit theorem and the delta method prove the stated asymptotic law only under its specified nondegenerate proportion assumptions. Finite exact certificates and separate numerical quadratic programs corroborate, not replace, those arguments.

## Originality

PASS, subject to bibliographic risk. The primary 2022 panhandle paper establishes the halfspace description and Ehrhart/volume results; the 2021 Schubert-matroid paper treats Ehrhart properties. The rank-two specialization is covered by the earlier paving-matroid distance theorem and is expressly excluded. The 2015 capped-simplex projection paper provides a general optimization method but no comparison of the two present polytopes or their entire metric spectrum, maximizing locus, and distribution limit. Publicly indexed panhandle circumball, inball, covariance, asymmetry, and width results concern other geometric invariants. General hypersimplex facial-distance results compare coordinate faces with their complements, not the panhandle truncation. These are statement-level distinctions, not mere title comparisons; earlier equivalents using the language of cardinality-constrained hypersimplex projection remain a residual risk.

## Mathematical value

PASS. The panhandle family is a natural one-inequality truncation of all rank-\(r\) uniform-matroid bases, central to the geometry of matroid relaxation. The finding determines an *entire* Euclidean metric spectrum and its binomial multiplicities, explicit unique nearest points and exposed contact-face types, and *all* farthest points of the continuous hypersimplex. The limiting law quantitatively distinguishes the typical and worst-case geometric displacement in proportional dimensions. The facts are motivated by the named canonical polytopes, not an arbitrary finite slice.

## Closest literature and limits

Hanely et al., arXiv:2201.12442 (Definition 4.1; Proposition 4.4); Fan–Li, arXiv:2110.11549 (Schubert matroids and Ehrhart); Wang–Lu, arXiv:1503.01002 (general capped-simplex projection). No earlier all-parameter exact metric spectrum was established by the inspected sources. This is not an independent priority or correctness certification. The proof and checker apply to ordinary Euclidean coordinates, not weighted metrics or continuous-volume distance laws.

Self-review: passed. Independent audit: not yet performed.
