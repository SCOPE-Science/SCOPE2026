# Identical spectral data and a sharp expansiveness transition for two-scale Jordan semigroups

## Finding
Let \(a,c,\beta,\gamma>0\), let \(\omega=a+c+1\), and let \(H=\bigoplus_{n=1}^{\infty}\mathbb C^2\) with the Hilbert direct-sum norm. Put
\[
N=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
G_\gamma=\bigoplus_{n\ge1}\left((i\omega+a n^{-\beta})I+c n^{-\gamma}N\right),\qquad T_\gamma(t)=e^{tG_\gamma}.
\]
The bounded generator is uniformly bounded below, \(\|G_\gamma z\|\ge\|z\|\). Every nonzero orbit of \(T_\gamma\) is unbounded, hence the semigroup is positively kinematically expansive, and no \(T_\gamma\) is uniformly exponentially expanding. Yet **Bowen–Walters positive expansiveness has the exact threshold**
\[
\boxed{T_\gamma\text{ is positively expansive}\quad\Longleftrightarrow\quad\gamma\ge\beta.}
\]
For fixed \(a,c,\beta\), the full, point and approximate-point spectra of the generator are independent of \(\gamma\):
\[
\sigma(G_\gamma)=\sigma_{\rm ap}(G_\gamma)=\{i\omega\}\cup\{i\omega+a n^{-\beta}:n\ge1\},\qquad
\sigma_{\rm p}(G_\gamma)=\{i\omega+a n^{-\beta}:n\ge1\}.
\]
For every \(t>0\), the analogous spectral sets of \(T_\gamma(t)\) are obtained by exponentiating the displayed sets and are also independent of \(\gamma\). Thus even all one-time spectra together do not determine positive expansiveness within this compact-perturbation family.

Write \(m_\gamma(t)=\inf_{\|z\|=1}\|T_\gamma(t)z\|\). Its complete large-time trichotomy is:

1. If \(0<\gamma<\beta\), put \(q=\gamma/\beta\). Then
\[
\boxed{m_\gamma(t)\sim \frac{a^q e^q}{c q^q}\,t^{-(1-q)}.}
\]
Every minimizing block index \(n_t\) for sufficiently large \(t\) satisfies \(n_t\sim(a t/q)^{1/\beta}\).
2. If \(\gamma=\beta\) and \(c\le2a\), then \(m_\gamma(t)=1\) for all \(t\ge0\). If \(\gamma=\beta\) and \(c>2a\), write \(r=2a/c\) and \(d=\sqrt{1-r^2}\). Then
\[
\boxed{\lim_{t\to\infty}m_\gamma(t)=\frac{r e^d}{1+d}\in(0,1).}
\]
3. If \(\gamma>\beta\), then \(m_\gamma(t)=1\) for all sufficiently large \(t\). In both cases \(\gamma\ge\beta\), \(\inf_{t\ge0}m_\gamma(t)>0\).

For example, at \(a=c=1\), \(\beta=2\), \(\omega=3\), changing the off-diagonal decay exponent from \(\gamma=1\) to \(\gamma=2\) preserves every generator and semigroup spectral set, while changing non-positive to positive Bowen–Walters expansiveness. In the first case \(m_1(t)\sim e^{1/2}\sqrt2\,t^{-1/2}\); in the second, \(m_2(t)=1\) for every nonnegative time.

## Assumptions and scope
All parameters \(a,c,\beta,\gamma\) are positive real numbers. The semigroup acts on the complex Hilbert space \(H\), with exactly two coordinates per positive integer. The standard nilpotent matrix \(N\) has \(N^2=0\). The term *positively expansive* uses the Bowen–Walters semigroup definition: for each \(\varepsilon>0\) some \(\delta>0\) ensures that
\[
\|T(t)x-T(s(t))y\|<\delta\|x\|\quad(t\ge0),
\]
for a continuous \(s:[0,\infty)\to[0,\infty)\) with \(s(0)=0\), implies \(y=T(u)x\) or \(x=T(u)y\) for some \(u\in[0,\varepsilon)\). The negative construction below even uses increasing homeomorphisms \(s\). Positive kinematic expansiveness restricts to \(s(t)=t\). Uniform exponential expansion means \(m_\gamma(t)\ge M e^{\eta t}\) for some \(M,\eta>0\) and every \(t\ge0\).

