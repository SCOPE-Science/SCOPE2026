# Sharp two-pivot greedy trace penalties for highly correlated exponential kernels

## Finding
Let \(n\ge3\), \(0<\rho<1\), and \(K_{n,\rho}\) be the real positive-definite Toeplitz covariance matrix
\[
(K_{n,\rho})_{ab}=\rho^{|a-b|},\qquad 0\le a,b<n.
\]
For a two-element subset \(S=\{i,j\}\), put
\[
E_{n,\rho}(S)=\operatorname{tr}\!\left[K_{n,\rho}-K_{n,\rho}[:,S]K_{n,\rho}[S,S]^{-1}K_{n,\rho}[S,:]\right].
\]
Write \(E_n^*\) for the minimum over all two-element sets. In diagonal-greedy pivoted Cholesky, the first pivot may be any vertex (all original diagonal entries tie); the second maximizes the remaining residual diagonal. Write \(E_n^{\mathrm{g,min}}\) and \(E_n^{\mathrm{g,max}}\) for the best and worst final trace errors across all legitimate first-pivot tie choices and second-pivot ties.

For **every** sequence \(n\to\infty\) and \(\rho_n\in(0,1)\) satisfying
\[
n(1-\rho_n^2)\longrightarrow0,
\]
the following sharp ratios hold:
\[
\boxed{\frac{E_n^{\mathrm{g,min}}}{E_n^*}\longrightarrow\frac54,
\qquad\frac{E_n^{\mathrm{g,max}}}{E_n^*}\longrightarrow\frac53.}
\]
The unrestricted trace-optimal locations converge, after division by \(n\), to \((1/5,4/5)\). The best diagonal-greedy first-pivot locations converge to \(1/4\) or \(3/4\), and the second pivot is the opposite endpoint. An endpoint-first greedy choice selects both endpoints and attains the limiting \(5/3\) ratio; a central first pivot also attains the same worst-case limiting ratio. At every finite \(n\), the endpoint pair uniquely maximizes the determinant of the selected \(2\times2\) principal kernel matrix. Thus, for this natural covariance family, the two-pivot determinant-optimal choice can have a trace error asymptotically \(5/3\) times the trace-optimal error.

This is a two-column **subset/Nyström** comparison, not a claim about best unconstrained rank-two approximation.

## Assumptions and scope
All indices are zero-based, \(0\le i<j<n\); all observations/pivots are noiseless. The kernel is normalized to have unit diagonal, the objective is the unweighted residual trace, and the two-pivot greedy rule maximizes the *residual diagonal*, not the immediate total trace reduction. The assumption \(n(1-\rho_n^2)\to0\) specifies the simultaneously large-dimension, strong-correlation regime; holding \(\rho<1\) fixed is **not** covered by these ratios.

For finite \(n\), set \(t=\rho^2\), \(d=j-i\). The exact objective, with empty sums interpreted as zero, is
\[
\begin{split}
E_{n,\rho}(\{i,j\})={}&\sum_{a=1}^{i}(1-t^a)
 +\sum_{b=1}^{n-1-j}(1-t^b)\\
 &+\sum_{s=1}^{d-1}\frac{(1-t^s)(1-t^{d-s})}{1-t^d}.
\end{split}
\]
In particular this identity permits exact finite-size evaluation without constructing or inverting an \(n\times n\) matrix.

## Proof
**1. Positive definiteness and the residual formula.** The covariance \(K_{n,\rho}\) is that of a stationary scalar Gaussian Markov chain \(X_{k+1}=\rho X_k+\sqrt{1-\rho^2}\,Z_k\) with independent standard Gaussian innovations. It is positive definite for \(0<\rho<1\). The selected-column Nyström residual is the Gaussian conditional covariance given \(X_i,X_j\). If \(k<i\), the Markov property makes \(X_i\) separate \(X_k\) from \(X_j\), so its conditional variance is \(1-\rho^{2(i-k)}\); symmetrically for \(k>j\). If \(i<k<j\), direct inversion of the selected \(2\times2\) covariance yields
\[
\operatorname{Var}(X_k\mid X_i,X_j)
=\frac{(1-t^{k-i})(1-t^{j-k})}{1-t^{j-i}}.
\]
Summing these diagonal terms proves the displayed exact formula. The selected-site variances vanish.

**2. Greedy-pivot restriction.** At the initial stage each diagonal is \(1\), so every first index is permitted. After first pivot \(i\), its residual variance at \(j\) is \(1-t^{|i-j|}\), strictly increasing with the distance \(|i-j|\). Hence the second pivot is one of the two path endpoints farthest from \(i\); two choices can tie only when \(i\) is the center.

**3. Uniform strong-correlation asymptotics.** Let \(\epsilon_n=1-\rho_n^2\), with \(n\epsilon_n\to0\). Uniformly in integer \(0\le k\le n\),
\[
1-(1-\epsilon_n)^k=k\epsilon_n\bigl(1+O(n\epsilon_n)\bigr).
\]
For \(1\le s<d\le n-1\), using the same bound in the numerator and denominator gives, uniformly,
\[
\frac{(1-t^s)(1-t^{d-s})}{1-t^d}
=\epsilon_n\frac{s(d-s)}d\bigl(1+O(n\epsilon_n)\bigr).
\]
The exact finite sums \(\sum_{a=1}^{i}a=i(i+1)/2\) and \(\sum_{s=1}^{d-1}s(d-s)/d=(d^2-1)/6\) now give
\[
E_{n,\rho_n}(\{i,j\})
=\epsilon_n\left[\frac{i(i+1)}2+\frac{(n-1-j)(n-j)}2+\frac{d^2-1}6\right]
\bigl(1+O(n\epsilon_n)\bigr).
\]
The error statement is uniform across all distinct pairs, because the summed terms are nonnegative. With \(x=i/n\), \(y=j/n\), it follows uniformly that
\[
\frac{E_{n,\rho_n}(\{i,j\})}{\epsilon_n n^2}
=F(x,y)+O(n\epsilon_n+n^{-1}),
\quad F(x,y)=\frac{x^2}2+\frac{(1-y)^2}2+\frac{(y-x)^2}6.
\]
The formula extends continuously to the closed triangle \(0\le x\le y\le1\); the discrete feasible pairs become dense in it.

