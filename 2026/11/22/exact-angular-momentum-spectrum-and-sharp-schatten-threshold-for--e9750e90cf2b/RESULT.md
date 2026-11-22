# Exact angular-momentum spectrum and sharp Schatten threshold for harmonic Bergman coordinate commutators

## Finding

Let \(d\ge3\) be an integer and \(\beta>-1\). Let \(b^2_\beta(B^d)\) be the complex Hilbert space of harmonic functions on the real unit ball with the normalized weight \(c_{d,\beta}(1-|x|^2)^\beta\), and let \(P_\beta\) be its orthogonal projection. Define the bounded self-adjoint coordinate Toeplitz operators \(T_j f=P_\beta(x_j f)\). Their compact, skew-adjoint commutator \(C=[T_1,T_2]\) has **the following complete spectrum including multiplicities**.

For each integer \(\ell\ge1\), let \(\mathcal H_\ell\) denote the complex solid harmonics of degree \(\ell\). Put
\[
q_\ell=\frac{4(\beta+1)}{(2\ell+d-2)(2\ell+d+2\beta)(2\ell+d+2\beta+2)}.
\]
On \(\mathcal H_\ell\),
\[
C=-q_\ell J_{12},\qquad J_{12}=x_1\partial_{x_2}-x_2\partial_{x_1}.
\]
For every \(m=1,\dots,\ell\), the positive singular value \(mq_\ell\) occurs with multiplicity \(2\binom{\ell-m+d-3}{d-3}\), counted by the labels \((\ell,m)\) even when numerical values coincide between labels. The eigenvalues \(\pm i m q_\ell\) each occur with multiplicity \(\binom{\ell-m+d-3}{d-3}\). There is also an infinite-dimensional zero eigenspace consisting of the rotation-weight-zero harmonics.

