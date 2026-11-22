# Spectral outliers and critical eigenprojection conditioning in radial Bergman Markov channels

## Finding

Let \(w\) be any admissible normalized radial Bergman weight on the open unit disk: \(w\geq 0\) is integrable, \(\int_{\mathbb D}w\,dA=1\), and every annulus touching the unit circle has positive \(w\,dA\)-mass. Define its moments \(\omega_n=\int_{\mathbb D}|z|^{2n}w\,dA\), its ratios \(\delta_n=\omega_n/\omega_{n+1}\), and \(d=\delta_0>1\). Let \(\Psi_w\) be the normal unital completely positive map introduced by Panja [1], and let \(P_w\) be its restriction to the diagonal von Neumann algebra, identified with \(\ell^\infty(\mathbb N_0)\).

Set \(a=1/d\), \(b=1-a\), and \(\beta_n=1-\delta_n/d\). Then \(\beta_n\) strictly increases from \(0\) to \(b\), and

\[
\boxed{\sigma(P_w)=\sigma_{\mathrm p}(P_w)=\overline B(b,a)\ \cup\ \{\beta_n:\delta_n>2\}.}
\]

The second set is finite and lies strictly to the left of the disk. Every point in the displayed spectrum has one-dimensional eigenspace; each external point \(\beta_n\) is algebraically simple. Moreover,

\[
\boxed{\sigma_{\mathrm e}^{\mathrm{Fredholm}}(P_w)=\partial B(b,a),\qquad \operatorname{ind}(P_w-\lambda I)=1\quad (|\lambda-b|<a).}
\]

For the beta weight \(w_\alpha(z)=(\alpha+1)(1-|z|^2)^\alpha\) with \(\alpha>-1\), put \(A=\alpha+2\), \(\beta_j=(\alpha+1)j/[A(j+1)]\), and \(r_j=(j+1)/(\alpha+1)\). There are exactly \(\max(0,\lceil\alpha\rceil)\) external eigenvalues, indexed by integers \(0\le j<\alpha\). For each such \(j\), its Riesz spectral projection \(\Pi_j\), acting on \(\ell^\infty\), has the **exact norm**

\[
\boxed{\|\Pi_j\|=\frac{2(A)_j}{j!}\,r_j^j(1-r_j)^{-(A+j+1)},}
\]

where \((A)_j=\prod_{s=0}^{j-1}(A+s)\), with \((A)_0=1\). As \(\alpha\downarrow j\) through values \(\alpha>j\), its spectral point joins the essential disk and

\[
\boxed{\|\Pi_j\|\sim \frac{2(j+2)_j}{j!}(j+1)^{2j+3}(\alpha-j)^{-(2j+3)}.}
\]

In particular, successive eigenvalue mergers have distinct odd-power conditioning exponents \(3,5,7,\ldots\).

## Assumptions and scope

The diagonal algebra is taken relative to the normalized monomial basis \(e_n=z^n/\sqrt{\omega_n}\) of the analytic weighted Bergman Hilbert space. The spectrum and Fredholm notions refer to the bounded operator \(P_w:\ell^\infty\to\ell^\infty\), **not** to the entire completely positive map on \(\mathcal B(A^2_w)\) and not to its predual action on \(\ell^1\). The measure is a genuine integrable radial density; in particular the squared-radius distribution is nondegenerate. The beta-weight refinement applies only for \(\alpha>-1\), and an external projection \(\Pi_j\) exists only when \(\alpha>j\).

## Proof

