# A sharp positivity-time staircase for three-state circulant semigroups

## Finding

Write \(\mathbf 1=(1,1,1)^{\mathsf T}\), \(P=\mathbf1\mathbf1^{\mathsf T}/3\), and
\[
J=\frac1{\sqrt3}\begin{pmatrix}0&-1&1\\1&0&-1\\-1&1&0\end{pmatrix}.
\]
For arbitrary \(\delta,\omega>0\), consider the real normal generator
\[
A_{\delta,\omega}=-\delta(I-P)+\omega J.
\]
It has spectrum \(\{0,-\delta+i\omega,-\delta-i\omega\}\), and \(e^{tA_{\delta,\omega}}\) converges to the positive rank-one matrix \(P\). Let \(\mathcal P_{\delta,\omega}=\{t\geq0:e^{tA_{\delta,\omega}}\text{ is entrywise nonnegative}\}\), and put \(a=\delta/\omega\).

**Exact test at every time.** Set \(\theta=\omega t\). Then
\[
t\in\mathcal P_{\delta,\omega}
\quad\Longleftrightarrow\quad
 e^{a\theta}\ge F(\theta),\qquad
F(\theta)=\max\{-2\cos\theta,\,\cos\theta+\sqrt3|\sin\theta|\}.
\]
In particular, \(\mathcal P_{\delta,\omega}=[0,\infty)\) precisely when \(a\ge\sqrt3\).

**Sharp component count.** For \(0<a<\sqrt3\) define
\[
H(a)=\log\frac{2}{\sqrt{1+a^2}}+a\arctan a,
\quad R(a)=\frac{3H(a)}{\pi a},\quad
N(a)=\left\lceil\frac{R(a)-1}{2}\right\rceil.
\]
The set of **strictly negative matrix-entry times** is a disjoint union of exactly \(N(a)\) nonempty open intervals. The nonnegative-time set \(\mathcal P_{\delta,\omega}\) has exactly \(N(a)+1\) connected components, including the singleton \(\{0\}\). For \(a\ge\sqrt3\), there are no failure intervals and \(\mathcal P_{\delta,\omega}\) has one component.

More precisely, the failure intervals are indexed by the integers
\[
k\ge0\quad\text{such that}\quad 2k+1<R(a).
\]
For each such \(k\), the interval lies in the angular cell \((2\pi k/3,2\pi(k+1)/3)\), contains the point \(\theta_k=(2k+1)\pi/3-\arctan a\), and its endpoints are given by the two solutions of
\[
e^{a\theta}=2\cos\left(\theta-\frac{(2k+1)\pi}{3}\right)
\]
inside the closed cell (for \(k=0\), the left endpoint is \(0\)). At equality \(2k+1=R(a)\), the corresponding cell has one nonnegative tangency, not a failure interval.

For every integer \(k\ge1\), there is a unique \(a_k\in(0,\sqrt3)\) satisfying \(R(a_k)=2k+1\). These are the exact parameter thresholds at which successive transient sign-loss intervals are born as \(a\) decreases. They satisfy \(a_1\approx0.228903469804832\), \(a_2\approx0.134093311567059\), and \(a_3\approx0.095175044126649\). As \(a\downarrow0\),
\[
N(a)\sim\frac{3\log2}{2\pi a}.
\]
Thus, although each fixed member is strictly positive at every sufficiently large time, this **single three-dimensional family** has arbitrarily many alternating negative and nonnegative time windows.

**Minimal dimension.** Every real \(1\times1\) or \(2\times2\) matrix whose exponential is entrywise nonnegative at all sufficiently large times in fact generates an entrywise nonnegative semigroup at **every** nonnegative time. Hence dimension three is minimal for the disconnected positivity-time phenomenon, without a normality or conservation assumption on the lower-dimensional matrices.

## Assumptions and scope

All matrix inequalities mean entrywise inequalities in the standard coordinatewise order on \(\mathbb R^3\). Parameters \(\delta,\omega\) are strictly positive; \(t\ge0\). The semigroup has constant row and column sums one, but it is **not** a Markov semigroup when \(a<\sqrt3\), since some entries are then negative for small times. The quantity \(N(a)\) counts open connected components of the **failure set**, not eigenvalues or approximate numerical sign changes. The spectral parameters and component count are exact, whereas quoted decimal threshold values are approximations.

