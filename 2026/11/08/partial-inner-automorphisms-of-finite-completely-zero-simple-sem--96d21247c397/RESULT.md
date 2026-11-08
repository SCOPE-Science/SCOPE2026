# Partial inner automorphisms of finite completely zero-simple semigroups

## Finding
Let \(G\) be a finite group, \(I\) and \(\Lambda\) nonempty finite sets, and \(P=(p_{\lambda i})\) a regular \(\Lambda\times I\) matrix over \(G\cup\{0\}\), meaning that each row and column has a nonzero entry. Put
\[
S=M^0(G;I,\Lambda;P),\qquad m=|\{(\lambda,i):p_{\lambda i}\ne0\}|,\qquad H=G/Z(G).
\]
Define \(\operatorname{Inn}(S)\) using the partial automorphisms \(\varphi_{u,v}:D_{u,v}\to D_{v,u}\) associated with \(u,v\in S^1\), where
\[
D_{u,v}=\{x\in S:(uv)x=x=x(uv)\},\qquad \varphi_{u,v}(x)=vxu.
\]
Under composition, the generated inverse monoid admits the complete classification
\[
\boxed{\operatorname{Inn}(S)\cong\begin{cases}H^0,&m=1,\\B_m(H)^1,&m\ge2.\end{cases}}
\]
Here \(H^0\) is the group \(H\) with an absorbing zero, while \(B_m(H)^1\) is the Brandt semigroup with matrix index set of size \(m\) and an **external identity** adjoined. In particular,
\[
|\operatorname{Inn}(S)|=\begin{cases}|H|+1,&m=1,\\m^2|H|+2,&m\ge2.\end{cases}
\]
For any two such semigroups, their partial inner automorphism monoids are isomorphic **if and only if** their numbers of nonzero sandwich entries coincide and their quotients by the centers of their structure groups are isomorphic.

## Assumptions and scope
Multiplication is
\[
(i,a,\lambda)(j,b,\mu)=\begin{cases}(i,a p_{\lambda j} b,\mu),&p_{\lambda j}\ne0,\\0,&p_{\lambda j}=0,\end{cases}
\]
with \(0\) absorbing. The group identity of \(G\) is \(1_G\), and \(0\) denotes the additional absorbing element, not an element of \(G\). The index sets and \(G\) are finite and nonempty, and regularity means no all-zero row or column. The nonzero \(\mathcal H\)-class at coordinates \((i,\mu)\) is a subgroup precisely when \(p_{\mu i}\ne0\). All \(\varphi_{u,v}\) fix \(0\) and are defined there. The identity of \(S^1\) is adjoined only when \(S\) is not already a monoid.

## Proof
**Step 1: classify the domains.** Fix nonzero \(u=(i,a,\lambda)\) and \(v=(j,b,\mu)\). The element \(0\) belongs to \(D_{u,v}\). Suppose a nonzero \(x=(k,c,\nu)\) lies there. Since \((uv)x=x=x(uv)\), the outer coordinates force \(k=i\) and \(\nu=\mu\). Nonvanishing of these two products forces \(p_{\lambda j}\ne0\) and \(p_{\mu i}\ne0\). The group equation then forces
\[
b=(p_{\mu i}a p_{\lambda j})^{-1}.
\]
Conversely these three conditions make \(uv\) the identity of the maximal subgroup \(\mathcal H_{i\mu}\). Thus
\[
D_{u,v}=\{0\}\cup\mathcal H_{i\mu}
\]
exactly in this case, and otherwise \(D_{u,v}=\{0\}\). Each \(\mathcal H_{i\mu}=\{(i,c,\mu):c\in G\}\) in this display is a **group** \(\mathcal H\)-class, not an arbitrary nonregular class. Interchanging \(u,v\) gives \(D_{v,u}=\{0\}\cup\mathcal H_{j\lambda}\).

**Step 2: normalize each group class.** For \(p_{\mu i}\ne0\), identify \(\mathcal H_{i\mu}\) with \(G\) by
\[
(i,c,\mu)\longmapsto c p_{\mu i}.
\]
With \(w=a p_{\lambda j}\), the partial automorphism in Step 1 sends the source normalized group coordinate \(x\) to the target normalized coordinate
\[
 x\longmapsto w^{-1}xw.
\]
Indeed, its target is \((j,b p_{\mu i}c p_{\mu i}a,\lambda)\); multiplying this element's middle entry on the right by \(p_{\lambda j}\), and substituting the expression for \(b\), gives \(w^{-1}(c p_{\mu i})w\). Conversely, for **any** two nonzero sandwich positions \((\mu,i)\) and \((\lambda,j)\) and **any** \(w\in G\), the choices
\[
 a=w p_{\lambda j}^{-1},\qquad b=(p_{\mu i} a p_{\lambda j})^{-1}
\]
realize exactly this map. The conjugation maps \(x\mapsto w^{-1}xw\) form a group isomorphic to \(G/Z(G)\); equality of two maps is equivalent to equality of the corresponding cosets modulo \(Z(G)\).

**Step 3: cover generators involving the external identity.** If \(u=v=1\), the map is the global identity \(S\to S\). If exactly one of \(u,v\) is \(1\) and the other is \(s\in S\), then a nonzero point in the domain must lie in a group \(\mathcal H\)-class at which \(s\) acts as both left and right identity. Consequently \(s\) is that group's identity, and the partial map is the identity on \(\{0\}\cup\mathcal H\). Otherwise the map is the identity of \(\{0\}\). If either argument is \(0\), its domain is just \(\{0\}\). These are already among the maps described in Steps 1 and 2. (If \(S\) has an identity, the same conclusion holds without formally adjoining one.)

