# Uniform logarithmic shape splitting for small incircles of random cyclic triangles

## Finding

Let three points be sampled independently and uniformly by arclength on the unit circle. Order their circular gaps cyclically as \(G_1,G_2,G_3\) and put \(X_j=G_j/4\), so \(\sum_jX_j=\pi/2\). Let \(R\) be the inradius. Define \(I=\operatorname{argmax}_{1\le j\le3}X_j\) (unique almost surely) and, on \(E_t=\{R<t\}\), set
\[
U_t=\frac{\log X_{I+1}}{\log t},\qquad W_t=\frac Rt,
\]
where indices are cyclic. Then, in the product of counting and Lebesgue measures,
\[
\boxed{\mathcal L(I,U_t,W_t\mid E_t)\ \xrightarrow[t\downarrow0]{\mathrm{TV}}\ \mathrm{Unif}\{1,2,3\}\otimes\mathrm{Unif}(0,1)\otimes\mathrm{Unif}(0,1).}
\]
The known scalar normalization is \(\Pr(E_t)\sim(6/\pi^2)t\log(1/t)\), which is cited, not claimed as new. The contribution is the conditional joint marked law and its total-variation strength.

## Assumptions and scope

Three independent arclength-uniform points on one *unit* Euclidean circle define a nondegenerate inscribed triangle almost surely. Here \(0<t<1/2\). Circular gaps use cyclic order and \(X_j\) are half of the triangle's interior angles (in possibly permuted order). The index \(I+1\) means the next circular gap after the maximal gap. The numerical value of \(U_t\) need not belong to \((0,1)\) at finite \(t\); convergence is a statement about complete probability measures on \(\{1,2,3\}\times\mathbb R\times[0,1]\). Total variation is \(\sup_B|\mu_t(B)-\mu(B)|\).

## Proof

**Exact density and the incircle formula.** The spacing law for three independent uniform circle points is Dirichlet \((1,1,1)\). Hence in the triangle \(\mathcal T=\{x,y>0:x+y<\pi/2\}\) the joint density of \((X_1,X_2)\) is \(8/\pi^2\). The exact geometric identity is \(R=4\sin X_1\sin X_2\sin X_3\), with \(X_3=\pi/2-X_1-X_2\). By permutation symmetry, \(I\) is exactly uniform on three indices even after conditioning on \(E_t\).

**Corners dominate.** Fix \(\delta\in(0,\pi/12)\). In the corner with maximal angle \(z=\pi/2-x-y\), with \(0<x,y<\delta\), write
\[
R=4xy\,q(x,y),\qquad q(x,y)=\frac{\sin x}{x}\frac{\sin y}{y}\cos(x+y),
\]
so \(q(x,y)=1+O(\delta^2)\), uniformly as \(\delta\downarrow0\). On the complement of the three such disjoint corner squares, at most one of the angles can approach zero. There the other two sine factors have positive lower bounds depending on \(\delta\); the exceptional set is a finite union of strips of area \(O_\delta(t)\). In each corner the elementary product-sublevel formula
\[
\operatorname{area}\{0<x,y<\delta:xy<c\}=c\bigl(1+\log(\delta^2/c)\bigr)\quad(0<c<\delta^2)
\]
yields corner mass \((2/\pi^2)t\log(1/t)(1+O(\delta^2)+o_t(1))\); send \(t\downarrow0\) and then \(\delta\downarrow0\) to obtain the stated known normalization.

