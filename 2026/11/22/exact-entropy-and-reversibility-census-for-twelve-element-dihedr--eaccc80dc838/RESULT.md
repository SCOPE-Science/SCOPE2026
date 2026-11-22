# Exact entropy and reversibility census for twelve-element dihedral group cellular automata

## Finding
Let \(G\cong S_3\times C_2\), the dihedral group of order twelve, and let \(J\subset\mathbb Z\) be any fixed nonempty finite set with \(r=|J|\). Consider continuous, shift-commuting **group homomorphisms** \(F:G^{\mathbb Z}\to G^{\mathbb Z}\) whose local rule uses only coordinates in \(J\). Such a rule is surjective if and only if, for unique \(k\in J\), \(\alpha\in\operatorname{Aut}(S_3)\), and polynomials \(P\ne0,Q\in\mathbb F_2[u,u^{-1}]\) supported within \(J\), it has the form
\[
F(y,z)_i=\left(\alpha(y_{i+k}),\ \sum_{j\in J}p_jz_{i+j}+\sum_{j\in J}q_j\varepsilon(y_{i+j})\pmod2\right),
\]
where \(\varepsilon:S_3\to\mathbb F_2\) is the sign homomorphism, \(P(u)=\sum p_ju^j\), and \(Q(u)=\sum q_ju^j\). The topological entropy and reversibility criterion are
\[
h_{\rm top}(F)=|k|\log 6+\bigl(\max(0,\max\operatorname{supp}P)-\min(0,\min\operatorname{supp}P)\bigr)\log2,
\]
\[
F\text{ reversible}\quad\Longleftrightarrow\quad P\text{ is a single monomial}.
\]
For \(r\) prescribed sites, exactly \(6r\,2^r(2^r-1)\) rules are globally surjective, and exactly \(6r^2 2^r\) of these are reversible; the reversible fraction is \(r/(2^r-1)\). In contrast, \(6r(4^r-2)\) group-homomorphism local rules are surjective **as finite local maps**, so exactly \(6r(2^r-2)\) local-surjectivity false positives exist for \(r\ge2\).

For the one-sided interval \(J=\{0,1,\ldots,r-1\}\), the attainable entropy values are the **exactly \(r^2\) distinct numbers** \(\log(6^k2^d)\), \(0\le k,d<r\). Each is attained by exactly \(6\cdot2^{r+d}\) surjective rules, of which \(6\cdot2^r\) are reversible. Equivalently, with a formal variable tracking each exponent, their complete multiplicity polynomial is
\[
\mathcal E_r(X,Y)=6\cdot2^r\left(\sum_{k=0}^{r-1}X^k\right)\left(\sum_{d=0}^{r-1}2^dY^d\right).
\]

## Assumptions and scope
The group is written as \(G=S_3\times\mathbb F_2\) with direct-product multiplication, the spatial lattice is bilateral \(\mathbb Z\), and the shift convention is \((\sigma^jx)_i=x_{i+j}\). A local rule 'supported within \(J\)' may ignore some elements of \(J\); this matters for the counting formulas. The global map must be a group endomorphism, not merely an arbitrary cellular automaton. Entropy is the time-iteration topological entropy of \(F\), not the spatial entropy of a factor shift. Zero coefficients outside \(J\) are understood. The formulas also hold for negative offsets in the general \(J\) statement.

## Proof
**1. Algebraic normal form.** Every local group homomorphism \(f:G^J\to G\) decomposes into commuting images of the input factors. Project onto \(S_3\). If the projected local map is onto, at least one input factor must have nonabelian projected image, because the commuting product of proper homomorphic images of \(S_3\) and images of \(C_2\) is abelian: proper quotients of \(S_3\) are trivial or \(C_2\). Therefore one input \(S_3\) factor maps onto \(S_3\), hence by an automorphism \(\alpha\). Every other input factor projects trivially, because it commutes with all of \(S_3\) and \(Z(S_3)=1\). The automorphism-bearing site \(k\) and \(\alpha\) are unique. Any homomorphism \(S_3\to C_2\) is either zero or sign; any homomorphism \(C_2\to C_2\) is zero or identity. Hence the central coordinate is uniquely described by \(P,Q\). Conversely every displayed rule is a group homomorphism.

