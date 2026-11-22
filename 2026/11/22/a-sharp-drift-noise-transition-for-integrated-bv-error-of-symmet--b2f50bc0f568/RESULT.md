# A sharp drift–noise transition for integrated BV error of symmetric Bernstein–Stancu sampling

## Finding

For every integer \(n\ge1\) and \(b\ge0\), set \(\beta_n=b\sqrt n\), \(\alpha_n=\beta_n/2\) and define the positive polynomial sampling operator
\[
(T_{n,b}f)(x)=\sum_{k=0}^n\binom nk x^k(1-x)^{n-k} f\!\left(\frac{k+\beta_n/2}{n+\beta_n}\right),\quad 0\le x\le1.
\]
On the canonical real BV class specified below, its sharp integrated approximation-error coefficient is
\[
C_n(b)=\sup_{|Df|(0,1)>0}\frac{\|T_{n,b}f-f\|_{L^1(0,1)}}{|Df|(0,1)}.
\]
Write \(s_{n,j}=(j+\beta_n/2)/(n+\beta_n)\) for \(0\le j\le n\); let \(U_{n,0}=0\), \(U_{n,n+1}=1\) deterministically, and for \(1\le j\le n\) let \(U_{n,j}\) have the \(\operatorname{Beta}(j,n-j+1)\) distribution. Then the exact finite-degree formula is
\[
\boxed{C_n(b)=\max_{0\le j\le n}\max\big\{\mathbb E|U_{n,j}-s_{n,j}|,\ \mathbb E|U_{n,j+1}-s_{n,j}|\big\}.}
\]
The critical inward-knot displacement scale is \(\beta_n\asymp\sqrt n\). Precisely,
\[
\boxed{\lim_{n\to\infty}\sqrt n\,C_n(b)=\frac12\max\left\{\sqrt{\frac2\pi},b\right\}.}
\]
Thus the limiting sharp constant changes branches at \(b_*=\sqrt{2/\pi}\). For \(0\le b<b_*\), every asymptotically norming single-jump location converges to \(1/2\); for \(b>b_*\), its distance to \(\{0,1\}\) tends to zero. At \(b=b_*\), any subsequential limiting norming location belongs to \(\{0,1/2,1\}\). These claims include the possibility of nonattained finite-degree suprema; no finite-degree equality classification is asserted.

## Assumptions and scope

Real functions have finite distributional variation on \((0,1)\), are represented by their right-continuous representative at each interior point, and have endpoint values equal to the corresponding one-sided traces. This prevents unpenalized isolated modifications at sampled nodes. Constants are factored out by the variation seminorm \(V(f)=|Df|(0,1)\); all output errors are measured using unweighted Lebesgue \(L^1(0,1)\). The parameters satisfy \(b\ge0\), so \(0\le\alpha_n\le\beta_n\), and the sampled nodes lie in \([0,1]\). The theorem concerns classical binomial Bernstein–Stancu sampling, not integral Durrmeyer variants or nonsymmetric parameter sequences.

An asymptotically norming sequence of jumps means \(s_n\in(0,1)\) with \(\sqrt n\,\|T_{n,b}\mathbf1_{[s_n,1]}-\mathbf1_{[s_n,1]}\|_{L^1}\to\tfrac12\max\{\sqrt{2/\pi},b\}\). A jump exactly at a sampling node is evaluated according to the stated right-continuous convention; one-sided limits of jump locations may also determine the supremum.

## Proof

**1. Reduction to step functions.** Let \(h_s=\mathbf1_{[s,1]}\) for \(0<s<1\). Every admissible \(f\) has the signed-derivative representation \(f(x)=c+\int_{(0,1)}h_s(x)\,d(Df)(s)\), with the prescribed representatives. Since \(T_{n,b}\mathbf1=\mathbf1\), linearity, Fubini and the triangle inequality yield
\[
\|T_{n,b}f-f\|_1\le \int_{(0,1)}\|T_{n,b}h_s-h_s\|_1\,d|Df|(s)
\le \big(\sup_{0<s<1}E_n(s)\big)|Df|(0,1),
\]
where \(E_n(s)=\|T_{n,b}h_s-h_s\|_1\). A single step has \(|Dh_s|(0,1)=1\), giving equality of the operator norm and \(\sup_s E_n(s)\).

**2. Exact Beta formula.** For \(s\) strictly between two successive nodes, let \(k\) be the smallest sampling index with \(s_{n,k}\ge s\), allowing \(k=0\) or \(n+1\). The binomial-tail identity
\[
(T_{n,b}h_s)(x)=\mathbb P\{\operatorname{Bin}(n,x)\ge k\}=\mathbb P\{U_{n,k}\le x\}
\]
holds for \(1\le k\le n\), and almost everywhere at the two extremes with the above point masses. Consequently, by Tonelli,
\[
E_n(s)=\int_0^s\mathbb P(U_{n,k}\le x)\,dx+\int_s^1\mathbb P(U_{n,k}>x)\,dx
=\mathbb E|U_{n,k}-s|.
\]
For fixed \(k\), \(s\mapsto\mathbb E|U_{n,k}-s|\) is convex. Its supremum on each interval between consecutive sampling nodes is at an interval endpoint. Accounting for both one-sided values of every threshold gives exactly the displayed finite maximum. For implementation, if \(1\le k\le n\), writing \(m=k/(n+1)\) and \(I_s(a,c)\) for the regularized incomplete Beta function,
\[
\mathbb E|U_{n,k}-s|=m-s+2\big[sI_s(k,n-k+1)-mI_s(k+1,n-k+1)\big].
\]
The two point masses have absolute deviations \(s\) and \(1-s\).

