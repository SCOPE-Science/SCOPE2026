# Review of Gaussian habitat-viability window

## Correctness — PASS

The proof decomposes the grounded Laplacian into the uniform viable-site mode and its orthogonal complement. An explicit independent-edge matrix Bernstein calculation establishes an internal gap \(pm+O_{\mathbb P}(\sqrt{m\log m})\); the exact Schur-complement identity then shows the eigenvalue differs from the boundary-edge mean by \(\|b\|^2/(pm)+o_{\mathbb P}(1/m)\). Independent binomial boundary degrees give the limiting variance, and the binomial central limit theorem gives the Gaussian viability crossover. The coefficient is \(\|b\|^2/p\to s(1-p)\). A fresh packaged numerical checker validates finite spectral inequalities and the Schur identity, but the infinite claims are proved analytically. Risk: only fixed positive density and fixed absorbing set cardinality are covered.

## Originality — PASS (bounded comparison)

Pirani–Sundaram, Theorem 3, already proves first-order fixed-sink concentration around \(sp\); Apollonio–Tora–Vergni formalize network population viability and obtain concentration primarily under increasing sink mass. The present single finding addresses an unprovided second-order relaxation and the corresponding nondegenerate survival-probability window. Searches addressed Gaussian/central-limit aliases, Dirichlet/grounded Laplacian equivalences and established eigenvalue bounds, including published-claim comparisons. No directly covering statement was identified. The Tora–Vergni 2026 mathematical biology article remained inaccessible beyond its abstract; broader spectral fluctuation work may also contain an equivalent formulation. Lack of discovery is not proof of historical novelty.

## Value — PASS

A law of large numbers alone cannot resolve populations at a proliferation threshold just \(O(n^{-1/2})\) away from marginal viability. The Gaussian crossover gives the limiting fraction of viable random habitats in that biologically motivated critical window. The explicit \(1/n\) correction isolates the systematic advantage of internal dispersal relative to naive use of boundary contact counts. No claim is made about demographic extinction in a finite stochastic population.

## Assessment status

Self-review: passed. Independent audit: not yet performed.
