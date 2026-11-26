# Exact Lambert-W period law for an unbounded piecewise linear-quadratic pseudo-center

## Finding

For the normalized flow
\[
(\dot X,\dot Y)=
\begin{cases}
(X-Y,-1),&X\le 0,\\
(-2X-Y+Y^2,1),&X\ge 0,
\end{cases}
\]
the unbounded periodic annulus is parameterized by \(\kappa\in(-1,0)\), and their least period is
\[
T(\kappa)=2\bigl[W_0(\kappa/e)-W_{-1}(\kappa/e)\bigr].
\]
Here \(W_0\) and \(W_{-1}\) are the two real branches of Lambert's \(W\) function. The period increases strictly from zero to infinity. At the outer end of the unbounded annulus it has a logarithm-plus-logarithm-of-a-logarithm divergence:
\[
T(\kappa)=2\left[L+\log L+o(1)\right],\qquad
L=\log\!\left(\frac{e}{-\kappa}\right),\quad \kappa\uparrow0.
\]

## Assumptions and scope

The vector field is interpreted piecewise, with trajectories crossing the switching line \(X=0\) transversely except at the limiting orbit through the origin. Time is the normalized time \(\theta\). The claim concerns the global pseudo-center family
\[
\dot X=X-Y,\quad \dot Y=-1\quad(X\le0),\qquad
\dot X=-2X-Y+Y^2,\quad \dot Y=1\quad(X\ge0),
\]
which is the canonical form obtained from the \(\delta>0\) linear-quadratic family in Barkat, Benterki, and Ponce after \((X,Y,\theta)=(\delta^2x,\delta y,\delta\tau)\). The original-time period is the normalized period divided by \(\delta\). No assertion is made for the separate \(\delta=0\) subfamily or for perturbations of this vector field.

## Proof

On the left half-plane, integration of \(\dot X=X-Y\), \(\dot Y=-1\) gives the orbit family
\[
X+\kappa e^{-Y}-Y+1=0.
\]
At a crossing \(X=0\), the crossing height \(y\) therefore satisfies
\[
F(y):=(y-1)e^y=\kappa.
\]
On the right half-plane, integration gives
\[
2X+\lambda e^{-2Y}-(Y-1)^2=0.
\]
At \(X=0\), this orbit family has \(\lambda=(y-1)^2e^{2y}=F(y)^2\). For the periodic component with crossing heights \(p\) and \(q\), \(\lambda=\kappa^2\) and
\[
X(Y)=\frac12e^{-2Y}\bigl(F(Y)^2-\kappa^2\bigr).
\]
Since \(F(Y)<\kappa<0\) for \(p<Y<q\), this branch satisfies \(X(Y)>0\) throughout the open interval. The additional root of \(F(Y)=-\kappa\), which lies above \(1\), is separated from this branch because \(|F(Y)|<|\kappa|\) between \(q\) and that root, so the corresponding level has \(X<0\) there.

