# Sharp large-noise median asymptotics for variance-gamma laws

## Result

Let
\[
V_{r,\theta,\sigma}\sim \operatorname{VG}(r,\theta,\sigma,0),
\qquad r>0,\quad \theta>0,\quad \sigma>0,
\]
in the parameterization
\[
f(x)=\frac{e^{\theta x/\sigma^2}}{\sigma\sqrt\pi\,\Gamma(r/2)}
\left(\frac{|x|}{2\sqrt{\theta^2+\sigma^2}}\right)^{(r-1)/2}
K_{(r-1)/2}\!\left(\frac{\sqrt{\theta^2+\sigma^2}}{\sigma^2}|x|\right).
\]
Write \(M_{r,\theta,\sigma}=\operatorname{Med}(V_{r,\theta,\sigma})\).  Gaunt--Ouimet proved that, as \(\sigma\to\infty\),
\[
M_{r,\theta,\sigma}\longrightarrow
\begin{cases}
0,&0<r\le 1,\\
(r-1)\theta,&r>1.
\end{cases}
\]
The convergence has the following sharp first-order asymptotics.

### Theorem

As \(\sigma/\theta\to\infty\):

1. If \(0<r<1\), then
\[
M_{r,\theta,\sigma}
\sim C_r\,\theta^{1/r}\sigma^{-(1-r)/r},
\]
where
\[
C_r=
\left[
\frac{r2^r\Gamma((r+1)/2)}{\Gamma((1-r)/2)}
\right]^{1/r}.
\]

2. If \(r=1\), then, with \(\gamma_E\) the Euler--Mascheroni constant,
\[
M_{1,\theta,\sigma}
=
\frac{\theta}{
\log(\sigma/\theta)+\log\!\bigl(2\log(\sigma/\theta)\bigr)+1-\gamma_E+o(1)}.
\]
In particular, \(M_{1,\theta,\sigma}\sim\theta/\log(\sigma/\theta)\).

3. If \(1<r<3\), then
\[
M_{r,\theta,\sigma}
=(r-1)\theta+A_r\theta^r\sigma^{-(r-1)}
+o\!\left(\sigma^{-(r-1)}\right),
\]
where
\[
A_r=
\frac{2}{r}
\left(\frac{r-1}{2}\right)^{r-1}
\frac{\Gamma((3-r)/2)}{\Gamma((r-1)/2)}.
\]

4. If \(r=3\), then
\[
M_{3,\theta,\sigma}
=2\theta+\frac{2}{3}\frac{\theta^3}{\sigma^2}
\log\!\left(\frac{\sigma^2}{\theta^2}\right)
+o\!\left(\frac{\theta^3}{\sigma^2}
\log\!\frac{\sigma^2}{\theta^2}\right).
\]

5. If \(r>3\), then
\[
M_{r,\theta,\sigma}
=(r-1)\theta+
\frac{2(r-1)}{3(r-3)}\frac{\theta^3}{\sigma^2}
+o(\sigma^{-2}).
\]

Thus the large-noise median exhibits two genuine shape transitions: the density-singularity threshold \(r=1\), where the polynomial law turns into a reciprocal logarithm, and the Bessel regularity threshold \(r=3\), where the correction changes from \(\sigma^{-(r-1)}\) to \(\sigma^{-2}\) through a \(\sigma^{-2}\log\sigma\) critical law.

## Proof

By the gamma-difference representation used by Gaunt--Ouimet,
\[
V_{r,\theta,\sigma}\stackrel d=
\theta\bigl[(a+1)Y_1-(a-1)Y_2\bigr],
\qquad
a=\sqrt{1+\kappa},\quad
\kappa=\frac{\sigma^2}{\theta^2},
\]
where \(Y_1,Y_2\) are independent \(\Gamma(s,1)\) variables and \(s=r/2\).  Hence it is enough to take \(\theta=1\), determine the normalized median \(m_r(\kappa)\), and multiply by \(\theta\) at the end.

