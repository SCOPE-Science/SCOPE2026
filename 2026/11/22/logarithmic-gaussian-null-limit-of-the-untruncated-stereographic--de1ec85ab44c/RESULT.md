# Logarithmic Gaussian null limit of the untruncated stereographic statistic on the two-sphere

## Finding

Let \(X_1,X_2,\ldots\) be independent uniform points on the unit two-sphere \(\mathbb S^2\), and write \(\Theta_{ij}=\arccos(X_i\cdot X_j)\). Define the two centered stereographic channels
\[
C_n=\frac{2}{n}\sum_{i<j}\cot(\Theta_{ij}/2)-(n-1)\frac{\pi}{2},\qquad
A_n=\frac{2}{n}\sum_{i<j}\tan(\Theta_{ij}/2)-(n-1)\frac{\pi}{2}.
\]
Then, without truncating either singular kernel,
\[
\boxed{\frac{(C_n,A_n)}{\sqrt{\log n}}\ \Longrightarrow\ (2G_1,2G_2),}
\]
where \(G_1,G_2\) are independent standard normal variables. Consequently, for every fixed finite list of real parameters \(a_1,\ldots,a_s\), the statistic
\[
T_n(a)=\frac{2}{n}\sum_{i<j}\bigl\{\cot(\Theta_{ij}/2)+a\tan(\Theta_{ij}/2)\bigr\}-(n-1)\frac{(1+a)\pi}{2}
\]
satisfies
\[
\boxed{\frac{(T_n(a_1),\ldots,T_n(a_s))}{\sqrt{\log n}}\ \Longrightarrow\ 2(G_1+a_1G_2,\ldots,G_1+a_sG_2).}
\]
The limit covariance between parameters \(a,b\) is \(4(1+ab)\). The original stereographic test uses \(a\in[-1,1]\); the linear identity permits this joint statement for arbitrary fixed real parameters. **At each finite \(n\ge2\), every nontrivial scalar channel has infinite second moment**, so this limit covariance must not be described as a limit of finite-sample covariances.

## Assumptions and scope

All sampling is independent from normalized area measure on \(\mathbb S^2\). The dimension is exactly two, sample size \(n\to\infty\), and each indicated parameter is fixed (not sample-size-dependent). The pairwise angle lies strictly between zero and \(\pi\) almost surely. The logarithm is natural. The proof covers the raw, diagonal-free statistic; it does not establish alternative power, finite-sample critical values, rates of weak convergence, or a uniform result in growing parameter ranges.

## Proof

**1. Pair distribution and critical tails.** For two independent uniform directions, \(U=\cos\Theta\) is uniform on \((-1,1)\). Thus \(Z=\cot(\Theta/2)=\sqrt{(1+U)/(1-U)}\) has density
\[
f_Z(z)=\frac{2z}{(1+z^2)^2},\quad z>0,\qquad \Pr(Z>t)=\frac{1}{1+t^2},\qquad \mathbb EZ=\mathbb E Z^{-1}=\frac\pi2.
\]
For arbitrary fixed real \(b,c\), write \(W=bZ+c/Z\) and \(\mu=(b+c)\pi/2\). Direct integration at zero and infinity gives, for \(t\to\infty\),
\[
\Pr(|W|>t)=O_{b,c}(t^{-2}),\quad
\mathbb E[|W|\mathbf1_{\{|W|>t\}}]=O_{b,c}(t^{-1}),\quad
\mathbb E[W^2\mathbf1_{\{|W|\le t\}}]=2(b^2+c^2)\log t+O_{b,c}(1),\quad
\mathbb E[W^4\mathbf1_{\{|W|\le t\}}]=O_{b,c}(t^2).
\]
These estimates remain valid when either coefficient is zero or their signs differ. They follow from the density asymptotics \(f_Z(z)\sim2z\) at zero and \(f_Z(z)\sim2z^{-3}\) at infinity; the mixed product \(Z\cdot Z^{-1}=1\) cannot contribute a logarithmic second-moment term. For any fixed \(n\ge2\), a nonzero cotangent coefficient forces an infinite second moment by restricting all other sampled points to separated open caps and sending one pair angle to zero, where the squared summand contributes \(\int_0^\varepsilon r^{-2}r\,dr=\infty\). If the cotangent coefficient is zero but the tangent coefficient is nonzero, the same argument uses a nearly antipodal pair. Thus every nonzero linear combination of the two raw channels has infinite finite-sample variance.

