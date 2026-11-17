# Commuting involution tuples in incidence algebras recover the comparability-graph Tutte polynomial

## Finding
Let \(P\) be an arbitrary finite poset with \(n\) elements, \(G(P)\) its undirected comparability graph, and \(m\) the number of strict comparable pairs. Let \(k=\mathbb F_q\) with \(q\) odd, and \(A=I(P,k)\) its incidence algebra. For every integer \(r\ge1\), define \(C_r(P;q)\) as the number of ordered \(r\)-tuples \((g_1,\ldots,g_r)\in A^r\) satisfying \(g_i^2=1\) for all \(i\) and \(g_ig_j=g_jg_i\) for all \(i,j\). Put \(Q=2^r\).

**Theorem.** For every such \(P,q,r\),
\[
C_r(P;q)=\sum_{\sigma:P\to\{\pm1\}^r}q^{b(\sigma)}
=\sum_{F\subseteq E(G(P))}Q^{\kappa(F)}q^{m-|F|}(1-q)^{|F|},
\]
where \(b(\sigma)\) counts strict comparable pairs with different sign-vector labels and \(\kappa(F)\) is the component count of the spanning subgraph on \(P\) with edge set \(F\). Thus the entire commuting-involution-tuple hierarchy is the \(Q\)-state Potts partition function on the comparability graph, at edge weight \((1-q)/q\), multiplied by \(q^m\).

If \(G(P)\) is a forest with \(c\) components, then
\[
C_r(P;q)=2^{rc}\bigl(1+(2^r-1)q\bigr)^m.
\]
In particular, among independently uniformly selected involutions of \(A\), the probability that \(r\) of them commute pairwise is
\[
\left(\frac{1+(2^r-1)q}{(1+q)^r}\right)^m.
\]
For all finite posets, the complete array \(\{C_r(P;q):r\ge1,\ q\text{ an odd prime power}\}\) determines \(n\), \(m\) and the full two-variable Tutte polynomial of \(G(P)\). Conversely, the graph's Tutte polynomial together with \(n\) determines this entire array. The statement is about the Tutte polynomial, not reconstruction of the graph or poset up to isomorphism.

## Assumptions and scope
The incidence algebra \(A\) has basis \(e_{xy}\) for \(x\le y\) in \(P\), with multiplication \(e_{xy}e_{uv}=\delta_{yu}e_{xv}\). Its identity is \(1=\sum_x e_{xx}\). The ideal \(J\) spanned by \(e_{xy}\) with \(x<y\) is nilpotent and has dimension \(m\). A comparability-graph edge is an unordered pair \(\{x,y\}\) with \(x<y\) or \(y<x\); it need not be a cover relation. Every comparable pair, not merely a Hasse-diagram edge, is included. Isolated vertices and disconnected posets are permitted, and \(r\) is any positive integer. Odd characteristic is essential to separate the two roots of \(z^2-1\).

## Proof
**Step 1: lift a commuting tuple to diagonal form.** Fix a commuting tuple \((g_i)_{i=1}^r\). For every sign vector \(\varepsilon\in\{\pm1\}^r\), define
\[
p_{\varepsilon}=2^{-r}\prod_{i=1}^r(1+\varepsilon_i g_i).
\]
The factors commute. Since \(g_i^2=1\), the \(p_{\varepsilon}\) are pairwise orthogonal idempotents summing to \(1\), and \(g_i=\sum_{\varepsilon}\varepsilon_i p_{\varepsilon}\). On the diagonal, each \(g_i\) has entries \(\pm1\), determining a unique coloring \(\sigma:P\to\{\pm1\}^r\). Define diagonal idempotents \(f_{\varepsilon}=\sum_{x:\sigma(x)=\varepsilon}e_{xx}\). Then \(p_{\varepsilon}\equiv f_{\varepsilon}\pmod J\). Set
\[
u=\sum_{\varepsilon}p_{\varepsilon}f_{\varepsilon}.
\]
Modulo \(J\), this is \(\sum_{\varepsilon}f_{\varepsilon}=1\); hence \(u\in1+J\) is invertible. Orthogonality gives \(p_{\varepsilon}u=p_{\varepsilon}f_{\varepsilon}=uf_{\varepsilon}\), so \(p_{\varepsilon}=uf_{\varepsilon}u^{-1}\). Therefore
\[
g_i=ud_i u^{-1},\qquad d_i=\sum_{x\in P}\sigma_i(x)e_{xx}.
\]
Conversely, every \(u\in1+J\) produces a commuting involution tuple with the same diagonal coloring. So all tuples having fixed \(\sigma\) form exactly one orbit under \(1+J\).

**Step 2: exact orbit cardinality.** The group \(1+J\) has \(q^m\) elements. Writing \(u=1+\sum_{x<y}a_{xy}e_{xy}\), the equality \(ud_i=d_iu\) for every \(i\) is equivalent to
\[
a_{xy}\bigl(\sigma_i(y)-\sigma_i(x)\bigr)=0
\qquad\text{for each strict pair }x<y\text{ and each }i.
\]
Because the characteristic is odd, this forces \(a_{xy}=0\) exactly when \(\sigma(x)\ne\sigma(y)\). All remaining coefficients are free. The stabilizer thus has cardinality \(q^{m-b(\sigma)}\), giving exactly \(q^{b(\sigma)}\) tuples with fixed coloring. Summation over all \(\sigma\) proves the first formula.

