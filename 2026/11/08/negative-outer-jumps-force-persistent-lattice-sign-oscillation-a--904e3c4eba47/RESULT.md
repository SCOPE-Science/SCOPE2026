# Negative outer jumps force persistent lattice sign oscillation and a linear cycle-positivity delay

## Finding

A stable finite-range symmetric finite-difference diffusion generator whose **outermost jump coefficient is negative** can have a distinctly different positivity behavior on the infinite lattice and on finite periodic grids. At **every** strictly positive time the infinite-lattice kernel has infinitely many positive and infinitely many negative coefficients. Every finite periodic approximation becomes strictly positive at sufficiently late times, but this recovery cannot occur on a time window smaller than a constant multiple of its circumference.

More precisely, let \(m\ge2\), let real numbers \(a_{-j}=a_j\), \(-m\le j\le m\), obey \(\sum_j a_j=0\), \(a_m<0\), and
\[
q(\theta)=\sum_{j=-m}^m a_j e^{ij\theta}<0\qquad(0<\theta<2\pi).
\]
On \(\ell^2(\mathbb Z)\), let \(Q=\sum_j a_jS^j\) where \((Su)_k=u_{k+1}\), and write \(p_j(t)=(e^{tQ})_{0j}\). Then, for every \(t>0\), both the sets \(\{j\ge1:p_j(t)>0\}\) and \(\{j\ge1:p_j(t)<0\}\) are infinite. For periodic \(n\)-point restrictions \(Q_n\) with \(n\ge2m+1\), each \(e^{tQ_n}\) becomes strictly entrywise positive for all sufficiently large \(t\), but there is a stencil-dependent \(c>0\) and an \(n_0\) such that every \(n\ge n_0\) and \(0<t\le cn\) have at least one negative entry in \(e^{tQ_n}\).

For the classical fourth-order five-point heat stencil,
\[
Q=D-\frac1{12}D^2,\quad D=S+S^{-1}-2I,
\quad (a_0,a_{\pm1},a_{\pm2})=\left(-\frac52,\frac43,-\frac1{12}\right),
\]
one can take \(c=1/500\). If \(H_n\) denotes the first time after which all later periodic heat operators are nonnegative, the concrete bounds are
\[
\boxed{\liminf_{n\to\infty}\frac{H_n}{n}\ge\frac1{500},\qquad H_n\le\frac{n^2}{16}\quad(n\ge5).}
\]
The lower bound is deliberately conservative and is **not** asserted to be the optimal linear coefficient.

## Assumptions and scope

All operators and kernels are real. The infinite operator is bounded because its stencil is finite. The strict symbol condition makes its spectrum nonpositive and ensures strict negativity away from zero frequency, despite its negative off-diagonal second-neighbor interactions. Each periodic \(Q_n\) is a symmetric circulant matrix with zero row sums. Nonnegative matrices and vectors are ordered entrywise. Time \(t\) is dimensionless: if the physical mesh spacing is \(h\) and diffusivity is \(\kappa\), the physical time is \(h^2t/\kappa\). The theorem does not assert a lower bound uniform in a fixed *physical* time as \(h\to0\).

For \(r>0\), put \(q(r)=\sum_{j=-m}^m a_jr^j\). The kernel is the Laurent coefficient sequence of
\[
F_t(z)=\exp(tq(z))=\sum_{j\in\mathbb Z}p_j(t)z^j,
\]
a Laurent series converging absolutely for every \(z\ne0\). Symmetry yields \(p_{-j}(t)=p_j(t)\). On a cycle, the coefficient for a residue class is \(P^{(n)}_j(t)=\sum_{\ell\in\mathbb Z}p_{j+\ell n}(t)\), an absolutely convergent periodization.

## Proof

**1. Infinitely many coefficients of each sign at every time.** Fix \(t>0\). Since \(a_m<0\) is the coefficient of the highest positive power, \(q(r)\to-\infty\), and hence \(F_t(r)\to0^+\), as \(r\to\infty\). The Laurent function \(F_t\) has an essential singularity at infinity, because \(q\) has a genuine positive-degree term. Thus there are infinitely many nonzero \(p_j(t)\) with \(j>0\). Suppose only finitely many of them were negative. Select \(J\) above all negative nonnegative-index coefficients with \(p_J(t)>0\). Absolute convergence at \(r=1\) bounds the entire negative-index contribution uniformly for \(r\ge1\); the finitely many negative nonnegative-index terms are at most \(Cr^{J-1}\). Consequently \(F_t(r)\ge p_J(t)r^J-Cr^{J-1}-C\to+\infty\), a contradiction. Similarly, if only finitely many positive high-index coefficients existed, select a negative \(p_J(t)\) above all positive nonnegative-index coefficients and obtain \(F_t(r)\le p_J(t)r^J+Cr^{J-1}+C\to-\infty\), contradicting \(F_t(r)>0\). Hence infinitely many coefficients of both signs occur. The reflection symmetry gives the same result on both spatial half-lines.

