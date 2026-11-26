# Independent mathematical audit

## correctness

PASS

Write H=n p̂, D=∑(Xᵢ−1)₊. The numerator H−K is S²/(n+S)−D, and the denominator (1−p̂)√H is Sn/(n+S)^(3/2). When np is bounded, Var(p X̄)=q/n proves p̂/p→1; H→λ and K has the binomial-to-Poisson limit, or K=0 with high probability for λ=0. When nq² is bounded, D agrees with the count of Xᵢ≥2 off an event of probability at most nq³. At positive critical intensity, S/(nq)→1 from the first two moments, and the fit terms tend to λ and √λ. At zero intensity, D=0 with high probability and S/√n→0 by Markov, giving Z→0 with the stated zero-total convention. For Gaussian sufficiency the centered score Y=p²(X−q/p)+1{X=0}−p has variance pq² using Cov(X,1{X=0})=−q. Its third absolute moment is O(p) for p≤1/2 by geometric moments and the rare indicator, and O(q²) for p≥1/2 by splitting X=0, X=1 and X≥2 (the first two scores are q² and −2pq; the remaining geometric tail has uniformly bounded scaled third moment). This gives the required Lyapunov ratios. The fitted numerator's Taylor remainder is p³δ²/(1+pδ), δ=X̄−q/p; the good-event expected standardized bound is 2√(p/n), and the complementary event is negligible by Var(pδ)=q/n. Fitted-to-true scales tend to one because nq→∞. A bounded subsequence of either critical intensity has a lattice or degenerate limit, proving necessity for arbitrary sequences. Conditional on S=s, joint masses p^n q^s are equal, so counting supports of size n−k and their positive compositions gives the formula. The fixed conditional denominator preserves ordering by |K−H|, and the tie-inclusive conditional tail is superuniform. For the stated cutoff and strictly subcritical λ, zero Poisson events do not reject and every positive count rejects, with no atom on the boundary. Independent numerical evaluation gives λ*=0.176524554935153 and 1−exp(−λ*)=0.1618218025087914.

## originality

PASS

Credit is restricted to the sharp triangular-parameter normality and two Poisson boundary laws for the exact Di Noia statistic and the resulting quantitative normal-calibration failure. Its fixed-parameter statistic and CLT are known. The exact conditional calibration itself, although useful here, is covered in substance by the earlier uniform-composition law and general conditional-tail method, with the mass function an elementary counting corollary. No independent novelty credit is given to conditioning, this corollary, or the generic level guarantee; these are not the stated novel target. The closest sparse Poisson-null analogue has one rare-doubleton boundary for a different distribution and statistic, not the two opposite geometric limits.

## value

PASS

The statistic and its fixed-parameter normal reference are published and practically interpretable. Proving that normal calibration specifically fails at two different null scales, with limiting size near 16.18% at nominal 5%, identifies a substantial inference problem and explains it via two distinct rare events. The exact parameter-free calibration is a useful existing alternative when applied here; value does not depend on its novelty.

The dated certificate retains the supplied scientific assessment, sources and limitations.
