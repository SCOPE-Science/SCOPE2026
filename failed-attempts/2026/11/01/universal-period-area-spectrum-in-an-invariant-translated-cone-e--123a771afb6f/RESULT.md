# Universal period-area spectrum in an invariant translated-cone-exchange trapezium

## Finding

For the identity-permutation, three-cone translated cone exchange described below, the invariant trapezium has a complete, angle-independent periodic-orbit census when the horizontal translation parameter is rational. If \(\lambda=p/q\in(0,1)\) in lowest terms, **every one** of the \(p+1\) least periods \(q,q+1,\ldots,q+p\) occupies positive planar area in the trapezium, and no other least period occurs there apart from boundary-convention exceptions. The fraction of trapezium area with least period \(q+j\) is

\[
\boxed{\Pr_{\mathrm{area}}(\text{least period}=q+j)
 =\frac{w_j(q+j)}{pq+p^2/2},\qquad
 w_0=w_p=\tfrac12,\quad w_j=1\ (1\le j\le p-1).}
\]

The same map has **no periodic points in the invariant horizontal intervals** (away from arbitrary boundary assignments) for irrational \(\lambda\). In that case each such horizontal interval is minimal and uniquely ergodic with normalized length measure. This rational/irrational dichotomy is independent of the cone angles.

More precisely, at an intermediate height let \(\delta=\lambda-y(\cot\alpha_0+\cot\alpha_2)\in(0,\lambda)\), set \(n=\lfloor q\delta\rfloor\) and \(\theta=q\delta-n\). When \(0<\theta<1\), the only least periods on that horizontal interval are \(q+n\) and \(q+n+1\), with length fractions

\[
\frac{(q+n)(1-\theta)}{q+q\delta}
\quad\text{and}\quad
\frac{(q+n+1)\theta}{q+q\delta},
\]

respectively. If \(\theta=0\), the sole least period is \(q+n\). The lower boundary has period \(q+p\); the upper boundary and the higher invariant strip have period \(q\) (with the usual half-open branch assignment).

## Assumptions and scope

Choose \(\alpha_0,\alpha_2\in(0,\pi/2)\) and \(\alpha_1=\pi-\alpha_0-\alpha_2>0\), and choose \(0<\lambda<1\). Put \(\eta=1-\lambda\). Divide the closed upper half-plane into successive cones \(P_0,P_1,P_2\) with angular widths \(\alpha_0,\alpha_1,\alpha_2\). Define the planar piecewise translation

\[
F(z)=\begin{cases}
 z-1,&z\in P_0,\\
 z-\eta,&z\in P_1,\\
 z+\lambda,&z\in P_2.
\end{cases}
\]

All statements about boundary trajectories adopt the natural half-open interval-exchange convention; the planar area assertions are independent of the arbitrary allocation of finitely many discontinuity lines. This is the nonrotating case of the family in Cockram--Ashwin--Rodrigues, arXiv:2312.17412, Section 3, whose Theorem 3.1 supplies the invariant horizontal intervals and the invariant trapezium. Let

\[
c=\cot\alpha_0+\cot\alpha_2>0,
\qquad y_*=\lambda/c.
\]

For \(0\le y\le y_*\), write \(u=y\cot\alpha_0\), \(v=y\cot\alpha_2\), and \(\delta=\lambda-cy\). Up to its boundary, the trapezium is

\[
\mathcal T=\{x+iy:0<y<y_*,\; u-1<x<\lambda-v\}.
\]

Its horizontal width is \(1+\delta\), and its area is

\[
|\mathcal T|=\frac{\lambda+\lambda^2/2}{c}.
\]

The full maximal invariant set also includes an unbounded strip above \(y_*\); the finite area probabilities in the theorem **refer only to \(\mathcal T\)**.

## Proof

**Step 1: Exact horizontal interval exchange.** At height \(0\le y<y_*\), make the horizontal coordinate change \(X=x-u+1\). The source's three translation branches simplify to the exact bijection on \([0,1+\delta)\):

\[
f_{\lambda,\delta}(X)=\begin{cases}
X+\lambda,&0\le X<1-\lambda+\delta,\\
X+\lambda-1,&1-\lambda+\delta\le X<1,\\
X-1,&1\le X<1+\delta.
\end{cases}\tag{1}
\]

Indeed the domain intervals have lengths \(1-\lambda+\delta\), \(\lambda-\delta\), and \(\delta\), and their images, in increasing order, are \([\lambda,1+\delta)\), \([\delta,\lambda)\), and \([0,\delta)\), so they partition \([0,1+\delta)\). At \(\delta=0\) the last interval is empty and (1) reduces to a rotation on \([0,1)\). At height \(y\ge y_*\), the source's two-interval exchange is also the circle rotation \(X\mapsto X+\lambda\pmod1\), after a translation of origin.

**Step 2: A concrete one-step-delay tower.** Let \(R_\lambda X=\{X+\lambda\}\) act on \([0,1)\), and let

\[
I_\delta=[1-\lambda,1-\lambda+\delta).
\]

For \(X\in[0,1)\setminus I_\delta\), equation (1) agrees with \(R_\lambda X\). For \(X\in I_\delta\), equation (1) first sends \(X\) to \(1+R_\lambda X\in[1,1+\delta)\) and then sends it to \(R_\lambda X\in[0,1)\). Thus (1) is exactly the integer-height tower over \(R_\lambda\) with return duration \(\tau(X)=1+\mathbf 1_{I_\delta}(X)\). Its invariant length measure has total mass \(1+\delta\). If \(\lambda\) is irrational, the rotation is minimal and uniquely ergodic; the explicit bounded tower is likewise minimal and uniquely ergodic, with normalized length measure. In particular it contains no periodic point.

