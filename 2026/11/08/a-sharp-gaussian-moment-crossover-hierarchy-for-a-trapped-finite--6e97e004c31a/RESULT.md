# A sharp Gaussian moment-crossover hierarchy for a trapped finite-tumble particle

## Finding

A harmonically confined one-dimensional run-and-tumble particle with finite-duration pauses has a **unique Gaussian-moment crossing at every even order beyond variance**. Although the complete stationary moments were available previously, their joint order–switching-rate phase diagram and its singular high-order scale have a sharp form.

Normalize the trap relaxation and active speed to one. Write \(R>0\) for the rate of leaving a running state, \(T>0\) for the rate of leaving the nonpropelling tumble state, and \(m_{2n}=\mathbb E[X^{2n}]\) for the stationary even moment. For every integer \(n\ge 2\), define the matched-variance Gaussian ratio
\[
Q_n(R,T)=\frac{m_{2n}}{(2n-1)!!\,m_2^n}.
\]
For each fixed \(R>0\), there is exactly one \(T_n(R)\in(0,\infty)\) satisfying \(Q_n(R,T_n(R))=1\). More precisely,
\[
Q_n(R,T)>1\quad(0<T<T_n(R)),\qquad Q_n(R,T)<1\quad(T>T_n(R)),
\]
and \(Q_n(R,\cdot)\) is strictly decreasing. Thus long tumble residence can produce excess high-order Gaussian-normalized moments, while sufficiently rapid tumble exit produces a deficit. This comparison concerns moments, not a stochastic or tail ordering of distributions.

The finite-order boundary is defined explicitly by the strictly monotone product equation
\[
\prod_{j=2}^{n}\frac{(R+1)(R+T)(T+2j-2)}{T(R+2j-1)(R+T+2j-2)}=1.
\]
In particular,
\[
T_2(R)=\frac{\sqrt{5R^2+8R+4}-R-2}{2}.
\]

The hierarchy has a **sharp singular large-order law**, including its logarithmic displacement. Set
\[
c_R=\frac{eR(R+1)}{2},\qquad
B_R=\log\!\left(\frac{c_R\Gamma((R+1)/2)\Gamma(R/2)}{2\sqrt{2\pi}}\right)+\frac{c_R}{R}.
\]
Then, with \(R>0\) fixed and \(n\to\infty\),
\[
\boxed{T_n(R)=\frac{c_R}{n}\left[1-\frac{(R+1)\log n-B_R}{n}+O_R\!\left(\frac{(\log n)^2}{n^2}\right)\right].}
\]
In particular, \(nT_n(R)\to c_R\). The conclusion is not a claim of uniformity when \(R\) simultaneously tends to zero or infinity.

## Assumptions and scope

Let \(X_t\) solve \(\dot X_t=-X_t+S_t\) and let \(S_t\) be a continuous-time Markov chain on \(\{-1,0,+1\}\). Each state \(+1\) or \(-1\) transitions to \(0\) at rate \(R\); the state \(0\) transitions to each of \(\pm1\) at rate \(T/2\). Each new running direction is independent of the preceding running direction. Both rates are finite and strictly positive; no translational Brownian noise is present. This is the one-dimensional finite-tumble model of Sun, Ye and Podgornik with dimensionless parameters \(R=\gamma_R/b\), \(T=\gamma_T/b\), and position \(X=bx/v\).

The irreducible internal chain has a unique stationary law. Its pullback position solution \(X_t=\int_{-\infty}^{t}e^{-(t-s)}S_s\,ds\) is well-defined, supported in \([-1,1]\), and unique by exponential contraction. Symmetry gives vanishing odd moments. Every assertion concerns the exact stationary ensemble law, not empirical finite-sample estimates.

## Proof

