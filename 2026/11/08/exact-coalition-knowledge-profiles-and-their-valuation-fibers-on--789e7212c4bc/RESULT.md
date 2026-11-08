# Exact coalition-knowledge profiles and their valuation fibers on finite \(\mathsf{S5}\) products

## Finding
For \(k\ge2\) agents with finite local sets \(X_1,\ldots,X_k\) of sizes \(n_i\ge2\), use the full state product \(W=\prod_iX_i\), a distinguished state \(o\), and agent accessibility determined by agreement in that agent's coordinate. Fix one proposition \(p\). The full collection of coalitions that **fail** to know \(p\) at \(o\), including the empty coalition (the global modality), is precisely an order ideal of the Boolean lattice \(2^{[k]}\). Every order ideal is attainable, so the number of different coalition-failure profiles is the classical Dedekind number \(M(k)\).

The result determines the exact number and probability of valuations giving **each** profile, not just the number of profiles. For a subset \(C\subseteq[k]\), put
\[
m_C=\prod_{i\notin C}(n_i-1).
\]
For an order ideal \(F\subseteq2^{[k]}\), write \(A=\operatorname{Max}(F)\). The number of independent Boolean valuations with failure profile \(F\) is
\[
N_F=2^{\sum_{C\in F\setminus A}m_C}\prod_{C\in A}(2^{m_C}-1).
\]
An empty sum is zero and an empty product is one. A family that is not an order ideal has zero realizations. In particular, for a uniformly random valuation, \(\Pr(\mathcal F=F)=N_F/2^{\prod_i n_i}\).

When truth values are independent with common probability \(t\in(0,1)\), the exact probability is
\[
\Pr_t(\mathcal F=F)=t^{\sum_{C\notin F}m_C}\prod_{C\in A}(1-t^{m_C}).
\]
The probability of **grand-coalition-only knowledge**, namely \(D_{[k]}p\) holds but \(D_Gp\) fails for every strict \(G\subsetneq[k]\), is
\[
t\prod_{i=1}^{k}(1-t^{n_i-1}).
\]
For balanced local sizes \(n_i=n\), the conditional probability given \(p(o)\) equals \((1-t^{n-1})^k\). In any regime with \(t^{n-1}\to0\) and \(k t^{n-1}\to\lambda\in[0,\infty)\), it tends to \(e^{-\lambda}\). It tends to zero when \(k t^{n-1}\to\infty\). Thus \(k t^{n-1}\) gives a sharp transition scale for the extreme coalition-information pattern.

With observations restricted to nonempty coalitions, precisely the empty failure profile and the singleton ideal consisting only of the empty coalition become indistinguishable. Therefore the number of restricted profiles is \(M(k)-1\).

## Assumptions and scope
Fix integers \(k\ge2\), \(n_1,\ldots,n_k\ge2\) and finite labelled nonempty sets \(X_i\) of sizes \(n_i\). Let \(o=(o_1,\ldots,o_k)\in W=\prod_iX_i\). For each agent \(i\), the indistinguishability relation is \(xR_i y\) exactly if \(x_i=y_i\); this is an equivalence relation. Every world combination is present in the **full** Cartesian product, and every valuation \(V\subseteq W\) of the one atomic proposition \(p\) is permitted. Define \(R_G=\bigcap_{i\in G}R_i\), including \(R_\varnothing=W\times W\), and let \(o\models D_Gp\) if and only if \(R_G[o]\subseteq V\). A failure profile is \(\mathcal F(V)=\{G:o\not\models D_Gp\}\). Here \([k]=\{1,\ldots,k\}\) and order ideals are downward closed under subset inclusion.

For each world \(y\), define its **agreement signature** \(C(y)=\{i:y_i=o_i\}\). All signature cells are nonempty because \(n_i\ge2\), and their exact sizes are \(m_C\) as above. All counts are for labelled worlds and labelled agents, without quotienting by permutations. The probability statement assumes independent, identically distributed Bernoulli truth values, not a dependent random epistemic model.

## Proof
**Step 1 (semantic reduction).** The condition \(oR_Gy\) holds exactly when \(G\subseteq C(y)\). Consequently
\[
\mathcal F(V)=\bigcup_{y\notin V}\{G\subseteq C(y)\}=\downarrow\{C(y):y\notin V\}.
\]
This is a downward-closed family. Conversely, for any downward-closed \(F\), if \(F=\varnothing\), choose \(V=W\). Otherwise choose one false world from every signature cell indexed by a maximal member of \(F\) and make all other worlds true. The chosen cells exist because each \(n_i\ge2\). The displayed identity gives exactly \(\mathcal F(V)=F\). This proves the bijection between possible profiles and order ideals and hence their classical Dedekind-number count.

**Step 2 (exact fibers).** Fix a downset \(F\) and let \(A=\operatorname{Max}(F)\), so \(F=\downarrow A\). Any false point whose signature \(C\) lies outside \(F\) would create a failure not in \(F\), hence all points in such cells are forced true. For each maximal \(C\in A\), at least one false point is necessary: a world with any other signature in \(F\) cannot force failure of \(D_Cp\) unless its signature contains \(C\), and maximality then forces equality. Conversely, these nonempty false choices at maximal cells ensure every failure in \(F\). Cells indexed by \(F\setminus A\) are unrestricted. A maximal cell admits \(2^{m_C}-1\) nonempty false subsets, and every unrestricted cell admits \(2^{m_C}\) choices. Their independent product is the claimed \(N_F\). This is a full classification of all Boolean valuations and implies \(\sum_F N_F=2^{|W|}\).

