# A sharp three-habitat recovery-site reversal with logarithmic critical delay

## Finding

In an idealized linear population occupying a three-habitat corridor, a release at the habitat with the greater local growth rate can produce a larger total population at every short horizon, yet a release one habitat farther along the corridor can produce a larger total at every sufficiently long horizon. There is **at most one** such reversal. The reversal exists precisely above an explicit threshold in the third habitat's intrinsic growth rate. At the threshold, the eventual reversal time diverges logarithmically.

More precisely, let \(m>0\), \(r_1>r_2\), and \(r_3\in\mathbb R\), and define \(\Delta=r_1-r_2>0\) and
\[
r_3^*=r_1+\frac{m\Delta}{m+\Delta}.
\]
The number of individuals at time \(t\) resulting from one individual released at site \(i\), summed across all three habitats, is \(F_i(t)\), as defined below. If \(r_3\le r_3^*\), then \(F_1(t)>F_2(t)\) for all \(t>0\). If \(r_3>r_3^*\), there is a unique \(t_*>0\) such that \(F_1(t)>F_2(t)\) for \(0<t<t_*\), \(F_1(t_*)=F_2(t_*)\), and \(F_1(t)<F_2(t)\) for \(t>t_*\). The crossing is simple. No such reversal can occur on a two-habitat undirected corridor with conservative symmetric movement and unequal local growth rates.

An additional quantitative conclusion describes a near-threshold effect. For \(r_3=r_3^*+\varepsilon\) with \(\varepsilon\downarrow0\), let \(\lambda_1^*=r_1>\lambda_2^*>\lambda_3^*\) be the eigenvalues at threshold, set \(s=1+\Delta/m\), and put
\[
K=\frac{s^2(2+s)}{m(2+s^2)^2},\qquad H=\frac{\Delta}{\lambda_2^*-\lambda_3^*}.
\]
Then \(K,H>0\) and
\[
t_*(\varepsilon)=\frac{1}{\lambda_1^*-\lambda_2^*}\log\!\left(\frac{H}{K\varepsilon}\right)+o(1).
\]
Consequently an arbitrarily small increase above the threshold can create a genuine but very late reversal.

## Assumptions and scope

The habitats form an undirected path with sites \(1\!\!\leftrightarrow\!\!2\!\!\leftrightarrow\!\!3\). Per-capita movement occurs independently in both directions along each edge at the same positive rate \(m\), and local linear net demographic growth rates are \(r_1,r_2,r_3\). There is no saturation, density dependence, movement loss, external input after the initial release, or site-specific observation weighting. Growth rates may be negative. The model is a deterministic mean-field expectation or linearized rare-population regime, not a finite-population survival-probability model.

With column-vector state \(x(t)\),
\[
\dot x=Mx,\quad M=\begin{pmatrix}
r_1-m&m&0\\m&r_2-2m&m\\0&m&r_3-m
\end{pmatrix},\quad x(0)=e_i,\quad F_i(t)=\mathbf{1}^{\!\top}e^{Mt}e_i.
\]
All statements compare site \(1\) with site \(2\), for every real \(t>0\), at fixed \(m,r_1,r_2,r_3\). The asymptotic holds with \(m,r_1,r_2\) fixed and \(\varepsilon\) positive tending to zero.

## Proof

