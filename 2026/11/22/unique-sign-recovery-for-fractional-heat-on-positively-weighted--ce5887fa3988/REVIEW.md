# Review of the weighted-star fractional-heat sign classification

## Correctness — PASS

The precise domain is a finite symmetric weighted star with at least two leaves, arbitrary strictly positive conductances, and \(\alpha>0\). Spectral calculus is unambiguous because \(L\) is symmetric positive semidefinite. Distinct conductances produce an arrowhead secular equation; tied conductances produce additional class-contrast eigenvalues. Both cases are treated explicitly. For every leaf pair the ordered spectral coefficients have sign pattern \(+,-,+\), total mass and first moment zero, so strict convexity gives a negative initial kernel derivative. The generalized Descartes rule bounds the number of real zeros by two, counting the simple zero at time zero; the positive constant-mode limit then forces exactly one further simple positive zero. A hub–leaf coefficient pattern \(+,-\) proves its all-time positivity. Bernstein subordination proves strict positivity for subunit orders. Since every row sums to one, entrywise nonnegativity and maximum-norm contractivity are equivalent. The result does not depend on finite sampling for its universal quantifiers.

Numerical verification was replayed from `verify_star.py`: 216 parameter/order configurations and 1,608 leaf-pair trials, including repeated conductances. The test does not certify arbitrary time or dimension; the proof does.

## Originality — PASS, with residual historical-priority uncertainty

The principal motivating full text is F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370 (first public 2017-12-20). Section 2, especially the three-vertex path example and Proposition 2.3, establishes nonpositivity at early times for general noncomplete graphs but gives no arbitrary-weight star-wide single-sign-recovery classification. M. Benzi and I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389 (first public 2020-12-15), presents fractional diffusion and the classical singular-\(M\)-matrix positivity regime for orders at most one. These known parts are acknowledged, not presented as independent novelties.

The closest published mathematical record, *A sharp positivity transition for fractional graph heat on complete multipartite networks* (2026-10-26), covers unweighted complete multipartite graphs, including equal-weight stars. Its available summary does not give an arbitrary-conductance star theorem or the convex spectral-function extension. Its full record was inaccessible in this check, so this is a disclosed priority risk, not a declaration that the whole record was ruled out. Related weighted-star Crank–Nicolson and weighted-star biharmonic resolvent records concern different scalar matrix functions and do not, by themselves, imply unique zero counts for the continuous-time exponential. Prior claims in accessible historical ledgers were compared by mathematical object and implication, not by title alone. No exact earlier arbitrary-weight all-order claim was identified; search incompleteness does not establish absolute novelty.

## Mathematical value — PASS

Generic eventual positivity only says every matrix entry is eventually nonnegative. It does not preclude multiple sign reversals, different negative bands, or hub–leaf negativity at intermediate times. The theorem establishes a complete entrywise time-sign diagram, one simple crossing for **each** leaf pair, all-time hub protection, and the exact first time when the operator once again becomes an \(\ell^\infty\)-contraction, for an arbitrarily heterogeneous branching network. The convex spectral-function strengthening isolates the mechanism and applies beyond polynomial or fractional powers. These are structural results for a natural diffusion family, not a small numerical improvement or an unmotivated finite table.

## Limitations and risks

The root equation is finite and explicit but not generally elementary. The identity of the last-recovering leaf pair for arbitrary weights is not classified. The theorem excludes arbitrary trees, normalized and directed Laplacians, and nonconvex spectral multipliers. Historical priority is subject to external review, especially against inaccessible full texts in specialized matrix-function literature; no independent mathematical review has occurred.

Self-review: passed. Independent audit: not yet performed.