### 1. The exact probability deficit at zero

Beta--gamma algebra gives
\[
\frac{Y_1}{Y_1+Y_2}\sim\operatorname{Beta}(s,s).
\]
Therefore
\[
F_\kappa(0)
=I_{1/2-1/(2a)}(s,s),
\]
and the positive probability mass that must be accumulated between \(0\) and the median is
\[
H_\kappa:=\frac12-F_\kappa(0).
\]
Expanding the symmetric beta density at \(1/2\) gives
\[
H_\kappa
=h_s\kappa^{-1/2}
\left[1-\frac{2s+1}{6\kappa}+O(\kappa^{-2})\right],
\qquad
h_s=\frac{\Gamma(s+1/2)}{\sqrt\pi\,\Gamma(s)}.
\tag{1}
\]
The median is characterized by
\[
\int_0^{m_r(\kappa)}f_\kappa(x)\,dx=H_\kappa.
\tag{2}
\]

For \(\theta=1\), the positive-half density is
\[
f_\kappa(x)=
\frac{e^{x/\kappa}}{\sqrt\kappa\sqrt\pi\,\Gamma(s)}
\left(\frac{x}{2\sqrt{1+\kappa}}\right)^{s-1/2}
K_{s-1/2}\!\left(\frac{x\sqrt{1+\kappa}}{\kappa}\right).
\tag{3}
\]
All remaining statements follow from the standard small-argument expansions of \(K_\nu\).

### 2. The singular regime \(0<r<1\)

Put \(\mu=(1-r)/2=1/2-s>0\).  Since \(K_{-\mu}=K_\mu\) and
\[
K_\mu(z)\sim 2^{\mu-1}\Gamma(\mu)z^{-\mu},
\qquad z\downarrow0,
\]
formula (3), uniformly on the shrinking median interval, yields
\[
f_\kappa(x)
\sim c_s\kappa^{-s}x^{2s-1},
\qquad
c_s=2^{-2s}\frac{\Gamma(1/2-s)}{\sqrt\pi\,\Gamma(s)}.
\tag{4}
\]
Gaunt--Ouimet already give \(m_r(\kappa)\to0\), so (4) can be integrated in (2).  Using (1),
\[
\frac{c_s}{2s}\kappa^{-s}m_r(\kappa)^{2s}
\sim h_s\kappa^{-1/2}.
\]
Since \(2s=r\), this is exactly
\[
m_r(\kappa)
\sim C_r\kappa^{-(1-r)/(2r)}.
\tag{5}
\]
Rescaling \(\kappa=(\sigma/\theta)^2\) gives part 1.

### 3. The critical singularity \(r=1\)

Now \(s=1/2\) and (3) becomes
\[
f_\kappa(x)=\frac{e^{x/\kappa}}{\pi\sqrt\kappa}
K_0\!\left(\frac{x\sqrt{1+\kappa}}{\kappa}\right).
\]
From (1), \(\pi\sqrt\kappa H_\kappa=1+O(\kappa^{-1})\).  The expansion
\[
K_0(z)=-\log(z/2)-\gamma_E+O(z^2|\log z|)
\]
and \(m_1(\kappa)\to0\) imply from (2)
\[
m_1(\kappa)
\left[
\log\frac{2\sqrt\kappa}{m_1(\kappa)}+1-\gamma_E+o(1)
\right]
=1+O(\kappa^{-1}).
\tag{6}
\]
Writing \(y_\kappa=1/m_1(\kappa)\), first (6) gives \(y_\kappa\sim\tfrac12\log\kappa\), and then one substitution back into (6) gives
\[
y_\kappa
=\frac12\log\kappa+\log\log\kappa+1-\gamma_E+o(1).
\tag{7}
\]
This is part 2 after rescaling.

### 4. The finite nonzero limit \(r>1\)