**2. Finite periodic recovery.** On an \(n\)-cycle the real eigenvalues are \(q(2\pi k/n)\), with a simple zero at \(k=0\) and all others strictly negative. Thus
\[
e^{tQ_n}=\frac1n\mathbf1\mathbf1^{\mathsf T}+\frac1n\sum_{k=1}^{n-1}e^{tq(2\pi k/n)}v_kv_k^*,
\]
where \(v_k\) denotes the corresponding unit-modulus Fourier vector (so the Fourier sum uses the normalization shown). The remainder converges entrywise to zero, proving eventual strict positivity. The exact periodization identity follows by Fourier transformation or by uniqueness of the finite circulant matrix exponential.

**3. A uniform negative-entry window.** Let \(b>1\) be so large that \(q(b)<0\), choose \(s>0\), and define
\[
\alpha=a_0+\sum_{j=1}^{m}|a_j|\bigl((be^s)^j+(be^s)^{-j}\bigr)>0.
\]
Choose \(c>0\) with \(c\alpha<s/2\). Factoring out \(e^{ta_0}\) from the Laurent exponential and majorizing the remaining convolution coefficients by those of the nonnegative-coefficient Laurent exponential gives
\[
\sum_{j\in\mathbb Z}|p_j(t)|e^{(\log b+s)|j|}\le2e^{\alpha t}.\tag{1}
\]
For each \(n\), choose centered representatives \(I_n\) of the residue classes modulo \(n\), and form the (real) finite polynomial \(W_n(b,t)=\sum_{j\in I_n}P_j^{(n)}(t)b^j\). Every aliased integer \(j+\ell n\), with \(\ell\ne0\), has magnitude at least \(n/2\) and is no closer to zero than its representative. From (1), for every \(t>0\),
\[
\left|W_n(b,t)-e^{tq(b)}\right|
\le4\exp\bigl(\alpha t-sn/2\bigr).\tag{2}
\]
If \(e^{tQ_n}\) were entrywise nonnegative, then \(W_n(b,t)\ge P_0^{(n)}(t)\), since all the terms are nonnegative and the representative zero occurs exactly once.

There is a constant \(C_0>0\), depending only on the stencil, such that
\[
P_0^{(n)}(t)\ge \frac{C_0}{\sqrt t}
\qquad\bigl(1\le t\le cn,\ n\text{ sufficiently large}\bigr).\tag{3}
\]
Indeed \(q(\theta)\ge-C_1\theta^2\) on \([-\pi,\pi]\) because the real symmetric symbol is twice differentiable, vanishes at zero with zero derivative, and is otherwise negative. In the positive spectral formula \(P_0^{(n)}(t)=n^{-1}\sum_k e^{tq(2\pi k/n)}\), retain the \(\asymp n/\sqrt t\) frequencies of magnitude at most \(1/\sqrt t\); their multipliers are at least \(e^{-C_1}\). This proves (3) uniformly in the indicated range.

For \(1\le t\le cn\), (2) is bounded by \(4e^{-(s/2-c\alpha)n}\), whereas \(e^{tq(b)}\) decays exponentially in \(t\). Choose a fixed sufficiently large \(T\) and then large \(n\); for all \(T\le t\le cn\), the sum of these two quantities is strictly less than the lower bound (3). Thus the assumed entrywise nonnegativity contradicts \(W_n\ge P_0^{(n)}\).

For times \(0<t\le\delta\) with a fixed small \(\delta>0\), the distance-\(m\) entry satisfies \(P_m^{(n)}(t)=a_mt+O(t^2)<0\) uniformly for \(n\ge2m+1\): the uniform error follows from the uniform operator-norm bound \(\|Q_n\|\le\sum_j|a_j|\). On the compact intermediate interval \([\delta,T]\), step 1 supplies a negative infinite-lattice coefficient at each time; continuity, a finite subcover, and uniform convergence of the corresponding periodized coefficients on this compact interval make the finite-cycle kernel negative somewhere for all sufficiently large \(n\). Combining the three time intervals proves the asserted linear lower bound.