**Step 3: the subgraph expansion.** For each graph edge \(xy\), the weight \(q^{\mathbf1_{\sigma(x)\ne\sigma(y)}}\) equals \(q+(1-q)\mathbf1_{\sigma(x)=\sigma(y)}\). Expanding the product over all \(m\) edges and summing over colorings gives
\[
C_r(P;q)=\sum_{F\subseteq E(G(P))}q^{m-|F|}(1-q)^{|F|}Q^{\kappa(F)},
\]
because requiring equality of colors on the edges of \(F\) leaves \(Q\) choices on each component. No appeal to unproved combinatorial identities is required.

**Step 4: forests and probability.** If \(G(P)\) is a forest, assign a color to one root of each component in \(Q\) ways and extend it along each edge. Each new vertex can match its parent (weight \(1\)) or take one of \(Q-1\) other colors (total weight \((Q-1)q\)). This yields \(Q^c(1+(Q-1)q)^m\). For \(r=1\), the total number of involutions is \(2^c(1+q)^m\). Dividing the \(r\)-tuple count by the \(r\)-th power of this total establishes the stated probability.

**Step 5: what the invariant determines.** Regard the graph expansion as a polynomial \(W_G(Q,q)\) in two independent indeterminates. For each fixed odd prime power \(q\), knowing its values at \(Q=2,4,8,\ldots\) uniquely determines the polynomial in \(Q\). Values at infinitely many odd prime powers then uniquely determine every coefficient as a polynomial in \(q\). Since \(G\) has no loops, the coefficient of \(Q^n\) in \(W_G\) is exactly \(q^m\) (only the empty subset has \(n\) components); hence \(n\) and \(m\) are determined. Define the standard random-cluster polynomial
\[
Z_G(Q,v)=\sum_{F\subseteq E(G)}Q^{\kappa(F)}v^{|F|}.
\]
The identity \(W_G(Q,q)=q^m Z_G(Q,(1-q)/q)\) is an invertible rational substitution: \(Z_G(Q,v)=(1+v)^m W_G(Q,1/(1+v))\). Thus the array recovers \(Z_G\), and therefore the standard Tutte polynomial via
\[
T_G(x,y)=\sum_{F\subseteq E(G)}(x-1)^{\kappa(F)-\kappa(G)}(y-1)^{|F|-n+\kappa(F)}.
\]
Conversely, \(n\) and \(T_G\) recover \(m\), \(Z_G\), \(W_G\), and all \(C_r(P;q)\). This finishes the proof.

## Verification
A dependency-free Python checker independently constructs the incidence-algebra multiplication table, enumerates involutions by testing their actual squares, checks pairwise products for all ordered tuples in seven test configurations, and independently calculates the coloring and subgraph expansions. It tests nonzero radical products in the three-element chain and four-element diamond, as well as a fork, disconnected poset, and two-element chain over fields of size \(3\) and \(5\). The checker also checks \(r=3\), not only pairs. Execute `python checker.py`; the exact recorded output is in `checker_output.txt`. All cases matched. This finite evidence is a check of the proof, not an exhaustive test of all posets, fields, or tuple lengths.

## Relationship to prior work
R. Słowik's *Involutions in triangular groups* (2013; DOI below) classifies individual involutions of full triangular groups. I. Gargate and M. Gargate's *Involutions on Incidence Algebras of Finite Posets* (first public July 16, 2019) gives counts and methods for individual involutions in incidence algebras; the \(r=1\) case here is not claimed original. D. Quinn's 2015 preprint develops incidence algebras of posets as quiver quotients. A. D. Sokal's 2005 survey presents the established Fortuin–Kasteleyn/Potts/Tutte identity; the graph-polynomial identity itself is not claimed original. The proposed new connection is the **simultaneous pairwise-commuting tuple orbit count for all \(r\)**, its extension to arbitrary posets with nonzero higher radical products, and the equivalence with Tutte-polynomial data. Standard conjugacy of idempotent liftings supplies part of the mechanism, so an unidentified earlier representation-count theorem could subsume the result.

## Limitations
The field must have odd characteristic. The count concerns labeled ordered commuting tuples of algebra elements satisfying \(g_i^2=1\), not conjugacy classes, anti-automorphisms, or all finite-group representations. It recovers only the comparability-graph Tutte polynomial and vertex count, not the poset or comparability graph itself. For \(r=1\), the underlying individual-involution count is covered by earlier literature; the Fortuin–Kasteleyn subgraph formula and its forest evaluation are classical. The primary novelty claim is the incidence-algebra realization of the full \(r\)-tuple hierarchy and its invariant consequence. A broader general theorem on finite-group homomorphisms into triangular algebra unit groups may imply it; independent assessment of historical priority has not been performed.

## References
1. Alan D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1, first public March 25, 2005, https://arxiv.org/abs/math/0503607.
2. David Quinn, *The incidence algebras of posets and acyclic categories*, arXiv:1501.02481v1, first public January 11, 2015, https://arxiv.org/abs/1501.02481.
3. Roksana Słowik, *Involutions in triangular groups*, Linear and Multilinear Algebra 61 (2013), 909–916, DOI:10.1080/03081087.2012.716432. Earliest online appearance not independently established in this package.
4. Ivan Gargate and Michael Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805v1, first public July 16, 2019, https://arxiv.org/abs/1907.06805.
5. Takahide Adachi, *Characterizing τ-rigid-finite algebras with radical square zero*, arXiv:1401.1438v1, first public January 7, 2014, https://arxiv.org/abs/1401.1438. Context for neighboring quiver algebra classifications, not a claim about commuting involutions.
