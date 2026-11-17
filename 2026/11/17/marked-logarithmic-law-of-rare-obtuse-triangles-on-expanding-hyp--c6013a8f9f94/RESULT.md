# Marked logarithmic law of rare obtuse triangles on expanding hyperbolic circles

## Finding

On a curvature-\(-1\) hyperbolic plane, independently sample three arclength-uniform vertices on a geodesic circle of radius \(R>0\). Condition on their geodesic triangle having an obtuse angle. It has almost surely exactly one, at a vertex \(V\). In counterclockwise order let \(a,b>0\) be the two consecutive polar-angle gaps on either side of \(V\) (so the remaining gap is \(c=2\pi-a-b\)). Set
\[
 q=\operatorname{sech}^2 R,\quad \ell=\log(1/q),\quad x=\tan(a/2),\quad y=\tan(b/2),\quad U_R=\frac{\log(1/x)}{\ell},\quad W_R=\frac{xy}{q}.
\]
On the obtuse event, \(a+b<\pi\), \(x,y>0\), and \(0<W_R<1\). The **complete finite-radius marked conditional law** is
\[
 \boxed{f_R(u,w)=\frac{q\ell}{J(q)}\frac{\mathbf1_{\{0<w<1\}}}{(1+q^{2u})(1+w^2q^{2(1-u)})}},\quad u\in\mathbb R,\quad
 J(q)=\int_0^q\frac{-\log t}{1-t^2}\,dt.
\]
As \(R\to\infty\), \(f_R\to\mathbf1_{(0,1)^2}\) in \(L^1(du\,dw)\), hence **the logarithmic gap-split \(U_R\) and the product mark \(W_R\) converge jointly in total variation to two independent uniform \((0,1)\) variables**. The original label of \(V\) is uniform on \(\{1,2,3\}\) and independent of both marks for every finite \(R\).

Let \(d_a,d_b\) be the intrinsic geodesic lengths corresponding to the two angular gaps incident to \(V\). Jointly, conditionally on obtuseness,
\[
 \left(\frac{d_a}{2R},\frac{d_b}{2R}\right)\Rightarrow\left((1-2U)_+,(2U-1)_+\right),\qquad U\sim\operatorname{Unif}(0,1).
\]
Consequently the larger of these two lengths, divided by \(2R\), converges to \(\operatorname{Unif}(0,1)\); the smaller, divided by \(2R\), tends to zero in probability. These limiting length statements are weak convergence, **not** total-variation convergence. The already established scalar acuteness probability and its logarithmic asymptotic are used for normalization and are **not** part of the novelty claim.

## Assumptions and scope

The hyperbolic curvature is \(-1\), \(R\) is intrinsic radial distance, and vertices are independent uniform samples with respect to the geodesic circle's hyperbolic arclength, equivalently independent uniform polar angles. Straight hyperbolic geodesic segments, rather than Euclidean drawn chords, define the triangle's angles and side lengths. Ties, right angles and degenerate triples have probability zero. The counterclockwise order is fixed by an orientation of the ambient plane. The conditional marks are defined only on the positive-probability event that the triangle is obtuse; \(U_R\) is allowed to lie outside \((0,1)\) for finite \(R\). Here \(z_+=\max(z,0)\).

## Proof

**1. Exact obtuseness domain.** Sorting three independent angular samples gives successive gaps \(a,b,c>0\), \(a+b+c=2\pi\), with Dirichlet \((1,1,1)\) density \(1/(2\pi^2)\) with respect to \(da\,db\). For two vertices on the circle with angular gap \(t\), the hyperbolic chord length \(d_t\) satisfies
\[
 \cosh d_t=1+2\sinh^2R\sin^2(t/2),\qquad \sinh(d_t/2)=\sinh R\sin(t/2).
\]
The hyperbolic cosine law says that the angle between the sides corresponding to \(a,b\), opposite \(c\), is obtuse precisely when \(\cosh d_c>\cosh d_a\cosh d_b\). Substitution and cancellation of positive factors give
\[
 \sinh^2R\sin(a/2)\sin(b/2)<\cos((a+b)/2),
\]
Because the left side is positive, obtuseness first forces \(\cos((a+b)/2)>0\), hence \(a+b<\pi\) and in particular \(0<a,b<\pi\). Only on this domain do we divide by the strictly positive factors \(\cos(a/2)\cos(b/2)\), obtaining the equivalent criterion
\[
 (1+\sinh^2R)\tan(a/2)\tan(b/2)<1,
 \quad\text{i.e.}\quad xy<q=\operatorname{sech}^2R.
\]
Conversely, for positive \(x,y\), the inequality \(xy<q<1\) forces \(\arctan x+\arctan y<\pi/2\), so the corresponding \(a,b\) do satisfy \(a+b<\pi\), and the original obtuseness criterion follows. Thus the opposite angular gap \(c>\pi\). Only one of three gaps can exceed \(\pi\), so the obtuse vertex is unique. Exchangeability makes its original label uniform and independent of the oriented gap pair.