**Step 3: Complete least periods at one rational height.** Write \(\lambda=p/q\), \(1\le p<q\), \(\gcd(p,q)=1\). Every base orbit under \(R_\lambda\) visits a uniformly spaced grid of \(q\) points and has least period \(q\). Its return-cycle duration in (1) is precisely

\[
q+m(X),\qquad m(X)=\#\{0\le k<q:R_\lambda^kX\in I_\delta\}.
\]

No shorter physical cycle is possible, since a return to the same tower state requires an integer number of base turns, with the smallest positive number being \(q\). A half-open circular interval of length \(\delta\) contains either \(\lfloor q\delta\rfloor\) or \(\lceil q\delta\rceil\) points of every translated \(q\)-grid. Write \(n=\lfloor q\delta\rfloor\) and \(\theta=\{q\delta\}\). Under normalized base length measure, the frequency of \(m=n+1\) is \(\theta\): indeed \(\int m(X)\,dX=q\delta=n+\theta\). The frequency of \(m=n\) is \(1-\theta\). Lifting a base class with visit count \(m\) into the tower multiplies its length by \(1+m/q\), because the \(q\)-orbit spends exactly \(m\) of its visits in \(I_\delta\). Division by the total length \(1+\delta\) gives the stated two physical-length fractions. For integer \(q\delta\), every grid has exactly that number of visits, so a single period remains.

**Step 4: Integrate the period layers in the plane.** Change vertical coordinate from \(y\) to \(t=q\delta\). Then \(|dy|=dt/(qc)\) and \(0<t<p\) covers the trapezium. On each interval \(j<t<j+1\), the actual horizontal lengths of points of periods \(q+j\) and \(q+j+1\) are, respectively,

\[
\frac{(q+j)(j+1-t)}q,
\qquad \frac{(q+j+1)(t-j)}q.
\]

Each triangular weight integrates to \(1/2\). Therefore the planar area of the period-\(q+j\) class is

\[
\frac{w_j(q+j)}{q^2c},\qquad
w_0=w_p=\tfrac12,\quad w_j=1\ (1\le j\le p-1).
\]

The sum is \((pq+p^2/2)/(q^2c)=|\mathcal T|\); division gives the boxed period-area spectrum. Every weight is positive, so the spectrum contains exactly \(p+1\) distinct least periods with positive area. At the lower boundary \(\delta=\lambda\), exactly \(p\) of the \(q\) grid visits lie in the delayed interval, giving least period \(p+q\). At and above the upper boundary \(\delta=0\), the map is an ordinary \(q\)-periodic rotation. All claims follow. \(\square\)

## Verification

An independent-of-proof exact-rational script, `period_spectrum_check.py`, performs 8,091 rational orbit/least-period checks and 383 integrated spectrum equalities across reduced rational parameters, including degenerate horizontal boundaries. Its sole third-party dependency is the Python standard library. Invoke `python3 period_spectrum_check.py`. The run used to prepare this note printed `PASS` for both suites and the \(\lambda=2/5\) area fractions \((5/24,1/2,7/24)\). These finite checks corroborate only the concrete algebra; the full rational/irrational claims and every-height quantifiers are established by Steps 1--4.

## Relationship to prior work

Cockram, Ashwin and Rodrigues (2023 preprint; 2025 journal publication), Theorem 3.1 and equation (3.7), provide the exact identity-permutation cone-exchange family, the maximal invariant set, its trapezium, and its three-interval horizontal exchanges. Those are explicitly credited starting points, not claimed discoveries. Their Theorem 4.5 studies a different rotating, four-cone family of invariant curves. The present contribution is the explicit rotation-with-delay model of the three-cone slices and, especially, the complete two-dimensional, angle-independent area distribution of their least periods for **all** rational translations. Classical facts about irrational rotations and finite cyclic grids enter the proof; they do not alone specify these geometric area fractions. The 2024 work *Renormalization of translated cone exchange transformations* treats return-map renormalization near the cone vertex in a different regime, not this rational trapezium census.

## Limitations

The period-area law is for the bounded invariant trapezium, not the unbounded invariant strip or the non-invariant transients. It is an area census of periodic points, not a finite count of periodic orbits: each positive-area class contains continuum-many orbits. The rational/irrational pointwise assertions adopt the canonical half-open interval-exchange convention, while all area assertions are invariant under null-boundary changes. The proof uses the special identity cone permutation and horizontal translations; rotating cone exchanges require different arguments. The area formula is a consequence of a previously published explicit IET representation plus a new return-clock and integration analysis; it is not a claim that the initial cone-exchange family or elementary rotation facts are new. Independent scientific and priority assessment has not been performed.

## References

1. N. Cockram, P. Ashwin, A. Rodrigues, *Construction of Invariant Curves for Some Piecewise Isometries*, arXiv:2312.17412v1 (first posted 2023-12-29), especially Section 3, Theorem 3.1 and equation (3.7). https://arxiv.org/abs/2312.17412 . Published as *Dynamical Systems* **40** (2025), 602–625, DOI:10.1080/14689367.2025.2514193.
2. N. Cockram, P. Ashwin, A. Rodrigues, *Renormalization of translated cone exchange transformations*, *Dynamical Systems* **39** (2024), 725–758, DOI:10.1080/14689367.2024.2378297.
3. M. Boshernitzan, *Subgroup of interval exchanges generated by torsion elements and rotations*, arXiv:1208.1023 (2012). Context for structural relations among three-interval exchanges and rotations; no period-area law is taken from this work.