**1. Reconstruct the stationary moment recurrence.** Define \(u_k=\mathbb E[X^k\mathbf1_{\{|S|=1\}}]\), \(z_k=\mathbb E[X^k\mathbf1_{\{S=0\}}]\), \(h_k=\mathbb E[X^kS]\), and \(m_k=u_k+z_k\). Applying the stationary Markov generator to \(X^k\), \(X^{k-1}S\), and \(X^k\mathbf1_{\{|S|=1\}}\) gives, for integers \(k\ge1\),
\[
m_k=h_{k-1},\qquad (k-1+R)h_{k-1}=(k-1)u_{k-2}\quad(k\ge2),
\]
\[
(k+R+T)u_k=(k+T)m_k.
\]
Taking \(k=2j\) in the first two identities and \(k=2j-2\) in the third yields the exact product recurrence
\[
m_{2j}=\frac{2j-1}{2j-1+R}\frac{2j-2+T}{2j-2+R+T}\,m_{2j-2},\qquad m_0=1.
\]
It follows in particular that \(m_2=T/[(R+1)(R+T)]\), and all the moment formulas here agree with the known stationary characteristic function. This recurrence itself is **not** claimed as new.

**2. Strict monotonicity and uniqueness of every boundary.** Dividing the above recurrence by the matched-variance Gaussian moments gives the displayed finite product for \(Q_n\). For \(j\ge2\), its logarithmic factor has \(T\)-derivative
\[
\frac1{T+2j-2}-\frac1{R+T+2j-2}-\frac1T+\frac1{R+T}<0,
\]
because \(x\mapsto 1/x-1/(x+R)=R/[x(x+R)]\) strictly decreases for \(x>0\). Hence \(Q_n(R,\cdot)\) strictly decreases for all integers \(n\ge2\). As \(T\downarrow0\), the stationary even moment has first-order size \(m_{2n}\asymp_R T\), whereas \(m_2^n\asymp_R T^n\), so \(Q_n(R,T)\to\infty\). As \(T\to\infty\),
\[
Q_n(R,T)\longrightarrow\prod_{j=2}^{n}\frac{R+1}{R+2j-1}<1.
\]
Continuity and strict decrease prove existence, uniqueness and the strict sign regimes. For \(n=2\), clearing positive denominators reduces equality to \(R^2+R-RT-T^2-2T=0\), yielding the displayed positive root.

**3. Gamma representation and double scaling.** The known moment recurrence has the exact gamma-product form
\[
m_{2n}=\frac{\Gamma(n+1/2)\Gamma((R+1)/2)}{\sqrt\pi\,\Gamma(n+(R+1)/2)}
\frac{\Gamma(n+T/2)\Gamma((R+T)/2)}{\Gamma(T/2)\Gamma(n+(R+T)/2)}.
\]
Let \(c>0\) vary over any fixed compact subinterval of \((0,\infty)\), and set \(T=c/n\). Uniform gamma-ratio asymptotics for fixed \(R>0\) give
\[
m_{2n}=\frac{c\Gamma((R+1)/2)\Gamma(R/2)}{2\sqrt\pi}\,n^{-(R+1)}[1+O_R(n^{-1})].
\]
Meanwhile Stirling's formula and \(m_2=T/[(R+1)(R+T)]\) give
\[
(2n-1)!!\,m_2^n=\sqrt2\,e^{-c/R}\left(\frac{2c}{eR(R+1)}\right)^n[1+O_R(n^{-1})].
\]
Here both error statements are uniform for \(c\) on such a compact set. Thus
\[
\log Q_n(R,c/n)=n\log(c_R/c)-(R+1)\log n
+\log\!\left(\frac{c\Gamma((R+1)/2)\Gamma(R/2)}{2\sqrt{2\pi}}\right)+\frac cR+O_R(n^{-1}).
\]
Dividing by \(n\) shows that the sign of \(Q_n(R,c/n)-1\) is eventually positive when \(c<c_R\) and negative when \(c>c_R\). Strict monotonicity therefore brackets \(c_n=nT_n(R)\) in every sufficiently small neighborhood of \(c_R\), proving \(c_n\to c_R\).

