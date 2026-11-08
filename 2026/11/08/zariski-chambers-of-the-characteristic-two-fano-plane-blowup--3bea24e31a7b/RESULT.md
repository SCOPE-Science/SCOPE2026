# Zariski chambers of the characteristic-two Fano-plane blowup

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(X\) be the blowup of \(\mathbb P^2_k\) at all seven \(\mathbb F_2\)-rational points. Let \(z_r(X)\) denote the number of Zariski chambers in the big cone whose generic negative part is supported on exactly \(r\) distinct irreducible curves, including the nef chamber for \(r=0\). Then
\[
\sum_{r\ge0}z_r(X)t^r
=1+14t+91t^2+322t^3+651t^4+728t^5+392t^6+58t^7.
\]
Consequently \(z(X)=2257\), and the maximum support size is \(7\).

More structurally, the only negative irreducible curves are the seven exceptional \((-1)\)-curves and the seven strict transforms of the \(\mathbb F_2\)-lines, which have self-intersection \(-2\). Their nonzero pairwise intersections form the point-line incidence graph of the Fano plane, also called the Heawood graph. A subset of these fourteen curves supports a Zariski chamber if and only if the corresponding induced graph has maximum degree at most one (a disjoint union of isolated vertices and isolated edges). This criterion identifies all chambers, not just their number.

## Assumptions and scope

The blowup is taken over the algebraically closed field \(k\), although its centers are defined over \(\mathbb F_2\). The seven points are the projective classes of all nonzero triples in \(\mathbb F_2^3\). They form the Fano plane: seven lines, each containing three marked points, and any two marked points lie on a unique such line. A Zariski chamber is counted through its generic negative support, as in Bauer–Funke–Neumann's correspondence between chambers other than the nef chamber and reduced negative-definite divisors. This is a smooth weak del Pezzo surface with anticanonical degree \(2\), *not* the smooth del Pezzo surface obtained by blowing up seven points in general position.

## Proof

**1. Anticanonical nefness and bigness.** Let \(H\) be the pullback of a line and \(E_1,\dots,E_7\) the exceptional curves. Then \(-K_X=3H-\sum_iE_i\) and \((-K_X)^2=2\). In characteristic two the cubics
\[
XY(X+Y),\qquad XZ(X+Z),\qquad YZ(Y+Z)
\]
vanish simultaneously, over \(k\), exactly at the seven marked points. Their linear terms generate the cotangent space at each such point: in coordinate charts this follows from the derivatives of \(s(s+1)\) and \(t(t+1)\) at \(s,t\in\{0,1\}\). Thus the corresponding anticanonical sections have no residual base points after the seven blowups. In particular \(-K_X\) is basepoint free and hence nef; its positive square makes it big.

**2. All negative curves.** If \(C\) is irreducible with \(C^2<0\), nefness and adjunction give
\[
2p_a(C)-2=C^2+K_X\cdot C,
\qquad -K_X\cdot C\ge0.
\]
It follows that the only possibilities are \((C^2,-K_X\cdot C)=(-2,0)\) or \((-1,1)\). An irreducible curve of degree zero under the blowdown is one of the exceptional \(E_i\). For any other \(C\), write \(C=dH-\sum_{i=1}^7m_iE_i\), with integers \(d\ge1\) and \(m_i\ge0\).

For a \((-2)\)-curve, the equations are \(\sum m_i=3d\) and \(\sum m_i^2=d^2+2\). Cauchy–Schwarz gives \(9d^2\le7(d^2+2)\), so \(d\le2\). For \(d=1\), the multiplicities are three ones, yielding a line through three marked points, precisely one of the seven Fano lines. For \(d=2\), they are six ones, but any six of the seven Fano points contain a collinear triple. An irreducible conic cannot pass through three distinct collinear points by Bézout. Thus there are precisely seven \((-2)\)-curves, the strict transforms \(L_j\) of the Fano lines.

For a nonexceptional \((-1)\)-curve the equations are \(\sum m_i=3d-1\) and \(\sum m_i^2=d^2+1\). Cauchy–Schwarz implies \(d\le3\). The only multiplicity patterns are: \(d=1\), two simple points; \(d=2\), five simple points; and \(d=3\), one double point and the other six simple. A line through two marked points contains a third marked point, ruling out the first pattern for an irreducible strict transform. Every five-point set contains a collinear triple: otherwise its ten unordered point pairs would determine ten distinct Fano lines, but there are only seven. This rules out the irreducible conic. In the cubic case, each of the three Fano lines through the proposed double point meets the cubic with multiplicity at least \(2+1+1=4>3\), hence must be a component. Such a cubic cannot be irreducible. Therefore the seven \(E_i\) are the only \((-1)\)-curves, proving exhaustiveness of the fourteen negative curves.

