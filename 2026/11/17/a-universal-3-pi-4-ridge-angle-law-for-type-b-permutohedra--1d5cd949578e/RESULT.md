# A universal \(3\pi/4\) ridge-angle law for type-\(B\) permutohedra

## Finding

**Theorem.** Fix an integer \(n\ge2\). Let \(P\subset\mathbb R^n\) be a full-dimensional polytope with the complete standard type-\(B_n\) Coxeter normal fan, in the ordinary coordinate Euclidean metric. For each pair of integers \(1\le k<\ell\le n\), its ridge-dihedral-angle multiset contains

\[
\theta_{k,\ell}=\pi-\arccos\sqrt{\frac{k}{\ell}}
=\frac\pi2+\arctan\sqrt{\frac{k}{\ell-k}}
\]

with multiplicity

\[
M_n(k,\ell)=2^\ell\binom n\ell\binom\ell k.
\]

These contributions are added if two different parameter pairs give the same numerical angle. There are precisely

\[
R_n=5^n-2\cdot3^n+1
\]

ridges. If \(\Theta_n\) is the angle of a uniformly sampled ridge, then, **for every dimension and every full-fan realization**,

\[
\mathbb E\Theta_n=\frac{3\pi}{4}.
\]

Moreover,

\[
\sqrt n\bigl(\Theta_n-3\pi/4\bigr)\ \Longrightarrow\ N(0,5/16),
\qquad
\operatorname{Var}(\Theta_n)=\frac{5}{16n}+o(n^{-1}).
\]

All statements also hold simultaneously for the entire class of strictly ordered signed-permutation orbit polytopes described below. The ridge count itself is a known type-\(B\) face-enumeration consequence; the specified Euclidean angle distribution and its universal mean/fluctuation law are the asserted metric conclusions.

## Assumptions and scope

For \(0<a_1<\cdots<a_n\), a concrete realization is

\[
P_n(a)=\operatorname{conv}\bigl\{(\varepsilon_1a_{\sigma(1)},\ldots,\varepsilon_na_{\sigma(n)}):\sigma\in S_n,\;\varepsilon_i\in\{-1,1\}\bigr\}.
\]

Here the strict inequalities ensure the normal fan is precisely the type-\(B_n\) Coxeter fan; no coordinate rescaling of the ambient Euclidean metric is permitted. Its facet outer normal rays are indexed by nonzero signed-support vectors \(u\in\{-1,0,1\}^n\setminus\{0\}\). For a support of size \(k\), the orbit realization has the sharp facet inequality

\[
\langle u,x\rangle\le\sum_{j=n-k+1}^n a_j.
\]

A ridge means a face of dimension \(n-2\). For \(n=2\), the interior dihedral angle is the ordinary polygon interior angle at that vertex. The sampling measure is uniform over ridges, **not** weighted by their \((n-2)\)-dimensional measures.

## Proof

**1. Facets and compatible pairs.** The fan has one ray for each nonzero signed-support vector. The standard type-\(B_n\) Coxeter fan is simplicial. Its two-dimensional cones are exactly the spans of distinct vectors \(u,v\) with strictly nested supports and matching signs on the smaller support. Consequently a ridge is uniquely represented by such a pair. This description is the geometric form of the signed-set-chain facet incidence rule; it can also be verified by ordering the absolute values of a generic linear functional and recording their signs.

**2. Exact multiplicities and angles.** Write \(k=|\operatorname{supp}u|\) and \(\ell=|\operatorname{supp}v|\), with \(k<\ell\). First choose the larger support (\(\binom n\ell\) choices), then the smaller (\(\binom\ell k\) choices), then the signs of the larger support (\(2^\ell\) choices). These choices specify each ridge exactly once and prove \(M_n(k,\ell)\). The matching-sign property gives \(\langle u,v\rangle=k\), \(\|u\|=\sqrt k\), and \(\|v\|=\sqrt\ell\). The angle of the outward normals is \(\arccos\sqrt{k/\ell}\); its supplementary angle is the interior dihedral angle, as asserted. No support function values enter, proving the fan-wide metric universality.

**3. A finite multinomial representation.** Divide each coordinate into three classes: in the smaller support, in the larger support only, or outside both. The first two classes each admit two independent sign choices, the last only one. Thus summing ridge counts is equivalent to counting words of length \(n\) over groups of respective sizes \(2,2,1\), requiring the first two groups to occur. Inclusion-exclusion gives \(R_n=5^n-2\cdot3^n+1\). Equivalently, if \((A_n,B_n,C_n)\sim\operatorname{Multinomial}(n;2/5,2/5,1/5)\), then for a uniformly sampled ridge

