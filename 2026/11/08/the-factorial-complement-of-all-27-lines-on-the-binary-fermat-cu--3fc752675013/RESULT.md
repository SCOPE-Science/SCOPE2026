# The factorial complement of all 27 lines on the binary Fermat cubic

## Finding
Let \(S\subset\mathbb P^3_{\mathbb F_2}\) be the smooth cubic
\[
S:\quad X_0^3+X_1^3+X_2^3+X_3^3=0.
\]
Let \(D\) be the **reduced** union of its 27 geometric lines, defined over \(\mathbb F_2\), and set \(U=S\setminus D\). For every integer \(m\ge1\), put \(k_m=\mathbb F_{2^m}\) and \(Q=2^m\). Then:

1. \(D\) is the effective Cartier divisor cut out on \(S\) by
\[
 (X_0^3+X_1^3)(X_0^3+X_2^3)(X_0^3+X_3^3)=0,
\]
so \(D\sim9H\), \(p_a(D)=109\). Its 27 smooth geometric components meet in exactly 45 ordinary triple points, each defined over \(\mathbb F_4\). Frobenius fixes 3 components, 7 triple points and 9 branches; all remaining components, points and branches are in two-cycles.
2. **Every arithmetic complement has trivial Picard group**:
\[
\operatorname{Pic}(U_{k_m})=0,\qquad
\mathcal O(U_{k_m})^*/k_m^*\cong
\begin{cases}\mathbb Z^{11},&m\text{ odd},\\
\mathbb Z^{20},&m\text{ even}.
\end{cases}
\]
In particular, \(U\) is smooth, geometrically factorial and affine.
3. For any prime \(\ell\ne2\), the nonzero compactly supported étale cohomology of \(U_{\overline{\mathbb F}_2}\) has the following **geometric Frobenius eigenvalues with multiplicities**:
\[
\begin{array}{c|c|c}
 i&\text{eigenvalues}&\dim H^i_c(U_{\overline{\mathbb F}_2},\mathbb Q_\ell)\\\hline
 2&(1)^{32},(-1)^{32}&64\\
 3&(2)^{11},(-2)^9&20\\
 4&(4)^1&1.
\end{array}
\]
All other compactly supported cohomology groups vanish. Consequently,
\[
 Z(U/\mathbb F_2,T)=\frac{(1-2T)^{11}(1+2T)^9}
 {(1-4T)(1-T^2)^{32}},
\]
and for every \(m\ge1\),
\[
 \#U(k_m)=
 \begin{cases}Q(Q-2),&m\text{ odd},\\(Q-4)(Q-16),&m\text{ even}.
 \end{cases}
\]
Thus \(U(k_m)=\varnothing\) exactly when \(Q\in\{2,4,16\}\). The three point-free cases are included for completeness and **are not presented as a new priority claim**: the split-cubic-surface point-free problem, including the characteristic-two example over \(\mathbb F_{16}\), has classical antecedents.

## Assumptions and scope
The scheme \(D\) is the reduced union of every geometric line, *not* the divisor of an arbitrary arrangement chosen over the ground field. Statements over \(k_m\) concern the given diagonal model and its base changes. For the cohomology eigenvalues, the Frobenius convention is the one compatible with the Grothendieck trace formula, for which \(\mathbb Q_\ell(-1)\) has eigenvalue \(2\). The direct-sum description is at the level of semisimple Frobenius representations over \(\mathbb Q_\ell\); no claim of splitting over \(\mathbb Z_\ell\) is needed. The Picard and unit calculations hold integrally over all finite extensions.

