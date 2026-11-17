# A sharp universal discount-calibration barrier between Abel and Cesàro averages

## Finding
For every integer \(n\ge2\), every real or complex Banach space \(X\), and every linear contraction \(T:X\to X\), define the finite-horizon Cesàro average and the geometric Abel average by
\[
C_n(T)=\frac1n\sum_{k=0}^{n-1}T^k,\qquad
A_p(T)=p\sum_{k=0}^{\infty}(1-p)^kT^k,\quad 0<p\le1.
\]
Set \(E_n=\inf_{0<p\le1}\sup_{X,T:\,\|T\|\le1}\|C_n(T)-A_p(T)\|\). Then the exact finite-horizon objective is
\[
\sup_{X,T:\,\|T\|\le1}\|C_n(T)-A_p(T)\|
=F_n(p):=2\left[(1-p)^n+\sum_{k=0}^{n-1}\left(p(1-p)^k-\frac1n\right)_+\right],
\]
where \((z)_+=\max\{z,0\}\). In fact, the same unilateral shift on \(\ell^\infty(\mathbb N_0)\) achieves equality for every \(n,p\) (with a parameter-dependent norming vector).

There is one constant \(\lambda_*\in(1,2)\) solving
\[
\log\lambda_*=\lambda_*^2e^{-\lambda_*},\qquad
\lambda_*=1.694600920503554\ldots.
\]
Every choice \(p_n\) minimizing \(F_n\) satisfies \(np_n\to\lambda_*\), and
\[
\boxed{\lim_{n\to\infty}E_n
=\kappa:=2\left[1-\frac{1+\log\lambda_*}{\lambda_*}+e^{-\lambda_*}\right]
=0.564622925201137\ldots.}
\]
At the conventional matching \(p=1/n\), the limit is instead \(2/e=0.735758882342884\ldots\). Consequently, no horizon-dependent choice of one geometric discount uniformly approximates the length-\(n\) Cesàro average over all Banach-space contractions in operator norm: even optimal calibration has asymptotic error \(\kappa>0\).

## Assumptions and scope
All Banach spaces are nonzero and may be real or complex. A contraction satisfies \(\|T\|\le1\); no compactness, spectral-gap, ergodicity, positivity, or finite-dimensionality is assumed. The operator series defining \(A_p(T)\) converges in norm for \(0<p\le1\). The supremum ranges jointly over all spaces and all contractions. Here \(n\) is an integer at least two and \(p\) is a real discount probability in \((0,1]\). The minimizer exists strictly inside \((0,1)\) for each \(n\). The theorem is about universal worst-case operator-norm discrepancy, **not** about whether both averages converge for a particular ergodic operator.

## Proof
**1. Coefficient norm and a universal extremizer.** Let \(c_k=1/n\) for \(0\le k<n\) and \(c_k=0\) otherwise, and put \(g_k=p(1-p)^k\). The triangle inequality and \(\|T^k\|\le1\) give
\[
\|C_n(T)-A_p(T)\|\le\sum_{k=0}^{\infty}|c_k-g_k|.
\]
For the fixed unilateral shift \((Sf)(j)=f(j+1)\) on \(\ell^\infty(\mathbb N_0)\), choose \(f(k)=\operatorname{sgn}(c_k-g_k)\), taking either sign when a coefficient vanishes. Then \(\|f\|_\infty=1\) and the value of \((C_n(S)-A_p(S))f\) at coordinate zero equals the entire coefficient absolute sum. Thus the upper bound is an equality for this one fixed contraction.

**2. Exact finite formula.** Since \(\sum c_k=\sum g_k=1\), positive and negative parts of \(g-c\) have the same total mass. Outside the first \(n\) indices the positive mass is \(\sum_{k=n}^{\infty}g_k=(1-p)^n\); inside, it is \(\sum_{k<n}(g_k-1/n)_+\). Twice this positive mass is the asserted \(F_n(p)\). The map \(p\mapsto F_n(p)\) extends continuously to \(p=0\) with value two. At \(p=1\) it equals \(2(1-1/n)\), while at \(p=1/n\) it equals \(2(1-1/n)^n\), strictly smaller than both endpoint values. Hence a minimizer exists in \((0,1)\).

**3. Continuum scaling.** For any fixed \(\lambda\ge0\), put \(p=\lambda/n\) for sufficiently large \(n\). The geometric tail tends to \(e^{-\lambda}\). The positive finite sum is a Riemann sum:
\[
\sum_{k=0}^{n-1}\left(\frac\lambda n(1-\lambda/n)^k-\frac1n\right)_+
\longrightarrow\int_0^1(\lambda e^{-\lambda t}-1)_+\,dt.
\]
Convergence is uniform when \(\lambda\) is in a compact interval. Direct integration gives the continuous limit
\[
\Phi(\lambda)=\begin{cases}
2e^{-\lambda},&0\le\lambda\le1,\\
2\left[1-\frac{1+\log\lambda}{\lambda}+e^{-\lambda}\right],&\lambda>1.
\end{cases}
\]
In particular \(F_n(1/n)\to2/e\).