**3. Intersection graph and definiteness.** We have
\[
E_i^2=-1,\quad L_j^2=-2,\quad E_i\cdot E_{i'}=L_j\cdot L_{j'}=0\quad (i\ne i',\ j\ne j'),
\]
and \(E_i\cdot L_j=1\) exactly when the point \(i\) belongs to the line \(j\), otherwise \(0\). Hence the intersection graph is the Heawood graph. If an induced support graph has maximum degree at most one, its intersection form is block diagonal, with blocks \((-1)\), \((-2)\), and
\[
\begin{pmatrix}-1&1\\1&-2\end{pmatrix};
\]
all are negative definite. Conversely, an induced vertex of degree at least two yields a three-curve principal submatrix centered at a \((-1)\)- or \((-2)\)-curve with two disjoint neighbors. The determinant of either such \(3\times3\) matrix is \(0\); therefore the full form cannot be negative definite (all principal submatrices of a negative-definite form are negative definite). Thus negative definiteness is equivalent to the induced-matching criterion. Bauer–Funke–Neumann, Proposition 1.1, gives the chamber bijection.

**4. Exact enumeration.** Index the seven points and seven lines by the nonzero three-bit vectors \(i,j\in\mathbb F_2^3\), with incidence when \(i\cdot j=0\). The exhaustive finite identity is
\[
Z_X(t)=\sum_{P\subseteq\{1,\ldots,7\}}\ \sum_{J\subseteq\{1,\ldots,7\}}
t^{|P|+|J|}\,\mathbf1\!\left[\begin{array}{l}
\text{every selected point lies on at most one selected line,}\\
\text{every selected line contains at most one selected point}
\end{array}\right].
\]
The attached standalone verifier evaluates all \(2^{14}=16384\) possible vertex subsets, computing their exact principal-submatrix definiteness by rational Gaussian elimination separately from the incidence-degree test. It gives the coefficient vector \((1,14,91,322,651,728,392,58)\), with all later coefficients zero; summing yields \(2257\). Thus the finite computation is exhaustive and, combined with the established chamber-support correspondence, proves the numerical claims.

## Verification

Run `python3 verify_fano.py` with standard Python 3. The verifier constructs the Fano incidences from three-bit vectors, builds the complete \(14\times14\) intersection matrix, and independently checks Sylvester positivity for all \(16384\) possible supports using exact rational Schur elimination. It asserts agreement with the induced-matching criterion and with each claimed polynomial coefficient and total. The expected run is recorded verbatim in `verify_output.txt`, ending `ALL_CHECKS_PASSED`. The general geometric negative-curve classification is proved above and is not inferred from finite experimental enumeration.

## Relationship to prior work

Bauer–Funke–Neumann, *Counting Zariski chambers on Del Pezzo surfaces* (arXiv:0912.0958, first public 2009-12-04), establish the negative-definite support bijection (Proposition 1.1) and count chambers for *general-position* blowups, including a degree-two del Pezzo surface with \(33645\) chambers. Their generic theorem does not apply directly to this highly special characteristic-two configuration, where seven \((-2)\)-curves replace most usual exceptional curves. Bauer–Schmitz, *Zariski chambers on surfaces of high Picard number* (arXiv:1204.4373), give a general computational acceleration and apply it to the Segre–Schur quartic, not to this Fano-plane blowup. The present statement contributes the complete negative-curve classification for this configuration, its Heawood induced-matching characterization, and the exact support polynomial. The arithmetic/geometric Heawood incidence itself is classical. No assertion is made that its dissociation polynomial is unknown as a graph-theoretic object.

## Limitations

This concerns the big-cone Zariski chamber decomposition of the specified weak del Pezzo surface in characteristic two, not the Mori chamber decomposition or a general-position del Pezzo. A finite literature search cannot establish historical priority. Specialist accounts of this particular weak del Pezzo surface and existing tabulations of Heawood dissociation sets are a residual overlap risk; the geometric connection and exact polynomial should receive independent priority review. No independent mathematical audit has yet been performed.

## References

1. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (initial submission 2009-12-04), especially Proposition 1.1 and Section 3. https://arxiv.org/abs/0912.0958
2. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (initial submission 2012-04-19), especially Proposition 1.1 and the stated examples. https://arxiv.org/abs/1204.4373
3. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in characteristic 2*, for comparison with **smooth** degree-two del Pezzo surfaces (the present surface is only weak del Pezzo). https://dept.math.lsa.umich.edu/~idolga/autodelPezzoEven.pdf
