# Review of the two-circle boundary-layer law

## Correctness: PASS

The final theorem specifies two independent angular samples, a positive inward radial gap \(\lambda(2\pi/n)^2/2\), and a finite nonzero inner-to-outer sample ratio \(\alpha\). The supporting-line inequalities reduce vertex membership to the four nearest neighbors, because the ratio \((r/R-\cos\phi)/\sin\phi\) is monotone on each signed angular side. After scaling, the outer and inner angular neighbors become independent exponential variables of rates one and \(\alpha\); the three strict inequalities have no boundary atoms. Conditioning on two outer gaps gives the stated normalized integral. Two-point Palm localization yields covariance convergence and the \(L^2\) law. Parameter limits and the sharp \(n^{-2}\) window follow by dominated convergence and coupling monotonicity. Direct convex-hull calculations corroborate the exact local criterion, not merely the integral.

## Originality: PASS, provisional

The closest inspected historical full-text results treat a single boundary with intrinsic-volume error (Böröczky–Fodor–Hug, 2011), mean area and perimeter via support functions (Majumdar–Comtet–Randon-Furling, 2009), and interior-uniform hull complexity (Har-Peled, 2011). Their statements neither determine the fraction of inner points on the hull in a two-circle sample nor imply the critical \(n^{-2}\) profile. Related published concentric-regular-polygon rotation results use finite deterministic vertex grids, not independent random angular clouds. The accessible 1991 Carnal–Hüsler abstract concerns interior-disk sampling; full text was not verified, so its precise connection remains a residual priority risk. Searches and implication comparisons support best-knowledge originality, not exhaustive historical uniqueness.

## Mathematical value: PASS

The problem asks when a second closely spaced geometric stratum contributes macroscopic numbers of genuine convex-hull vertices. The sharp transition \(n^{-2}\), its explicit two-rate Poisson crossover \(p(\lambda,\alpha)\), and the nontrivial high- and low-density limiting profiles answer that geometric question and explain competition between boundary layers. This is not an arbitrary parameter slice: the scale matches the intrinsic \(n^{-2}\) gap geometry of sampled smooth curves. Unlike computing a known hull invariant, the fraction of surviving inner vertices is not fixed by the single-curve intrinsic-volume laws.

## Closest literature and limitations

See the references and prior-work discussion in RESULT.md. The 1991 historical article was available as bibliographic abstract only; other unindexed random-polytope literature may still contain equivalent results. The theorem is qualitative asymptotics for circles with independent uniform angles; no finite-sample error bound, extensions to other curves, or independent audit are claimed. The numerical checker is corroborative rather than a substitute for the mathematical proof.

Self-review: passed. Independent audit: not yet performed.
