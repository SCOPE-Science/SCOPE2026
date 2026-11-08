# Transitive Fischer–Servi relations on rooted stars: a structural decomposition and exact census

## Finding
For every integer \(m\ge1\), let \(P_m=\{r\}\cup L\) with \(L=\{1,\ldots,m\}\), ordered by \(r\le i\) for every \(i\in L\) and otherwise only by equality. The number \(F_m\) of **labelled** transitive relations \(R\subseteq P_m\times P_m\) satisfying both Fischer–Servi forward and backward confluence is
\[
F_m=T_m+V_m+1+2\sum_{c=0}^{m-1}\binom mc\bigl((2^{m-c}-1)T_c+U_c\bigr).
\]
Here \(T_c\) counts arbitrary transitive relations on a fixed labelled \(c\)-set; \(U_c\) counts those having no empty outgoing row; \(V_c\) counts those with neither an empty outgoing row nor an empty incoming column; and \(T_0=U_0=V_0=1\). Incoming and outgoing conditions are equivalent in number by transposition. The resulting exact values for \(m=1,2,3,4,5\) are, respectively, \(8,38,379,7182,238810\).

The theorem also provides a complete structural normal form of every such relation; the formula is not merely a finite experimental fit.

## Assumptions and scope
A relation is transitive if for all \(x,y,z\in P_m\), \(xRy\) and \(yRz\) imply \(xRz\). It need not be reflexive, serial, symmetric, antisymmetric, or total. The two confluences mean precisely:

* **Forward (FC):** for all \(x\le y\) and \(xRz\), there is \(z'\ge z\) with \(yRz'\).
* **Backward (BC):** for all \(xRz\) and \(z\le z'\), there is \(y\ge x\) with \(yRz'\).

The leaf labels are fixed, so relations differing by a permutation of leaves are counted separately. For \(c=0\), the empty relation on the empty carrier is counted once and has no empty rows or columns (vacuously). The theorem assumes \(m\ge1\); the isolated one-world case \(m=0\) has two transitive relations and is not covered by this formula.

## Proof
Write \(a=1\) when \(rRr\), and \(a=0\) otherwise. Set \(A=\{i\in L:rRi\}\) and \(E=\{i\in L:iRr\}\). For any leaf \(i\), write \(R(i)\) for its successor set.

**First reductions.** The only proper order comparisons are \(r\le i\). Thus (FC) is equivalent to the conjunction of: \(A\subseteq R(i)\) for every leaf \(i\), and if \(a=1\), every leaf has a nonempty row. Likewise, (BC) says: if \(i\in E\), then \(L\subseteq R(i)\); and, if \(a=1\), every leaf belongs to at least one row (possibly the root row). No further nontrivial instances exist. If \(A\cap E\ne\varnothing\), transitivity gives \(a=1\). In that case each \(i\in A\cap E\) has \(R(i)=P_m\) by (BC) and \(iRr\). Since \(rRi\) and \(iRj\) for every \(j\in L\), transitivity forces \(A=L\). Moreover, every leaf \(j\) has \(jRi\) by (FC), so \(jRr\) by transitivity; hence \(E=L\). Thus either \(A\cap E=\varnothing\), or \(a=1\) and \(A=E=L\).

**Normal form when \(A\cap E=\varnothing\).** Put \(C=L\setminus(A\cup E)\). Confluence forces every leaf row to contain \(A\). Transitivity then forces, for \(i\in A\), exactly \(R(i)=A\): indeed \(rRi\) implies \(R(i)\subseteq R(r)=A\cup(\{r\}\text{ if }a=1)\), and \(i\notin E\). For \(i\in E\), (BC) gives \(R(i)=P_m\). For \(i\in C\), transitivity forbids edges from \(i\) to \(E\), because every \(e\in E\) has \(eRr\), which would imply \(iRr\). It also forbids an edge from \(i\) to \(r\) by definition of \(C\). Therefore \(R(i)=A\cup S(i)\), where \(S\) is a binary relation on \(C\). Transitivity of \(R\) reduces exactly to transitivity of \(S\). Conversely, every such construction satisfies all transitivity requirements; the only additional conditions are the nonempty-row and leaf-coverage requirements when \(a=1\).

If \(a=0\), the sets \(A,E,C\) may be any ordered three-part partition of \(L\), and \(S\) any transitive relation on \(C\). This contributes
\[
H_m=\sum_{c=0}^m\binom mc\,2^{m-c}T_c.
\]
If \(a=1\) and \(A=L\), there are exactly two possibilities: \(E=\varnothing\), with every leaf row equal to \(L\), or the exceptional \(A=E=L\), with every row equal to \(P_m\). These are distinct from each other and from every \(a=0\) relation, and contribute two relations.

