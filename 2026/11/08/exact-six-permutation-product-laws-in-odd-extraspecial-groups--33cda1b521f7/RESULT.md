# Exact six-permutation product laws in odd extraspecial groups

## Finding
Fix an odd prime \(p\), an integer \(m\ge1\), and **any** extraspecial \(p\)-group \(G\) of order \(p^{2m+1}\). Let \(g_1,g_2,g_3\) be independently uniformly distributed elements of \(G\), **sampled with replacement**. Define
\[
K=\bigl|\{g_{\sigma(1)}g_{\sigma(2)}g_{\sigma(3)}:\sigma\in S_3\}\bigr|,
\qquad \alpha=\frac{1-p^{-2m}}{p^3}.
\]
Then the **complete distribution** is
\[
\begin{array}{c|l}
 k&\Pr(K=k)\\\hline
1&p^{-2m}+\alpha\\
2&4(p-1)\alpha\\
3&9(p-1)\alpha\\
4&6(p-1)(p-3)\alpha\\
5&3(p-1)(p-3)\alpha\\
6&(p-1)(p-3)(p-5)\alpha.
\end{array}
\]
In particular, values larger than three are impossible when \(p=3\); six distinct products are impossible when \(p=5\); and all six cardinalities occur with positive probability when \(p\ge7\). The result is identical for the exponent-\(p\) and exponent-\(p^2\) isomorphism types and for all dimensions \(2m\), after the stated scalar correction. **This is a distributional theorem, not an existence statement for selected distinct elements.**

