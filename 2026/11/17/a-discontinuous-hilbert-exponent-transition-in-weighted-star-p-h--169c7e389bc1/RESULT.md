# A discontinuous Hilbert-exponent transition in weighted star \(p\)-harmonic extension stability

## Finding

Fix an integer \(m\ge2\), a real exponent \(1<p<\infty\), and positive conductances \(w_1,\ldots,w_m\). On the unweighted metric star with center \(o\) and leaves \(v_1,\ldots,v_m\), prescribe real values \(f_i\) at its leaves. Let \(E_{p,w}(f)\) be the unique extension minimizing the weighted edge energy \(\sum_{i=1}^m w_i |f_i-u(o)|^p\). Define the sharp two-input distortion
\[
L_{p,w}=\sup_{\operatorname{Lip}_B(f-g)>0}
\frac{\operatorname{Lip}_V(E_{p,w}(f)-E_{p,w}(g))}
{\operatorname{Lip}_B(f-g)},
\]
where the Lipschitz seminorms use ordinary (unweighted) shortest-path distances on the boundary and the whole star, respectively.

**The exact classification** is
\[
\boxed{
L_{p,w}=\begin{cases}
\displaystyle\frac{2\max\{w_1^{1/(p-1)},w_2^{1/(p-1)}\}}
{w_1^{1/(p-1)}+w_2^{1/(p-1)}} & m=2,\\[2mm]
\displaystyle 2\left(1-\frac{\min_i w_i}{\sum_{j=1}^m w_j}\right) & m\ge3,\ p=2,\\[2mm]
2 & m\ge3,\ p\ne2.
\end{cases}}
\]
For \(m\ge3\) and \(p\ne2\), the supremum \(2\) is **never attained by a pair with nonconstant difference**, though it is approached by explicit arbitrarily small perturbations. In contrast, for \(p=2\) the displayed constant is attained; the two-leaf formula is attained at every pair with nonconstant difference. In particular, with equal conductances and \(m=3\), the sharp constant is \(4/3\) at \(p=2\) and \(2\) for every other finite exponent \(p>1\). Yet for any fixed boundary values the extensions depend continuously on \(p\).

## Assumptions and scope

The star has exactly one interior vertex, \(m\ge2\) boundary leaves, strictly positive conductances, real data and the *unweighted* graph metric. The weights enter only the energy, not the distance; this distinction is essential. The extension is a nonlinear operator from the leaf-data quotient by constants (with \(\operatorname{Lip}_B\)) to vertex-data quotient by constants (with \(\operatorname{Lip}_V\)). The exponent is any real \(1<p<\infty\), not a quasi-Banach target exponent.

Writing \(c_{p,w}(f)=E_{p,w}(f)(o)\), strict convexity gives the unique root
\[
\sum_{i=1}^m w_i\,\phi_p(c_{p,w}(f)-f_i)=0,
\qquad \phi_p(t)=|t|^{p-2}t,\quad \phi_p(0)=0.
\]
If \(h=f-g\), leaf distances are \(2\) and central edge distances are \(1\), whence
\[
\operatorname{Lip}_B(h)=\frac{\max_i h_i-\min_i h_i}{2},\qquad
\operatorname{Lip}_V(E(f)-E(g))=
\max_i|h_i-(c(f)-c(g))|.
\]

## Proof

**1. Universal bound and nonattainment at level two.** The root \(c\) is coordinatewise strictly increasing and translation equivariant: \(f\le g\) componentwise implies \(c(f)\le c(g)\), with strict inequality if any component inequality is strict. Indeed, \(\phi_p\) is strictly increasing, so increasing any input coordinate strictly decreases the equilibrium expression at the old root, moving the unique root strictly upwards. Also \(c(f+a\mathbf1)=c(f)+a\). Put \(a=\min_i h_i\), \(b=\max_i h_i\). Then \(a\le c(f)-c(g)\le b\). Hence the output Lipschitz seminorm is at most \(b-a=2\operatorname{Lip}_B(h)\). If \(a<b\), both inequalities are strict, so the quotient is strictly below \(2\) for *each finite pair*. Thus \(L_{p,w}\le2\), with nonattainment whenever the sharp constant is exactly \(2\).

**2. Two leaves.** Let \(\alpha_i=w_i^{1/(p-1)}\). Solving the scalar first-order condition for two terminal values shows
\[
c_{p,w}(f)=\frac{\alpha_1 f_1+\alpha_2 f_2}{\alpha_1+\alpha_2}.
\]
For \(h=f-g\) nonconstant, the ratio equals \(2\max(\alpha_1,\alpha_2)/(\alpha_1+\alpha_2)\). This proves its formula and equality assertion.

**3. Hilbert exponent.** At \(p=2\), \(c_{2,w}(f)=\sum_i (w_i/W)f_i\) with \(W=\sum_i w_i\). Write \(a_i=w_i/W\). The linear map from \(h\) to the edge difference \(h_i-\sum_j a_jh_j\) has norm \(2(1-a_i)\) under the boundary seminorm \((\max h-\min h)/2\): its upper bound follows by writing \(h_i-\sum_j a_jh_j=\sum_{j\ne i}a_j(h_i-h_j)\), and equality holds when \(h_i=1\) and \(h_j=-1\) for all \(j\ne i\). Taking an index with the smallest \(a_i\) proves the Hilbert formula.