**4. Fully explicit constants for the five-point stencil.** For this stencil the symbol equals \(-A-A^2/12\) with \(A=2-2\cos\theta\), so the spectral assumption holds. Take \(b=16\), \(s=1/2\), \(c=1/500\). Direct rational evaluation gives
\[
q(16)=-\frac{2475}{1024}<0.
\]
Using \(e^{1/2}<2\), \(e<3\), and \(e^{-1/2},e^{-1}<1\),
\[
\alpha< -\frac52+\frac43\left(32+\frac1{16}\right)
+\frac1{12}\left(768+\frac1{256}\right)<105,
\quad \frac{105}{500}<\frac14=\frac s2.
\]
Thus (2) is at most \(4e^{-n/25}\) on \(0<t\le n/500\). The preceding steps yield \(\liminf H_n/n\ge1/500\), without requiring a numerical estimate for the first successful grid size.

For the upper bound, with \(d=\min(k,n-k)\), \(-q(2\pi k/n)\ge4\sin^2(\pi d/n)\ge16d^2/n^2\). Hence, at every \(t\ge n^2/16\),
\[
\sum_{k=1}^{n-1}e^{tq(2\pi k/n)}\le2\sum_{d\ge1}e^{-d^2}<1.
\]
The final strict inequality follows, for example, by bounding the tail \(d\ge2\) by \(e^{-4}/(1-e^{-2})\) and using \(e>8/3\). Each periodic matrix entry is the zero-mode contribution \(1/n\) plus a Fourier sum bounded in absolute value by the left-hand side divided by \(n\), proving strict positivity for all such times and \(H_n\le n^2/16\).

## Verification

The standalone script `artifacts/verify_signed_stencil.py` reproduces the five exact rational stencil coefficients, exact values of \(q(16)\) and the upper majorant \(\alpha<105\), and the strict inequality needed to obtain the \(1/500\) delay coefficient. It also checks finite Fourier eigenvalues, the periodic discrete heat kernel at multiple dimensions and times, explicit negative-kernel witnesses, eventual positive entries, and the distance-two short-time sign. It reports 3977 successful deterministic checks using only Python's standard library. These finite tests do not prove the infinite-coordinate sign statement or the uniform-in-dimension delay: both are established by the preceding analytic arguments.

## Relationship to prior work

Cross and Zhang [1, Section 2.2] display the classical fourth-order centered five-point discrete Laplacian as part of a discussion of **inverse-positive elliptic discretizations** and Bramble–Hubbard boundary closure. Inverse positivity of a stationary discrete Poisson solve is distinct from positivity of the continuous-time matrix exponential considered here. Hu and Zhang [2] develop positivity-preserving finite difference schemes for nonlinear and linear drift-diffusion settings under appropriate numerical conditions, rather than this periodic five-point-stencil semigroup problem.

Chen and collaborators [3] establish general spectral connections between signed graph Laplacians and eventual exponential positivity. Their qualitative finite-dimensional eventual-positivity criterion is consistent with, and covers the finite eventual-positivity portion here. It does not establish the **all-positive-time infinite-lattice alternating-sign phenomenon or the quantitative cycle-length lower bound** proved here. Earlier finite-range time stepping and lattice heat positivity results concern different spatial stencils or different time discretizations. Available mathematical record comparisons were performed at the claim and implication level, not merely by matching titles; their accessible claims do not entail the combined sign-and-delay statement. An equivalent specialized result in older finite-difference literature remains possible and is not ruled out by unsuccessful searches.

## Limitations

The sign-and-delay theorem requires a symmetric finite-range *translation-invariant* generator, strictly negative nonzero-frequency spectrum, and a negative outermost coupling. It does not apply to arbitrary variable-coefficient grids, Dirichlet boundary closures, or generic signed diffusion matrices. The explicit \(1/500\) constant is sufficient, not optimal; no sharp finite-cycle recovery time is claimed. The upper \(n^2/16\) estimate is also sufficient and may be far from sharp. Infinite-lattice sign changes occur at increasingly remote indices, so the theorem does not say fixed near-diagonal coefficients remain negative forever. All claims are in exact arithmetic and dimensionless semidiscrete time; they do not imply negativity of a convergent continuum solution at fixed macroscopic positions.

## References

1. L. J. Cross and X. Zhang, *On the monotonicity of Q3 spectral element method for Laplacian*, arXiv:2010.07282, first posted 2020-10-14, especially Section 2.2 (Bramble–Hubbard stencil), https://arxiv.org/html/2010.07282v3 .
2. J. Hu and X. Zhang, *Positivity-preserving and energy-dissipative finite difference schemes for the Fokker–Planck and Keller–Segel equations*, arXiv:2103.16790, first posted 2021-03-31, https://arxiv.org/abs/2103.16790 .
3. W. Chen, D. Wang, J. Liu, Y. Chen, S. Z. Khong, T. Başar, K. H. Johansson, L. Qiu, *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity*, arXiv:2009.03581, first posted 2020-09-08, especially its finite-dimensional eventual-positivity theorem, https://arxiv.org/abs/2009.03581 .
