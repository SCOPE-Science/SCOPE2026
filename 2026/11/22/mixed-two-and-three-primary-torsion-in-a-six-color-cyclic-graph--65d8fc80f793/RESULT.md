# Mixed two- and three-primary torsion in a six-color cyclic graph-Hom quotient

## Finding

Let \(X=\operatorname{Hom}(K_3,K_6)\) be the graph-Hom polyhedral complex for the simple complete graphs. Number the **target colors** by \(\mathbb Z/6\mathbb Z\), and let \(C_6=\langle g\rangle\) act by \(g(i)=i+1\) simultaneously in all three ordered source-color blocks. For the *ordinary geometric orbit space* \(Y=|X|/C_6\),

\[
\pi_1(Y)\cong\mathbb Z/3\mathbb Z,
\qquad
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/3\mathbb Z,&i=1,\\
\mathbb Z/2\mathbb Z,&i=2,\\
\mathbb Z^{10},&i=3,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus the canonical six-cycle of colors creates two different torsion primes in adjacent positive homological degrees. In particular, the order-two class is invisible in the rational target-color homology character, and the quotient is not a lens space or a wedge of integral spheres.

## Assumptions and scope

A cell of \(X\) is an ordered triple \((A_0,A_1,A_2)\) of nonempty, pairwise disjoint subsets of \(\mathbb Z/6\mathbb Z\). Its closure is \(\Delta(A_0)\times\Delta(A_1)\times\Delta(A_2)\) and has dimension \(\sum_{j=0}^2(|A_j|-1)\le3\). Incidence means independently shrinking nonempty blocks; unused colors are permitted. The cyclic group acts on target labels only, **not** by permuting the three source positions. Quotient means pointwise geometric orbits, with fixed points retained.

## Proof

**1. Original complex and stabilizers.** The standard complete-graph Hom theorem of Babson and Kozlov gives \(X\simeq\bigvee^{61}S^3\), so \(X\) is connected and simply connected. A point in the relative interior of a Hom cell can be fixed by a color rotation only if that rotation preserves each of the three nonempty disjoint color blocks. For a rotation of order six, three, or its inverse, there are fewer than three color orbits, so such a cell is impossible. The half-turn \(g^3\) has three two-element orbits \(\{0,3\},\{1,4\},\{2,5\}\). Exactly six cells are invariant: their three blocks are the three opposite-color pairs, assigned in any order to the three source positions. Each is a product of three intervals, and the half-turn reverses all three interval coordinates. It has precisely the center of each cube as its fixed-point set. No other nonidentity group element has a fixed point. Armstrong's orbit fundamental-group theorem therefore gives \(\pi_1(Y)\cong C_6/\langle g^3\rangle\cong C_3\).

**2. Exact quotient chain groups.** Barycentrically subdivide the product-of-simplices Hom cell complex. A simplex is a strict chain of cells; its orientation is the order of increasing cell dimension. The cyclic color action preserves this order, so every orbit of flags yields a well-defined oriented quotient simplex; faces are alternating deletions, followed by canonical choice of a color-rotation orbit representative. Even when a fixed barycenter exists, this flag-orbit construction is a genuine triangulation-by-orbit cellular chain model of the geometric quotient. There are \(120,540,900,540\) original Hom cells in dimensions zero to three. The exhaustive flag calculation finds \(19440\) maximal flags and quotient chain-group ranks

\[
(\operatorname{rank} C_0,\operatorname{rank} C_1,\operatorname{rank} C_2,\operatorname{rank} C_3)
=(351,3060,5940,3240).
\]

Its Euler characteristic is \(351-3060+5940-3240=-9\), consistent independently with the fixed-point formula \(\bigl(\chi(X)+\chi(X^{g^3})\bigr)/6=(-60+6)/6=-9\).

**3. Integral Smith invariants.** The complete signed cellular differentials have respectively \(6120,17820,12960\) nonzero entries in degrees one, two, three; every adjacent composition is the zero matrix. Integer elementary row and column operations pivot on entries of absolute value one. The exact remaining matrices each have rank at most one, with every nonzero entry having the indicated absolute value. The full nonzero Smith invariant lists are

\[
\operatorname{SNF}(\partial_1):\quad 1^{\times350},
\qquad
\operatorname{SNF}(\partial_2):\quad 1^{\times2709},3,
\qquad
\operatorname{SNF}(\partial_3):\quad 1^{\times3229},2.
\]

The rank-one residual test checks all matrix positions, including zeros, and an entry of value \(\pm3\), respectively \(\pm2\), proves the final invariant is exactly three, respectively two, not a higher power. Because the next boundary target is free, torsion in the cokernel of a boundary occurs in the homology one degree below its source. The resulting free Betti ranks are \((1,0,0,10)\); the nonunit factors give \(\mathbb Z/3\) in degree one and \(\mathbb Z/2\) in degree two. There are no cells above dimension three.

## Verification

The included standard-library Python 3 program `verify.py` independently constructs all Hom cells from four-valued color assignments (three used block labels plus unused), all maximal chains and their orbit representatives, the complete signed boundary maps, and the fixed-cell census. It checks \(\partial^2=0\), all orbit-cell counts, exact integer unit reductions and all residual rank-one identities. Run `python3 verify.py`; the success marker is `HOM_K3_K6_C6_INTEGRAL_HOMOLOGY_OK`. This is an exhaustive calculation for this **single finite complex**; it is not claimed as an infinite-family certification.

## Relationship to prior work

Babson and Kozlov established the underlying Hom construction, its barycentric cell-poset model, the sphere-wedge theorem, and the original rank \(61\); none of these is new here. Their source-position symmetry is different from the target-color rotation used above. A later public finding classifies prime-order target-color rotations for \(\operatorname{Hom}(K_3,K_p)\) with odd primes \(p\ge5\), where every nonidentity rotation acts freely. Its explicitly stated scope excludes composite color counts; it cannot imply this six-color quotient with half-turn fixed points. A published complete rational target-color character yields rational ranks but cannot distinguish the two integral torsion summands. The present claim is restricted to the **first nonfree six-color cyclic orbit space's integral homology and fundamental group**, not a new nonequivariant theorem or a general composite-order formula.

## Limitations

No full homotopy equivalence, higher homotopy groups, cup-product structure, or larger composite-color classification is asserted. The integral chain calculation is reproducible but not independently mathematically audited. A not-yet-indexed source with the same geometric quotient remains a possible bibliographic priority risk. This calculation uses the existing Hom connectivity and general orbit fundamental-group theorem as prior inputs.

## References

1. E. Babson and D. N. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first publicly posted 2003-10-05), https://arxiv.org/abs/math/0310056; Definition 1.2 and Propositions 4.5–4.6.
2. M. A. Armstrong, *On the fundamental group of an orbit space*, Proc. Cambridge Philos. Soc. 61 (1965), 639–646, doi:10.1017/S0305004100038974.
3. *Prime cyclic color quotients of triangle-coloring Hom complexes: integral homology and cup-length*, public mathematical finding, 2026; specifically its stated odd-prime hypothesis and composite-color exclusion.
4. *Color-permutation characters of complete-graph Hom complexes*, public mathematical finding, 2026; specifically the rational-character theorem and explicit integral limitation.
