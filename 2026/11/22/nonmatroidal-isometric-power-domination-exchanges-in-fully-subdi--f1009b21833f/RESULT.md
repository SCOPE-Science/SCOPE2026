# Nonmatroidal isometric power-domination exchanges in fully subdivided cliques

## Finding

Let \(n\ge 3\) and let \(H_n\) be the *full one-subdivision* of the complete graph \(K_n\): it has original vertices \([n]\) and subdivision vertices \(s_{uv}\), one for every unordered pair \(\{u,v\}\subseteq[n]\), joined only to \(u\) and \(v\). Under the usual power-domination rule (one closed-neighborhood observation step, followed by forcing from an observed vertex with exactly one unobserved neighbor), the following statements hold.

**Forest criterion and all-set enumerator.** For any initially chosen vertices \(S=A\cup\{s_e:e\in B\}\), with \(A\subseteq[n]\) and \(B\subseteq\binom{[n]}2\), put \(R=[n]\setminus A\). Then \(S\) power dominates \(H_n\) **if and only if**
\[
  F_S=\left(R,\binom R2\setminus B\right)
\]
is a forest, including the empty forest. Write \(N_j=\binom j2\), and let \(f_{r,k}\) count labeled forests on \([r]\) having exactly \(k\) edges (\(f_{0,0}=f_{1,0}=1\)). The complete power-domination polynomial, counting all successful initial *vertex sets* by cardinality, is
\[
  \mathcal P(H_n;z)=\sum_{r=0}^n \binom nr z^{n-r}(1+z)^{N_n-N_r}
                 \sum_{k=0}^{\max(0,r-1)}f_{r,k}z^{N_r-k}.
\]
Equivalently, the inner forest coefficients are given by the labeled-tree exponential formula
\[
  \sum_{r\ge0}\frac{t^r}{r!}\sum_k f_{r,k}u^k
   =\exp\!\left(\sum_{j\ge1}\frac{j^{j-2}}{j!}t^j u^{j-1}\right),
\]
with the singleton convention \(1^{-1}=1\).

**Complete minimum-set classification.** For every \(n\ge3\),
\[
 \gamma_P(H_n)=n-2,\qquad |\mathcal B_n|=\frac{n(n-1)^2}{2}.
\]
The complete set \(\mathcal B_n\) of minimum power-dominating vertex sets consists exactly of two disjoint types:

* Type \(A(U)=[n]\setminus U\), where \(U\subseteq[n]\) has cardinality two; there are \(\binom n2\) such sets.
* Type \(B(V,e)=([n]\setminus V)\cup\{s_e\}\), where \(V\subseteq[n]\) has cardinality three and \(e\subset V\) has cardinality two; there are \(3\binom n3\) such sets.

**Nonmatroidal isometric exchange theorem.** Let \(\mathcal R_n\) join two members of \(\mathcal B_n\) when one initially chosen graph vertex can be replaced by another while remaining minimum power dominating. For every \(S,T\in\mathcal B_n\),
\[
   d_{\mathcal R_n}(S,T)=(n-2)-|S\cap T|.
\]
Thus \(\mathcal R_n\) is connected and is an *isometric* induced subgraph of the ambient Johnson graph on the \((n-2)\)-subsets of \(V(H_n)\), even though for every \(n\ge4\), \(\mathcal B_n\) **does not satisfy the matroid basis-exchange axiom**. Its two types have respective degrees \(5(n-2)\) and \(n+2\), and its exact edge count is
\[
   |E(\mathcal R_n)|=\frac{n(n-1)(n-2)(n+7)}4.
\]
For \(n=3,4,5\) the radius and diameter are both respectively \(1,2,3\). For every \(n\ge6\), the radius is \(3\) and diameter \(4\); precisely the \(\binom n2\) type-\(A\) configurations have eccentricity three, and the \(3\binom n3\) type-\(B\) configurations have eccentricity four.

## Assumptions and scope

The graph is finite, labeled, simple, undirected, and every edge of \(K_n\) is subdivided **once**. A power-dominating set is any set \(S\) for which initially observing \(N_{H_n}[S]\), then repeatedly observing a unique unobserved neighbor of any observed vertex, eventually observes the whole graph. Every selected original or subdivision vertex is a distinct sensor location. The forest \(F_S\) retains all original vertices not selected, including isolated vertices. The two types of optimum sets are counted by actual labeled vertex subsets, not modulo automorphisms. A reconfiguration step changes one sensor location without changing the number of sensors; no adjacency requirement is imposed on the old and new sensor locations. All quantifiers run over integer \(n\ge3\); no other graph family is asserted.

## Proof

**1. Cycles obstruct.** Suppose \(F_S\) has a cycle \(C\). Each edge of \(C\) corresponds to a subdivision vertex \(s_e\) not initially selected (because \(e\notin B\)) and with neither endpoint initially chosen (because both endpoints lie in \(R\)). Consequently no such \(s_e\) is observed in the initial closed-neighborhood step. Each original vertex on \(C\) has at least two unobserved neighboring subdivision vertices along \(C\), and a subdivision vertex has neighbors only at its two originals. Inductively no \(s_e\) belonging to \(C\) can be the first vertex of this cycle to be forced. Thus \(S\) cannot power dominate.

