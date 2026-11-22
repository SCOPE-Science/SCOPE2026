# Exceptional-point lattice and sharp eigenvalue counting for a nilpotent rank-one factorial-shift perturbation

## Finding

Let \(H=\ell^2(\mathbb N_0)\), with canonical basis \((e_n)_{n\ge0}\). Define the factorially damped unilateral shift and the linear functional
\[
Se_n=\frac{e_{n+1}}{n+1},\qquad
\varphi(e_0)=0,\qquad \varphi(e_n)=\frac1{n+1}\quad(n\ge1),
\]
and \(Fx=\varphi(x)e_0\). For every \(\alpha\in\mathbb C\setminus\{0\}\), put \(T_\alpha=S+\alpha F\) and \(\beta=\alpha^{-1}\). Thus \(F\) is nonzero, rank one and square-zero. The operator \(T_\alpha\) is compact and injective, has dense range, and has Fredholm essential spectrum \(\{0\}\). Its complete spectrum is
\[
\sigma(T_\alpha)=\{0\}\cup
\left\{z^{-1}:z\in\mathbb C\setminus\{0\},\quad
 e^z-1-z=\beta\right\}.
\tag{1}
\]
Every nonzero eigenvalue has geometric multiplicity one. All are algebraically simple except at precisely the couplings
\[
\alpha_k=\frac{i}{2\pi k}\qquad(k\in\mathbb Z\setminus\{0\}),
\tag{2}
\]
where \(T_{\alpha_k}\) has exactly one algebraically double nonzero eigenvalue \(\lambda_k=(2\pi i k)^{-1}=-\alpha_k\), with one Jordan chain of length two, and all its other nonzero eigenvalues are algebraically simple. At each such coupling, writing \(\beta_k=-2\pi i k\), the two local eigenvalue branches split for \(\beta\to\beta_k\) as
\[
\lambda_{k,\pm}(\beta)
=\frac1{2\pi i k}\mp
 \frac{\sqrt{2(\beta-\beta_k)}}{(2\pi i k)^2}
 +O_k(|\beta-\beta_k|).
\tag{3}
\]
The two choices of the square root merely exchange labels.

For every fixed nonzero \(\alpha\), all sufficiently large positive and negative integers \(j\) label exactly one reciprocal root satisfying
\[
z_j=\log(2\pi |j|)+i\left(2\pi j+\frac\pi2\operatorname{sgn}j\right)
 +O_\alpha\left(\frac{\log|j|}{|j|}\right),
\qquad \lambda_j=z_j^{-1}.
\tag{4}
\]
There are only finitely many remaining eigenvalues. Consequently, counting nonzero eigenvalues with algebraic multiplicity,
\[
N_\alpha(r):=\#\{\lambda\in\sigma(T_\alpha)\setminus\{0\}:|\lambda|>r\}
=\frac1{\pi r}+O_\alpha(1)\quad(r\downarrow0),
\tag{5}
\]
and
\[
\sum_{\lambda\ne0}|\lambda|^p<\infty\quad\Longleftrightarrow\quad p>1,
\qquad
\lim_{p\downarrow1}(p-1)\sum_{\lambda\ne0}|\lambda|^p=\frac1\pi.
\tag{6}
\]
Here eigenvalues are repeated according to algebraic multiplicity. For all \(p>0\), \(T_\alpha\in\mathcal S_p\) if and only if \(p>1\), so the eigenvalue summability threshold matches the operator Schatten threshold.

When \(\alpha>0\) is real, there are exactly two real nonzero eigenvalues \(\lambda_-<0<\lambda_+\), and \(\lambda_+\) is the unique eigenvalue of maximal modulus. As \(\alpha\downarrow0\),
\[
\rho(T_\alpha)=\lambda_+(\alpha)\sim\frac1{\log(1/\alpha)},
\qquad \lambda_-(\alpha)\sim-\alpha.
\tag{7}
\]
Thus arbitrarily small nilpotent rank-one perturbations produce a universal reciprocal counting law, a discrete set of defective-eigenvalue couplings accumulating at zero, and two sharply different real weak-coupling eigenvalue scales.

## Assumptions and scope

All Hilbert spaces and operators are complex; \(\mathbb N_0=\{0,1,2,\ldots\}\). The coefficient functional is linear, not conjugate-linear. The scalar parameter is any fixed nonzero complex \(\alpha\), and the implied constants in (4)–(5) may depend on it. The counting function includes algebraic multiplicities. The Schatten statement concerns all \(p>0\), interpreted as quasi-ideals for \(p<1\). At \(\alpha=0\), the operator is \(S\), which is quasinilpotent and has spectrum \(\{0\}\); equations (1)–(7) are not assertions for that limiting parameter.

## Proof

