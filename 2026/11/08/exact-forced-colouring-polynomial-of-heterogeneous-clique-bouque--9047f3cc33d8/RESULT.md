# Exact forced-colouring polynomial of heterogeneous clique bouquets

## Finding
Let \(r\ge2\), let \(a_1,\ldots,a_r\) be positive integers, and form the clique bouquet
\[
G=K_1\vee\left(\bigsqcup_{i=1}^r K_{a_i}\right).
\]
Thus a single hub is adjacent to every vertex in \(r\) pairwise nonadjacent clique blades. Put \(s=\max_i a_i\), \(t=|\{i:a_i=s\}|\), \(B=\sum_{a_i<s}a_i\), and
\[
L=\prod_{a_i<s}(s)_{a_i},\qquad
L_-=\prod_{a_i<s}(s-1)_{a_i},
\]
with \((u)_v=u(u-1)\cdots(u-v+1)\) and empty products equal to one. Use the named palette of exactly \(\lambda=s+1=\chi(G)\) colours. Write \(F_G(x)=\sum_f x^{|\operatorname{dom}f|}\), where the sum is over all proper partial \(\lambda\)-assignments that **eventually force** a full proper \(\lambda\)-colouring by the local rule: an uncoloured vertex is coloured when its already coloured neighbours exhibit exactly \(\lambda-1\) distinct colours, in which case it receives the unique missing colour.

For every such clique bouquet, the complete domain-size generating polynomial is
\[
\boxed{F_G(x)=(s+1)(s!)^t x^{B+t(s-1)}\bigl[L(1+x)(s+x)^t-sL_-\bigr].}
\]
In particular, for \(s\ge2\), the smallest forcing domain has exactly
\[
\boxed{h=B+t(s-1)}
\]
vertices, and the number of forcing partial assignments of that smallest size is
\[
\boxed{(s+1)(s!)^t\bigl(s^tL-sL_-\bigr).}
\]
For \(s=1\), the graph is a star and \(F_G(x)=2((1+x)^{r+1}-1)\); the minimum size is one, with \(2(r+1)\) assignments. All colours and vertices are distinguished.

For \(0\le p\le 1/(s+1)\), define \(q=1-(s+1)p\). In the independent random partial-assignment model, each named colour has probability \(p\) at a vertex and leaving the vertex blank has probability \(q\). The corresponding forcing probability is
\[
\boxed{\operatorname{FC}_{s+1}(G;p)=(s+1)(s!)^t p^{B+t(s-1)}
\bigl[L(q+p)(sq+p)^t-sL_-q^{t+1}\bigr].}
\]
The total number of successful partial assignments is
\[
F_G(1)=(s+1)(s!)^t\bigl[2L(s+1)^t-sL_-\bigr].
\]

## Assumptions and scope
All graphs are finite, simple, and labelled. There are at least two nonempty blades. The hub is a specified vertex. A blade of size \(a_i\) is complete, and distinct blades have no edges between them. The formula uses the chromatic palette size exactly, not a larger palette. The forcing predicate is iterative local forcing, not mere existence or uniqueness of a proper extension. Each partial assignment counts once, independent of the order of legal forcing steps. If there is no small blade, both products defining \(L,L_-\) equal one.

## Proof
**1. Proper completed colourings.** Because some blade has \(s\) vertices, the hub together with that blade is a clique of size \(s+1\), so the chromatic number is \(s+1\). In any proper colouring \(\phi\) with exactly these \(s+1\) named colours, the hub receives one colour. Each maximum-size blade uses each of the other \(s\) colours exactly once, yielding \(s!\) options independently per maximum blade. A blade with \(a_i<s\) receives an injection into these \(s\) remaining colours, yielding \((s)_{a_i}\) options. Hence the total number of completed colourings is \((s+1)(s!)^t L\).

**2. Initial seeds required inside blades.** Fix a completed colouring \(\phi\). An outer vertex in a smaller blade has degree \(a_i\le s-1\), so it cannot be forced under the rule requiring \(s\) neighbour colours; it must be coloured initially. An outer vertex in a maximum blade has degree exactly \(s\). Because its \(s\) neighbours have pairwise distinct colours under \(\phi\), this vertex can be forced precisely when its hub neighbour and all other vertices of its own blade are already coloured. Thus at most one vertex per maximum blade can initially be blank. Conversely, after the hub is coloured, every such isolated blank is forced.

**3. When the hub is initially coloured.** For each fixed \(\phi\), the smaller blades contribute \(x^B\), while each maximum blade can have zero or one initially blank vertex and therefore contributes \(x^s+s x^{s-1}=x^{s-1}(x+s)\). The hub contributes \(x\). So all hub-seeded forcing restrictions have generating polynomial
\[
x^{B+t(s-1)}x(s+x)^t
\]
per fixed completed colouring.

