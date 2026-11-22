# Cyclic Frobenius Picard tori of nodal line divisors: a nonsplit parity lattice

## Finding
Let \(n\ge4\) and let \(k=\mathbb F_q\) be **any** finite field. Suppose \(D\subset\mathbb P^2_k\) is the reduced union of \(n\) distinct geometric lines with no three concurrent, on which arithmetic Frobenius is a single \(n\)-cycle. (Such divisors exist for every pair \((q,n)\), as shown below.) Let \(T=\operatorname{Pic}^0_{D/k}\), let \(C_m\) denote a cyclic group of order \(m\), and put \(R_n=\operatorname{Res}_{\mathbb F_{q^n}/k}\mathbb G_m\).

The scheme \(D\) is a connected nodal curve of arithmetic genus \((n-1)(n-2)/2\), and \(T\) is a torus of that dimension. Its **complete integral Frobenius character lattice** is:
\[
X^*(T)\cong
\begin{cases}
\mathbb Z\oplus\bigl(\mathbb Z[s]/(s^n-1)\bigr)^{\oplus(n-3)/2},&n\text{ odd},\\[2mm]
\bigl(\mathbb Z[s]/(s^n-1)\bigr)^{\oplus(n-4)/2}\oplus
\mathbb Z[s]/\bigl((s-1)(s^{n/2}+1)\bigr),&n\text{ even}.
\end{cases}
\]
Here \(s\) denotes the Frobenius generator acting by multiplication; each quotient is an **integral** module, not a rational representation or an isogeny class. In the even case the final module is an intrinsically nonsplit index-two gluing of a trivial character and an antipodal signed orbit module.

Define \(U_h/k\) for \(h\ge2\) to be the torus whose character lattice is \(\mathbb Z[s]/((s-1)(s^h+1))\), with \(s\) acting by multiplication. Then equivalently:
\[
T\cong
\begin{cases}
\mathbb G_m\times R_n^{\,(n-3)/2},&n\text{ odd},\\
R_n^{\,(n-4)/2}\times U_{n/2},&n\text{ even}.
\end{cases}
\]
In particular **the full finite abelian rational-point group** is
\[
\boxed{T(k)\cong
\begin{cases}
C_{q-1}\times C_{q^n-1}^{\,(n-3)/2},&n\text{ odd},\\
C_{(q-1)(q^{n/2}+1)}\times C_{q^n-1}^{\,(n-4)/2},&n\text{ even}.
\end{cases}}
\]
The cyclic factor in the second line cannot in general be replaced by \(C_{q-1}\times C_{q^{n/2}+1}\); for odd \(q\), those two groups are not isomorphic.

The curve zeta function is determined simultaneously:
\[
\boxed{Z(D/k,t)=
\begin{cases}
\dfrac{(1-t^n)^{(n-3)/2}}{1-q^n t^n},&n\text{ odd},\\[2mm]
\dfrac{(1-t^n)^{(n-4)/2}(1+t^{n/2})}{1-q^n t^n},&n\text{ even}.
\end{cases}}
\]
For instance, for \(n=4\) and \(q=3\), the torus has cyclic rational-point group \(C_{20}\), not \(C_2\times C_{10}\), and \(Z(D/\mathbb F_3,t)=(1+t^2)/(1-81t^4)\). This distinction reflects integral rather than merely rational descent.

## Assumptions and scope
All lines and incidences are taken geometrically after base change to \(\bar k\). “No three concurrent” means that every pair of distinct lines meets transversely at a different ordinary node. Arithmetic Frobenius acts as one cycle on the set of geometric components. Its inverse (geometric Frobenius) gives an isomorphic cyclic module after changing the generator to its inverse.

The term \(\operatorname{Pic}^0\) means the connected identity component, parametrizing multidegree-zero line bundles; it does not mean the full, generally disconnected Picard functor. The formula for \(U_h\) is a definition by its complete \(k\)-torus character lattice, so it specifies an isomorphism class of tori, not just the cardinalities of their rational points.

The hypothesis is nonvacuous for every \(q\) and \(n\): choose an element \(a\in\mathbb F_{q^n}\) of degree exactly \(n\) over \(k\), and take the lines
\[
L_i:\quad X+a^{q^i}Y+a^{2q^i}Z=0,\qquad 0\le i<n.
\]
They form a Frobenius orbit. The determinant of the coefficient vectors of any three distinct conjugates is a nonzero Vandermonde product, so no three lines meet at one point, even in characteristic two.