It remains to consider \(a=1\), \(A\cap E=\varnothing\), and \(A\ne L\). If \(A=E=\varnothing\), both (FC) and (BC) require \(S\) to have no empty row and no empty column, contributing \(V_m\). If \(A\ne\varnothing,E=\varnothing\), the nonempty-row condition is automatic, but the leaf coverage condition says \(S\) has no empty column, contributing \(U_c\) when \(|C|=c\) (transpose of the row version); here \(1\le c\le m-1\). If \(A=\varnothing,E\ne\varnothing\), coverage is automatic but every row on \(C\) must be nonempty, also contributing \(U_c\), now for \(0\le c\le m-1\). Finally, if \(A\ne\varnothing,E\ne\varnothing\), both conditions are automatic and \(S\) is arbitrary transitive, contributing \((2^{m-c}-2)T_c\) for each chosen \(c\)-element set \(C\), where \(0\le c\le m-2\).

The nonexceptional \(a=1\) count is consequently
\[
V_m+\sum_{c=1}^{m-1}\binom mc U_c +\sum_{c=0}^{m-1}\binom mc U_c +\sum_{c=0}^{m-2}\binom mc(2^{m-c}-2)T_c.
\]
Adding the \(a=0\) count \(H_m\) and the two \(A=L\) cases, then grouping terms by \(c\), including the \(c=m\) term \(T_m\) from \(H_m\), yields the asserted boxed formula. In particular the lone \(c=0\) contribution in the nonempty-\(E\), empty-\(A\) case, together with the two \(A=L\) cases, accounts exactly for the constant \(1+2U_0=3\) in the final formula. Every relation is recovered uniquely from \(a,A,E,S\), apart from the explicitly separated all-world relation. Hence the sum has neither overlap nor omissions. This proves the statement for every \(m\ge1\).

## Verification
Independent exhaustive enumeration directly tested every one of the \(2^{(m+1)^2}\) labelled relations for \(0\le m\le4\), using Boolean transitivity and the two quantified confluence conditions, producing \(2,8,38,379,7182\). An independent normal-form constructor agreed with the exact set of accepted matrices for \(0\le m\le3\), not just their cardinalities. Complete enumeration of all \(2^{25}\) relations on five points gives
\[
\begin{array}{c|rrrrrr}
 c&0&1&2&3&4&5\\\hline
 T_c&1&2&13&171&3994&154303\\
 U_c&1&1&6&68&1387&47262\\
 V_c&1&1&4&35&583&16762
\end{array}
\]
and substitution into the formula gives \(238810\) when \(m=5\). Reproduce using `c++ -std=c++17 -O3 checker.cpp -o checker && ./checker`, `python3 checker.py`, and `c++ -std=c++17 -O3 count_transitive5.cpp -o count5 && ./count5`.

These computations are finite corroboration. The unrestricted theorem in \(m\) follows from the structural proof, not from extrapolation.

## Relationship to prior work
Balbiani–Gencer, *Four intuitionistic modal connectives* (arXiv:2606.07348, first public June 5, 2026), Section 3.2 distinguishes the forward, backward, downward and upward confluence conditions and studies their semantics and correspondence, but does not enumerate transitive relations on finite rooted stars. Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic* (arXiv:2609.27078, September 22, 2026), proves a finite model property for a related intuitionistic modal system; its expansivity terminology is not to be conflated automatically with the present (FC)+(BC) definition, and the paper does not count these stars. Published finite-chain classifications have different underlying orders and/or relations.

The (FC)+(BC) class is not the same as the (FC)+(downward) class: on a two-leaf star, the one-edge relation \(1R2\) with isolated root is transitive and (FC)+(BC), but fails downward confluence. Conversely, \(R=\{(r,r),(1,1),(2,1)\}\) is transitive and (FC)+(downward), but fails (BC) because no world relates to leaf \(2\) despite \(rRr\). Consequently a census for the latter class does not subsume this one. Nor does an unlabelled orbit census imply the stated labelled count without full stabilizer data.

## Limitations
The formula uses the general transitive-relation counts \(T_c,U_c,V_c\); it is an exact finite sum and normal form, not a claimed elementary closed form for those auxiliary sequences. The count is for **labelled** non-reflexive-optional, non-serial-optional relations on rooted stars only; neither larger posets nor unlabelled isomorphism counts follow automatically. Prior historical work not available or not indexed may contain an equivalent enumeration. Independent mathematical or priority audits have not been conducted.

## References
1. P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348, posted 2026-06-05, especially Sections 1 and 3.2. https://arxiv.org/abs/2606.07348
2. D. Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic*, arXiv:2609.27078, posted 2026-09-22, especially Sections 1–2 and 15. https://arxiv.org/abs/2609.27078
3. Classical labelled transitive-relation enumeration (auxiliary enumeration; independent derivation here does not depend on a pre-existing table).
