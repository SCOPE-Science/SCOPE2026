# A sharp antiphase sink ceiling and coexistence with escape in a coupled Gaussian map

## Finding
Let \(a>0\), \(b\in\mathbb R\), and consider the planar map
\[
F_{a,b}(x,y)=\bigl(f_a(x)+b(y-x),\ f_a(y)+b(x-y)\bigr),
\qquad f_a(t)=at(1-t^2)e^{-t^2}.
\]
The anti-diagonal \(\mathcal A=\{(s,-s):s\in\mathbb R\}\) is invariant. Write \(c=(1+2b)/a\). The number of **nonzero** fixed points on \(\mathcal A\) is exactly zero for \(c\notin[-e^{-2},1)\); two for \(c=-e^{-2}\), \(c=0\), or \(0<c<1\); and four for \(-e^{-2}<c<0\). Every such point is \((\pm\sqrt u,\mp\sqrt u)\), where
\[
(1-u)e^{-u}=c,\qquad u>0,
\]
or equivalently \(u=1-W_j(ec)\) on whichever real Lambert-\(W\) branches give \(u>0\). On \(-e^{-2}<c<0\), the larger-radius pair \(u>2\) always has an expanding anti-diagonal multiplier.

The existence of a **hyperbolic sink on the anti-diagonal for some coupling \(b\)** has a sharp gain threshold:
\[
\boxed{\exists b\in\mathbb R:\ F_{a,b}\text{ has a nonzero anti-diagonal hyperbolic sink}\ \Longleftrightarrow\ 0<a<e^2.}
\]
More precisely put
\[
b_{\rm fold}(a)=-\frac12-\frac{a}{2e^2}.
\]
For each \(0<a<e^2\), there exists \(\eta(a)>0\) such that at every \(b\in(b_{\rm fold}(a),b_{\rm fold}(a)+\eta(a))\) **exactly two anti-diagonal fixed points are hyperbolic sinks, while two more have an expanding anti-diagonal multiplier**. The interval can be chosen entirely within \(b<-1/2\), where the same planar map also has a nonempty open set of orbits escaping to infinity. Thus two finite attracting equilibria coexist with an open escaping basin. At the endpoint \(b=b_{\rm fold}(a)\), the two radius branches meet at \(u=2\) with multipliers \(1\) and \(-a/e^2\); when \(a=e^2\), they are exactly \((1,-1)\). For \(b\downarrow b_{\rm fold}(a)\) from above,
\[
u_{\pm}(b)=2\pm 2e\sqrt{\frac{b-b_{\rm fold}(a)}a}+O(b-b_{\rm fold}(a)).
\]
No claim is made about all off-diagonal fixed points or about global attraction.

## Assumptions and scope
All maps act on the full real plane, not a clipped square. The gain is strictly positive and the diffusive coupling is any real number. A hyperbolic sink means both eigenvalues of the full two-dimensional derivative have modulus strictly below one. An expanding multiplier means a real derivative eigenvalue strictly above one. Statements of counts exclude the origin, which is always fixed. The analytic branch multiplicities are counted as distinct real fixed points, not with algebraic multiplicity.

