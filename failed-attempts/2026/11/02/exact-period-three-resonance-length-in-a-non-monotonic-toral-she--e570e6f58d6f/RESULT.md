# Exact period-three resonance length in a non-monotonic toral shear

## Finding
For the continuous area-preserving toral shear family of Myers Hill, Sturman, and Wilson, define
\[
H_\eta(x,y)=\bigl(x+f_\eta(y),\ y+x+f_\eta(y)\bigr)\pmod 1,
\qquad 0<\eta<\tfrac12,
\]
where
\[
f_\eta(y)=\begin{cases}
 y/(1-\eta),&0\le y\le1-\eta,\\
 (1-y)/\eta,&1-\eta\le y\le1.
\end{cases}
\]
The torus has its standard quotient Euclidean metric, and \(P_3(\eta)=\operatorname{Fix}(H_\eta^3)\). The exact period-three geometric phase transition is
\[
\boxed{\mathcal H^1(P_3(\eta))=
\begin{cases}
0,&0<\eta<\tfrac12,\ \eta\ne\tfrac13,\\
\tfrac49(1+\sqrt2+\sqrt5),&\eta=\tfrac13.
\end{cases}}
\]
For every nonresonant parameter, \(P_3(\eta)\) is finite. At \(\eta=1/3\), it is the union of finitely many points and exactly **six maximal connected straight segments**, two each of respective flat-torus lengths \(2/9\), \(2\sqrt2/9\), and \(2\sqrt5/9\). These split into twelve natural affine-itinerary pieces, four each of respective lengths \(1/9\), \(\sqrt2/9\), and \(\sqrt5/9\). The six segments form two disjoint three-cycles under the map. Every relative-interior point has least period three. The conclusion concerns the full torus, not a selected symbolic subsystem. In particular, none of the parameters in the stated open interval supports a positive-area subset of period-three points.

## Assumptions and scope
The phase coordinates are representatives in \([0,1]^2\) with opposite sides identified. Addition and reduction modulo one are performed after the two shear operations. The tent apex is at \(1-\eta\). The map is continuous across the tent apex and torus seams; choices of branch or wrap at a boundary do not change its torus value. Hausdorff length is measured in the flat torus, not by adding multiplicities of symbolic presentations. The statement covers only \(0<\eta<1/2\) and only period dividing three; no mixing-rate claim is made.

## Proof
**(1) The sole possible resonance parameter.** On a tent branch of slope \(s\), the derivative is
\[
B(s)=\begin{pmatrix}1&s\\1&1+s\end{pmatrix}.
\]
Thus \(B_L=B(1/(1-\eta))\) and \(B_R=B(-1/\eta)\), both of determinant one. Each three-step symbolic itinerary has derivative a product of three such matrices. Cyclically permuting factors does not change the trace (and here \(\det(I-A)=2-\operatorname{tr}A\)); reversal is also trace-equivalent for the words of length three with two symbols. Direct multiplication gives the four complete classes:
\[
\begin{array}{c|c}
\text{itinerary class}&\det(I-A)\\\hline
LLL&-(4-3\eta)^2/(1-\eta)^3\\
LLR&(4-3\eta)(2-3\eta)/(\eta(1-\eta)^2)\\
LRR&3(3\eta-1)/\eta^2\\
RRR&(3\eta-1)^2/\eta^3
\end{array}
\]
Only \(\eta=1/3\) makes one of these determinants vanish in the specified range. After fixing a three-step tent itinerary and two integer wrap choices at every step, \(H_\eta^3\) is affine on a convex polygon, and its fixed points solve \((I-A)z=w\). There are at most \(2^3\cdot4^3=512\) such closed itinerary polygons. Outside \(\eta=1/3\), all associated matrices are invertible and each polygon contributes at most one point. Boundary points are included in at least one closed itinerary polygon, so this also proves finiteness on the whole torus.

**(2) Exact finite rational census at the resonance.** Set \(\eta=1/3\). The two branches are \(f_L(y)=3y/2\) and \(f_R(y)=3-3y\); all coefficients, polygon bounds, intersections, and intersections with affine fixed loci are rational. Enumerate three successive choices \((b,m,n)\), where \(b\in\{L,R\}\) selects the branch, and \(m,n\in\{0,1\}\) are the coordinate wraps. For each choice intersect the preimage inequalities for \(x_j,y_j\in[0,1]\) and \(y_j\in[0,2/3]\) if \(b=L\), or \([2/3,1]\) if \(b=R\). The branch-affine update is
\[
 z_{j+1}=B_bz_j+v_b-(m,m+n),\qquad
 v_L=(0,0),\quad v_R=(3,3).
\]
Solving the resulting exact linear system \((I-A)z=w\) on each closed polygon produces exactly twelve nondegenerate **itinerary** line pieces, which join at endpoints into exactly six maximal connected straight segments. All other affine fixed loci are at most zero-dimensional. In particular, the only four rank-zero, translation-consistent words are the all-right-branch words with the same wrap pair \((m,n)\) at each step. Their return derivative is the identity, and the affine rotation center is \((n,1-m/3)\). The average of the three right-branch vertical coordinates equals the center's vertical coordinate \(1-m/3\), an endpoint of the common permitted band \([2/3,1]\). Every vertical coordinate must therefore equal that endpoint; the recurrence \(y_{j+1}=y_j+x_{j+1}-n\) then forces every horizontal coordinate to be \(n\). Consequently each such word has exactly one boundary point, yielding only two distinct fixed points after torus-side identifications, with zero length. The twelve itinerary pieces, with endpoints in the closed unit square, are:

