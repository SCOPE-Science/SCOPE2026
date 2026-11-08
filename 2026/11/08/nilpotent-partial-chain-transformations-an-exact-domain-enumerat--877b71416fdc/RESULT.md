# Nilpotent partial-chain transformations: an exact domain enumerator and Gaussian law

## Finding
For an integer \(n\ge0\), let \(\mathcal P_n\) be the finite monoid of partial weakly increasing maps on the ordered set \([n]=\{1,\ldots,n\}\), including the empty map. Write \(N_{n,d}\) for the number of nilpotent elements of \(\mathcal P_n\) with domain of cardinality \(d\). Introduce the formal variables \(z,u\) and
\[
\Delta(z,u)=1-2(1+2u)z+z^2,\qquad
R(z,u)=\frac{1+z-\sqrt{\Delta(z,u)}}{2(1+u)z}.
\]
Here \(\sqrt\Delta\) has constant term one; the apparent division by \(z\) is removable, and \(R(0,u)=1\). Then the exact domain-size generating function is
\[
\boxed{\sum_{n,d\ge0}N_{n,d}z^nu^d=\frac{1}{R(z,u)\big(\sqrt{\Delta(z,u)}+uzR(z,u)\big)}.}
\]
If \(D_n\) is the domain size of a uniformly random nilpotent element, then
\[
\boxed{\frac{D_n-n/\sqrt2}{\sqrt{n/(4\sqrt2)}}\ \xrightarrow[]{\ d\ }\ \mathcal N(0,1).}
\]
The finite-size mean and variance consequently have leading terms \(n/\sqrt2+O(1)\) and \(n/(4\sqrt2)+O(1)\). The unweighted counts are known; the finding is the domain refinement and its normal law.

## Assumptions and scope
A partial map \(f:D\longrightarrow[n]\) is order-preserving when \(i<j\) in \(D\) implies \(f(i)\le f(j)\). Composition is partial-map composition. Nilpotent means some positive iterate is the empty map. The set \([0]\) is empty and has one empty map, so \(N_{0,0}=1\). All assertions concern this full partial transformation monoid, not solely order-decreasing, injective, or everywhere-defined transformations. The domain size is a natural semigroup parameter, appearing in the projection characteristic of the motivating work.

## Proof
**1. Nilpotence and fixed points.** Every finite partial functional digraph consists of directed paths feeding into directed cycles (or terminating at undefined values). An order-preserving map cannot have a cycle with two or more vertices: on the ordered cycle vertices its restriction is an order-preserving bijection, hence the identity. Consequently all its nontrivial persistent orbits are fixed points. Hence \(f\) is nilpotent if and only if \(f(i)\ne i\) for every \(i\in\operatorname{dom}(f)\).

**2. Unconstrained interval maps.** For integers \(m,k\ge0\), let
\[
P_{m,k}(u)=\sum_{d=0}^m\binom md\binom{k+d-1}{d}u^d.
\]
This counts partial increasing maps from a prescribed ordered \(m\)-set to a prescribed ordered \(k\)-set, marked by domain cardinality; the convention is \(P_{m,0}(u)=1\). Indeed there are \(\binom md\) domains and \(\binom{k+d-1}{d}\) weakly increasing target sequences. Set
\[
A(z,u)=\sum_{m\ge0}P_{m,m}(u)z^m,\quad
B(z,u)=\sum_{m\ge0}P_{m,m+1}(u)z^m,\quad
C(z,u)=\sum_{m\ge0}P_{m,m+2}(u)z^m.
\]
For any prescribed ordered set of \(r\ge1\) fixed points, gaps to the left and right of the extreme fixed points have \(m+1\) available target values, and internal gaps have \(m+2\). Monotonicity makes these gap maps independent: a point to the left of a fixed point can map at most to that fixed point, and a point between two consecutive fixed points maps between them. A fixed point contributes \(zu\). Thus the generating function for maps whose fixed points contain some marked \(r\)-element set is
\[
(zu)^r B(z,u)^2 C(z,u)^{r-1}.
\]
Inclusion-exclusion over all fixed points gives
\[
N(z,u)=A(z,u)+\sum_{r\ge1}(-1)^r(zu)^rB(z,u)^2C(z,u)^{r-1}
=A(z,u)-\frac{zuB(z,u)^2}{1+zuC(z,u)}.
\]
The coefficient extraction is legitimate in the ring of formal power series: the denominator has constant term one.

