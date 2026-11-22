# Three renewal stages are the sharp onset of a finite optimal gap between two confirmatory acoustic windows

## Finding

Consider one stationary animal-call renewal process whose successive inter-call times are independent Erlang laws with an integer number \(m\) of exponential phases, all of rate \(\lambda>0\). Two perfect recording windows, each of duration \(w>0\), are \([0,w]\) and \([w+g,2w+g]\), with selectable nonnegative silent gap \(g\ge0\). The objective \(P_m(w,g)\) is the probability that **each** window contains at least one call from the same continuously present animal, not merely that their union contains a call.

For \(m=1\), the objective is exactly independent of the gap. For \(m=2\), it is strictly increasing in \(g\); its supremum occurs only as \(g\to\infty\), so no finite gap is optimal. For \(m=3\), **there is exactly one finite global optimal gap** for every \(\lambda,w>0\). With dimensionless window length \(x=\lambda w\), let

\[
R(x)=\frac{\sqrt3(8+4x-x^2)}{3x(x+4)}.
\]

The unique maximizing dimensionless gap is

\[
\boxed{\lambda g_*(w)=\frac2{\sqrt3}\left(\frac\pi2+\arctan R(\lambda w)\right).}
\]

It decreases strictly with \(w\), with sharp endpoint limits

\[
\lim_{w\downarrow0}\lambda g_*(w)=\frac{2\pi}{\sqrt3},\qquad
\lim_{w\to\infty}\lambda g_*(w)=\frac{2\pi}{3\sqrt3}.
\]

Thus three exponential renewal phases are the **smallest** number for which any finite strictly optimal positive recording gap exists for the stated two-confirmation objective. For \(\lambda w=1\), the optimum is \(\lambda g_*=2.85747542539998\ldots\), raising the two-confirmation probability from \(0.05711456541455\ldots\) at zero gap to \(0.10634765599656\ldots\). This is a model-based probability comparison, not an empirical acoustic scheduling prescription.

## Assumptions and scope

All call events are instantaneous, unambiguously detected, and belong to a single animal continuously present throughout both recording windows and the intervening gap. The calling process is in its stationary equilibrium at time zero; it is neither newly initiated nor conditioned on a call at zero. The number \(m\in\{1,2,3\}\) of independent exponential phases per inter-call duration is an integer, and each has common positive rate \(\lambda\). There is no fixed deployment deadline, travel penalty, circadian nonstationarity, false alarm, detector failure, or rate change. Both windows have equal positive duration, and the gap may be any finite nonnegative real number. Claims about \(m\ge4\), unequal recording windows, multiple animals, or non-Erlang renewal laws are not made.

To avoid confusing the Erlang event rate with the stationary call rate: the mean inter-call interval is \(m/\lambda\), so the mean calls per time unit are \(\lambda/m\). The stationary initial phase is uniform over the \(m\) cyclic phases.

## Proof

**1. Finite-state event representation.** Rescale time by \(\lambda\), so the phase-transition rate becomes one. Number the phases \(1,\ldots,m\). At each transition \(i\to i+1\), and \(m\to1\), the phase advances; only the last transition emits a call. Let \(P\) be the cyclic successor matrix, \(N\) the same matrix with its last-to-first entry set to zero, \(Q=P-I\), and \(Q_0=N-I\). Row vectors act on the right, and \(\pi=m^{-1}(1,\ldots,1)\) is the stationary phase law. If \(x=\lambda w\) and \(y=\lambda g\), the matrix for a window with **no call** is

\[
Z_m(x)=e^{xQ_0}=e^{-x}\sum_{j=0}^{m-1}\frac{x^jN^j}{j!}.
\]

The unconstrained gap has transition matrix \(T_m(y)=e^{yQ}\). With \(\mathbf1\) the all-one column, stationarity and inclusion–exclusion give the exact formula

\[
P_m(w,g)=1-2\pi Z_m(x)\mathbf1+\pi Z_m(x)T_m(y)Z_m(x)\mathbf1.\tag{1}
\]

