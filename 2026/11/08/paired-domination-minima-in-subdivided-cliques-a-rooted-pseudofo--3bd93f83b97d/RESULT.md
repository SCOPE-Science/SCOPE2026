# Paired-domination minima in subdivided cliques: a rooted-pseudoforest enumeration

## Finding

Let \(n\ge 2\), and let \(S(K_n)\) be the simple graph obtained by subdividing **every** edge of the labelled complete graph \(K_n\) exactly once. Denote the original vertex corresponding to \(i\) by \(v_i\), and the subdividing vertex on \(\{i,j\}\) by \(s_{ij}\). A paired dominating set is a dominating vertex set whose induced graph admits a perfect matching.

For every minimum paired dominating set \(D\), there is a unique omitted original vertex \(v_w\) and a unique selected edge set \(F\subseteq E(K_n)\) of size \(n-1\) such that
\[
D=\{v_i:i\ne w\}\cup\{s_{ij}:\{i,j\}\in F\}.
\]
These and only these pairs \((w,F)\) are minimum paired dominating sets when the spanning simple graph \(([n],F)\) has (i) a **nontrivial tree** component containing \(w\), and (ii) only **unicyclic** components elsewhere. If there are \(c\) nonroot unicyclic components, the induced graph \(S(K_n)[D]\) has exactly \(2^c\) perfect matchings. In particular, the paired-domination number is \(\gamma_{\mathrm{pr}}(S(K_n))=2(n-1)\).

Write \(A_n(y)=\sum_{D}y^{c(D)}\), summing over minimum paired dominating sets, where \(c(D)\) is the number of unicyclic components just described. Define the unique formal series \(T(x)\in x\mathbb Q[[x]]\) by \(T(x)=x\exp(T(x))\) and put
\[
U(x)=\sum_{j\ge3}\frac{T(x)^j}{2j}
=\frac12\left(\log\frac1{1-T(x)}-T(x)-\frac{T(x)^2}{2}\right).
\]
Then the **entire matching-multiplicity distribution** is
\[
\boxed{A_n(y)=n(n-1)!\,[x^{n-1}]\bigl(e^{T(x)}-1\bigr)e^{yU(x)}.}
\]
In particular, the number of minimum sets is \(A_n(1)\); exactly \(n^{n-1}\) of them have a unique perfect matching. Multiple perfect matchings first occur at \(n=5\), where \(A_5(y)=625+20y\). The initial total counts for \(n=2,3,4,5,6,7\) are \(2,9,64,645,8406,133938\), respectively.

## Assumptions and scope

All graphs are finite, simple, and labelled; \(n\) is an integer with \(n\ge2\). Subdivision is performed exactly once on every edge of \(K_n\), producing one new vertex per edge. Domination means each vertex outside the selected set has a selected neighbour, and an induced perfect matching covers every selected vertex, without requiring the matching to be induced. Different sets of selected vertices are counted once each, even if they admit multiple matchings. The indeterminate \(y\) records the number of nonroot unicyclic components, not the number of available matchings directly; the latter equals \(2^{c(D)}\). All exponential and logarithmic series are formal at zero, so no convergence assumption is required.

## Proof

**Minimum size and original-vertex coverage.** Every edge of \(S(K_n)\) joins an original to a subdivision vertex. Thus a perfect matching of the induced subgraph of a paired dominating set \(D\) entails equal numbers of selected vertices of these two types. Let \(W\subseteq[n]\) be its omitted original indices. If \(i,j\in W\) are distinct, then \(s_{ij}\), having no selected neighbour among its two original neighbours, must itself belong to \(D\) to be dominated. But then it has no selected neighbour with which to be matched, a contradiction. Therefore \(|W|\le1\) and \(|D|\ge2(n-1)\). Equality is attained by selecting every original except \(v_w\) and all \(n-1\) subdivision vertices \(s_{wi}\) incident with \(w\): pair \(v_i\) to \(s_{wi}\) for each \(i\ne w\). Every omitted subdivision vertex meets a selected original, and the omitted original \(v_w\) meets a selected subdivision vertex.

**Structure at equality.** Equality forces \(W=\{w\}\) and exactly \(n-1\) selected subdivision vertices, indexed by a set of edges \(F\). All unselected subdivision vertices are automatically dominated, because their corresponding edge has at least one endpoint different from \(w\). The only additional domination condition is \(\deg_F(w)\ge1\). The induced graph on selected vertices is precisely the incidence bipartite graph between \(U=[n]\setminus\{w\}\) and \(F\), with each \(e\in F\) adjacent to its selected endpoints. A perfect matching is equivalent to assigning each edge of \(F\) to one of its ends in \(U\), bijectively onto \(U\).