**2. Exact joint density.** For the choice of the long gap \(c>\pi\), the change \(x=\tan(a/2)\), \(y=\tan(b/2)\) gives the unnormalized positive measure
\[
 \frac{4\,\mathbf1_{\{xy<q\}}}{(1+x^2)(1+y^2)}\,dx\,dy.
\]
(The common constant \(1/(2\pi^2)\) and the three equally likely choices of long gap cancel after conditioning.) Its total mass equals
\[
 4\int_0^\infty\frac{\arctan(q/x)}{1+x^2}\,dx=4J(q).
\]
To check the last equality without invoking a tabulated integral, differentiate the integral divided by four with respect to \(q\):
\[
 \int_0^\infty\frac{x\,dx}{(x^2+q^2)(1+x^2)}=\frac{-\log q}{1-q^2},
\]
and use the zero limit as \(q\downarrow0\). Now put \(x=q^u\), \(y=qw/x=q^{1-u}w\). The absolute Jacobian is \(q\ell\) for \((u,w)\in\mathbb R\times(0,1)\). Dividing by \(4J(q)\) gives the stated exact density \(f_R\).

**3. Total-variation limit.** Expanding \((1-t^2)^{-1}\) or estimating the integral at zero yields
\[
 J(q)=q(\ell+1)+O(q^3(\ell+1)),\qquad \frac{q\ell}{J(q)}\longrightarrow1.
\]
For every \(w\in(0,1)\) and almost every real \(u\), the exact density converges to \(\mathbf1_{\{0<u<1\}}\): within \((0,1)\), both denominator terms tend to one, while outside, at least one denominator diverges. Every \(f_R\) integrates to one, as does its pointwise limiting density. Scheffé's lemma therefore gives \(\int|f_R-\mathbf1_{(0,1)^2}|\,du\,dw\to0\), which is the asserted total-variation limit. Permutation symmetry gives the independent uniform original obtuse-vertex label exactly.

**4. Macroscopic geodesic sides.** From the chord formula and the exact marks,
\[
 \sinh(d_a/2)=\sqrt{\frac{1-q}{q}}\frac{q^{U_R}}{\sqrt{1+q^{2U_R}}},\quad
 \sinh(d_b/2)=\sqrt{\frac{1-q}{q}}\frac{q^{1-U_R}W_R}{\sqrt{1+q^{2(1-U_R)}W_R^2}}.
\]
For fixed \((u,w)\in(0,1)^2\), \(\log(1/q)/(2R)\to1\), and the elementary asymptotics of \(\operatorname{arsinh}\) imply
\[
 \frac{d_a}{2R}\to(1-2u)_+,\qquad \frac{d_b}{2R}\to(2u-1)_+.
\]
The total-variation limit of the marks, combined with continuity except on null boundaries and these deterministic asymptotics (or a Skorokhod coupling), proves joint weak convergence. Finally \(\max\{(1-2U)_+,(2U-1)_+\}=|1-2U|\), uniform on \((0,1)\), while the minimum is zero. The latter limit law is a geometric shape description, not a new claim about the known marginal event frequency.

## Verification

The supplied standard-library checker `verify_marked.py` independently tests the obtuse-region criterion by direct circular-gap sampling at radii \(1.5\) and \(3.5\), checks numerical normalization of the exact two-dimensional marked density at two small values of \(q\), and tests the hyperbolic chord-length scaling at several logarithmic mark values. It returns `MARKED_HYPERBOLIC_CHECKS_OK`. An additional numerical calculation using quadrature and hyperbolic cosine-law comparisons gave consistent results. The infinite-dimensional \(L^1\) assertion and limiting side laws follow from the proof, not from these finite computations.

## Relationship to prior work

Horváth's 2014 work gives hyperbolic triangle and circle formulas including the cosine law but does not study probabilistic conditioning of random circle-inscribed triangles [1]. Lv and Guo's 2016 acute-triangle probabilities are based on uniformly distributed *angle coordinates over triangle shape space*, a different sampling measure [2]. A previously published exact dilogarithmic formula for the scalar acuteness probability of **this same fixed-circle sampling model** is particularly close [3]. Its statement and proof establish the total probability and angular gap criterion, but do not identify the conditional two-mark density, a total-variation conditional limit, or the surviving geodesic-scale shape law. Those marked claims, not the scalar probability or the cosine law, are the contribution here. No independent historical-priority certification is asserted.

## Limitations

The sampling is from one fixed-radius geodesic circle in curvature \(-1\), not the enclosed disk, and not from a general surface. The limit requires \(R\to\infty\); no explicit finite-radius total-variation error bound is proved. The conditional marked limit and side-length limit have different convergence modes. The orientation convention fixes the ordered pair of adjacent gaps; reversing it exchanges the gaps and sends the limiting split mark to its reflection. The result has not been independently validated, and priority comparisons cannot exclude unindexed publications.

## References

[1] Á. G. Horváth, *Hyperbolic plane geometry revisited*, arXiv:1405.1068v1, publicly submitted May 5, 2014; especially §§1.1, 4.2. https://arxiv.org/abs/1405.1068

[2] Z. Lv and Y. Guo, *Probability of an Acute Triangle in the Two-dimensional Spaces of Constant Curvature*, first verified archive upload August 13, 2016, §§1, 3.3. https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20160813215159148123192

[3] *Exact dilogarithmic acuteness law for random triangles on hyperbolic circles*, publicly available record, November 2, 2026, particularly its Finding, Proof and Limitations. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-dilogarithmic-acuteness-law-for-random-triangles-on-hyperb--e75fde9a2b70
