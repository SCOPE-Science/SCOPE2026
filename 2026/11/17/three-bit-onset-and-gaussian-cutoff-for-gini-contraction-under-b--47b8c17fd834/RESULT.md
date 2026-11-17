# Three-bit onset and Gaussian cutoff for Gini contraction under Boolean noise

## Finding
Let \(d\geq 1\), \(V_d=\{-1,1\}^d\), and \(0\leq\rho\leq 1\). Define the independent-coordinate noise operator
\[
(T_{d,\rho}f)(x)=\sum_{y\in V_d}2^{-d}\prod_{j=1}^{d}(1+\rho x_jy_j)f(y).
\]
With the unweighted complete-pair Gini seminorm
\[
\mathcal G_d(f)=\sum_{\{x,y\}\subset V_d}|f(x)-f(y)|,
\qquad
\gamma_d(\rho)=\sup_{\mathcal G_d(f)>0}\frac{\mathcal G_d(T_{d,\rho}f)}{\mathcal G_d(f)},
\]
the exact first three dimensions are
\[
\boxed{\gamma_1(\rho)=\gamma_2(\rho)=\rho,\qquad
\gamma_3(\rho)=\frac{\rho(15-\rho^2)}{14}.}
\]
For every \(d\geq3\) and \(0<\rho<1\),
\[
\gamma_d(\rho)\geq \gamma_3(\rho)>\rho.
\]
Here \(\rho\) is also the exact mean-zero Hilbert-space spectral norm of \(T_{d,\rho}\): three bits are the first dimension where complete-pair Gini contracts strictly more slowly than the spectral benchmark.

The high-dimensional Gini operator norm has a sharp *scale of transition*. For any sequence \(\rho_d\in[0,1]\),
\[
\boxed{
 d\rho_d^2\longrightarrow0\ \Longrightarrow\ \gamma_d(\rho_d)\longrightarrow0,
\qquad
 d\rho_d^2\longrightarrow\infty\ \Longrightarrow\ \gamma_d(\rho_d)\longrightarrow1.}
\]
At the critical scale, a single-vertex indicator has an explicit, attained finite-dimensional ratio \(R_d(\rho)\) with the Gaussian limit
\[
\boxed{\rho_d\sqrt d\longrightarrow a\in[0,\infty)
\quad\Longrightarrow\quad
R_d(\rho_d)\longrightarrow2\Phi(a/\sqrt2)-1.}
\]
This is a statement about the *single-vertex witness*; an exact Gaussian limit for the **full** operator norm inside the critical window is **not claimed**. The full norm obeys the rigorous window bounds
\[
2\Phi(a/\sqrt2)-1\leq\liminf_{d\to\infty}\gamma_d(\rho_d)
\leq\limsup_{d\to\infty}\gamma_d(\rho_d)
\leq\min\{1,4\Phi(a)-2\}.
\]
For the continuous-time process where every bit flips independently at rate one, \(\rho=e^{-2t}\). Thus the Gini contraction coefficient falls from asymptotically one to asymptotically zero across the time scale \(t=\tfrac14\log d\): if \(t_d-\tfrac14\log d\) tends to negative or positive infinity, then \(\gamma_d(e^{-2t_d})\) tends respectively to one or zero (for valid nonnegative times).

## Assumptions and scope
All vertex signals are real. Every unordered pair of different vertices receives unit Gini weight. Noise is independent over coordinates and uniform across coordinates. The operator is symmetric, bistochastic, and translation-invariant on the Boolean group. The exact finite-dimensional formula covers dimensions one through three for all \(0\leq\rho\leq1\). The dimension threshold covers every dimension at least three and every strict interior correlation. The asymptotic statements assume \(d\to\infty\) and the indicated scaling; there is no assertion of finite-dimensional singleton optimality above three bits.

## Proof
**1. Binary-cut reduction.** For any real signal with finite range, the layer-cake representation expresses \(f\), up to an additive constant, as a positive integral of indicators of superlevel sets. Positivity and constant preservation of \(T_{d,\rho}\), followed by the triangle inequality for \(\mathcal G_d\), show that \(\gamma_d\) is the maximum over nonempty proper cuts \(S\subset V_d\) of
\[
\frac{\mathcal G_d(T_{d,\rho}\mathbf1_S)}{|S|(2^d-|S|)}.
\]
An indicator therefore attains the norm in every fixed dimension.