## Proof

**1. Explicit exponential and entrywise envelope.** The projection and skew matrix obey \(P^2=P\), \(PJ=JP=0\), and \(J^2=-(I-P)\). Their commuting functional calculus gives
\[
e^{tA_{\delta,\omega}}=P+e^{-\delta t}\bigl[\cos(\omega t)(I-P)+\sin(\omega t)J\bigr].
\]
The three diagonal entries equal \((1+2e^{-\delta t}\cos\theta)/3\). The six off-diagonal entries consist of three copies each of
\[
\frac13\bigl(1-e^{-\delta t}\cos\theta\bigr)
\pm\frac{e^{-\delta t}}{\sqrt3}\sin\theta.
\]
Requiring all nine entries to be nonnegative is exactly \(e^{a\theta}\ge F(\theta)\). In particular, \(e^{a\theta}>2\) suffices for strict positivity, proving eventual strict positivity.

**2. Reduction to one concave hump per cell.** Direct trigonometric comparison yields, for each integer \(k\ge0\),
\[
F(\theta)=2\cos\left(\theta-\frac{(2k+1)\pi}{3}\right),\quad
\frac{2k\pi}{3}\le\theta\le\frac{2(k+1)\pi}{3}.
\]
The argument of the cosine on a cell belongs to \([-\pi/3,\pi/3]\), so its logarithm is defined. Put \(c_k=(2k+1)\pi/3\) and
\[
g_k(\theta)=\log(2\cos(\theta-c_k))-a\theta.
\]
Strict entrywise negativity occurs on precisely the part of a cell where \(g_k(\theta)>0\). Since \(g_k''(\theta)=-\sec^2(\theta-c_k)<0\), there can be at most one connected interval of failure per cell; its two endpoints have \(g_k\le0\), with equality only at the origin of the first cell.

