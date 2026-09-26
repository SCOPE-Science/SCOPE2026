# Certified Ramanujan census of connected cubic graphs on 10–18 vertices with maximal-gap extremals

## Context
Expander graphs and the Ramanujan bound are a recognized demand center from
Alon–Boppana through Lubotzky–Phillips–Sarnak (LPS) to Marcus–Spielman–Srivastava
(MSS). Small-order extremal expanders calibrate constructions and spectral-gap
heuristics. Existence/construction theorems are asymptotic and give no per-order
small census; count/list databases store graphs but tabulate no certified
Ramanujan-verdict-plus-maximal-gap table with enclosures and residuals.

## Definitions
- Population: one representative per isomorphism class of all connected cubic
  (3-regular) simple graphs on even orders n in {10,12,14,16,18}, in
  Meringer/GENREG canonical order. Counts: 19 / 85 / 509 / 4060 / 41301
  (total 45974).
- For adjacency eigenvalues 3 = lambda1 >= lambda2 >= ... >= lambdan:
  spectral gap = 3 − lambda2.
- Ramanujan iff lambda2 <= 2*sqrt(2) ≈ 2.8284271247461903.
- Alon–Boppana residual reported as lambda2 − 2*sqrt(2).

## Result
Complete certified census with zero ambiguous verdicts:

| n | graphs | Ramanujan | non-Ramanujan | max enclosure width | min lambda1−lambda2 separation |
|---|--------|-----------|---------------|---------------------|--------------------------------|
| 10 | 19 | 19 | 0 | 2.02e-12 | 0.2215 |
| 12 | 85 | 84 | 1 | 2.02e-12 | 0.1677 |
| 14 | 509 | 480 | 29 | 2.04e-12 | 0.1049 |
| 16 | 4060 | 3870 | 190 | 2.04e-12 | 0.0840 |
| 18 | 41301 | 39686 | 1615 | 2.04e-12 | 0.0620 |

Every verdict is backed by a recomputed lambda2 interval of width at most
~2.05e-12 (required gate <= 1e-6).

Unique (within-stratum) maximal-gap extremals (minimizers of lambda2):

| n | extremal index (1-based) | lambda2 | gap 3−lambda2 | residual lambda2−2√2 | runner-up margin | girth / bipartite / diameter |
|---|--------------------------|---------|---------------|----------------------|------------------|------------------------------|
| 10 | #19 | 1.0000000000 | 2.0000000000 | −1.8284271247 | 0.561553 | 5 / no / 2 — Petersen graph |
| 12 | #85 | 1.5320888862 | 1.4679111138 | −1.2963382385 | 0.029464 | 5 / no / 3 |
| 14 | #509 | 1.4142135624 (√2) | 1.5857864376 | −1.4142135624 | 0.296616 | 6 / yes / 3 — Heawood graph (see note) |
| 16 | #4060 | 1.7320508076 (√3) | 1.2679491924 | −1.0963763172 | 0.095040 | 6 / yes / 4 |
| 18 | #41301 | 1.7320508076 (√3) | 1.2679491924 | −1.0963763172 | 0.134147 | 6 / yes / 4 |

Exact integer characteristic polynomials from the committed adjacency matrices:
- n=10: x^10 − 15x^8 + 75x^6 − 24x^5 − 165x^4 + 120x^3 + 120x^2 − 160x + 48,
  spectrum {3, 1^5, −2^4} (Petersen).
- n=12: x^12 − 18x^10 + 117x^8 − 18x^7 − 354x^6 + 126x^5 + 486x^4 − 272x^3 − 207x^2 + 162x − 27.
- n=14: x^14 − 21x^12 + 168x^10 − 700x^8 + 1680x^6 − 2352x^4 + 1792x^2 − 576
  = (x^2−9)(x^2−2)^6; spectrum {±3, ±√2^×6}.
- n=16: x^16 − 24x^14 + 228x^12 − 1144x^10 + 3342x^8 − 5832x^6 + 5940x^4 − 3240x^2 + 729.
- n=18: x^18 − 27x^16 + 297x^14 − 1755x^12 + 6075x^10 − 12393x^8 + 13851x^6 − 6561x^4.

Committed witnesses (GENREG shortcode, 0-based adjacency lists, full 0/1 matrix)
are in `output/artifacts/extremals.json`. Example n=10 (Petersen):
`[[1,2,3],[0,4,5],[0,6,7],[0,8,9],[1,6,8],[1,7,9],[2,4,9],[2,5,8],[3,4,7],[3,5,6]]`.
Example n=14: `[[1,2,3],[0,4,5],[0,6,7],[0,8,9],[1,10,11],[1,12,13],[2,10,12],[2,11,13],[3,10,13],[3,11,12],[4,6,8],[4,7,9],[5,6,9],[5,7,8]]`.

