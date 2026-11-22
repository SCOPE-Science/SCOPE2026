# Return bridges double the missing-direction intensity at hypercube coverage

## Finding

Consider the non-lazy, uniform coordinate-flip walk on the binary \(d\)-cube, started at the origin. For an even length \(L\ge2\), condition on the walk returning to the origin at time \(L\) (not necessarily its first return). Let \(V_{d,L}\) be the number of coordinate directions that were **never** used. This is the codimension of the smallest coordinate face containing the complete walk path.

The conditional law has the exact probability-generating function
\[
\mathbb E[u^{V_{d,L}}\mid X_L=0]
=\frac{[z^L](\cosh z-1+u)^d}{[z^L](\cosh z)^d},\qquad
\mathbb E[(V_{d,L})_r\mid X_L=0]
=(d)_r\frac{[z^L](\cosh z)^{d-r}}{[z^L](\cosh z)^d}.
\]
The second identity holds for each integer \(0\le r\le d\), where \((a)_r=a(a-1)\cdots(a-r+1)\).

**Fixed-density conditional central limit theorem.** Suppose \(d\to\infty\), \(L=L_d\) is even, and \(L_d/d\to\mu\in(0,\infty)\). Let \(\lambda_d>0\) uniquely solve \(\lambda_d\tanh\lambda_d=L_d/d\), put \(p_d=\operatorname{sech}\lambda_d\), and let \(\lambda>0\) solve \(\lambda\tanh\lambda=\mu\). Then
\[
\frac{V_{d,L_d}-dp_d}{\sqrt d}\xrightarrow{d}
N(0,\sigma_\mu^2),\qquad
\sigma_\mu^2=p(1-p)-\frac{p^2\mu^2}{\mu+\lambda^2p^2}>0,
\quad p=\operatorname{sech}\lambda.
\]
In particular \(V_{d,L_d}/d\to p\) in probability, whereas without the return condition the corresponding fraction tends to \(e^{-\mu}\), and \(p>e^{-\mu}\).

**Critical coverage window.** Suppose instead \(L_d/d-\log d\to c\in\mathbb R\), with \(L_d\) even. Then
\[
V_{d,L_d}\mid\{X_{L_d}=0\}\xrightarrow{d}
\operatorname{Poisson}(2e^{-c}),\qquad
\Pr(V_{d,L_d}=0\mid X_{L_d}=0)\longrightarrow\exp(-2e^{-c}).
\]
Without conditioning, the missing-direction count tends to \(\operatorname{Poisson}(e^{-c})\). Thus fixing the endpoint to the origin **doubles** the mean number of missing directions in the coupon-collector window and shifts the coverage transition by \(d\log 2\) flips, at first order in its width-\(d\) window.

## Assumptions and scope

For each integer \(d\ge1\), write \(X_0=0\in\{0,1\}^d\). At each discrete step choose one of \(d\) coordinate indices independently and uniformly, then flip that bit. Let \(N_i\) be the number of selections of coordinate \(i\) during the first \(L\) steps; then \(X_L=0\) holds **if and only if** all \(N_i\) are even. This event has positive probability at every positive even \(L\). Define \(V_{d,L}=\sum_{i=1}^d\mathbf 1_{\{N_i=0\}}\). The proof and all limit statements use exact integer times; no first-return conditioning, holding steps, uniform random endpoints, or distinct-vertex visit counts are involved.

For the fixed-density limit, the centering \(dp_d\) uses the **actual** ratio \(L_d/d\), not merely its limit: under the stated hypothesis one cannot generally replace it by \(dp\) without an additional convergence-rate assumption. The critical-window statement also uses the actual even integer \(L_d\).

## Proof

