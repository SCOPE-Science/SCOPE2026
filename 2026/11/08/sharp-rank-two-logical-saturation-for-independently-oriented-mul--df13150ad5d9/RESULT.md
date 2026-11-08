# Sharp rank-two logical saturation for independently oriented multitournaments

## Finding
For each integer \(k\geq1\), let \(q=2^k\). A **\(k\)-multitournament** is a finite nonempty set \(V\) equipped with \(k\) strict tournament relations \(R_1,\ldots,R_k\). For distinct vertices \(u,v\), the **orientation signature** \(\sigma(u,v)\in\{0,1\}^k\) records whether \(R_i(u,v)\) holds in each coordinate. Thus \(\sigma(v,u)=\mathbf1-\sigma(u,v)\). Define its local signature set and its set of local profiles by
\[
S(u)=\{\sigma(u,v):v\in V\setminus\{u\}\},\qquad
\mathcal P(V)=\{S(u):u\in V\}.
\]

**Theorem (exact profile, minimum model, and random window).**

1. For any two finite \(k\)-multitournaments \(A,B\), their first-order theories agree on **every sentence of quantifier rank at most two** if and only if \(\mathcal P(A)=\mathcal P(B)\).
2. Write \(\mathsf{Sat}_k\) for the rank-two sentence asserting that every vertex has a neighbor of every orientation signature. The least size of a finite model of \(\mathsf{Sat}_k\) is exactly \(q+1\), and an explicit model of this size has each signature exactly once around each vertex.
3. Independently orient each unordered pair of \(n\) labeled vertices in each of the \(k\) relations with equal probability. Let \(Z_{n,k}\) be the number of vertices missing at least one signature, and let
\[
p_{n,q}=\sum_{j=1}^q(-1)^{j+1}{q\choose j}\left(1-\frac jq\right)^{n-1}.
\]
Then \(\mathbb EZ_{n,k}=np_{n,q}\), and the indicators that **two distinct vertices** are deficient are exactly pairwise independent for every \(n\geq2\). In particular,
\[
\operatorname{Var}Z_{n,k}=np_{n,q}(1-p_{n,q}).
\]
If \(np_{n,q}\to0\), then \(\Pr(\mathsf{Sat}_k)\to1\); if \(np_{n,q}\to\infty\), then \(\Pr(\mathsf{Sat}_k)\to0\). For each fixed \(k\), the first alternative holds as \(n\to\infty\).
4. In the growing-vocabulary regime \(k\to\infty\), \(q=2^k\), and
\[
\frac nq=2\log q+\log\log q+c+o(1),\qquad c\in\mathbb R,
\]
we have
\[
Z_{n,k}\xrightarrow{\mathrm d}\operatorname{Poisson}(2e^{-c}),
\qquad
\boxed{\Pr(\mathsf{Sat}_k)\longrightarrow\exp(-2e^{-c}).}
\]
The logarithms are natural. The constant \(2\) arises from simultaneous coverage of all signatures at **every** vertex, rather than coverage at one distinguished vertex.

## Assumptions and scope
All structures are finite, nonempty, and interpreted in the pure relational vocabulary \(R_1,\ldots,R_k\) with equality, without auxiliary constants, vertex colors, counting quantifiers, or an order. Each \(R_i\) is irreflexive and, for distinct \(u,v\), exactly one of \(R_i(u,v)\), \(R_i(v,u)\) holds. The number \(k\) is fixed when comparing structures or sentences, but may grow with \(n\) in the probabilistic statement. The random relations are mutually independent uniform tournaments, so the signatures of distinct unordered pairs are independent uniform \(q\)-valued samples in either chosen orientation. Convergence in distribution in part 4 concerns the integer-valued count \(Z_{n,k}\). For \(n=1\), there is one deficient vertex; pairwise independence is only asserted for \(n\geq2\).