**3. Exact maxima and sharp count.** For \(0<a<\sqrt3\), the unique cell maximum occurs at \(\theta_k=c_k-\arctan a\), which lies strictly inside the cell. Its value is
\[
\max_{\theta\in[2k\pi/3,2(k+1)\pi/3]}g_k(\theta)
=\log\frac2{\sqrt{1+a^2}}+a\arctan a-a\frac{(2k+1)\pi}{3}
=H(a)-a\frac{(2k+1)\pi}{3}.
\]
Thus cell \(k\) contributes one open failure interval if and only if \(2k+1<R(a)\), and none otherwise. Counting these nonnegative integers gives \(N(a)=\lceil(R(a)-1)/2\rceil\). The first cell has \(g_0(0)=0\) and \(g_0'(0)=\sqrt3-a>0\), so its failure interval starts immediately after zero. Distinct failure intervals are separated by strictly positive matrix times at their cell boundaries. The continuous complement on the nonnegative half-line consequently has \(N(a)+1\) connected components, counting the isolated origin.

For \(a\ge\sqrt3\), both types of off-diagonal generator entry, \(\delta/3\pm\omega/\sqrt3\), are nonnegative. Adding a sufficiently large scalar multiple of the identity to the generator makes every matrix entry nonnegative, so the exponential series proves entrywise nonnegativity for all \(t\ge0\). Conversely, if \(a<\sqrt3\), one off-diagonal generator entry is negative, and the first-order expansion of the exponential gives negative entries for every sufficiently small positive time.

**4. Monotone bifurcations and growth.** Differentiation gives
\[
H'(a)=\arctan a,\qquad
\frac{d}{da}\frac{H(a)}a=\frac{\tfrac12\log(1+a^2)-\log2}{a^2}<0
\quad(0<a<\sqrt3).
\]
Also \(R(a)\to\infty\) as \(a\downarrow0\), and \(R(a)\to1\) as \(a\uparrow\sqrt3\). Every horizontal level \(2k+1\), \(k\ge1\), is therefore attained exactly once. The expansion \(H(a)=\log2+a^2/2+O(a^4)\) proves \(N(a)=3\log2/(2\pi a)+O(1)\).

**5. Dimension two is rigid.** Let \(B\) be any real \(2\times2\) generator with \(e^{tB}\) entrywise nonnegative for every sufficiently large \(t\). If its eigenvalues are nonreal, write them \(m\pm ib\), \(b>0\). Cayley–Hamilton gives \(e^{tB}=e^{mt}[I\cos(bt)+(B-mI)\sin(bt)/b]\). Nonreal eigenvalues require the two off-diagonal entries of \(B\) to be nonzero of opposite sign. Both exponential off-diagonal entries oscillate in sign for arbitrarily large \(t\), a contradiction. If its eigenvalues are real \(\lambda_1,\lambda_2\), the off-diagonal entries are \(B_{ij}\phi(t)\), where \(\phi(t)=(e^{\lambda_1t}-e^{\lambda_2t})/(\lambda_1-\lambda_2)>0\) for distinct eigenvalues and \(\phi(t)=te^{\lambda_1t}>0\) for repeated eigenvalues. Eventual nonnegativity therefore forces both \(B_{ij}\ge0\). A real matrix with nonnegative off-diagonal entries generates an entrywise nonnegative exponential for every nonnegative time (by shifting its diagonal and using the positive exponential series). The one-dimensional case is immediate.

## Verification

The included `check.py` is a standard-library Python program. It independently computes matrix exponentials by scaling, Taylor expansion, and squaring rather than by the stated trigonometric formula. It compares all nine matrix entries and the sign criterion for multiple parameter ratios and times; checks the algebraic identities \(J^2=-(I-P)\), \(JP=PJ=0\); verifies the predicted number and location of angular failure cells; and brackets early bifurcation values and failure endpoints. Run `python3 check.py` from this file's directory. Its current successful execution reports **1,276 finite-precision assertions**. Such tests are supplemental checks, not a proof for all times or all parameters; the preceding analytic argument provides the infinite-parameter proof.

## Relationship to prior work

Glück's 2022 survey gives a three-dimensional rotation-plus-decay example, equivalent after an orthogonal basis choice and orientation to a fixed member of the present family, to demonstrate eventual positivity without all-time positivity. That example and the general eventual-positive-semigroup criterion are **prior work**, not new constructions. The finding here is specifically the exact, globally quantified **time-set topology**, sharp damping/frequency phase staircase and the ability to produce an arbitrary finite number of positivity components already in the smallest possible matrix dimension. Subsequent work of Glück–Hölz and Arora–Glück treats general eventual cone invariance and irreducibility, respectively. The older Daners–Glück–Kennedy spectral theory supplies background sufficient conditions but does not, in the inspected relevant text, state the component-count formula. The fully explicit result is compatible with those theories; it is not a counterexample to any general spectral characterization.

## Limitations

This statement concerns the particular real normal circulant family, not every eventually positive matrix generator or arbitrary cones. The two-dimensional rigidity observation is elementary and is not separately claimed as novel. Existing eventual positivity of the three-dimensional example is known. The full literature record is not exhaustively searchable, so historical priority of the quantified staircase remains a risk. Independent mathematical verification has not occurred. The numerical checker cannot establish either originality or infinite-dimensional/infinite-parameter correctness.

## References

1. Jochen Glück, *Evolution equations with eventually positive solutions*, arXiv:2202.10133v1, first public 21 February 2022, Section 2, Example 5; https://arxiv.org/html/2202.10133v1 .
2. Jochen Glück and Julian Hölz, *Eventual cone invariance revisited*, arXiv:2303.07809, first public 14 March 2023; https://arxiv.org/html/2303.07809v2 .
3. Sahiba Arora and Jochen Glück, *Irreducibility of eventually positive semigroups*, arXiv:2307.04627, first public 10 July 2023; https://arxiv.org/abs/2307.04627 .
4. Daniel Daners, Jochen Glück and James B. Kennedy, *Eventually and asymptotically positive semigroups on Banach lattices*, arXiv:1511.05294, first public 17 November 2015; https://arxiv.org/pdf/1511.05294 .
5. D. Noutsos and M. J. Tsatsomeros, *Reachability and holdability of nonnegative states*, SIAM Journal on Matrix Analysis and Applications 30 (2008), 700–712; https://doi.org/10.1137/070693850 .
