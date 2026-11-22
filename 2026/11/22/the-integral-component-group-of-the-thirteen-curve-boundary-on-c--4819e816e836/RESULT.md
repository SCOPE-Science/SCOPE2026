# The integral component group of the thirteen-curve boundary on Cayley's four-nodal cubic resolution

## Finding
Let \(X\) be the blow-up of \(\mathbb P^2_{\mathbb C}\) at the six pairwise intersections of four lines with no triple concurrence. Equivalently, \(X\) is the minimal resolution of Cayley's four-nodal cubic surface. Let \(D\subset X\) be the reduced sum of **all thirteen negative curves**: four \((-2)\)-curves, six exceptional \((-1)\)-curves, and three diagonal \((-1)\)-curves.

The divisor \(D\) is a connected stable nodal curve with thirteen rational components, twenty-one ordinary nodes, and arithmetic genus nine. Its dual graph \(\Gamma\) has complete integral critical group
\[
\boxed{K(\Gamma)\cong \mathbb Z/7\mathbb Z\oplus(\mathbb Z/91\mathbb Z)^2.}
\]
In primary notation, this is \((\mathbb Z/7\mathbb Z)^3\oplus(\mathbb Z/13\mathbb Z)^2\), of order \(57\,967\) and exponent \(91\). The graph Laplacian has exact characteristic polynomial
\[
\det(tI-L_\Gamma)=t(t^2-8t+13)^3(t^2-6t+7)^3.
\]
In particular there are \(57\,967\) spanning trees. If \(D\) occurs as the reduced special fiber of any proper regular split semistable family of curves with smooth geometrically connected generic fiber and unit node thicknesses, the **geometric** component group of the generic Jacobian's Néron model is precisely the displayed finite group.

## Assumptions and scope
The ground field for the geometric assertion is \(\mathbb C\). Label the four original lines \(\ell_0,\ell_1,\ell_2,\ell_3\), their six distinct intersections \(p_{ij}=\ell_i\cap\ell_j\) for \(0\le i<j\le3\), and the blow-up map \(\pi:X\to\mathbb P^2\). In \(\operatorname{Pic}(X)\), write \(H\) for the pullback of a line and \(E_{ij}\) for the six exceptional curves, with intersection form \(H^2=1\), \(H\cdot E_{ij}=0\), \(E_{ij}^2=-1\) and distinct exceptional classes mutually orthogonal.

There are four strict original-line transforms
\[
R_i=H-\sum_{j\ne i}E_{\min(i,j),\max(i,j)},
\]
and three diagonal transforms
\[
T_{ij\mid kl}=H-E_{ij}-E_{kl},\qquad\{\{i,j\},\{k,l\}\}\text{ a perfect matching of }\{0,1,2,3\}.
\]
The full reduced boundary is \(D=\sum_iR_i+\sum_{i<j}E_{ij}+\sum_TT\). No assertion is made that this divisor is a fiber of a fibration on \(X\); the semistable-smoothing assertion concerns \(D\) as an abstract nodal curve. The graph critical group is \(\operatorname{coker}(L_\Gamma^{\mathrm{red}})\), where one vertex is deleted from a connected graph Laplacian; it is independent of that choice.

## Proof
**1. Geometric boundary and normal crossings.** The four \(R_i\) have self-intersection \(-2\); all six \(E_{ij}\) and all three \(T\) have self-intersection \(-1\). Their pairwise intersection numbers are \(1\) precisely for \(R_i\) with \(E_{ij}\), for \(T_{ij\mid kl}\) with \(E_{ij}\) or \(E_{kl}\), and for any two distinct diagonal transforms \(T\). All other distinct pairs have intersection zero. The three diagonal lines form the diagonal triangle of the original complete quadrangle, with three distinct vertices away from the six blown-up points. Hence these intersections are twenty-one distinct transverse ordinary nodes; there is no triple concurrence on \(X\).

