# Exact beta contraction of Gaussian error by Haar sketching in scalar least squares

## Finding

For every ambient dimension \(n\ge3\), sketch dimension \(1\le\ell<n\), and field \(\mathbb K\in\{\mathbb R,\mathbb C\}\), consider ordinary one-column sketch-and-solve applied to any deterministic inconsistent least-squares problem \(y=u x_\star+r_0\), with \(u,r_0\in\mathbb K^n\), \(u\ne0\), \(r_0\ne0\), and \(u^*r_0=0\). Let \(R_{\mathrm H}\) and \(R_{\mathrm G}\) denote normalized *excess unsketched squared residuals* when the sketch is respectively a Haar-orthonormal \(n\times\ell\) frame and an independent standard Gaussian \(n\times\ell\) matrix:

\[
R=\frac{\|y-u\widehat x\|_2^2}{\|r_0\|_2^2}-1
 =\frac{\|u\|_2^2|\widehat x-x_\star|^2}{\|r_0\|_2^2},\qquad
\widehat x=(\Omega^*u)^\dagger\Omega^*y.
\]

Set \(\delta=1/2\) over \(\mathbb R\) and \(\delta=1\) over \(\mathbb C\); write \(a=\delta\ell\), \(b=\delta(n-\ell)\), and \(c=\delta(\ell-1)\). Then there is an **independent** coupling

\[
\boxed{R_{\mathrm G}\stackrel d=Z/W,\quad
R_{\mathrm H}\stackrel d=B\,(Z/W),}
\]

where \(Z\sim\operatorname{Gamma}(\delta,1)\), \(W\sim\operatorname{Gamma}(a,1)\), and, for \(\ell>1\), \(B\sim\operatorname{Beta}(b,c)\) are mutually independent. For \(\ell=1\), interpret \(B=1\) deterministically. Thus for \(2\le\ell<n\), \(R_{\mathrm H}\) is strictly smaller than \(R_{\mathrm G}\) in usual first-order stochastic order: for each \(t>0\),

\[
\Pr(R_{\mathrm H}>t)<\Pr(R_{\mathrm G}>t).
\]

For every real \(q>0\), the Haar excess-error moment is finite **if and only if** \(q<a\). In that range,

\[
\boxed{\mathbb E R_{\mathrm H}^{q}=
\frac{\Gamma(\delta+q)\Gamma(a-q)}{\Gamma(\delta)\Gamma(a)}
\frac{\Gamma(b+q)\Gamma(b+c)}{\Gamma(b)\Gamma(b+c+q)}.}
\]

The Gaussian moment omits the second fraction. At the sharp tail scale,

\[
\boxed{\lim_{t\to\infty}t^a\Pr(R_{\mathrm H}>t)
=\frac{\Gamma(a+\delta)}{\Gamma(\delta)\Gamma(a+1)}
\frac{\Gamma(b+a)\Gamma(b+c)}{\Gamma(b)\Gamma(b+c+a)}.}
\]

These formulas also hold for \(\ell=1\) with the beta multiplier and its moment factor interpreted as one. In particular, the real Haar-sketch excess error has a finite mean but infinite variance at \(\ell=3\) or \(\ell=4\); for complex sketches the corresponding finite-mean/infinite-variance boundary is \(\ell=2\). The assertion concerns variance of the nonnegative excess squared residual \(R\), rather than the variance of the signed regression coefficient.

## Assumptions and scope

Sketch matrices are drawn independently of the fixed input data; the Gaussian entries are independent standard real normals or standard circular complex normals, as appropriate. A Haar frame means Haar-uniform on the real or complex Stiefel manifold, with \(\Omega^*\Omega=I_\ell\). The conventional overall scaling of a Gaussian sketch cancels in the least-squares coefficient. Almost surely \(\Omega^*u\ne0\), so the pseudoinverse is unambiguous. The result assumes exact arithmetic, a **single** covariate column and a **single** response, with a nonzero deterministic orthogonal residual.

## Proof

