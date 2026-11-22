# A sharp dimension barrier for compactly supported geodesic tent kernels

## Finding
For any real \(c>0\) and any integer \(d\ge1\), define the zonal kernel on the unit sphere \(\mathbb S^d\) by
\[
T_{c,d}(x,y)=(c-\theta(x,y))_+,
\qquad \theta(x,y)=\arccos\langle x,y\rangle.
\]
Then the kernel is positive semidefinite on **all finite configurations** if and only if
\[
\boxed{d=1\quad\text{or}\quad c\ge\pi.}
\]
For every fixed \(0<c<\pi\), define the unnormalized Legendre coefficient
\[
I_n(c)=\int_0^c(c-\theta)P_n(\cos\theta)\sin\theta\,d\theta.
\]
As \(n\to\infty\),
\[
\boxed{I_n(c)=-\sqrt{\frac{2\sin c}{\pi}}\,n^{-5/2}
\cos\big((n+\tfrac12)c-\tfrac\pi4\big)
+O_c\big(n^{-3}\log(n+1)\big).}
\]
In particular, infinitely many of these coefficients are strictly negative and infinitely many strictly positive. Thus each proper geodesic tent cutoff is spectrally obstructed already on \(\mathbb S^2\), however close its support radius is to \(\pi\). For \(c\ge\pi\), the kernel is positive semidefinite but **not strictly positive definite** on configurations of distinct sites.

## Assumptions and scope
The sphere \(\mathbb S^d\subset\mathbb R^{d+1}\) carries intrinsic angular distance in \([0,\pi]\). The notation \((u)_+=\max(u,0)\) denotes the positive part. Positive semidefiniteness means that for every finite choice of sites, the matrix of kernel values is positive semidefinite; strict positive definiteness requires positive quadratic form for every nonzero coefficient vector at distinct sites. Legendre polynomials satisfy \(P_n(1)=1\). An implicit constant indexed by \(c\) may deteriorate as fixed \(c\) approaches either endpoint of \((0,\pi)\).

## Proof
**Circle positivity.** On \(\mathbb S^1\), angular separation has representative \(t\in[-\pi,\pi]\). For \(0<c<\pi\), the \(2\pi\)-periodic even profile \(f_c(t)=(c-|t|)_+\) has Fourier integrals
\[
\int_{-\pi}^{\pi} f_c(t)e^{-int}\,dt
=\begin{cases}c^2,&n=0,\\2(1-\cos(nc))/n^2,&n\in\mathbb Z\setminus\{0\}.
\end{cases}
\]
All are nonnegative. Fourier positivity on the circle therefore proves the claim for this range. The remaining \(c\ge\pi\) are covered below.

**Positive side in every dimension.** Let \(U\) be uniformly distributed on \(\mathbb S^d\). Rotational symmetry and the planar wedge between two hemispheres yield
\[
\mathbb E\big[\operatorname{sgn}\langle U,x\rangle\operatorname{sgn}\langle U,y\rangle\big]
=1-\frac{2\theta(x,y)}\pi.
\]
For \(c\ge\pi\), the positive part is inactive and
\[
T_{c,d}(x,y)=\big(c-\tfrac\pi2\big)+\tfrac\pi2\,
\mathbb E[\operatorname{sgn}\langle U,x\rangle\operatorname{sgn}\langle U,y\rangle].
\]
This is a sum of two positive-semidefinite kernels with nonnegative coefficients. It is not strictly positive definite: for distinct \(x,-x,y,-y\), where \(y\ne\pm x\), the coefficient vector \((1,1,-1,-1)\) annihilates both the constant feature and each hemisphere-sign feature.

