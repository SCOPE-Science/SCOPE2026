# A positive-area period-four core at a doubly neutral border of a four-partition map

## Finding

For the planar continuous piecewise-affine map
\[
T_{a,c}(x,y)=(|x|+ay-1,\ x+c|y|-1),
\]
the joint flip and unit-modulus boundary \(a=0,c=1\) has an **exact, globally absorbing periodic set of planar area \(1/2\)**. Every point of the plane enters this compact set after finitely many iterates, and \(T_{0,1}^{4}\) is the identity on it. Almost every point of the set has least period four; its exceptional periods are exactly one and two. In particular, uncountably many period-four orbits occupy positive area, rather than forming isolated attracting/saddle branches.

More precisely, for \(-1\le u\le0\), set
\[
J(u)=\begin{cases}
[0,-1-2u],&-1\le u<-1/2,\\
[-3/2,0],&u=-1/2,\\
[-2-u,u-1],&-1/2<u\le0,
\end{cases}
\qquad
\mathcal P=\{(u,y):-1\le u\le0,\ y\in J(u)\}.
\]
Then the **entire set of periodic points** of \(T_{0,1}\) is \(\mathcal P\), and
\[
T_{0,1}(\mathcal P)=\mathcal P,\qquad
T_{0,1}^{4}|_{\mathcal P}=\mathrm{id},\qquad
\operatorname{area}(\mathcal P)=\tfrac12.
\]
Every orbit is eventually periodic with least eventual period dividing four. The sole fixed point is \((-1/2,-3/4)\); on the vertical fiber \(u=-1/2\), all other points of \(J(u)\) have least period two. Away from this fiber, the least period is two at exactly one point of each \(J(u)\), and four at every other point.

The result also has a sharp selection contrast with the subcritical family \(a=0,\ 0<c<1\): for each eventual two-cycle \(u\leftrightarrow-1-u\) of the first coordinate, the second coordinate converges to a unique two-cycle with geometric two-step contraction ratio at most \(c^2\). As \(c\uparrow1\), its even-phase coordinate converges pointwise to
\[
Y_*(u)=\begin{cases}
-u-1/2,&-1\le u<-1/2,\\
-3/4,&u=-1/2,\\
-3/2,&-1/2<u\le0.
\end{cases}
\]
The limiting attracting-cycle graph has two different one-sided limits at \(u=-1/2\), whereas the critical periodic set contains the entire connecting segment there. Thus the parameter limit selects the central two-cycle of each noncentral critical fiber but does not converge uniformly in the phase parameter.

## Assumptions and scope

The phase space is the full real plane. Parameters are fixed, with \(a=0\) and \(0<c\le1\); no restrictions are imposed on real initial coordinates. At \(c=1\) all periodic-core claims are exact, including border points. The \(c<1\) statements are fiberwise because the first coordinate is neutral and retains its initial eventual two-cycle parameter. Periods are forward discrete-time least periods.

## Proof

**1. The base enters an involution.** For \(a=0\), the first-coordinate map is \(f(x)=|x|-1\). Every \(x\in\mathbb R\) reaches \([-1,0]\) in finitely many iterates: values below \(-1\) first become positive, and positive values decrease by one until reaching \([0,1]\), whose image lies in \([-1,0]\). On that interval \(f(u)=-u-1\), so \(f^2(u)=u\). For any chosen even phase \(u\in[-1,0]\), write \(v=-u-1\), \(b_0=1-u\) and \(b_1=1-v=2+u\). Both forcings lie in \([1,2]\), and \(b_0+b_1=3\).

**2. Uniform finite entrance into a fiber trap at the neutral boundary.** When \(c=1\), the scalar second-coordinate update alternates between \(h_{b_0}(y)=|y|-b_0\) and \(h_{b_1}(y)=|y|-b_1\). Put \(B=\max(b_0,b_1)\). Whenever \(|y|>B\), the next magnitude is \(|y|-b_i<|y|\), decreased by at least \(\min(b_0,b_1)>0\); the interval \([-B,B]\) is forward invariant because \(\big||y|-b_i\big|\le B\) for \(|y|\le B\). Hence every scalar trajectory reaches \([-B,B]\) after finitely many steps. Its two-step return map on this interval is
\[
G(y)=h_{b_1}(h_{b_0}(y))=\big||y|-b_0\big|-b_1.
\]
If \(u<-1/2\), then \(t=b_0-b_1=-1-2u>0\), \(B=b_0\) and \(G(y)=t-|y|\) throughout \([-B,B]\). It first maps this interval into \([-b_1,t]\), then increases a negative argument by exactly \(t\) at each two-step return until it reaches \([0,t]=J(u)\). On \(J(u)\) it is the reflection \(G(y)=t-y\).

If \(u>-1/2\), let \(d=b_1-b_0>0\), \(B=b_1\). The first return maps \([-B,B]\) into \([-b_1,-d]\). On \([-b_1,-b_0]=J(u)\) it is the reflection \(G(y)=-3-y\). Any point in the remaining interval \((-b_0,-d]\), if nonempty, moves downward by the fixed amount \(d\) at each two-step return, until it enters \(J(u)\). Thus every trajectory again reaches \(J(u)\) after finitely many returns.

If \(u=-1/2\), both forcings are \(3/2\); on \([-3/2,3/2]\), \(G(y)=-|y|\), so one return enters \(J(u)=[-3/2,0]\), where \(G(y)=y\).

