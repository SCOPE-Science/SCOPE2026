# Exact two-step total-variation optimum for \(\mathrm{SU}(2)\) conjugacy-class walks

## Finding
For each \(0\le\theta\le\pi\), let \(\mu_\theta\) be the unique conjugation-invariant probability on the class of \(\mathrm{SU}(2)\) with trace \(2\cos\theta\). Let \(m\) denote normalized Haar probability, and use \(d_{\mathrm{TV}}(\nu,m)=\sup_E|\nu(E)-m(E)|\). The sharp two-step minimization is
\[
\min_{0\le\theta\le\pi}d_{\mathrm{TV}}(\mu_\theta^{*2},m)=0.10253004609429855\ldots.
\]
Precisely two angles attain the minimum:
\[
\theta_* = \frac12\arccos(1-L_*)=75.403373880458\ldots^\circ,
\qquad \pi-\theta_*,
\]
where \(L_*\) is the **unique** root in \((\pi/2,2)\) of
\[
4L^7(2-L)-4\pi^2L^2+\pi^4=0.
\]
The exact minimum is \(H(1-L_*)+\frac2\pi\arcsin b_* -b_*/L_*\), with
\[
H(a)=\frac12+\frac{a\sqrt{1-a^2}+\arcsin a}{\pi},\qquad
b_* = \sqrt{1-\frac{\pi^2}{4L_*^2}}.
\]
In particular the equatorial class \(\theta=\pi/2\) has strictly larger two-step variation distance \(0.11542101470975824\ldots\). The familiar \(L^2\)-spectral tuning \(|\cos\theta|=1/4\) also has different two-step variation distance \(0.102532502980557\ldots\); the statement here is about **two-step total variation**, not the limiting \(L^2\) spectral rate.

## Assumptions and scope
Identify \(\mathrm{SU}(2)\) with unit quaternions. For \(0<\theta<\pi\), a class-uniform element has the form \(g=\cos\theta+\sin\theta\,u\), with \(u\) uniform on the imaginary unit sphere \(S^2\). The two samples defining \(\mu_\theta^{*2}\) are independent. At \(\theta=0,\pi\) the class is a central point mass. Define the real scalar coordinate \(t(g)=\operatorname{Re}g\in[-1,1]\); every conjugation-invariant measure is determined by its radial pushforward. Conditional on a noncentral scalar value, both measures in this theorem have the same uniform angular law. Therefore their total-variation distance equals the one-dimensional radial total-variation distance. \(\mu_\theta\) itself is singular against Haar, so its one-step total variation is exactly one at every angle; two steps are the first nontrivial horizon.

## Proof
**1. Exact radial convolution law.** For independent uniform \(u,v\in S^2\), the scalar part of \((c+su)(c+sv)\), with \(c=\cos\theta\), \(s=\sin\theta\), is \(c^2-s^2(u\cdot v)\). Since \(u\cdot v\) is uniform on \([-1,1]\), its scalar distribution is uniform on \([a,1]\), where
\[
a=\cos(2\theta),\qquad L=1-a=2\sin^2\theta.\]
For \(0<\theta<\pi\) the radial density is \(f_a(t)=L^{-1}\mathbf1_{[a,1]}(t)\). The Haar scalar density on \(\mathrm{SU}(2)\cong S^3\) is
\[
h(t)=\frac2\pi\sqrt{1-t^2}\,\mathbf1_{[-1,1]}(t).\]
Consequently \(F(a):=d_{\mathrm{TV}}(\mu_\theta^{*2},m)=\frac12\int_{-1}^1|f_a-h|\,dt\), and \(F(1)=1\) by the endpoint convention.

**2. All-parameter exact variation formula.** Write \(H(a)=\int_{-1}^a h(t)\,dt\) as above. If \(L\le\pi/2\), then \(1/L\ge2/\pi\ge h(t)\) on \([a,1]\). Thus \(F(a)=H(a)\). If \(\pi/2<L\le2\), set
\[b(L)=\sqrt{1-\frac{\pi^2}{4L^2}}.\]
Now \(f_a<h\) exactly for \(t\in(-b,b)\), which lies inside \([a,1]\). Indeed \(a<-b\) follows from \(L^3(2-L)<\pi^2/4\), because the maximum of \(L^3(2-L)\) on \([0,2]\) is \(27/16<\pi^2/4\). Integrating the positive part of \(h-f_a\) gives
\[
F(a)=H(a)+\int_{-b}^b\left(h(t)-\frac1L\right)\,dt
=H(a)+\frac2\pi\arcsin b-\frac bL.
\]
Both branches agree at \(L=\pi/2\), where \(b=0\).