**Step 3 (exact probability).** In a signature cell of size \(m_C\), the probability that all points are true is \(t^{m_C}\). Cells outside \(F\) must all be true, contributing the first factor. Maximal cells must have at least one false point, contributing \(1-t^{m_C}\). The remaining cells are unrestricted, contributing one. Independence across disjoint cells gives the probability formula. The same argument covers \(F=\varnothing\) and the full ideal: in the latter case, the unique maximal cell is \(C=[k]\) of size one, so the condition is exactly \(p(o)\) false.

**Step 4 (grand-only knowledge and sharp scale).** For the ideal \(F=2^{[k]}\setminus\{[k]\}\), the maximal signatures are \(C_i=[k]\setminus\{i\}\), one for each agent. The grand-coalition fiber is the singleton \(\{o\}\), so knowing \(p\) as that coalition means \(p(o)\) is true (probability \(t\)). Each cell of signature \(C_i\) has exactly \(n_i-1\) worlds, and cells for different \(i\) are disjoint. Thus each must have some false point, yielding \(t\prod_i(1-t^{n_i-1})\). In the balanced case, set \(x=t^{n-1}\). For \(x\to0\), \(\log(1-x)=-x+O(x^2)\), so if \(kx\to\lambda<\infty\), \((1-x)^k\to e^{-\lambda}\); if \(kx\to\infty\), \((1-x)^k\le e^{-kx}\to0\). More generally, if \(\max_i t^{n_i-1}\to0\) and \(\sum_i t^{n_i-1}\to\lambda<\infty\), the product tends to \(e^{-\lambda}\). For fixed \(k\) and growing \(n_i\), the entire distribution concentrates on the two extreme profiles: full failure with probability \(1-t\), and grand-only knowledge with probability tending \(t\).

**Step 5 (excluding the empty coalition).** The empty coalition belongs to every nonempty order ideal, and every ideal containing any nonempty coalition contains it. Hence removing its coordinate leaves only the empty ideal and \(\{\varnothing\}\) with the same restricted profile. Both are realized by Step 1, while all other ideals remain distinguishable. The count decreases from \(M(k)\) to \(M(k)-1\).

## Verification
Run `python3 distributed_knowledge_verifier.py` with a standard-library Python 3 interpreter. It reconstructs the original \(D_G\) semantics directly for every Boolean valuation on eight finite parameter tuples, compares semantic profiles with their signature-cell descriptions, checks the fiber-count formula for every ideal and the nonempty-coalition count, and checks the grand-only number against the closed form. It enumerated 74,832 valuations in total: local sizes \((2,2)\), \((2,3)\), \((3,3)\), \((2,4)\), \((2,2,2)\), \((2,2,3)\), \((2,3,2)\), and \((2,2,2,2)\). The observed profile counts were respectively \(6,6,6,6,20,20,20,168\), and all checks passed. These are finite regression tests, not substitutes for Steps 1–5, which establish the all-size statements.

## Relationship to prior work
Murai, Liu and Sano (2026, arXiv:2606.31886v1) analyze distributed-knowledge logics and explicitly allow the empty group as a global modality. Their results concern sequent calculi, analytic cut and Craig interpolation, rather than enumerating pointwise truth/failure profiles and their valuation multiplicities on complete finite product frames. Ågotnes, Alechina and Galimullin (2022) develop group-announcement logic with distributed knowledge and the intersection semantics; that source does not provide these specific all-profile exact fibers. Classical Dedekind numbers already enumerate antichains/order ideals, and the elementary signature-cell factorization is based on standard finite counting: no new general theorem on Dedekind numbers is claimed. Nearby published enumerations of inquisitive epistemic frames and irredundant value knowledge concern different classes of structures and do not imply the stated fiber-count and Bernoulli sharp-threshold theorem for a fixed full-product frame. Literature priority outside the inspected sources is not certified.

## Limitations
The full-product assumption and \(n_i\ge2\) are essential to universal realization of every downset. For incomplete state products or singleton local factors, some agreement-signature cells can be empty and the realizability and fiber formulas must be modified. Only one propositional atom at a single pointed state is counted, not simultaneous profiles for many atoms or states, and no quotient by automorphisms is taken. No statement about nonproduct epistemic frames, dependent random valuations, or arbitrary epistemic formulas is proved. Established order-ideal enumeration and older distributed-knowledge literature could contain equivalent descriptions; the new contribution is the explicit combined model-theoretic fiber and sharp-probability law in the specified setting. Independent assessment of correctness or historical priority is not claimed.

## References
1. R. Murai, S. Liu and K. Sano, *Analytic Cut in Epistemic Logics with Distributed Knowledge*, arXiv:2606.31886v1, first publicly posted 2026-06-30. https://arxiv.org/abs/2606.31886
2. T. Ågotnes, N. Alechina and R. Galimullin, *Logics with Group Announcements and Distributed Knowledge: Completeness and Expressive Power*, 2022, DOI 10.1007/s10849-022-09355-0. https://link.springer.com/article/10.1007/s10849-022-09355-0
3. *Ability and knowledge: from epistemic transition systems to labelled stit models*, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11538171/
4. Classical Dedekind-number identity: the number of downsets of a \(k\)-element Boolean lattice is the number of antichains, equivalently monotone Boolean functions, on \(k\) generators.