The sentence \(\mathsf{Sat}_k\) can be written explicitly. For \(a\in\{0,1\}^k\), put
\[
\tau_a(x,y)=(x\ne y)\ \land\bigwedge_{i:a_i=1}R_i(x,y)\ \land\bigwedge_{i:a_i=0}R_i(y,x).
\]
Then \(\mathsf{Sat}_k=\bigwedge_{a\in\{0,1\}^k}\forall x\exists y\,\tau_a(x,y)\) has quantifier rank two. Its formula length grows with \(k\); no uniform fixed-language first-order limit assertion is made for growing \(k\).

## Proof
**(1) Two-round Ehrenfeucht–Fraïssé classification.** A one-point configuration has no nontrivial atomic relation. After Spoiler chooses a vertex \(u\) in either structure, Duplicator can answer with \(u'\) having the same set \(S(u)=S(u')\) precisely when the two structures have the same collection of local profiles. At the second round, a repeated vertex is matched by repetition; a distinct vertex of signature \(a\) is matched by a distinct vertex of signature \(a\). This preserves all atomic formulas on the chosen pair. Conversely, if a local profile occurs in one structure and not the other, Spoiler selects a vertex having that profile, then selects a second vertex in the structure witnessing a signature belonging to the symmetric difference of the two selected profiles. Duplicator cannot preserve the two-point atomic type. The two-round game theorem gives the stated equivalence for all rank-at-most-two sentences.

**(2) Sharp finite representative.** Each vertex has \(n-1\) distinct other vertices, so realizing all \(q\) signatures requires \(n\geq q+1\). To attain equality, put \(n=q+1=2s+1\) and identify the vertices with \(\mathbb Z/n\mathbb Z\). The complete graph is partitioned into the \(s\) undirected two-factors whose edges are \(\{i,i+d\}\) for \(d=1,\ldots,s\) and \(i\in\mathbb Z/n\mathbb Z\). Orient each two-factor by the rule \(i\to i+d\). For each \(d\) choose one of the \(s\) complementary pairs \(\{a,\mathbf1-a\}\) of binary signatures, and assign \(a\) to the oriented edge and \(\mathbf1-a\) to its reverse. Since every vertex has exactly one incoming and one outgoing edge in each two-factor, it sees every binary signature exactly once. Reading each bit as a tournament orientation realizes \(\mathsf{Sat}_k\) at the claimed minimum size.

**(3) Exact pairwise independence and the general regimes.** The \(n-1\) signatures incident to one fixed vertex are independent and uniform on \(q\) possible values. Inclusion–exclusion for missing coupons gives exactly \(p_{n,q}\). For distinct vertices \(u,v\), condition on the signature of their shared edge. All remaining edge signatures incident to \(u\) and \(v\) come from disjoint unordered edges and are independent. The conditional probability that \(u\) misses a signature is independent of the value of the conditioned signature because all \(q\) signatures play symmetric roles. It equals the unconditional value \(p_{n,q}\), and the same is true for \(v\). Hence the two deficiency events are independent, without an approximation. The variance formula follows. The union bound gives \(\Pr(Z_{n,k}>0)\le np_{n,q}\), whereas Chebyshev's inequality gives \(\Pr(Z_{n,k}=0)\le (np_{n,q})^{-1}\) when the mean is positive. For fixed \(q\), \(p_{n,q}\le q(1-1/q)^{n-1}\), so \(np_{n,q}\to0\).

**(4) Critical Poisson limit.** Write \(L=\log q\) and \(m=n-1\). In the stated window, a specified signature is absent from one vertex with probability
\[
a_q=(1-1/q)^m=\frac{e^{-c+o(1)}}{q^2L}.
\]
The probability that two specified distinct signatures are both absent is
\[
b_q=(1-2/q)^m=\frac{e^{-2c+o(1)}}{q^4L^2}.
\]
The first two Bonferroni bounds imply \(p_{n,q}=qa_q(1+o(1))\), since \(q^2b_q/(qa_q)\to0\). Therefore \(np_{n,q}\to2e^{-c}\).

