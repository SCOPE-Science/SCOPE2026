# Scientific review

## Correctness (PASS)

The exact domain is the entire rational point set on the explicitly stated ternary plane quartic over the two fields with \(27\) and \(81\) elements. The homogeneous polynomial follows by homogenizing formula (5) of Korchmáros–Nagy–Szőnyi in the characteristic-three specialization. A canonical complete set of \(Q^2+Q+1\) projective points also enumerates the dual lines. Exhaustive finite arithmetic evaluates the quartic, each line incidence, every four-secant, and its incidence with every point. Two independently chosen irreducible field polynomials at each extension degree, pairing-based recovery of all four-secants, exact sum identities, and comparison with the published normalization parameterization support the correctness claims. Computation is exhaustive, not sampling; the standalone `verify_bks.py` reproduces it. The work establishes no general infinite-family statement.

## Originality (PASS; residual priority risk)

The central paper [Korchmáros–Nagy–Szőnyi, arXiv:2302.10162, introduction, §§4.2, 7.2] states the construction and its known geometry and expressly excludes the extension degrees \(r=3\) and \(r=4\) from its final covering conclusions. The final theorem there requires \(r\ge5\) in the BKS case. The new finding gives both full line-section splitting spectra and the exact number of external points missed by all four-secants in those excluded degrees at \(q=3\), including the even-degree failure. Their results on field size, smooth normalization, singularities and eventual behavior are credited rather than reclaimed. Targeted published-record and prior-statement comparisons identified no statement subsuming these exact small-field distributions. An older, differently expressed finite-geometry table remains a possible priority risk; a negative search cannot prove novelty.

## Mathematical value (PASS)

These are the first base-field cases in two extension degrees identified as unsettled in the motivating primary article. The exact rational hyperplane-section weights and complete multiplicity distributions answer a natural missing arithmetic question for a distinguished genus-zero plane quartic, including a boundary failure over an even extension where large-extension behavior would suggest eventual completeness. The six/seven-valued histograms sharpen a bare existence or counterexample to an exhaustive geometric classification. The scope is narrow but specifically motivated, rather than an arbitrary slice.

## Closest literature and limitations

Korchmáros–Nagy–Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, arXiv:2302.10162 (20 February 2023), §4.2 and §7.2; JCTA 204 (2024), article 105851. No theorem beyond the stated two finite fields is asserted, and earlier tabulations under other terminology may exist.

Self-review: passed. Independent audit: not yet performed.