**Step 4: multiplication and the exceptional one-position case.** Let \(E=\{(\mu,i):p_{\mu i}\ne0\}\). Its size is \(m\). Besides the global identity, the nonzero component maps are precisely every triple \((e,h,f)\in E\times H\times E\), interpreted as conjugation by the representative of \(h\) from the group class indexed by \(e\) to the one indexed by \(f\), fixing \(0\). Composing two maps whose intermediate group classes match multiplies their labels in \(H\) (with the conventional choice of composition order). If they do not match, their only common point is \(0\), and the composite is the unique partial identity on \(\{0\}\). The component maps and this zero form \(B_m(H)\); adjoining the global identity gives \(B_m(H)^1\).

When \(m=1\), regularity forces \(|I|=|\Lambda|=1\). Thus \(S\cong G^0\) is itself a monoid, and its global identity agrees with the identity of the unique component group. There is no additional external identity. Hence \(\operatorname{Inn}(S)\cong H^0\). When \(m\ge2\), at least two disjoint group components occur, so their component identities differ from the global identity, which must be adjoined. This proves the classification and order formula.

**Step 5: recover the complete isomorphism invariant.** The monoid \(H^0\) has two idempotents; for \(m\ge2\), the monoid \(B_m(H)^1\) has \(m+2\) idempotents (zero, global identity, and \(m\) distinct local identities). Thus the isomorphism type recovers \(m\). The maximal subgroup at any nonzero nonglobal primitive idempotent recovers \(H\). Conversely, an isomorphism \(H\cong H'\) and a bijection of the two size-\(m\) index sets induce an isomorphism of their Brandt monoids. Therefore \(m\) and \(G/Z(G)\) classify \(\operatorname{Inn}(S)\) exactly.

**Step 6: distinct semigroups with the same invariant.** Let \(G\) be trivial and let the two regular \(3\times3\) zero-one sandwich matrices have supports
\[
P_1=\begin{pmatrix}1&1&1\\0&1&0\\0&0&1\end{pmatrix},\qquad
P_2=\begin{pmatrix}1&1&0\\1&0&1\\0&1&0\end{pmatrix}.
\]
Both have five nonzero entries, so both give \(\operatorname{Inn}(S)\cong B_5(1)^1\), of order \(27\). Their multisets of row degrees are \((3,1,1)\) and \((2,2,1)\), respectively. Since the numbers of idempotents in the distinct \(\mathcal L\)-classes are preserved by semigroup isomorphism and give precisely these row degrees, these two Rees semigroups are not isomorphic. In fact, their support bipartite graphs differ in degree sequence.

## Verification
A standalone exhaustive checker constructs finite Rees zero-matrix semigroups, enumerates all maps \(\varphi_{u,v}\) for \(u,v\in S^1\), compares their cardinalities with the theorem, verifies the specified domain geometry and closure under all compositions, and prints `VERIFY_OK`. Cases include cyclic groups, the symmetric group on three points, the order-eight dihedral group, multiple sparse support matrices, and both boundary cases \(m=1\). All thirteen tests passed. The finite tests are not the infinite proof; the symbolic proof above covers every finite regular Rees zero-matrix semigroup.

## Relationship to prior work
Araújo, Bentz, Kinyon, Konieczny, Malheiro, and Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041v1 (first public 2026-04-28), define the same monoid in Section 3 and explicitly characterize Rees matrices **without zero entries** in Theorem 4.2. Their Problem 7.5 expressly leaves the completely zero-simple case open. The present theorem answers that finite case and provides its exact isomorphism invariant, cardinality, and explicit nonfaithfulness example. Their earlier arXiv:2301.04252 (first posted in 2023) contains a precursor of the partial-inner-automorphism theory; a fully resolved comparison with that historical version remains a priority caveat. The 2026 paper *Complete Mappings of Semigroups* (arXiv:2608.25092) studies Rees zero-matrix semigroups using a different invariant, not partial inner automorphism monoids. General semigroup conjugacy results do not alone supply the Brandt structure established here.

## Limitations
The proof and isomorphism classification are restricted to **finite** completely zero-simple semigroups, represented by regular Rees zero-matrices. No characterization is claimed for arbitrary infinite Rees zero-matrix semigroups or arbitrary finite semigroups. The source classification concerns partial **inner** automorphisms, not the full partial automorphism inverse monoid. Source overlap with a 2023 predecessor to the 2026 motivating paper is an unresolved historical-priority consideration; no independent certification or universal novelty claim is made.

## References
1. J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, and V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041v1 (2026), Sections 3–4 and Problem 7.5. https://arxiv.org/pdf/2605.00041
2. J. Araújo et al., *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252 (initially posted 2023). https://arxiv.org/abs/2301.04252
3. J. Araújo et al., *Complete Mappings of Semigroups*, arXiv:2608.25092 (2026). https://arxiv.org/abs/2608.25092
4. A. H. Clifford and G. B. Preston, *The Algebraic Theory of Semigroups*, Vol. I, American Mathematical Society (1961), standard Rees zero-matrix conventions.