**2. Acyclicity suffices.** Suppose \(F_S\) is a forest. If \(A\ne\varnothing\), choose an original \(a\in A\). For each initially unobserved original \(v\in R\), the already observed subdivision \(s_{av}\) has \(a\) observed and \(v\) as its sole unobserved neighbor. After one forcing round every original is observed. Now all unobserved vertices are subdivision vertices for edges of the forest \(F_S\). A leaf of the current forest is an observed original with exactly one unobserved subdivision neighbor, so its edge subdivision can be forced. Repeating leaf removal observes every forest edge, and hence every vertex.

If \(A=\varnothing\), the selected subdivision vertices initially observe themselves and their endpoints. Two unobserved originals \(u,v\) would have no incident edge in \(B\), making every edge incident with either of them an edge of \(F_S\); for \(n\ge3\), these include a triangle \(u,v,w\), contradicting acyclicity. Hence at most one original \(w\) is unobserved initially. If none is unobserved, leaf removal works as above. If \(w\) is unobserved, all \(n-1\) edges incident to \(w\) belong to \(F_S\), so acyclicity forces \(F_S\) to be precisely that star. All other originals are already observed and each has exactly one unobserved subdivision neighbor, namely \(s_{vw}\). They force these subdivision vertices, and then one of those vertices forces \(w\). This establishes the criterion also when \(A\) is empty.

**3. Counting all sets.** Fix \(R\) of size \(r\), hence the \(n-r\) selected originals. The internal edge-subdivision sensors selected inside \(R\) are exactly the complement of a forest with \(k\) edges, giving \(N_r-k\) selected sensors and \(f_{r,k}\) possibilities. The \(N_n-N_r\) subdivision sensors corresponding to edges not wholly inside \(R\) may independently be selected or omitted. Multiplication by \((1+z)^{N_n-N_r}\), followed by \(\binom nr\) choices of \(R\), gives the stated polynomial. The displayed exponential formula is the standard labeled set-of-tree-components construction, using Cayley's \(j^{j-2}\) labeled trees for \(j\ge2\).

**4. Minimum cardinality and rigidity.** For \(r\ge1\), a forest on \(r\) vertices has at most \(r-1\) edges. A successful placement therefore needs at least \(n-r+N_r-(r-1)\) sensors. At \(r=0\), it needs at least \(n\). For \(r\ge1\), the bound is \(n-r+\binom{r-1}{2}\). It equals \(n-2\) exactly at \(r=2,3\), is greater at \(r=1\) and \(r\ge4\), and no smaller value exists. At \(r=2\), equality selects all but two original vertices and no subdivision vertex. At \(r=3\), equality selects all but three originals and exactly one subdivision vertex inside those three; the two surviving edges of \(K_3\) form a tree. This yields exactly the two stated types and count \(\binom n2+3\binom n3=n(n-1)^2/2\). In particular, the \(r=n\) case is included (and gives the three edge-subdivision-only minima when \(n=3\)).

**5. Exchange edges.** Two type-\(A\) minima are adjacent iff their omitted pairs differ by one element, giving \(2(n-2)\) type-\(A\) neighbors. Each type-\(A\) set has \(3(n-2)\) type-\(B\) neighbors, obtained by extending its omitted pair to a triple and choosing one of three internal edges. Hence type-\(A\) degree is \(5(n-2)\). A type-\(B(V,e)\) set is adjacent to three type-\(A\) sets (omit any two of \(V\)), to two other type-\(B\) sets with the same triple and a different internal selected edge, and to \(n-3\) other type-\(B\) sets having the same selected subdivision edge and a different third omitted original. These classes are disjoint, giving degree \(n+2\). Summing degrees across the two parts and dividing by two gives the edge formula.