## Proof
**1. Exact blocks and spectra.** The generator is bounded because \(\|a n^{-\beta}I+c n^{-\gamma}N\|\le a+c\); the reverse triangle inequality gives \(\|G_\gamma z\|\ge(\omega-a-c)\|z\|=\|z\|\). The block exponential is exactly
\[
T_{\gamma,n}(t)=e^{(i\omega+a n^{-\beta})t}\begin{pmatrix}1&c t n^{-\gamma}\\0&1\end{pmatrix}.
\]
The operator \(G_\gamma-i\omega I\) is compact, since it is a direct sum of finite matrices with norms tending to zero. Its nonzero spectrum consists precisely of the eigenvalues \(a n^{-\beta}\), while zero belongs to its approximate point spectrum by coordinate vectors but not to its point spectrum. Exponentiation gives the stated semigroup spectra, including the point and approximate-point sets. All of these are independent of \(\gamma\). Each nonzero vector has a nonzero finite block; on that block the factor \(e^{a t n^{-\beta}}\) dominates the degree-one polynomial, so its orbit norm tends to infinity. Huynh's orbit characterization (Theorem 3.3 in [1]) yields positive kinematic expansiveness. As \(n\to\infty\), each fixed-time block tends to \(e^{i\omega t}I\), so \(m_\gamma(t)\le1\) for every \(t\) and uniform exponential expansion is impossible.

**2. Minimum modulus.** A shear \(J(u)=\left(\begin{smallmatrix}1&u\\0&1\end{smallmatrix}\right)\) with \(u\ge0\) has smallest singular value
\[
\mu(u)=\frac{\sqrt{u^2+4}-u}{2}=\frac{2}{\sqrt{u^2+4}+u}.
\]
Therefore the exact infinite-dimensional identity is
\[
 m_\gamma(t)=\inf_{n\ge1} e^{a t n^{-\beta}}\mu(c t n^{-\gamma}). \tag{1}
\]
For \(\gamma<\beta\), set \(q=\gamma/\beta\in(0,1)\), \(\theta=1-q\), and \(x_n=a t n^{-\beta}\). Equation (1) becomes the infimum of
\[
F_t(x_n)=e^{x_n}\mu(c a^{-q}t^\theta x_n^q).
\]
Since \(\mu(u)\sim u^{-1}\) as \(u\to\infty\), uniformly on compact subsets of \((0,\infty)\),
\[
 t^\theta F_t(x)\longrightarrow \frac{a^q}{c}e^x x^{-q}.
\]
There is no loss of minimizers at zero or infinity: \(\mu(u)\ge(1+u)^{-1}\) gives
\[
t^\theta F_t(x)\ge\frac{e^x}{t^{-\theta}+c a^{-q}x^q},
\]
which diverges uniformly as \(x\to0\) or \(x\to\infty\), once \(t\) is large. The limiting profile has the unique minimizer \(x=q\), with value \(a^q e^q/(c q^q)\). The mesh \(x_n=a t n^{-\beta}\) has points converging to \(q\) with spacing tending to zero, by taking \(n\) nearest \((a t/q)^{1/\beta}\). Compactness of minimizing \(x_n\) and uniqueness of the continuous minimizer prove both the sharp equivalent and the minimizing-index localization.

