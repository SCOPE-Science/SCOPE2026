# A sharp one-half sample-reuse threshold for stochastic extragradient on bilinear games

## Finding

Consider the scalar bilinear saddle-point problem \(\min_x\max_y\mu xy\) with \(\mu\ne0\). In the equal-step stochastic extragradient method, let the coefficients \((A_k,B_k)\) used in the probing and correction evaluations have the same scalar marginal \(S\), and let the pairs be independent and identically distributed across iterations. Write \(m_2=\mathbb E S^2>0\), \(c=\mathbb E[A_kB_k]\), and \(d=\mathbb E[A_k^2B_k^2]\). For every fixed \(\eta>0\), every deterministic \(z_0\in\mathbb R^2\), and every integer \(n\ge0\),

\[
\mathbb E\|z_n\|^2=\bigl(1+\eta^2(m_2-2c)+\eta^4d\bigr)^n\|z_0\|^2.
\]

For nonzero \(z_0\), mean-square convergence to the unique saddle is possible at some positive constant step size **if and only if** \(2c>m_2\). In that case it occurs precisely for \(0<\eta^2<(2c-m_2)/d\). At equality in the step-size bound the expected squared norm is constant; at larger step sizes or when \(2c\le m_2\), it diverges geometrically.

Suppose more specifically that with probability \(\rho\in[0,1]\), the correction call reuses the probing coefficient, while otherwise it draws an independent coefficient. Let \(m_4=\mathbb E S^4<\infty\), and write \(\mu=\mathbb E S\ne0\). Then

\[
\mathbb E\|z_n\|^2=R_\rho(\eta)^n\|z_0\|^2,\qquad
R_\rho(\eta)=1-a_\rho\eta^2+b_\rho\eta^4,
\]
\[
a_\rho=(2\rho-1)m_2+2(1-\rho)\mu^2,\qquad
b_\rho=\rho m_4+(1-\rho)m_2^2>0.
\]

The existence of a positive mean-square-stable constant step size holds for **every** such nondegenerate scalar oracle distribution exactly when \(\rho\ge\tfrac12\). The threshold is sharp: for **each** \(0\le\rho<\tfrac12\), there exists a strictly positive two-point coefficient law of nonzero mean and finite moments for which no positive constant step size is mean-square stable. More precisely, for a fixed law with \(m_2>\mu^2\), stability is possible exactly when

\[
\rho>\rho_{\mathrm c}:=\frac{m_2-2\mu^2}{2(m_2-\mu^2)}
\]

(with the understanding that a negative critical value makes every admissible reuse fraction stable; equality is not stable), and then exactly for \(0<\eta^2<a_\rho/b_\rho\). If \(m_2=\mu^2\), the coefficient is deterministic and all reuse fractions have the usual positive stable step interval.

## Assumptions and scope

Set \(z=(x,y)^\mathsf T\), \(J=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\) and \(F_s(z)=sJz\). The expected operator is \(F(z)=\mu Jz\), hence its only zero is \(z_\star=0\) when \(\mu\ne0\). The oracle pair \((A_k,B_k)\) may be arbitrarily dependent within each iteration, but both components have the distribution of a real random variable \(S\) with \(\mathbb E|S|^4<\infty\). The pairs are iid over iterations and independent of the deterministic initial vector. The equal-step update is

\[
\widehat z_k=z_k-\eta F_{A_k}(z_k),\qquad z_{k+1}=z_k-\eta F_{B_k}(\widehat z_k).
\]

The special partial-reuse coupling is defined by an iid Bernoulli choice each iteration: with probability \(\rho\), draw \(S\) and take \(A=B=S\); with probability \(1-\rho\), draw \(A,B\) independently from \(S\). Reuse is independent between iterations. The universal assertion concerns *existence* of a law-dependent positive constant step size, not a single step size working for all laws.

## Proof

Because \(J^2=-I\), the exact update is
\[
z_{k+1}=\bigl[(1-\eta^2 A_kB_k)I-\eta B_kJ\bigr]z_k.
\]

For any real \(u,v\) and vector \(z\), skew symmetry and orthogonality give \(\|(uI+vJ)z\|^2=(u^2+v^2)\|z\|^2\). Hence the squared-norm multiplier is exactly \(1-2\eta^2 A_kB_k+\eta^4A_k^2B_k^2+\eta^2B_k^2\). Conditioning on the past and using independence of successive coefficient pairs proves the first identity by induction, with \(R=1+\eta^2(m_2-2c)+\eta^4d\).

If \(2c>m_2\), then \(c>0\), so \(d=\mathbb E[A^2B^2]\ge c^2>0\). Therefore \(R<1\) holds precisely when \(0<\eta^2<(2c-m_2)/d\). If \(2c\le m_2\), the same formula gives \(R\ge1\), and in fact \(R>1\) for every positive step: when \(2c<m_2\) the quadratic term is strictly positive, whereas if \(2c=m_2>0\) then \(d\ge c^2>0\). This proves the necessary-and-sufficient stability criterion and all boundary cases.

For partial reuse, linearity of expectation gives
\[
\mathbb E[AB]=\rho m_2+(1-\rho)\mu^2,
\qquad\mathbb E[A^2B^2]=\rho m_4+(1-\rho)m_2^2.
\]

