# Endpoint-to-midpoint transition in the optimal reset location for interval cover times

## Finding

Let a Brownian particle with generator \(D\partial_{xx}\) move on the reflecting interval \([0,L]\), start at \(x\), and reset to that same \(x\) at independent Poisson times of rate \(r>0\). The cover time \(T_x\) is the first instant by which both endpoints have been visited. For every \(L,D,r>0\), the set of global minimizers of \(\mathbb E[T_x]\), as \(x\) ranges over the **closed** interval \([0,L]\), is exactly

\[
\operatorname*{arg\,min}_{0\le x\le L}\mathbb E[T_x]
=\begin{cases}
\{0,L\},&0<\rho<\rho_c,\\
\{0,L/2,L\},&\rho=\rho_c,\\
\{L/2\},&\rho>\rho_c,
\end{cases}
\qquad
\rho=\frac{rL^2}{4D},\quad
\rho_c=\left[\operatorname{arcosh}\!\left(\frac{1+\sqrt{17}}4\right)\right]^2.
\]

Here \(\rho_c=0.5370803732334924\ldots\). No off-center, non-endpoint reset location is a global optimum. The transition is discontinuous: the optimal resetting site jumps from an endpoint to the midpoint.

A distinct and smaller spinodal occurs at

\[
\rho_s=\left[\operatorname{arcosh}\!\left(\sqrt{1+1/\sqrt5}\right)\right]^2
=0.3929655742721049\ldots<\rho_c.
\]

For \(0<\rho\le\rho_s\), the midpoint is a strict local maximum of the mean cover time. For \(\rho>\rho_s\), the midpoint and both endpoints are strict local minima, separated by exactly one strict local maximum in each open half-interval. Consequently the midpoint is metastable when \(\rho_s<\rho<\rho_c\), while the endpoints are metastable when \(\rho>\rho_c\). At \(\rho=\rho_s\), the midpoint maximum is quartically flat, rather than a local minimum.

The exact minimum value is

\[
\min_{x\in[0,L]}\mathbb E[T_x]
=\frac1r\min\left\{\cosh\!\left(L\sqrt{r/D}\right)-1,\;3\cosh\!\left(\frac L2\sqrt{r/D}\right)-2\operatorname{sech}\!\left(\frac L2\sqrt{r/D}\right)-1\right\}.
\]

## Assumptions and scope

The diffusion is a continuous reflecting Brownian motion on \([0,L]\), with infinitesimal generator \(D\partial_{xx}\) in the interior and instantaneous reflection at both endpoints. The particle starts at \(x\in[0,L]\); every reset returns it to this *same, deterministic, fixed* position, independently of previous paths. Resets do not erase endpoints previously visited for purposes of cover time. The reset clock is Poissonian with constant rate \(r>0\). All conclusions quantify over arbitrary fixed \(D,L,r>0\), with spatial location freely chosen on the entire closed interval, including its endpoints. The claim is for mean cover time, not the entire distribution, and makes no assertion when resetting locations and starting location are independently varied.

Set \(k=\sqrt{r/D}\), \(b=\cosh(kL/2)>1\), and \(z=\cosh(k(x-L/2))\). As \(x\in[0,L]\), \(z\in[1,b]\), with \(z=1\) only at the midpoint and \(z=b\) only at the two endpoints.

## Proof

**1. Exact objective, with previously known first-passage ingredients.** Let \(\tau_0\), \(\tau_L\), and \(\tau_e=\min(\tau_0,\tau_L)\) be the first hitting times of \(0\), \(L\), and either endpoint, under the same resetting process. Continuity of paths between resets, with resets constrained to \([0,L]\), implies that the cover time is \(T_x=\max(\tau_0,\tau_L)=\tau_0+\tau_L-\tau_e\), *pathwise*, even though previous visits survive a reset. In particular, one may add and subtract the expected hitting times without assuming independence.

For ordinary (nonresetting) diffusion, the transforms \(\phi_j(x)=\mathbb E_x[e^{-r\tau_j^{(0)}}]\) solve \(D\phi_j''=r\phi_j\) with unit data at absorbing target boundaries and reflecting Neumann data elsewhere. The unique solutions are

\[
\phi_0(x)=\frac{\cosh(k(L-x))}{\cosh(kL)},\quad
\phi_L(x)=\frac{\cosh(kx)}{\cosh(kL)},\quad
\phi_e(x)=\frac{\cosh(k(x-L/2))}{\cosh(kL/2)}.
\]

The standard first-reset renewal equation, for a process which always restarts at its own starting point, yields \(\mathbb E_x[\tau_j]=(1-\phi_j(x))/(r\phi_j(x))\). All three transforms are strictly positive, so these means are finite. Substituting into the pathwise identity gives

\[
 r\mathbb E[T_x]=\cosh(kL)\left[\operatorname{sech}(kx)+\operatorname{sech}(k(L-x))\right]-b\operatorname{sech}(k(x-L/2))-1.
\]

The elementary hyperbolic product identity \(\cosh(kx)\cosh(k(L-x))=z^2+b^2-1\) simplifies the known cover-time objective to

\[
 H_b(z):=r\mathbb E[T_x]
 =\frac{2b(2b^2-1)z}{z^2+b^2-1}-\frac bz-1,
 \qquad 1\le z\le b.
\]

The unoptimized mean cover-time law is prior work, particularly the general asymmetric reflected-interval expression of Linn and Lawley (2024, Section 4.1, equation (38)). The step beyond that law is the complete minimizer and local-extremum classification below.

**2. There are no interior spatial minima except possibly the midpoint.** Direct differentiation, including the full positive denominator, gives