For completeness, these are exactly the negative curves on \(X\). Indeed, \(-K_X=3H-\sum E_{ij}=H+\frac12\sum_iR_i\) is nef: its intersection with any irreducible curve other than the \(R_i\) is nonnegative, while \((-K_X)\cdot R_i=0\). Adjunction restricts each negative irreducible curve to \((C^2,(-K_X)\cdot C)=(-1,1)\) or \((-2,0)\). For a nonexceptional plane image of degree \(d\) with multiplicities \(m_{ij}\), these conditions yield respectively \(\sum m_{ij}=3d-1,\sum m_{ij}^2=d^2+1\), or \(\sum m_{ij}=3d,\sum m_{ij}^2=d^2+2\). Cauchy's inequality bounds \(d\le2\) in either case. Degree-one possibilities are precisely the original four lines (three marked points each, self-intersection \(-2\)) and the three diagonals (two marked points each, self-intersection \(-1\)). Every five of the six marked points contain a collinear triple, so no irreducible conic through five of them exists; likewise none through all six. The degree-zero case gives the six exceptional curves.

The dual graph is connected. Its four \(R_i\) have valency three, six \(E_{ij}\) have valency three, and three \(T\) have valency four. Every component is \(\mathbb P^1\) meeting the rest at least three times, so \(D\) is stable. There are \(4+6+3=13\) vertices and \(12+6+3=21\) edges, hence \(p_a(D)=21-13+1=9\).

**2. Laplacian and its characteristic polynomial.** Order vertices by the four \(R_i\), the six \(E_{ij}\), then the three \(T\). Let \(Q\) be the unsigned \(4\times6\) vertex-edge incidence matrix of \(K_4\); let \(P\) be the \(3\times6\) matrix whose rows are the three perfect matchings. With \(J_r\) denoting the \(r\times r\) all-ones matrix, the Laplacian is
\[
L_\Gamma=\begin{pmatrix}
3I_4&-Q&0\\
-Q^{\mathsf T}&3I_6&-P^{\mathsf T}\\
0&-P&5I_3-J_3
\end{pmatrix}.
\]
The identities \(QQ^{\mathsf T}=2I_4+J_4\), \(PP^{\mathsf T}=2I_3\), and \(QP^{\mathsf T}=J_{4\times3}\) give three invariant blocks over \(\mathbb Q\), with dimensions three, six and four. The constant-coordinate block is
\[
\begin{pmatrix}3&-3&0\\-2&3&-1\\0&-2&2\end{pmatrix},
\]
with characteristic polynomial \(t(t^2-8t+13)\). On the three-dimensional sum-zero subspace of the four vertices and its image under \(Q^{\mathsf T}\), the repeated \(2\times2\) block is \(\bigl(\begin{smallmatrix}3&-2\\-1&3\end{smallmatrix}\bigr)\), with characteristic polynomial \(t^2-6t+7\). On the two-dimensional sum-zero subspace of the three matchings and its image under \(P^{\mathsf T}\), the repeated block is \(\bigl(\begin{smallmatrix}3&-1\\-2&5\end{smallmatrix}\bigr)\), with characteristic polynomial \(t^2-8t+13\). These spaces have total dimension \(3+6+4=13\), proving the displayed characteristic polynomial. The matrix-tree theorem now yields
\[
|K(\Gamma)|=\frac{13^3\,7^3}{13}=7^3\,13^2=57\,967.
\]