**6. Distances have no detours.** The intersection bound \(d_{\mathcal R_n}(S,T)\ge(n-2)-|S\cap T|\) holds because each replacement increases overlap with the target by at most one. For type-\(A\) configurations the induced graph is the Johnson graph on omitted pairs and achieves this bound. For \(A(U)\) and \(B(V,e)\), choose an omitted pair \(U'\subset V\) maximizing \(|U\cap U'|=|U\cap V|\); go from \(A(U)\) to \(A(U')\) in \(2-|U\cap V|\) steps and then to \(B(V,e)\) in one step. This length equals \(3-|U\cap V|=(n-2)-|A(U)\cap B(V,e)|\).

For two type-\(B\) configurations \(B(V,e)\) and \(B(W,f)\), if \(e=f\) their omitted triples differ in at most one element and their distance is one unless they coincide. If \(V=W\) and \(e\ne f\), they differ only in their selected subdivision sensor and are adjacent. Otherwise \(e\ne f\) and \(V\ne W\). Choose pairs \(U\subset V\), \(U'\subset W\) with \(|U\cap U'|=\min\{2,|V\cap W|\}\). The path \(B(V,e)\to A(U)\to\cdots\to A(U')\to B(W,f)\) has length \(4-\min\{2,|V\cap W|\}\). Because distinct triples have intersection of size at most two, this length is \(4-|V\cap W|=(n-2)-|B(V,e)\cap B(W,f)|\). All pair types attain the lower bound. The eccentricity assertions follow by taking disjoint omitted pairs/triples when ground-set size permits: a type-\(A\) state sees distance at most three, with distance three attained for \(n\ge5\), whereas type-\(B\) states have distance four precisely when an omitted triple disjoint from theirs exists (\(n\ge6\)). Direct size bounds give the smaller \(n=3,4,5\) cases.

**7. The optimizer family is not a matroid.** For \(n\ge4\), choose distinct \(a,b,c,d\in[n]\). The type-\(B\) optimum \(P=([n]\setminus\{a,b,c\})\cup\{s_{ab}\}\) and type-\(A\) optimum \(Q=[n]\setminus\{c,d\}\) satisfy \(d\in P\setminus Q\) and \(Q\setminus P=\{a,b\}\). Removing \(d\) from \(P\) and inserting either \(a\) or \(b\) yields a size-\((n-2)\) set whose selected subdivision vertex is incident with a selected original, and hence is of neither allowable optimum type. No basis-exchange replacement exists for the element \(d\), proving the asserted failure despite the isometric exchange property.

## Verification

The supplied `check_forest.cpp` constructs the incidence graph directly and independently applies the synchronous power-domination rule to **every** initial vertex subset for \(n=3,4,5,6\). It compares each result with a union–find acyclicity test for \(F_S\), reproduces every coefficient and verifies the minimum and number of optimum subsets. There are \(2^{21}=2{,}097{,}152\) full cases at \(n=6\). Compile and run:

```sh
g++ -O3 -std=c++17 check_forest.cpp -o check_forest
./check_forest
```

The independent standard-library Python program `check_enumerator.py` implements both direct propagation and labeled-forest enumeration for \(n=3,4,5\), then independently constructs every optimum and its full exchange graph through \(n=9\). It checks the optimum counts, edge counts, degree formulae, all-pairs isometry and eccentricity distributions. Run `python3 check_enumerator.py`. All checks passed against these exact packaged sources. Exhaustive finite checks are supplementary to, not substitutes for, the all-order proof.

## Relationship to prior work

Haynes, Hedetniemi, Hedetniemi and Henning (2002) introduced power domination to model electric-network monitoring. Brimkov, Patel, Suriyanarayana and Teich (2018) defined and studied the full power-domination polynomial, but the inspected 23-page text treats other graph families, not the present full subdivisions. Bjorkman *et al.* (2026) studied general power-domination reconfiguration and established baseline exchange definitions, without a subdivision-of-clique classification in the inspected article.

A published same-object result, *Minimal forts and the complete zero forcing polynomial of fully subdivided complete graphs* (2026), fully classifies **ordinary zero forcing**, not power domination. Its cycle-fort and forest analysis anticipates the cycle obstruction used here; the general known equivalence between power domination and zero forcing from a closed neighborhood also supplies a route to that obstruction. The present claim therefore does **not** claim discovery of forest enumeration or the scalar zero-forcing number. Its distinctive assertion is the exact classification and **isometric, nonmatroidal reconfiguration** of every minimum power-dominating placement, together with the direct power-domination polynomial. Ordinary zero forcing, requiring a more restrictive initial condition, does not itself identify that optimum family or establish its all-pairs exchange distances, degrees and eccentricities. The earlier result on *paired domination minima in subdivided cliques* concerns matching-backed dominating sets, not the propagation rule here.

## Limitations

The theorem concerns the special full subdivision \(H_n\) and the ordinary power-domination rule only. It does not assert anything about mixed subdivisions, arbitrary graphs, token sliding (where a replacement is constrained by an edge), physical electrical load flows, reliability under failures or polynomial real-rootedness. The labeled forest exponential formula uses the standard Cayley tree count. The earliest exact publicly verifiable day attached to the archival introductory paper is its online date of 2006-08-01, while the journal issue carries 2002 without an exact verified first public day; the older year is credited. Search and inspected primary texts cannot rule out unpublished or unindexed equivalent reconfiguration results. These statements have received only self-review, not independent validation.

## References

1. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM Journal on Discrete Mathematics 15(4), 519–529 (2002), DOI: https://doi.org/10.1137/S0895480100375831 (online date 2006-08-01 shown on publisher page).
2. B. Brimkov, R. Patel, V. Suriyanarayana and A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984v1 (2018-05-28), https://arxiv.org/abs/1805.10984 .
3. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob and C. Reinhart, *Power Domination Reconfiguration*, La Matematica 5, article 8 (2026-01-13), https://doi.org/10.1007/s44007-025-00187-5 .
4. *Minimal forts and the complete zero forcing polynomial of fully subdivided complete graphs* (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-minimal-forts-and-the-complete-zero-forcing-polynomial-of-fully--43a4c9836292 .
5. *Paired-domination minima in subdivided cliques: a rooted-pseudoforest enumeration* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-paired-domination-minima-in-subdivided-cliques-a-rooted-pseudofo--3bd93f83b97d .
