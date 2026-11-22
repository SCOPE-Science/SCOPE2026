# Two numerical types recover every multipartite shore at the critical Henson clique rank

## Finding
For each integer \(m\ge5\), let \(H_m\) be the countable universal homogeneous \(K_m\)-free graph. Put \(k=m-2\ge3\). Pointwise name a finite induced complete \(\ell\)-partite parameter graph
\[
A=K_{a_1,\ldots,a_\ell},\qquad 1\le\ell\le k,\quad a_i\ge1,\quad n=\sum_{i=1}^\ell a_i.
\]
For \(r\in\{1,2\}\), write \(t_r(A)\) for the number of complete types of **ordered, injective, nonparameter** \(r\)-tuples over all the individually named vertices of \(A\). Let \(F(d)=4^d-3^d\). Then
\[
t_1(A)=2^n,\qquad
t_2(A)=\begin{cases}
2\cdot4^n,&\ell<k,\\
2\cdot4^n-\prod_{i=1}^kF(a_i),&\ell=k.
\end{cases}
\]
Consequently, within the family of **critical** \(k\)-partite bases, the two integers \((t_1(A),t_2(A))\) determine \(n\) and the entire **unordered multiset of shore sizes** \(\{a_1,\ldots,a_k\}\), without a supplied value of \(n\). The result uses the primitive-prime-divisor theorem for \(4^d-3^d\), not only monotonicity or a bounded part-size search.

This is a sharp arity threshold. For every \(n\ge k+2\), nonisomorphic critical \(k\)-partite parameter bases with total size \(n\) have identical \(t_1\), whereas \(t_2\) distinguishes all critical \(k\)-partite bases. The smallest collision in \(t_1\), at \(n=k+2\), is already separated by twelve pair types:
\[
A=K_{3,1,\ldots,1},\qquad B=K_{2,2,1,\ldots,1},\qquad
 t_2(A)-t_2(B)=12.
\]
By contrast, for every subcritical number \(\ell<k\) of shores, **both** numerical counts depend only on \(n\): the two-type fingerprint cannot identify subcritical shore sizes. Thus the jump from \(\ell=k-1\) to \(\ell=k\) is the exact first multipartite clique-rank at which pair types detect part structure.

## Assumptions and scope
All graphs are finite, undirected, loopless and induced when describing the parameter base. A complete multipartite graph has nonempty independent parts, with all cross-part edges present. The ambient homogeneous graph forbids a clique of order \(m\); the number of named parts satisfies \(\ell\le m-2\). Every named parameter is fixed individually, so a complete tuple type records each adjacency to every parameter and, for two new points, their mutual adjacency. Both new points must be distinct and outside the named parameter set. The result concerns numerical counts of logical types, never sampling frequencies of ambient vertices. The rank and arity restrictions are part of the claim; no statement is made about larger-part bases \(\ell\ge m-1\), or tuple arities above two.

## Proof
**(1) Complete types are exactly legal finite diagrams.** The age of \(H_m\) is all finite \(K_m\)-free graphs, and every finite partial isomorphism of \(H_m\) extends to an automorphism. Hence each labelled graph on the named base together with one or two new vertices, provided it remains \(K_m\)-free, produces exactly one complete type, and distinct adjacency diagrams produce different types. In the relational graph language this follows from homogeneity/quantifier elimination. The condition that the new vertices be outside the named set and pairwise distinct is imposed in every count.

**(2) One-point types.** A new vertex \(x\) can be adjacent to any subset \(X\) of the base, because a new \(K_m\) containing \(x\) would require \(K_{m-1}\) among its named neighbors, while the base has clique number at most \(\ell\le m-2\). Every one of the \(2^n\) subsets \(X\) yields a legal and distinct complete one-type.

**(3) Nonadjacent pair types.** Give \(x\) an arbitrary named neighborhood \(X\subseteq A\), and \(y\) an arbitrary one \(Y\subseteq A\). If \(x\not\sim y\), a forbidden clique cannot contain both, and each single-coordinate extension is legal by (2). There are therefore \(4^n\) nonadjacent ordered pair types.

**(4) Adjacent pair types.** If \(x\sim y\), any newly created forbidden \(K_m\) that was not ruled out in (2) contains \(x,y\), plus a \(K_{m-2}=K_k\) of common named neighbors. For \(\ell<k\) the base contains no \(K_k\); hence all \(4^n\) adjacent diagrams are legal, and \(t_2=2\cdot4^n\).

If \(\ell=k\), the common neighborhood \(X\cap Y\) contains a \(K_k\) precisely when it intersects all \(k\) parts of the base. For each vertex in a part of size \(d\), there are four labels representing membership in neither, \(X\) only, \(Y\) only, or both. Of the \(4^d\) assignments, precisely \(3^d\) avoid any occurrence of 'both', so \(F(d)=4^d-3^d\) assignments give a nonempty intersection in that part. The independent choices across parts multiply. Exactly \(\prod_i F(a_i)\) adjacent diagrams are illegal; all other adjacency diagrams are legal. Adding the nonadjacent contribution proves the formula for \(t_2\). Note that each \(F(d)>0\), so the critical and subcritical cases are numerically separated by the correction.

**(5) Prime-divisor rigidity of the inverse fingerprint.** From the first count recover \(n=\log_2(t_1)\), and then from the second recover
\[
P=2(t_1)^2-t_2=\prod_{i=1}^k (4^{a_i}-3^{a_i})
\]
for critical bases. It suffices to prove the following arithmetic lemma.