Substitution gives \(a_\rho,b_\rho\) above. At \(\rho\ge1/2\), since \(m_2\ge\mu^2\),
\[
a_\rho=\mu^2+(2\rho-1)(m_2-\mu^2)\ge\mu^2>0.
\]
Thus every finite-fourth-moment law admits a nonempty stable step-size interval. For \(\rho<1/2\), first take the nonnegative two-point law \(\Pr\{S=0\}=1-q\), \(\Pr\{S=q^{-1}\}=q\), with \(0<q<1\). Here \(\mu=1\), \(m_2=q^{-1}\), and
\[
a_\rho=(2\rho-1)q^{-1}+2(1-\rho)<0
\]
whenever \(q<(1-2\rho)/[2(1-\rho)]\). To make the coefficients *strictly positive* while preserving mean one, replace zero by \(\delta>0\) and \(q^{-1}\) by \([1-(1-q)\delta]/q>0\). For fixed \(q\) satisfying the strict inequality, sufficiently small \(\delta\) preserves \(a_\rho<0\) by continuity. Thus no positive step can contract the second moment for that strictly positive two-point law. This proves sharpness even without zero-valued oracle calls.

If \(m_2>\mu^2\), rearranging \(a_\rho>0\) yields precisely the displayed \(\rho_{\mathrm c}\) boundary; if \(m_2=\mu^2\), equality in Cauchy–Schwarz forces \(S=\mu\) almost surely, so \(a_\rho=m_2>0\) and \(b_\rho=m_2^2\) for every \(\rho\). This concludes the proof.

As an explicit mean-versus-second-moment separation, take \(\Pr\{S=0\}=3/4\), \(\Pr\{S=4\}=1/4\), independent probing/correction samples, and \(\eta=1/10\). Then \(\mu=1\), \(m_2=4\), and
\[
\mathbb E\|z_n\|^2=(1277/1250)^n\|z_0\|^2,
\quad \|\mathbb E z_n\|^2=(9901/10000)^n\|z_0\|^2.
\]
Thus the expected iterate converges while its second moment diverges. With the same law and half reuse, \(R_{1/2}(1/10)=497/500<1\).

## Verification

Run the standard-library checker with `python3 verify.py`. It conducts 86 independent exact-rational comparisons, including different bounded coefficient laws, reusing fractions, exact one-step and multi-step moments, the explicit mean/mean-square separation, and strictly positive rare-coefficient witnesses close to the half-reuse threshold. These finite computations check identities and examples only; the distribution-free statement and strict endpoint follow from the foregoing algebra and continuity argument.

## Relationship to prior work

Chavdarova et al. (2019, Section 2.2, Theorem 1 and Appendix C.1) prove that independently sampled extragradient may diverge on a bilinear game, including a finite-sum example with a batch-overlap parameter. Mishchenko et al. (2019, Section 2) motivate same-sample extragradient and analyze its convergence. Li et al. (2021/2022, Section 2 and Appendix A) work with the same sample in bilinear games, while Gorbunov et al. (2021/2022, Sections 1–4) provide broader same-sample and independent-sample convergence frameworks. Yoon and Loizou (2026, Sections 1–4) exhibit additional differences between these endpoint schemes. None of the inspected relevant sections establishes a distribution-free **half-reuse** necessity-and-sufficiency threshold over arbitrary finite-fourth-moment scalar oracle laws.

A related exact result for *uniformly weighted positive two-point* bilinear coefficients analyzes all within-iteration couplings. That restricted family necessarily has \(m_2<2\mu^2\), and consequently its independently sampled method always admits sufficiently small stable steps. It therefore does not imply the rare-coefficient obstruction or the universal one-half threshold here. Other general theorems about stochastic matrix products may give an alternate derivation; a broad noncoverage claim is not made.

## Limitations

The result is for equal extrapolation/correction step sizes, an unconstrained two-dimensional scalar bilinear game, iid iteration-level oracle pairs, and finite fourth moments. It is a *mean-square* statement about last iterates, not an equivalence with almost-sure convergence, performance of averaged iterates, or convergence on general noncommuting matrix-valued and nonlinear games. A universal *positive* stepsize independent of the oracle distribution does not follow. The explicit mean-versus-variance example allows zero coefficients; the proof of sharp universal necessity uses strictly positive coefficients. Publication precedence under other terms for correlated stochastic oracles remains a risk.

## References

1. Chavdarova, Gidel, Fleuret, Lacoste-Julien, "Reducing Noise in GAN Training with Variance Reduced Extragradient," initial arXiv release 2019-04-18, https://arxiv.org/abs/1904.08598.
2. Mishchenko, Kovalev, Shulgin, Richtárik, Malitsky, "Revisiting Stochastic Extragradient," initial arXiv release 2019-05-27, https://arxiv.org/abs/1905.11373.
3. Li et al., "On the Convergence of Stochastic Extragradient for Bilinear Games using Restarted Iteration Averaging," https://proceedings.mlr.press/v151/junchi-li22a/junchi-li22a.pdf.
4. Gorbunov, Berard, Gidel, Loizou, "Stochastic Extragradient: General Analysis and Improved Rates," initial arXiv release 2021-11-16, https://arxiv.org/abs/2111.08611.
5. Yoon and Loizou, "On Same-Sample and Independent-Sample Stochastic Extragradient for Monotone Variational Inequalities," https://arxiv.org/abs/2608.06182.
