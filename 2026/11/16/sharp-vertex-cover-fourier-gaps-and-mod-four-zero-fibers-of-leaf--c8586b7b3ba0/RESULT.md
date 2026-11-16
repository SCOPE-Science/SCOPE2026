# Sharp vertex-cover Fourier gaps and mod-four zero fibers of leaf coronas

## Finding
Let \(G\) be any finite simple graph on \(n\ge1\) labelled vertices, and form its leaf corona \(F=G\circ K_1\) by adjoining one private leaf to each vertex. Let \(A_F\subseteq\mathbb F_2^{2n}\) be all independent-set incidence vectors of \(F\). The unnormalized Walsh transform of \(1_{A_F}\), with the first \(n\) coordinates corresponding to core vertices, is
\[
W_G(a,b)=\sum_{(x,y)\in A_F}(-1)^{a\cdot x+b\cdot y},\qquad a,b\in\mathbb F_2^n.
\]
Write \(\alpha(G)\) for the maximum independent-set size and \(\tau(G)=n-\alpha(G)\) for the vertex-cover number. **Every nonzero coefficient has magnitude at least \(2^{\tau(G)}\), and this bound is attained.** In particular, for unnormalized convolution \(C_F f=1_{A_F}*f\) on \(\ell^2(\mathbb F_2^{2n})\),
\[
\min_{W_G(a,b)\ne0}|W_G(a,b)|=2^{\tau(G)},\quad
\|C_F^\dagger\|_{2\to2}=2^{-\tau(G)},\quad
\kappa_+(C_F)=2^{\alpha(G)}I_G(1/2).
\]
Here \(I_G(t)=\sum_{J\text{ independent in }G}t^{|J|}\), and \(\kappa_+\) is the largest-to-smallest positive singular-value ratio; zero multipliers are excluded from that ratio.

There is also an exact *frequency-fiber zero-existence criterion* for every core path \(G=P_n\). Fix a pendant-frequency vector \(b\), with support \(B\subseteq\{1,\ldots,n\}\). If \(B\) is not independent in the path, \(W_G(a,b)=0\) for every \(a\). Otherwise let \(R=P_n-N[B]\) be the induced graph outside the closed neighborhood of \(B\), and let its nonempty components have lengths \(\ell_1,\ldots,\ell_r\). Then:

- **Universal nonvanishing:** \(W_G(a,b)\ne0\) for every \(a\) if and only if no \(\ell_j\equiv2\pmod4\).
- **Mixed fiber:** if some \(\ell_j\equiv2\pmod4\), both a vanishing and a nonvanishing coefficient occur as \(a\) varies.
- **Fixed dyadic order in universal fibers:** if no component has length \(2\pmod4\), every multiplier in the fiber satisfies
\[
\nu_2(W_G(a,b))=|N(B)|+\sum_{j=1}^{r}\left\lfloor\ell_j/2\right\rfloor.
\]

For an empty residual graph, the empty product is \(1\) and the sum of component lengths is \(0\). This theorem classifies entire core-frequency fibers, not the individual zero patterns within mixed fibers.

## Assumptions and scope
All graphs are finite, simple, undirected, and have labelled core vertices. An independent set may be empty. The open neighborhood \(N(B)\) excludes \(B\), and \(N[B]=N(B)\cup B\). All Walsh transforms and convolutions use unnormalized sums; the Fourier transform diagonalizes convolution without changing its operator eigenvalues. Singular-value statements refer to the counting-measure Hilbert space and the Moore–Penrose pseudoinverse. The empty residual path has continuant value \(1\).

## Proof
**1. Exact corona factorization.** The core part \(I\) of any independent set of \(F\) is an independent subset of \(G\). For each core vertex outside \(I\), its private leaf may be either selected or omitted; for each core vertex in \(I\), its leaf must be omitted. Consequently
\[
W_G(a,b)=\sum_{I\subseteq V(G),\ I\text{ independent}}(-1)^{\sum_{i\in I}a_i}\prod_{i\notin I}(1+(-1)^{b_i}).
\tag{1}
\]
Put \(B=\{i:b_i=1\}\). If \(B\) is not independent, no \(I\) in (1) contains it and the transform vanishes. For independent \(B\), write \(R=G[V(G)\setminus N[B]]\). Every contributing core set is uniquely \(I=B\cup J\), with \(J\) independent in \(R\). Thus
\[
W_G(a,b)=(-1)^{\sum_{i\in B}a_i}2^{|N(B)|}\,P_R(s),\qquad
P_R(s)=\sum_{J\subseteq V(R),\ J\text{ independent}}2^{|V(R)|-|J|}\prod_{i\in J}s_i,
\tag{2}
\]
where \(s_i=(-1)^{a_i}\) on \(R\). This equality also holds for an empty \(R\).

**2. Universal sharp gap and conditioning.** Formula (1) is a sum of integer multiples of \(2^{n-|I|}\). Since \(|I|\le\alpha(G)\), every multiplier is divisible by \(2^{n-\alpha(G)}\), so every nonzero multiplier has magnitude at least this power of two. Let \(B\) be a maximum independent set of \(G\); any independent \(I\supseteq B\) equals \(B\). Formula (1) then has precisely one surviving term, giving \(W_G(a,1_B)=(-1)^{\sum_{i\in B}a_i}2^{n-|B|}\). Hence the lower bound is attained. Since \(\max_{a,b}|W_G(a,b)|=W_G(0,0)=|A_F|=2^n I_G(1/2)\) by the triangle inequality and positive terms, the operator and condition-number identities follow by Fourier diagonalization.

