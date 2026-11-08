# Essential-range rigidity of random two-state metastable weights

## Finding

For an independently driven two-state stochastic-matrix cocycle whose transition probabilities are proportional to a small parameter, the random stationary mass converges to the averaged stationary mass in mean square, yet **uniform convergence over environmental histories holds if and only if all environment types have the same stationary proportion**. More precisely, for every admissible perturbation size, the essential range of the stationary left-state mass has endpoints equal to the smallest and largest stationary proportions of the individual environment matrices. Its exact essential-supremum distance from the averaged mass is therefore independent of the perturbation size. An exact variance formula quantifies the simultaneous mean-square concentration.

## Assumptions and scope

Fix an integer \(k\ge2\), probabilities \(p_j>0\) with \(\sum_{j=1}^k p_j=1\), and finite rates \(a_j,b_j>0\). Put \(s_j=a_j+b_j\), \(u_j=b_j/s_j\), \(u_-=\min_j u_j\), and \(u_+=\max_j u_j\). Let \(\Omega=\{1,\ldots,k\}^{\mathbb Z}\) carry the two-sided product probability with symbol probabilities \(p_j\), and let \(\sigma\) be the left shift. For every
\[
0<\varepsilon<1/\max_j s_j,
\]
consider the column-stochastic matrices
\[
M_j^\varepsilon=\begin{pmatrix}1-\varepsilon a_j&\varepsilon b_j\\\varepsilon a_j&1-\varepsilon b_j\end{pmatrix}.
\]
Let \(v_\varepsilon(\omega)=(W_\varepsilon(\omega),1-W_\varepsilon(\omega))^{\mathsf T}\) be the unique pullback stationary probability vector satisfying \(v_\varepsilon(\sigma\omega)=M_{\omega_0}^\varepsilon v_\varepsilon(\omega)\). Expectations and essential suprema below refer to the product probability, not to a fixed deterministic history. Define the averaged mass
\[
m=\frac{\sum_j p_jb_j}{\sum_j p_js_j}.
\]

**Theorem.** For every admissible \(\varepsilon\),
\[
\operatorname{ess\,inf}W_\varepsilon=u_-,\qquad
\operatorname{ess\,sup}W_\varepsilon=u_+,
\]
\[
\boxed{\ \|W_\varepsilon-m\|_{L^\infty}
=\max\{m-u_-,u_+-m\}\ },
\]
and
\[
\boxed{\ \mathbb E W_\varepsilon=m,\qquad
\operatorname{Var}(W_\varepsilon)=
\frac{\varepsilon\,\mathbb E[(B-mS)^2]}
{2\mathbb E S-\varepsilon\mathbb E[S^2]}\ },
\]
where \((S,B)=(s_j,b_j)\) with probability \(p_j\). In particular, \(W_\varepsilon\to m\) in \(L^2\) with standard deviation of order \(\sqrt\varepsilon\) whenever the \(u_j\) are not all equal. In contrast,
\[
\lim_{\varepsilon\downarrow0}\|W_\varepsilon-m\|_{L^\infty}=0
\quad\Longleftrightarrow\quad u_1=\cdots=u_k,
\]
and in the latter case \(W_\varepsilon=m\) almost surely for every admissible \(\varepsilon\). The vector \(\ell^1\) essential-supremum deviation is twice the scalar deviation displayed above.

For the explicit fair two-type environment \((a_1,b_1)=(1,1)\), \((a_2,b_2)=(3,1)\), and \(p_1=p_2=1/2\), every \(0<\varepsilon<1/4\) satisfies
\[
m=1/3,\qquad
\|W_\varepsilon-1/3\|_{L^\infty}=1/6,\qquad
\operatorname{Var}(W_\varepsilon)=\frac{\varepsilon}{9(6-10\varepsilon)}.
\]

## Proof

**Pullback existence and bounds.** The first coordinate evolves under the contraction
\[
F_j^\varepsilon(w)=(1-\varepsilon s_j)w+\varepsilon b_j
=u_j+(1-\varepsilon s_j)(w-u_j).
\]
Every contraction factor \(r_j=1-\varepsilon s_j\) lies strictly between zero and one. Consequently, finite past compositions converge uniformly in their initial value, producing a unique random stationary coordinate. Each \(F_j^\varepsilon\) maps \([u_-,u_+]\) into itself, so the stationary coordinate lies in that interval almost surely.

**Sharp essential endpoints.** Fix a symbol \(j\), a perturbation size \(\varepsilon\), and an integer \(N\ge1\). The event that the latest \(N\) environmental symbols are all \(j\) has probability \(p_j^N>0\). On that event, for some past value \(w\in[u_-,u_+]\),
\[
W_\varepsilon=u_j+r_j^N(w-u_j),\qquad
|W_\varepsilon-u_j|\le r_j^N(u_+-u_-).
\]
For fixed \(\varepsilon\), this upper bound tends to zero as \(N\to\infty\), while each event retains positive probability. Therefore every \(u_j\) belongs to the essential closure of the stationary law, and both extremal \(u_j\)'s are its essential endpoints. Since \(m=(\sum p_js_ju_j)/(\sum p_js_j)\in[u_-,u_+]\), the exact essential-supremum formula follows. If all \(u_j\) coincide, every affine map fixes their common value and the unique pullback state is deterministic; otherwise the exact uniform gap is strictly positive.