**1. Compactness, nullspace, range and the scalar resolvent.** The weights \(1/(n+1)\) tend to zero, and
\[
\|S^m\|=1/m!\quad(m\ge1),\qquad \|\varphi\|^2=\sum_{n=1}^\infty(n+1)^{-2}<\infty.
\]
Hence \(S\) is compact and quasinilpotent, \(F\) is bounded rank one, and \(F^2=\varphi(e_0)F=0\). Compactness of \(T_\alpha\) follows. For \(\lambda\ne0\), the entire-in-\(\lambda^{-1}\) resolvent expansion gives
\[
R_\lambda e_0=(\lambda-S)^{-1}e_0
=\sum_{n=0}^\infty\frac{\lambda^{-n-1}}{n!}e_n,
\quad
\varphi(R_\lambda e_0)
=\sum_{n=1}^\infty\frac{\lambda^{-n-1}}{(n+1)!}
=e^{1/\lambda}-1-1/\lambda.
\tag{8}
\]
The rank-one resolvent identity says that \(\lambda-T_\alpha\) is invertible exactly when
\(D_\alpha(\lambda)=1-\alpha\varphi(R_\lambda e_0)\ne0\), proving (1) for nonzero \(\lambda\). Every nonzero eigenvector is proportional to \(R_\lambda e_0\), so geometric multiplicity is one. For \(T_\alpha x=0\), the positive-coordinate equations \((T_\alpha x)_{n+1}=x_n/(n+1)\) force \(x=0\). If \(T_\alpha^*y=0\), then \(y_1=0\) and \(y_{n+1}=-\overline\alpha y_0\) for all \(n\ge1\), forcing \(y_0=0\) by square summability and then \(y=0\). Therefore \(T_\alpha\) is injective and has dense, nonclosed range; \(0\) belongs to its continuous spectrum. A compact operator on an infinite-dimensional Hilbert space has essential spectrum \(\{0\}\) here.