**1. Reduce to two coordinates.** Unitary or orthogonal invariance permits \(u/\|u\|_2=e_1\), \(r_0/\|r_0\|_2=e_2\). The normalized excess error is the squared modulus of \((\Omega^*e_1)^\dagger(\Omega^*e_2)\). For Haar frames \(Q\), write \(P=QQ^*\). Because \(P=P^*=P^2\),

\[
R_{\mathrm H}=\frac{|P_{12}|^2}{P_{11}^2},\qquad
\sum_{j=2}^n|P_{j1}|^2=P_{11}(1-P_{11}).
\]

The first-column rotational invariance of the random projector, with rotations fixing \(e_1\), implies that conditional on \(U=P_{11}\), the vector \((P_{21},\ldots,P_{n1})/\sqrt{U(1-U)}\) is uniform on the unit sphere of \(\mathbb K^{n-1}\). Thus the squared modulus of its first coordinate, \(V\), is \(\operatorname{Beta}(\delta,\delta(n-2))\), independent of \(U\), and

\[
R_{\mathrm H}=\frac{1-U}{U}V.
\]

Moreover, \(U=\|Q^*e_1\|_2^2\sim\operatorname{Beta}(a,b)\); the standard Gaussian-sphere construction gives this distribution for both fields. This establishes all independence assertions in the geometric representation without assuming a product law for arbitrary projector entries.

**2. Identify the independent multiplier.** Let \(W\sim\operatorname{Gamma}(a,1)\), \(T\sim\operatorname{Gamma}(b,1)\), and \(V\sim\operatorname{Beta}(\delta,\delta(n-2))\) be independent. Then \(U=W/(W+T)\) has the law above and \(R_{\mathrm H}\stackrel d=(T/W)V\). If \(\ell>1\), append an independent \(H\sim\operatorname{Gamma}(c,1)\), define \(S=T+H\) and \(B=T/S\). Classical beta–gamma factorization gives \(B\sim\operatorname{Beta}(b,c)\), independent of \(S\sim\operatorname{Gamma}(b+c,1)\). Since \(b+c=\delta(n-1)\), the beta–gamma product \(SV\) has distribution \(\operatorname{Gamma}(\delta,1)\), independently of \(B,W\). Therefore \((T/W)V=B(SV)/W\) proves the claimed independent product. For \(\ell=1\), \(c=0\), \(T\) alone has gamma shape \(\delta(n-1)\), and the same argument gives \(B=1\).

**3. Identify the Gaussian law and strict order.** For a Gaussian sketch \(G\), \(G^*e_1\) and \(G^*e_2\) are independent standard Gaussian \(\ell\)-vectors. Conditional on \(G^*e_1\), the normalized inner product with \(G^*e_2\) is standard real or complex Gaussian, with squared modulus gamma-distributed at shape \(\delta\), independent of the squared length of \(G^*e_1\), which is gamma-distributed at shape \(a\) after a common cancellation of scale. This proves \(R_{\mathrm G}\stackrel d=Z/W\). When \(c>0\), \(0<B<1\) almost surely, and the beta-prime variable \(Z/W\) has a strictly positive density for all positive arguments, proving strict stochastic dominance at every positive threshold. For \(c=0\), the two laws coincide.

**4. Positive moments and extreme tails.** Independent gamma moments yield \(\mathbb E Z^q=\Gamma(\delta+q)/\Gamma(\delta)\), \(\mathbb E W^{-q}=\Gamma(a-q)/\Gamma(a)\) exactly when \(q<a\), and \(\mathbb E B^q=\Gamma(b+q)\Gamma(b+c)/[\Gamma(b)\Gamma(b+c+q)]\). Since \(B>0\) almost surely, \(\mathbb E R_{\mathrm H}^q=\infty\) when \(q\ge a\), not merely an inconclusive infinite-factor expression. The beta-prime density of \(Z/W\) is

\[
f_{\mathrm G}(s)=\frac{s^{\delta-1}}{\operatorname B(\delta,a)(1+s)^{a+\delta}},\qquad s>0,
\]

