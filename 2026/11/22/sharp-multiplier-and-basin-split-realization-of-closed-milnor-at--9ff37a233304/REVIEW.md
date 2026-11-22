# Scientific review — sharp multiplier and basin-split realization

## Correctness
PASS. The proof gives necessary derivative restrictions at fixed points, a piecewise polynomial \(C^1\) scalar field with exactly assigned slopes and signs, a gap-independent derivative envelope, global gluing at accumulation points, and the precise Milnor full-basin/minimality argument. The standalone checker verifies finite symbolic and rational cases; it is not used in place of a limit proof. The time-one derivative is \(\exp(v'(p))\) at each equilibrium.

## Originality
PASS within the inspected evidence. The closest primary source, Hantáková–Mlíchová (2026, Section 4), proves continuous/homeomorphic Milnor-attractor realization, not smooth admissible derivative data. Eynard-Bontemps–Navas (2019) studies interval flow embeddings and distortion, not the combined necessary/sufficient attractor multiplier theorem. A compared topological graph-realization statement does not address differentiable multiplier data. Actual published-finding corpus, own-ledger and literature comparisons are recorded in `AUDIT.json`. Historical priority remains a risk, especially from older one-dimensional jet interpolation work; no universal absence claim is made.

## Mathematical value
PASS. Arbitrary closed invariant sets can be realized with a complete classification of their allowable local derivatives and arbitrary complementary-gap basin splits. The theorem identifies a sharp rigidity at accumulation points and a sharp hyperbolicity-compatibility condition for infinitely many repellers, providing more information than mere topological realizability.

## Scope and limitations
Only orientation-preserving \(C^1\) interval diffeomorphisms fixing the target attractor pointwise; the construction is a \(C^1\) flow. It does not address \(C^2\) matching or nontrivial dynamics on the attractor. Exact numerical tests are finite, and independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
