# Sharp sixth-cumulant obstruction after fourth-cumulant cancellation in planar run-and-tumble transport

## Finding

**Theorem (exact cumulant rates and a sharp feasibility threshold).** A planar particle moves with constant speed \(v>0\) in its current orientation and turns at independent exponential times of rate \(\alpha>0\). Each turn adds an independent angle \(\Delta\) sampled from an arbitrary probability law symmetric under \(\Delta\mapsto-\Delta\). The initial orientation is uniform on the circle. An independent translational Brownian motion with diffusivity \(D\ge0\) is allowed. Let \(X_t\) denote the displacement projected onto any fixed axis, let \(m_j=\mathbb E[\cos(j\Delta)]\), and put

\[
a=\alpha(1-m_1),\qquad b=\alpha(1-m_2),\qquad c=\alpha(1-m_3).
\]

Assume \(a,b,c>0\). For the ordinary scalar cumulants \(\kappa_j(X_t)\), the three limits \(R_j=\lim_{t\to\infty}\kappa_j(X_t)/t\) exist for \(j=2,4,6\) and are

\[
\begin{aligned}
R_2&=2D+\frac{v^2}{a},\\
R_4&=\frac{3v^4(a-2b)}{a^3b},\\
R_6&=\frac{45v^6(a^3-a^2c-6abc+8b^2c)}{2a^5b^2c}.
\end{aligned}
\]

Write \(m=m_1\). Under the condition \(R_4=0\), necessarily and sufficiently \(m_2=(1+m)/2\), and such a turning law exists **exactly** for \(-3/4\le m<1\). Over all symmetric turning laws with these first two harmonics, the attainable third harmonic \(w=m_3\) is the *entire closed interval*

\[
\frac{9m^2+2m-3}{4(1+m)}\ \le\ w\ \le\ \frac{m+3}{4}.
\]

On this interval, \(R_6=90v^6(a-2c)/(a^5c)\), so its sign is precisely the sign of \(w-(1+m)/2\). Consequently:

- For \(-3/4\le m<-5/7\), every law with \(R_4=0\) has \(R_6>0\): simultaneous cancellation is impossible.
- At \(m=-5/7\), simultaneous \(R_4=R_6=0\) is possible only for the unique symmetric law putting probability \(3/7\) at angle \(\pi\) and \(2/7\) each at angles \(\pm2\pi/3\), modulo angle equivalence.
- For \(-5/7<m<1\), laws with \(R_4=0\) attain all three signs \(R_6<0\), \(R_6=0\), and \(R_6>0\).

Thus \(-5/7\) is the **sharp first-harmonic threshold** for suppressing both leading fourth- and sixth-order long-time non-Gaussian cumulants. Independent translational Brownian motion changes \(R_2\) but not either cancellation condition.

## Assumptions and scope

Take a rate-\(\alpha\) Poisson process, iid symmetric increments \(\Delta\in\mathbb R/(2\pi\mathbb Z)\), and a uniform independent \(\Theta_0\). Set \(\Theta_t=\Theta_0+\sum_{i\le N_t}\Delta_i\) modulo \(2\pi\), and define

\[
X_t=v\int_0^t\cos\Theta_s\,ds+\sqrt{2D}\,B_t,
\]

with an independent standard Brownian motion \(B_t\). All claims concern the ordinary one-dimensional projected-displacement cumulants, not radial cumulants. Turning distributions may have atoms; no positive density, global angular mixing gap, or Gaussian approximation is assumed. The strict conditions \(a,b,c>0\) are needed for the general rate formulas and hold automatically throughout the fourth-cancellation feasible family. Cumulant cancellation means only \(\lim_{t\to\infty}\kappa_j(X_t)/t=0\), not that the finite-time distribution or its cumulants are Gaussian.

## Proof

**1. Exact six-moment closure.** Let \(G_n(k,t)=\mathbb E[e^{kX_t+in\Theta_t}]\), for integer \(n\). The even turning law gives, with \(a_n=\alpha(1-m_n)\) and \(m_0=1\),

