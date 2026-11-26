# Independent mathematical audit

## correctness

PASS

The Poisson add-one formula shows Cov(M,ΣXᵢ)=Σλᵢ Pr(Xᵢ≥max_{j≠i}Xⱼ); shifting the mass by one in each term makes this the expected maximum on unique-winner events. Thus the gap is the weighted tie term plus Cov(M,R). Both M and R are coordinatewise increasing, so the covariance is nonnegative; a tie at one with other counts zero gives strictness. For two counts, Δ=(Y−X)₊ satisfies Δ(Y−X)=Δ² and direct expansion of Cov(X+Δ,Y−Δ) gives EΔ[(a−b)t+EΔ]. At small t, the tie term is abt²+O(t³) and the overshoot is bt+O(t²), hence the two terms contribute abt² each. For q=√(b/a)<1, after removing the common fixed-order Bessel asymptotic, I_k≤I₀ permits dominated summation against kq^k. The overshoot constant is q/(1−q)², the weighted tie constant is t√(ab), and the two leading contributions combine via √(ab)+(a−b)q/(1−q)²=2a√b/(√a−√b). This yields the printed prefactor; the overshoot square is lower order. At equal rates the CLT with bounded scaled second moments gives EΔ/√t→√(a/π), while the Bessel tie term is O(√t). In both cases the mean is asymptotic to at, giving the claimed Fano limits. Inspection of the two scripts confirms their role as finite corroboration only; they were not executed.

## originality

PASS

Credit is for the exact two-rate gap decomposition and its sharp fixed-unequal-rate equivalent, not qualitative underdispersion or the equal-rate limit. A prior indexed iid result implies the latter. The standard Skellam representation supplies the underlying masses, not the asserted variance cancellation and sharp unequal-rate constant as a compared theorem. There is no demonstrated equivalent prior coverage of that core; this conclusion does not certify historical priority.

## value

PASS

Knowing only underdispersion or that the Fano ratio tends to one does not quantify how fast the maximum becomes indistinguishable from its dominant parent by this statistic. The prefactor captures two effects of the same order (weighted ties and rare overshoots) and reveals the singular contrast with coincident rates. The positive all-scale decomposition provides an interpretable, cancellation-free formula precisely where direct moment subtraction becomes ineffective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