**3. Full integral structure, not just order.** The same block decomposition is valid over \(\mathbb F_7\) and \(\mathbb F_{13}\): its direct-sum projectors require only division by \(2\), \(3\), and \(4\). The three-dimensional constant block has nullity one in either characteristic (a \(2\times2\) minor equals three). In characteristic seven, the standard \(2\times2\) block has rank one and the matching block is invertible, yielding Laplacian nullity \(1+3=4\). In characteristic thirteen, the standard block is invertible and each matching block has rank one, yielding nullity \(1+2=3\). Deleting one vertex reduces these nullities by one, so a reduced Laplacian has nullities three modulo seven and two modulo thirteen. As the full critical-group order has respective valuations three and two, each primary group must be elementary abelian. Therefore
\[
K(\Gamma)\cong(\mathbb Z/7\mathbb Z)^3\oplus(\mathbb Z/13\mathbb Z)^2
\cong\mathbb Z/7\mathbb Z\oplus(\mathbb Z/91\mathbb Z)^2.
\]
This establishes all invariant factors without inferring them from the rational spectrum.

**4. Arithmetic interpretation.** For a proper regular semistable smoothing with split nodes and unit thicknesses, Raynaud's degree-class-group description identifies the geometric Néron component group with the reduced graph-Laplacian cokernel. The assertion is conditional on that model and does not identify the Picard group of the surface \(X\).

## Verification
The accompanying `verify_cayley_boundary.py` uses only the Python standard library. It constructs an explicit rational complete quadrangle; checks that the three diagonal intersections are distinct; reconstructs the thirteen divisor classes and all twenty-one transverse graph incidences by the intersection form; computes the exact Laplacian characteristic polynomial from integer traces; computes its reduced determinant by fraction-free Bareiss elimination; and performs independent finite-field Gaussian eliminations. The resulting ranks are nine modulo seven and ten modulo thirteen for a \(12\times12\) rooted Laplacian, confirming the theoretical ranks and all invariant factors. See `verification_output.txt` for actual output. These finite checks certify the specific finite incidence matrix; the algebraic proof supplies the geometric and arithmetic generality.

## Relationship to prior work
Hassett's *Rational surfaces over nonclosed fields*, §4.1 (2009), gives the four-nodal Cayley cubic, its nine lines, and its resolution by the complete quadrangle's six-point blow-up. Derenthal–Hausen–Heim–Keicher–Laface (arXiv:1409.0799, Theorem 3.1, type \(4A_1\)) give the Cox ring with thirteen generators, not the curve's graph Jacobian. Busonero–Melo–Stoppino (arXiv:math/0602553) establish general degree-class-group methods for stable curves but do not calculate this Cayley boundary. A published Zariski-chamber calculation for the same resolution gives its thirteen negative curves and their support-count polynomial, not the integral cokernel of their nodal-incidence graph. These earlier results provide the geometric configuration or general machinery, but do not state the present \(7\)- and \(13\)-primary classification. The absence of a matching indexed publication is not proof of historical priority.

## Limitations
The primary theorem concerns this unique complex four-nodal cubic resolution and the reduced union of its thirteen negative curves. No statement is made about arbitrary singular cubic surfaces, nonregular smoothing models, non-unit node thicknesses, or arithmetic descent of component groups over nonclosed residue fields. The characteristic polynomial alone determines the group order, not the integral isomorphism type; the prime-local ranks are indispensable. An unindexed specialist computation remains a priority risk. Independent mathematical audit has not been performed.

## References
1. B. Hassett, *Rational surfaces over nonclosed fields*, in *Arithmetic Geometry*, Clay Mathematics Proceedings 8 (2009), §4.1, pp. 188–190; https://www.claymath.org/wp-content/uploads/2022/03/cmip08c.pdf.
2. U. Derenthal, J. Hausen, A. Heim, S. Keicher and A. Laface, *Cox rings of cubic surfaces and Fano threefolds*, arXiv:1409.0799 (first posted 2014-09-02), https://arxiv.org/abs/1409.0799.
3. S. Busonero, M. Melo and L. Stoppino, *Combinatorial aspects of nodal curves*, arXiv:math/0602553 (first posted 2006-02-24), https://arxiv.org/abs/math/0602553.
4. *Zariski-chamber support polynomial of the maximally nodal cubic resolution* (published calculation, 2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-zariski-chamber-support-polynomial-of-the-maximally-nodal-cubic--496f00e7e487/RESULT.md.