## Proof
**1. From the curve to the complete graph.** Over \(\bar k\) the normalization is the disjoint union of \(n\) copies of \(\mathbb P^1\), and the \(\binom n2\) ordinary nodes join every unordered pair of components. The dual graph is \(K_n\). Normalization of units yields the exact sequence of \(k\)-tori
\[
1\to\mathbb G_m\to\mathbb G_m^{V}\to\mathbb G_m^{E}\to T\to1
\]
after interpreting the geometric products with Frobenius descent. On character lattices this gives \(X^*(T)=\ker(\partial:\mathbb Z^E\to\mathbb Z^V)=H_1(K_n,\mathbb Z)\), with its signed action on oriented edges. The cycle rank is \(\binom n2-n+1=(n-1)(n-2)/2\).

**2. Integral orbit elimination.** Label vertices by \(\mathbb Z/n\mathbb Z\), with \(s(i)=i+1\), and let \(e_i\) denote the oriented perimeter edge \(i\to i+1\). For each \(d\) strictly between \(1\) and \(n/2\), the oriented chords \(f_{i,d}:i\to i+d\) form one free orbit of length \(n\). Their cycles
\[
z_{i,d}=e_i+e_{i+1}+\cdots+e_{i+d-1}-f_{i,d}
\]
form a full free \(\mathbb Z[s]/(s^n-1)\)-summand. This assertion is integral: the coefficient of \(f_{i,d}\) is \(-1\), and the selected chord orbits are mutually disjoint, so deleting all such chords by these cycles is a unimodular change of the edge-chain basis. There remain only the perimeter edges and, if \(n\) is even, the antipodal chords.

**3. Odd case.** If \(n\) is odd, the perimeter alone is the residual cycle graph. Its integral cycle lattice is generated by the invariant perimeter cycle \(c=\sum_{i=0}^{n-1}e_i\). There are \((n-3)/2\) eliminated chord orbits, giving the first displayed character-module decomposition.

**4. Even case and the nonsplit extension.** Write \(n=2h\). The remaining antipodal edges are \(a_i:i\to i+h\) for \(0\le i<h\), with \(s a_i=a_{i+1}\) for \(i<h-1\) but \(s a_{h-1}=-a_0\). Put
\[
v_i=e_i+\cdots+e_{i+h-1}-a_i\quad(0\le i<h),
\qquad c=\sum_{i=0}^{n-1}e_i.
\]
Each is a cycle. Projection to the antipodal-edge coordinates maps the \(v_i\) onto a signed integral basis, and the kernel is precisely \(\mathbb Zc\), since the perimeter has one-dimensional integral cycle lattice. Hence \(c,v_0,\ldots,v_{h-1}\) are an integral basis of the residual kernel. The Frobenius action is
\[
sc=c,\qquad sv_i=v_{i+1}\ (i<h-1),\qquad sv_{h-1}=c-v_0.
\]
Thus \((s^h+1)v_0=c\), and then \((s-1)(s^h+1)v_0=0\). The listed \(h+1\) basis vectors show that **no additional integral relation** occurs. Therefore the residual module is exactly \(\mathbb Z[s]/((s-1)(s^h+1))\). The eliminated \(h-2\) chord orbits provide the displayed regular summands.

To see why this is not the split rational decomposition, an invariant generator is \(c=(s^h+1)v_0\). Every equivariant homomorphism from the residual module to the trivial module \(\mathbb Z\) sends \(c\) to an even integer: if it sends \(v_0\) to \(a\), it sends \(c\) to \(2a\). Thus \(\mathbb Zc\) admits no equivariant retraction. Over \(\mathbb Q\) it splits off, so the obstruction is genuinely integral and of index two.

**5. Exact groups of rational points.** For any finite-field torus with integral character lattice \(M\) and Frobenius matrix \(s\), the finite abelian group of rational points is (noncanonically) Pontryagin dual to \(M/(q-s)M\); hence it has the same invariant factors. For a regular summand \(\mathbb Z[s]/(s^n-1)\), substitution \(s=q\) gives \(\mathbb Z/(q^n-1)\). For the odd fixed summand it gives \(\mathbb Z/(q-1)\). In the even residual summand it gives
\[
\mathbb Z[s]/\bigl((s-1)(s^h+1),q-s\bigr)
\cong\mathbb Z/\bigl((q-1)(q^h+1)\bigr).
\]
The asserted complete finite groups follow for every prime power \(q\), including characteristic two.