For \(\gamma=\beta\), equation (1) samples \(f(x)=e^{a x}\mu(c x)\) at \(x=t n^{-\beta}\). Its logarithmic derivative is
\[
\frac{f'(x)}{f(x)}=a-\frac{c}{\sqrt{c^2x^2+4}}.
\]
If \(c\le2a\), this is nonnegative and \(\inf_{x\ge0}f(x)=1\); since \(n\to\infty\) gives \(x\to0\), (1) equals one at every time. If \(c>2a\), the unique minimizer is \(x_*=(2/c)\sqrt{1-r^2}/r\), and direct substitution gives \(f(x_*)=r e^d/(1+d)\). The sampling mesh approaches \(x_*\) as \(t\to\infty\), so the infimum tends to this strictly positive limit and is always at least this limit.

For \(\gamma>\beta\), the block generator's Hermitian part is positive semidefinite whenever \(c n^{-\gamma}\le2a n^{-\beta}\), giving a block minimum modulus at least one at all times. Only finitely many indices violate this inequality. On each exceptional fixed block, \(e^{a t n^{-\beta}}\mu(c t n^{-\gamma})\to\infty\) as \(t\to\infty\); hence all finite exceptions also have minimum modulus at least one after a common finite time. The infimum is exactly one because blocks tend to scalar rotations as \(n\to\infty\). Its infimum over all times is positive because each of the finitely many exceptional block-modulus functions is continuous, positive and grows at infinity.

**3. Positive-expansive branch.** If \(\gamma\ge\beta\), the preceding estimates yield a uniform positive lower bound \(m_\gamma(t)\ge m_0>0\). Every nonzero orbit is unbounded and the generator is bounded below by one. These are exactly the three hypotheses of Huynh's proved positive-expansiveness criterion, Theorem 5.1 in [1], including its short-time displacement lemma. Thus \(T_\gamma\) is positively expansive.

**4. Failure below the threshold.** Let \(\gamma<\beta\), \(q=\gamma/\beta\), \(\tau=2\pi/\omega\), and
\[
t_n=\frac{q}{a}n^\beta,\quad u_n=c n^{-\gamma}t_n=\frac{cq}{a}n^{\beta-\gamma}\to\infty.
\]
In the \(n\)-th block define the unit vector \(x_n=(-u_n,1)/\sqrt{1+u_n^2}\) and \(y_n=T_\gamma(-\tau)x_n\); the inverse-time operator exists because \(G_\gamma\) is bounded. Use the increasing homeomorphism
\[
s_n(t)=\begin{cases}
t,&0\le t\le t_n-\tau,\\
2t-t_n+\tau,&t_n-\tau\le t\le t_n,\\
t+\tau,&t\ge t_n.
\end{cases}
\]
This is well-defined for sufficiently large \(n\). Within the active block,
\[
\|T_\gamma(t)x_n\|=e^{a t n^{-\beta}}
\frac{\sqrt{1+c^2 n^{-2\gamma}(t-t_n)^2}}{\sqrt{1+u_n^2}}.
\]
It is at most \(e^q\) on \([0,t_n]\) and tends uniformly to zero on \([t_n-2\tau,t_n]\). The phase choice \(e^{-i\omega\tau}=1\) implies \(\|(I-T_\gamma(-\tau))|_{\mathbb C^2_n}\|=O(n^{-\beta}+n^{-\gamma})\). Hence on \([0,t_n-\tau]\) the discrepancy \(\|T_\gamma(t)x_n-T_\gamma(s_n(t))y_n\|\) is \(O(n^{-\beta}+n^{-\gamma})\). On the transition interval it tends uniformly to zero by the displayed short norm bound. For \(t\ge t_n\) it is exactly zero, since \(s_n(t)-\tau=t\). Consequently
\[
\sup_{t\ge0}\|T_\gamma(t)x_n-T_\gamma(s_n(t))y_n\|\longrightarrow0.
\]
But if \(x_n=T_\gamma(v)y_n\), then \(T_\gamma(v-\tau)x_n=x_n\); the only real \(v\) for which a nonzero vector in this block is fixed is \(v=\tau\), because its exponential eigenvalue has modulus \(e^{a n^{-\beta}(v-\tau)}\). The reverse relation \(y_n=T_\gamma(v)x_n\) is impossible for \(v\ge0\). Thus no orbit relation holds with \(v<\tau/2\), contradicting Bowen–Walters expansiveness for every proposed closeness constant. This proves the negative branch without relying on any asymptotic experiment.

## Verification
The exact block identity, spectral calculation, closed-form shear singular value, one-variable saddle point and reparametrization witness prove the infinite-dimensional assertions. The standalone `checker.py` uses only the Python standard library and returned `CHECKS_OK 130 finite assertions`. Checks include the shear singular-value trace/determinant identities, subcritical asymptotic constants and block localization, critical plateau values, supercritical block inequalities, and explicit discrepancy bounds for the non-expansiveness witness. For \(a=c=1\), \(\beta=2\), \(\gamma=1\), the predicted asymptotic coefficient is approximately \(2.331643981597124\); a critical example \(a=1,c=3,\beta=\gamma\) has limiting lower modulus approximately \(0.8048755115018571\). Numerical checks are finite diagnostics only.

## Relationship to prior work
Huynh [1, Theorem 3.3] identifies positive kinematic expansiveness with unbounded orbits and [1, Theorem 5.1] gives positive expansiveness under a uniform lower bound plus boundedness below of the generator. Its Corollary 5.4 treats diagonal semigroups. This finding uses the positive direction of that theorem, while adding the opposite nonnormal Jordan branch, its explicit reparametrization obstruction, identical spectral data across distinct dynamical regimes, and exact transient minimum-modulus constants. Lee and Morales [2] introduced the semigroup Bowen–Walters property and established necessary generator restrictions, but these do not distinguish the present families: all their generator eigenvalues have positive real parts and each generator is bounded below. Unlike a diagonal family, the nilpotent coupling changes expansiveness without changing any spectral set.

## Limitations
The result is confined to bounded two-dimensional Jordan-block direct sums with the specified power-law diagonal and coupling sequences; it is not a universal characterization of all nonnormal semigroups. It establishes spectral-set equality, not similarity or equality of pseudospectra. The lower-modulus trichotomy is asymptotic, except where exact equality is expressly given. The external 2022 semigroup source [2] was accessible in abstract form but not full text, leaving a bibliographic priority risk; the 2026 paper's relevant proofs and statements were inspected directly.

## References
[1] H. M. Huynh, *Positive expansiveness of operator semigroups: orbit growth and spectral criteria*, arXiv:2611.01005v1, publicly posted 31 October 2026. https://arxiv.org/html/2611.01005

[2] J. Lee and C. A. Morales, *Bowen–Walters expansiveness for semigroups of linear operators*, Ergodic Theory Dynam. Systems 43 (2023), 1942–1951; first published online 18 April 2022. https://doi.org/10.1017/etds.2022.20
