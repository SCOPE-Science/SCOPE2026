# Review: sharp asymmetric two-sided exponential Gabor bounds

## Correctness — PASS

The two-parameter theorem is reconstructed from the geometric Zak series for each exponential tail. Separating even and odd Zak frequency shifts produces a scalar multiplier at redundancy two. Every fiber minimum lies at \(\theta=\pi/2\), and every maximum at \(\theta=0\), because the rational multiplier is strictly increasing in \(\cos(2\theta)\). Strict convexity makes the maximum occur at the integer boundary fiber; an exact quadratic sign-change gives the unique lower extremizer \(x_*\in(0,1)\). Simultaneous parity cancellation is impossible for strictly positive tail rates. The unitary-dilation factor \(hc^2\) is explicit. The Python standard-library checker replayed 12,431 deterministic assertions; the proof, not finite arithmetic, supplies the all-parameter conclusion.

## Originality — PASS, provisional

Faulhuber–Shafkulovska (arXiv:2204.02917, especially Sections 2.4 and 8) establish sharp frame bounds for the **even** two-sided exponential, not the unequal-decay family. Kloos–Stöckler (arXiv:1311.7359) give the full TP frame set and bounds for **even** exponentials, whereas Gröchenig (arXiv:2301.00857) proves qualitative TP frame results. Indexed asymmetric two-sided exponential sampling results concern integer-grid translations with no modulations; they do not imply sharp Gabor bounds. The accessible historical equal-rate claim concerns high-redundancy optimal-lattice asymptotics, not two-rate density-two exact constants. The Janssen 1996 original quantitative frame-bound paper could not be read in full; historical priority remains provisional. This unresolved risk does not provide positive prior implication.

## Mathematical value — PASS

The exact lower bound is the worst possible uniform reconstruction stability constant, and the upper bound controls noise and condition number. The theorem supplies the full nontrivial unequal-rate phase profile rather than one example: both spectral endpoints and the unique location of the bottleneck on the Zak torus follow from explicit formulas. It extends a natural long-studied totally positive window family quantitatively, without pretending the known equal-rate restriction is novel.

## Scope and limitations

Only continuous strictly positive real two-tail exponential windows and rectangular density-two Gabor lattices are covered. No optimal lattice geometry, other densities, nonrectangular lattices, or independent priority certification is established. Janssen's original 1996 frame-bound calculations remain a named uninspected risk; finite software tests are nonexhaustive.

Self-review: passed. Independent audit: not yet performed.