## Proof
**Geometric boundary.** Choose \(\omega\in\mathbb F_4^*\) of order three. For each of the three partitions of \(\{0,1,2,3\}\) into unordered pairs \(\{i,j\}\sqcup\{r,s\}\), and each \(a,b\in\{1,\omega,\omega^2\}\), the equations \(X_i=aX_j\), \(X_r=bX_s\) define a line on \(S\). These 27 distinct lines are all the geometric lines of a smooth cubic surface. The displayed degree-nine section factors into exactly these 27 distinct line components, proving the claimed Cartier divisor identity. Over \(\mathbb F_4\), enumerate the 45 points of the Hermitian cubic: each lies on exactly three of the 27 lines, and no other projective point can be an intersection of two \(\mathbb F_4\)-defined lines. Distinct tangent directions for distinct lines on the smooth surface establish ordinary transverse triple points. The normalized incidence graph has 27 component vertices, 45 triple-point vertices and 135 branch edges, and is connected. Counting shows the fixed subsets under squaring have sizes 3, 7 and 9, respectively. The arithmetic genus is \(1+(9H)(8H)/2=109\) using \(H^2=3\) and \(K_S=-H\); alternatively its normalization contributes 135 node-equivalent defects, 27 components and one connected component.

**Integral Picard and units.** Over the algebraic closure, the Picard group of a smooth cubic surface is the unimodular rank-seven lattice with basis \(H,E_1,\ldots,E_6\) from six disjoint lines. The 27 line classes are the six \(E_i\), the fifteen \(H-E_i-E_j\) and the six \(2H-\sum_{j\ne i}E_j\). The complete intersection graph of the explicit 27 lines identifies six skew lines, and recovers all 27 classes by their intersections with this sixer; the accompanying exact script checks all 729 intersection pairings. Frobenius on the rank-seven lattice is an integral involution with trace 1, hence its invariant sublattice has rank four. The 27 lines form three fixed components and twelve two-cycles, giving fifteen invariant orbit-sum divisor classes. In the \(H,E_1,\ldots,E_6\) basis, a \(4\times4\) minor of their \(7\times15\) column matrix has determinant \(+1\), explicitly using zero-based row indices \((0,1,2,4)\) and orbit-column indices \((0,1,3,5)\) in the accompanying deterministic enumeration. All columns lie in the invariant sublattice. Hence their rank-four span is saturated in \(\mathbb Z^7\), and therefore equals the full invariant lattice. For odd \(m\), Frobenius has the same invariants; for even \(m\), all 27 lines are individually defined and generate the whole geometric Picard lattice, since any \(H\) is a sum of a chord class and two exceptional classes.

The Brauer group of each finite field is zero, and Hochschild--Serre descent identifies \(\operatorname{Pic}(S_{k_m})\) with the geometric Frobenius-invariant Picard lattice. The divisor sequence
\[
 0\to k_m^*\to\mathcal O(U_{k_m})^*\to
 \operatorname{Div}_D(S_{k_m})\to\operatorname{Pic}(S_{k_m})
 \to\operatorname{Pic}(U_{k_m})\to0
\]
then gives \(\operatorname{Pic}(U_{k_m})=0\) and unit ranks \(15-4=11\) (odd \(m\)) or \(27-7=20\) (even \(m\)). The divisor \(9H\) is ample, so its complement is affine. Smoothness and trivial geometric Picard group imply factoriality of the geometric coordinate ring.

**Cohomology.** The normalization of \(D_{\overline{k}}\) consists of 27 copies of \(\mathbb P^1\), so \(H^1(D_{\overline{k}},\mathbb Q_\ell)\) is the first cohomology of the bipartite incidence graph just described. Its dimension is \(135-45-27+1=64\). The Frobenius graph trace is \(9-7-3+1=0\); because its action has order two, the eigenmultiplicities are 32 each. Meanwhile \(H^2(D_{\overline{k}})=\mathbb Q_\ell(-1)^{27}\), with Frobenius \(+2\) of multiplicity 15 and \(-2\) of multiplicity 12. The seven-dimensional \(H^2(S_{\overline{k}})\), generated by line classes, has corresponding multiplicities four and three, as shown by the integral Picard matrix.