**1. Canonical diagonal reduction and moments.** Panja's displayed Kraus formula [1, Eq. (1.9)] is
\[
\Psi_w(X)=d^{-1}\left(S^{\prime *}XS'+\sum_{k=1}^{\infty}(\delta_{k-1}-\delta_k)Q_kXQ_k\right),
\]
where \(S'e_n=\sqrt{\delta_n}e_{n+1}\) and \(Q_ke_n=\mathbf1_{\{n\ge k\}}e_n\). Consequently a diagonal \(X=\operatorname{diag}(x_n)\) is mapped to a diagonal operator, and telescoping yields
\[
(P_wx)_n=\underbrace{\frac{\delta_n}{d}}_{a_n}x_{n+1}+\underbrace{\left(1-\frac{\delta_n}{d}\right)}_{\beta_n}x_n.
\tag{1}
\]
By strict log-convexity of the moment sequence, \(\delta_n\) strictly decreases; by support arbitrarily near radius one, \(\delta_n\to1\). Thus \(a_n\downarrow a=1/d>0\), \(\beta_n\uparrow b=1-a\), and \(\beta_0=0\).

**2. Essential disk and Fredholm index.** Let \(B:\ell^\infty\to\ell^\infty\) be the backward shift \((Bx)_n=x_{n+1}\). From (1),
\[
P_w=(bI+aB)+K,\qquad K=\operatorname{diag}(\beta_n-b)+\operatorname{diag}(a_n-a)B.
\]
The two diagonals of \(K\) vanish at infinity; their finite-rank truncations converge in operator norm, hence \(K\) is compact even on \(\ell^\infty\). For \(|\zeta|>1\), \(B-\zeta I\) is invertible by Neumann series. For \(|\zeta|<1\), it is onto (the recursive solution with initial coordinate zero is uniformly bounded) and has one-dimensional kernel, hence Fredholm of index \(+1\). For \(|\zeta|=1\), slowly varying finite-support approximate eigenvectors, placed arbitrarily far out, have residual tending to zero while staying a fixed distance from the one-dimensional kernel, so the range is not closed. Compact-perturbation invariance gives the essential circle and the interior index.

**3. Exact point and full spectra.** Equation \(P_wx=\lambda x\) is the forward recurrence
\[
x_{n+1}=\frac{\lambda-\beta_n}{a_n}x_n.\tag{2}
\]
Every eigenvector is determined by \(x_0\); taking \(x_0=1\), the solution remains bounded whenever \(|\lambda-b|<a\), since its eventual multiplier modulus is strictly less than one. If \(|\lambda-b|=a\), writing \(a_n=a+\varepsilon_n\) and \(\beta_n=b-\varepsilon_n\), the triangle inequality gives \(|\lambda-\beta_n|\le a+\varepsilon_n=a_n\), so the solution is again bounded. If \(|\lambda-b|>a\), eventual multipliers have modulus greater than one, hence a nonzero bounded solution exists exactly when a numerator in (2) vanishes, i.e. \(\lambda=\beta_j\). It then terminates at coordinate \(j\). The condition for an external point is \(\beta_j<b-a\), equivalent to \(\delta_j>2\); only finitely many qualify. For a parameter outside the closed disk not among the \(\beta_j\), choose a tail on which \(\sup a_n<\inf|\lambda-\beta_n|\), invert the tail bidiagonal operator by a Neumann series, and then invert the finite upper-triangular head by back substitution. Thus there are no additional spectral points. External spectral points are algebraically simple because the finite head has distinct diagonal values and the tail is invertible.

**4. Exact beta-weight Riesz projections.** Here \(\delta_n=(n+A)/(n+1)\), \(a_n=(n+A)/[A(n+1)]\), and \(\beta_n=(A-1)n/[A(n+1)]\). The external condition \(\delta_j>2\) becomes \(j<\alpha\), establishing the count. For fixed such \(j\), normalize the right eigenvector \(u\) by \(u_j=1\); it is supported on \(\{0,\ldots,j\}\) and
\[
\frac{u_{n+1}}{u_n}=\frac{(A-1)(j-n)}{(j+1)(n+A)}\quad(n<j),\qquad
\|u\|_\infty=u_0=\frac{(A)_j}{j!}r_j^j.
\tag{3}
\]
The corresponding left eigenvector belongs to \(\ell^1\), is normalized by \(q_j=1\), vanishes before \(j\), and satisfies
\[
q_{j+k}=(-r_j)^k\frac{(j+A)_k(j+2)_k}{(j+1)_k k!}\quad(k\ge0).
\tag{4}
\]
Indeed, (4) follows from the transpose recurrence \((\beta_n-\beta_j)q_n+a_{n-1}q_{n-1}=0\). Since \(0<r_j<1\), the \(\ell^1\)-norm is the convergent hypergeometric sum
\[
\begin{aligned}
\|q\|_1&=\sum_{k\ge0}r_j^k\frac{(j+A)_k}{k!}\frac{j+1+k}{j+1}\\
&=(1-r_j)^{-(j+A)}+\frac{j+A}{j+1}r_j(1-r_j)^{-(j+A+1)}\\
&=2(1-r_j)^{-(j+A+1)},
\end{aligned}
\tag{5}
\]
using \((A-1)r_j=j+1\). The overlap \(\langle q,u\rangle=1\), because their supports meet only at \(j\). Hence the rank-one Riesz projection is \(\Pi_jx=\langle q,x\rangle u\) and its operator norm is exactly \(\|u\|_\infty\|q\|_1\). Formula (3)--(5) gives the asserted closed form. For \(\alpha=j+\varepsilon\), \(r_j=(j+1)/(j+1+\varepsilon)\), so \(1-r_j=\varepsilon/(j+1+\varepsilon)\) and \(A+j+1=2j+3+\varepsilon\). Substitution yields the stated sharp power-law constant, since \(\varepsilon^{-\varepsilon}\to1\).

## Verification

The companion `CHECK.py` executes exact rational checks of the right/left eigenvector recurrences and the beta-weight outlier criterion, and floating-point evaluations of the infinite hypergeometric sum against its closed form. The analytical proof above establishes the infinite-dimensional assertions; finite truncations and numerical sums alone do not establish them. The checker has no external dependencies and may be run with `python3 CHECK.py`.

## Relationship to prior work

Panja [1] constructs \(\Psi_w\) and characterizes its fixed points as harmonic-symbol Toeplitz operators. The present result analyzes the **distinct operator** obtained by restricting that channel to its canonical diagonal subalgebra, with exact point/Fredholm spectra and beta-weight spectral projection norms. Classical shift Fredholm theory and compact perturbations account for the essential circle, while the exact external moment-ratio threshold, beta-weight eigenprojections, and high-order conditioning law are not stated in [1]. Trefethen--Contedini--Embree [2] give random iid bidiagonal spectral and pseudospectral theory, not this deterministic monotone-moment channel or its beta-weight projection blow-up. These basic mechanisms are acknowledged; the isolated-point formulas and merger exponents are the specific subject of this result.

## Limitations

No formula is claimed for the spectrum of \(\Psi_w\) on the whole algebra \(\mathcal B(A^2_w)\), for its predual, or for nonradial weights. The projection-norm formula applies to beta weights, not to an arbitrary moment sequence. Bibliographic completeness for general deterministic bidiagonal matrix similarity and Riesz projection results has not been established; an equivalent older theorem could affect originality. Same-source fixed-point characterizations do not by themselves settle these spectrum and conditioning questions.

## References

[1] S. Panja, *Toeplitz operators with bounded harmonic symbols on weighted Bergman spaces are the fixed points of a normal unital completely positive map*, arXiv:2611.09731v1, first submitted 2026-11-06, https://arxiv.org/html/2611.09731v1 .

[2] L. N. Trefethen, M. Contedini and M. Embree, *Spectra, pseudospectra, and localization for random bidiagonal matrices*, Communications on Pure and Applied Mathematics **54** (2001), 595--623, https://people.maths.ox.ac.uk/trefethen/publication/PDF/2001_96.pdf .

[3] Classical Fredholm theory of the unilateral shift and invariance of the Fredholm index under compact perturbations (standard functional-analysis facts; re-proved as needed above).
