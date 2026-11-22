# Restrained domination of circular ladders: complete polynomial and exponential filtering

## Finding
Let \(G_n=C_n\square K_2\) be the simple **labelled circular ladder** with \(n\ge4\) rungs and two cyclic rows. A *restrained dominating set* \(S\subseteq V(G_n)\) is a set such that every vertex outside \(S\) has both a neighbour in \(S\) and a neighbour outside \(S\). Write
\[
R_n(z)=\sum_{S\text{ restrained dominating}}z^{|S|}.
\]
For indeterminates \(x,z\), define the following explicit polynomials:
\[
\begin{aligned}
A(x,z)={}&1-xz+x^2z+x^2z^2-x^3z^2,\\
B(x,z)={}&1-xz-xz^2-x^2z-2x^2z^2+x^2z^3\\
 &{}-2x^3z^2-2x^3z^3-x^3z^4+x^5z^3+x^6z^4.
\end{aligned}
\]
The **entire restrained-domination polynomial at every length** is
\[
\boxed{R_n(z)=[x^n]\left(-x\frac{\partial}{\partial x}\log(A(x,z)B(x,z))\right).}
\]
Its least degree and number of minimum sets are, for every \(n\ge4\),
\[
\boxed{\gamma_r(G_n)=\left\lceil\frac n2\right\rceil+\mathbf1_{n\equiv2\pmod4}},
\qquad
\boxed{[z^{\gamma_r(G_n)}]R_n(z)=
\begin{cases}
4,&n\equiv0\pmod4,\\
2n,&n\text{ odd},\\
n^2+3\mathbf1_{n=6},&n\equiv2\pmod4.
\end{cases}}
\]
The boundary coefficients are \([z^{2n}]R_n=1\), \([z^{2n-1}]R_n=0\), and \([z^{2n-2}]R_n=3n\). Thus adding a vertex can destroy the property.

If \(D_n(z)\) is the **ordinary domination** polynomial of the same prism, the minimum ordinary dominating sets have the same minimum size; precisely \(2n\) of them fail restrained domination when \(n\equiv2\pmod4\) and \(n\ge6\), and none fail otherwise. This distinguishes two natural guarding conditions that have the same optimum cardinality.

There is also an all-cardinality asymptotic separation. Define \(r\) and \(d\) as the unique dominant positive roots (the roots of smallest complex modulus) of
\[
\begin{aligned}
p_r(x)&=x^6+x^5-5x^3-2x^2-2x+1,\\
p_d(x)&=x^5+x^4-2x^3-2x^2-3x+1.
\end{aligned}
\]
Numerically, \(r\approx0.319111235263402\) and \(d\approx0.272620702494296\). Then
\[
\boxed{\frac{R_n(1)}{D_n(1)}\sim\left(\frac dr\right)^n
\approx(0.854312453992000)^n.}
\]
In particular, restrained dominating sets constitute an exponentially vanishing fraction of all ordinary dominating sets, even though the minimum sizes agree.

## Assumptions and scope
The vertices are \((i,h)\) with \(i\in\mathbb Z/n\mathbb Z\) and \(h\in\{0,1\}\). Every vertex has three distinct neighbours: its two horizontal neighbours and its vertical rung partner. The rows, rungs and vertices are labelled; sets are **not** identified under graph automorphisms. The full vertex set is included, because the condition on outside vertices is vacuous. The result is for ordinary, not total, restrained domination.

## Proof
**1. Exact local rule.** Represent rung \(i\) by the two-bit selection symbol \(s_i\in\{0,1,2,3\}\), with bit \(h\) equal to one precisely when \((i,h)\) is selected. For three successive symbols \(a,b,c\), define
\[
q_h(a,b,c)=a_h+c_h+b_{1-h},\qquad h\in\{0,1\},
\]
where the subscript denotes the relevant bit. A middle symbol \(b\) is admissible precisely when
\[
 b_h=0\ \Longrightarrow\ 1\le q_h(a,b,c)\le2\quad(h=0,1).
\]
This condition is exactly the definition of restrained domination: an unselected vertex has three distinct neighbours, so at least one and at most two must be selected. There are no requirements on a selected vertex.

