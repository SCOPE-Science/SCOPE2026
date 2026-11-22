# Exact minimal sizes for elementary-abelian symmetries of commuting-permutation braid solutions

## Finding

For a prime \(p\) and an integer \(r\geq1\), let \(\mu_p(r)\) be the smallest cardinality of a **nonempty finite** set \(X\) admitting two commuting permutations \(f,g\in\operatorname{Sym}(X)\) for which the braid solution
\[
R_{f,g}(x,y)=(f(y),g(x))
\]
has automorphism group \(\operatorname{Aut}(X,R_{f,g})\cong(C_p)^r\). Set \(\mu_p(r)=\infty\) if there is no such set. Then
\[
\boxed{\mu_p(r)=\begin{cases}
2r,&p=2,\ 1\leq r\leq6,\\
pr,&p\text{ odd},\ 1\leq r\leq p+1,\\
p^2+p(r-2),&p\text{ odd},\ p+2\leq r\leq p+3,\\
\infty,&\text{otherwise}.
\end{cases}}
\]
In particular, the largest elementary-abelian rank attainable in this entire class, regardless of set size, is \(p+3\) for odd \(p\), and \(6\) for \(p=2\). For odd \(p\), the minimum faithful permutation degree \(pr\) ceases to be attainable precisely when \(r>p+1\), and the exact excess above it is \(p(p-2)\) in both remaining attainable ranks.

## Assumptions and scope

Here \(C_p\) denotes the cyclic group of order \(p\), and the automorphisms are *all* permutations \(\sigma\) of the underlying set satisfying \((\sigma\times\sigma)R_{f,g}=R_{f,g}(\sigma\times\sigma)\). The solution is bijective and nondegenerate, but is not required to be involutive. The theorem is **only** about this commuting-permutation family, not about arbitrary set-theoretic braid or Yang--Baxter solutions.

All cardinalities are ordinary finite set cardinalities. No assumption that the two permutations generate the displayed automorphism group is imposed. The minimum is attained explicitly in every finite case.

## Proof

**Step 1 (the braid condition and automorphisms).** A direct calculation on triples shows that \(R_{f,g}\) satisfies \(R^{12}R^{23}R^{12}=R^{23}R^{12}R^{23}\) if and only if \(fg=gf\). The two coordinate identities defining an automorphism are respectively \(\sigma f=f\sigma\) and \(\sigma g=g\sigma\); hence
\[
\operatorname{Aut}(X,R_{f,g})=C_{\operatorname{Sym}(X)}(f,g).
\]
If this group \(A\) is elementary abelian of exponent \(p\), then \(f,g\in A\): indeed, each commutes with itself and with the other. Thus \(H=\langle f,g\rangle\) is elementary abelian with \(\dim_{\mathbb F_p}H\leq2\), and \(A=C_{\operatorname{Sym}(X)}(H)\).

**Step 2 (the centralizer of an abelian group action).** For each subgroup \(K\leq H\), let \(m_K\) be the number of \(H\)-orbits isomorphic to the transitive \(H\)-set \(H/K\). Since \(H\) is abelian, distinct stabilizer subgroups give nonisomorphic transitive \(H\)-sets. An equivariant bijection can translate an orbit by any element of \(H/K\) and permute its \(m_K\) copies. Consequently,
\[
C_{\operatorname{Sym}(X)}(H)\cong
\prod_{K\leq H}\bigl((H/K)\wr S_{m_K}\bigr).
\]
If \(K\ne H\), an orbit is nontrivial and \(m_K\geq2\) would give a nonabelian wreath-product factor, contrary to \(A\) being elementary abelian. Therefore \(m_K\in\{0,1\}\) for every proper \(K\). For \(K=H\), the factor is \(S_{m_H}\), elementary abelian of exponent \(p\) only when \(m_H\leq1\), or \(m_H=2\) and \(p=2\). The latter contributes one additional independent \(C_2\)-factor. A lone globally fixed point contributes no factor and only increases the set size.

When \(\dim H=2\), there are precisely \(p+1\) subgroups \(K\) of index \(p\), giving orbit size \(p\) and centralizer rank one; there is one subgroup \(K=0\), giving an orbit of size \(p^2\) and centralizer rank two; and the fixed-point type \(K=H\). Write \(a\) for the number of distinct index-\(p\) types used, \(b\in\{0,1\}\) for the presence of the free \(H\)-orbit, and \(e\in\{0,1\}\) for a pair of \(H\)-fixed points (allowed only when \(p=2\)). The rank and size then satisfy
\[
r=a+2b+e,\qquad
|X|\geq pa+p^2b+2e,
\quad 0\leq a\leq p+1.
\]
For \(\dim H\leq1\), there is at most one nontrivial orbit type, and its centralizer rank contribution is at most one, with at most one further factor from a fixed pair when \(p=2\). These cases cannot exceed the asserted maximal ranks and do not improve the eventual minimum formulas.

It follows immediately that no rank exceeding \(p+3\) for odd \(p\), or exceeding \(3+2+1=6\) for \(p=2\), is possible, regardless of \(|X|\).

