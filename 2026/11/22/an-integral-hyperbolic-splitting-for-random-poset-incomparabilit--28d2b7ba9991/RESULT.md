# An integral hyperbolic splitting for random-poset incomparability feasibility over every finite base

## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order, and let \(A\subseteq\mathbb P\) be any finite induced subposet whose elements are individually named. Let \(\mathcal T_A\) be its complete nonalgebraic one-point types. Index a symmetric integer matrix \(M_A\) by \(\mathcal T_A\), and set \(M_A(p,q)=1\) precisely when **distinct** realizations of the two types can be incomparable, and zero otherwise. A diagonal entry asks for two distinct incomparable realizations of the same type; it does not describe an element compared with itself.

Write \(j(A)\) for the number of downward-closed subsets of \(A\), including \(\varnothing\) and \(A\). Let \(t(A)\) count the one-point types in which the new point has **both** an old strict predecessor and an old strict successor. The number of all types is
\[
N_A=2j(A)-1+t(A).
\]
For every finite \(A\), including the empty set, the exact integral congruence is
\[
\boxed{M_A\cong_{\mathbb Z}[1]\oplus
\begin{pmatrix}0&1\\1&0\end{pmatrix}^{\oplus(j(A)-1)}\oplus 0_{t(A)}.}
\]
The basis change is unimodular over \(\mathbb Z\), not only invertible over \(\mathbb Q\). In particular,
\[
\boxed{\operatorname{SNF}_{\mathbb Z}(M_A)=\operatorname{diag}(I_{2j(A)-1},0_{t(A)})},
\qquad
\boxed{\operatorname{inertia}(M_A)=(j(A),j(A)-1,t(A))}.
\]
Consequently the rank of \(M_A\) over **every field** is \(2j(A)-1\), its integral cokernel is free of rank \(t(A)\), and its real signature is exactly \(1\). The integral null lattice has the explicit primitive basis displayed below, one vector for each two-sided type.

The result is not restricted to chains, antichains, bounded width, connected bases or height-two orders. For example, a three-point fork with one minimal element and two incomparable maximal elements has \(N_A=12\), \(j(A)=5\), and \(t(A)=3\); its matrix therefore has Smith form \(\operatorname{diag}(I_9,0_3)\) and inertia \((5,4,3)\). A four-point diamond has \(N_A=18\), \(j(A)=6\), and \(t(A)=7\), giving \(\operatorname{diag}(I_{11},0_7)\).

## Assumptions and scope
A **down-set** is any subset closed downward under the finite order (no directedness requirement); an **up-set** is closed upward. The empty set is allowed for either. By the extension property and ultrahomogeneity of the generic poset, one-point types are exactly the pairs \((L,U)\) where \(L\) is a down-set, \(U\) is an up-set, and every \(\ell\in L\) is strictly below every \(u\in U\). In particular, \(L\cap U=\varnothing\), with the empty-set condition interpreted vacuously. Here \(L\) consists of named points below the new point and \(U\) of those above it. Distinct type realizations are available by finite extension.

There is a neutral type \(z=(\varnothing,\varnothing)\). For each nonempty down-set \(L\), write \(a_L=(L,\varnothing)\); for each nonempty up-set \(U\), write \(b_U=(\varnothing,U)\). All other types are exactly the two-sided or **mixed** \(c_{L,U}=(L,U)\) with \(L,U\ne\varnothing\). Since complementation bijects down-sets with up-sets, there are \(j(A)-1\) types of each pure kind; counting these and the mixed types proves the formula for \(N_A\).

## Proof
**1. Exact feasibility predicate.** For \(p=(L,U)\) and \(q=(L',U')\), the two new points may be incomparable exactly when
\[
\boxed{M_A(p,q)=\mathbf 1_{U\cap L'=\varnothing}\,\mathbf 1_{L\cap U'=\varnothing}.}\tag{1}
\]
Indeed, if an old point is above the first new point and below the second, transitivity forces their comparability; the reverse path gives the second obstruction. Conversely, if both intersections vanish, declare the new points incomparable and retain their prescribed relationships to the base. Every possible two-step transitivity failure must involve one of the two forbidden paths, since each unary extension is already a poset. The result is a finite poset and therefore is realized in \(\mathbb P\). The same reasoning covers diagonal type pairs with two distinct new realizations.

