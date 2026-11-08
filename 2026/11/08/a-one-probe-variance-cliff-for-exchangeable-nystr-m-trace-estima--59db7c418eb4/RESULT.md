# A one-probe variance cliff for exchangeable Nyström trace estimation

## Finding

Let \(k\ge 2\), \(n\ge k\), \(\lambda>0\), and let \(P\in\mathbb R^{n\times n}\) be any orthogonal projector of rank \(k\). Set \(A=\lambda P\) and let \(f:[0,\infty)\to\mathbb R\) satisfy \(f(0)=0\) and \(a=f(\lambda)>0\). In particular, the claim applies to the operator-monotone functions considered in FlexTrace, such as \(f(x)=\log(1+x)\). Use exactly \(m=k\) independent, unnormalized standard real Gaussian test columns in the published full-sketch/leave-one-out FlexTrace estimator. Let \(\widehat\tau_k\) denote its trace estimate, and \(\widehat V_k\) the standard squared-error proxy based on the empirical spread of the \(k\) leave-one-out basic estimates (as used by XNysTrace).

Then the estimator is unbiased, but its variance and the mean squared-error proxy are exactly

\[
\operatorname{Var}(\widehat\tau_k)=a^2\frac{k+3}{2k},\qquad
\mathbb E\widehat V_k=a^2\frac{3}{2k},\qquad
\frac{\mathbb E\widehat V_k}{\mathbb E(\widehat\tau_k-ka)^2}=\frac{3}{k+3}.
\]

Every two distinct basic leave-one-out estimates have correlation exactly \(1/4\), independently of \(k\). In particular, the mean squared-error proxy can underestimate the actual mean squared error by an arbitrarily large factor in this sequence of problems: the ratio tends to zero as \(k\to\infty\). By contrast, using \(m=k+1\) independent Gaussian columns makes every basic estimate exactly \(ka\) almost surely, so both the trace error and its error proxy vanish. This is a sharp one-additional-probe transition for this rank-\(k\) family.

For \(k=2\), the normalized excess \(S=(\widehat\tau_2/a)-1\) has the explicit Laplace transform

\[
\mathbb E e^{-sS}=\frac{s+2}{2(1+s)^{3/2}}\quad(s\ge0),
\]

and hence is an equal mixture of \(\chi_1^2/2\) and \(\chi_3^2/2\), rather than their sum.

## Assumptions and scope

The Nyström map for any test matrix \(X\) is \(\mathcal N(A,X)=AX(X^{\mathsf T}AX)^\dagger X^{\mathsf T}A\), with Moore–Penrose inverse. Let \(\Omega=[\omega_1,\dots,\omega_m]\) have independent \(N(0,I_n)\) columns, and let \(\Omega_{-i}\) omit column \(i\). The full-sketch FlexTrace basic estimates and their exchangeable average are defined by

\[
T_i=\operatorname{tr} f(\mathcal N(A,\Omega_{-i}))+
\omega_i^{\mathsf T}\bigl[f(\mathcal N(A,\Omega))-f(\mathcal N(A,\Omega_{-i}))\bigr]\omega_i,
\qquad \widehat\tau_m=\frac1m\sum_{i=1}^m T_i.
\]

The squared-error proxy (defined for \(m\ge2\)) is

\[
\widehat V_m=\frac{1}{m(m-1)}\sum_{i=1}^m(T_i-\widehat\tau_m)^2.
\]

On the flat-spectrum projector input, these basic estimates equal the XNysTrace basic estimates for \(f(A)=aP\) (equivalently, \(a/\lambda\) times those for \(A\)). This comparison concerns the real Gaussian estimator, not the normalized-spherical or non-Gaussian variants. The function need not be operator monotone for the algebraic identity, but the cited application uses that class.

## Proof

**1. Flat-spectrum Nyström identity.** Write \(G=P\Omega\). The defining pseudoinverse gives, for every \(X\),

\[
\mathcal N(\lambda P,X)=\lambda\,\Pi_{\operatorname{range}(PX)},
\]

where \(\Pi\) is the orthogonal projector onto the indicated column space. Functional calculus and \(f(0)=0\) give \(f(\mathcal N(\lambda P,X))=a\,\Pi_{\operatorname{range}(PX)}\). At \(m=k\), \(P\Omega\) has rank \(k\) almost surely, while each \(P\Omega_{-i}\) has rank \(k-1\) almost surely. Consequently,

\[
T_i=a(k-1+R_i),\qquad
R_i=\| (I-\Pi_{-i})P\omega_i\|^2,
\]

where \(\Pi_{-i}\) is the orthogonal projector onto the span of all projected columns except the \(i\)-th, within \(\operatorname{range}(P)\).

**2. Single and paired residual moments.** By independence of \(P\omega_i\) from \(\Pi_{-i}\), the residual \(R_i\) has the \(\chi^2_1\) law. Hence \(\mathbb E R_i=1\) and \(\operatorname{Var}R_i=2\). For distinct \(i,j\), condition on the projected \(k-2\) other columns. Their orthogonal complement inside \(\operatorname{range}(P)\) is a two-dimensional Euclidean plane. The remaining projected columns are independent standard Gaussian vectors \(u,v\) in this plane, so