*Lemma.* If two finite multisets of positive integers have the same total sum and the same product of factors \(F(d)=4^d-3^d\), then the multisets are equal.

*Proof of lemma.* Cancel all matching part sizes, with multiplicity, on the two sides. If a size \(d\ge2\) remains, take the greatest remaining such size, switching the sides if necessary so that it occurs on the left. By the Bang--Zsigmondy primitive-divisor theorem, \(4^d-3^d\) has a prime factor \(p_d\) dividing none of \(4^j-3^j\) for \(1\le j<d\). The theorem has no exceptions here: \(\gcd(4,3)=1\), the exceptional \(d=2\) condition fails since \(4+3=7\) is not a power of two, and the exceptional \(d=6\) pair is \((2,1)\), not \((4,3)\). After cancellation, all sizes on the right are smaller than \(d\), so \(p_d\) divides the left remaining product but not the right, a contradiction. Thus no unmatched size \(d\ge2\) remains. Since \(F(1)=1\), the product alone cannot see singleton parts; however the equality of total sums forces the numbers of remaining singletons to agree. This proves the lemma and the claimed injectivity. To reconstruct effectively without integer factorization, enumerate the finitely many partitions of \(n\) into \(k\) positive parts and select the unique one with product \(P\). \(\square\)

**(6) Sharpness and the subcritical boundary.** At \(n=k\) and \(n=k+1\) there is only one unordered partition into \(k\) positive parts, whereas at \(n=k+2\) the distinct multisets \((3,1^{k-1})\) and \((2,2,1^{k-2})\) have identical \(t_1\). Since \(F(3)=37\) and \(F(2)^2=49\), their total two-type counts differ by \(49-37=12\). For every \(n>k+2\), the multisets \((n-k+1,1^{k-1})\) and \((n-k,2,1^{k-2})\) are distinct positive \(k\)-part partitions of the same \(n\), so unary counts still fail to distinguish them, while (5) separates their pair counts. Equation (4) already proves that any subcritical \(\ell<k\) has no pair-type structural information beyond \(n\). \(\square\)

## Verification
The standalone standard-library Python program `verification/check_counts.py` constructs actual finite named-base graphs, enumerates each ordered adjacency diagram for two new vertices, and independently checks the absence of every forbidden clique. This was compared against the formula for 64 small parameter cases of forbidden clique orders 5, 6 and 7. A separate exhaustive integer-partition comparison found no duplicate corrected pair fingerprint among 74,481 candidate critical partitions of total size at most 36 (with at most 12 parts), and explicit boundary cases were checked. Output is in `verification/output.txt`. These computations verify finite instances and not the unbounded primitive-divisor lemma or Henson homogeneity, which are supplied by the mathematical arguments and cited literature.

## Relationship to prior work
Henson's homogeneous \(K_m\)-free graphs and Conant's optimal-realization criterion establish the diagram-to-type correspondence; those results do not state any numerical inversion from two type counts. A prior explicit two-type formula for **maximal** \((m-1)\)-partite bases in a \(K_m\)-free Henson graph has different one-point restrictions: its base already contains \(K_{m-1}\), so its single-coordinate neighborhoods must omit a part. Here the base has only \(m-2\) parts, the one-point restrictions disappear, and the pair correction is the single product \(\prod_i(4^{a_i}-3^{a_i})\). A previously studied two-shore specialization is subsumed numerically at forbidden clique order four, which is deliberately outside the claimed range \(m\ge5\). The **all-part inverse reconstruction via primitive prime divisors**, and the exact part-rank boundary, are the claims here. Bang--Zsigmondy itself is a classical theorem used as an input, not a new result. Search and primary-text comparison did not locate a statement dominating this inverse reconstruction theorem; historical priority remains open to independent checking.

## Limitations
The theorem assumes an induced complete multipartite base with at most \(m-2\) parts and counts ordered injective one- and two-variable types. For fewer than \(m-2\) parts, the inverse conclusion is false, as shown by the formula. Recoverability is mathematical uniqueness with a finite exhaustive reconstruction procedure; an efficient factorization or polynomial-time inverse algorithm is not established. No result is claimed for arbitrary bases, larger numbers of parts or higher arities. Numerical tests cannot establish the cited infinite prime-divisor theorem. Historical priority and independent verification remain unconfirmed.

## References
- C. W. Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics **38** (1971), 69–83, Section 2 and Theorem 2.3. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf ; https://doi.org/10.2140/pjm.1971.38.69
- G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1 (publicly posted 2014-01-08), Section 3, Definitions 3.1–3.3 and Proposition 3.4. https://arxiv.org/html/1401.1570v1
- K. Zsigmondy, *Zur Theorie der Potenzreste*, Monatshefte für Mathematik und Physik **3** (1892), 265–284. A statement and proof of the primitive-prime-divisor theorem and its exceptions are accessible at https://proofwiki.org/wiki/Zsigmondy's_Theorem ; see also https://mathworld.wolfram.com/ZsigmondyTheorem.html
- *A collision law for two-types over maximal multipartite parameter graphs in Henson structures*, published technical result (2026), full RESULT text, https://github.com/published-finding corpus/2026/blob/main/2026/10/26/SCOPE-a-collision-law-for-two-types-over-maximal-multipartite-paramete--8c8e5c9b100b/RESULT.md