**Step 3 (the universal size lower bound).** The group \(A\cong(C_p)^r\) acts faithfully on \(X\). If its orbits have stabilizers \(L_i\) of codimensions \(d_i\), faithfulness gives an injection \(A\hookrightarrow\bigoplus_i A/L_i\), so \(\sum_i d_i\geq r\). Since \(p^d\geq pd\) for every integer \(d\geq0\),
\[
|X|=\sum_i p^{d_i}\geq p\sum_i d_i\geq pr.
\]
For odd \(p\) and \(r\leq p+1\), this lower bound is sharp by the construction below. For odd \(p\) and \(r\geq p+2\), Step 2 forces \(\dim H=2\) and the presence of the free orbit \(b=1\); otherwise at most \(p+1\) rank-one orbit types are available. Thus \(a=r-2\), and
\[
|X|\geq p(r-2)+p^2.
\]
This exhausts the possible odd-prime ranks because \(a\leq p+1\). For \(p=2\), the universal lower bound is \(2r\) at every permitted rank.

**Step 4 (attaining all bounds).** Put \(H_0=\mathbb F_p^2\) and choose the \(p+1\) distinct projective linear forms represented by \((1,t)\), for \(t\in\mathbb F_p\), together with \((0,1)\). For each chosen form \(\ell(u,v)=au+bv\), create a block \(X_\ell=\mathbb F_p\), on which the first permutation translates by \(a\) and the second by \(b\). All these blocks are pairwise nonisomorphic as \(H_0\)-sets. Optionally add the free block \(H_0\), on which the first and second permutations translate by the two standard basis vectors. When \(p=2\), we may also add a pair of common fixed points; their only additional equivariant automorphism is the transposition.

For odd \(p\) and \(1\leq r\leq p+1\), take \(r\) distinct form blocks. For odd \(p\) and \(p+2\leq r\leq p+3\), take \(r-2\) form blocks and the free block. The above wreath-product formula shows that the common centralizer is exactly \((C_p)^r\), with sizes \(pr\) and \(p(r-2)+p^2\) respectively. If only one form is chosen, the actual generated action is cyclic rather than rank two, but its centralizer is still exactly \(C_p\), as required.

For \(p=2\), use respectively the following blocks as \(r\) runs from one through six: one form block; two form blocks; all three form blocks; all three form blocks and a fixed pair; all three form blocks and the free block; all three form blocks, the free block, and a fixed pair. Their sizes are \(2r\), and their centralizers are exactly \((C_2)^r\). This proves all positive cases and all impossibility cases. \(\square\)

## Verification

The accompanying standalone Python 3 program `CHECK.py` constructs the explicit permutations, verifies their commutativity and the braid equation by direct triple evaluation for all asserted ranks at primes \(2\), \(3\), and \(5\). Whenever the constructed set has at most eight points, it exhaustively enumerates all permutations commuting with both generators and checks the resulting centralizer cardinality and exponent. The analytic proof of the general bound and all-rank classification is independent of those finite computations.

To replay: execute `python3 CHECK.py` from the directory containing the extracted file. Expected terminal marker: `COMMUTING_PERMUTATION_BRAID_CENTRALIZERS_OK`.

## Relationship to prior work

Permutation-type braid solutions determined by two commuting permutations are classical; neither their existence nor the elementary centralizer formula is asserted as newly invented. Agore--Chirvasitu--Militaru establish very general representations of groups as centralizers of two arbitrary maps, and Militaru's 2026 preprint transfers such centralizers to braid-solution automorphism groups. Militaru explicitly poses the minimum-size realization question for finite groups. Those constructions allow arbitrary maps or broader Yang--Baxter families and do not provide the sharp finite/infinite rank cutoff or exact minimum sizes for the restricted commuting-permutation family here.

Jedlička--Pilitowska--Zamojska-Dzienio classify a different class of indecomposable *involutive* solutions with abelian associated permutation group, and analyze their automorphism groups; their results concern different hypotheses and do not imply the above noninvolutive, potentially highly decomposable realizations. The proof also uses familiar finite-abelian-group-set and wreath-product techniques; priority for an equivalent reformulation in older permutation-group literature cannot be ruled out.

## Limitations

The theorem concerns exact automorphism groups, not the group generated by the left translation permutations, and only the specific two-commuting-permutation ansatz. In particular, its infinite minimal-cardinality entries do **not** prohibit realizing larger elementary-abelian groups by other set-theoretic Yang--Baxter solutions or by commuting noninvertible maps. The verification program tests selected small finite primes and ranks, not the infinite proof or exhaustive historical priority. No independent mathematical audit has been performed.

## References

1. G. Militaru, *Centralizers of maps as automorphism groups of Yang--Baxter solutions*, arXiv:2611.03380v1, 2 November 2026. https://arxiv.org/html/2611.03380v1
2. G. Militaru, *Every group is the automorphism group of a set-theoretic solution of the Yang--Baxter equation*, arXiv:2610.39228, first posted 29 October 2026. https://arxiv.org/abs/2610.39228
3. A. L. Agore, A. Chirvasitu, G. Militaru, *The set-theoretic Yang--Baxter equation, Kimura semigroups and functional graphs*, arXiv:2303.06700, 2023; journal version 2025. https://arxiv.org/abs/2303.06700
4. P. Jedlička, A. Pilitowska, A. Zamojska-Dzienio, *Indecomposable involutive solutions of the Yang--Baxter equation of multipermutational level 2 with abelian permutation group*, arXiv:2011.00229, 2020. https://arxiv.org/abs/2011.00229