**3. Exact periodic set and area.** The preceding proof applies after the finite entrance of the base coordinate into \([-1,0]\); it proves finite entrance into \(\mathcal P\) for every initial condition. A direct one-step substitution maps \(J(u)\) bijectively onto \(J(-u-1)\). On each noncentral fiber, \(G\) is a reflection and so \(G^2=\mathrm{id}\); on the central fiber, \(G=\mathrm{id}\). Hence \(T(\mathcal P)=\mathcal P\) and \(T^4=\mathrm{id}\) there. No periodic point can lie outside \(\mathcal P\): such a periodic orbit would enter the forward-invariant set \(\mathcal P\) after finitely many iterates and, by periodicity, its initial point would also belong to \(\mathcal P\). The lengths of the vertical sections for \(u\ne-1/2\) equal \(|1+2u|\); the exceptional vertical segment has planar area zero. Therefore
\[
\operatorname{area}(\mathcal P)=\int_{-1}^{0}|1+2u|\,du=\tfrac12.
\]
The reflection has a single fixed point on each noncentral fiber, yielding a unique least-period-two orbit there. On the central fiber, \(T^2=\mathrm{id}\), and \(T(y)=-y-3/2\) fixes only \(y=-3/4\). The remaining two-dimensional set has least period four, with the same area \(1/2\).

**4. Subcritical two-cycle attraction and singular selection.** For \(0<c<1\), the two-step scalar return is
\[
G_c(y)=c\big|c|y|-b_0\big|-b_1.
\]
It is globally Lipschitz with constant at most \(c^2<1\), so Banach's contraction theorem gives a unique fixed point \(Y_c(u)\) and the bound \(|G_c^m(y)-Y_c(u)|\le c^{2m}|y-Y_c(u)|\) for every initial fiber state. The corresponding odd-phase value gives the unique attracting two-cycle over the fixed base pair \(u,v\).

The fixed points \(Y_c(u)\) are uniformly bounded in \(c\le1\): any period-two scalar orbit has both magnitudes at most \(B\), because if its maximal magnitude \(M>B\), each update has magnitude at most \(\max(B,cM-\min(b_0,b_1))<M\), contradicting periodicity. Every accumulation point of \(Y_c(u)\) as \(c\uparrow1\) is therefore a fixed point of \(G\). For \(u<-1/2\), the only such point is \(t/2\); for \(u>-1/2\), it is \(-3/2\). At \(u=-1/2\), both phases are equal and the unique scalar fixed point is \(-3/[2(1+c)]\), which tends to \(-3/4\). These formulas prove the asserted pointwise limit and its failure of uniformity, since each function \(u\mapsto Y_c(u)\) is continuous by the uniform contraction on a fixed compact base interval, whereas \(Y_*\) has unequal one-sided limits.

## Verification

Run `python3 check.py` with Python 3. The bundled standalone checker uses exact rational arithmetic to verify 2,989 sampled finite-entrance trajectories, 1,369 sampled periodic-core points, the exact fourth-iterate identity and forward invariance at those samples, and 500 instances of the subcritical contraction inequality. It also checks the exact area arithmetic. These are reproducible finite tests, **not** substitutes for the proofs of finite entrance for every real initial condition or of the full periodic-point classification.

## Relationship to prior work

Tikjha's 2026 analysis introduces the exact four-partition family and identifies its flip boundary \(a=0\), isolated stable and saddle period-two/four branches and the separate dimension-reducing line \(c=a\). Its propositions and concluding classification do not state the present positive-area, globally absorbing periodic core at the double-neutral parameter point \((a,c)=(0,1)\), nor the singular selection from \(c<1\). The distinction is logical as well as terminological: the preceding results on isolated branches and linear stability do not imply a finite-time global period-four identity.

Cima, Gasull, Mañosa and Mañosas (2024) prove eventual periodicity for a **different** piecewise-linear family \(F_{p,q}(x,y)=(|x|-y+p,x-|y|+q)\). Their result does not cover the map here by parameter specialization: the first coordinate of the present \(a=0\) family is autonomous, whereas that of their family retains a \(-y\) term. Their result motivates careful distinction between isolated periodic points and positive-area periodic cores, but does not imply this exact classification. General piecewise-affine periodic-map results are a remaining historical-priority risk.

## Limitations

The positive-area finite-time classification is proved only for \(a=0,c=1\); the fiberwise contraction and selection statements cover \(a=0,0<c<1\). No assertion is made for \(c>1\), for any nonzero \(a\), or for generic perturbations of the nonsmooth boundary. Although every orbit is eventually periodic at the critical parameter, the entrance time depends on the initial state and may be arbitrarily large. This is an analytical result with self-review; no independent audit or historical-priority certification has been performed.

## References

1. W. Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519v1, first submitted 2026-07-15, https://arxiv.org/abs/2607.13519.
2. A. Cima, A. Gasull, V. Mañosa, F. Mañosas, *Invariant graphs and dynamics of a family of continuous piecewise linear planar maps*, arXiv:2410.01052v1, first submitted 2024-10-01, https://arxiv.org/abs/2410.01052.
3. G. Cairns, Y. Nikolayevsky, G. Rossiter, *Piecewise linear periodic maps of the plane with integer coefficients*, arXiv:1407.3364, https://arxiv.org/abs/1407.3364 (general historical comparison, different class).