\[
R_i=\|u\|^2\sin^2\theta,\qquad R_j=\|v\|^2\sin^2\theta,
\]

where \(\theta\) is their relative angle. The lengths are independent of each other and of the angle; \(\mathbb E\|u\|^2=\mathbb E\|v\|^2=2\), and uniform angular directions yield \(\mathbb E\sin^4\theta=3/8\). Therefore \(\mathbb E[R_iR_j]=3/2\) and \(\operatorname{Cov}(R_i,R_j)=1/2\). This also covers \(k=2\), when the conditioning span is zero-dimensional. The basic-estimate correlation is \((1/2)/2=1/4\).

**3. Variance and calibration.** Because \(\widehat\tau_k=a(k-1+k^{-1}\sum_iR_i)\), linearity yields \(\mathbb E\widehat\tau_k=ka=\operatorname{tr}f(A)\). Exchangeability and the moments in step 2 give

\[
\operatorname{Var}(\widehat\tau_k)
=\frac{a^2}{k^2}\left(2k+\frac{k(k-1)}2\right)
=a^2\frac{k+3}{2k}.
\]

For exchangeable variables with individual variance \(v\) and distinct-pair covariance \(c\), the expected sample-spread proxy equals \((v-c)/k\). Substitution of \(v=2a^2\) and \(c=a^2/2\) proves \(\mathbb E\widehat V_k=3a^2/(2k)\), and the displayed calibration ratio follows. These are identities for each finite \(k\), not asymptotic guesses.

**4. One additional column.** For \(m=k+1\), every leave-one-out projected matrix \(P\Omega_{-i}\) has rank \(k\) almost surely, so \(\mathcal N(A,\Omega_{-i})=\mathcal N(A,\Omega)=A\). The formula for every \(T_i\) reduces to \(\operatorname{tr}f(A)=ka\) exactly, proving zero variance and zero proxy. The same argument applies to all \(m\ge k+1\).

**5. Exact two-probe law.** For \(k=2\), let \(u,v\in\mathbb R^2\) be independent standard Gaussians and \(\theta\) their relative angle. Then \(S=(\|u\|^2+\|v\|^2)\sin^2\theta/2\). The sum of squared lengths has the \(\chi^2_4\) law and is independent of \(B=\sin^2\theta\sim\operatorname{Beta}(1/2,1/2)\). Conditioning on \(B\) gives

\[
\mathbb E e^{-sS}=\mathbb E(1+sB)^{-2}=
\frac{s+2}{2(1+s)^{3/2}}=
\frac12(1+s)^{-1/2}+\frac12(1+s)^{-3/2}.
\]

Uniqueness of Laplace transforms identifies the claimed equal mixture.

## Verification

The self-contained NumPy script `verify.py` independently evaluates the literal Nyström and matrix-function formulas on projector matrices of ranks \(2,3,4,6\), for both \(k\) and \(k+1\) probes, and compares them against the geometric residual identity. It numerically integrates the two angular moments and the two-probe Laplace formula and separately simulates leave-one-out Gaussian residuals for ranks \(2,3,5,8\). On the documented deterministic random seed it passed 479 assertions. The integral identities and all-dimensional covariance calculation are proved above; Monte Carlo samples are diagnostics rather than proof.

## Relationship to prior work

Madhavan, Alexanderian, and Saibaba (2026) introduce FlexTrace with a full Nyström function estimate and leave-one-out correction, together with global bias and mean-squared-error bounds. Epperly, Tropp, and Webber (2023/2024) establish the exchangeable XNysTrace construction, their general variance bounds, and an exact relation between the average estimated squared error and the correlation of the leave-one-out terms (Proposition 3.1). Those formulas are used here and are not claimed as new. The contribution of the present specialization is the explicit rank-critical joint covariance \(a^2/2\), the exact variance and proxy ratio \(3/(k+3)\), the one-probe exactness transition, and the two-probe distribution. In particular, the prior general posterior-error formula does not itself determine the correlation \(1/4\) for this model.

## Limitations

This is a flat positive-eigenvalue projector family and uses exact arithmetic and independent, unnormalized real Gaussian probes. The failure is in the expectation of the squared-error proxy; no universal lower bound on the probability of individual underestimation is asserted. The absolute variance floor as \(k\to\infty\) does not prevent the relative root-mean-square error from decaying because the true trace increases linearly with \(k\). No claims are made for arbitrary spectra, probe normalization, numerical rank decisions, or general-purpose adaptive stopping. An equivalent result in older Gaussian regression/Wishart literature cannot be categorically excluded without exhaustive historical indexing.

## References

1. Madhusudan Madhavan, Alen Alexanderian, and Arvind K. Saibaba, *FlexTrace: Exchangeable Randomized Trace Estimation for Matrix Functions*, arXiv:2603.05721v1 (first submitted 2026-03-05), https://arxiv.org/abs/2603.05721 .
2. Ethan N. Epperly, Joel A. Tropp, and Robert J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, arXiv:2301.07825 (first submitted 2023-01-19), subsequently SIAM Journal on Matrix Analysis and Applications 45 (2024), 1–23, https://arxiv.org/abs/2301.07825 .
