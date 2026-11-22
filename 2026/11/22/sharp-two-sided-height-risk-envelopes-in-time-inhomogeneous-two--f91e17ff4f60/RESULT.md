# Sharp two-sided height-risk envelopes in time-inhomogeneous two-predecessor trees

## Finding
Consider the rooted tree with vertices \(v_0,v_1,\ldots,v_n\), initially joined by \(v_0v_1\). Independently, for each \(i=2,\ldots,n\), attach \(v_i\) to \(v_{i-1}\) with probability \(p_i\in[0,1]\) or to \(v_{i-2}\) with probability \(1-p_i\). Let \(H_n\) be the maximum root distance. Write \(r=\lfloor n/2\rfloor\) and \(h=\lceil n/2\rceil\).

**Complete attainable-law classification.** For each integer \(n\ge2\), the set of all possible marginal distributions of \(H_n\), as the deterministic probability schedule varies, is exactly
\[
\boxed{\left\{\mathcal L\left(h+\sum_{j=1}^{r}Y_j\right):
  Y_j\text{ independent},\quad Y_j\sim\operatorname{Bernoulli}(t_j),\quad t_j\in[0,1]\right\}.}
\]
In particular every such height law has a probability-generating polynomial with only real nonpositive zeros. This is a statement about the **distribution**, not independence of the actual successive height increments.

**Sharp fixed-mean convex-order envelopes.** For any target \(\mu\in[h,n]\), consider only schedules satisfying \(\mathbb EH_n=\mu\). Put \(a=(\mu-h)/r\), \(k=\lfloor\mu\rfloor\), and \(\delta=\mu-k\). Then
\[
\boxed{k+\operatorname{Bernoulli}(\delta)
  \ \le_{\mathrm{cx}}\ H_n\ \le_{\mathrm{cx}}\
  h+\operatorname{Bin}(r,a).}
\]
Both bounds are attained by explicit independent-attachment schedules, simultaneously for **every** convex test function. Consequently, with the convention \(\delta(1-\delta)=0\) for integral \(\mu\), the exact attainable variance interval has endpoints
\[
\boxed{\delta(1-\delta)\ \le\ \operatorname{Var}(H_n)
  \ \le\ \frac{(\mu-h)(n-\mu)}r.}
\]
Every variance between these endpoints is attainable by a suitable deterministic schedule. For \(\mu\in(h,n)\), the upper variance inequality is strict unless the Bernoulli parameters of the height law are all equal; the lower inequality is an equality precisely when the height is supported on the two integers surrounding its mean (or is deterministic when the mean is integral).

Here \(U\le_{\mathrm{cx}}V\) means \(\mathbb E\phi(U)\le\mathbb E\phi(V)\) for every convex \(\phi:\mathbb R\to\mathbb R\), with equal means; all variables are bounded, so their expectations exist.

## Assumptions and scope
The horizon is an integer \(n\ge2\). Attachment probabilities \(p_i\) are deterministic and may vary arbitrarily with arrival time, including the endpoints zero and one; attachment choices are independent. Every vertex has unit edge distance from its parent. The root is \(v_0\), so the tree has \(n+1\) vertices. The classification concerns the one-dimensional height law, not the joint distribution of height with tree shape, leaf counts or diameter. All inequalities are exact finite-size statements; no asymptotic or adaptive-control claim is implied.

## Proof
**1. The newest vertex attains the height.** Let \(D_i\) be the distance from \(v_0\) to \(v_i\), so \(D_0=0,D_1=1\). Put \(X_i=D_i-D_{i-1}\), with \(X_1=1\). If the arrival at time \(i\) chooses \(v_{i-1}\), then \(X_i=1\); otherwise \(D_i=D_{i-2}+1\), so \(X_i=1-X_{i-1}\). Induction gives \(X_i\in\{0,1\}\) for every \(i\), and hence \(D_0\le D_1\le\cdots\le D_n\) and \(H_n=D_n\). Further, zeros cannot occur in two consecutive height increments, giving \(h\le H_n\le n\) almost surely.