**An exact Legendre identity.** For \(0<c<\pi\), let \(Y_n(\theta)=P_n(\cos\theta)\) and \(N=n(n+1)\). The Legendre equation gives
\[
(\sin\theta\,Y_n'(\theta))'=-N\sin\theta\,Y_n(\theta).
\]
Twice integrating by parts, using \(c-\theta=0\) at the upper endpoint, yields for every integer \(n\ge1\)
\[
I_n(c)=\frac{J_n(c)-\sin c\,P_n(\cos c)}{n(n+1)},
\qquad J_n(c)=\int_0^c\cos\theta\,P_n(\cos\theta)\,d\theta.
\tag{1}
\]
The bound \(J_n(c)=O(\log(n+1)/n)\) holds uniformly in \(c\in[0,\pi]\). To prove it, set \(p_j=\binom{2j}{j}/4^j\), with \(p_j\le(j+1)^{-1/2}\). The Legendre generating function factors, for \(z=e^{i\theta}\), as
\[
(1-2t\cos\theta+t^2)^{-1/2}
=(1-zt)^{-1/2}(1-z^{-1}t)^{-1/2},
\]
so coefficient comparison gives the finite exact identity
\[
P_n(\cos\theta)=\sum_{k=0}^n p_kp_{n-k}e^{i(n-2k)\theta},
\qquad \sum_{k=0}^n p_kp_{n-k}=1.
\tag{2}
\]
For terms \(k<n/4\) or \(k>3n/4\), the Fourier frequency has absolute value at least \(n/2\); integration against \(\cos\theta\) is \(O(1/n)\), and the nonnegative coefficients sum to at most one. For the remaining terms, each coefficient is \(O(1/n)\), while
\[
\left|\int_0^c\cos\theta\,e^{im\theta}\,d\theta\right|
\le \frac{C}{1+|m|},\qquad 0\le c\le\pi,
\]
with an absolute \(C\), including the two resonant frequencies. Summing over frequencies of spacing two gives \(O(\log(n+1)/n)\), as claimed.

**Oscillatory obstruction.** The fixed-interior-angle Darboux asymptotic (DLMF §18.15(iii), or classical Legendre asymptotics) is
\[
P_n(\cos c)=\sqrt{\frac{2}{\pi n\sin c}}
\cos\big((n+\tfrac12)c-\tfrac\pi4\big)+O_c(n^{-3/2}).
\tag{3}
\]
Substituting the bound for \(J_n\) and (3) into (1) gives the asserted coefficient asymptotic. For irrational \(c/(2\pi)\), its cosine phase is dense in \([-1,1]\); for rational \(c/(2\pi)=p/q\) in lowest terms, the phase visits \(q\ge3\) equally spaced points on the circle and takes both signs. In either case its cosine exceeds a fixed positive number and is less than a fixed negative number along separate infinite subsequences. The leading \(n^{-5/2}\) term then dominates the \(O_c(n^{-3}\log(n+1))\) remainder, establishing infinitely many negative and positive \(I_n(c)\).

Schoenberg's criterion says that every Legendre coefficient of a continuous positive-semidefinite zonal kernel on \(\mathbb S^2\) must be nonnegative. The negative coefficients exclude \(\mathbb S^2\). Every higher-dimensional sphere contains an isometric great \(\mathbb S^2\), so restriction excludes all \(d\ge2\). Combining with the positive cases proves the classification.

## Verification
Identity (1) follows from the differential equation and two integrations by parts. Identity (2) is an exact generating-function coefficient extraction, not a numerical approximation. The estimate of \(J_n\) controls the potential origin contribution, while DLMF §18.15 controls the single interior cutoff boundary at fixed \(c\). All quantifiers are explicit: the asymptotic is for each fixed \(0<c<\pi\), whereas the positivity classification covers every real \(c>0\) and integer \(d\ge1\). The companion script `verify_numeric.py` checks selected numerical Legendre coefficients and the exact integral identity to numerical tolerance; its finite checks are supplementary and are not the proof of infinitely many sign changes.

## Relationship to prior work
Schoenberg's harmonic criterion and Gneiting's 2013 survey provide the classical framework. The recent work of Feng and Ge on truncated-power kernels studies positive definiteness on \(\mathbb S^2\) for powers \(\delta\ge3/2\) at small support; it does not settle the linear power \(\delta=1\). The published quadratic geodesic Askey classification instead treats \((1-\theta/c)_+^2\): that family is positive definite through dimension three even for proper support and is not a stronger result implying the present linear-power boundary. The exact all-support, all-spherical-dimension phase boundary here is established separately by its Legendre asymptotic. The elementary circular Fourier positivity is classical and is not claimed as novel by itself.

## Limitations
No uniform remainder is asserted as \(c\to0\) or \(c\to\pi\), nor is an effective bound claimed for the first negative Legendre degree. This theorem treats only the linear truncated-power profile, not arbitrary compactly supported covariances or higher powers. Its novelty comparison relies on the inspected literature and records; a previously unlocated equivalent classification remains a bibliographic risk. Numerical checks do not independently certify the infinite-dimensional argument.

## References
[1] H. Feng and Y. Ge, *Isotropic Positive Definite Functions on Spheres*, arXiv:2604.11187v1, first public 13 April 2026, especially Theorems 1.7 and 1.9. https://arxiv.org/abs/2604.11187

[2] T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, Bernoulli 19 (2013), arXiv:1111.7077, especially the Schoenberg characterization, circle criterion, and the Askey family. https://arxiv.org/abs/1111.7077

[3] NIST Digital Library of Mathematical Functions, §18.15(iii), Legendre asymptotic formulas 18.15.12–13. https://dlmf.nist.gov/18.15

[4] R. K. Beatson, W. zu Castell and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437 (2011). https://arxiv.org/abs/1110.2437

[5] *Exact spherical dimension and support boundary for the quadratic geodesic Askey kernel*, publicly archived mathematical research result (27 October 2026), specifically the quadratic rather than linear cutoff.