**2. A rare-event truncation that does not modify the weak limit.** Fix \(M_n=n(\log n)^{1/4}\), and put \(h_n(x,y)=W(x,y)\mathbf1_{\{|W(x,y)|\le M_n\}}-\mu_n\), with \(\mu_n\) its mean under two independent uniform points. By rotation invariance, \(\mathbb E[h_n(x,X)]=0\) for every \(x\in\mathbb S^2\). Its second and fourth moments satisfy
\[
v_n=\mathbb Eh_n(X_1,X_2)^2=2(b^2+c^2)\log n+O_{b,c}(\log\log n+1),\qquad
r_n=\mathbb Eh_n(X_1,X_2)^4=O_{b,c}(M_n^2).
\]
Set \(U_n=\frac2n\sum_{i<j}h_n(X_i,X_j)\) and \(S_n=\frac2n\sum_{i<j}(W(X_i,X_j)-\mu)=bC_n+cA_n\). A union bound gives
\[
\Pr\{\exists i<j:|W(X_i,X_j)|>M_n\}\le O_{b,c}(n^2/M_n^2)=O_{b,c}((\log n)^{-1/2}).
\]
On its complement, \(S_n-U_n=-(n-1)\mathbb E[W\mathbf1_{\{|W|>M_n\}}]=O_{b,c}(n/M_n)=o(1)\). Therefore \(S_n-U_n\to0\) in probability. The original statistic may have infinite variance; the approximation only requires a high-probability equality up to a vanishing deterministic shift.

**3. Quadratic-variation concentration.** With \(\mathcal F_j=\sigma(X_1,\ldots,X_j)\), the increments \(D_{n,j}=\frac2n\sum_{i<j}h_n(X_i,X_j)\) form a martingale-difference array and sum to \(U_n\). Define
\[
g_n(x,y)=\int_{\mathbb S^2}h_n(x,z)h_n(y,z)\,d\sigma(z),
\]
where \(\sigma\) is uniform area measure. The predictable quadratic variation is
\[
Q_n=\sum_{j=2}^n\mathbb E[D_{n,j}^2\mid\mathcal F_{j-1}]
=\frac{2(n-1)}{n}v_n+\frac8{n^2}\sum_{1\le i<k\le n-1}(n-k)g_n(X_i,X_k).
\]
The kernel \(g_n\) is centered in either argument, so two distinct unordered pairs in this last sum are uncorrelated, including pairs sharing one endpoint. Let \(H_n\) denote the self-adjoint integral operator with kernel \(h_n\). By the row-integral (Schur) bound and rotation invariance,
\[
\|H_n\|_{\mathrm{op}}\le\sup_x\int|h_n(x,z)|\,d\sigma(z)\le 2\mathbb E|W|<\infty.
\]
As \(H_n\) is Hilbert--Schmidt, \(g_n\) is the integral kernel of \(H_n^2\), and
\[
\mathbb E[g_n(X_1,X_2)^2]=\operatorname{tr}(H_n^4)
\le\|H_n\|_{\mathrm{op}}^2\operatorname{tr}(H_n^2)=O_{b,c}(v_n)=O_{b,c}(\log n).
\]
The sum of squared deterministic coefficients \(\bigl(8(n-k)/n^2\bigr)^2\), over \(i<k\le n-1\), is uniformly bounded. Hence the off-diagonal part of \(Q_n\) has variance \(O_{b,c}(\log n)\), and
\[
\frac{Q_n}{\log n}\longrightarrow 4(b^2+c^2)\quad\text{in probability}.
\]

