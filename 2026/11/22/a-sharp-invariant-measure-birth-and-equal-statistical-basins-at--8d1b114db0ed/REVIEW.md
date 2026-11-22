# Mathematical review

## Correctness

PASS. The exact source map at \(a=b=1/2\), \(d=2\) yields the return \(G_c(x)=16cx^2(1-x)^2\) for positive left inputs, with the exceptional value \(F_c^2(0)=1\) explicitly tracked. Monotonicity, the strict maximum \(\max G_c(x)/x=64c/27\), the exact critical factorization and the right-branch inverse establish every basin and all genuine cycles. Dominated convergence of continuous-test-function time averages, coupled with the explicit non-invariance of \(\nu\), proves the complete invariant-measure statement without assuming continuity of the discontinuous original map. The cubic-root and spectral assertions are not invoked. Exact polynomial and quadratic-field identities passed in `check.py`; all continuum steps have proofs in `RESULT.md`.

## Originality

PASS within inspected evidence. The originating article [1] proves fixed-point absence and presents numerical dynamical scans, not the stated invariant-probability threshold, exact basin masses and ghost/physical coexistence. The published contraction-edge result [6] applies only to \(c<1/8\) on this slice; the strict-alternation cycle results [5] assume \(a>b\), excluding this discontinuous border. Therefore neither entails the parameter transition at \(27/64\), the immediate \(2/9\) stationary physical basin, or the exact half/half split at \(c=1/2\). Kryzhevich [2] and Catsigeras et al. [3] establish general non-invariant-limit/ghost mechanisms and appropriately limit novelty claims. The 2024 follow-up [4] was only available through its abstract and metadata, with its accepted manuscript inaccessible; related priority risk remains.

## Value

PASS. The source construction is motivated by avoiding equilibria in supposedly chaotic maps. A complete natural border slice instead exhibits three sharply separated invariant-measure phases and two incompatible observable-statistical outcomes. The exact \(2/9\) onset and symmetric \(1/2\) ghost-basin mass quantify a discontinuous failure of the usual continuous-map implication from empirical limits to stationary probabilities. The classification covers the entire maximal strict-alternation range of this quadratic border slice, rather than an arbitrarily tuned finite example.

## Relationship to closest literature and limitations

The existence of ghost limits and missing invariant measures in discontinuous systems is known. The new result concerns a specific sharp parameter-dependent phenomenon and exact physical basin geometry, not a general new theory of discontinuous dynamics. The detailed bounds, comparison identifiers, and source-access risks appear in `AUDIT.json`. The theorem is exact-real and limited to \(0<c\le1/2\); no cryptographic implication or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