**2. A tridiagonal determinant gives a Poisson-binomial height law.** Let \(F_i(z)=\mathbb E[z^{D_i}]\). Conditioning on the independent parent choice yields
\[
F_0(z)=1,\qquad F_1(z)=z,\qquad
F_i(z)=z\bigl[p_iF_{i-1}(z)+(1-p_i)F_{i-2}(z)\bigr].
\tag{1}
\]
Set \(R_i(s)=s^i F_i(1/s)\), where the polynomial identity is interpreted algebraically. Then \(R_0=R_1=1\) and
\[
R_i(s)=p_iR_{i-1}(s)+(1-p_i)sR_{i-2}(s).
\tag{2}
\]
First suppose every \(0<p_i<1\). Define the \(n\times n\) diagonal matrix \(D=\operatorname{diag}(1,p_2,\ldots,p_n)\) and the symmetric, zero-diagonal matrix \(E\) with \(E_{i-1,i}=E_{i,i-1}=\sqrt{1-p_i}\) for \(2\le i\le n\). Expanding the symmetric tridiagonal determinant by its last row and using (2) gives the exact polynomial identity
\[
R_n(-s)=\det(D-\sqrt{s}\,E).
\tag{3}
\]
The square root is merely a notational way to express a polynomial in \(s\), since each off-diagonal term occurs in a paired product. Put \(B=D^{-1/2}ED^{-1/2}\). This is a real symmetric weighted path adjacency matrix. The diagonal sign matrix with alternating entries conjugates \(B\) to \(-B\), so its eigenvalues occur in opposite pairs; as the path is connected with strictly positive edge weights, the symmetric tridiagonal matrix has simple eigenvalues, consisting of \(r\) distinct positive numbers \(\beta_1,\ldots,\beta_r\), their negatives, and a possible zero if \(n\) is odd. Therefore
\[
R_n(-s)=\biggl(\prod_{i=2}^np_i\biggr)
\prod_{j=1}^{r}(1-s\beta_j^2).
\]
As \(F_n(1)=R_n(1)=1\), normalization gives
\[
\boxed{F_n(z)=z^h\prod_{j=1}^{r}
  \frac{\beta_j^2+z}{1+\beta_j^2}.}
\tag{4}
\]
Each factor is the generating polynomial of a Bernoulli variable with success probability \(1/(1+\beta_j^2)\). Thus \(H_n\) has the claimed shifted independent-Bernoulli-sum representation when the probabilities are interior. At boundary schedules, approximate all probabilities by interior values; the probability polynomial coefficients are continuous. Since \([0,1]^r\) is compact and the product-form map is continuous, the class of shifted \(r\)-term Bernoulli sums is closed and includes every boundary limit. This proves **inclusion** in the claimed class.

**3. Every shifted Poisson-binomial law is attained.** For arbitrary \(t_1,\ldots,t_r\in[0,1]\), set \(p_{2j}=t_j\) for \(1\le j\le r\) and \(p_{2j+1}=1\) whenever \(2j+1\le n\). Every odd arrival after the first then increases depth by one, while the even increment \(X_{2j}\) equals the independent nearest-parent indicator at time \(2j\). Consequently
\[
H_n\stackrel d=h+\sum_{j=1}^{r}\operatorname{Bernoulli}(t_j)
\]
with independent summands. This establishes **surjectivity**, and hence the complete attainable-law classification, including degenerate endpoint schedules.

**4. The upper mean-constrained envelope.** For any Bernoulli representation from Steps 2–3, put \(t=\sum_jt_j=\mu-h\). Consider two parameters \(u,v\) replaced by their average \(m=(u+v)/2\). For any convex \(\phi\), conditioning on the other Bernoulli summands, the change in expected \(\phi\) is
\[
(m^2-uv)\bigl[\phi(b)+\phi(b+2)-2\phi(b+1)\bigr]\ge0,
\]
where \(b\) is the realized value of the other summands plus \(h\). Repeated pairwise averaging, or the usual majorization argument, yields
\[
\mathbb E\phi\left(h+\sum_{j=1}^rY_j\right)
\le\mathbb E\phi\bigl(h+\operatorname{Bin}(r,t/r)\bigr).
\]
This is the classical binomial convex-order inequality for a fixed-mean Poisson-binomial sum [3]; it is proved here in the form needed for the tree. Step 3 with every \(t_j=a\) realizes equality for all convex functions. The variance identity \(\sum_jt_j(1-t_j)\le r a(1-a)\) follows directly, with equality exactly when all \(t_j=a\).