**4. When the hub is initially blank.** Until the hub is coloured, no blank outer vertex can be forced: smaller-blade vertices are unforceable and a blank vertex in a maximum blade needs the hub already coloured. Therefore the hub can be forced if and only if the initially coloured outer vertices collectively exhibit all \(s\) other palette colours. Under the restrictions from step 2, if any maximum blade is fully seeded, this is automatic. Otherwise every maximum blade has one blank vertex; in a fixed \(\phi\), the only bad choices are those in which every maximum blade's blank vertex has the same colour \(c\) and no smaller blade contains colour \(c\). For each colour absent from all smaller blades there is exactly one such bad choice. Denote the union of colours used on the smaller blades under \(\phi\) by \(U(\phi)\). The hub-unseeded good restrictions consequently contribute
\[
x^{B+t(s-1)}\bigl[(s+x)^t-(s-|U(\phi)|)\bigr].
\]
If the hub sees all \(s\) colours it is immediately forced to its colour in \(\phi\); then each remaining blank in a maximum blade is forced. This proves sufficiency, not just necessity.

**5. Sum the completed colourings without overcounting.** For a fixed hub colour and fixed colour permutations in the maximum blades, the smaller blades have \(L\) joint proper colourings. Also,
\[
\sum_{\phi_{\mathrm{small}}}(s-|U(\phi)|)
=\sum_{c=1}^{s}\#\{\phi_{\mathrm{small}}:c\notin U(\phi)\}
=s\prod_{a_i<s}(s-1)_{a_i}=sL_-.
\]
Adding the hub-seeded and hub-unseeded cases, multiplying by the \(s+1\) hub colours and \((s!)^t\) maximum-blade permutations, yields precisely the boxed formula. Every forcing partial assignment has a uniquely determined completed colouring: each legal forcing step adds its only possible colour, and a successful process colours every vertex. Hence counting restrictions by completed colouring does not overcount.

**6. Smallest domain and probability transformation.** Put \(h=B+t(s-1)\). For \(s\ge2\), the constant coefficient in the bracket is \(s^tL-sL_-\). It is positive when \(t\ge2\), since \(s^t>s\) and \(L\ge L_-\). When \(t=1\), there must be a smaller nonempty blade because \(r\ge2\); then \(L>L_-\) and the constant is again positive. Therefore the smallest exponent is exactly \(h\), with the stated multiplicity. For \(s=1\), all blades are singleton leaves, and direct substitution gives the stated star polynomial. Finally \(|V(G)|=1+B+st\) and
\[
\operatorname{FC}_{s+1}(G;p)=q^{|V(G)|}F_G(p/q).
\]
Substitution and cancellation of powers of \(q\) give the displayed probability polynomial, valid as a polynomial identity also when \(q=0\).

## Verification
The standalone `artifacts/verify.py` builds the labelled graph explicitly and enumerates all partial assignments for twenty-one small blade vectors, independently applying the local forcing rule. It compares the resulting complete coefficient dictionaries to the closed expression. Checks include \((2,2)\), \((2,2,2)\), \((3,3)\), \((3,2,1)\), and \((3,3,1)\), as well as the star boundary. Additional algebraic checks cover \(2\le s\le14\), \(1\le t\le6\), and \(1\le a<s\) for a maximum-blade vector augmented by one smaller blade; these check the minimum-exponent formula and the total count. To reproduce, execute `python3 artifacts/verify.py` from a directory containing the extracted artifact. The program prints `VERIFY_OK` on success. These finite checks are corroboration, not an infinite proof.

## Relationship to prior work
Farr and Morgan introduced the forced-colouring function for partial colourings, and Farr's September 2026 work develops its general framework, special values, small-graph examples, and computational hardness; neither inspected primary text contains the heterogeneous clique-bouquet polynomial. Farr's paper gives the complete graph as a small-family case, which the present proof uses as a boundary rather than claiming as new. Related exact results for chromatic-palette forcing on complete multipartite graphs and for forced three-colouring on graphs of maximum degree at most two do not imply this theorem: clique bouquets with multiple nontrivial blades are neither complete multipartite nor of maximum degree at most two, and the local seed constraints differ. The present enumeration provides the arbitrary blade-size multiset, not just equal-size friendship graphs. Relevant published searches and matching-parameter comparisons found no stronger covering formula; unindexed equivalent results remain a historical-priority risk.

## Limitations
The theorem does not give a formula with more than \(\chi(G)\) available colours, or for block graphs whose clique blocks meet along several articulation vertices. The family consists of clique blades meeting at one common hub, not arbitrary chordal or block graphs. The computational checks are finite and are not proof for all sizes. Priority remains provisional; no independent mathematical audit has been performed.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first publicly submitted 15 September 2026, https://arxiv.org/abs/2609.17108.
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1, 22 June 2024, https://arxiv.org/abs/2406.15746.
3. *Forced colourings of complete multipartite graphs at the chromatic palette size*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-forced-colourings-of-complete-multipartite-graphs-at-the-chromat--ab08eebc2655.
4. *Exact forced 3-colouring polynomials at maximum degree two*, public research result, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd.
