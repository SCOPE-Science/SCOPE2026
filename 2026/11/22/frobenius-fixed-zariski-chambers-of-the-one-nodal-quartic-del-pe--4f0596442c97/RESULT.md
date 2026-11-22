# Frobenius-fixed Zariski chambers of the one-nodal quartic del Pezzo resolution

## Finding
Let \(k=\mathbb F_q\) be a finite field of odd characteristic and let \(X/k\) be a smooth weak del Pezzo surface of degree four whose geometric anticanonical model has precisely one \(A_1\) singularity. Suppose geometrically that \(X\) is the blowup of five distinct plane points, with precisely one collinear triple and no other collinear triple. Denote by \(Z_r(g)\) the number of geometric Zariski chambers with negative-support cardinality \(r\) that are invariant under the action \(g\) on the geometric Picard lattice. A field-rational chamber means a geometric chamber stable under Frobenius; equivalently, its support is defined over \(k\).

The canonical geometric \((-2)\)-curve is unique, and the Frobenius element belongs to its root stabilizer \(G\cong S_4\times C_2\), of order \(48\), inside \(W(D_5)\). The complete fixed-chamber generating polynomial \(Z_g(t)=\sum_{r=0}^{5}Z_r(g)t^r\) depends only on the cycle partition \(\lambda\) in \(S_4\) and the central-coordinate exponent \(\epsilon\in\{0,1\}\), as follows:

| \(\lambda\) | \(\epsilon\) | Class size | \((Z_0,Z_1,Z_2,Z_3,Z_4,Z_5)\) | Total |
|---|---:|---:|---|---:|
| \((1,1,1,1)\) | 0 | 1 | \((1,13,58,112,87,14)\) | 285 |
| \((1,1,1,1)\) | 1 | 1 | \((1,5,14,20,25,4)\) | 69 |
| \((2,1,1)\) | 0 | 6 | \((1,7,18,26,27,8)\) | 87 |
| \((2,1,1)\) | 1 | 6 | \((1,3,6,6,5,2)\) | 23 |
| \((2,2)\) | 0 | 3 | \((1,1,6,4,7,2)\) | 21 |
| \((2,2)\) | 1 | 3 | \((1,1,2,0,1,0)\) | 5 |
| \((3,1)\) | 0 | 8 | \((1,4,4,4,9,5)\) | 27 |
| \((3,1)\) | 1 | 8 | \((1,2,2,2,1,1)\) | 9 |
| \((4)\) | 0 | 6 | \((1,1,0,0,3,2)\) | 7 |
| \((4)\) | 1 | 6 | \((1,1,0,0,1,0)\) | 3 |

There are exactly \(30\) orbits of the full \(G\)-action on the \(285\) geometric chambers. In particular, for the class \((\lambda,\epsilon)=((4),1)\), precisely three geometric chambers are Frobenius-stable: the nef chamber; the chamber with support the unique \((-2)\)-curve; and the chamber supported by the four disjoint \((-1)\)-curves \(E_1,E_2,E_3,L_{45}\) in an appropriate geometric marking. This is a conditional classification of Frobenius actions: it does not assert that every conjugacy class is realized over every finite field.

## Assumptions and scope
Choose a geometric marking \(\operatorname{Pic}(X_{\bar k})=\mathbb ZH\oplus\bigoplus_{i=1}^{5}\mathbb ZE_i\), where \(H^2=1\), \(E_i^2=-1\), \(H\cdot E_i=0\), and distinct \(E_i\) are disjoint. Relabel so that the unique triple line passes through the first three points. Then \(-K_X=3H-\sum E_i\) is big and nef, with square four, and its unique \((-2)\)-curve is \(R=H-E_1-E_2-E_3\). For \(i<j\), write \(L_{ij}=H-E_i-E_j\) for a two-point line transform. A Zariski chamber is indexed by the support of the negative part of a Zariski decomposition of a big divisor, with the nef chamber indexed by the empty support. The classical negative-definite-support correspondence of Bauer--Funke--Neumann applies to the geometric smooth surface. The statement concerns that geometric chamber arrangement with a finite-field Galois action, not analytic chamber volumes or existence of all possible twists.