**5. The lower envelope and its realization.** Let \(k=\lfloor\mu\rfloor\) and \(\delta=\mu-k\). For each convex function \(\phi\), its affine interpolation through \((k,\phi(k))\) and \((k+1,\phi(k+1))\) is no larger than \(\phi\) at every integer argument. Thus any integer-valued random variable of mean \(\mu\) satisfies
\[
\mathbb E\phi(H_n)\ge (1-\delta)\phi(k)+\delta\phi(k+1).
\]
To attain this law, use the schedule of Step 3 with exactly \(k-h\) of the \(t_j\)'s equal to one, the next equal to \(\delta\) if \(\delta>0\), and the remaining \(t_j\)'s zero. For integral \(\mu\), take exactly \(\mu-h\) ones and the rest zeros. All indices exist because \(h\le\mu\le h+r=n\). This realizes \(k+\operatorname{Bernoulli}(\delta)\) and proves sharpness of the lower convex-order and variance bounds. Finally, linearly interpolate the vectors \(t_1,\ldots,t_r\) of the explicit lower and upper schedules, keeping their common sum \(\mu-h\) fixed. The resulting variance is continuous along this interpolation; its endpoint values are the proven minimum and maximum, so the intermediate-value theorem attains every intermediate variance. Taken together, Steps 2–5 prove the theorem for all schedules and all admissible target means.

## Verification
The accompanying standalone `verify.py` requires only Python 3 standard libraries and runs with `python3 verify.py`. It enumerates all parent-choice histories for finite horizons and rational probability schedules, independently computes the probability-generating recursion, checks both convex-order inequalities by every integer stop-loss function \(\phi_b(x)=(x-b)_+\), verifies the variance bounds, and checks that even/odd control schedules attain every tested shifted Poisson-binomial law and both sharp endpoints. Its latest run returned `PASSED 67354 exact assertions`. Enumeration is finite and supplements but does not replace the arbitrary-size determinant and convexity proof.

## Relationship to prior work
Tang, Wang and Wu [1] define the corresponding homogeneous-parameter two-predecessor random tree and study one-endedness, trunk and branch structure, and collision behavior of independent random walks. Their inspected Sections 1–3 and stated results do not classify finite height laws under time-dependent attachment schedules or their fixed-mean stochastic-order optima. Prior work on fixed-parameter height fluctuations gives Gaussian limits and height/leaf dependence, but does not imply the exact time-inhomogeneous attainable family.

The real-rootedness of weighted path matching polynomials is an established special case of Heilmann–Lieb theory [2], and the fixed-mean convex-order maximality of binomial distributions among independent Bernoulli sums is the established Hoeffding result reviewed in [3]. Neither of these general tools is claimed as new. Dekking and Kong [4, Proposition 4.2] established negative-real-rooted generating polynomials for a *homogeneous* antipersistent two-state Markov occupation model, which is an important equivalent representation of fixed-parameter height increments. The new model-specific content is the exact **arbitrary time-inhomogeneous** height-law characterization, including converse realization of every Bernoulli-parameter vector by attachment choices, and the simultaneously attainable **two-sided** tree-height risk envelopes. The general tools apply only after identifying the special depth recurrence and proving that exact realization theorem.

## Limitations
The result is restricted to a two-predecessor attachment rule, independent exogenous probabilities and marginal finite-horizon height. It does not characterize adaptation to past random choices, longer parent memories, or joint height/shape dependencies. Convex-order bounds do not assert pointwise ordering of all tail probabilities. The proof determines the complete attainable family but not which distinct schedules generate the same member of that family. Novelty remains subject to independent historical review, including possible unindexed formulations of the height polynomial under matching-polynomial terminology. Independent scientific audit has not yet been performed.

## References
[1] J.-s. Tang, F. Wang, X.-Y. Wu, *Infinite collisions of simple random walks on random recursive trees generated by Bernoulli sequences*, arXiv:2607.02916, first publicly posted 2026-07-03. https://arxiv.org/abs/2607.02916

[2] D. G. Wagner, *Weighted enumeration of spanning subgraphs with degree constraints*, arXiv:0803.1659, 2008; see the discussion and extensions of Heilmann–Lieb matching-polynomial real-rootedness. https://arxiv.org/abs/0803.1659

[3] W. Tang and F. Tang, *The Poisson binomial distribution — Old & New*, arXiv:1908.10024, first posted 2019-08-27, especially Theorem 2.1 on fixed-mean convex order. https://arxiv.org/html/1908.10024v1

[4] M. Dekking and D. Kong, *Multimodality of the Markov binomial distribution*, arXiv:1102.3613, 2011, especially Proposition 4.2. https://arxiv.org/html/1102.3613v1
