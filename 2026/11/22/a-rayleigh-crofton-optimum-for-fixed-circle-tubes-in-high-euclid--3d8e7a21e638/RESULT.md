# A Rayleigh Crofton optimum for fixed-circle tubes in high Euclidean dimension

## Finding
For each integer \(d\ge4\) and radius ratio \(r>1\), consider the closed unit-radius tube about a **fixed planar circle** in Euclidean \(d\)-space,
\[
T_{d,r}=\bigl\{(x,y,z)\in\mathbb R^2\times\mathbb R^{d-2}:\ (\sqrt{x^2+y^2}-r)^2+\|z\|^2\le1\bigr\}.
\]
Sample an unoriented affine hyperplane with the Euclidean-motion-invariant measure on hyperplanes, conditioned on meeting the interior of \(T_{d,r}\). Except on a measure-zero set of tangencies, its section is either contractible, disconnected into exactly two contractible components, or connected with the homotopy type of a circle. These three types have an explicit joint law.

Let \(U\) be uniformly distributed on \(S^{d-1}\), set \(S=(U_1^2+U_2^2)^{1/2}\), and write
\[
b=\frac{d-2}{2},\qquad S^2\sim\operatorname{Beta}(1,b),\qquad
\mu_d=\mathbb E S=\frac{\sqrt\pi}{2}\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}.
\]
For every \(d\ge4\) and \(r>1\), the probabilities of the three types, respectively, are
\[
\begin{aligned}
P_d(r)&=\frac{2\,\mathbb E\min(rS,1)}{1+r\mu_d}
=\frac{2\left[r\mu_d I_{r^{-2}}(3/2,b)+(1-r^{-2})^b\right]}{1+r\mu_d},\\
P_d^{(2)}(r)&=\frac{\mathbb E(rS-1)_+}{1+r\mu_d},\\
P_d^{(\circ)}(r)&=\frac{\mathbb E(1-rS)_+}{1+r\mu_d}.
\end{aligned}
\]
Here \(I_x(a,b)\) is the regularized incomplete beta function; \(P_d\) counts **contractible, connected** sections, not sections whose components are each simply connected.

For each finite \(d\ge4\), \(P_d(r)\) has exactly one maximizer \(r_d>1\). It is the unique solution of
\[
\boxed{I_{r_d^{-2}}(3/2,(d-2)/2)=(1-r_d^{-2})^{(d-2)/2}},
\qquad
\boxed{P_d(r_d)=2(1-r_d^{-2})^{(d-2)/2}}.
\]
In particular, in dimension four \(r_4\) is the plastic constant, the unique real root greater than one of \(r_4^3-r_4-1=0\); numerically, \(r_4=1.324717957245\ldots\) and \(P_4(r_4)=0.860319418004\ldots\).

There is a sharp and nontrivial high-dimensional optimum. Set \(a=\sqrt{\pi/2}\), and let \(t_*>0\) be the unique strictly positive solution of
\[
a\operatorname{erf}(t_*/\sqrt2)=(t_*+a)e^{-t_*^2/2}.
\]
Then
\[
\boxed{\lim_{d\to\infty}\frac{r_d}{\sqrt d}=\frac1{t_*}=0.734903908748\ldots},
\qquad
\boxed{\lim_{d\to\infty}P_d(r_d)=2e^{-t_*^2/2}=0.792442639800\ldots}.
\]
The limit is neither a vanishing nor a unit success probability. For comparison, replacing the fixed circular core by a growing-dimensional spherical core yields a different optimization scale and success limit; those are different families of solids even though their boundaries can have the same abstract topological type.

## Assumptions and scope
The minor tube radius is exactly one, and \(r>1\) ensures that the circular core is separated from its opposite side. All probabilities concern **solid**, not surface-only, sections. The hyperplane measure is the usual invariant measure \(d\sigma(U)\,dm\) (uniform normal and Lebesgue signed offset), normalized after conditioning on positive \((d-1)\)-dimensional section volume. It does not mean a uniform plane through the origin or a uniform orientation after conditioning. The finite-dimensional theorem is asserted for every integer \(d\ge4\); the dimension-three specialization is a previously published result and is used only for a consistency check. Null sets where a hyperplane is tangent or touches a transition level are ignored.

The probability \(P_d(r)\) is for contractible sections and not for arbitrary simply connected spaces: a disconnected union of contractible components is excluded. The large-dimension limit keeps the 2-dimensional circle core fixed, while the codimension of that core grows. In particular, it is not the higher-dimensional spherical-spine torus \(\{(x,z): (\|x\|-r)^2+z^2\le1\}\), whose core is \(S^{d-2}\).

