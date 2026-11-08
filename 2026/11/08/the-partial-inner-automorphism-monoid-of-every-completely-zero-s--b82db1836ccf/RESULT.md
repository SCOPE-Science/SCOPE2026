# The partial inner automorphism monoid of every completely zero-simple Rees semigroup

## Finding
Let \(G\) be a group, let \(I,\Lambda\) be nonempty sets, and let \(P=(p_{\lambda i})\) be a \(\Lambda\)-by-\(I\) matrix over \(G\cup\{0\}\) with no zero row or column. Consider the completely zero-simple Rees semigroup \(S=M^0(G;I,\Lambda;P)\), with multiplication
\[
(i,x,\lambda)(j,y,\mu)=
\begin{cases}
(i,xp_{\lambda j}y,\mu),&p_{\lambda j}\ne0,\\
0,&p_{\lambda j}=0.
\end{cases}
\]
Define
\[
E=\{(i,\lambda)\in I\times\Lambda:p_{\lambda i}\ne0\},
\qquad m=|E|,\qquad H=G/Z(G).
\]
Let \(B_E(H)=(E\times H\times E)\sqcup\{0_B\}\) be the Brandt semigroup, with its usual matrix-unit product and zero. Then
\[
\operatorname{Inn}(S)\cong
\begin{cases}
B_E(H),&m=1,\\
B_E(H)^1,&m>1,
\end{cases}
\]
where \(B_E(H)^1\) has a **new** identity. In particular, the inverse monoid is independent of the incidence geometry of nonzero positions and independent of all nonzero sandwich values. Two such inverse monoids are isomorphic precisely when their numbers of nonzero positions agree and their groups \(G/Z(G)\) are isomorphic. For finite \(m\) and \(H\), the cardinality is \(m^2|H|+1\) for \(m=1\), and \(m^2|H|+2\) otherwise.

This supplies an explicit answer to Problem 7.5 of Araújo et al. (2026), which asks for the partial inner automorphism monoids of Rees zero-matrix semigroups.

## Assumptions and scope
A regular Rees zero-matrix semigroup has underlying set \(S=\{0\}\sqcup(I\times G\times\Lambda)\), with zero absorbing. The matrix has no zero row or column; \(I\), \(\Lambda\), and \(G\) may be infinite. For \(g,h\in S^1\), define
\[
D_{g,h}=\{a\in S:(gh)a=a=a(gh)\},
\qquad\phi_{g,h}(a)=hag.
\]
By the definition in [1], \(\operatorname{Inn}(S)\) is the inverse monoid of partial maps generated under composition by all \(\phi_{g,h}\). Every domain contains zero. The zero \(0_B\) in the Brandt description is the partial map on \(\{0\}\) that fixes zero, **not** the empty partial map.

For each \(e=(i,\lambda)\in E\), write
\[
e_{i,\lambda}=(i,p_{\lambda i}^{-1},\lambda),
\quad U_e=\{0\}\cup\{(i,x,\lambda):x\in G\},
\quad\rho_e((i,x,\lambda))=xp_{\lambda i}.
\]
The nonzero part of \(U_e\) is the maximal subgroup with identity \(e_{i,\lambda}\), and \(\rho_e\) identifies it with \(G\).

## Proof
**1. Every nontrivial domain is a maximal subgroup plus zero.** The zero element always belongs to \(D_{g,h}\). If \(gh=0\), then \(D_{g,h}=\{0\}\). If \(gh=(i,c,\lambda)\) is nonzero and \(D_{g,h}\) contains a nonzero element \(a\), the equations \((gh)a=a=a(gh)\) force \(a=(i,z,\lambda)\) and \(p_{\lambda i}\ne0\). Then the first equality yields \(cp_{\lambda i}z=z\), hence \(c=p_{\lambda i}^{-1}\). Thus \(gh=e_{i,\lambda}\) and precisely \(D_{g,h}=U_{(i,\lambda)}\). If \(gh\) is nonzero but not of this form, the domain is again just \(\{0\}\).

**2. All maps between these domains and their labels.** Suppose \(g=(i,x,\mu)\), \(h=(j,y,\lambda)\) and \(gh=e_{i,\lambda}\). Then \(p_{\mu j},p_{\lambda i}\ne0\) and
\[
xp_{\mu j}y=p_{\lambda i}^{-1},
\qquad hg=e_{j,\mu}.
\]
For \(a\in U_{(i,\lambda)}\setminus\{0\}\), a multiplication using the coordinates above gives
\[
\rho_{(j,\mu)}(hag)=t\rho_{(i,\lambda)}(a)t^{-1},
\qquad t=yp_{\lambda i}.
\]
Thus the map from \(U_e\) to \(U_f\) is conjugation by an element of \(G\), with zero fixed. Conjugations are identical exactly when their parameters differ by a central element, so these labels form \(H=G/Z(G)\). Conversely, for arbitrary \(e=(i,\lambda),f=(j,\mu)\in E\) and arbitrary \(t\in G\), choose
\[
y=tp_{\lambda i}^{-1},
\qquad x=p_{\lambda i}^{-1}y^{-1}p_{\mu j}^{-1}.
\]
Then \(g=(i,x,\mu)\), \(h=(j,y,\lambda)\) satisfy \(gh=e_{i,\lambda}\), and their partial map is exactly the prescribed inner conjugation from \(U_e\) to \(U_f\). If \(g\) or \(h\) equals the adjoined identity, the only maps beyond these cases are the full identity and maps already present; no new intermediate domains arise.