**3. Exact diagonal identity.** Let \(T(x)=(1-x)/(1-(1+u)x)\). Elementary coefficient extraction gives, also for \(k=0\),
\[
P_{m,k}(u)=[x^m]\frac{T(x)^k}{1-x}.
\]
Let \(R=T(zR)\) be the unique formal solution with \(R(0,u)=1\). Its quadratic equation is
\[
(1+u)zR^2-(1+z)R+1=0,
\]
so the stated radical expression follows. By the standard formal Lagrange diagonal identity (obtainable by the residue substitution \(x=zT(x)\)), for each \(h\ge0\),
\[
\sum_{m\ge0}[x^m]\frac{T(x)^{m+h}}{1-x}z^m
=\frac{R^h}{(1-zR)(1-zT'(zR))}
=\frac{R^{h-1}}{\sqrt\Delta}.
\]
The last equality follows by substituting \(R=T(zR)\) and \(T'(x)=u/(1-(1+u)x)^2\), or by differentiation of the quadratic equation. Taking \(h=0,1,2\) gives
\[
A=\frac1{R\sqrt\Delta},\qquad B=\frac1{\sqrt\Delta},\qquad C=\frac R{\sqrt\Delta}.
\]
Substituting these three expressions into the inclusion-exclusion formula and cancelling yields exactly
\[
N(z,u)=\frac1{R(\sqrt\Delta+uzR)}.
\]
Every equality is a formal-power-series identity in \(\mathbb Q[u][[z]]\) (with rational expressions interpreted by their unique expansions).

**4. Uniform singularity and Gaussian law.** For positive \(u\) near one, the dominant branch point is
\[
\rho(u)=(\sqrt{1+u}-\sqrt u)^2,
\quad\Delta(z,u)=(1-z/\rho(u))(1-\rho(u)z).
\]
The branch of \(R\) chosen above is analytic in the slit disk, and the denominator \(R(\sqrt\Delta+uzR)\) has no zeros on its continuation near the closed dominant disk except for the displayed square-root branch behavior: for real \(0\le z\le\rho(u)\) both factors are positive, while direct substitution of a putative denominator zero gives an algebraic candidate lying on the other square-root branch. Compactness and continuity extend this exclusion uniformly to complex \(u\) in a neighborhood of one. Expanding at \(z=\rho(u)\) gives
\[
N(z,u)=\frac{1+u}{u}
-\frac{\sqrt{1+u}\sqrt{1-\rho(u)^2}}{u^2\sqrt{\rho(u)}}
\sqrt{1-z/\rho(u)}+O(1-z/\rho(u)).
\]
Standard square-root coefficient extraction, uniformly for \(u\) near one, therefore gives
\[
[z^n]N(z,u)=c(u)n^{-3/2}\rho(u)^{-n}(1+O(n^{-1})),\quad
c(u)=\frac{\sqrt{1+u}\sqrt{1-\rho(u)^2}}{2\sqrt\pi\,u^2\sqrt{\rho(u)}}.
\]
Thus the moment-generating function of the random domain size satisfies, uniformly for small complex \(t\),
\[
\mathbb E[e^{tD_n}]
=\frac{c(e^t)}{c(1)}\left(\frac{\rho(1)}{\rho(e^t)}\right)^n(1+O(n^{-1})).
\]
For \(h(t)=-\log(\rho(e^t)/\rho(1))\), direct differentiation yields
\[
h'(0)=1/\sqrt2,\qquad h''(0)=1/(4\sqrt2)>0.
\]
Put \(t=s/\sqrt{nh''(0)}\), subtract the linear centering, and expand \(h(t)\) through second order. The centered-normalized moment generating functions converge locally to \(e^{s^2/2}\), proving the stated central limit theorem. The same asymptotics give the claimed mean and variance expansions.

## Verification
A standalone standard-library Python program `verify.py` enumerates all partial order-preserving maps through \(n=8\), tests fixed-point-freeness directly, records domain sizes, and independently computes the predicted coefficients using the interval-polynomial inclusion-exclusion recurrence. Every coefficient matches. The resulting domain-polynomial coefficient vectors, in increasing \(d\), are:
\[
\begin{array}{c|l}
n& (N_{n,0},N_{n,1},\ldots,N_{n,n})\\\hline
1&(1,0)\\
2&(1,2,0)\\
3&(1,6,5,0)\\
4&(1,12,26,14,0)\\
5&(1,20,80,104,42,0)\\
6&(1,30,190,434,405,132,0)\\
7&(1,42,385,1344,2134,1562,429,0)\\
8&(1,56,700,3444,8154,9932,6006,1430,0)
\end{array}
\]
The univariate totals are \(1,1,3,12,53,247,1192,5897,29723\) for \(n=0,\ldots,8\). This finite replay checks the formula only at the indicated finite degrees; the general identity and limit rely on the preceding argument.

## Relationship to prior work
Imam–Usman–Idris–Ibrahim, first available online January 20, 2024, examine quasi-idempotent generation in the very same semigroup and use domain size explicitly as a structural parameter. Their analysis does not determine nilpotent elements by domain size. Garba studies the nilpotent-generated subsemigroup and its depth and rank. Laradji determines counts by the number of fixed points, including the unweighted nilpotent sequence when that number is zero, but a fixed-point-only distribution cannot recover domain size. The integer sequence A110122 records the unweighted nilpotent counts and their asymptotic; those are acknowledged and excluded from the claimed novelty. Laradji–Umar's lattice-path formulas concern the order-decreasing partial subsemigroup, not the entire order-preserving partial monoid. The new contribution is the joint nilpotence/domain enumeration and conditional Gaussian law, not the underlying unweighted totals or classical square-root transfer methods.

## Limitations
The result assumes a linearly ordered finite domain/range and the entire partial order-preserving monoid. It does not enumerate nilpotents jointly by image size, index of nilpotence, or arbitrary finite poset. Direct computations through \(n=8\) are finite checks, not a substitute for the proof. The complete full texts of the most relevant Laradji 2021 and Garba 1994 antecedents could not be fully inspected; undiscovered equivalent weighted formulas remain a publication-priority risk. The scientific claims have not undergone an independent audit.

## References
1. A. T. Imam, L. Usman, A. Idris and S. Ibrahim, *Product of Quasi-Idempotents in Finite Semigroup of Partial Order-Preserving Transformations*, International Journal of Mathematical Sciences and Optimization 10(1) (2024), 53–59. https://doi.org/10.5281/zenodo.10580237 (available online 2024-01-20).
2. A. Laradji, *Fixed points of order-preserving transformations*, Journal of Algebra and Its Applications 21(4) (2022), article 2250082. https://doi.org/10.1142/S0219498822500827 (first online 2021-02-05).
3. G. U. Garba, *Nilpotents in semigroups of partial order-preserving transformations*, Proceedings of the Edinburgh Mathematical Society 37(3) (1994), 361–377. https://doi.org/10.1017/S001309150001885X.
4. A. Laradji and A. Umar, *Lattice paths and order-preserving partial transformations*, arXiv:1304.7574 (2013). https://arxiv.org/abs/1304.7574.
5. OEIS A110122, fixed-point-free order-preserving partial maps, https://oeis.org/A110122. Its unweighted counts are prior art.
