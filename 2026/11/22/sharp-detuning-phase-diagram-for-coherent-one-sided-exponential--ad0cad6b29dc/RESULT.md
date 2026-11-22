# Sharp detuning phase diagram for coherent one-sided exponential Gabor windows

## Finding

For every real \(a>0\), \(c>0\), and \(0<h<1\), consider the causal two-tone window
\[
f_{a,c,h}(t)=e^{-2\pi a t}(1+c e^{-2\pi i h t})\mathbf1_{[0,\infty)}(t)
\]
and its critical-lattice Gabor system \(\{e^{2\pi i mt}f_{a,c,h}(t-n):m,n\in\mathbb Z\}\). Define \(r=e^{-2\pi a}\in(0,1)\), \(\theta=2\pi h\), and \(q=1-r^2\). The **complete frame/nonframe classification** is as follows.

**Short detuning, \(0<h\le\tfrac12\).** If \(r<\cos(\pi h)\), the system is a Riesz basis for every \(c>0\). If \(r\ge\cos(\pi h)\), define
\[
c_{\pm}=\frac{r^2-\cos\theta\ \pm\ 2\sin(\pi h)\sqrt{r^2-\cos^2(\pi h)}}{q}.
\]
The system is **not a frame precisely for** \(c\in[c_-,c_+]\), including the endpoints. It is a Riesz basis elsewhere. At \(r=\cos(\pi h)\) the nonframe interval is the single amplitude \(c=1\).

**Long detuning, \(\tfrac12<h<1\).** Let
\[
P=\sqrt{1+r^4-2r^2\cos\theta},\qquad
c_{\pm}=\frac{P\pm2r\sin(\pi h)}{q}.
\]
For **every** \(a>0\), the system is not a frame precisely for \(c\in[c_-,c_+]\). Outside this interval it is a Riesz basis. In both regimes, \(0<c_-\le c_+\) and \(c_-c_+=1\).

In particular, for equal-amplitude sidebands \(c=1\), the system is a frame exactly when \(0<h<\tfrac12\) **and** \(e^{-2\pi a}<\cos(\pi h)\). Thus the half-integer detuning is a sharp qualitative boundary: below it sufficiently strong damping restores stability, whereas above it no positive damping restores equal-amplitude stability.

**Zero geometry.** In the open nonframe interval, the Zak transform has exactly one zero in \((0,1)\times[0,1)\) for \(0<h\le\tfrac12\). At either interval endpoint that zero reaches the limiting edge \(x=1\). For \(\tfrac12<h<1\), each nonframe endpoint instead has one *interior* Zak zero at which the scalar circle-intersection equation is tangent. In the open nonframe interval, there is one or two interior zeros: writing
\[
E=q(1+c^2)+2c(\cos\theta-r^2),
\]
there are two when \(E>0\), one when \(E<0\), and one interior zero plus one limiting boundary zero when \(E=0\). These assertions concern the open fundamental cell, not a multiplicity claim for the full two-variable complex Zak map.

## Assumptions and scope

All parameters are real with \(a,c>0\) and \(h\in(0,1)\); no integer or rational restriction is placed on \(h\). The lattice is exactly \(\mathbb Z\times\mathbb Z\), with modulation \(M_mf(t)=e^{2\pi i mt}f(t)\) and translation \(T_nf(t)=f(t-n)\). The frame property is the standard two-sided inequality in \(L^2(\mathbb R)\). At this critical lattice a frame is a Riesz basis; failure is equivalent to essential infimum zero of the Zak-energy function. Values at jump points of the causal window do not affect the assertion.

The equivalent Cauchy-pair window is, up to a nonzero scalar and Fourier transformation, \((t+ia)^{-1}+c(t-h+ia)^{-1}\). The theorem does not claim optimal positive frame bounds, stability for other lattice densities, or arbitrary relative complex amplitudes.

## Proof