Write \(N(t)=\#\{j:s_j(C)>t\}\) with multiplicities and put \(p_*=(d-1)/2\). Then, as \(t\downarrow0\),
\[
N(t)\sim K_{d,\beta}t^{-p_*},\qquad K_{d,\beta}=\frac{2((\beta+1)/2)^{p_*}}{(d-1)(d-3)!}\,\mathrm B\!\left(\frac{d+1}{2},d-2\right)>0.
\]
Consequently \(C\) belongs to the Schatten class \(\mathcal S_p\) exactly when \(p>(d-1)/2\) (for \(p>0\)); its ordered positive singular values satisfy \(s_j(C)\sim(K_{d,\beta}/j)^{1/p_*}\). The exact critical-degree trace growth is
\[
\sum_{\ell=1}^{L}\sum_{m=1}^{\ell}2\binom{\ell-m+d-3}{d-3}(mq_\ell)^{p_*}
=(d-1)K_{d,\beta}\log L+O_{d,\beta}(1).
\]
In particular, \(C\) is Hilbert--Schmidt precisely in dimensions \(d=3,4\), and the three-dimensional counting coefficient is \(K_{3,\beta}=(\beta+1)/4\).

## Assumptions and scope

The inner product uses \(dV_\beta(x)=c_{d,\beta}(1-|x|^2)^\beta dx\), with \(c_{d,\beta}=\Gamma(d/2+\beta+1)/(\pi^{d/2}\Gamma(\beta+1))\). All harmonic functions are complex valued, and \(\mathcal H_\ell\) consists of *homogeneous* harmonic polynomials (restricted to the ball). The operators \(T_j\) are defined on the whole Hilbert space, not merely on polynomial subspaces. A nonzero pair of real linear coordinate symbols \(a\cdot x,b\cdot x\) has the same singular list multiplied by \(|a\wedge b|\), by orthogonal covariance; if \(a\wedge b=0\), its commutator is zero. The main formula is stated for the first two orthogonal coordinates to fix conventions.

## Proof

1. **Harmonic decomposition and radial moments.** The orthogonal harmonic-degree decomposition is \(b^2_\beta=\widehat\bigoplus_{\ell\ge0}\mathcal H_\ell\). For \(H\in\mathcal H_\ell\), \(\ell\ge1\), the Fischer decomposition and a Laplacian calculation give
\[
x_jH=U_jH+\frac{|x|^2}{2\ell+d-2}\,\partial_jH,\quad U_jH=x_jH-\frac{|x|^2}{2\ell+d-2}\partial_jH\in\mathcal H_{\ell+1}.
\]
The radial-weight projection of \(|x|^2Q\) onto \(\mathcal H_{\ell-1}\), for \(Q\in\mathcal H_{\ell-1}\), multiplies \(Q\) by the ratio
\[
\frac{\int_0^1r^{2\ell+d-1}(1-r^2)^\beta dr}{\int_0^1r^{2\ell+d-3}(1-r^2)^\beta dr}=
\frac{\ell-1+d/2}{\ell+d/2+\beta}.
\]
Therefore \(T_jH=U_jH+L_jH\), with \(L_jH=(2\ell+d+2\beta)^{-1}\partial_jH\). At \(\ell=0\), \(L_j=0\) and \(U_jH=x_jH\). Each formula holds independently of normalization of a homogeneous harmonic polynomial.

2. **Exact commutator.** The degree-raising maps \(U_j\) commute with one another, as do the lowering maps \(L_j\) (these assertions follow by differentiating the displayed Fischer formula). The antisymmetrized raise-after-lower contribution on \(\mathcal H_\ell\) equals \((2\ell+d+2\beta)^{-1}J_{12}\). The lower-after-raise contribution equals
\[
-\frac{2\ell+d}{(2\ell+d-2)(2\ell+d+2\beta+2)}J_{12}.
\]
Adding and factoring yields \(-q_\ell J_{12}\). The constant sector has zero commutator because it has zero angular derivative. Since \(\|J_{12}|_{\mathcal H_\ell}\|=\ell\) and \(\ell q_\ell=O(\ell^{-2})\), \(C\) is compact.

3. **Exact multiplicities.** Under rotation in the first coordinate two-plane, let the formal weight variable be \(z\). The graded character of all complex harmonic homogeneous polynomials is
\[
\sum_{\ell\ge0}\chi_{\mathcal H_\ell}(z)t^\ell=
\frac{1-t^2}{(1-tz)(1-tz^{-1})(1-t)^{d-2}}.
\]
Taking the coefficient of rotation weight \(m\in\mathbb Z\) gives \(t^{|m|}(1-t)^{-(d-2)}\), hence multiplicity \(\binom{\ell-|m|+d-3}{d-3}\) if \(|m|\le\ell\), and zero otherwise. On that weight space \(J_{12}\) has eigenvalue \(im\). This proves the complete signed and singular spectrum.

4. **Sharp counting asymptotic.** Uniformly for \(1\le m\le\ell\), the positive singular value satisfies
\[
mq_\ell=\frac{\beta+1}{2}\frac{m/\ell}{\ell^2}\bigl(1+O_{d,\beta}(\ell^{-1})\bigr).
\]
Writing \(c=(\beta+1)/2\) and replacing the polynomial multiplicities by their leading term, a two-variable Riemann-sum argument (first restrict \(m/\ell\) and \(\ell\sqrt{t/c}\) away from their endpoints, then control endpoint strips by the same polynomial bounds) gives
\[
\lim_{t\downarrow0}t^{p_*}N(t)
=\frac{2c^{p_*}}{(d-3)!(d-1)}\int_0^1u^{p_*}(1-u)^{d-3}du=K_{d,\beta}.
\]
The omitted finitely many low degrees contribute \(O(1)\) to \(N(t)\). The strict positivity of the beta integral proves the necessary and sufficient Schatten exponent and the ordered singular-value law. For \(p=p_*\), the same binomial/Riemann expansion degree by degree gives \((d-1)K_{d,\beta}/\ell+O(\ell^{-2})\); summing proves the critical logarithmic formula.

## Verification

A standalone checker, `check.py`, uses exact rational symbolic polynomial identities in three dimensions for harmonic degrees one through six and three beta weights, verifies the scalar commutator coefficient for symbolic dimension/degree/weight, and checks all rotation-weight dimensions for dimensions three through eight and degrees one through thirty-four. Replaying it produces `PASS: 256 symbolic polynomial and representation-dimension diagnostics`. These finite diagnostics are not substituted for the all-dimensional analytic proof. Independent formal proof or independent human assessment has not been performed.

## Relationship to prior work

Hagger, Liu, Taskinen and Virtanen (arXiv:2011.04699, first posted 9 November 2020) develop boundedness and compactness for Toeplitz operators with locally integrable symbols in precisely these weighted real-ball harmonic Bergman spaces. Their results provide the analytic setting but do not state an exact pairwise coordinate-commutator angular spectrum or a singular-value counting constant. Nishio and Tanaka (2017) analyze harmonic Bergman kernels and Toeplitz operators with radial measures on real balls; their radial diagonal moment formulas are related background, whereas the present coordinate symbols are nonradial and their commutator is governed by rotation weight. Classical spherical-harmonic branching and beta moments are used as standard ingredients, not claimed as new. The new statement is the explicit coordinate-commutator law together with its complete multiplicities and sharp Weyl/Schatten constant.

## Limitations

The result concerns real balls with the standard power weight, dimension \(d\ge3\), and linear coordinate symbols. It does not classify general bounded symbols, other domains, or arbitrary nonradial weights. Novelty is a best-knowledge comparison, not a formal priority determination. The checker tests finite low-degree identities only. An independent audit has not been conducted.

## References

- R. Hagger, C. Liu, J. Taskinen, J. A. Virtanen, *Toeplitz operators on the unit ball with locally integrable symbols*, arXiv:2011.04699 (9 November 2020), https://arxiv.org/abs/2011.04699 .
- M. Nishio and K. Tanaka, *Harmonic Bergman kernels and Toeplitz operators on the ball with radial measures*, Rev. Roumaine Math. Pures Appl. **62** (2017), 155–169, https://imar.ro/journals/Revue_Mathematique/pdfs/2017/1/8.pdf .
- B. R. Choe, Y. J. Lee, K. Na, *Toeplitz operators on harmonic Bergman spaces*, Nagoya Math. J. **174** (2004), 165–186, https://doi.org/10.1017/S0027763000008837 .