\[
\Theta_n\ \stackrel{d}{=}\ \frac\pi2+\arctan\sqrt{A_n/B_n}\ \bigg|\ \{A_n\ge1,\ B_n\ge1\}.
\]

The conditioning event has probability \(1-2(3/5)^n+(1/5)^n\).

**4. Exact mean.** Interchanging \(A_n\) and \(B_n\) preserves this conditional distribution. The two paired angles satisfy

\[
\left(\frac\pi2+\arctan\sqrt{a/b}\right)
+\left(\frac\pi2+\arctan\sqrt{b/a}\right)=\frac{3\pi}{2}
\]

for all positive integers \(a,b\). Hence \(\mathbb E\Theta_n=3\pi/4\) exactly.

**5. Gaussian law and variance.** The excluded multinomial event has exponentially small probability. The multinomial law of large numbers gives \(A_n/n,B_n/n\to2/5\), while

\[
\frac{A_n-B_n}{\sqrt n}\ \Longrightarrow\ N(0,4/5).
\]

For \(g(a,b)=\pi/2+\arctan\sqrt{a/b}\), at \(a=b=2/5\) its gradient is \((5/8,-5/8)\). The delta method therefore yields

\[
\sqrt n(\Theta_n-3\pi/4)\ \Longrightarrow\ N\left(0,\frac{25}{64}\cdot\frac45\right)=N(0,5/16).
\]

To justify the variance statement beyond weak convergence, restrict to \(A_n,B_n\ge n/4\). On this exponentially likely event the angle is Lipschitz, with \(|\Theta_n-3\pi/4|\le C|A_n-B_n|/n\); the fourth moments of the normalized multinomial difference are uniformly bounded. On the complement the angle is bounded and the event has exponentially small probability. This gives uniform integrability of the squared normalized angle fluctuations and proves \(n\operatorname{Var}(\Theta_n)\to5/16\).

## Verification

Run \(\texttt{python3 type_b_ridge_check.py}\) in a standard Python 3 environment. The embedded script uses only the standard library. It independently constructs all signed-permutation vertices in dimensions \(n=2,3,4\), identifies facet contacts from the coordinate support inequalities, checks the rank of every facet-pair contact set by fraction-exact elimination, compares ridge compatibility and all multiplicities, and recomputes the normal cosines and mean. The observed numbers of vertices, facets and ridges are \((8,8,8)\), \((48,26,72)\) and \((384,80,464)\). These finite computations check premises; the proof above establishes the arbitrary-dimensional claims.

## Relationship to prior work

Gábor Hetyei, *The type B permutohedron and the poset of intervals as a Tchebyshev transform* (arXiv:2007.07362, first submitted 2020-07-14), gives the signed facet labels and their chain condition (Corollary 1.11), as well as the combinatorial structure of the dual. Thus the unrefined ridge count is already implied by established face enumeration and is **not** claimed as an original counting formula. José Bastidas, *The polytope algebra of generalized permutahedra* (arXiv:2009.05876), studies type-\(B\) normal-fan deformations and their algebra; the type-\(B\) orbit polytope is classical. The proposed additional geometric information is the complete fixed-Euclidean-metric ridge angle law (for every full-fan realization), its exactly constant mean, and the sharp Gaussian fluctuation variance. The cited inspected treatments do not state these metric and probabilistic conclusions.

## Limitations

This is a theorem for a specified Euclidean metric and the **full** type-\(B\) Coxeter fan; it does not extend unchanged to singular signed-orbit weights, coarsened type-\(B\) fans, arbitrary affine transformations, or area-weighted ridge sampling. The normal-fan data and combinatorial counts are prior mathematics, not newly proved historical discoveries. The comparison of the angle law against available literature and indexed results supports, but cannot establish, historical first priority; unindexed equivalent treatments remain possible. No independent external audit is claimed.

## References

- G. Hetyei, *The type B permutohedron and the poset of intervals as a Tchebyshev transform*, arXiv:2007.07362 (initial submission 2020-07-14), https://arxiv.org/abs/2007.07362 ; see Corollary 1.11 in the accessible version.
- J. Bastidas, *The polytope algebra of generalized permutahedra*, arXiv:2009.05876 (2020), https://arxiv.org/abs/2009.05876 ; see Section 6 on type-\(B\) generalized permutahedra.