**1. Exact Zak symbol.** For \(0\le x<1\) and \(y\in[0,1)\), define \(Zf(x,y)=\sum_{n\in\mathbb Z}f(x+n)e^{-2\pi i ny}\). Put \(z=e^{-2\pi i y}\), \(\phi=\theta x\). Because the window is supported on the nonnegative half-line, the geometric series converges absolutely and gives
\[
Zf(x,y)=r^x\left[\frac1{1-rz}+\frac{c e^{-i\phi}}{1-r e^{-i\theta}z}\right]
=\frac{r^x N(\phi,z)}{(1-rz)(1-r e^{-i\theta}z)},
\]
where
\[
N(\phi,z)=1+c e^{-i\phi}-rz(e^{-i\theta}+c e^{-i\phi}).
\]
Both denominator factors have modulus between \(1-r\) and \(1+r\); the continuous extension to \(0\le x\le1\) is bounded above. Classical critical Zak diagonalization now reduces frame positivity to a strictly positive minimum of \(|Zf|^2\) on this closed cell. A zero at the excluded edge \(x=1\) still makes the *essential* lower frame bound zero.

**2. Scalar equality criterion.** A unit-modulus \(z\) solves \(N=0\) precisely when
\[
|1+c e^{-i\phi}|=r|e^{-i\theta}+c e^{-i\phi}|.
\]
The two factors on this equation cannot both be zero since \(0<\theta<2\pi\). Squaring and subtracting gives the real expression
\[
Q(\phi)=q(1+c^2)+2cF(\phi),\qquad
F(\phi)=\cos\phi-r^2\cos(\theta-\phi).
\]
At \(\phi=0\), \(Q(0)=q(1+c^2)+2c(1-r^2\cos\theta)>0\). Therefore continuity shows that the Zak essential lower bound is zero if and only if
\[
q(1+c^2)+2c\min_{0\le\phi\le\theta}F(\phi)\le0.
\]
Indeed, a nonpositive minimum forces a crossing of zero because the value at the left endpoint is positive, and equality yields a limiting or actual zero. Conversely, if the minimum is positive, the numerator is bounded away from zero uniformly in \((\phi,z)\).

For completeness, in the stable regime set \(D=q(1+c^2)+2c\min F>0\). The identity \((|U|-r|V|)(|U|+r|V|)=Q\), with \(U=1+c e^{-i\phi}\), \(V=e^{-i\theta}+c e^{-i\phi}\), implies \(|N|\ge D/[(1+r)(1+c)]\) by the reverse triangle inequality. Consequently a concrete (not generally optimal) positive squared frame lower bound is
\[
A\ge\left[\frac{rD}{(1+r)^3(1+c)}\right]^2>0.
\]