Now \(F'(y)=ye^y\). The function \(F\) decreases on \((-\infty,0)\), increases on \((0,\infty)\), has minimum \(F(0)=-1\), and satisfies \(F(y)\to0^-\) as \(y\to-\infty\) and \(F(1)=0\). Hence for every \(\kappa\in(-1,0)\) there are exactly two roots \(p<0<q<1\). The left flight moves from \(q\) to \(p\) with \(\dot Y=-1\), so its duration is \(q-p\); the right flight moves from \(p\) to \(q\) with \(\dot Y=1\), with the same duration. Therefore \(T(\kappa)=2(q-p)\).

Solving \((y-1)e^y=\kappa\) gives \(y=1+W_j(\kappa/e)\). The root \(p\) corresponds to \(W_{-1}\), and \(q\) to \(W_0\), yielding the stated formula. Implicit differentiation gives
\[
p'(\kappa)=\frac{1}{p e^p}<0,\qquad
q'(\kappa)=\frac{1}{q e^q}>0,
\]
so \(T'(\kappa)=2(q'-p')>0\).

For the inner endpoint, expansion at \(y=0\) gives
\[
F(y)=-1+\frac{y^2}{2}+\frac{y^3}{3}+O(y^4).
\]
Inverting the two branches around \(\kappa=-1\) yields
\(q-p=2\sqrt{2(\kappa+1)}+O((\kappa+1)^{3/2})\), proving the stated small-period law.

For the outer endpoint, put \(L=\log(e/(-\kappa))\). The standard defining equation \(W_{-1}(\kappa/e)e^{W_{-1}(\kappa/e)}=\kappa/e\) gives
\[
W_{-1}(\kappa/e)=-L-\log L+o(1)\quad(\kappa\uparrow0),
\]
whereas \(W_0(\kappa/e)=o(1)\). Substitution into the exact period formula proves
\(T(\kappa)=2[L+\log L+o(1)]\). Since \(p\to-\infty\) and \(q\to1\), this divergence occurs at the unbounded edge of the periodic annulus, not at a finite saddle separatrix.

## Verification

The proof uses only the two explicit half-plane orbit equations, the signs of \(F'(y)\), the two real Lambert-\(W\) branches on \((-1/e,0)\), and endpoint expansions. Direct differentiation confirms the orbit equations along their respective vector fields. Numerical spot checks at \(\kappa=-0.9999,-0.9,-0.5,-0.1,-10^{-4}\) are consistent with strict period growth; the asymptotic coefficients were also checked against the exact Lambert-\(W\) formula. These finite checks are corroborative only; the proof above establishes the claims for the full interval \(\kappa\in(-1,0)\).

## Relationship to prior work

Barkat, Benterki, and Ponce classify the global phase portraits of several piecewise quadratic systems with a pseudo-center, including the canonical linear-quadratic family used here. Their analysis supplies the orbit equations and establishes the unbounded periodic annulus, but does not state this exact physical-time period map or its Lambert-\(W\) logarithm-plus-logarithm-of-a-logarithm asymptotic. The present result quantifies the timing along that already identified annulus rather than claiming a new existence or phase-portrait theorem.

Related period-function results for piecewise-affine or piecewise-linear systems study different vector-field classes or separation geometries. In particular, the five spectral edge laws for a balanced two-zone affine family and the four-sector relay-oscillator period law do not cover the present linear-quadratic canonical flow. A 2026 abstract on period functions for piecewise-linear systems is a relevant but not decisive priority risk: its accessible summary does not state the Lambert-\(W\) formula or the present quadratic half-plane system, and its full text was not inspected.

## Limitations

The formula is specific to the normalized system above. The endpoint \(\kappa=-1\) is the limiting orbit through the origin and is not a nontrivial periodic orbit; \(\kappa=0\) is not attained by a finite crossing cycle. The logarithm-plus-logarithm-of-a-logarithm expansion is for \(\kappa\uparrow0\) at fixed normalized parameters. No stability claim, perturbation theorem, or independent validation is asserted.

## References

1. M. Barkat, R. Benterki, and E. Ponce, “Global phase portraits of piecewise quadratic differential systems with a pseudo-center,” *International Journal of Bifurcation and Chaos* 34 (2024), DOI: 10.1142/S0218127424500329. First public date used here: 2024-03-06.
2. M. Barkat, *Phase planes and bifurcations in planar linear-quadratic differential systems with a pseudo-focus*, doctoral thesis, Mohamed El Bachir El Ibrahimi University of Borj Bou Arréridj, 2024, Chapter 5, §5.2.1, especially system (5.35) and Theorem 5.1. Public full-text repository bitstream: cbd03bb4-eb3c-4e18-a57f-4dd1b25b019c.
3. S. Wang and J. Yang, “Period functions and critical periods of piecewise linear system,” *Electronic Journal of Differential Equations* (2020), article 79, DOI: 10.58997/ejde.2020.79.
4. A. C. Rezende, M. A. S. Santos, and J. Torregrosa, “The period function of centers at infinity in planar piecewise linear systems,” *Bulletin des Sciences Mathématiques* 210 (2026), article 103809, DOI: 10.1016/j.bulsci.2026.103809.