**Uniform marked density away from endpoints.** Fix \(0<\eta<1/2\). In a given corner label the two small angles \(x=X_{I+1}\), \(y=X_{I+2}\) and use \(u=\log x/\log t\), \(w=R/t\). When \(\eta\le u\le1-\eta\) and \(0<w<1\), \(x=t^u\to0\); the inradius is strictly increasing in \(y\) in the small corner, because
\[
\frac{\partial R}{\partial y}=4\sin x\cos(x+2y)>0.
\]
The implicit solution \(y=y_t(u,w)\) exists uniquely there for all sufficiently small \(t\), and uniformly for \(u\in[\eta,1-\eta]\), \(w\in[0,1]\) satisfies \(y\sim tw/(4x)\) in the absolute-error sense at \(w=0\) (and uniformly in relative error for \(w>0\)). The change of variables yields
\[
\left|\frac{\partial(x,y)}{\partial(u,w)}\right|
=t\log(1/t)\frac{x}{\partial R/\partial y}
=\frac{t\log(1/t)}4(1+o(1))
\]
uniformly on that rectangle. Multiplying by the constant density \(8/\pi^2\) proves that in each corner the unconditioned \((u,w)\)-density is \((2/\pi^2)t\log(1/t)(1+o(1))\) uniformly there. Dividing by the full event probability, the conditional density tends uniformly to \(1/3\) for each index on every \([\eta,1-\eta]\times(0,1)\).

**Removal of the truncation and total variation.** The limiting mass of those three rectangles is \(1-2\eta\). By integrating the uniform local densities, their conditional mass also tends to \(1-2\eta\), so the mass omitted, including all other corners, regions and values of \(u\) outside \((0,1)\), has limsup at most \(2\eta\). The \(L^1\) error inside tends to zero. The total-variation distance is therefore at most \(2\eta+o(1)\); let \(\eta\downarrow0\). This proves the complete joint limit, the corner-index independence and both independent uniform marks. No finite-sample simulation is used as an infinite proof.

## Verification

The standalone file `verify_cyclic_marks.py` implements an independent sampling calculation using uniform cyclic spacings and the exact inradius identity, checks three shrinking thresholds, and compares the empirical corner labels and the conditional \((U_t,W_t)\) distributions with their predicted limits. The program completed for \(650{,}000\) trials at each of \(t=0.03,0.01,0.003\). Because logarithmic convergence is slow, the finite-threshold ratios to the leading scalar asymptotic were approximately \(1.692,1.519,1.407\), respectively; these are not claimed to be close-to-asymptotic values. All three corner counts are near equality. This numerical evidence is corroboration only; the proof above supplies the infinite limiting statement.

## Relationship to prior work

The independently published *The full inradius law and two contrasting tails of random cyclic triangles* derives the exact marginal incircle-radius distribution and its \((6/\pi^2)t\log(1/t)\) lower tail for this same sampling model. Thus neither scalar fact is claimed here; the prior scalar distribution does not itself specify the conditional geometry or joint total-variation limit of two angular/radius marks. Finch's 2016 discussion of cyclic-triangle sampling provides the arclength-uniform model, while traditional uniform circular-spacing theory supplies the input Dirichlet law. published-finding corpus index searches for the conditional logarithmic split, alternative thin-incircle variables and joint marked limits did not identify a pre-existing equivalent marked statement. This is a finite-search originality assessment, not a proof of global historical priority.

## Limitations

The marks depend on a specified cyclic ordering. The theorem does not concern nonuniform circle samples, interior disk samples or perimeter-normalized triangle models. Convergence is qualitative total variation, without a quantitative rate. The known scalar small-inradius asymptotic is prior work. Earlier literature not available in full and unindexed treatments could affect priority. Independent mathematical audit has not been performed.

## References

1. Steven R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510, first posted 2016-10-03, https://arxiv.org/abs/1610.00510 (cyclic-triangle model and related statistics; abstract/catalogue inspected).
2. *The full inradius law and two contrasting tails of random cyclic triangles*, public research result, 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-full-inradius-law-and-two-contrasting-tails-of-random-cyclic--f4fa44ae752a (complete RESULT.md inspected; known scalar distribution and endpoint asymptotics).
3. P. Kórus, *Average Values of Triangles*, Fundamental Journal of Mathematics and Applications 3 (2020), 57–60, DOI:10.33401/fujma.692916 (known radius moments; bibliographic comparison).