**4. Exact sharpness for \(p>2\) and \(m\ge3\).** Relabel any three leaves as \(1,2,3\). Choose \(f_1=0\), \(f_2=1\), \(f_3=-(w_2/w_3)^{1/(p-1)}\), and \(f_i=0\) for \(i\ge4\). Then \(c_{p,w}(f)=0\). The equilibrium equation is continuously differentiable at this data, and its derivative in the central value is positive. Implicit differentiation gives
\[
D c_{p,w}(f)[h]=\sum_i a_i h_i,\qquad
 a_i=\frac{w_i|f_i-c_{p,w}(f)|^{p-2}}
{\sum_j w_j|f_j-c_{p,w}(f)|^{p-2}}.
\]
Here \(a_1=0\). With \(h_1=1\) and \(h_j=-1\) for \(j\ne1\), the boundary Lipschitz seminorm is \(1\), while the first edge difference of the infinitesimal output is \(h_1-Dc(f)[h]=2\). Thus taking \(g=f+th\) and \(t\downarrow0\) proves \(L_{p,w}\ge2\).

**5. Exact sharpness for \(1<p<2\) and \(m\ge3\).** For any \(\delta>0\), choose \(f_1=1\), \(f_i=\delta\) for \(i\ge3\), and
\[
f_2=-\left(\frac{w_1+\delta^{p-1}\sum_{i\ge3}w_i}{w_2}\right)^{1/(p-1)}.
\]
The equilibrium value is again \(c_{p,w}(f)=0\), and now all residuals are nonzero, so implicit differentiation is valid. Its positive derivative weights are proportional to \(w_i|f_i|^{p-2}\). Because \(p-2<0\), their total for \(i\ge3\) diverges as \(\delta\downarrow0\), while the first weight stays \(w_1\); hence \(a_1\to0\). Choosing \(h_1=1\), \(h_j=-1\) otherwise gives tangent amplification \(2(1-a_1)\to2\). For each \(\delta\), a sufficiently small finite perturbation realizes a ratio arbitrarily near that tangent value. Combining with part 1 gives the sharp constant and its nonattainment.

**6. Discontinuous optimal modulus.** For fixed \(f\) and positive \(w\), the unique minimizer of \(\sum_i w_i|f_i-c|^p\) depends continuously on \(p>1\), by compactness of the interval \([\min f_i,\max f_i]\) and strict convexity. This convergence is uniform on compact sets of boundary data. Yet for every \(m\ge3\), \(L_{p,w}=2\) on both sides of \(p=2\), whereas \(L_{2,w}<2\). The jump is exactly \(2\min_i w_i/W\).

## Verification

Run `python3 check_star_pmean.py` from this directory. The standalone checker requires only Python's standard library. It tests the exact weighted-Hilbert formulas using fractions and exhaustive sign vectors for several weights, the two-leaf power-mean formula, the universal two-input bound on finite samples, and both super- and sub-Hilbert sharpness constructions. The exact symbolic sub-Hilbert tangent witnesses are rational for \(p=3/2\). All cases were executed successfully. The proof above is independent of these finite diagnostics.

## Relationship to prior work

The standard finite-graph \(p\)-energy extension problem and its Hilbert and large-\(p\) versions are developed in Kyng–Rao–Sachdeva–Spielman (2015), notably the energy formulation and Theorems 7–8; their Theorem 7 concerns pointwise \(\ell_\infty\) stability of the *lexicographic infinite-exponent* extension, not the sharp two-input boundary-to-graph Lipschitz constant for each finite \(p\). Puls (2008) discusses \(p\)-harmonic graph energies in an infinite-graph boundary context. Closely related nonlinear extension constants for quasi-Banach-valued targets concern a different exponent and optimization problem. The novelty assessed here is the exact weighted all-exponent perturbation modulus and its nonattained jump at the Hilbert exponent, rather than the known existence or definition of \(p\)-energy extensions. Possible implicit treatments of one-point weighted \(p\)-means remain a priority risk.

## Limitations

This result covers one-interior-vertex stars, not general graphs or trees. It concerns the perturbation of an entire extension operator, not the ordinary one-input Lipschitz constant of each output, nor metric target spaces other than the real line. The upper bound \(2\) is a supremum and is never attained at finite distinct-input pairs for \(m\ge3\), \(p\ne2\). The numerical checker does not prove the infinite parameter range; that is established by the analytic argument. No independent mathematical validation is claimed.

## References

1. R. Kyng, A. Rao, S. Sachdeva and D. A. Spielman, *Algorithms for Lipschitz Learning on Graphs*, Proceedings of Machine Learning Research **40** (2015), 1190–1223, https://proceedings.mlr.press/v40/Kyng15.html (full text https://proceedings.mlr.press/v40/Kyng15.pdf).
2. M. J. Puls, *Graphs of bounded degree and the \(p\)-harmonic boundary*, arXiv:0806.3073, first publicly posted 18 June 2008, https://arxiv.org/abs/0806.3073.
3. T. Andersson, *An iterative solution method for p-harmonic functions on finite graphs with an implementation*, Linköping University master's thesis (2009), https://users.mai.liu.se/andbj49/pharmgraph/ (repository full text was not available for substantive inspection).