**2. Exact dimensions and the onset.** In dimensions one and two, cut orbits under coordinate permutation, translation, and complementation yield respectively \(\rho\), and the possibilities \(\rho\) and \(\rho^2\). Thus \(\gamma_1=\gamma_2=\rho\). In dimension three there are exactly thirteen orbits of the \(254\) nontrivial cuts under cube automorphisms and complementation. Encode vertices by integers from zero through seven (binary digits) and a cut by the integer whose set bits identify its vertices. A complete set of orbit representatives and their ratios is given below. A piecewise row uses its first branch below the threshold and its second branch above it; the branches agree at the threshold.

| Representative | Ratio to input Gini |
|---|---|
| 1 | \(\rho(15-\rho^2)/14\) |
| 3 | \(\rho\) |
| 6 | \(\rho(\rho+2)/3\) |
| 7 | \(\rho\) |
| 15 | \(\rho\) |
| 22 | \(\rho(\rho^2+5)/10\) for \(\rho\leq1/3\); \(\rho(2\rho^2+\rho+2)/5\) for \(\rho\geq1/3\) |
| 23 | \(\rho(\rho^2+15)/16\) |
| 24 | \(\rho^2\) |
| 25 | \(\rho(15+8\rho-\rho^2)/30\) for \(\rho\leq\sqrt5-2\); \(\rho(\rho^2+16\rho+13)/30\) otherwise |
| 27 | \(\rho(\rho+3)/4\) |
| 30 | \(\rho(3\rho+4)/8\) for \(\rho\leq\sqrt2-1\); \(\rho(\rho+1)(\rho+7)/16\) otherwise |
| 60 | \(\rho^2\) |
| 105 | \(\rho^3\) |

Each listed expression is bounded above by the first row for \(0\leq\rho\leq1\). For example, the difference from the first row for representative 6 is \(\rho(1-\rho)(3\rho+17)/42\); the three piecewise cases have nonnegative differences on each of their stated intervals. The finite orbit verification and polynomial sign checks are replayable in `verify_hypercube_gini.py`, using exact symbolic algebra and exact rational arithmetic. The singleton cut (representative 1) is extremal. Since lifting a signal from \(d\) bits to \(d+1\) bits without using its last coordinate multiplies both input and output Gini seminorms by four, \(\gamma_{d+1}\geq\gamma_d\). Moreover \(\gamma_3-\rho=\rho(1-\rho^2)/14>0\) in the strict interior. Fourier-Walsh diagonalization gives mean-zero Hilbert norm \(\rho\), since a Walsh character of degree \(k\geq1\) has multiplier \(\rho^k\).

**3. Nonexpansivity and comparison with total variation.** Write \(N=2^d\), and let \(u\) be uniform on the \(N\) vertices. For any vector \(g\) with mean \(\bar g\), the triangle inequality and Jensen's inequality give
\[
\frac N2\sum_x|g(x)-\bar g|\leq\mathcal G_d(g)
\leq(N-1)\sum_x|g(x)-\bar g|.
\]
The noise operator is convolution by a probability measure on the Boolean group, hence a convex combination of vertex permutations. It therefore contracts Gini and \(\gamma_d\leq1\). Let \(\delta_d(\rho)=\tfrac12\max_{x,z}\sum_y|T_{d,\rho}(x,y)-T_{d,\rho}(z,y)|\) be its Dobrushin coefficient. Symmetry and the classical zero-sum \(\ell^1\) contraction inequality imply
\[
\gamma_d(\rho)\leq\min\{1,2(1-N^{-1})\delta_d(\rho)\}.
\]
By coordinatewise data processing, the maximum row distance occurs for antipodal input vertices, so \(\delta_d\) is the total-variation distance between \(d\) independent Bernoulli variables with success probabilities \((1+\rho)/2\) and \((1-\rho)/2\), respectively.

