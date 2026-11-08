# Counting longest total-dominating sequences in \(\operatorname{KG}(n,2)\)

## Finding
For each integer \(n\ge5\), let \(G_n=\operatorname{KG}(n,2)\), whose vertices are the two-element subsets of \([n]\), with adjacency meaning disjointness. A *legal open-neighborhood sequence* is an ordered tuple \((e_1,\ldots,e_k)\) of distinct vertices such that, for every \(i\), some vertex is adjacent to \(e_i\) and to none of \(e_1,\ldots,e_{i-1}\). If the tuple totally dominates \(G_n\), it is a total-dominating sequence. A *longest* such sequence has length six (the known Grundy total domination number, reproved below).

**Theorem.** The number \(A(n)\) of ordered longest total-dominating sequences, with the six positions distinguished, is
\[
\boxed{A(n)=720\binom n4+33120\binom n5+257040\binom n6+655200\binom n7+624960\binom n8+181440\binom n9.}
\]
As usual, \(\binom nt=0\) when \(t>n\). Every such sequence uses at most nine distinct underlying ground elements, and sequences using exactly nine occur for every \(n\ge9\). Thus the polynomial has degree nine, even though a six-term sequence could a priori use twelve ground elements. In particular, \(A(5)=36\,720\), \(A(6)=466\,560\), \(A(7)=3\,175\,200\), \(A(8)=14\,968\,800\), and \(A(9)=55\,248\,480\).

## Assumptions and scope
The ground set has individually named labels \(1,\dots,n\), the vertices of \(G_n\) are unordered two-subsets, and sequences are ordered and must contain six distinct graph vertices. The theorem counts neither unordered sets nor sequences modulo graph automorphisms. It covers every integer \(n\ge5\), without extrapolation from finitely many ground-set sizes. The classification is finite because each sequence contains six two-subsets.

## Proof
**Step 1 (witness-cover equivalence).** Identify each graph vertex with an edge of the complete graph on \([n]\). For \(i>1\), a vertex \(f\) of \(G_n\) is adjacent to \(e_i\) but to none of its predecessors exactly when the pair \(f\) is disjoint from \(e_i\) and meets every preceding edge. Equivalently, the edge family \(e_1,\ldots,e_{i-1}\) has a vertex cover of size at most two, using no endpoint of \(e_i\). To justify the phrase "at most": if a one-point cover exists, it can be padded to a two-point cover avoiding \(e_i\) because \(n\ge5\). If a witness includes an unused ground element, its other element alone covers all preceding edges; conversely a two-point cover supplies the witness directly. The first step is legal for \(n\ge5\). After six steps, the chosen vertices totally dominate \(G_n\) exactly when the six selected edges have no vertex cover of size at most two.

**Step 2 (the known maximum length, with a direct upper-bound proof).** For any legal sequence of length \(k\), choose for each \(e_i\) a witnessing two-set \(f_i\). Then \(e_i\cap f_i=\varnothing\) and \(e_j\cap f_i\ne\varnothing\) for every \(j<i\). Choose pairwise distinct scalars \(t_x\) for all ground labels and let \(v_x=(1,t_x,t_x^2,t_x^3)\in\mathbb Q^4\). Any four of these vectors are linearly independent (Vandermonde determinant). Set \(\alpha_i=\bigwedge_{x\in e_i}v_x\) and \(\beta_i=\bigwedge_{x\in f_i}v_x\), each in \(\Lambda^2\mathbb Q^4\). Then \(\alpha_i\wedge\beta_i\ne0\), while \(\alpha_j\wedge\beta_i=0\) for \(j<i\). The \(\alpha_i\) are linearly independent: in any nonzero relation choose the largest index \(i\) with a nonzero coefficient and wedge the relation with \(\beta_i\). Therefore \(k\le\dim\Lambda^2\mathbb Q^4=6\). Conversely, take all six two-subsets of one fixed four-element ground set in any order. Each new two-subset is disjoint from its complementary pair, which meets each preceding, different two-subset of the four-set. After six selections, every two-subset of \([n]\) is disjoint from at least one selected two-subset. Hence the maximum equals six. This also independently verifies the previously published exact maximum.

**Step 3 (a complete finite pattern reduction).** At each stage, give ground elements labels \(0,1,\ldots,t-1\) in first-appearance order. The first edge is \((0,1)\). A subsequent unordered edge is either a pair of earlier labels, a pair \((a,t)\) with one new label, or the pair \((t,t+1)\) with two new labels. Exclude duplicates. The witness-cover equivalence is a local test on the existing edge list, and the final absence of a two-cover is another local test. Consequently the recursive generator in `verify_canonical.py` exhausts all patterns of six distinct selected edges, without reference to \(n\), provided the later label injections exist. This is a finite complete search, not an assumption about all graphs based on small examples.