**4. A unique limiting calibration.** The function \(\Phi\) decreases on \([0,1]\). For \(\lambda>1\),
\[
\Phi'(\lambda)=2\left[\frac{\log\lambda}{\lambda^2}-e^{-\lambda}\right].
\]
Define \(h(\lambda)=e^{\lambda}\log\lambda/\lambda^2\). Its derivative has the sign of \(1+(\lambda-2)\log\lambda\). This is positive for \(\lambda\ge2\); for \(1<\lambda<2\), use \(0<(2-\lambda)\log\lambda\le(2-\lambda)(\lambda-1)\le1/4\). Thus \(h\) is strictly increasing from zero to infinity, crossing one exactly once at \(\lambda_*\in(1,2)\). Therefore \(\Phi\) has exactly one global minimizer, \(\lambda_*\), with minimum \(\kappa\).

**5. Minima cannot escape the scaling window.** Let \(p_n\) minimize \(F_n\), and let \(\lambda_n=np_n\). Since \(F_n(\lambda_*/n)\to\kappa<2\), any sequence of minimizers has values bounded away from two eventually. If along a subsequence \(\lambda_n\to0\), then \(F_n(p_n)\ge2(1-p_n)^n\to2\), a contradiction. If \(\lambda_n\to\infty\), choose \(m_n=\lfloor n/\sqrt{\lambda_n}\rfloor\). Then \(m_n/n\to0\), and the first \(m_n\) geometric weights have mass \(1-(1-p_n)^{m_n}\to1\) because \(p_nm_n\to\infty\). The uniform weights give the same initial segment mass \(m_n/n\to0\). Their absolute coefficient distance is at least twice the difference of these two segment masses, so \(F_n(p_n)\to2\), again a contradiction. Thus every subsequence of \(\lambda_n\) has a further subsequence converging inside \((0,\infty)\). Uniform-on-compact convergence of \(F_n(\lambda/n)\) and uniqueness of the minimizer of \(\Phi\) force each limit to equal \(\lambda_*\). Consequently \(\lambda_n\to\lambda_*\) and \(E_n\to\kappa\).

**6. Exact finite candidate reduction.** On any open interval of probabilities on which exactly \(j\) of the inequalities \(p(1-p)^k>1/n\), \(0\le k<n\), hold, the active indices are precisely \(0,\ldots,j-1\). Then, with \(r=1-p\), \(F_n(p)/2=1-r^j-j/n+r^n\). Every smooth interior critical point consequently has \(r^{n-j}=j/n\). There are at most \(n-1\) active indices because \(p(1-p)^{n-1}<1/n\). It follows that the exact finite minimum can be found by evaluating \(F_n\) at the endpoints, at the finite set of crossing roots \(p(1-p)^k=1/n\) and at the candidate points \(p=1-(j/n)^{1/(n-j)}\), \(1\le j<n\). A candidate need not be in its purported active-index interval, but keeping all candidates preserves exactness. This is an optional finite algorithm; the limiting theorem does not depend on numerical minimization.

## Verification
Run `python3 check_abel_cesaro.py` with standard Python. It verifies the coefficient identity using exact rational arithmetic on 1,800 instances across \(2\le n\le26\); checks sign patterns, the shift norm and finite candidate rule; and compares the limiting equation with finite-horizon evaluations. The analytical arguments above, rather than numerical extrapolation, prove the limit and uniqueness of the limiting optimizer.

## Relationship to prior work
Kozitsky, Shoikhet and Zemanek (arXiv:1208.0936, first posted 2012-08-04) study power convergence of Abel resolvent averages and recall operator-norm Abel/Cesàro ergodic equivalences under hypotheses. Estrada and Vindas (arXiv:1201.1408, 2012-01-06) prove Tauberian implications between summability methods under additional assumptions. Ziliotto (arXiv:1501.06525, 2015-01-26) proves convergence equivalences in a nonexpansive dynamic setting. Those conclusions do not state or imply a uniform quantitative minimax approximation over *all* contractions: the shift witness is not restricted by a uniform ergodicity hypothesis. The contribution claimed here is the exact finite universal discrepancy formula, its optimized positive limiting barrier, and the unique asymptotic discount rate—not equivalence of Abel and Cesàro limits.

## Limitations
No exact closed-form minimizing discount is asserted for each individual finite \(n\); the finite candidate recipe is exact but can have active-set boundary minima. The universal obstruction does not prevent convergence or small discrepancies for particular operators with additional structure. Historical originality is qualified by possible unindexed literature on total-variation approximation of uniform laws by geometric laws. Numerical experiments are checks, not proofs of the asymptotic theorem.

## References
1. Y. Kozitsky, D. Shoikhet, J. Zemanek, *Power convergence of Abel averages*, arXiv:1208.0936, first publicly posted 2012-08-04, https://arxiv.org/abs/1208.0936.
2. R. Estrada, J. Vindas, *Distributional versions of Littlewood's Tauberian theorem*, arXiv:1201.1408, first publicly posted 2012-01-06, https://arxiv.org/html/1201.1408v1.
3. B. Ziliotto, *A Tauberian theorem for nonexpansive operators and applications to zero-sum stochastic games*, arXiv:1501.06525, first publicly posted 2015-01-26, https://arxiv.org/abs/1501.06525.