**3. Differentiation and candidate isolation.** In the first regime \(F'(a)=h(a)>0\) for interior \(a\). In the second, the moving-boundary terms vanish because \(h(\pm b)=1/L\), yielding
\[
F'(a)=\frac2\pi\sqrt{L(2-L)}-\frac{2b(L)}{L^2}.
\]
Both summands are nonnegative. Squaring their comparison and clearing positive denominators shows that the sign of \(F'(a)\) equals the sign of
\[P(L)=4L^7(2-L)-4\pi^2L^2+\pi^4.\]
Its derivative is
\[
P'(L)=8L\bigl[L^5(7-4L)-\pi^2\bigr]<0\quad(\pi/2\le L\le2).
\]
Indeed \(L^5(7-4L)\) decreases for \(L\ge3/2\), is at most \(243/32\) there, and \(243/32<\pi^2\). At the two endpoints, \(P(\pi/2)>0\), whereas \(P(2)=\pi^2(\pi^2-16)<0\). Hence there is exactly one zero \(L_*\). In increasing \(a\), the derivative is negative before \(a_*=1-L_*\) and positive afterwards, so \(a_*\) is the unique global minimizer over \([-1,1]\).

**4. Exact angle classification and boundary.** The equation \(\cos2\theta=a_*\in(-1,1)\) has precisely the two solutions \(\theta_*\) and \(\pi-\theta_*\) on \([0,\pi]\). At the central endpoints \(\theta=0,\pi\), the square of the point-mass step remains a point mass and has distance one, so neither is an optimizer. This completes the proof for every parameter.

## Verification
The standalone Python file `verify.py` evaluates the unique polynomial root by bracketed bisection, checks stationarity, evaluates the closed variation formula, and independently integrates the absolute radial-density difference over its exact sign intervals. It tests a finite collection of parameters on both sides of the analytic branch transition. The universal monotonicity, uniqueness and endpoint assertions follow from the displayed calculus and polynomial inequalities; finite numerical comparisons are supplemental, not proofs.

## Relationship to prior work
The fixed-geodesic-step walk is the classical spherical averaging construction and here appears as convolution by a class probability on a compact group. Su studied the analogous sphere walk using discrepancy and its harmonic/Gelfand-pair expansion, obtaining asymptotic discrepancy bounds rather than this two-step \(L^1\) optimum. Mangoubi and Smith studied geodesic walks of fixed step time and derived manifold-uniform mixing bounds in Wasserstein distance. Schär and Stier developed dimension-independent Wasserstein bounds for a different geodesic-sampling kernel that samples along a random great circle. Those results motivate the distinction between finite-time total variation and geometric or spectral convergence; none of their examined claims specifies the exact optimizer or the unique polynomial root above.

## Limitations
This theorem is specifically for the square of a single conjugacy-class probability on \(\mathrm{SU}(2)\). It does not optimize arbitrary central probability mixtures, noncentral kernels, later finite horizons, \(L^2\) norms, or walks on other compact groups. The algebraic equation has coefficients involving \(\pi\); no claim of algebraicity over the rationals is made. The independently unverified possibility of older specialized class-convolution \(L^1\) tables remains a historical-priority risk. No independent mathematical audit has been performed.

## References
- Philip Schär and Thilo D. Stier, *A Dimension-Independent Bound on the Wasserstein Contraction Rate of a Geodesic Random Walk on the Sphere*, first public September 16, 2023, https://arxiv.org/abs/2309.09097 .
- Oren Mangoubi and Aaron Smith, *Rapid Mixing of Geodesic Walks on Manifolds with Positive Curvature*, first public September 9, 2016, https://arxiv.org/abs/1609.02901 .
- Francis Edward Su, *Discrepancy Convergence for the Drunkard's Walk on the Sphere*, first public February 2001, https://arxiv.org/abs/math/0102205 .