The two terms \(\pi Z_m(x)\mathbf1\) agree by stationarity. Multiplication of the two no-call matrices with the unconstrained gap matrix correctly permits **any** number of calls during the gap and rules out calls during each observed window. The matrices are substochastic only during no-call intervals.

**2. One and two stages.** With one stage the process is Poisson, and disjoint-window event counts are independent. Hence

\[
P_1(w,g)=(1-e^{-x})^2.
\]

With two stages, \(\pi Z_2(x)\mathbf1=e^{-x}(1+x/2)\), and diagonalization of the two-cycle gives

\[
P_2(w,g)=\left[1-e^{-x}(1+x/2)\right]^2-\frac{x^2}{4}e^{-2x-2y}.
\]

This expression has strictly positive derivative with respect to \(y\) for every \(x>0\). It approaches, but never attains for finite \(y\), the independent-window limit.

**3. Three stages and its damped oscillation.** Define

\[
s(x)=e^{-x}\left(1+\frac{2x}{3}+\frac{x^2}{6}\right),\quad
A(x)=-\frac{x^2(x^2+8x+4)}{36},\quad
B(x)=\frac{\sqrt3 x^2(x^2-4)}{36},\quad
\omega=\frac{\sqrt3}{2}.
\]

The cyclic generator has eigenvalues \(0,-3/2+i\omega,-3/2-i\omega\). Direct substitution into (1) (or the three-point roots-of-unity filter) yields

\[
P_3(w,g)=[1-s(x)]^2+e^{-2x-3y/2}\big[A(x)\cos(\omega y)+B(x)\sin(\omega y)\big].\tag{2}
\]

For explicit verification of the factorization, remove the common factor \(e^{-x}\) from the two no-call factors and form \(v=\pi(I+xN+x^2N^2/2)\) and \(u=(I+xN+x^2N^2/2)\mathbf1\). The three cyclic contractions are

\[
\begin{aligned}
z_0&=1+4x/3+2x^2/3,\\
z_1&=1+4x/3+2x^2/3+x^3/3+x^4/12,\\
z_2&=1+4x/3+x^2+x^3/3.
\end{aligned}
\]

Thus \(A=(2z_0-z_1-z_2)/3\) and \(B=\sqrt3(z_1-z_2)/3\), proving the coefficients in (2) without relying on a numerical fit. The term \([1-s]^2\) is the large-gap independent-window limit.

Differentiation of (2) gives a strictly positive prefactor times

\[
C(x)\cos(\omega y)+D(x)\sin(\omega y),
\quad C(x)=\frac{x^3(x+4)}{12}>0,\quad
D(x)=-\frac{\sqrt3 x^2(x^2-4x-8)}{36}.
\]

Writing \(\phi(x)=\arctan(D/C)\in(-\pi/2,\pi/2)\), this derivative has sign \(\cos(\omega y-\phi)\) for \(y\ge0\). Its first zero is therefore \(y_*=(\pi/2+\phi)/\omega>0\), where the derivative changes from positive to negative. All later local maxima occur exactly \(4\pi/\sqrt3\) apart. At each local maximum, the oscillatory bracket \(A\cos+B\sin\) equals \(\omega(A^2+B^2)/\sqrt{C^2+D^2}>0\). Consequently all later maxima lie strictly below the first, because the common envelope strictly decays by the factor \(e^{-2\pi\sqrt3}\) per cycle. Finally \(A(x)<0\) makes the initial value strictly below the limiting value \([1-s]^2\), whereas the first local maximum lies strictly above it. The first maximum is thus the unique **global** maximum, including the boundary \(y=0\) and the limit \(y\to\infty\).

**4. Monotonicity and sharp limits.** The phase ratio simplifies to \(D/C=R(x)\), with derivative

\[
R'(x)=-\frac{8\sqrt3(x^2+2x+4)}{3x^2(x+4)^2}<0.
\]