**Exact generating function.** An ordered coordinate word with counts \(n_1,\ldots,n_d\) and \(\sum n_i=L\) has multinomial multiplicity \(L!/\prod_i n_i!\). Returning home requires every \(n_i\) to be even. Marking zero counts by \(u\) gives
\[
\sum_{\substack{n_1+\cdots+n_d=L\\ n_i\ \mathrm{even}}}
\frac{L!}{\prod_i n_i!}\,u^{\#\{i:n_i=0\}}
=L!\,[z^L](\cosh z-1+u)^d.
\]
Dividing by the same count at \(u=1\) proves the generating function. Differentiating \(r\) times at \(u=1\) proves the factorial-moment identity. In particular
\(\Pr(X_L=0)=L!d^{-L}[z^L](\cosh z)^d\).

**An exact independent-variable representation.** For any \(\lambda>0\), let \(Y_1,\ldots,Y_d\) be independent with
\[
\Pr(Y_i=2j)=\frac{\lambda^{2j}}{(2j)!\cosh\lambda},\qquad j=0,1,\ldots.
\]
For every even \(L\), the joint law of \((N_1,\ldots,N_d)\) given \(X_L=0\) is exactly the law of \((Y_1,\ldots,Y_d)\) given \(\sum_iY_i=L\): the common weight of any admissible count vector is proportional to \(1/\prod_i n_i!\). The unconditioned one-site moments of this auxiliary law are
\[
\mathbb E Y_i=\lambda\tanh\lambda,
\quad \operatorname{Var}(Y_i)=\lambda\tanh\lambda+\lambda^2\operatorname{sech}^2\lambda,
\quad \Pr(Y_i=0)=\operatorname{sech}\lambda.
\]
For \(Z_i=\mathbf1_{\{Y_i=0\}}\), one has \(\operatorname{Cov}(Z_i,Y_i)=-p\mu\), where \(p=\operatorname{sech}\lambda\) and \(\mu=\lambda\tanh\lambda\). The function \(\lambda\mapsto\lambda\tanh\lambda\) is strictly increasing from zero to infinity.

**Fixed-density fluctuations.** Choose \(\lambda_d\) so that \(\mathbb EY_i=L_d/d\). In this regime the parameters \(\lambda_d\) tend to a finite positive \(\lambda\). The independent two-dimensional variables \((Z_i,Y_i/2)\) have exponentially decaying tails, a nondegenerate covariance matrix, and full difference lattice \(\mathbb Z^2\): their support contains \((1,0),(0,1),(0,2)\). Fourier inversion therefore gives a uniform two-dimensional local central limit theorem for \((\sum Z_i,\sum Y_i/2)\), and the one-dimensional local limit for \(\sum Y_i/2\). Divide the joint local approximation by the latter at its exact mean \(L_d/2\). The resulting conditional normal density has mean zero and covariance equal to the Schur complement
\[
\operatorname{Var}(Z_i)-\frac{\operatorname{Cov}(Z_i,Y_i)^2}{\operatorname{Var}(Y_i)}
=p(1-p)-\frac{p^2\mu^2}{\mu+\lambda^2p^2}.
\]
The local central limit theorem gives convergence of the normalized conditional point masses on bounded intervals, and tightness follows from the same Fourier bounds; hence the claimed conditional weak limit. Its variance is strictly positive because \(Z_i\) cannot be an affine function of \(Y_i\) on the support \(\{0,2,4,\ldots\}\). The weak limit implies the law of large numbers. For unconditioned coordinate choices, \(\mathbb EV_{d,L}/d=(1-1/d)^L\to e^{-\mu}\), and \(\operatorname{Var}(V_{d,L}/d)\to0\), by the two-coordinate untouched probability \((1-2/d)^L\). Finally, \(\lambda\tanh\lambda-\log\cosh\lambda>0\) for \(\lambda>0\), since its derivative is \(\lambda\operatorname{sech}^2\lambda>0\); exponentiation gives \(p>e^{-\mu}\).

**A local-limit ratio in the growing-mean window.** Now \(\mu_d=L_d/d=\log d+c+o(1)\), and take \(\lambda_d\tanh\lambda_d=\mu_d\). Since \(\lambda_d-\mu_d=O(\mu_de^{-2\mu_d})\),
\[
p_d=\operatorname{sech}\lambda_d=\frac{2e^{-c}+o(1)}d,
\quad v_d=\operatorname{Var}(Y_i)=\log d+O(1).
\]
For each fixed integer \(r\ge0\), the even-lattice local limit theorem for the auxiliary sums gives
\[
\frac{\Pr(\sum_{i=r+1}^dY_i=L_d)}{\Pr(\sum_{i=1}^dY_i=L_d)}\longrightarrow1.
\]
Here both numerator and denominator have the same leading local-normal factor \(2/\sqrt{2\pi d v_d}\). For completeness, this growing-parameter local theorem follows by Fourier inversion on one full period \([ -\pi/2,\pi/2]\) of the characteristic function \(\cosh(\lambda_de^{it})/\cosh\lambda_d\). Near zero its logarithm has the centered quadratic term \(-v_dt^2/2\), with higher cumulants \(O(\lambda_d)\); outside a shrinking neighborhood, the modulus is exponentially suppressed by \(d\lambda_d(1-\cos t)\). Thus Gaussian inversion is uniform for the denominator and for the numerator with \(d-r\) sites. In the latter the mean differs from \(L_d\) by \(r\mu_d=O(\log d)=o(\sqrt{d v_d})\), yielding the displayed ratio. The parity lattice factor two is the same in both terms and cancels.

Consequently the factorial moments of the *return-conditioned* number of untouched coordinates obey, for each fixed \(r\),
\[
\mathbb E[(V_{d,L_d})_r\mid X_{L_d}=0]
=(d)_r p_d^r\frac{\Pr(\sum_{i=r+1}^dY_i=L_d)}{\Pr(\sum_{i=1}^dY_i=L_d)}
\longrightarrow(2e^{-c})^r.
\]
These moments imply the asserted Poisson law, including convergence at the atom zero (e.g. by the probability-generating-function/moment method for the Poisson distribution). Unconditionally, for fixed \(r\), \(\mathbb E(V_{d,L_d})_r=(d)_r(1-r/d)^{L_d}\to e^{-cr}\), proving the comparison Poisson law. Replacing \(c\) by \(c+\log2\) matches the two limit curves and gives the stated additive \(d\log2\) coverage-window shift.

## Verification

The standalone, standard-library Python file `verify.py` computes the exact coefficient distribution by rational polynomial convolution and inclusion–exclusion. It independently enumerates coordinate words for bounded small hypercubes and compares counts and the first two factorial moments. Executing `python3 verify.py` reports **482 passed exact assertions** over \(1\le d\le7\), \(1\le L/2\le8\), with wordwise enumeration when \(d\le4\) and \(L\le8\). It also evaluates nine sample asymptotic constants as floating-point diagnostics. Finite enumeration and numerical evaluation do not constitute proofs of either asymptotic theorem; those are established in the preceding analytic argument.

## Relationship to prior work

Classical occupancy theory supplies unconditional empty-box counts and coupon-collector limits. Bogachev, Gnedin and Yakubovich analyze occupied-box variance without the simultaneous-even-count bridge condition. Muratov and Zuyev study bit flipping and recurrence of infinite, nonuniform-coordinate systems; their return-time and active-coordinate results do not state the finite-dimensional fixed-endpoint **support** laws above. Durieu and Wang study occupied and odd-occupied processes under infinite-urn regular variation, not these equal-weight return-bridge conditional fluctuations. Peixoto and Marcondes use coordinate parity in high-dimensional hypercube first-return and self-intersection questions, but do not give conditional missing-direction laws. A previously published result on two-scale correlation of exploration and Hamming displacement for unconditioned hypercube walks establishes different joint moments, not this conditional distribution or its doubled critical Poisson intensity.

The coefficient identity is an elementary exact encoding, and the conditioning/local-limit strategy uses established probabilistic methods. The distinctive quantitative claim is the unified conditional face-codimension law, particularly the factor-two critical missing-direction intensity and corresponding coverage shift; no priority is asserted for generating-function or local-limit techniques themselves.

## Limitations

Return means endpoint equality at the specified even time, **not first return**. The number of untouched coordinate directions is not the number of unvisited vertices. The critical Poisson law is only for uniform iid non-lazy flips at an even fixed time; it does not describe other endpoint constraints, unequal coordinate weights, or arbitrary growing \(L_d\) outside the given scaling windows. The fixed-density theorem does not assert a rate of normal approximation, and its centering must use the exact \(L_d/d\). A primary historical-priority risk remains: older studies of hypercube sample-path and conditional occupancy laws might contain a more general implication, and not every older full text was accessible.

## References

- L. V. Bogachev, A. V. Gnedin, and Yu. V. Yakubovich, *On the variance of the number of occupied boxes*, arXiv:math/0609498, first posted 2006-09-18, https://arxiv.org/abs/math/0609498.
- A. Muratov and S. Zuyev, *Bit flipping and time to recover*, arXiv:1310.1306, first posted 2013-10-04, https://arxiv.org/abs/1310.1306.
- O. Durieu and Y. Wang, *From infinite urn schemes to decompositions of self-similar Gaussian processes*, arXiv:1508.01506, first posted 2015-08-06, https://arxiv.org/abs/1508.01506.
- P. Diaconis, R. L. Graham, and J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72, https://doi.org/10.1002/rsa.3240010105.
- P. Matthews, *Some sample path properties of a random walk on the cube*, Journal of Theoretical Probability 2 (1989), 129–147; complete text not inspected.
- S. Peixoto and A. Marcondes, *Stopping times of random walks on a hypercube*, arXiv:1709.02359, first posted 2017-09-07, https://arxiv.org/abs/1709.02359.
