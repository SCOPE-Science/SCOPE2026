# Exact reflected-density crossing for standardized lognormal laws
## Finding
Let \(X\sim\operatorname{LogNormal}(\mu,\sigma^2)\) with \(\sigma>0\), and standardize about the arithmetic mean:
\[
Z=\frac{X-\mathbb EX}{\sqrt{\operatorname{Var}(X)}}.
\]
Write \(g_\sigma\) for the density of \(Z\) and
\[
c_\sigma=\sqrt{e^{\sigma^2}-1}.
\]
The common support on which both \(g_\sigma(z)\) and \(g_\sigma(-z)\) are positive is
\[
0<z<c_\sigma^{-1}.
\]
On that interval,
\[
\log\frac{g_\sigma(z)}{g_\sigma(-z)}
=
\operatorname{artanh}(c_\sigma z)
\left(
-3-\frac{\log(1-c_\sigma^2z^2)}{\sigma^2}
\right).
\]
Consequently there is exactly one crossing,
\[
\kappa_\sigma
=
\sqrt{e^{-\sigma^2}+e^{-2\sigma^2}+e^{-3\sigma^2}},
\]
and
\[
g_\sigma(z)<g_\sigma(-z)\quad\text{for }0<z<\kappa_\sigma,
\]
while
\[
g_\sigma(z)>g_\sigma(-z)\quad\text{for }\kappa_\sigma<z<c_\sigma^{-1}.
\]
The function \(\sigma\mapsto\kappa_\sigma\) is strictly decreasing,
\[
\kappa_\sigma\longrightarrow\sqrt3\quad(\sigma\downarrow0),
\qquad
\kappa_\sigma\sim e^{-\sigma^2/2}\quad(\sigma\to\infty).
\]
There is a unique one-standard-deviation transition:
\[
\kappa_\sigma=1
\iff
\sigma=\sigma_\star=0.78062658386453\ldots,
\]
where \(q=e^{-\sigma_\star^2}\) is the unique root in \((0,1)\) of
\[
q+q^2+q^3=1.
\]

## Assumptions and scope
The result concerns an ordinary one-dimensional lognormal law with arbitrary real log-location \(\mu\) and positive log-scale \(\sigma\). The log-location cancels after standardization. The reflected comparison is made only where both reflected points belong to the standardized support, namely \(0<z<c_\sigma^{-1}\). No claim is made about mixtures, shifted lognormal laws, or multivariate lognormal distributions.

## Proof
Let \(s=\sigma^2\). The mean and standard deviation of \(X\) are
\[
m=e^{\mu+s/2},
\qquad
d=m\sqrt{e^s-1}=mc_\sigma.
\]
For \(0<z<c_\sigma^{-1}\), put \(u=c_\sigma z\), so \(0<u<1\). The two reflected original-scale points are
\[
x_+=m(1+u),
\qquad
x_-=m(1-u).
\]
Since the standardized density is \(g_\sigma(z)=d f_X(m+dz)\), the Jacobian factor \(d\) cancels in the reflected ratio. For the lognormal density,
\[
\log x_\pm-\mu=\frac{s}{2}+\log(1\pm u).
\]
Therefore
\[
\log\frac{g_\sigma(z)}{g_\sigma(-z)}
=
-\log\frac{1+u}{1-u}
-
\frac{
\left(\frac{s}{2}+\log(1+u)\right)^2
-
\left(\frac{s}{2}+\log(1-u)\right)^2
}{2s}.
\]
Using
\[
\log\frac{1+u}{1-u}=2\operatorname{artanh}(u)
\]
and
\[
\log(1+u)+\log(1-u)=\log(1-u^2),
\]
this simplifies exactly to
\[
\log\frac{g_\sigma(z)}{g_\sigma(-z)}
=
\operatorname{artanh}(u)
\left(
-3-\frac{\log(1-u^2)}{s}
\right).
\]
Because \(\operatorname{artanh}(u)>0\), the sign is controlled by
\[
h_s(u)=-3-\frac{\log(1-u^2)}{s}.
\]
This function is strictly increasing on \((0,1)\), with \(h_s(0+)=-3\) and \(h_s(1-)=+\infty\). Hence it has one zero, determined by
\[
1-u^2=e^{-3s},
\qquad
u_\star=\sqrt{1-e^{-3s}}.
\]
Thus
\[
\kappa_\sigma^2
=
\frac{1-e^{-3s}}{e^s-1}
=
e^{-s}+e^{-2s}+e^{-3s},
\]
which proves the crossing formula and both sign statements.

Strict monotonicity follows immediately because
\[
\frac{d}{ds}\kappa_\sigma^2
=
-e^{-s}-2e^{-2s}-3e^{-3s}<0.
\]
The endpoint limits follow from this closed form. Finally, \(\kappa_\sigma=1\) is equivalent to
\[
q+q^2+q^3=1,
\qquad
q=e^{-\sigma^2}\in(0,1).
\]
The left side is strictly increasing in \(q\), so the root and therefore \(\sigma_\star\) are unique.

## Verification
The analytic proof establishes the result for every \(\sigma>0\). The bundled script `verify_lognormal_reflection.py` independently evaluates the original lognormal density and the closed reflected-ratio formula at representative shape values, checks the crossing sign on both sides, verifies the one-standard-deviation root numerically, and checks monotonicity on a deterministic mesh. Its successful output is:
`VERIFY_OK sigma_star=0.780626583864530 q=0.543689012692076`.
These finite checks are regression checks only; they are not used to justify uniqueness or the all-\(\sigma\) theorem.

## Relationship to prior work
Hu, Song and Tan study standardized anti-concentration for familiar distribution families. Their lognormal Proposition 3.8 proves that, for every fixed standardized threshold, the infimum over lognormal parameters is zero. The proof uses the exact lognormal mean and variance and then sends the log-scale to infinity through a one-sided Gaussian tail. It does not compare densities at reflected standardized points, state a reflected-density crossing, or identify the exact radius \(\kappa_\sigma\).

A separate previously obtained endpoint result gives the large-\(\sigma\) asymptotic of a standardized lognormal tail probability. That tail asymptotic neither implies nor is implied by the present exact finite-\(\sigma\) density-ratio identity: one concerns integrated probability in a degeneration limit, while the other gives the local reflected-density geometry for every positive shape.

Targeted searches for reflected lognormal densities, symmetric points about the arithmetic mean, the exact expression \(e^{-\sigma^2}+e^{-2\sigma^2}+e^{-3\sigma^2}\), and the numerical threshold \(0.78062658386453\ldots\) found no covering statement.

## Limitations
The formula is elementary once the correct standardized reflected comparison is posed, so an older equivalent identity may exist under terminology from applied lognormal modeling that was not retrieved. The theorem concerns density asymmetry about the arithmetic mean; it does not determine a global anti-concentration optimum, a stochastic order, or an extremal statement over distributions beyond the lognormal family.

## References
Hu, Z.-C., Song, R., and Tan, Y., *On the anti-concentration functions of some familiar families of distributions*, arXiv:2401.09998v1, 2024. The first public version was submitted on 2024-01-18; the paper lists MSC \(60E07,60E15\). Proposition 3.8 treats the lognormal family.