**3. Composition yields a Brandt semigroup.** Distinct \(U_e\) intersect in precisely \(\{0\}\). Therefore composing a map from \(U_e\) to \(U_f\) with one from \(U_{e'}\) to \(U_{f'}\) gives the bottom map on \(\{0\}\) if \(f\ne e'\). If \(f=e'\), their conjugation parameters multiply. To match the conventional Brandt product \((e,a,f)(f,b,d)=(e,ab,d)\) with partial functions acting successively on the right, label conjugation by \(t\) using \(t^{-1}Z(G)\); then successive conjugations have the product of labels in the stated order. This identifies the nonidentity partial maps, including the bottom map, with \(B_E(H)\). The full identity is \(\phi_{1,1}\). If \(m=1\), regularity forces \(|I|=|\Lambda|=1\), so the full identity is already the unique local identity in \(B_E(H)\). If \(m>1\), it is a distinct externally adjoined identity. Hence the displayed isomorphism holds even for infinite \(I,\Lambda,G\).

**4. Exact isomorphism information.** The nonzero primitive idempotents of the Brandt ideal are indexed by \(E\), and each associated maximal subgroup is \(H\). These properties can be recovered intrinsically from the inverse monoid, so isomorphism requires equal \(m\) and isomorphic \(H\); conversely those data give the same Brandt construction. Counting the Brandt triples and their bottom (and, when needed, external identity) gives the cardinalities.

For example, with \(G=C_2\), the one-row matrix \(P_1=[1\;1]\) on two columns and the two-by-two diagonal sandwich matrix \(P_2=\begin{psmallmatrix}1&0\\0&1\end{psmallmatrix}\) define nonisomorphic semigroups of orders five and nine. Both have \(m=2\) and \(H=1\); hence both partial-inner monoids have six elements and are isomorphic to \(B_2(1)^1\).

## Verification
The standalone script `check_rees.py` constructs finite groups (cyclic groups of orders one, two and three and the symmetric group \(S_3\)), all elements of the corresponding Rees semigroups, and the partial maps \(\phi_{g,h}\) directly from their definitions. Independently it constructs the predicted Brandt maps from normalized maximal-subgroup coordinates, checks equality of both sets of maps, verifies closure under every ordered composition, and checks the cardinalities. Eleven tests exercise one, two, three and four nonzero matrix entries; rectangular, Brandt, triangular and full sandwich patterns; and nonidentity nonzero sandwich values. The recorded execution ends with `VERIFY_OK cases=11`. These finite computations are not used to prove the infinite theorem.

Reproduce with `python3 check_rees.py`, requiring only the Python standard library. `check_output.txt` records the run.

## Relationship to prior work
Araújo et al. [1] define partial inner automorphisms in §3, obtain the completely simple (zero-free) Rees matrix case in Theorem 4.2, and expressly pose the zero-matrix problem as Problem 7.5. The present theorem treats the zero structure, including disjoint local subgroup domains, their common fixed zero and the resulting Brandt multiplication. The earlier conjugacy study [2], which originally contained parts of the 2026 paper, supplies further background on natural conjugacy and Rees-type semigroups. A description of elementwise conjugacy is not the same as the inverse monoid of partial maps and its composition table. The inverse Brandt specialization already follows from the central-congruence theorem for inverse semigroups (Remark 3.11 of [1]), and the one-maximal-subgroup case reduces to ordinary group inner automorphisms; these special cases are not separately claimed as new. The center quotient \(G/Z(G)\) is standard in group inner automorphisms; its use in this zero-simple classification, and the complete loss of the sandwich support geometry, are the new statements asserted here.

## Limitations
The theorem concerns completely zero-simple Rees semigroups whose sandwich matrix is regular. It does not classify arbitrary nonregular zero-matrix semigroups or finite presentations of the resulting inverse monoid. The first public source for the **specific zero-Rees question** is [1], submitted April 28, 2026, whereas the underlying natural-conjugacy programme has a publicly accessible January 2023 antecedent [2]. The result has not undergone independent mathematical audit, and historical priority is qualified by the possibility of an older equivalent characterization of the inverse monoid.

## References
[1] J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041v1, submitted 2026-04-28, https://arxiv.org/html/2605.00041v1 (Definitions 3.8; Theorem 4.2; Problem 7.5).

[2] J. Araújo et al., *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252, first posted 2023-01-11, https://arxiv.org/abs/2301.04252 (natural-conjugacy and partial-inner background, earlier versions).