**6. Zeta functions.** Normalization contributes \(1/((1-t^n)(1-q^nt^n))\). If \(n\) is odd, all node orbits have length \(n\), in number \((n-1)/2\); each has two branch orbits of length \(n\). Correcting normalization by the ratio of node and branch zeta functions yields the odd formula. If \(n=2h\), the \(h-1\) non-antipodal node orbits have length \(n\) with two branch orbits each, while the single antipodal orbit has node length \(h\) but its branches comprise **one orbit of length \(n\)**, since \(s^h\) exchanges the branches. The node/branch correction yields
\[
Z(D/k,t)=\frac{(1-t^n)^{h-1}}{(1-t^h)(1-q^nt^n)}
=\frac{(1-t^n)^{h-2}(1+t^h)}{1-q^nt^n},
\]
as asserted. This proves point counts over every finite extension, not only a finite sample.

## Verification
Run `python3 verify.py` using only the Python standard library. It builds the complete-graph integral cycle lattice independently from a star-spanning-tree basis; constructs the perimeter and translated shortcut cycles; checks that their coordinate-change determinant has absolute value one by fraction-free Bareiss elimination; and checks the full Frobenius conjugacy identity over \(\mathbb Z\) against the asserted regular and nonsplit companion modules for every \(4\le n\le11\). It also independently enumerates fixed geometric components, nodes and ordered branches for six sample values of \(q\) and every \(1\le r\le2n\), comparing point counts with the coefficients implied by the zeta formulas.

The recorded successful run is in `CHECKS.txt`. Finite checks are supplementary: the unrestricted \(n,q\) claims are proved by the integral cycle basis, polynomial quotient, normalization and Vandermonde arguments, not extrapolated from finite experiments.

## Relationship to prior work
Generic plane line arrangements and their moduli are classical; Paul, Traves and Wakefield (2014) study them through enumerative geometry rather than their finite-field Picard tori. Busonero, Melo and Stoppino (2006) develop nodal-curve dual graphs and degree-class groups, which are *component/critical groups*, not the connected Picard-torus character lattice here. Casalaina-Martin, Kass and Viviani (2011) study compactified Jacobian local rings using graph-invariant techniques rather than a cyclic Frobenius integral splitting for \(K_n\).

Other evaluated arithmetic examples of integral Picard tori concern the fifteen-line Igusa curve, the sixteen-curve quartic del Pezzo boundary, or the Heawood graph curve. Their graphs, Frobenius actions and exact claims do not imply the generic \(K_n\) theorem, particularly its even-order glued cyclic factor. The normalization/Galois-module method is standard and not claimed as new. The assessed contribution is the **uniform all-degree integral decomposition with the even-index-two obstruction**, together with the resulting complete finite groups and branch-reversal zeta spectrum. No assertion of definitive historical priority is made.

## Limitations
Only the transitive \(n\)-cycle Frobenius action and general-position ordinary nodes are covered; this does not classify arbitrary Frobenius permutations on the lines or arrangements with triple or higher intersections. The torus is the connected component of the curve Picard scheme, not a Néron component group or the Picard group of the ambient plane. The even-degree nonsplitting occurs in the integral Galois lattice irrespective of characteristic; the finite point-group distinction from the split isogeny is most visible in odd characteristic. Historical priority remains provisional and requires independent specialist review.

## References
1. S. Busonero, M. Melo, L. Stoppino, *Combinatorial aspects of nodal curves*, arXiv:math/0602553, first public 2006-02-24, https://arxiv.org/abs/math/0602553.
2. S. Casalaina-Martin, J. L. Kass, F. Viviani, *The Local Structure of Compactified Jacobians*, arXiv:1107.4166, first public 2011-07-21, https://arxiv.org/abs/1107.4166.
3. T. Paul, W. Traves, M. Wakefield, *The Enumerative Geometry of Hyperplane Arrangements*, arXiv:1409.6275, first public 2014-09-22, https://arxiv.org/abs/1409.6275.