**3. Signed path continuants.** If \(R\) is a disjoint union of paths, (2) factors over its connected components. For a path of length \(m\) vertices with signs \(s_1,\ldots,s_m\), write
\[
Q_m(s)=\sum_{J\text{ independent}}2^{m-|J|}\prod_{j\in J}s_j.
\]
Condition on whether the last vertex is selected: \(Q_0=1\), \(Q_1=2+s_1\), and
\[
Q_m=2Q_{m-1}+2s_m Q_{m-2}\quad(m\ge2).
\tag{3}
\]
For every sign sequence, induction in blocks of four gives
\[
\begin{array}{c|c}
m\bmod4&\nu_2(Q_m)\\\hline
0& m/2\\
1&(m-1)/2\\
2&\ge m/2+1\text{, if }Q_m\ne0\\
3&(m-1)/2
\end{array}
\tag{4}
\]
with \(Q_m\ne0\) in rows \(0,1,3\). For clarity, the block step uses the successive facts
\[
\nu_2(Q_{4k})=2k,\quad\nu_2(Q_{4k+1})=2k,
\quad 2^{2k+2}\mid Q_{4k+2},\quad
\nu_2(Q_{4k+3})=2k+1.
\]
The first two claims at \(k=0\) follow from \(Q_0=1\) and odd \(Q_1=2+s_1\). The recurrence makes \(Q_{4k+2}/2^{2k+1}\) a sum of two odd integers, hence even. Its next application gives \(\nu_2(Q_{4k+3})=2k+1\), followed by \(\nu_2(Q_{4k+4})=2k+2\) and \(\nu_2(Q_{4k+5})=2k+2\), closing the induction. Zero is possible only in row \(2\).

**4. Every permitted resonance is real.** Put every sign equal to \(-1\) on a path component. Recurrence (3) has characteristic roots \(1\pm i\), giving the exact real expression
\[
Q_m(-1,\ldots,-1)=2^{m/2}\cos(m\pi/4).
\tag{5}
\]
This vanishes precisely when \(m\equiv2\pmod4\). By contrast, with all signs \(+1\), every term in \(Q_m\) is positive. Since the signs on different residual components are independent choices of \(a\), (4) and (5) prove the universal/mixed fiber dichotomy and the fixed two-adic valuation in universal fibers.

## Verification
The standalone `corona_walsh_checker.py` uses only Python's standard library. It constructs full independent-set indicators and performs separate exact-integer Walsh butterflies for every graph on up to four labelled vertices (75 graphs and 16,932 multipliers), then verifies the proposed residual graph factorization and the sharp gap. For every path length one through eight it checks the full Walsh spectrum against the asserted all-zero/universal/mixed fiber criterion and fixed two-adic orders. Finally, it tests all 131,071 sign sequences over signed path continuants of lengths zero through sixteen. Expected terminal marker: `LEAF_CORONA_WALSH_EXACT_PASS`. Finite tests corroborate, but do not replace, the induction and graph-theoretic proof.

## Relationship to prior work
The independence polynomial and its corona substitution identity are classical; the published 2013 exposition by Levit and Mandrescu contains the unsigned formula and deletion recurrence but not the present character-weighted spectral stability statement. Blažej, Dvořák and Opler (2021) employ multivariate signed independence polynomials in hat-guessing games; their investigated questions concern winning thresholds rather than Fourier-fiber cancellation or pseudoinverse norms. A published 2026 result titled *Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance* determines zeros of entries in the inverse of a **principal restricted Fourier matrix indexed by independent supports**. In particular, its ordinary homogeneous path independence polynomial at \(-1/2\) already has the mod-four resonance in (5). That is acknowledged as known: the distinct assertions here are the all-sign rigidity (4), its exact application to the full ambient Fourier spectrum of **independent sets of leaf coronas**, and the all-core-graph sharp multiplier gap. A prior analysis of \(K_h\circ (bK_1)\) supplies a clique-core special case, not arbitrary core graphs or the path-fiber classification.

## Limitations
The fiber theorem determines whether every, some, or no core frequencies vanish when the pendant frequency is fixed; it does not enumerate the zeros inside a mixed fiber or give a closed rank formula for the entire path corona. The sharp inverse norm is for \(\ell^2\) only, not endpoint projection constants. General graph structural criteria for *all* Fourier zeros are not asserted. The elementary nature of the divisibility part leaves a genuine risk of a prior equivalent vertex-cover formulation, and an earlier general multivariate-zero result could subsume parts of the path classification. Independent validation and exhaustive historical-priority verification are not asserted.

## References
- V. E. Levit and E. Mandrescu, *On f-Symmetries of the Independence Polynomial*, arXiv:1303.2564v1 (first public 2013-03-11), especially §1, Theorems 1.1–1.2, and §2. https://arxiv.org/html/1303.2564v1
- V. Blažej, P. Dvořák, and M. Opler, *Bears with Hats and Independence Polynomials*, Graph-Theoretic Concepts in Computer Science, 2021, DOI:10.1007/978-3-030-86838-3_22, §5. https://link.springer.com/chapter/10.1007/978-3-030-86838-3_22
- *Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance*, publicly indexed mathematical research result (2026-11-08), RESULT.md, especially the inverse-entry formula and path specialization. Available through the public published-finding corpus mathematics repository.