Put
\[
\nu=\frac{r-1}{2}>0.
\]
The leading small-argument term in (3) is constant in \(x\):
\[
f_\kappa(x)
=d_\nu\kappa^{-1/2}(1+o(1)),
\qquad
d_\nu=\frac{\Gamma(\nu)}{2\sqrt\pi\,\Gamma(\nu+1/2)}.
\tag{8}
\]
Moreover \(h_s/d_\nu=2\nu=r-1\), recovering the Gaunt--Ouimet limit.

#### 4a. \(0<\nu<1\), equivalently \(1<r<3\)

The second branch of the Bessel expansion gives, uniformly on fixed compact \(x\)-intervals,
\[
f_\kappa(x)=d_\nu\kappa^{-1/2}
\left[1+B_\nu x^{2\nu}\kappa^{-\nu}+o(\kappa^{-\nu})\right],
\tag{9}
\]
where
\[
B_\nu=2^{-2\nu}\frac{\Gamma(-\nu)}{\Gamma(\nu)}<0.
\]
The \(O(\kappa^{-1})\) term in (1) is smaller than \(\kappa^{-\nu}\).  Substituting
\(m_r(\kappa)=2\nu+c\kappa^{-\nu}+o(\kappa^{-\nu})\) into (2) and (9) gives
\[
c=-B_\nu\frac{(2\nu)^{2\nu+1}}{2\nu+1}
=\frac{2\nu^{2\nu}\Gamma(1-\nu)}{(2\nu+1)\Gamma(\nu)}.
\tag{10}
\]
This is the stated \(A_r\).

#### 4b. \(\nu=1\), equivalently \(r=3\)

Here
\[
zK_1(z)=1+\frac{z^2}{2}
\left(\log(z/2)+\gamma_E-\frac12\right)
+O(z^4|\log z|).
\]
The unique logarithmically enhanced term in (3) is therefore
\[
f_\kappa(x)=d_1\kappa^{-1/2}
\left[1-\frac{x^2}{4\kappa}\log\kappa+O(\kappa^{-1})\right]
\tag{11}
\]
uniformly on fixed compact intervals.  Since the leading median is \(2\), integration of the correction over \([0,2]\) contributes
\[
-\frac{\log\kappa}{4\kappa}\int_0^2x^2\,dx
=-\frac{2}{3}\frac{\log\kappa}{\kappa}.
\]
Equation (2) therefore forces
\[
m_3(\kappa)=2+\frac{2}{3}\frac{\log\kappa}{\kappa}
+o\!\left(\frac{\log\kappa}{\kappa}\right).
\tag{12}
\]

#### 4c. \(\nu>1\), equivalently \(r>3\)

The nonanalytic Bessel branch is now \(o(\kappa^{-1})\).  The regular branch gives
\[
f_\kappa(x)=d_\nu\kappa^{-1/2}
\left[1+\frac{A_\nu(x)}{\kappa}+o(\kappa^{-1})\right],
\tag{13}
\]
where
\[
A_\nu(x)=-\nu+x+\frac{x^2}{4(1-\nu)}.
\]
From (1),
\[
H_\kappa=h_s\kappa^{-1/2}
\left[1-\frac{\nu+1}{3\kappa}+o(\kappa^{-1})\right].
\tag{14}
\]
Because
\[
\int_0^{2\nu}A_\nu(x)\,dx
=-\frac{2\nu^3}{3(\nu-1)},
\]
substituting \(m_r(\kappa)=2\nu+c/\kappa+o(\kappa^{-1})\) into (2), (13), and (14) yields
\[
c=\frac{2\nu}{3(\nu-1)}.
\tag{15}
\]
This is part 5.  The same calculation also shows directly why the coefficient diverges as \(r\downarrow3\): exactly at \(r=3\), the regular \(z^2\) Bessel coefficient is replaced by the logarithmic term in (11).

## Consistency check at the asymmetric Laplace case