Let \(t\) be the number of introduced labels and let \(q\) be the number of edges introducing *two* new labels (including the first edge). Every fixed pattern has \((n)_t=n(n-1)\cdots(n-t+1)\) injective assignments of its abstract ground labels to \([n]\). In the union over patterns each concrete ordered sequence occurs exactly \(2^q\) times: only the relative order of the two new labels at each simultaneous two-label introduction can vary. Hence a pattern contributes \((n)_t/2^q\). This accounts for the unordered nature of each selected graph vertex.

The complete recursive enumeration gives the following histogram, where the third entry is the number of patterns \(h_{t,q}\):

| \(t\) | \(q\) | \(h_{t,q}\) |
|---:|---:|---:|
|4|1|48|
|4|2|24|
|5|1|432|
|5|2|240|
|6|1|504|
|6|2|408|
|6|3|24|
|7|1|112|
|7|2|264|
|7|3|64|
|8|2|48|
|8|3|28|
|9|3|4|

All 2,200 generated six-edge patterns pass the final domination test. No pattern has \(t>9\). Therefore
\[
 A(n)=\sum_{t,q}h_{t,q}\,\frac{(n)_t}{2^q}
 =\sum_{t=4}^{9}\left(t!\sum_q\frac{h_{t,q}}{2^q}\right)\binom nt,
\]
which simplifies to the stated formula. The four patterns with \((t,q)=(9,3)\) prove that support nine occurs for every \(n\ge9\).

**Step 4 (an independent exhaustive partition proof).** The separate program `verify_endpoint_partitions.py` enumerates restricted-growth strings for the *twelve oriented endpoint positions*, not the unordered-edge first-appearance generator. Each concrete unordered six-edge sequence corresponds to exactly \(2^6=64\) oriented endpoint lists. The program independently obtains the support-count histogram
\[
 (h_4,h_5,h_6,h_7,h_8,h_9)=(1920,17664,22848,8320,992,32).
\]
Thus \(A(n)=\sum_{t=4}^{9}h_t(n)_t/64\), again giving the six coefficients. This second enumeration uses a distinct exhaustive representation and independent cover predicate. The finite checks support the exact all-order statement because every candidate six-edge sequence has only twelve endpoint slots, represented without omission by the restricted-growth recursion.

## Verification
Run the three included programs with Python 3 (standard library only):

```sh
python3 verify_canonical.py
python3 verify_endpoint_partitions.py
python3 verify_labelled.py
```

All were executed successfully using the package files, with recorded output in the corresponding `_output.txt` files. The first program checks the entire \((t,q)\) histogram, its 2,200 leaves, and the formula. The second checks all 51,776 oriented endpoint partitions and recomputes the formula independently. The third directly enumerates sequences using the graph's adjacency predicate for \(n=5,6,7,8\), obtaining respectively \(36\,720\), \(466\,560\), \(3\,175\,200\), \(14\,968\,800\). The extended mode `python3 verify_labelled.py --extended` additionally checks \(n=9\), which was executed during investigation but is not required for the proof. The general argument is the finite-pattern bijection, not numerical interpolation.

As a consequence, if six distinct vertices are drawn uniformly in a random order without replacement from \(G_n\), the probability of a longest total-dominating sequence equals \(A(n)/(\binom n2)_6\), and is asymptotic to \(32/n^3\). This gives a quantitative rarity statement for optimal greedy procedures.

## Relationship to prior work
Brešar, Henning and Rall (arXiv:1601.07525v1, 27 January 2016) introduced and studied total-dominating sequences. Brešar, Kos and Torres (2019, Proposition 4.2) proved the exact maximum length \(\gamma^t_{\mathrm{gr}}(\operatorname{KG}(n,r))=\binom{2r}{r}\); for \(r=2\), that is six. The latter result and its six-subsets-of-four construction are explicitly treated as known. The present theorem instead enumerates *all ordered maximum sequences*, including those spanning five through nine ground elements, and gives their full labelled support distribution. The known six-subsets-of-four construction accounts only for the first summand \(720\binom n4\), not for the other five summands. Searches did not locate a previously published exact counting polynomial; this is limited evidence, not proof of historical priority.

## Limitations
The theorem concerns \(r=2\) Kneser graphs only and counts ordered legal open-neighborhood sequences, not maximum independent sets, zero-forcing sets, or un-ordered total dominating sets. The proof's finite part relies on auditable exhaustive enumeration; readers should independently replay and inspect the two algorithms. No independent external audit or historical priority certification has been performed. Search coverage is not exhaustive across unpublished or unindexed material.

## References
1. B. Brešar, M. A. Henning and D. F. Rall, "Total Dominating Sequences in Graphs," arXiv:1601.07525v1 (first posted 2016-01-27), https://arxiv.org/abs/1601.07525.
2. B. Brešar, T. Kos and P. D. Torres, "Grundy domination and zero forcing in Kneser graphs," *Ars Mathematica Contemporanea* **17** (2019), 419–430, https://doi.org/10.26493/1855-3974.1881.384; especially Section 4 and Proposition 4.2.