**4. Unrestricted optimum.** The Hessian of \(F\), in variables \((x,y)\), is
\[
\begin{pmatrix}4/3&-1/3\\-1/3&4/3\end{pmatrix},
\]
which is positive definite. The unique stationary point is \((x,y)=(1/5,4/5)\), strictly inside the triangle, and its objective is \(F=1/10\). Uniform convergence and compactness give \(E_n^*/(\epsilon_n n^2)\to1/10\) and convergence of all minimizing site pairs to this point.

**5. Best and worst diagonal-greedy choices.** By reflection it suffices to consider first sites \(0\le x\le1/2\), when the second site is the right endpoint. Their limiting objective is
\[
f(x)=F(x,1)=\frac{x^2}2+\frac{(1-x)^2}6
=\frac18+\frac23\left(x-\frac14\right)^2.
\]
Its unique minimum on this half-interval is \(1/8\) at \(x=1/4\); its maximum is \(1/6\) at both \(x=0\) and \(x=1/2\). Reflection adds the positions \(3/4\) for best and \(1\) for worst. Uniform convergence on the discrete greedy site pairs gives \(E_n^{\mathrm{g,min}}/(\epsilon_n n^2)\to1/8\) and \(E_n^{\mathrm{g,max}}/(\epsilon_n n^2)\to1/6\). Dividing by the positive unrestricted limit \(1/10\) yields \(5/4\) and \(5/3\).

**6. Determinant contrast.** For any pair \(i<j\),
\[
\det K_{n,\rho}[\{i,j\},\{i,j\}]=1-\rho^{2(j-i)}.
\]
This strictly increases with \(j-i\), so the unique determinant-maximizing pair is \(\{0,n-1\}\). It is also exactly the pair produced by an endpoint-first diagonal-greedy run. The already-proved asymptotic objective gives its sharp trace ratio \(5/3\).

## Verification
The companion `check.py` independently evaluates Schur complements using exact rational \(2\times2\) inverses and compares them to the Markov-bridge trace formula for every two-site subset of sizes \(3\) through \(11\), at four rational correlations. It also checks the farthest-endpoint greedy-pivot rule for every first site, totaling 1,128 exact checks. Separate large-size numerical comparisons illustrate convergence of the ratios but are not substitutes for the uniform analytic proof. Run with `python check.py`; it uses the Python standard library only.

## Relationship to prior work
Liu and Matthies (2015) formulate diagonal-pivoted Cholesky/cross approximation for kernel matrices and explicitly use a maximum-residual-diagonal rule. Harbrecht, Peters and Schneider (2012) study trace-norm performance of pivoted Cholesky. Chen, Epperly, Tropp and Webber (2022/2024) discuss the impact of diagonal-pivot ties, including dependence on input ordering, and give general approximation results. The present claim is restricted to an explicit stationary exponential covariance, the two-pivot algorithm, and the sharp **relative trace-error** penalties of the permitted greedy choices, rather than introducing pivoted Cholesky or a new OU optimal-design principle.

Optimal-design research by Mukherjee (2002) and Baldi Antognini–Zagoraiou (2010) already treats OU/Markov covariance prediction problems; the unrestricted site-placement limit alone is not claimed as new. The incremental content here is the sharp greedy-versus-optimal trace loss and determinant-optimal-vs-trace-optimal comparison for the same kernel. The complete text of these two optimal-design sources was not available for this comparison, so a bibliographic-priority caveat remains.

## Limitations
The constants require \(n\to\infty\) jointly with \(n(1-\rho_n^2)\to0\), and cannot be extended to fixed \(\rho<1\) without further analysis. This theorem does not compare with unconstrained spectral rank-two approximation, randomized pivot selection, or greedy rules optimizing a different gain. It does not assert that the OU optimal two-point design, the Markov bridge covariance, or pivot-tie pathology is new. Full text of some historical OU design literature remains an originality risk. No independent audit has been performed.

## References
1. D. Liu and H. G. Matthies, *Pivoted Cholesky decomposition by Cross Approximation for efficient solution of kernel systems* (first arXiv version, 2015-05-21), https://arxiv.org/abs/1505.06195.
2. H. Harbrecht, M. Peters and R. Schneider, *On the low-rank approximation by the pivoted Cholesky decomposition*, Applied Numerical Mathematics 62 (2012), 428–440, https://doi.org/10.1016/j.apnum.2011.10.001.
3. Y. Chen, E. N. Epperly, J. A. Tropp and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations* (arXiv 2022; journal 2024), https://arxiv.org/abs/2207.06503.
4. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process* (doctoral thesis, 2002), https://docs.lib.purdue.edu/dissertations/AAI3043760/.
5. A. Baldi Antognini and M. Zagoraiou, *Exact optimal designs for computer experiments via Kriging metamodelling*, Journal of Statistical Planning and Inference 140 (2010), 2607–2617, https://doi.org/10.1016/j.jspi.2010.03.027.