| Branch word | First endpoint | Second endpoint | Length |
|---|---|---|---|
| LRR | \((1/3,2/9)\) | \((4/9,2/9)\) | \(1/9\) |
| LRR | \((2/9,2/9)\) | \((1/3,2/9)\) | \(1/9\) |
| LRR | \((2/3,4/9)\) | \((7/9,4/9)\) | \(1/9\) |
| LRR | \((5/9,4/9)\) | \((2/3,4/9)\) | \(1/9\) |
| RLR | \((0,8/9)\) | \((2/9,1)\) | \(\sqrt5/9\) |
| RLR | \((0,7/9)\) | \((2/9,8/9)\) | \(\sqrt5/9\) |
| RRL | \((2/3,8/9)\) | \((7/9,1)\) | \(\sqrt2/9\) |
| RRL | \((1/3,7/9)\) | \((4/9,8/9)\) | \(\sqrt2/9\) |
| RRL | \((5/9,7/9)\) | \((2/3,8/9)\) | \(\sqrt2/9\) |
| RRL | \((2/9,2/3)\) | \((1/3,7/9)\) | \(\sqrt2/9\) |
| RLR | \((7/9,7/9)\) | \((1,8/9)\) | \(\sqrt5/9\) |
| RLR | \((7/9,2/3)\) | \((1,7/9)\) | \(\sqrt5/9\) |

The twelve arcs pair off through common endpoints (including opposite-side torus identifications), giving six connected straight segments. The exact endpoint-incidence graph has six degree-two joining vertices and twelve degree-one terminal vertices. The six maximal segments have squared lengths \(4/81\), \(8/81\), and \(20/81\), with two of each. The displayed list is not a numerical fit: the accompanying `verify_resonance.py` is an exact-arithmetic, finite exhaustive certificate for the 512 itinerary/wrap cases. It implements explicit affine-composition matrices, exact rational segment clipping, boundary-inclusive feasibility tests, and assertions on the complete length histogram. Its twelve itinerary segments have no overlapping relative interiors or unrecorded crossings, including after opposite unit-square sides are identified: segments touch those seams only at endpoints. The exact endpoint graph verifies six maximal connected components, with no intersections between them. Therefore their \(\mathcal H^1\)-measures add, and finitely many isolated points contribute zero. The asserted exact formula follows.

**(3) Direct witness and least period.** One representative interval is
\[
 S=\{(x,2/9):1/3<x<4/9\}.
\]
Its successive images at \(\eta=1/3\) are explicitly
\[
(x,2/9)\mapsto(x+1/3,x+5/9)
\mapsto(5/3-2x,11/9-x)\mapsto(x,2/9).
\]
The first image differs from the starting point. The other maximal line components are cyclically permuted by the homeomorphism \(H\), and their rational itinerary-piece midpoints are checked to have least period three by the exact certificate. Because \(H^3\) fixes these components pointwise, their six-component permutation has order dividing three; as no component consists of fixed points, it is exactly two disjoint three-cycles. Since the fixed-point set of \(H\) is finite (indeed, the tent map takes integer values only at its endpoints and apex), every nondegenerate segment consists of least-three points except at most finitely many possible fixed endpoints. Finally, finite fixed-point sets and finite unions of straight segments have zero \(\mathcal H^2\)-measure.

## Verification
Run `python3 verify_resonance.py` with Python 3.11 or later; only the standard library is used. The script enumerates all 512 branch-and-wrap words and computes intersections using `fractions.Fraction`. Assertions certify that 256 words have singular three-step derivative at resonance, four identity-affine words have only one feasible boundary point each, exactly twelve positive-length line pieces remain, and their squared-length histogram is four each of \(1/81\), \(2/81\), and \(5/81\). It also verifies midpoint return, nonfixedness, and absence of pairwise positive-length overlap. Separately, direct symbolic multiplication verifies all four determinant factorizations above. The finite exact enumeration is a proof component restricted to the explicitly finite 512-cell decomposition; it is not an empirical proxy for an infinite-time assertion. No independent validation is claimed.

## Relationship to prior work
Myers Hill, Sturman, and Wilson introduced this toral shear family and proved mixing properties on portions of its parameter range; they explicitly identified the loss of hyperbolicity of a three-step itinerary matrix at \(\eta=1/3\) and discussed emerging period-three islands for greater parameters. The present contribution **does not** claim discovery of that critical parameter or of the qualitative period-three mechanism. It determines the complete critical set's positive-length decomposition and its exact one-dimensional Hausdorff measure, and shows isolation of period-three points at every other parameter in \((0,1/2)\). Their later paper on the different orthogonal-two-tent shear family discusses periodic segments and slowed mixing, but does not provide this critical 12-segment census or its length. Classical symbolic-affine methods motivate the finite cell decomposition; the explicit instance-specific complete rational census and geometric total are the additional claims.

## Limitations
The theorem is about fixed points of the third iterate, not the count of arbitrary higher periods or the invariant probabilities of \(H_\eta\). It supplies no decay-of-correlation rate and does not establish a positive-area elliptic island exactly at the resonance. The finite-exhaustive certificate is transparent and reproducible but has not received independent audit; unindexed literature may contain equivalent formulas. Boundary representatives can be duplicated among the closed itinerary cells, but that duplication affects neither the positive-length decomposition nor its Hausdorff measure.

## References
1. J. Myers Hill, R. Sturman, M. C. T. Wilson, *A Continuous Family of Non-Monotonic Toral Mixing Maps*, arXiv:2112.07346, initially public 2021-12-14. Published as *A Family of Non-Monotonic Toral Mixing Maps*, Journal of Nonlinear Science **32**, article 31 (2022), DOI:10.1007/s00332-022-09790-0.
2. J. Myers Hill, R. Sturman, M. C. T. Wilson, *Loss of Exponential Mixing in a Non-Monotonic Toral Map*, arXiv:2303.08515 (2023), on a distinct two-tent toral shear system.