**4. Logarithmic correction and remainder.** Substituting \(c=c_n\) into the displayed log-ratio expansion, which is now valid uniformly in a compact neighborhood of \(c_R\), and using \(\log Q_n(R,c_n/n)=0\), gives
\[
n\log(c_R/c_n)=(R+1)\log n-B_R+O_R(|c_n-c_R|+n^{-1}).
\]
The same relation first implies \(c_n-c_R=O_R((\log n)/n)\). Expanding the logarithm with this estimate and solving yields
\[
c_n=c_R\left[1-\frac{(R+1)\log n-B_R}{n}
+O_R\!\left(\frac{(\log n)^2}{n^2}\right)\right],
\]
which is the asserted sharp expansion after dividing by \(n\). No finite collection of numerical roots is used to justify this infinite-order conclusion.

## Verification

The standalone standard-library checker `check.py` evaluates stationary-generator equations in exact rational arithmetic and compares them with the gamma/product recurrence for multiple rate pairs and even orders through \(24\). It separately tests the exact fourth-moment crossing, numerical uniqueness brackets for several finite orders, and the limiting \(1/n\) scale. The package reproduces **206 finite diagnostic assertions**. These are computational consistency checks; the infinite-order uniqueness and asymptotic conclusions rely on the proof above, not on finite sampling.

The logarithmic correction can also be checked directly: at \(R=1\), the critical constant is \(c_R=e\); numerically \(10000T_{10000}(1)\approx2.7140043\), approaching \(e\) with the predicted \((\log n)/n\) displacement.

## Relationship to prior work

Sun, Ye and Podgornik, arXiv:2409.00578 (first public version September 1, 2024), derive the exact stationary distribution and an arbitrary-order moment recursion for a trapped particle with finite tumble time. Their section III and equation (38) give the underlying one-dimensional hypergeometric characteristic function; section II.4 discusses large-order **unnormalized** moments and support-edge behavior. Those exact formulas and the model are prior results, not novel here. The new comparison is to a Gaussian matched to the **varying stationary variance**, at each even order, with a unique crossing in the tumble-exit rate and a nontrivial singular double scaling of order and rate including an explicit logarithmic correction.

Basu, Majumdar, Rosso, Sabhapandit and Schehr, arXiv:1910.10083, studied the earlier three-state harmonically confined particle with equal run and tumble transition rates and a stationary spatial shape transition. That special-rate subfamily does not establish the two-parameter crossing hierarchy. More recent work on kurtosis of inertial, memory-bearing active particles concerns a different position process. The known formulas in the cited papers imply the raw moments, but neither inspected primary paper presents the threshold uniqueness, Gaussian comparison across all even orders, or the two-term asymptotic boundary. Priority beyond the inspected literature remains subject to independent checking.

## Limitations

The result requires strictly positive fixed dimensionless run-exit rate \(R\); no uniformity is asserted for \(R\to0\), \(R\to\infty\), changing trap parameters during observation, or translational Brownian noise. Each crossing compares exact stationary even moments with a centered Gaussian of the same variance and does not imply tail dominance, convex ordering, or Gaussian convergence. The statement does not establish monotone ordering of thresholds across successive moment orders, nor a finite-sample estimation procedure. The exact moment recursion and full stationary law were previously published, and a non-indexed asymptotic comparison could be prior art.

## References

1. A. Sun, F. Ye and R. Podgornik, “Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time,” arXiv:2409.00578, first version September 1, 2024. https://arxiv.org/abs/2409.00578
2. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, “Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap,” arXiv:1910.10083, October 22, 2019. https://arxiv.org/abs/1910.10083
3. A. Sun, F. Ye and R. Podgornik, “Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap,” Physical Review E 111, 044136 (2025). https://doi.org/10.1103/PhysRevE.111.044136 (later journal version of reference 1).