which has survival asymptotic \(\Pr(R_{\mathrm G}>t)\sim \Gamma(a+\delta)t^{-a}/[\Gamma(\delta)\Gamma(a+1)]\). Conditioning on \(0<B\le1\) and applying dominated convergence to the regularly varying survival function gives the displayed Haar tail constant multiplied by \(\mathbb E B^a\). All boundaries, including \(\ell=1\) and \(\ell=n-1\), are covered.

## Verification

The companion `verify.py` constructs independent real and circular-complex Gaussian sketches, obtains Haar frames via QR, computes the unsketched excess residual directly, and compares both empirical laws with the **independently generated** gamma/beta factorization. It also checks projector identities, finite-moment predictions, first-order ordering under the constructed coupling, and the strict moment threshold. Run `python verify.py` with Python 3 and NumPy. The deterministic run reports `VERIFIER_OK 610` with seed 20261105. These finite numerical checks do not establish the exact distribution or infinite-moment statement; the analytic derivations above do.

As a nontrivial calibration, in the real case \(n=8,\ell=5\), the two mean excess-error values are \(\mathbb E R_{\mathrm H}=1/7\) and \(\mathbb E R_{\mathrm G}=1/3\). The former is a strict beta-contraction of the latter with factor \(B\sim\operatorname{Beta}(3/2,2)\). In the complex case \(n=6,\ell=3\), the two means are \(3/10\) and \(1/2\).

## Relationship to prior work

Epperly and Webber (2026, Theorem 2.1 and Section 5) prove the exact *expected* squared residual and minimax optimality for Haar sketches, explicitly using inverse Wishart and matrix-beta means. With one covariate, the \(q=1\) specialization here agrees with their expected-Haar formula when finite: \(\mathbb E R_{\mathrm H}=(n-\ell)/[(n-1)(\ell-2)]\) in the real case and \((n-\ell)/[(n-1)(\ell-1)]\) in the complex case. Their mean statement does not determine stochastic dominance, all moments, or the tail coefficient. The classical Gaussian distributional calculation (Ahfock et al., 2020; Browne and Andrews, 2024) accounts for the beta-prime Gaussian marginal; that marginal is not asserted as new. Haas, Giles and Nakatsukasa (2026) study multilevel sketch-and-solve estimator variances using Gaussian and structured sketches; their variance analysis concerns a different randomized estimator and does not supply the present Haar finite-dimensional law. The result here is the **independent beta contraction connecting the exact finite-dimensional Haar and Gaussian excess-residual laws** and its distribution-level consequences. Elementary beta–gamma identities and invariant-sphere laws are standard tools, not new claims.

## Limitations

There is no claim for multiple covariate columns, several responses, non-Haar structured transforms, correlated Gaussian sketches, regularization, rounding, or adaptive sketch choice. The stochastic dominance compares the two specified embedding distributions for a fixed one-column inconsistent problem; it does not say Haar is optimal for every loss among all possible sketch distributions. The tail equivalence is a leading regularly varying coefficient, not a finite-threshold bound. Classical distributional identities may appear elsewhere in different notation; originality is assessed relative to the specific published sources inspected, not as proof that no historical equivalent exists.

## References

1. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation*, arXiv:2605.19096, first public May 18, 2026; https://arxiv.org/html/2605.19096v2 (especially Theorem 2.1, Sections 5.1–5.5).
2. A. Ahfock et al., *Statistical properties of sketching algorithms*, 2020; https://pmc.ncbi.nlm.nih.gov/articles/PMC7612324/ (Section 3).
3. R. P. Browne and J. L. Andrews, *Statistical inference for sketching algorithms*, arXiv:2306.03593 (2023 preprint), published in *Information and Inference* (2024); https://arxiv.org/abs/2306.03593 (Sections 1–2).
4. M. L. Eaton and R. J. Muirhead, *A decomposition result for the Haar distribution on the orthogonal group*, arXiv:0807.2598 (2008); https://arxiv.org/abs/0807.2598 (conditional Haar sphere-law background).
5. I.-B. Haas, M. B. Giles and Y. Nakatsukasa, *A multilevel sketch-and-solve method for overdetermined least squares problems*, arXiv:2605.25809, May 25, 2026; https://arxiv.org/html/2605.25809v1 (Sections 2–3).