**2. Transfer bijection and finite determinant identity.** Index a \(16\times16\) matrix \(T(z)\) by ordered pairs \((a,b)\) of two-bit symbols. Set
\[
T(z)_{(a,b),(b',c)}=
\begin{cases}
z^{\operatorname{popcount}(b)},&b=b'\text{ and }(a,b,c)\text{ is admissible},\\
0,&\text{otherwise}.
\end{cases}
\]
A closed walk of length \(n\) in these ordered-pair states is bijective with one labelled cyclic selection word \((s_0,\ldots,s_{n-1})\), and the product of transition weights is exactly \(z^{|S|}\). Consequently \(R_n(z)=\operatorname{tr}(T(z)^n)\). Explicit finite polynomial arithmetic on the fully specified matrix gives
\[
\boxed{\det(I-xT(z))=A(x,z)B(x,z).}
\]
The included standalone verifier constructs the matrix from the local criterion and checks this identity symbolically over the polynomial ring \(\mathbb Z[x,z]\). The formal trace–determinant identity
\[
-x\partial_x\log\det(I-xT)=\sum_{m\ge1}\operatorname{tr}(T^m)x^m
\]
now proves the all-cardinality formula. The formal terms for lengths below three have no interpretation as simple prisms.

**3. Minimal weight and exact optimum multiplicities.** Introduce \(z=t^2\) and \(x=u/t\); then the exponent of \(t\) in a set's contribution is \(2|S|-n\). Direct substitution in the displayed determinant gives
\[
\begin{aligned}
A(u/t,t^2)B(u/t,t^2)={}&(1-u^4)\\
&{}+t\,u(u^2-2)(u^2+1)^2+2t^2u^6+O(t^3).
\end{aligned}
\]
Crucially, the *entire* substituted determinant has no negative powers of \(t\); its constant term in \(u\) is one. Thus its formal logarithmic derivative has no negative powers either. Set
\[
H(u,t)=-u\partial_u\log(A(u/t,t^2)B(u/t,t^2))=
H_0(u)+tH_1(u)+t^2H_2(u)+O(t^3).
\]
Elementary expansion of \(-\log\) gives the following exact rational identities:
\[
H_0(u)=\frac{4u^4}{1-u^4},\qquad
H_1(u)=\frac{u(3u^6-6u^4+5u^2+2)}{(1-u^2)^2},
\]
\[
H_2(u)=\sum_{k\ge1}4k(4k+2)u^{4k}
+\sum_{k\ge0}(4k+2)^2u^{4k+2}+3u^6.
\]
For every even multiple of four, the first nonzero coefficient is in \(H_0\) and equals four. For odd lengths at least five the first one is in \(H_1\) and equals twice the length; for lengths congruent to two modulo four, the first is in \(H_2\), equalling the square of the length, with the single correction three at length six. Since the exponent is \(2|S|-n\), these three cases prove both minimum formulas at every \(n\ge4\). The quoted rational expansion identities are also checked symbolically in the included verifier.

**4. Comparison with unrestricted domination.** Omit the upper bound \(q_h\le2\) in the local condition to get the ordinary-domination transfer \(U(z)\). Its analogous finite determinant is
\[
\det(I-xU(z))=(1+x^2z)\big(1-2xz-xz^2-x^2z-x^2z^2-x^3z^2-x^3z^3+x^4z^3+x^5z^3\big).
\]
The same \((u,t)\) substitution has identical coefficients at orders zero and one in \(t\); at order two the difference of the logarithmic-derivative coefficients is exactly
\[
\frac{2u^2(1+4u^4-u^8)}{(1-u^4)^2}
=\sum_{k\ge0}2(4k+2)u^{4k+2}.
\]
This proves that the two domination parameters agree for all lengths, and that among the ordinary minima exactly \(2n\) fail restraint in the residue class two modulo four, with none failing in the other three classes. The full-vertex and near-full-vertex coefficients follow directly from the fact that the unselected subgraph must have no isolated vertices: with two omitted vertices exactly the \(3n\) graph edges qualify.

**5. Exponential rarity.** Both unweighted directed transfer graphs \(T(1)\) and \(U(1)\) on the sixteen ordered-pair symbols are strongly connected and contain a self-loop, as checked by complete sixteen-state reachability (also implemented in the verifier). They are therefore primitive nonnegative matrices. Perron–Frobenius gives a unique positive strictly dominant eigenvalue and
\[
R_n(1)\sim\rho_r^n,\qquad D_n(1)\sim\rho_d^n.
\]
Specializing the two determinant identities at \(z=1\), the Perron eigenvalues are the reciprocals of the smallest-modulus positive roots of \(p_r,p_d\), respectively: the remaining factor for restrained domination is \(1-x+2x^2-x^3\), while that for ordinary domination is \(1+x^2\). Primitivity identifies the dominant roots without guessing from numerical root tables. Moreover \(T(1)\) is a proper entrywise submatrix of the irreducible \(U(1)\), so \(\rho_r<\rho_d\). The stated rate and asymptotic ratio follow.

## Verification
The included `verify_prism_restrained.py` uses Python 3 and SymPy. It independently constructs the two weighted transfer matrices from the local graph condition; checks **both exact symbolic determinants**; proves the displayed all-order low-weight coefficient identities by exact rational simplification; checks strong connectivity and aperiodicity of both state graphs; and compares every coefficient with **direct graph-subset enumeration** for rung lengths three through nine. It additionally checks exact minimum and boundary counts through length thirty. Its completed output is `DETERMINANT_IDENTITIES_OK`, `ALL_ORDER_LOW_WEIGHT_IDENTITIES_OK`, `DIRECT_SUBSET_VERSUS_TRANSFER_OK`, `MINIMUM_AND_BOUNDARY_COEFFICIENTS_OK`, `PERRON_ROOTS_NUMERICALLY_CHECKED`, and `VERIFY_OK`.

The direct finite checks alone are not proofs for arbitrary lengths. The infinite conclusions use the proved local-rule bijection, exact polynomial determinant identities, formal-power-series calculations, and Perron–Frobenius theory. The finite algebraic identities have explicit small matrix input and are independently reproducible.

## Relationship to prior work
Hemalatha, Chandrakala, Sooryanarayana and Vishu Kumar (2023), *Restrained and Total Restrained Domination of Ladder Graphs*, explicitly include circular ladders and report scalar domination and restrained-domination values. Their Theorem 5.2 does not give an all-cardinality polynomial. Its displayed scalar formula \(2\lceil n/4\rceil\) differs for odd lengths from the exact minimum proved here (for example, the explicit three-set \(\{(0,0),(1,0),(3,1)\}\) is restrained dominating on the five-rung circular ladder); hence it cannot serve as a proof of this result. The discrepancy is assessed from the actual theorem statement, not merely a search snippet.

Velmurugan and Kala (2023) enumerate restrained dominating sets of **single cycles**, without the rung edges. Brešar and Henning (2024) prove the sharp universal cubic-graph upper bound \(2|V|/5\), not an exact prism cardinality census. Allagan and collaborators (2026) enumerate **minimum ordinary** dominating sets of these prisms. Their arithmetic trichotomy is credited: the present result strengthens it only under the distinct restrained condition and additionally gives all cardinalities and the exponential all-set comparison. Distinct published analyses of one-limited domination and paired domination in cycle prisms also impose different local requirements and do not imply the restrained criterion. An unindexed equivalent formula could still exist.

## Limitations
Only simple labelled two-layer circular ladders with at least four rungs are included. The exact cardinality polynomial is not an algorithm for arbitrary cubic graphs. The asymptotic comparison concerns counts of vertex subsets, not a random sequential placement process or unlabelled orbit counts. The conclusions are self-reviewed but have not undergone independent mathematical audit; historical publication priority is provisional.

## References
- N. C. Hemalatha, S. B. Chandrakala, B. Sooryanarayana, M. Vishu Kumar, *Restrained and Total Restrained Domination of Ladder Graphs*, Communications in Mathematics and Applications 14 (2023), 1311–1323, Theorem 5.2, https://doi.org/10.26713/cma.v14i4.2569.
- S. Velmurugan and R. Kala, *Restrained Domination Polynomial of Cycles*, Palestine Journal of Mathematics 12, Special Issue II (2023), 58–64, https://pjm.ppu.edu/sites/default/files/papers/PJM_Special_Issue_II_58_to_64.pdf.
- B. Brešar and M. A. Henning, *Best possible upper bounds on the restrained domination number of cubic graphs*, Journal of Graph Theory 106 (2024), 763–815, https://doi.org/10.1002/jgt.23095.
- J. Allagan et al., *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488 (first posted 7 January 2026), https://arxiv.org/abs/2601.03488.