For any fixed \(r\geq1\), choose \(r\) distinct vertices and condition on the signatures of all edges among them. Vertex \(i\) has already seen at most \(r-1\) signatures internally; its remaining \(n-r\) signatures are independent uniform draws, and these sets of outside draws are independent for the \(r\) selected vertices. Uniformly over every assignment of internal signatures, Bonferroni bounds give the conditional deficiency probability
\[
(q-t_i)(1-1/q)^{n-r}+O\bigl(q^2(1-2/q)^{n-r}\bigr)
=qa_q(1+o(1)),\qquad 0\le t_i\le r-1.
\]
The big-O estimate is uniform in the internal assignment because \(r\) is fixed. Taking products and averaging shows
\[
\Pr(\text{the specified }r\text{ vertices are deficient})
=(qa_q)^r(1+o(1)).
\]
Consequently the factorial moments satisfy
\[
\mathbb E(Z_{n,k})_{\underline r}=(n)_{\underline r}(qa_q)^r(1+o(1))\longrightarrow(2e^{-c})^r.
\]
The factorial-moment characterization of the Poisson law yields convergence in distribution and, since the variables are integer valued, convergence of the probability at zero.

## Verification
The accompanying standard-library Python script `checker.py` constructs the optimal saturated model for \(k=1,\ldots,6\), checks every one of its local signatures, and exhaustively enumerates finite multi-tournaments for \(k=1\) on \(n=2,3,4,5\) and \(k=2\) on \(n=2,3,4\). It compares exact deficiency frequencies and pairwise frequencies with the rational inclusion–exclusion formulas. It also witnesses failure of three-way independence at \(k=1,n=3\). Run `python checker.py`; the checked script prints `ALL_CHECKS_OK`. These finite tests do not constitute proof of the general combinatorial construction, the all-size independence identity, or the limiting Poisson theorem; those follow from the arguments above.

## Relationship to prior work
The two-round game argument is an application of the standard Ehrenfeucht–Fraïssé theorem, the two-factor decomposition is elementary, and coupon collection, inclusion–exclusion, and the factorial-moment Poisson method are classical. None of those ingredients is asserted to be new. The specific result connects an exact rank-two invariant of **independent families of tournament relations** to its optimal finite representative, an exact pairwise-independence phenomenon, and a growing-vocabulary Poisson window with its explicit constant.

Jeż, Michaliszyn, and Witkowski's 2026 work studies finite satisfiability for an arbitrary number of linear-order **successor** relations, where each relation is a spanning directed path. Its local adjacency masks and finite-model methods motivate attention to multiple independent binary relations, but its theorem does not cover complete tournament relations or a random rank-two saturation law. Work on random edge-coloured graphs by Simonovits and Sós studies fixed-color Ramsey-type threshold properties, not the local full-signature coupon-coverage statement with a growing number of colors. These distinctions do not establish absolute historical priority; earlier results on colored complete graphs or symmetric random relational structures might imply part or all of the present theorem.

## Limitations
The claim concerns rank at most two, **not** full first-order equivalence. The distributional theorem allows the signature vocabulary to grow, and therefore does not say that a single fixed formula has a nontrivial limiting probability in a fixed vocabulary. The nearest comparable prior literature was checked to the extent described in the accompanying review; a general theorem about highly dependent coupon collectors or edge-colored complete graphs could subsume the probabilistic part. No independent mathematical validation or priority certification has been performed.

## References
1. Artur Jeż, Jakub Michaliszyn, and Piotr Witkowski, *Finite Satisfiability of Two-Variable Logic with Arbitrarily Many Successors*, arXiv:2610.19943v1, initially public 14 October 2026. https://arxiv.org/html/2610.19943v1
2. Miklós Simonovits and Vera T. Sós, *A hierarchy of randomness for graphs*, Discrete Mathematics **303** (2005), 209–233. https://doi.org/10.1016/j.disc.2004.12.024
3. Ehrenfeucht–Fraïssé game theorem; elementary two-factorization of odd-order complete graphs; standard coupon-collector inclusion–exclusion and Poisson factorial-moment principle (classical tools, invoked with full calculations above).