For a connected component \(C\) of \(([n],F)\) not containing \(w\), such an assignment requires \(|E(C)|\ge|V(C)|\). In the component containing \(w\), it requires \(|E(C)|\ge |V(C)|-1\). As the sum of all edge counts is exactly \(n-1\), every inequality must be equality. Hence the component containing \(w\) is a tree, and every other component is connected and unicyclic. Moreover, \(\deg_F(w)\ge1\) makes the root tree nontrivial. Conversely, for such a graph, assign each tree edge in the root component to its endpoint farther from \(w\). In every other component, orient its sole cycle coherently and assign each cycle edge to the endpoint it points toward, and assign all pendant-tree edges away from the cycle. This is a perfect incidence matching and gives the requisite domination.

**Perfect matching multiplicity.** In the root tree, the bijective edge-to-nonroot-vertex assignment is unique: prune leaves not equal to \(w\) repeatedly. In a nonroot unicyclic component, leaf pruning forces all attachments to the cycle; on the residual cycle there are exactly two consistent assignments. Different components are independent, hence precisely \(2^c\) induced perfect matchings.

**Labelled enumeration.** A rooted labelled tree attached at its distinguished uncounted root \(w\), having \(k\) other vertices, has \((k+1)^{k-1}\) possibilities (\(1\) for \(k=0\)) by Cayley's formula. Its exponential generating function on nonroot labels is \(e^{T(x)}\), because \(T=xe^T\). Excluding the isolated root subtracts \(1\). Every nonroot unicyclic component is an unoriented labelled cycle of length at least three, each cycle vertex supporting a rooted labelled tree. The exponential generating function for such a component is \(U(x)=\sum_{j\ge3}T(x)^j/(2j)\). The labelled set of these components, marked by their count, has generating function \(e^{yU(x)}\). Choosing the omitted vertex \(w\) in \(n\) ways and distributing the remaining \(n-1\) labels establishes the boxed formula.

The \(y^0\) term requires one spanning tree containing \(w\) and nothing else. There are \(n\cdot n^{n-2}=n^{n-1}\) such sets by Cayley's formula. Any nonroot unicyclic component uses at least three vertices and the nontrivial root component uses at least two, so \(n\ge5\) is necessary for matching multiplicity greater than one. It is sufficient: take a root edge and a disjoint triangle and, for larger \(n\), attach extra vertices as leaves to the root tree. This proves the first-occurrence claim.

## Verification

The included Python 3 script `artifacts/verify.py` directly constructs the subdivision incidence relations and enumerates every candidate pair \((w,F)\) with \(|F|=n-1\), for \(2\le n\le7\). It computes induced perfect matchings by direct recursion, independently tests domination, compares the result with the rooted-pseudoforest rule, and checks the full coefficient distribution against the labelled unicyclic-component recurrence. It also checks the recurrence and the unique-matching coefficient through \(n=30\). Run `python artifacts/verify.py` from the extracted package root. All those finite checks pass. The general theorem follows from the proof above, not from an extrapolation of finite enumeration.

## Relationship to prior work

Muthukamatchi and Arumugam (2016), Theorem 2.9, already establish the *minimum cardinality* \(\gamma_{\mathrm{pr}}(S(K_n))=2(n-1)\). That cardinality is background, **not claimed as new** here. Their paper does not enumerate the minimum sets, describe their pseudoforest structure, or determine the multiplicities of induced perfect matchings. Lu and Wu (2026) investigate a sharp universal upper bound for paired domination in cubic bipartite graphs, using dominating matchings. The subdivisions of \(K_n\) here are bipartite but not cubic for general \(n\), so that theorem does not provide the present enumeration. The counting reduces to classical Cayley-labelled trees and labelled unicyclic components; those classical enumeration facts are acknowledged as known inputs.

## Limitations

This result counts minimum-cardinality paired dominating **vertex sets**, not every paired dominating set and not distinct perfect matchings as separate vertex sets. It is restricted to the once-subdivided labelled complete graph; it does not classify subdivisions of arbitrary graphs or multiple subdivisions of the same edge. A negative literature search is not a proof of historical priority; less accessible earlier enumeration remains a risk. Independent mathematical audit has not been performed.

## References

1. A. Muthukamatchi and S. Arumugam, *Paired Domination in Subdivision Graphs*, International Journal of Innovative Research in Science, Engineering and Technology 5(10) (2016), Theorem 2.9, doi:10.15680/IJIRSET.2016.0510126, https://www.ijirset.com/upload/2016/october/126_Paired.pdf.
2. C. Lu and Q. Wu, *Paired Domination in Cubic Bipartite Graphs*, arXiv:2609.30152, first publicly submitted 2026-09-24, https://arxiv.org/abs/2609.30152.
3. A. Cayley, *A theorem on trees*, Quarterly Journal of Pure and Applied Mathematics 23 (1889), 376–378 (classical labelled-tree enumeration).