**4. A single-site lower bound and the scale transition.** For any vertex \(o\) put \(v=T_{d,\rho}\mathbf1_{\{o\}}\), viewed as a probability column. Define
\[
R_d(\rho)=\frac{\mathcal G_d(v)}{N-1}.
\]
If \(\xi_1,\ldots,\xi_d\) are independent fair signs and \(W_d=\prod_j(1+\rho\xi_j)\), then uniform sampling of the vertices gives
\[
R_d(\rho)=\frac{N}{2(N-1)}\mathbb E|W_d-W_d'|,
\]
where \(W_d'\) is an independent copy. This is an *exact* finite-dimensional identity, not an approximation. Jensen's inequality yields \(\mathcal G_d(v)\geq N\,\mathrm{TV}(v,u)\). The Hellinger affinity is
\[
\sum_y\sqrt{v(y)u(y)}
=\left(\frac{\sqrt{1+\rho}+\sqrt{1-\rho}}2\right)^d
=:a(\rho)^d,
\]
so \(\gamma_d\geq R_d\geq N(N-1)^{-1}(1-a(\rho)^d)\). Since \(a(\rho)\leq e^{-\rho^2/8}\), the norm tends to one whenever \(d\rho_d^2\to\infty\). Conversely, the chi-square divergence of the column \(v\) from uniform is \((1+\rho^2)^d-1\). Both antipodal rows are translates of this column, so \(\delta_d\leq\sqrt{(1+\rho^2)^d-1}\). The preceding upper bound forces \(\gamma_d\to0\) when \(d\rho_d^2\to0\).

**5. Gaussian critical witness and rigorous window bounds.** If \(\rho_d\sqrt d\to a<\infty\), then
\[
\log W_d=\rho_d\sum_{j=1}^d\xi_j-\frac{d\rho_d^2}{2}+o_{\mathbb P}(1)
\ \Longrightarrow\ \mathcal N(-a^2/2,a^2).
\]
The second moments \(\mathbb EW_d^2=(1+\rho_d^2)^d\) remain bounded, so \(W_d,W_d'\) are uniformly integrable and their absolute-difference expectation converges. For independent mean-one lognormals of log-standard-deviation \(a\), half the expected absolute difference is \(2\Phi(a/\sqrt2)-1\). This proves the stated single-site profile. The antipodal-row likelihood-ratio test depends only on the sign of the sum of \(d\) biased bits; the central limit theorem gives \(\delta_d(\rho_d)\to2\Phi(a)-1\). Combining this with step 3 yields the displayed bounds on all subsequential limits of the full norm. No equality of those upper and lower profiles is assumed.

## Verification
Run `python verify_hypercube_gini.py` with Python 3, SymPy, and NumPy. It checks all thirteen three-bit cut orbits, the exact branch-change domains and symbolic inequalities on each entire interval, exhaustively tests all binary cuts in dimensions one through three at six rational correlations, and separately exhaustively tests the four-bit cuts at three floating-point correlations. The latter numerical experiment is corroborative only. The unrestricted high-dimensional scale statements follow from the proof above and are not inferred from enumeration.

## Relationship to prior work
The Boolean-noise operator and its Fourier/low-influence setting are classical; Mossel, O'Donnell and Oleszkiewicz study quadratic noise stability and invariance principles, not the induced complete-pair Gini norm. Gaubert and Qu establish sharp Hopf-oscillation and total-variation contraction formulas (Dobrushin coefficients), which are used for a bound here but do not identify the Gini coefficient. Diaconis, Graham and Morrison derive a total-variation mixing profile for the **asynchronous** nearest-neighbor hypercube walk, a different transition kernel and a different functional from the induced Gini operator norm. Those results motivate, but do not directly state, the exact three-bit formula or the single-site Gini Gaussian profile. The dimensional cutoff scale is related to classical product-chain mixing and should not be construed as a new total-variation mixing-time theorem.

## Limitations
The exact full induced norm is proved only for one, two and three bits; in higher dimensions only bounds, a strict comparison, and a sharp dichotomy of scale are asserted. At the critical window the formula is exact for one-vertex indicators, **not** for arbitrary extremizers. No optimal finite-dimensional norming classification is claimed beyond three bits. The overlap search did not certify global historical priority. The process has independent bit flips and unit vertex-pair weights; other product alphabets, anisotropic flip rates, and weighted Gini measures are not covered.

## References
1. E. Mossel, R. O'Donnell, K. Oleszkiewicz, *Noise stability of functions with low influences: invariance and optimality*, arXiv:math/0503503, first posted 2005-03-23, https://arxiv.org/abs/math/0503503.
2. S. Gaubert, Z. Qu, *Dobrushin's ergodicity coefficient for Markov operators on cones*, arXiv:1307.4649, first posted 2013-07-17, https://arxiv.org/abs/1307.4649.
3. P. Diaconis, R. L. Graham, J. A. Morrison, *Asymptotic analysis of a random walk on a hypercube with many dimensions*, Random Structures & Algorithms 1 (1990), 51–72, DOI:10.1002/rsa.3240010105, openly available text at https://fanchung.ucsd.edu/ron/papers/90_02_hypercube_random_walk.pdf.