**2. Global surjectivity.** If \(F\) is globally onto, the projected \(S_3\) local map is onto, giving Step 1. Its induced quotient CA \(y\mapsto\alpha\sigma^ky\) is invertible, so for a prescribed target \(y'\) the entire input \(y\) is fixed. The remaining central equation is an affine translate of \(z\mapsto P(\sigma)z\). For \(P=0\) this cannot cover every target central configuration. For \(P\ne0\), the dual of \(P(\sigma)\) is multiplication by the nonzero Laurent polynomial \(P\) on the integral domain \(\mathbb F_2[u,u^{-1}]\), hence is injective. Pontryagin duality gives surjectivity of \(P(\sigma)\), so \(F\) is onto. Moreover, \(P(\sigma)\) is injective exactly when multiplication by \(P\) is onto on the Laurent polynomial module, equivalently \(P\) is a Laurent-polynomial unit, i.e. a monomial; this also characterizes reversibility of \(F\).

**3. Entropy.** The central subgroup \((C_2)^{\mathbb Z}\) is closed, normal and \(F\)-invariant; its restriction is \(P(\sigma)\), and its quotient action is \(\alpha\sigma^k\) on \(S_3^{\mathbb Z}\). Bowen's topological entropy addition theorem for continuous endomorphisms of compact metrizable groups yields the sum of their entropies. If \(t\) is the finite order of \(\alpha\), then \((\alpha\sigma^k)^t=\sigma^{kt}\), giving quotient entropy \(|k|\log6\). For the one-dimensional scalar linear CA, the exact Laurent characteristic-polynomial formula gives \(h(P(\sigma))=\bigl(\max(0,\max\operatorname{supp}P)-\min(0,\min\operatorname{supp}P)\bigr)\log2\). This result is also independently obtainable from growth of iterated Laurent-polynomial spans. The coupling polynomial \(Q\) does not change the entropy because the addition theorem depends only on quotient and subgroup dynamics.

**4. Exact counts.** On \(r\) prescribed sites, choose \(k\) in \(r\) ways, \(\alpha\) in \(6\) ways, nonzero \(P\) in \(2^r-1\) ways, and \(Q\) in \(2^r\) ways. The parameterization is injective. Reversibility requires one of \(r\) monomials for \(P\), giving \(6r^2 2^r\). The finite local map is onto also when \(P=0\) but \(Q\) has a nonzero coefficient at some site other than \(k\): varying that site's \(S_3\) input toggles the central output without changing the output \(S_3\) coordinate. There are \(2(2^{r-1}-1)=2^r-2\) such \(Q\), giving \(6r(4^r-2)\) locally onto rules. They are not globally onto, as Step 2 shows. For \(J=\{0,\dots,r-1\}\), \(\deg P=d\) occurs in exactly \(2^d\) nonzero polynomials. Entropy is \(k\log6+d\log2\). Unique prime factorization of \(6^k2^d\) makes all pairs \((k,d)\) spectrally distinct. There are \(6\cdot2^{r+d}\) rules at each level, of which precisely \(6\cdot2^r\) have monomial \(P\).

## Verification
The standalone pure-Python file `verify.py` implements \(S_3\times C_2\) by the semidirect coordinate law, independently enumerates all 64 endomorphisms of the twelve-element group from generators and relations, validates each multiplication table, and enumerates the commuting-image pairs. It checks 12 onto and reversible one-site rules, 144 globally onto and 96 reversible two-site rules, **168** onto finite local maps with two sites, and every entropy-multiplicity coefficient for \(1\le r\le7\). These are finite cross-checks. The infinite-space surjectivity, entropy identity, and all-radius formulas follow from the preceding proof, not from finite experimentation.

## Relationship to prior work
Dennunzio, Formenti and Margara (2024) describe image graphs and decomposable groups, including the hexagon dihedral group in their notation \(D_6\), and exhibit group cellular automata with non-surjective coordinate maps. Castronuovo, Dennunzio and Margara (2025) give general quotient decomposition and decidability criteria. Castronuovo, Dennunzio, Kari and Margara (2026) provide the compact-group entropy addition framework and explicit linear entropy formula used here. The contribution claimed here is the **closed all-radius classification and joint entropy/reversibility multiplicity law**, with the precise local-versus-global surjectivity gap, rather than a new general entropy algorithm, a new decomposition theorem, or the first decomposable-group example.

## Limitations
The formulas require group-homomorphism local rules and the specific twelve-element dihedral alphabet; they do not characterize all arbitrary cellular automata or all dihedral alphabets. The finite-state checker cannot certify historical priority or replace the cited general entropy theorem. Historical priority remains provisional because group image-graph tables may allow the count to be reconstructed indirectly. An independent mathematical audit has not been performed.

## References
- A. Dennunzio, E. Formenti, L. Margara, *On the Dynamical Behavior of Cellular Automata on Finite Groups*, IEEE Access 12 (2024), 122061–122077. https://doi.org/10.1109/ACCESS.2024.3452199
- N. Castronuovo, A. Dennunzio, L. Margara, *A Divide and Conquer Algorithm for Deciding Group Cellular Automata Dynamics*, arXiv:2507.09761 (2025). https://arxiv.org/abs/2507.09761
- N. Castronuovo, A. Dennunzio, J. Kari, L. Margara, *Topological Entropy of Group Cellular Automata is Effectively Computable*, arXiv:2611.16746v1 (first posted 2026-11-12). https://arxiv.org/abs/2611.16746
- R. Bowen, *Entropy for group endomorphisms and homogeneous spaces*, Trans. Amer. Math. Soc. 153 (1971), 401–414. https://doi.org/10.1090/S0002-9947-1971-0274707-X