## Proof
**All negative curves.** Since \(-K_X\) is big and nef, adjunction implies that a negative irreducible curve has self-intersection \(-1\) or \(-2\). For a nonexceptional curve of class \(dH-\sum m_iE_i\), nonnegative multiplicities, the \((-1)\) conditions give \(\sum m_i=3d-1\) and \(\sum m_i^2=d^2+1\). Cauchy--Schwarz bounds \(d\leq2\); a degree-two irreducible conic through the collinear triple is impossible, leaving just the ordinary pair lines. The \((-2)\) conditions give \(\sum m_i=3d\) and \(\sum m_i^2=d^2+2\), forcing \(d\leq1\), hence only \(R\). Thus the list of all negative curves is precisely
\[
R,\quad E_1,\ldots,E_5,\quad L_{14},L_{15},L_{24},L_{25},L_{34},L_{35},L_{45}.
\]
There are twelve \((-1)\)-curves and one \((-2)\)-curve.

**Support criterion.** Any two distinct \((-1)\)-curves occurring in a negative-definite support must be disjoint, since their two-by-two principal intersection matrix would otherwise have nonnegative determinant. The curve \(R\) meets exactly \(E_1,E_2,E_3,L_{45}\) once and has no other positive intersections. For \(k\) selected, mutually disjoint \((-1)\)-curves meeting \(R\), the Schur complement of their negative identity block is \(-2+k\). Consequently, a set of negative curves is a chamber support precisely if its chosen \((-1)\)-curves are pairwise disjoint and, when \(R\) is included, no more than one selected \((-1)\)-curve meets \(R\). Exhaustive enumeration of these conditions gives \(285\) allowed supports, with size polynomial \(1+13t+58t^2+112t^3+87t^4+14t^5\). This geometric total and support polynomial are independently known and not claimed to be new.

**The Galois group and ten classes.** The roots orthogonal to \(-K_X\) form \(D_5\), with Weyl group of order \(1920\). Every geometric arithmetic action fixes \(R\), so it lies in the stabilizer of \(R\), which has order \(48\). Three orthogonal-to-\(R\) roots
\[
\alpha_1=E_2-E_3,\qquad \alpha_2=E_1-E_2,\qquad \alpha_3=H-E_1-E_4-E_5
\]
form a simple \(A_3\)-chain. The root \(\beta=E_4-E_5\) is perpendicular to all three and to \(R\), yielding commuting reflection subgroups \(W(A_3)\times W(A_1)\cong S_4\times C_2\) of order \(48\). Hence these generate the full root stabilizer. Its ten conjugacy classes are indexed by \((\lambda,\epsilon)\) as in the table. The reflections preserve intersection numbers and permute the complete list of thirteen negative classes; this can be checked from the displayed divisor classes.

**Fixed supports and orbit counts.** Represent the intersection pairing in the ordered basis \((H,E_1,\ldots,E_5)\). A root reflection is the integral linear map \(v\mapsto v+(v\cdot\alpha)\alpha\). Starting from the identity, close under the five standard \(D_5\) reflections to obtain all \(1920\) Weyl elements and restrict to the \(48\) maps fixing \(R\). On each allowed support mask, each map acts as the induced permutation of the thirteen curves. For each group element, enumerate the fixed masks, grouping by support size. The explicit \(A_3\) simple reflections label the \(S_4\) cycle type, while the commuting reflection in \(\beta\) labels \(\epsilon\). The exact integer algorithm in `verify.py` proves all ten rows and independently cross-checks the support masks using both principal-minor tests and the preceding Schur criterion. The size-weighted sum of the ten fixed-chamber totals is \(1440\), yielding by Burnside's lemma \(1440/48=30\) orbits; a separate explicit orbit enumeration also yields \(30\). For the class \(((4),1)\), the only invariant masks are the empty mask, \(\{R\}\), and \(\{E_1,E_2,E_3,L_{45}\}\).