## Proof
**1. Exact reduction to a three-dimensional slice.** Write a general normal as \(U=(u_x,u_y,v)\), with \(v\in\mathbb R^{d-2}\). The orthogonal rotations preserving the body turn it into \((S,0,\sqrt{1-S^2},0,\ldots,0)\). With hyperplane offset \(m\), this reduces the equation to \(Sx+\sqrt{1-S^2}\,z_1=m\). The remaining \(d-3\) coordinates \(z_\perp\) occur in neither equation nor the circle. The straight-line homotopy \((x,y,z_1,z_\perp)\mapsto(x,y,z_1,(1-t)z_\perp)\), \(0\le t\le1\), stays inside both the hyperplane and the solid: it weakly decreases \(\|z\|^2\) and fixes the \(z_\perp=0\) slice pointwise. Hence every section strongly deformation retracts onto the corresponding ordinary three-dimensional circular-torus plane section. The reduction proves the **homotopy classification**, not a claimed classification by higher-dimensional homeomorphism.

**2. Offset intervals and topology.** Because the solid is centrally symmetric, the unoriented normal can be represented with \(m\ge0\). Put \(c=rS\). The meridian-line picture in three dimensions consists of two unit disks centered at signed normal offsets \(\pm c\), inside a convex stadium shadow. An offset in \([0,c+1]\) hits the solid. The meridian line meeting exactly one disk produces a contractible section; meeting neither yields two contractible components; meeting both yields a circle-homotopy section. For generic offsets, the respective Lebesgue lengths are
\[
2\min(c,1),\qquad(c-1)_+,\qquad(1-c)_+.
\]
The lengths sum to \(c+1\). This is also obtained directly from the inequalities \(|m-c|<1\) and \(m+c<1\). Finch's three-dimensional slicing lemma supplies a fully explicit disk-gluing justification for the meridian classification. Strong deformation retraction transfers those types to every \(d\ge4\).

**3. Crofton averaging.** The projection of a uniform normal onto the fixed circle plane satisfies \(S^2\sim\operatorname{Beta}(1,b)\), \(b=(d-2)/2\). Invariant hyperplane measure weights each orientation by its **available offset length** \(c+1\). Dividing the orientation-integrated lengths from step 2 by \(\mathbb E(1+rS)=1+r\mu_d\) gives all three probability formulas. Their sum is one because \(2\min(c,1)+(c-1)_++(1-c)_+=1+c\). Elementary beta integration gives
\[
\mathbb E[S\mathbf 1_{\{S<1/r\}}]=\mu_d I_{r^{-2}}(3/2,b),\qquad
\Pr(S\ge1/r)=(1-r^{-2})^b,
\]
which yields the incomplete-beta expression for \(P_d(r)\).