The restriction \(H^2(S_{\overline{k}})\to H^2(D_{\overline{k}})\) is injective: a class in its kernel has zero intersection against every geometric line, and the line classes span the nondegenerate Picard pairing. The localization long exact sequence for \(U=S\setminus D\), together with \(H^0(S)\cong H^0(D)\), identifies \(H_c^2(U)\cong H^1(D)\), \(H_c^3(U)\cong\operatorname{coker}(H^2(S)\to H^2(D))\), and \(H_c^4(U)\cong\mathbb Q_\ell(-2)\), with all other groups zero. This yields the stated eigenvalues, zeta function and all-extension point counts by the trace formula. The zero cases follow directly from the two factorizations.

## Verification
Two standalone Python 3 programs accompany this document. Execute `python3 verify.py` and `python3 verify_picard.py` from their directory; no external libraries are required. The first enumerates all 357 lines in \(\mathbb P^3(\mathbb F_4)\), the 45 Fermat surface points, the full incidence graph and Frobenius fixed sets, and tests the formula in degrees 1 through 6. The second verifies the integral rank-seven lattice realization, every line intersection, Frobenius involution and trace, all divisor orbit sums, and the determinant-one minor. Their exact recorded output is `verification_output.txt` and `picard_output.txt`. The finite-field enumerations are exhaustive for their stated finite domains; the all-degree claims use the structural algebraic proof above.

## Relationship to prior work
The classical 27 lines of a cubic surface, their exceptional-class lattice, and the Hermitian incidence geometry are not new. Debarre's *Around cubic hypersurfaces* explicitly notes that only three lines on the characteristic-two Fermat cubic are defined over \(\mathbb F_2\), with all 27 defined over \(\mathbb F_4\). Dolgachev and Duncan, *Automorphisms of cubic surfaces in positive characteristic*, Lemma 5.3, identify the 45 Eckardt points and 27 exceptional lines on the Hermitian model, with each line containing five Eckardt points. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines* (1981), studies the point-free line complement and classifies the small-field cases; those are not claimed as new. Sturmfels and Telen, *Positive Geometries from Cubic Surfaces* (2026), study the complement of all 27 lines from a real/positive-geometry perspective; the accessible abstract discusses positive regions and canonical forms, not the arithmetic characteristic-two Frobenius module. Its full paper was unavailable during this comparison, so priority relative to its full text has not been resolved by direct inspection.

The proposed new exact package is the all-extension **integral Picard and unit calculation** together with the explicit compactly supported Frobenius cohomology of this specific binary open surface, not the individual classical incidence or point-free ingredients. The derivation uses the lattice index-one calculation, rather than treating a previously known rational point count as a novelty certificate.

## Limitations
The statement concerns only the displayed binary Fermat cubic and its complete reduced 27-line boundary; it does not classify other cubic surfaces or arbitrary boundaries. The Frobenius decomposition is rational \(\ell\)-adic, not an integral \(\ell\)-adic decomposition. Historical priority of the entire arithmetic package is not established absolutely, because specialist literature (notably the complete text of Hirschfeld 1981 and Sturmfels--Telen 2026) could not be compared page by page. The argument is a self-contained mathematical verification, not independent peer review.

## References
- J. W. P. Hirschfeld, *Cubic surfaces whose points all lie on their 27 lines*, in *Finite Geometries and Designs*, proceedings (1981), pp. 169--171, DOI `10.1017/CBO9781107325579.020`.
- M. Homma and S. J. Kim, *Numbers of points of surfaces in the projective 3-space over finite fields*, arXiv:`1409.5842`, first posted 2014-09-20.
- O. Debarre, *Around cubic hypersurfaces*, lecture notes (2015), `https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/Duesseldorf2014.pdf`.
- I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:`1712.01167`, §5.1 and Lemma 5.3.
- B. Sturmfels and S. Telen, *Positive Geometries from Cubic Surfaces*, arXiv:`2605.11909` (2026), accessible abstract; full text not inspected.
