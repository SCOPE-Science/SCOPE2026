# Scientific review: variable-exponent two-cycle cusp

## Correctness (C): PASS

The strict-alternation map has the exact normalized return \(G(u)=r[1-q(1-u)^d]^d\), \(0<q,r<1\). Its fixed points are the roots of \(H_{d,q}(t)=r\), and the sign of \(H'\) is exactly the sign of \(qP_d(t)-1\). This proves the full phase census, including fold equality and physically inadmissible upper-fold cases. At the cusp the third derivative is negative and nonzero, giving global parabolic convergence and the exact rate. Integrating the derivative between neighboring extrema yields the fold-width coefficient. Two explicit test locations near the upper endpoint force three roots for large degree and make the root-location asymptotics rigorous. A standalone checker validates exact symbolic identities and selected high-precision regimes; it does not supply proofs for continuum claims. Main limitations: only strict alternation, no global dynamics outside it, no uniform joint cusp/high-degree crossover.

## Originality (O): PASS within accessible evidence

[1] Lawnik–Moysis–Volos (2023), doi:10.3390/sym15071311, defines the whole family; reviewed accessible full author text and numerical dynamical sections. [2] A cusp of coexisting two-cycles in a fixed-point-free quadratic interval map (published indexed 2026-11-08) already proves the degree-two cusp, coexistence and critical relaxation; [3] an additional indexed quadratic cusp study confirms this overlap. Accordingly **no quadratic-only result is claimed novel**. [4] An attracting two-cycle disappears into a nonstationary ghost at a discontinuity (published indexed 2026-11-01) treats a special contracting regime and singular a=b boundary. Our additional claim quantifies arbitrary real degrees, the degree-dependent cusp threshold and fold coefficient, and eventual three-cycle coexistence for every fixed parameter triple. The claim is not logically implied by those distinct prior assertions. Search aliases, actual queries, all comparisons and material-read limits are retained in AUDIT.json. Residual risks include unindexed general-degree publications, a related 2024 piecewise-system paper, and unavailable full indexed proofs; search absence does not guarantee priority.

## Value (V): PASS

The exponent d is intrinsic to the source family. A complete degree-dependent cusp criterion is useful because varying d changes the number and stability of physical primitive two-cycles from one to three, with two separate attracting basins; the sharp fold-width and exponentially small attractor corrections quantify numerical detectability. The fixed-degree quadratic classification cannot explain the universal high-degree bistability phenomenon. The result is a motivated dynamical phase diagram, not a single arbitrary parameter enumeration.

Self-review: passed. Independent audit: not yet performed.
