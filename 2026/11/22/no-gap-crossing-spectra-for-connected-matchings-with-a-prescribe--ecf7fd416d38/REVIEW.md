# Review of the fixed-opening-set connected crossing-spectrum theorem

## Correctness: PASS

The domain is precisely all Dyck opening words of semilength \(n\ge1\). Necessity of primitivity follows from the zero-height separator. The upper bound counts crossings at the first closing endpoint; FIFO achieves \(K(w)\) and connects consecutive arcs. The constructive induction inserts a consecutive interior opening–closing pair and splits the earliest-closing spanning chord. Its endpoint-order case analysis establishes a tree crossing graph with \(n-1\) edges. Finally, adjacent inverted opener assignments at *consecutive* closings create exactly one crossing and preserve connectedness, proving gap-free coverage. A distinct exhaustive finite enumerator and an independent transition check corroborate the proof. No finite enumeration is used to infer the universal case.

## Originality: PASS (historical priority provisional)

Gross and Šarković, arXiv:2607.02410 (publicly available July 2, 2026), analyze genus-preserving chord swaps; their main result is fixed-genus mixing, not prescribed opener sets or connected-crossing spectra. The primary PDF's definitions, Theorems 1.2 and 2.2, and the associated proof sections were inspected. Chen–Deng–Du–Stanley–Yan establish crossing/nesting symmetry under endpoint restrictions but do not impose connectivity of the crossing graph. Pilaud–Rué's §2.2 defines connected matchings by their crossing graph and gives the universal lower bound \(n-1\), but does not classify the fixed-opening-set range or prove interpolation. Published-results searching included both terminology changes and implication comparisons; Published-record searches found only distinct claims involving Dyck words, crossing covariances, chord swaps and perfect matchings. The earlier bound and all foundational definitions are expressly credited, and complete historical priority is not independently established.

## Value: PASS

Connectivity of the crossing graph is a substantive global constraint: for nonprimitive words it eliminates all matchings, whereas for every primitive word it imposes precisely the universal lower bound and *no internal gaps* up to a sharp opener-dependent maximum. This simultaneously determines feasibility and an infinite family of exact crossing-count supports. The proof supplies concrete tree and Hamilton-path realizations plus a monotone connectivity-preserving construction; the theorem does not attempt full coefficients of the corresponding generating polynomials.

## Limitations and remaining risk

Exact counts of connected matchings at each admissible crossing number, crossing-graph isomorphism types, and fixed-genus mixing are not derived. Close primary sources were inspected, but differently phrased or unindexed historical formulations might cover portions of the result. All reported correctness and originality assessments are non-independent.

Self-review: passed. Independent audit: not yet performed.