\[
\partial_tG_n=(-a_n+Dk^2)G_n+\frac{kv}{2}(G_{n-1}+G_{n+1}),\qquad G_n(k,0)=\mathbf1_{n=0}.
\]

The coefficient of \(k^j\) in \(G_0\) depends only on angular modes \(|n|\le\lfloor j/2\rfloor\): reaching mode \(n\) and returning to zero requires at least \(2|n|\) propulsion vertices. Therefore all derivatives through order six, for every finite time, are **exactly** those of the finite Fourier truncation \(|n|\le3\). This finite truncation at \(k=0\) has a simple zero eigenvalue, with remaining eigenvalues \(-a,-b,-c\), each twice. It has a simple analytic eigenvalue \(\lambda(k)\) near zero and an analytic nonvanishing overlap with the initial uniform state. Since the other finite-dimensional eigenvalues have negative real part there, logarithmic derivatives up to order six of \(G_0\) equal \(t\lambda^{(j)}(0)+O(1)\) as \(t\to\infty\). This argument does not require a spectral gap for unobserved high angular modes of the original turning law.

**2. Explicit dominant eigenvalue.** Set \(p=v^2k^2\) and temporarily \(D=0\). The symmetric cosine modes yield the scalar characteristic equation

\[
\lambda\left[(\lambda+a)\left((\lambda+b)(\lambda+c)-\frac p4\right)-\frac p4(\lambda+c)\right]
-\frac p2\left[(\lambda+b)(\lambda+c)-\frac p4\right]=0.
\]

Substitute \(\lambda=L_2p+L_4p^2+L_6p^3+O(p^4)\) and match the three coefficients. Exact polynomial division gives

\[
L_2=\frac1{2a},\qquad
L_4=\frac{a-2b}{8a^3b},\qquad
L_6=\frac{a^3-a^2c-6abc+8b^2c}{32a^5b^2c}.
\]

Multiplying by \(2!v^2\), \(4!v^4\), and \(6!v^6\) gives the three cumulant growth rates, except that the independent Brownian term \(Dk^2\) adds \(2D\) only to \(R_2\). In particular \(R_4=0\) iff \(b=a/2\). Substituting this into \(L_6\) gives \(R_6=90v^6(a-2c)/(a^5c)\).

**3. Sharp angular moment interval.** Let \(Y=\cos\Delta\in[-1,1]\). The fourth-cancellation constraint is \(\mathbb EY=m\) and \(\mathbb EY^2=q=(3+m)/4\), since \(\cos2\Delta=2Y^2-1\). The necessary variance inequality \(q\ge m^2\) becomes \((1-m)(4m+3)\ge0\), hence \(-3/4\le m<1\). Conversely these moment pairs are realizable.

For the third raw moment \(h=\mathbb EY^3\), the nonnegative polynomials \((1+Y)(Y-z)^2\) and \((1-Y)(Y-z)^2\), minimized over real \(z\), give

\[
\frac{(m+q)^2}{1+m}-q\ \le\ h\ \le\ q-\frac{(m-q)^2}{1-m}.
\]

These inequalities are *sufficient* as well as necessary. Equality on the left is realized by a two-point law supported at \(-1\) and \((m+q)/(1+m)=(5m+3)/(4(m+1))\). Equality on the right is realized by a two-point law supported at \(-3/4\) and \(1\), with positive weights chosen to give mean \(m\). Both laws have the same prescribed second moment \(q\); their mixtures realize every intermediate \(h\). Symmetrically lifting each atom \(Y=y\) to the two angles \(\Delta=\pm\arccos y\) constructs an admissible even angle law. Since \(m_3=4h-3m\), the claimed closed bounds for \(w=m_3\) follow.

**4. Classification and uniqueness.** Under \(b=a/2\) and \(c>0\), the sign of \(R_6\) is that of \(2w-1-m\). The upper feasible endpoint exceeds \((1+m)/2\) by exactly \((1-m)/4>0\). The lower endpoint satisfies