**4. The unique optimizer at every fixed dimension.** Put \(N_d(r)=\mathbb E\min(rS,1)\), \(I(r)=I_{r^{-2}}(3/2,b)\), and \(B(r)=(1-r^{-2})^b\). Since \(S\) has a continuous density, differentiation under the expectation gives \(N_d'(r)=\mathbb E[S\mathbf1_{\{S<1/r\}}]=\mu_d I(r)\), while \(N_d(r)=r\mu_d I(r)+B(r)\). Thus
\[
P_d'(r)=\frac{2\mu_d}{(1+r\mu_d)^2}[I(r)-B(r)].
\]
For \(r>1\), \(I(r)\) is strictly decreasing from 1 to 0 and \(B(r)\) is strictly increasing from 0 to 1. Hence there is precisely one root, where the derivative switches from positive to negative. Substitution into \(P_d\) gives \(P_d(r_d)=2B(r_d)\). At \(d=4\), \(b=1\) and \(I(r)=r^{-3}\), giving the stated cubic. This also supplies existence without any numerical optimization assumptions.

**5. The Rayleigh boundary law and convergence of the optimizers.** Let \(Y_d=\sqrt d\,S\). A unit-sphere normal can be represented by a standard Gaussian vector divided by its Euclidean norm, hence \(Y_d\Rightarrow Y\), where \(Y\) has Rayleigh density \(y e^{-y^2/2}\) on \(y>0\). Moreover \(\mathbb E Y_d=\sqrt d\,\mu_d\to a\), and the family \(\{Y_d\}\) is uniformly integrable since its second moments equal 2. For any \(\kappa>0\),
\[
P_d(\kappa\sqrt d)\longrightarrow
p(\kappa)=\frac{2\,\mathbb E\min(\kappa Y,1)}{1+a\kappa}
=\frac{2a\kappa\operatorname{erf}(1/(\sqrt2\kappa))}{1+a\kappa}.
\]
The convergence is uniform for \(\kappa\) in compact subintervals of \((0,\infty)\): the truncated expectations are uniformly Lipschitz in \(\kappa\) with constants \(\mathbb E Y_d\), and the denominators converge uniformly.

Set \(M(\kappa)=\mathbb E\min(\kappa Y,1)\). For positive \(\kappa\), \(M''(\kappa)=-f_Y(1/\kappa)/\kappa^3<0\). Therefore \(G(\kappa)=M'(\kappa)(1+a\kappa)-aM(\kappa)\) decreases strictly from \(a>0\) to \(-a<0\), and \(p\) has a unique global maximizer. The identity \(M(\kappa)=\kappa a\operatorname{erf}(1/(\sqrt2\kappa))\) reduces its critical-point equation, after setting \(t=1/\kappa\), to \(a\operatorname{erf}(t/\sqrt2)=(t+a)e^{-t^2/2}\). At the maximizer the same cancellation as in step 4 gives \(p=2e^{-t^2/2}\).

Finally, the finite-dimensional maximizers cannot escape the Rayleigh scaling window. Indeed \(P_d(r)\le2r\mu_d/(1+r\mu_d)\) and \(P_d(r)\le2/(1+r\mu_d)\). Since \(\sqrt d\,\mu_d\to a\), any subsequence with \(r_d/\sqrt d\to0\) or \(r_d/\sqrt d\to\infty\) would make the maximal probability tend to zero, contradicting the positive limiting probability at the test choice \(r=\sqrt d\). Thus \(r_d/\sqrt d\) remains in a fixed compact subinterval of \((0,\infty)\). Compact-uniform convergence and uniqueness of the maximum of \(p\) imply \(r_d/\sqrt d\to1/t_*\); substituting into the probability limit completes the proof.

## Verification
The included `check.py` evaluates the finite-dimensional probabilities both from the beta formula and from direct orientation integrals, checks that all three topological probabilities sum to one, verifies the optimizer equation and strict neighboring inequalities at a range of dimensions, recovers the published dimension-three optimizer and the dimension-four plastic constant, and compares large finite dimensions with the Rayleigh constants. It completed 246 finite assertions using Python 3 and SciPy. Run `python check.py`. The computations test the formulas but do not constitute a proof in all dimensions; the analytic steps above do.

## Relationship to prior work
Finch's *Slicing a Doughnut at Random* (arXiv:2611.15546, initially posted 2026-11-11), in Sections 4–5, proves the dimension-three, planar-circle case with the same invariant measure and provides its meridian slicing lemma. That case is **not** claimed as new; the higher-dimensional normal projection law, exact incomplete-beta classification, dimension-four algebraic optimum and Rayleigh-optimized limit are the results here. General Crofton integral geometry is classical, and the invariant measure is not a new construction.

The separately studied higher-dimensional **spherical-core** torus has equation \((\|x\|-r)^2+z^2\le1\), with core \(S^{d-2}\). Its published optimal radius tends to 1 at order \(d^{-1}\) and its optimal ball-section probability tends to one. In the present family the core remains \(S^1\), the optimizer diverges like \(\sqrt d\), and the success probability tends to a constant strictly below one. Because the underlying solids and orientation laws are different, neither result contains the other's theorem. A three-dimensional convex-meridian Crofton classification similarly covers the common dimension-three case but not the growing-codimension fixed-circle family.

## Limitations
The result is specific to a unit-radius Euclidean tube around one **planar circle**, with uniform invariant affine-hyperplane sampling conditioned on intersection. It does not treat arbitrary embedded loops, noncircular meridians, Haar central hyperplanes, random subspaces of other codimension, or the spherical-core torus. Generic section topologies are asserted up to **homotopy**, not as new higher-dimensional homeomorphism identifications. The asymptotic statement gives leading constants without a uniform convergence rate. The checks of scientific priority are based on accessible sources and are not a proof that no historical equivalent exists; no independent mathematical audit has been performed.

## References
1. Steven Finch, *Slicing a Doughnut at Random*, arXiv:2611.15546v1 (first public date 2026-11-11), https://arxiv.org/html/2611.15546v1 ; https://arxiv.org/abs/2611.15546 .
2. Daniel Hug and Rolf Schneider, *Integral geometry of pairs of hyperplanes or lines*, 2020, https://link.springer.com/article/10.1007/s00013-020-01465-0 .
3. *Gaussian-optimal Crofton ball sections of higher-dimensional spherical tori*, published research record 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-gaussian-optimal-crofton-ball-sections-of-higher-dimensional-sph--55079a76e4e3 .
4. *A three-topology Crofton law and inverse support tomography for convex-meridian toroids*, published research record 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-three-topology-crofton-law-and-inverse-support-tomography-for--8cf34e87984a .