## Assumptions and scope
An extraspecial \(p\)-group has \(Z(G)=G'=\Phi(G)\) cyclic of order \(p\); the quotient \(V=G/Z(G)\) is an elementary abelian vector space of dimension \(d=2m\). The commutator identifies, after a choice of generator of the center, with a nondegenerate alternating bilinear pairing \(\omega:V\times V\to\mathbb F_p\). These properties hold for both extraspecial isomorphism types and are the only group structure used. There is no assumption that the sampled elements are distinct, noncentral, or of order \(p\). The characteristic two case is outside the theorem.

## Proof
**1. Six central offsets.** Let \(v_i=g_iZ(G)\). Put \(a=\omega(v_1,v_2)\), \(b=\omega(v_1,v_3)\), and \(c=\omega(v_2,v_3)\). Because the commutators lie in the center, each permutation of three factors has the same image \(v_1+v_2+v_3\) in \(V\). Swapping adjacent factors changes the central coordinate by the corresponding commutator. Relative to one fixed ordering, the six offsets, up to a simultaneous sign and translation, form the set
\[
\{0,a,c,a+b,b+c,a+b+c\}\subseteq\mathbb F_p.
\]
Set \(u=a\), \(v=a+b\), and \(t=a+b+c\). The set is \(\{0,u,v,t,t-u,t-v\}\). Translating by \(-t/2\) turns it into
\[
\{\pm x,\pm y,\pm z\},\qquad
(x,y,z)=(t/2,t/2-u,t/2-v).
\]
The linear change from \((a,b,c)\) to \((x,y,z)\) is invertible over \(\mathbb F_p\) (recover \(t=2x\), \(u=x-y\), \(v=x-z\), \(a=u\), \(b=v-u\), \(c=t-v\)). Hence \(K\) equals the number of distinct elements among \(\pm x,\pm y,\pm z\).

**2. Symplectic Gram fibers.** Write \(d=2m\). The random quotient vectors \((v_1,v_2,v_3)\) are uniformly distributed on \(V^3\). The induced alternating \(3\)-by-\(3\) Gram matrix has entries \((a,b,c)\). The group \(\operatorname{GL}_3(\mathbb F_p)\) acts bijectively on \(V^3\) by changing the three vectors linearly, and transitively by congruence on the nonzero alternating \(3\)-by-\(3\) matrices, all of rank two. Thus every **nonzero** Gram triple has the same fiber cardinality.

To count the zero fiber, first choose \(v_1=0\), contributing \(p^d+(p^d-1)p^{d-1}\) orthogonal choices of \((v_2,v_3)\). For \(v_1\ne0\), the vector \(v_2\) lies in \(v_1^\perp\), of size \(p^{d-1}\). The \(p\) scalar multiples of \(v_1\) each permit \(p^{d-1}\) choices of \(v_3\). The remaining \(p^{d-1}-p\) choices of \(v_2\) permit \(p^{d-2}\) choices of \(v_3\), since two independent symplectic linear functionals must vanish. Summing gives
\[
Z=\#\{\omega(v_i,v_j)=0\ \text{for all }i<j\}
=p^{2d}+(p^d-1)p^{2d-3}.
\]
There are \(p^{3d}\) triples in total and \(p^3-1\) nonzero Gram values. Therefore each nonzero Gram triple occurs exactly
\[
T=\frac{p^{3d}-Z}{p^3-1}=(p^d-1)p^{2d-3}
\]
times. Dividing by \(p^{3d}\) gives mass \(p^{-d}+\alpha\) at Gram zero and mass \(\alpha\) at each of the \(p^3-1\) nonzero Gram values, where \(\alpha=(1-p^{-d})/p^3\).

**3. Signed-orbit occupancy.** Since the Gram-to-\((x,y,z)\) map is invertible, the same uniform nonzero fiber count applies to all nonzero signed triples. The field has one singleton sign orbit \(\{0\}\) and \(h=(p-1)/2\) two-point sign orbits \(\{s,-s\}\). For triples \((x,y,z)\) over \(\mathbb F_p\), the counts according to \(|\{\pm x,\pm y,\pm z\}|\) are
\[
\begin{array}{c|c|l}
k&N_k&\text{type}\\\hline
1&1&\text{all zero}\\
2&8h&\text{one nonzero sign orbit, no zero}\\
3&18h&\text{zero plus one nonzero sign orbit}\\
4&48\binom h2&\text{two distinct sign orbits, no zero}\\
5&24\binom h2&\text{zero plus two distinct sign orbits}\\
6&48\binom h3&\text{three distinct sign orbits, no zero}.
\end{array}
\]
The factors follow by distributing three labeled coordinates among the indicated orbits and choosing one of two signs at each nonzero coordinate. For instance \(N_4=\binom h2(2^3)(2^3-2)\), \(N_5=\binom h2\cdot3\cdot2\cdot2^2\), and \(N_6=\binom h3\cdot3!\cdot2^3\). The identities \(\sum_kN_k=p^3\) and \(N_1=1\) give \(\Pr(K=1)=p^{-d}+\alpha\), while \(\Pr(K=k)=N_k\alpha\) for \(k>1\). Substituting \(h=(p-1)/2\) proves the displayed formula and the sharp prime thresholds. \(\square\)

## Verification
The standalone `checker.py` independently enumerates all three quotient vectors and computes their commutator Gram triples for \((p,m)=(3,1),(5,1),(7,1),(3,2)\), comparing the complete histograms and every Gram-fiber multiplicity to the theorem. It also enumerates all ordered triples of group elements and their six actual products for two nonisomorphic groups of order \(27\): the exponent-three Heisenberg group and the exponent-nine semidirect product. The total quotient-vector cases are \(665444\); the two actual group calculations contribute \(39366\) ordered triples. The recorded verification is `VERIFY_OK`. Execute `python3 checker.py` from the extracted package directory. This finite verification is a check of the symbolic argument, not its substitute.

## Relationship to prior work
Van Doorn, Judin, Monticone, and Morrison, *On Some Problems from the Kourovka Notebook*, arXiv:2607.17477, Section 3 (first submitted 20 July 2026), prove that for any prescribed cardinality between one and a factorial there **exists a group and an ordered tuple of distinct elements** attaining that cardinality. Their explicit central-extension construction is an existence result, not an enumeration of the probabilities in a fixed finite group. The present distributional theorem for uniform triples in every odd extraspecial group is not implied by choosing existence witnesses. Kohl's earlier MathOverflow problem (2013) and Monticone's 2026 solution note are acknowledged, though the direct source pages could not be inspected during this review. Savelyev's arXiv:2608.28291 concerns Rota–Baxter operators on extraspecial groups and supplies contemporary group-family context, not the present probability distribution. Other available exact commutativity-degree formulas count different events (subgroups or pairs) and do not determine the six-way permutation collision law.

## Limitations
The law assumes independent uniform sampling with replacement. It is not a distribution conditioned on the three elements being distinct. It covers odd-prime extraspecial groups with center of order \(p\) and does not cover extraspecial two-groups, arbitrary class-two groups with higher-dimensional center, or products of four or more elements. The complete historical priority of the exact distribution is not certified: older unpublished enumerations and the inaccessible 2013 discussion or 2026 solution note could contain related computations. No independent mathematical audit has been performed.

## References
1. W. van Doorn, E. Judin, P. Monticone, D. Morrison, *On Some Problems from the Kourovka Notebook* (2026), arXiv:2607.17477, Section 3; https://arxiv.org/abs/2607.17477 . First public arXiv version 20 July 2026.
2. S. Kohl, *Numbers of distinct products obtained by permuting the factors*, MathOverflow question 123890 (7 March 2013); https://mathoverflow.net/q/123890 . Direct page unavailable during this review.
3. P. Monticone, *Kourovka Notebook Problem 18.50*, solution note, dated 16 May 2026; https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/05/18_50.pdf . The citation appears in reference 26 of [1]; direct note unavailable.
4. A. Savelyev, *Rota–Baxter operators on extraspecial groups* (28 August 2026), arXiv:2608.28291; https://arxiv.org/abs/2608.28291 . Only the abstract was accessible for inspection.