**4. Martingale Lindeberg condition.** Conditional on \(X_j\), the random variables \(h_n(X_i,X_j)\) for \(i<j\) are independent, centered and have moments \(v_n,r_n\). Expanding their fourth power yields
\[
\mathbb ED_{n,j}^4=\frac{16}{n^4}\bigl((j-1)r_n+3(j-1)(j-2)v_n^2\bigr),
\]
and hence
\[
\sum_{j=2}^n\mathbb ED_{n,j}^4
=O_{b,c}(r_n/n^2+v_n^2/n)
=O_{b,c}((\log n)^{1/2}+(\log n)^2/n)=o((\log n)^2).
\]
For every \(\varepsilon>0\), Markov's inequality applied to these fourth moments makes the Lindeberg sum of \(D_{n,j}/\sqrt{\log n}\) vanish. The martingale central limit theorem now gives
\[
U_n/\sqrt{\log n}\Longrightarrow N(0,4(b^2+c^2)).
\]
The truncation comparison transfers this result to \(bC_n+cA_n\). Cramér--Wold with arbitrary \((b,c)\) gives joint independent normal coordinates of variance four; continuous linear mapping yields the entire finite-parameter claim.

## Verification

The accompanying standalone \(\texttt{CHECK.py}\) verifies 31 independent analytic/numerical assertions for the exact spherical pair law, clipped first and second moments, logarithmic increments for five coefficient pairs, fourth moments, and the combinatorial quadratic-variation multiplier. Run \(\texttt{python CHECK.py}\) with Python 3; no third-party packages are needed. These checks support the stated constants but the proof of the infinite-sample limit is the martingale argument above, not numerical sampling.

## Relationship to prior work

Fernández-de-Marcos and García-Portugués (2024, first public preprint 2024-05-22) define precisely the same \(T_n(a)\). Their Theorem 1 gives a weighted chi-square limit when the sphere dimension \(q\ge3\); Section 4 expressly says its square-integrable-kernel argument does **not** apply at \(q=2\), and supplies instead a fixed-frequency Gegenbauer-truncated limit. The present theorem addresses the untruncated two-sphere statistic, with a divergent logarithmic normalization and Gaussian rather than fixed-truncation chi-square law. Earlier Sobolev and projection tests use different kernel constructions and do not imply the claimed heavy-tail two-channel limit. Neither the stereographic statistic, the general martingale CLT, nor classical Sobolev methods are claimed as new.

## Limitations

The limit is a null weak convergence statement for iid uniform samples from \(\mathbb S^2\); it is not a finite-sample variance identity, as the raw statistic has infinite second moment. The bound \(\operatorname{tr}(H_n^4)\le\|H_n\|_{\mathrm{op}}^2\operatorname{tr}(H_n^2)\) is specific to the bounded row integral of this truncated rotationally invariant kernel; it is not a general theorem for arbitrary non-square-integrable degenerate kernels. The result does not establish power under nonuniform distributions, fixed-\(n\) calibration accuracy, or the behavior at dimension one. Historical-priority uncertainty persists for nonstandard infinite-variance U-statistic literature.

## References

1. A. Fernández-de-Marcos and E. García-Portugués, *A stereographic test of spherical uniformity*, arXiv:2405.13531, first posted 2024-05-22, https://arxiv.org/abs/2405.13531 ; *Statistics & Probability Letters* 215 (2024), article 110218.
2. E. García-Portugués, P. Navarro-Esteban, and J. A. Cuesta-Albertos, *On a projection-based class of uniformity tests on the hypersphere*, arXiv:2008.09897 (2020), https://arxiv.org/abs/2008.09897.
3. S. R. Jammalamadaka, S. Meintanis, and T. Verdebout, *On Sobolev tests of uniformity on the circle with an extension to the sphere*, *Bernoulli* 26 (2020), 2226–2252, https://doi.org/10.3150/19-BEJ1191.
4. Classical martingale central limit theorem (triangular-array form with convergence in probability of predictable quadratic variation and a martingale Lindeberg condition).