\[
H_b'(z)=\frac{bF_b(z^2)}{z^2(z^2+b^2-1)^2},\qquad
F_b(y)=(3-4b^2)y^2+4b^2(b^2-1)y+(b^2-1)^2.
\]

For \(b>1\), the polynomial \(F_b\) has a negative leading coefficient and a strictly positive constant term. Its two real roots have opposite signs (the discriminant is strictly positive). Thus \(F_b(y)\) is positive before its unique positive root and negative after. Correspondingly \(H_b\), restricted to \([1,b]\), is either strictly decreasing or first increasing and then decreasing. It has *no interior local minimum* in the open \(z\)-interval. The only possible global minimizing values of \(z\) are therefore \(1\) and \(b\).

**3. Exact global transition and equality set.** Evaluation at both candidates gives

\[
H_b(1)=3b-\frac2b-1,\qquad H_b(b)=2b^2-2,
\]

and hence

\[
H_b(1)-H_b(b)=-\frac{(b-1)(2b^2-b-2)}{b}.
\]

The positive polynomial root in \(b>1\) is \(b_c=(1+\sqrt{17})/4\). For \(1<b<b_c\), the endpoint value is smaller; for \(b>b_c\), the midpoint value is smaller; at \(b=b_c\), they agree. The interior-maximum characterization in step 2 makes these equality sets exhaustive. Since \(b=\cosh\sqrt\rho\) strictly increases with \(\rho>0\), the global-location classification and \(\rho_c\) follow.

**4. The different local-stability threshold.** The sign of \(H_b'(1)\) is that of

\[
F_b(1)=5(b^2-1)^2-1.
\]

This changes sign exactly at \(b_s=\sqrt{1+1/\sqrt5}\). Because \(z-1=\tfrac12 k^2(x-L/2)^2+O((x-L/2)^4)\), the midpoint is a strict local maximum below \(b_s\) and a strict local minimum above it. At \(b=b_s\), \(F_b(1)=0\) but \(F_b(y)<0\) for every \(y>1\) sufficiently close to \(1\), so the leading nonconstant spatial correction is strictly negative and of fourth order. Further,

\[
F_b(b^2)=1-2b^2<0,
\]

so both endpoints are always strict one-sided local minima. For \(b>b_s\), the unique positive root \(y_*(b)\) of \(F_b\) lies strictly between \(1\) and \(b^2\); this yields exactly one strict separating spatial maximum on each side of the midpoint. Explicitly, with \(A=4b^2-3\), \(B=4b^2(b^2-1)\), and \(C=(b^2-1)^2\),

\[
 y_*(b)=\frac{B+\sqrt{B^2+4AC}}{2A},\qquad
 x_\pm=\frac L2\pm\frac1k\operatorname{arcosh}\sqrt{y_*(b)}.
\]

Finally \(b_s<b_c\), giving the stated metastability interval and its exact ordering. This proves all assertions. \(\square\)

## Verification

The accompanying standard-library-only script `verify.py` checks the endpoint and midpoint identities in exact rational arithmetic, scans the global spatial phase regimes, compares the objective against an **independently discretized** second-order first-passage boundary-value problem, and checks analytic derivatives by finite differences. Run `python3 verify.py` from a directory containing that file. The completed script returned 748 passing assertions and the two stated dimensionless transition values. These computations are reproducibility checks, not substitutes for the proof of the continuum and all-parameter claims.

## Relationship to prior work

Ghosh and Sabhapandit (arXiv:2605.31207v1, 29 May 2026) derive the midpoint-reset cover-time distribution and mean, notably their equation (21); they optimize the **reset rate** at the midpoint. Inserting \(x=L/2\) into the displayed expression reproduces that published mean identically. They do not optimize over the reset location.

Linn and Lawley (arXiv:2406.12154, first public 17 June 2024; updated 2025) derive the complete asymmetric-interval reflected Brownian **mean cover-time function** in Section 4.1, equation (38), and analyze high-reset-rate behavior. The dependence of the mean on arbitrary placement, and hence the unoptimized function itself, is not claimed new. Their treatment does not state the global spatial argmin, the discontinuous threshold \(\rho_c\), the distinct spinodal \(\rho_s\), or the exhaustive coexistence/minimum/maximum classification. Those explicit optimization statements and their proof are the contribution here.

Julián-Salgado, Dagdug and Boyer (arXiv:2507.14483) study discontinuities in the **optimal reset rate** for single-target hitting on a half-line with random reset locations. Their model and the optimized variable differ from the present deterministic-location, two-endpoint cover-time problem. Such prior discontinuous-rate results are not presented here as new discoveries.

## Limitations

The result does not cover arbitrary distributed reset locations, distinct starting and resetting positions, non-Poisson clocks, asymmetric drift, partial resets, or nonreflecting boundaries. It is about spatial optimization at each **fixed** positive resetting rate; it is not an optimization of both rate and position. It depends on a previously published exact mean cover-time law, so a broader existing optimization analysis of that law may implicitly contain the classification; a database search is not a uniqueness or novelty proof. Independent scientific validation has not been performed.

## References

1. A. Ghosh and S. Sabhapandit, *Cover time statistics of one-dimensional Brownian motion under stochastic resetting*, arXiv:2605.31207v1 (29 May 2026), Sections II–III, especially equation (21).
2. S. Linn and S. D. Lawley, *Cover times with stochastic resetting*, arXiv:2406.12154 (first posted 17 June 2024), Section 4.1, especially equation (38).
3. P. Julián-Salgado, L. Dagdug and D. Boyer, *Abrupt transitions in the optimization of diffusion with distributed resetting*, arXiv:2507.14483 (first posted 19 July 2025), Sections I–II.