**2. Algebraic multiplicity and exceptional couplings.** On a small circle enclosing a nonzero eigenvalue and no other spectrum, the rank-one resolvent formula gives
\[
(\lambda-T_\alpha)^{-1}-R_\lambda
=\frac{\alpha R_\lambda e_0\,\varphi R_\lambda}{D_\alpha(\lambda)},
\qquad
\operatorname{tr}\big((\lambda-T_\alpha)^{-1}-R_\lambda\big)
=\frac{D_\alpha'(\lambda)}{D_\alpha(\lambda)}.
\tag{9}
\]
The contour integral of the trace is the rank of the Riesz projection, equal to the zero order of \(D_\alpha\). Under \(z=1/\lambda\) this is the zero order of \(G(z)-\beta\), where \(G(z)=e^z-1-z\). A multiple zero requires \(G'(z)=e^z-1=0\), i.e. \(z=2\pi i k\). The case \(k=0\) is excluded by \(\beta\ne0\), while for \(k\ne0\), \(\beta=G(2\pi i k)=-2\pi i k\), giving (2). As \(G''(2\pi i k)=1\), the multiplicity is exactly two, and only one Jordan block occurs because geometric multiplicity is one. Taylor expansion \(G(z)=\beta_k+(z-2\pi i k)^2/2+O((z-2\pi i k)^3)\), inversion of the local quadratic ramification, and \(\lambda=1/z\) yield (3).

**3. Exhaustive asymptotic location of the roots.** Fix \(C=1+\beta\). The eigenvalue equation is \(e^z=z+C\), equivalently (as a set, with coincident branch values not counted twice) to
\[
z=-C-W_j(-e^{-C}),\qquad j\in\mathbb Z,
\tag{10}
\]
where \(W_j\) ranges over the complex Lambert-function branches. We also give a direct proof of the asymptotic and completeness, avoiding any branch-cut convention. If \(|z|\to\infty\) along solutions, then \(e^{\operatorname{Re}z}=|z+C|\), so \(\operatorname{Re}z=\log|z|+O_C(|z|^{-1})\). Thus \(|\operatorname{Im}z|\to\infty\), and comparison of arguments in \(e^z=z+C\) shows for an integer \(j\) of the same eventual sign as \(\operatorname{Im}z\),
\[
\operatorname{Im}z=2\pi j+\tfrac\pi2\operatorname{sgn}j
 +O_C(\log|j|/|j|).
\]
It follows also that \(\operatorname{Re}z=\log(2\pi|j|)+O_C(\log|j|/|j|)\). Conversely, define \(c_j=\log(2\pi|j|)+i(2\pi j+\operatorname{sgn}(j)\pi/2)\). In the fixed disk \(|z-c_j|\le1\) and for large \(|j|\), the principal logarithm is analytic at \(z+C\), and \(z\mapsto\operatorname{Log}(z+C)+2\pi i j\) maps that disk into itself with Lipschitz constant \(O_C(|j|^{-1})\). The contraction theorem supplies exactly one root there, differing from \(c_j\) by \(O_C(\log|j|/|j|)\). The preceding necessary localization shows that all sufficiently large roots are exhausted by these disks. Bounded regions contain only finitely many roots because \(G-\beta\) is a nonzero entire function. This proves (4) and infinitude for every \(\alpha\ne0\).

**4. Spectral counting and Schatten threshold.** By (4), \(|z_j|=2\pi|j|+O_\alpha(1)\). Counting two tails for the inequality \(|z_j|<r^{-1}\) gives (5), including the finitely many exceptional algebraic-multiplicity corrections. Similarly \(|\lambda_j|=(2\pi|j|)^{-1}(1+O_\alpha(|j|^{-1}))\); subtracting the two-sided Dirichlet series \(2(2\pi)^{-p}\sum_{j\ge1}j^{-p}\) leaves a term uniformly bounded for \(p\) near one. Its zeta pole has residue \(1/\pi\), proving (6). The singular values of \(S\) are exactly \(1,1/2,1/3,\ldots\); since \(F\) is finite rank, the same \(\mathcal S_p\) membership threshold \(p>1\) holds for \(T_\alpha\).

**5. Real positive coupling.** The real function \(G(x)=e^x-1-x\) is strictly convex with unique minimum \(G(0)=0\) and tends to infinity at both ends, so \(G(x)=\alpha^{-1}>0\) has exactly one negative and one positive real solution \(z_-<0<z_+\). Because \(G(z)=\sum_{n\ge2}z^n/n!\) has strictly positive coefficients of consecutive degrees, \(|G(z)|\le G(|z|)\), with equality for nonzero \(z\) only when \(z>0\). Therefore every root has \(|z|\ge z_+\), with equality only for \(z_+\); its reciprocal is the unique spectral-radius eigenvalue. For \(\alpha\downarrow0\), \(e^{z_+}=z_++1+\alpha^{-1}\) gives \(z_+\sim\log(1/\alpha)\); and \(e^{z_-}=z_-+1+\alpha^{-1}\) with \(z_-<0\) gives \(z_-=-1-\alpha^{-1}+o(1)\). Taking reciprocals proves (7).

## Verification

The standalone `CHECK.py` performs high-precision numerical substitutions into the exact characteristic equation, verifies the Lambert branch formula for selected complex couplings, checks the exceptional-point derivatives, tracks the two real roots, tests the two-sided large-index root locations, and verifies square-root splitting near several exceptional couplings. Running it with Python and `mpmath` produced `PASS: 186 finite diagnostic checks`. These finite checks are supplementary; the proofs above establish statements for all permitted parameters and infinitely many eigenvalues. They do not independently certify originality.

## Relationship to prior work

Tcaciuc (2018; 2019 journal version), §2 Example, uses the same factorial-weight shift with the **untruncated** functional \(\varphi_0(e_n)=1/(n+1)\) for all \(n\ge0\). That rank-one perturbation has \(\varphi_0(e_0)=1\), its resolvent characteristic function is \(e^z-1\), and the coupling \(\alpha=-1\) remains quasinilpotent. The present functional removes precisely the zeroth coefficient to impose the natural nilpotency condition \(F^2=0\); the resulting function \(e^z-1-z\) has no omitted nonzero level, but has an infinite explicit lattice of critical values and an exact defective-eigenvalue classification. The earlier example does not imply (2)–(7).

Bračič and Kandić (2026), §6, establish general rank-one spectral criteria and construct square-zero perturbations with infinitely many spectral components for shifts with summable weights and certain odd characteristic functions. Our weights \(1/(n+1)\) are **not** summable and the characteristic function is not odd. Their general infinitude mechanism and rank-one resolvent identity are acknowledged as antecedents; they do not give the new exceptional-point lattice, eigenvalue counting coefficient, Schatten-index matching, or sharply separated weak-coupling scales. The core transcendental analysis uses standard properties of exponential equations and Lambert branches, which are not themselves claimed new.

## Limitations

The result is for one explicitly specified natural shift and one nilpotent rank-one direction, not for arbitrary compact shifts or rank-one functionals. No uniformity as \(\alpha\to0\) is claimed in the \(O_\alpha(1)\) counting remainder. The exact nonzero spectrum is countable and accumulates only at zero; no claim of diagonalizability or basis completeness is made. Numerical diagnostics do not constitute an independent mathematical audit. Older unindexed calculations of the same exponential-minus-linear characteristic function could limit priority; the inspected sources do not establish coverage of the combined operator spectral and exceptional-point theorem.

## References

1. J. Bračič and M. Kandić, *On operators with many spectral components*, arXiv:2611.12208v1, first posted 9 November 2026, §6, https://arxiv.org/html/2611.12208v1 .
2. A. Tcaciuc, *On quasinilpotent operators and the invariant subspace problem*, arXiv:1805.03277, first posted 8 May 2018, §2, https://arxiv.org/abs/1805.03277 .
3. *SciPy special.lambertw documentation*, branch definition and numerical evaluation, https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.lambertw.html .