**Descent to the field.** An arithmetic Frobenius action fixes a chamber if and only if it fixes its negative support, by the uniqueness of Zariski decompositions and the support correspondence. Conversely, any Frobenius-stable allowed support determines a divisor over \(k\) by taking its component sum; together with a sufficiently large multiple and an ample divisor over \(k\), this provides a big rational divisor whose Zariski negative support is the prescribed set. Thus the fixed-support enumerations give field-rational chamber counts for every given Frobenius class.

## Verification
The standalone standard-library Python script `verify.py` reconstructs the Picard intersection form and the thirteen curve classes; enumerates all \(8192\) subsets; tests negative definiteness by exact Bareiss determinants; independently tests the Schur-complement criterion; enumerates the \(1920\) Weyl elements and the \(48\) root-stabilizing elements; labels the ten conjugacy classes; and verifies all displayed fixed-support polynomials. It checks \(30\) orbits independently by Burnside's lemma and explicit orbits. The full run transcript in `verify_output.txt` ends with `ONE_NODAL_QUARTIC_FROBENIUS_CHAMBER_CLASSIFICATION_OK`. Exhaustive finite computation supplies a complete certificate for this finite lattice action because the matrix constructions and group closure are explicit and finite; it is not used as a substitute for the geometric completeness proof above.

## Relationship to prior work
Derenthal--Joyce--Teitler (arXiv:math/0703202, first publicly posted 2007-03-07), especially Sections 5--7, establish root systems, Weyl actions, and nef-cone volumes for generalized del Pezzo surfaces, including nonsplit forms. Their results concern nef volumes and Galois root data, not this ten-class distribution of Zariski chambers. Bauer--Funke--Neumann (arXiv:0912.0958, first posted 2009-12-04), especially Proposition 1.1, give the negative-support correspondence, and their table reports \(393\) chambers for a **smooth** quartic del Pezzo. Bauer--Schmitz (arXiv:1205.3817, first posted 2012-05-16) study geometric chamber volumes. An independently available calculation of the one-nodal model reports the \(285\) geometric chambers and the support polynomial; those are explicitly accepted as prior, not part of the present originality claim. What is asserted here is the complete arithmetic fixed-subgroup enumeration for the ten conjugacy types and the \(30\)-orbit count. The classification is distinct from the smooth-quartic finite-field calculation, which concerns sixteen \((-1)\)-curves and \(393\) supports rather than thirteen negative curves including \(R\).

## Limitations
All numerical claims are for the prescribed geometric one-\(A_1\) weak quartic model and the indicated arithmetic actions. The argument does not prove realization of each of the ten classes over every finite field or classify other weak del Pezzo singularity configurations. No claim about chamber volumes over finite fields is made. Unindexed historical calculations may already contain equivalent fixed-support enumerations; targeted searches are not proof of global priority. No independent external mathematical audit has been performed.

## References
- U. Derenthal, M. Joyce, Z. Teitler, *The nef cone volume of generalized Del Pezzo surfaces*, arXiv:math/0703202 (first posted 2007-03-07), https://arxiv.org/abs/math/0703202.
- T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (first posted 2009-12-04), https://arxiv.org/abs/0912.0958.
- T. Bauer, D. Schmitz, *Volumes of Zariski chambers*, arXiv:1205.3817 (first posted 2012-05-16), https://arxiv.org/abs/1205.3817.
- *The 285 Zariski chambers of a one-nodal quartic del Pezzo resolution*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-285-zariski-chambers-of-a-one-nodal-quartic-del-pezzo-resolu--1e41cbd76c21.