**Mean and variance.** In the iid shift, the stationary coordinate at time zero depends only on negative-time symbols and is independent of the symbol at time zero. With \(W'=F_J^\varepsilon(W)\) having the same law as \(W\), taking expectations yields
\[
\mathbb EW=(1-\varepsilon\mathbb ES)\mathbb EW+\varepsilon\mathbb EB,
\]
hence \(\mathbb EW=m\). Center \(Z=W-m\), and put \(\xi=B-mS\). The stationary recurrence becomes
\[
Z'=(1-\varepsilon S)Z+\varepsilon\xi.
\]
Here \(Z\) is independent of \((S,\xi)\) and \(\mathbb EZ=\mathbb E\xi=0\). Squaring and taking expectations gives
\[
V=\mathbb E[(1-\varepsilon S)^2]V+\varepsilon^2\mathbb E[\xi^2].
\]
Since \(1-\mathbb E[(1-\varepsilon S)^2]=\varepsilon(2\mathbb ES-\varepsilon\mathbb ES^2)>0\), the stated formula follows. The numerator vanishes precisely when \(b_j=ms_j\) for all types, which is equivalent to equality of all \(u_j\). Otherwise the variance has a positive coefficient multiplying \(\varepsilon+O(\varepsilon^2)\), proving the sharp square-root mean-square fluctuation scale. Chebyshev's inequality also gives convergence in probability.

**Explicit two-type calculation.** The two type-specific proportions are \(1/2\) and \(1/4\), and \(\mathbb ES=3\), \(\mathbb EB=1\), \(\mathbb ES^2=10\), and \(\mathbb E[(B-mS)^2]=1/9\). Substitution yields the formulas in the theorem.

## Verification

The standalone reproducible script `check.py` uses exact rational arithmetic for the two-type witness. It exhaustively enumerates all \(2^n\) type histories for \(1\le n\le8\), at each of four admissible perturbation sizes. It checks the exact finite-time mean and variance recurrence, the invariant interval and the contracting endpoint words. It reports 2,040 finite histories, 64 rational mean/variance equalities and four parameter checks. These finite computations are supporting tests, not the proof of the infinite-history theorem.

## Relationship to prior work

González-Tokman and Peters, *Averaging for random metastable systems* (first arXiv release 14 June 2024, subsequently *Nonlinearity* 38 (2025), 105018), study random invariant densities and explicitly introduce the two-state stochastic matrix cocycle displayed in their introduction and Remark 5.4. Their equations establish an averaged limiting stationary vector for almost every environment, and Remark 5.4 asserts that a uniform-over-environments strengthening follows. The theorem above isolates the matrix cocycle, not the underlying interval maps, and supplies a sharp necessary-and-sufficient boundary for that stronger mode of convergence under iid finite-type driving. Distinct instantaneous stationary ratios produce a positive essential-supremum gap at every perturbation size, although mean-square averaging remains valid. **This is a matrix-level comparison only:** it does not construct an interval-map realization satisfying every condition of the paper's interval-map theorem and does not by itself refute that theorem.

The authors' later *Jumping for Diffusion in Random Metastable Systems* (2026) studies jump distributions and diffusion coefficients, rather than the essential range of the random stationary two-state vector. Standard iterated-function-system theory already supplies general contraction and attractor principles; those generic principles, and the basic mean/variance calculation in isolation, are not claimed as new. The point is the exact uniform-versus-mean-square dichotomy in the specific metastable Markov-cocycle setting and its implication for uniform quenched averaging claims.

## Limitations

The forcing is a two-sided iid finite alphabet with strictly positive type probabilities and strictly positive transition rates; no assertion is made for arbitrary ergodic forcing, zero rates, or non-Markov finite-dimensional reductions. The result addresses the stationary **matrix cocycle**, not a full random interval-map transfer-operator cocycle. Essential-supremum failure does not preclude pointwise almost-sure convergence on a fixed full-measure set or convergence in probability. Classical random affine recursion literature may contain equivalent versions of the endpoint-support rigidity; publication-priority verification beyond the inspected works remains warranted. No external or independent mathematical audit has been performed.

## References

1. C. González-Tokman and J. Peters, *Averaging for random metastable systems*, arXiv:2406.09672 (first public 2024-06-14), especially Remark 5.4 and Section 5; *Nonlinearity* **38** (2025), 105018, DOI:10.1088/1361-6544/ae11f0.
2. C. González-Tokman and J. Peters, *Jumping for Diffusion in Random Metastable Systems*, *Annales Henri Poincaré* (published 2026-07-28), DOI:10.1007/s00023-026-01738-4, arXiv:2505.22996.
3. M. F. Barnsley, *Fractals Everywhere*, Academic Press (1988), for standard iterated-function-system contraction background; no specific new statement in this result is attributed to the monograph.