## Proof
**Invariant subspace and complete branch census.** Oddness of \(f_a\) gives
\[
F_{a,b}(s,-s)=(f_a(s)-2bs,-f_a(s)+2bs).
\]
A nonzero point is fixed precisely when \(g(u)=(1-u)e^{-u}=c\), with \(u=s^2>0\). Its derivative is \(g'(u)=(u-2)e^{-u}\). Consequently \(g\) strictly decreases from \(1\) at \(u=0\) to \(-e^{-2}\) at \(u=2\), then strictly increases to \(0\) from below. Counting the positive solutions and their two signs gives all the assertions about the numbers of antidiagonal fixed points. The Lambert equation follows by setting \(v=1-u\) and solving \(v e^v=ec\).

**Exact two-dimensional multipliers.** Since \(f_a'(s)=a e^{-u}(1-5u+2u^2)\) is even, the derivative at \((s,-s)\) has eigenvectors \((1,1)\) and \((1,-1)\), with normal and tangent eigenvalues respectively
\[
\lambda_+=a e^{-u}(1-5u+2u^2),\qquad
\lambda_-=\lambda_+-2b=1+2au(u-2)e^{-u}.
\]
The second equality uses \(1+2b=a(1-u)e^{-u}\). For \(u>2\), \(\lambda_->1\), excluding sinks on the outer branch. At \(u=2\), \((\lambda_-,\lambda_+)=(1,-a/e^2)\).

**Sinks exist for every \(0<a<e^2\).** As \(u\uparrow2\) from below, \(\lambda_-<1\) tends to \(1\), and \(\lambda_+\to-a/e^2\in(-1,0)\). Both moduli are therefore less than one for all sufficiently close \(u<2\). The map \(b(u)=[a(1-u)e^{-u}-1]/2\) is strictly decreasing for \(u<2\), approaching \(b_{\rm fold}\) from above. The corresponding inner pair are full-plane sinks. The outer pair exists for the same \(b\) and has \(\lambda_->1\). By making the parameter interval small enough, one also ensures \(b<-1/2\).

**No antidiagonal hyperbolic sinks when \(a\ge e^2\).** For \(1\le u<2\), define \(h(u)=e^{-u}(5u-2u^2-1)\). It is positive and strictly decreasing on \([1,2]\), since \(h'(u)=e^{-u}(2u^2-9u+6)<0\) there, and \(h(2)=e^{-2}\). Thus \(\lambda_+=-a h(u)\le-a/e^2\le-1\). At \(u=2\), \(\lambda_-=1\), and for \(u>2\), \(\lambda_->1\).

It remains to exclude \(0<u<1\). If \(0<u\le3/20\), then
\[
\lambda_+\ge a e^{-3/20}(1-5(3/20))
\ge\frac{e^{37/20}}4>1.
\]
If \(3/20\le u\le1\), the function \(q(u)=u(2-u)e^{-u}\) has a single interior maximum at \(u=2-\sqrt2\), so its minimum on that interval is at an endpoint. Each endpoint satisfies \(e^2 q(u)>1\): for \(u=1\), the value is \(e\), and for \(u=3/20\), it is \(111e^{37/20}/400>1\). Hence \(a q(u)>1\) and \(\lambda_-=1-2aq(u)<-1\). The exponential inequalities follow already from \(e^t>1+t+t^2/2\) at \(t=37/20\). This exhausts every \(u>0\) and proves the sharp gain ceiling.

**Fold expansion and coexistence.** Taylor's theorem gives \(g(2+v)=-e^{-2}+(e^{-2}/2)v^2+O(v^3)\). Substituting \(g(u)=(1+2b)/a\) proves the stated square-root splitting. The two sink basins contain open neighborhoods by the contraction theorem. Independently, whenever \(b<-1/2\), write \(s=(x+y)/2\), \(d=(x-y)/2\). With \(M_a=\sup|f_a|<\infty\), the second coordinate obeys \(d'=-2bd+g_0(s,d)\), \(|g_0(s,d)|\le M_a\); therefore \(|d'|\ge 2|b||d|-M_a\). Every initial condition with \(|d|>M_a/(2|b|-1)\) escapes geometrically, proving a nonempty open escaping basin. This final estimate also follows from the earlier same-map global boundedness theorem cited below; the direct inequality makes the coexistence self-contained.

## Verification
Execute `python3 verify.py` from this package. Its assertions test the Lambert-branch census numerically, reconstruct eigenvalues from the actual two-by-two Jacobian, and check explicit examples below, at, and above the sharp \(e^2\) gain threshold. The analytic monotonicity and inequalities above, not the finite tests, prove the universal claims.

## Relationship to prior work
Soula, Jahanshahi, Al-Barakati and Moroz (2023) introduce the exact coupling law and investigate numerical stability regions, critical curves, global basin geometry and synchronization. They identify the anti-diagonal but do not give this exact full antidiagonal fixed-point census or the gain ceiling. An independently published analysis of this same map (2026) determines the global compact-absorbing coupling interval \(-1/2\le b<1/2\) and proves escape outside it, but explicitly leaves finite-attractor classification open. The new theorem determines a distinct local branch and shows that stable antiphase equilibria can coexist with unbounded orbits on the escaping side. The original map's numerical diagrams do not imply the gain-uniform necessary-and-sufficient bound \(a<e^2\).

## Limitations
Only equilibria on the invariant anti-diagonal are counted. There may be equilibria elsewhere, other attractors and complicated basins. The stability criterion concerns strict hyperbolic sinks; at multiplier moduli equal to one, nonlinear stability is not classified. No uniqueness of finite attractors, global basin geometry or stochastic robustness is asserted. An unindexed equivalent classification could alter publication priority; this is not an independent audit.

## References
[1] Y. Soula, H. Jahanshahi, A. A. Al-Barakati and I. Moroz, *Dynamics and Global Bifurcations in Two Symmetrically Coupled Non-Invertible Maps*, Mathematics 11 (2023), 1517, first published 2023-03-21, https://doi.org/10.3390/math11061517.

[2] *A sharp global boundedness interval and logarithmic critical escape in a coupled Gaussian map*, 2026, public mathematical research record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-sharp-global-boundedness-interval-and-logarithmic-critical-esc--f463338d3c52/RESULT.md.