**3. Minimize the phase cosine.** Differentiating directly gives \(F'(\phi)=-\sin\phi-r^2\sin(\theta-\phi)\). When \(0<\theta\le\pi\), it is strictly negative in the interior, so
\[
\min F=F(\theta)=\cos\theta-r^2.
\]
When \(\pi<\theta<2\pi\), let \(A_0=1-r^2\cos\theta>0\) and \(B_0=-r^2\sin\theta>0\). With \(\delta=\arg(A_0+iB_0)\in(0,\pi/2)\) and \(P=\sqrt{A_0^2+B_0^2}\), we have \(F(\phi)=P\cos(\phi-\delta)\). Since \(F'(\theta)=-\sin\theta>0\), the minimum \(\phi_*=\pi+\delta\) lies strictly inside \((0,\theta)\) and
\[
\min F=-P=-\sqrt{1+r^4-2r^2\cos\theta}.
\]

**4. Solve exactly.** In either case the condition is a quadratic inequality \(q c^2+2m c+q\le0\), with \(m=\min F\). For short detuning,
\[
m^2-q^2=4\sin^2(\pi h)(r^2-\cos^2(\pi h)).
\]
The quadratic can be nonpositive for positive \(c\) precisely when \(r\ge\cos(\pi h)\), and its two roots are the displayed short-detuning values. For long detuning,
\[
P^2-q^2=4r^2\sin^2(\pi h)>0,
\]
so it has two distinct positive reciprocal roots for every \(r\in(0,1)\), exactly the displayed long-detuning values. Including the roots is essential: the Zak essential infimum vanishes there. This proves the full frame classification and the equal-amplitude statement.

**5. Count zeros.** For each phase \(\phi\) satisfying \(Q(\phi)=0\), the unique corresponding unit-modulus \(z\) is
\[
z=\frac{1+c e^{-i\phi}}{r(e^{-i\theta}+c e^{-i\phi})}.
\]
Thus zero counting reduces to the intersections of \(F(\phi)\) with the negative level \(-q(1+c^2)/(2c)\). For short detuning, strict monotonicity gives one interior crossing for strict nonframe amplitudes and an endpoint contact at boundary amplitudes. For long detuning, \(F\) rises to its unique maximum, decreases to its unique interior minimum, then rises to \(F(\theta)\). At the two nonframe endpoints the line is tangent at the minimum. For strict nonframe amplitudes it crosses the descending branch once, and crosses the final ascending branch exactly when \(Q(\theta)>0\); equality puts the second root on the excluded edge. The displayed \(E\) is precisely \(Q(\theta)\). No further intersections are possible.

## Verification

The standalone `verify_detuning.py` independently checks the analytic minimizer against dense trigonometric grids across several disjoint parameter chambers, the reciprocal amplitude boundaries, absence of roots in stable test regions, unit-circle recovery of Zak zeros, the two-zero chamber, limiting boundary zeros, and the Zak geometric-series formula against a truncated sum. It passes 497 supplementary assertions with only Python's standard library. These numerical checks do **not** prove the quantified theorem; Steps 1–5 establish it for all admissible parameters. Run with `python verify_detuning.py` from the package directory.

## Relationship to prior work

Belov, Kulikov, and Lyubarskii (arXiv:2103.08959, first public 16 March 2021) establish Gabor frame theory for rational Cauchy-pole combinations and give a general Fourier/Zak framework; their cited Herglotz theorem concerns poles constrained to an imaginary axis, not this two-pole horizontal separation. Their general critical-density Zak criterion does not state the explicit arbitrary-detuning threshold or two-zero chamber derived here. The same authors' 2022 study (arXiv:2212.08915) gives critical sharp bounds for a **single** Cauchy pole. Faulhuber and Shafkulovska (arXiv:2204.02917) study optimizing bounds of standard one-sided and two-sided exponential windows, not these coherent noninteger sidebands.

The closest published half-frequency sideband phase diagram, *Exact critical Gabor phase diagram for a half-frequency exponential sideband* (public full result, 2026), treats \(h=1/2\) and already gives sharper bounds and a unique zero in that case. **That special case is not claimed as new here**. The present claim is the classification over **all** \(0<h<1\), particularly the nontrivial stability condition for \(0<h<1/2\), unconditional long-detuning nonframe interval, and the changing number and boundary location of Zak zeros for \(h>1/2\). These facts do not follow merely from the previously published single value \(h=1/2\), though they use the standard Zak method.

## Limitations

The result is for positive real relative amplitudes, the critical unit lattice and the stated coherent two-tone family only. It does not provide the optimal nonzero frame constants or classify general two-sided windows, arbitrary complex phases or other lattice densities. An equivalent prior two-frequency formula could have been missed despite targeted literature and overlap searches, so historical novelty remains a best-knowledge assessment; no independent mathematical validation has been performed.

## References

1. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959 (first public 2021-03-16), https://arxiv.org/abs/2103.08959 .
2. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915 (first public 2022-12-17), https://arxiv.org/abs/2212.08915 .
3. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (first public 2022-04-06), https://arxiv.org/abs/2204.02917 .
4. *Exact critical Gabor phase diagram for a half-frequency exponential sideband*, full publicly available result, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-exact-critical-gabor-phase-diagram-for-a-half-frequency-exponent--08ab1e642ad1/RESULT.md (half-frequency instance already covered).