Therefore \(y_*(x)\) decreases strictly. Since \(R(x)\to+\infty\) as \(x\downarrow0\) and \(R(x)\to-1/\sqrt3\) as \(x\to\infty\), continuity of principal \(\arctan\) gives the stated limits. This also proves both bounds are strict at finite positive \(x\).

## Verification

The supplied `check.py` computes the joint probability via *independent* finite-state transitions, using the truncated no-call exponential and a positive Poisson-series representation of the unconstrained cyclic gap. It checks its results against all three closed forms for nine window durations and fourteen gap values per stage, and checks the three-stage first maximum against nearby and remote alternatives and its strict decrease across positive window lengths. The standalone execution yielded `PASS 533 checks` with the numerical example above. Numerical samples are corroboration; global optimality for all positive parameters follows from the analytic proof, not the finite test grid. The Poisson-series tail in this finite-domain checker is bounded numerically by positivity and the asserted near-unit mass, but its double-precision tolerance is not an infinite-domain certificate.

To reproduce from the directory containing this file, execute `python3 check.py` with a Python 3 interpreter and no third-party packages.

## Relationship to prior work

Stevenson et al. (first public 23 October 2014) develop acoustic capture–recapture density estimation and discuss the importance of call rate variation, observed nearly regular calls in an amphibian and dependence among calls. Their objective is density estimation, not two separated windows both containing a call. Balantic and Donovan (2019) optimize field acoustic sampling with time-varying hourly vocalization probabilities, and explicitly discuss confirmation on two separate occasions; their published algorithm does not solve the stationary renewal-phase exact gap optimization. Nolan (2017), in the context of genetic recombination, supplies general finite-dimensional distributions of Erlang renewal counts via cyclic phase matrices and nonadjacent coincidence statistics, which encompass the **probability-calculation method** behind (1). That prior general probability law is not claimed new. The finding here is the **global optimization theorem**, its sharp one/two/three-phase distinction, the unique explicit three-phase optimizer, and its strict window-length response; those conclusions are not stated in the inspected paper. Van Helsdingen, Marques and Jones-Todd (first public 2024) model underdispersed acoustic cues using a Weibull–Hawkes process rather than the stationary Erlang renewal design studied here.

## Limitations

The optimality criterion is two confirmatory nonempty recording sessions for a continuously present, perfectly detected, single, stationary caller, not probability of at least one call anywhere. With an imposed final deployment deadline, \(g_*\) must be compared with that deadline's feasible endpoint; none is assumed here. The stationary phase assumption is essential, and a newly started renewal process can have different scheduling behavior. Call bouts, circadian changes, observer errors, multiple animals, acoustic masking, heterogeneous rate parameters, and discrete survey calendars are excluded. The Erlang model is a controllable underdispersed benchmark, not an empirical fit asserted for any named species. This does not establish a general theorem for all IFR or all underdispersed renewal laws. Historical priority is provisional given broad, older renewal and nonadjacent-window literature.

## References

1. Stevenson, B. C., Borchers, D. L., Altwegg, R., Swift, R. J., Gillespie, D. M., and Measey, G. J. (2014 online; 2015 volume). *A general framework for animal density estimation from acoustic detections across a fixed microphone array.* Methods in Ecology and Evolution. https://doi.org/10.1111/2041-210X.12291
2. Balantic, C. and Donovan, T. (2019). *Temporally adaptive acoustic sampling to maximize detection across a suite of focal wildlife species.* Ecology and Evolution. https://doi.org/10.1002/ece3.5579
3. Nolan, J. P. (2017). *Erlang renewal models for genetic recombination.* Journal of Statistical Distributions and Applications. https://doi.org/10.1186/s40488-017-0064-5
4. Van Helsdingen, A. B. M., Marques, T. A., and Jones-Todd, C. M. (2024 online; 2025 volume). *An Inhomogeneous Weibull–Hawkes Process to Model Underdispersed Acoustic Cues.* Journal of Agricultural, Biological and Environmental Statistics. https://doi.org/10.1007/s13253-024-00626-w