Note (correction): the candidate draft stated the n=14 witness differs from the
Heawood graph. It is the Heawood graph: Meringer tables give exactly one
connected cubic graph of girth >= 6 on 14 vertices, and the spectrum/poly above
is the Heawood spectrum. The extremal matrix, polynomial, and counts are
unaffected; only the classical name is corrected here.

## Proof / evidence
- Source: Meringer GENREG shortcode files committed as `raw_{n}_3_3.scd`;
  decoded counts exactly 19/85/509/4060/41301, matching OEIS A002851 and
  Meringer tables; every graph checks 3-regular and connected in the replay.
- Enclosure (auditable): for each symmetric 0/1 adjacency matrix A with
  `numpy.linalg.eigh` decomposition A ≈ V Λ V^T, residual E = A − VΛV^T,
  Frobenius norm f = ||E||_F >= ||E||_2; by Weyl each true eigenvalue lies
  within f of the computed value. Certified radius r = f + 1e-12; interval
  [lambda2−r, lambda2+r], width 2r. Ordering certificate: lambda1=3 lower end
  strictly above lambda2 upper end (worst separation ≈ 0.062 at n=18).
  Verdict: Ramanujan iff upper end <= 2√2; non-Ramanujan iff lower end > 2√2;
  otherwise AMBIGUOUS (never occurs among 45974).
- Margins: closest verdict to the bound (n=18 graphs #1902/#1903,
  lambda2 ≈ 2.8284494657) clears it by ~2.2e-05, ~2e7× the radius ~1e-12;
  thinnest stratum margin (n=16) is ~1.25e-03. Extremal runner-up margins
  0.029–0.56, vastly above enclosure widths, certifying unique minimality
  within each stratum.
- Independent audit replayed `verify.py` end-to-end (VERIFY_OK), re-tallied all
  per-graph tables, re-eigendecomposed all five extremal matrices, verified
  exact integer characteristic polynomials coefficient-for-coefficient with
  sympy, and recomputed girth/diameter/bipartiteness.

## Limitations
- Completeness up to isomorphism is inherited from the Meringer GENREG files
  (counts cross-checked vs OEIS/Meringer); no independent canonical-generation
  re-run is claimed.
- Enclosures are a-posteriori Weyl/Frobenius bounds around LAPACK output plus
  1e-12 slack, not from-scratch interval arithmetic; they clear the gate by
  ~1e6× but are not formal proofs.
- Only even n = 10–18 are covered.
- Extremal uniqueness means unique minimizer within the enumerated stratum
  (positional index + committed matrix), not a general graph-theoretic
  classification theorem; no nauty canonical-labeling certificate is supplied.
- The n=10 extremal being Petersen (and n=14 being Heawood) is acknowledged as
  famous-graph coincidence, not a novelty claim; substance is the closed
  per-n counts plus certified extremals and residuals.

## Reproducibility
```
python3 output/artifacts/verify.py
```
Uses only stdlib + numpy. Re-decodes the five committed `.scd` files, checks
counts / 3-regularity / connectivity, recomputes Weyl residual enclosures
(asserts width <= 1e-6 and lambda1/lambda2 separation), re-derives every
Ramanujan verdict (asserts zero ambiguous), and re-establishes each extremal's
unique minimality. Prints the per-n table and `VERIFY_OK`. Runtime: seconds.

## References
- A. Marcus, D. Spielman, N. Srivastava, Interlacing Families I: Bipartite
  Ramanujan Graphs of All Degrees, arXiv:1304.4132 (existential, no small-order census).
- A. Lubotzky, R. Phillips, P. Sarnak, Ramanujan graphs,
  doi:10.1007/BF02126799 (number-theoretic infinite families).
- OEIS A002851 — number of connected cubic graphs with 2n nodes
  (https://oeis.org/A002851; counts only).
- M. Meringer, Tables of Regular Graphs,
  https://www.mathe2.uni-bayreuth.de/markus/reggraphs.html (counts + raw lists).
- F. Bussemaker et al., Computer investigations of cubic graphs, 1976
  (spectra to n=14 at 4-decimal rounding).
- House of Graphs, doi:10.1016/j.disc.2012.10.026 (database, no combined table).
- G. Brinkmann, J. Goedgebeur, B. McKay, Generation of cubic graphs,
  doi:10.46298/dmtcs.551 (generator enabling enumeration).