**1. Spectral and zero-count facts.** The real symmetric irreducible tridiagonal matrix \(M\) has three distinct real eigenvalues \(\lambda_1>\lambda_2>\lambda_3\). Its leading eigenvector \(v_1\) is strictly positive by Perron--Frobenius after a scalar identity shift. Define
\[
G(t)=F_1(t)-F_2(t)=(e_1-e_2)^\top e^{Mt}\mathbf{1}=\sum_{j=1}^3a_je^{\lambda_jt},\quad a_j=\frac{(v_{j1}-v_{j2})(\mathbf{1}^{\!\top}v_j)}{v_j^\top v_j}.
\]
Since \(M\mathbf{1}=(r_1,r_2,r_3)^\top\), \(G(0)=0\) and \(G'(0)=r_1-r_2=\Delta>0\). A nonzero real linear combination of at most three exponentials with distinct real exponents has at most two real zeros counting multiplicity: divide by its lowest exponential, differentiate, apply Rolle's theorem, and induct on the number of exponentials. Thus \(G\) has at most one additional zero on \((0,\infty)\). Every positive zero is simple, as a multiple positive zero would already exceed the total multiplicity budget together with the zero at the origin. The function is not identically zero because its derivative at zero is positive.

**2. Long-horizon sign and sharp boundary.** The first row of \(Mv_1=\lambda_1v_1\) gives
\[
m v_{12}=(\lambda_1-r_1+m)v_{11},\qquad v_{11}-v_{12}=\frac{r_1-\lambda_1}{m}v_{11}.
\]
Therefore \(a_1\) has precisely the sign of \(r_1-\lambda_1\). Let \(s=1+\Delta/m\); at the proposed critical parameter \(r_3=r_3^*\), the positive vector \((1,1,s)^\top\) is an eigenvector of \(M\) with eigenvalue \(r_1\). Positivity proves that this eigenvalue is \(\lambda_1\). The leading eigenvalue is strictly increasing as \(r_3\) increases because its derivative is \(v_{13}^2/(v_1^\top v_1)>0\). Hence \(a_1>0\) below threshold, \(a_1<0\) above threshold, and \(a_1=0\) at threshold.

If \(a_1<0\), then \(G(t)<0\) at large time while \(G(t)>0\) near zero. Continuity gives a positive crossing; the zero bound establishes its uniqueness and simplicity. If \(a_1>0\), both the initial and eventual signs are positive; one simple positive zero cannot be consistent with both signs, so no positive zero exists. At equality \(a_1=0\), the remaining exponential expansion and the conditions \(G(0)=0\), \(G'(0)=\Delta\) give exactly
\[
G(t)=\frac{\Delta}{\lambda_2^*-\lambda_3^*}\left(e^{\lambda_2^*t}-e^{\lambda_3^*t}\right)>0\qquad(t>0).
\]
These arguments prove the complete phase classification including the boundary.

**3. Logarithmic delay.** Let \(\lambda_j(\varepsilon)\) and \(a_j(\varepsilon)\) vary analytically near the threshold, possible because all eigenvalues are simple. At \(\varepsilon=0\), \(a_1=0\), \(a_2=H\), and \(a_3=-H\). The normalized leading vector at threshold is proportional to \((1,1,s)\), and \(d\lambda_1/d\varepsilon=s^2/(2+s^2)\). Combining this with the displayed first-row eigenvector identity yields
\[
a_1(\varepsilon)=-\frac{s^2(2+s)}{m(2+s^2)^2}\varepsilon+O(\varepsilon^2)=-K\varepsilon+O(\varepsilon^2),\qquad a_2(\varepsilon)=H+O(\varepsilon).
\]
A fixed positive time has \(G(t)>0\) at the threshold and therefore for sufficiently small positive \(\varepsilon\), so the unique crossing time tends to infinity. At that crossing divide \(G(t_*)=0\) by \(e^{\lambda_2(\varepsilon)t_*}\):
\[
|a_1(\varepsilon)|e^{(\lambda_1-\lambda_2)t_*}=a_2(\varepsilon)+a_3(\varepsilon)e^{-(\lambda_2-\lambda_3)t_*}=H+o(1).
\]
The equality implies \(t_*=O(\log(1/\varepsilon))\), hence \(\varepsilon t_*\to0\), so the eigengap perturbation makes an \(o(1)\) difference in the logarithmic expansion. Substituting the coefficient expansions gives the asserted asymptotic including the additive \(o(1)\) remainder.

**4. Two-habitat sharpness.** In a two-site corridor with growth rates \(r_1>r_2\), the analogous difference \(G_2(t)\) is a sum of two distinct real exponentials. From \(G_2(0)=0\) and \(G_2'(0)=\Delta\),
\[
G_2(t)=\frac{\Delta}{\mu_1-\mu_2}\left(e^{\mu_1t}-e^{\mu_2t}\right)>0\quad(t>0),
\]
where \(\mu_1>\mu_2\) are the two eigenvalues. Thus a three-habitat path is the smallest corridor with the stated reversal.

## Verification

For an exact witness choose \(m=1\), \((r_1,r_2,r_3)=(2,1,5)\). Then \(r_3^*=5/2<5\) and
\[
M=\begin{pmatrix}1&1&0\\1&-1&1\\0&1&4\end{pmatrix}.
\]
The unique crossover is approximately \(t_*=0.3891806294\) time units. The bundled standard-library `CHECK.py` computes certified rational Taylor approximations, finding \(G(1/5)>0\) and \(G(2/5)<0\), with error per difference less than \(1.60\times10^{-31}\). This establishes a strict rational-time sign bracket without trusting floating-point root finding. The checker independently tests the general rational-parameter threshold eigenvector identities. The global uniqueness and asymptotics are analytic conclusions above, not consequences of finite computation.

To reproduce: run `python3 CHECK.py` in the directory containing the extracted public files; only the Python standard library is needed.

## Relationship to prior work

Wilson and colleagues' 2023 spatial-metapopulation recovery study considers spatial disturbance and population recovery on a more complex nonlinear habitat system, furnishing the ecological motivation but not a two-release-site time-horizon theorem. Moseby and colleagues' 2023 long-term multispecies reintroduction study documents temporally changing outcomes of reintroduction, but does not supply this linear spectral threshold. Benzi and Klymko (2013) establish the general matrix-exponential row-sum/total-communicability viewpoint and its Perron-limit relationship; neither total communicability nor the real-exponential zero count is claimed to be invented here. The proposed contribution is the explicit ecological three-corridor threshold, one-crossover classification including equality, sharp graph-size comparison, and logarithmic critical-delay law for this release-placement comparison.

## Limitations

The outcome is expected *linear* total abundance, not persistence probability, risk-adjusted abundance, nonlinear carrying-capacity performance, or a robust release policy under uncertain growth rates. All three habitats share the same symmetric movement rate. Unequal directed movement, longer corridors, stochastic environmental variation and time-dependent demographic rates can exhibit different rankings. The exact result assumes fixed known model parameters. Numerical witness checks do not replace the proof; prior-art assessment remains provisional pending broader independent literature review.

## References

1. Wilson and coauthors (2023), *The role of spatial structure in at-risk metapopulation recoveries*, *Ecological Applications*, DOI: https://doi.org/10.1002/eap.2898 (first online June 12, 2023).
2. Moseby and coauthors (2023), *Influence of interactive effects on long-term population trajectories in multispecies reintroductions*, *Conservation Biology*, DOI: https://doi.org/10.1111/cobi.14209 (first online October 25, 2023).
3. Benzi and Klymko (2013), *Total communicability as a centrality measure*, preprint https://arxiv.org/abs/1302.6770, supplying the general matrix-exponential centrality framework.
