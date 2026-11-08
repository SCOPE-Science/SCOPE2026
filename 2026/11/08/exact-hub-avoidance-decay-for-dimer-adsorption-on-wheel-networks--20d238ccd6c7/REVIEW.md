# Scientific review: wheel hub avoidance in irreversible dimer adsorption

## Correctness — PASS

The accepted claim is exactly the odd/even hub-vacancy law, the even-rim transfer integral, and its dominant Bessel-root exponential asymptotic. The wheel must have at least four rim vertices in the even case; clocks have equal positive rates. Rim-perfect-matching necessity and the matching-edge/intervening-edge/spoke inequalities are proved both ways. The trace-class decomposition gives a legitimate operator trace, not a formal integral. Strictly positive kernel arguments isolate the leading eigenvalue. The eigenfunction boundary problem gives the displayed modified-Bessel equation. The independent finite-state and rank-integration calculations match exactly for rim lengths 4 through 16; no finite experiment is used as a proof of the limit.

## Originality — PASS on the examined literature, with residual risk

The dimer adsorption model and graph generalities in Penrose–Sudbury (2005), https://arxiv.org/abs/math/0503519, are prior material. Pippenger (1989), https://doi.org/10.1137/0402034, develops graph random sequential adsorption including edge occupation. Miller–Pritikin (1997) treats the equivalent random greedy matching mechanism and expected-size bounds. Gamarnik–Goldberg (2009), https://dspace.mit.edu/entities/publication/36eae796-81ba-4fbd-980d-4455c69cd9f2, treats regular-graph/high-girth performance. None of the accessible inspected statements gives the specific wheel hub-survival integral, transfer spectrum, and Bessel constant. The Pippenger full manuscript and two related greedy-matching full texts remained inaccessible or rate-limited, so this is not an exhaustive priority determination. Generic arbitrary-graph recurrences imply finite values computationally but do not eliminate the new closed asymptotic analysis.

## Mathematical value — PASS

The probability that a distinguished high-degree adsorption site avoids occupation is a natural rare-event observable beyond expected coverage. There is a sharp parity obstruction and an exact special-function decay rate for even rims, providing a reproducible benchmark in irreversible adsorption on graphs with a diverging-degree defect. The result makes no claim about broad universal jamming laws or observed experiments.

## Evidence and limits

Run `python3 verify_wheel.py` to replay direct full-edge-order enumeration, exact finite-state dynamic programming, independent matching-clock order integration, and the special-function root check. The program proves no infinite asymptotic by itself; that rests on the trace-class spectral proof in RESULT.md. Historical-priority uncertainty is disclosed rather than hidden.

Self-review: passed. Independent audit: not yet performed.
