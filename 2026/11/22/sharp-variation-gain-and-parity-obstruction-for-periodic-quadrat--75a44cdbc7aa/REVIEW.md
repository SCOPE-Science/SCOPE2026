# Mathematical review

## Correctness — PASS

For any cell the quadratic is \(y_i+m_it+(\Delta_i-m_i)t^2\); matching first derivatives gives \((I+S)m=2\Delta\). On an odd circle its inverse is an alternating cyclic sum. For each elementary difference \(e_p-e_q\), the inverse yields derivatives in \(\{-2,0,2\}\), and the variation of each of the \(n\) cells is at most one. Finite positive/negative mass pairing of an arbitrary zero-sum difference vector gives the sharp upper bound \(nV_d(y)/2\). A one-site spike has variation one on every cell and achieves equality. The even-cycle alternating nullspace and compatibility condition follow directly from the cyclic shift. The exact-rational checker was run from the packaged source path and all its asserted tests passed; numerical testing does not substitute for the proof.

## Originality — PASS with historical-priority risk

The accessible full Schoenberg (1968) text treats odd-degree cardinal splines on the whole integer line. The Goodman (1983) synopsis concerns general interpolation solvability and may contain versions of the parity criterion, which is not offered as independently novel; the sharp quadratic odd-circle total-variation norm is the distinctive result. Albasiny–Hoskins (1973) studies periodic spline circulants and error/derivative bounds; its full text was inaccessible, so its possible implications cannot be exhaustively excluded. Nochetto–Salgado (2012) provides an averaging-based TV-diminishing operator, not this nodal quadratic interpolant. Published-record searches returned sharp norms for *linear spline orthogonal projectors* rather than the present exact periodic quadratic interpolation. The detailed equivalence and implication comparisons and access risks are recorded in the structured audit.

## Mathematical value — PASS

The theorem determines a complete, natural family of sharp BV sensitivity constants, not an arbitrary fixed-grid example. It exhibits a sharp parity cliff between unisolvence on every odd knot cycle and failure of unrestricted interpolation on every even cycle; the seemingly innocent exact-knot quadratic scheme is increasingly oscillatory, amplifying variation by a factor growing linearly in the number of sites. The single-spike extremizer identifies the mechanism and contrasts naturally with TV-diminishing averaging interpolants.

## Limits

Only equal-spaced real cyclic quadratic \(C^1\) knot interpolation is covered. The even-cycle compatibility mechanism is familiar in broad interpolation theory; no novelty is claimed for the underlying circulant algebra alone. Full-text access to relevant older articles was not achieved, so historical priority remains qualified. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