For \(r=2\), the exact median is known:
\[
M_{2,\theta,\sigma}
=(\theta+\sqrt{\theta^2+\sigma^2})
\log\!\left(1+\frac{\theta}{\sqrt{\theta^2+\sigma^2}}\right).
\]
Its large-\(\sigma\) expansion is
\[
M_{2,\theta,\sigma}
=\theta+\frac12\frac{\theta^2}{\sigma}+o(\sigma^{-1}),
\]
which agrees with part 3 because \(A_2=1/2\).

## Numerical verification

`artifacts/verify_asymptotics.py` computes the exact beta probability deficit at zero, numerically integrates the Bessel density, solves for the median, and compares against the five asymptotic formulas.  The output in `artifacts/verification_output.txt` shows convergence of the correction ratios to one across all five regimes and reproduces the exact \(r=2\) formula to about \(10^{-13}\) in the reported check.  The slowest visible convergence occurs at the two logarithmic critical values \(r=1\) and \(r=3\), as expected.

## Relation to prior work and originality boundary

Gaunt and Merkle (2021) formulated the variance-gamma median monotonicity and limiting-value conjectures.  Gaunt and Ouimet (2026) proved the monotonicity and established the large-\(\sigma\) limit \(0\vee(r-1)\theta\); their proof identifies the limiting value but does not state a convergence-rate expansion.  Fischer, Gaunt and Sarantsev (2025) review the VG density, its small-\(x\) singularity transition at \(r=1\), and the exact \(r=2\) median.  Standard small-argument expansions of \(K_\nu\) are classical.

The originality claim here is therefore deliberately narrow: to the best of our knowledge, the five-regime sharp large-noise median expansion above, including the reciprocal-log law at \(r=1\), the \(\sigma^{-(r-1)}\) coefficient for \(1<r<3\), the \(\sigma^{-2}\log\sigma\) law at \(r=3\), and the explicit \(\sigma^{-2}\) coefficient for \(r>3\), has not previously been stated.  Searches used the equivalent terms variance-gamma, generalized asymmetric Laplace, generalized Laplace, Bessel-function distribution, median/quantile, large scale/noise/dispersion, and the special values \(r=1,2,3\).  The 2025 review and the relevant theorem/proof in the 2026 median paper were inspected directly.

A residual originality risk remains in older generalized asymmetric-Laplace literature, especially the book by Kotz, Kozubowski and Podgorski (2001), whose full text was not exhaustively checked here.  The 2025 review is a strong mitigating source because it was written to consolidate VG distributional theory and its median section reports only the symmetric and \(r=2\) exact formulas together with the then-conjectural general bounds.

## Limitations

- The expansion is pointwise in fixed \(r>0\); no uniform result is claimed as \(r\) approaches 1 or 3 with \(\sigma\).
- Only fixed \(\theta>0\) with \(\sigma/\theta\to\infty\) is treated.  Negative \(\theta\) follows by reflection, while joint parameter scalings may have different crossover laws.
- No explicit remainder bound or quantitative error constant is proved.
- The result concerns the variance-gamma subfamily, not general generalized-hyperbolic medians.
- Numerical checks support but do not replace the analytic proof.

## References

1. R. E. Gaunt and F. Ouimet, *Bounds for the median of the generalized hyperbolic and related distributions*, arXiv:2609.20212 (2026).
2. R. E. Gaunt and M. Merkle, *On bounds for the mode and median of the generalized hyperbolic and related distributions*, J. Math. Anal. Appl. 493 (2021), 124508; arXiv:2002.01884.
3. A. Fischer, R. E. Gaunt and A. Sarantsev, *The Variance-Gamma Distribution: A Review*, Statistical Science 40 (2025), 235--258, doi:10.1214/24-STS929.
4. T. J. Kozubowski, S. Mazur and K. Podgorski, *The Laplace Distribution and Generalizations: A Revisit with Applications to Communications, Economics, Engineering, and Finance*, Birkhauser, 2001.
5. NIST Digital Library of Mathematical Functions, Chapter 10, especially Sections 10.30--10.31 (small-argument expansions of modified Bessel functions).