**3. Scaling limit of every candidate sequence.** Suppose \(j_n/n\to u\in[0,1]\). For each \(\delta\in\{0,1\}\), the order-statistic Beta law \(U_{n,j_n+\delta}\) obeys
\[
\sqrt n\left(U_{n,j_n+\delta}-\frac{j_n+\delta}{n+1}\right)\ \Rightarrow\ \sqrt{u(1-u)}Z,
\]
where \(Z\) is standard normal; for \(u=0,1\) the right side is the point mass at zero, as follows from the exact variance. Also
\[
\sqrt n\left(\frac{j_n+\delta}{n+1}-s_{n,j_n}\right)\longrightarrow b(u-\tfrac12).
\]
The exact Beta variance is at most \(1/[4(n+2)]\), hence the scaled absolute deviations are uniformly integrable. Therefore
\[
\sqrt n\,\mathbb E|U_{n,j_n+\delta}-s_{n,j_n}|\longrightarrow
F_b(u):=\mathbb E\left|\sqrt{u(1-u)}Z+b(u-\tfrac12)\right|.
\]
The formula remains valid at \(j_n=0\) and \(j_n=n\), using the deterministic end laws. Compactness and the finite maximum show that \(\sqrt n C_n(b)\to\max_{0\le u\le1}F_b(u)\): every maximizing index has a convergent subsequence, while any fixed \(u\) is approximated by indices \(j_n\sim nu\).

**4. Sharp Gaussian competition and location rigidity.** Put \(c=\sqrt{2/\pi}\) and \(t=|2u-1|\). Symmetry gives
\[
F_b(u)=\tfrac12G_b(t),\qquad G_b(t)=\mathbb E|\sqrt{1-t^2}Z+bt|.
\]
For \(b=0\), \(G_b(t)=c\sqrt{1-t^2}\) is strictly decreasing. If \(b>0\), let \(a=bt/\sqrt{1-t^2}\), \(\phi\) and \(\Phi\) denote standard normal density and CDF, and set
\[
R(a)=\frac{2\Phi(a)-1}{2a\phi(a)}=\int_0^1\exp\!\left(\frac{a^2(1-v^2)}2\right)dv.
\]
The function \(R\) increases strictly from one to infinity. Direct differentiation of the normal absolute moment gives
\[
G_b'(t)=\frac{2a\phi(a)}b\big[b^2R(a)-1\big]\quad(0<t<1).
\]
If \(b\ge1\), \(G_b\) increases strictly. If \(0<b<1\), its derivative changes exactly once, from negative to positive, so its unique interior stationary point is a *minimum*. Thus, for all \(b\ge0\), its only possible global maximizers are the endpoints \(t=0,1\), with \(G_b(0)=c\) and \(G_b(1)=b\). If \(b=c<1\), both endpoints maximize and every interior \(t\) is strictly suboptimal. This proves the sharp limit and all three localization regimes. For non-nodal jump sequences, the containing cell endpoint differs by at most \(1/(n+\beta_n)\), so the same compactness argument applies.

## Verification

The accompanying `check.py` compares the exact Beta-moment expression against independent numerical integration of binomial step-response tails over several degrees, parameters, and sampling indices. It also checks representative finite-degree normalized constants against the predicted limiting branches. Run `python check.py` with Python, NumPy and SciPy. These checks test formulas and normalization but do not establish the universal limit; Steps 1–4 above supply the proof.

## Relationship to prior work

Üster and İbikli (2015), in a paper dated May 15, 2015, study precisely the classical Stancu sampling nodes and give pointwise estimates for bounded-variation inputs; their Theorem 1.1 is not the exact integrated \(BV\to L^1\) operator norm, and does not address parameters of order \(\sqrt n\) or a sharp displacement/noise threshold. Gandhi and Mishra (2017) study parameter sensitivity, nodes and uniform approximation on continuous inputs, without the stated sharp BV norm or transition. Dong and Yu (2017) study a Durrmeyer-type *integral* variant and direct/converse approximation estimates, so its operator and norm differ. The classical Bernstein case \(b=0\) is a benchmark, not claimed as a newly introduced operator. The claimed contribution is the joint all-degree Beta finite formula, critical-scale sharp norm and complete limiting location transition for the symmetric parameter family, not the earlier definition or standard central limit theorem.

## Limitations

Only real canonical BV inputs and the symmetric Stancu family \(\alpha_n=\beta_n/2\) with \(\beta_n=b\sqrt n\) are classified. The result does not specify which finite-degree index attains the maximum, whether a finite-degree step norm is attained under a particular trace convention, or the finer finite-size crossover width near \(b_*\). An earlier unpublished or unindexed equivalent sharp result cannot be ruled out by a database search.

## References

1. R. Üster and E. İbikli, *On the rate of convergence of the Stancu type Bernstein operators for functions of bounded variation*, Mathematical Sciences and Applications E-Notes **3** (2015), 126–136, May 15, 2015. DOI: https://doi.org/10.36753/mathenot.421231. Full text: https://dergipark.org.tr/en/download/article-file/468245.
2. R. B. Gandhi and V. N. Mishra, *Study of sensitivity of parameters of Bernstein-Stancu operators*, arXiv:1707.07424 (first version July 24, 2017), https://arxiv.org/abs/1707.07424.
3. L. Dong and D. Yu, *Pointwise approximation by a Durrmeyer variant of Bernstein-Stancu operators*, Journal of Inequalities and Applications **2017**, article 28, January 27, 2017, https://doi.org/10.1186/s13660-016-1291-x.
4. D. D. Stancu, *Approximation of functions by means of a new generalized Bernstein operator*, Calcolo **20** (1983), 211–229 (historical definition; not inspected in full).