**2. The primitive radical relations.** Let \(e_p\) denote the standard integer basis vector of type \(p\). For every mixed type set
\[
\boxed{r_{L,U}=e_{c_{L,U}}-e_{a_L}-e_{b_U}+e_z.}\tag{2}
\]
For an arbitrary \(q=(L',U')\), formula (1) and the four-term alternating sum yield
\[
\langle r_{L,U},e_q\rangle_{M_A}
=\bigl(\mathbf 1_{U\cap L'=\varnothing}-1\bigr)
 \bigl(\mathbf 1_{L\cap U'=\varnothing}-1\bigr).
\]
This can be nonzero only if \(u\in U\cap L'\) and \(\ell\in L\cap U'\). But the first mixed type forces \(\ell<u\), and the second type forces \(u<\ell\), a contradiction. Hence every \(r_{L,U}\) is orthogonal to **every** basis vector. They are linearly independent, and together with the standard pure-type vectors and \(e_z\) they form a unimodular integer basis: each \(r_{L,U}\) has coefficient \(1\) on its unique mixed coordinate and only pure/neutral lower-order terms.

**3. The nonsingular pure block.** Replace the pure-type basis vectors by
\[
a_L^\ast=e_{a_L}-e_z,\qquad b_U^\ast=e_{b_U}-e_z.
\]
These differences are orthogonal to \(e_z\), and \(\langle e_z,e_z\rangle=1\). Formula (1) yields zero pairings within either pure family, and mixed pairings
\[
\langle a_L^\ast,b_U^\ast\rangle=-Q_{L,U},\qquad
Q_{L,U}=\mathbf 1_{L\cap U\ne\varnothing}.
\]
Thus the full integral Gram form is already congruent to
\[
[1]\oplus \begin{pmatrix}0&-Q\\-Q^{\mathsf T}&0\end{pmatrix}\oplus0_{t(A)},
\]
where \(Q\) is square of order \(j(A)-1\).

**4. Unimodularity of the ideal–filter intersection block.** Every nonempty up-set is uniquely \(A\setminus J\) for a **proper** down-set \(J\). Accordingly
\[
Q_{L,A\setminus J}=1-\mathbf 1_{L\subseteq J},
\]
with rows indexed by nonempty down-sets \(L\) and columns by proper down-sets \(J\). Put the full set \(A\) last among rows and the empty set first among columns. The row for \(L=A\) is all ones and the column for \(J=\varnothing\) is all ones. Subtract the full-set row from every other row, then expand along the empty-set column. The remaining square block, indexed by nonempty proper down-sets on both axes, is the negative of the zeta matrix
\[
Z_{L,J}=\mathbf 1_{L\subseteq J}.
\]
Ordering these down-sets by cardinality gives an upper-triangular integer matrix with every diagonal entry equal to one. Therefore \(\det Q=\pm1\), including the trivial \(j(A)=1\) case by the empty-matrix convention. A unimodular change of the pure bases reduces the off-diagonal \(-Q\) to the identity, proving the displayed hyperbolic congruence.

**5. Integral and field consequences.** The hyperbolic plane has Smith form \(I_2\) and real inertia \((1,1,0)\); the neutral block contributes one positive direction. All mixed vectors form a basis of the radical, not merely a spanning set, because the remaining Gram block is unimodular. Thus its null lattice is primitive; rank does not drop modulo any prime, and the complete assertions follow without extrapolation from finite computations.

## Verification
The included standalone Python 3 script `verify.py` independently enumerates all finite posets encoded by upward arcs in a fixed natural linear extension through four named points, plus fourteen five-point patterns. For each case, it creates the one-point types from downward/upward closure; checks every matrix entry against a direct transitivity test on the finite extension with two incomparable new points; and checks every entry of the transformed Gram form against the claimed zero, hyperbolic-incidence, and radical blocks. It also verifies the triangular zeta block used for unimodularity. The recorded output is `verification_output.txt`, ending in `FINITE_EXTENSION_AND_CONGRUENCE_OK`, with 90 input patterns and 45,913 matrix entries tested. Finite checks corroborate, but the all-size proof is the explicit argument above.

Run `python verify.py` in a directory containing that script, using the Python standard library only.

## Relationship to prior work
Pach, Pinsker, Pluhár, Pongrácz and Szabó characterize the random partial order and its reducts, and explicitly use the universal one-point extension property. Dolinka and Mašulović use down-set/up-set information for finite-poset one-point extensions; that unary parameterization is foundational background and not the contribution here. Classical incidence-algebra zeta matrices are integral unitriangular; the zeta step in Part 4 is accordingly not claimed to be new.

Previously reported work gives exact unary-type counting and fixed-base ordered-pair counts (including antichain and complete two-level parameter posets), which determine numerical totals rather than this entire integral feasibility form. A chain-only hyperbolic congruence is subsumed: for an \(n\)-element chain, \(j(A)=n+1\) and \(t(A)=\binom n2\). The new point is an explicit radical basis and unimodular decomposition for **every** finite poset, with no restriction on its comparability graph or width; chain formulas alone do not logically imply this.

## Limitations
The matrix asks only whether incomparable **distinct** realizations of a pair of nonalgebraic one-point types are possible; it does not count the complete two-point types, enumerate comparable types, or include algebraic types. The theorem does not give a polynomial-time method to compute \(j(A)\); counting down-sets is generally hard. This is an explicit integral congruence, not a formula for ordinary eigenvalue magnitudes. Although the proof establishes the theorem for all finite bases, historical priority of the combined logical-matrix statement remains subject to further specialist review, including literature under incidence- and Boolean-matrix terminology.

## References
1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892, first public 2010-09-15, especially §3.1 and Lemma 3.3. https://arxiv.org/abs/1009.2892
2. P. P. Pach, M. Pinsker, G. Pluhár, A. Pongrácz and C. Szabó, *Reducts of the random partial order*, arXiv:1111.7109, first public 2011-11-30, especially §3 (extension property). https://arxiv.org/abs/1111.7109
3. Finite-poset incidence-algebra zeta and Möbius inversion, standard background; e.g. the unitriangular zeta-matrix discussion in the open article *Dual braids and free cumulants*, §4. https://www.mat.univie.ac.at/~slc/s/s72dehorn.pdf