\[
w_{\min}-\frac{1+m}{2}=\frac{(m-1)(7m+5)}{4(1+m)}.
\]

It crosses zero exactly at \(m=-5/7\) inside the feasible interval. At this endpoint equality in the lower nonnegative-polynomial inequality forces \(Y\) to be supported on \(\{-1,-1/2\}\). The prescribed mean forces probabilities \(3/7\) and \(4/7\), respectively, and the even angle lift is unique. For \(m>-5/7\), mixing the two endpoint angle laws gives negative, zero or positive sixth cumulant growth as desired. No assertion about cancellation of higher cumulants follows.

## Verification

The standalone standard-library program `verification/verify.py` checks the cumulant-rate identities and fourth-cancellation conditions using exact rational arithmetic; reconstructs all endpoint turning laws and the sharp threshold law; independently expands the four-mode characteristic determinant through order six; compares truncated series against direct positive-root solutions; and integrates the exact finite-time Fourier moment hierarchy to check the opposing sixth-cumulant signs. Run `python3 verification/verify.py` from the package root. The observed result is `PASS: 271 exact algebraic, Fourier-generator and transient-ODE checks`. The continuum-time asymptotics and all-law classification come from the foregoing analytic argument, not from enumerating tests.

## Relationship to prior work

Britton, Zhang, Han and Bertrand (2026), arXiv:2608.23519, establish the arbitrary-turning Fourier hierarchy and develop systematic diagrammatic calculations of even spatial moments. Their Section 3.5 explicitly works through the fourth moment and states that still higher moments are accessible; the present result does not claim that hierarchy as new. Villa-Torrealba, Chávez-Raby, de Castro and Soto (2020), arXiv:2002.02872, already calculate the excess kurtosis for partial reorientation and are prior art for the fourth-order transport response. Jung (2023), arXiv:2308.00554, derives a general finite-harmonic rule for position moments. Santra, Basu and Sabhapandit (2022/2023), arXiv:2211.07337, derive an explicit sixth spatial moment (their equation (21)) as well as long-time corrections for the special case of uniform reorientation; that special case never satisfies the present fourth-rate cancellation equation. The present claim is narrower and different: the explicit general sixth-cumulant *linear rate* combined with a sharp, necessary-and-sufficient feasibility classification for jointly suppressing fourth and sixth rates. These prior methods are capable of supporting such a computation, but the inspected material did not supply its algebraic threshold or the unique equality law.

## Limitations

The result assumes Poisson turns, iid even angular increments, stationary uniform initial direction, fixed speed, and a planar noninteracting particle. It concerns projected-displacement cumulants and their terms linear in observation time. The no-go threshold is not a finite-time Gaussianity criterion or a claim about multibody transport. A general method for higher moments exists in prior literature, so unindexed explicit calculations and supplementary work remain a publication-priority risk; the analytic derivation and exact sign classification are supplied here independently. No independent external audit has been performed.

## References

1. C. Britton, Z. Zhang, S. Han and T. Bertrand, *Run-and-tumble particles with preferred reorientation*, first submitted 2026-08-24, arXiv:2608.23519, https://arxiv.org/abs/2608.23519.
2. A. Villa-Torrealba, C. Chávez-Raby, P. de Castro and R. Soto, *Run-and-tumble bacteria slowly approaching the diffusive regime*, first submitted 2020-02-07, arXiv:2002.02872, https://arxiv.org/abs/2002.02872; Phys. Rev. E 101, 062607 (2020).
3. Y. Jung, *Hyperdiffusion of Poissonian run-and-tumble particles in two dimensions*, first submitted 2023-08-01, arXiv:2308.00554, https://arxiv.org/abs/2308.00554.
4. I. Santra, U. Basu and S. Sabhapandit, *Long time behavior of run-and-tumble particles in two dimensions*, first submitted 2022-11-14, arXiv:2211.07337, https://arxiv.org/abs/2211.07337; J. Stat. Mech. (2023) 033203.
