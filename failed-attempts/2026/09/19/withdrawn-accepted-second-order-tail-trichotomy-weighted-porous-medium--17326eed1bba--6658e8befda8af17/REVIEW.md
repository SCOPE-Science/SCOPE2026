# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The source paper supplies both the leading far-field limit and a smooth two-dimensional center-manifold reduction at the tail critical point. In logarithmic radius the two stable rates are

\[
\delta=\frac{\sigma(m-1)+2(p-1)}{p-1},\qquad
h=\frac{\sigma(m-1)+2(p-1)}{m-p},
\]

so their order changes exactly at \(m=2p-1\). Direct substitution of
\(f=c_*\xi^{-\sigma/(p-1)}(1+\varepsilon)\) into the profile ODE fixes the universal forced coefficient below resonance and the logarithmic coefficient at resonance. A symbolic verifier independently checks these identities and their consistency with the center coordinates. Nonlinear reduced-system terms are of strictly higher order than the first correction in each regime.

The main hidden-hypothesis checks were: \(2p-1>p\) for every \(p>1\), so all three regimes are compatible with \(m>p\); the logarithmic spatial variable in the source reduction is exactly \(\log\xi\) up to an additive constant; and the exceptional factor \(\lambda-N+2\) has the expected interpretation through the radial harmonic function \(\xi^{2-N}\).

## Originality

PASS, to the best of our knowledge, with a deliberately narrow claim.

The source paper arXiv:2609.20397v1 states the common leading tail but does not state a second-order expansion, an \(m=2p-1\) transition, or a logarithmic tail correction. Its earlier companion work arXiv:2406.00349 concerns the opposite exponent ordering \(p>m\). Iagar--Laurençot, arXiv:2406.11518 / Nonlinearity 38 (2025), studies second-order asymptotics for a different PDE with singular p-Laplacian diffusion and gradient absorption; it establishes that the general method is prior art, not coverage of the present coefficient formulas.

Older homogeneous porous-medium absorption papers are the most important residual risk. In particular, McLeod--Peletier--Vázquez, Differential and Integral Equations 4 (1991), 1--14, studies the homogeneous equation underlying the classical \(1<p<m\) theory. Its complete text was not fully inspected. However, the weighted mechanism isolated here vanishes in the literal \(\sigma=0\) specialization because \(a=\lambda=0\), so no concrete coverage of the displayed weighted \(m=2p-1\) logarithmic coefficient was found.

Searches by the source identifier/title and by combinations of “second-order”, “logarithmic”, “weighted absorption”, “porous medium”, and the threshold \(m=2p-1\) found no matching statement. No overlapping SCOPE record was found under the source identifier or equivalent tail terminology. These searches do not guarantee first discovery.

## Value

PASS. The source paper proves that three globally different profile families converge to the same leading tail. The new expansion determines precisely when the far field forgets that global distinction one order further, when a resonance produces a logarithm, and when profile memory reappears at the first correction. The threshold and coefficients are explicit, and the harmonic cancellation identifies a geometric exception where the leading diffusion forcing disappears exactly.

## Limitations

The theorem is a far-field statement for the bounded self-similar profiles covered by the source classification. It does not prove PDE stability, attraction, uniqueness of all global profile branches, or a third-order expansion. In the harmonic-cancellation case, determining the next nonzero correction beyond the stated vanishing requires further analysis.
