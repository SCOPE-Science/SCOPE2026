# Sharp extremal geodesic multiplicities in the two-generated free inverse monoid

## Finding

Let \(FIM(a,b)\) be the free inverse monoid on two generators, with words written over \(\{a,a^{-1},b,b^{-1}\}\). For an element \(g\), its Munn tree \(T(g)\) is the finite subtree of the Cayley tree of the free group \(F(a,b)\) visited by a representing walk, including the identity and the endpoint. Put \(e(g)=|E(T(g))|\). Let \(c(g)\) be the number of **distinct words of minimum length** representing \(g\), and define

\[
M_m=\max\{c(g):g\in FIM(a,b),\ e(g)=m\}\qquad(m\ge0).
\]

**Theorem (sharp redundancy and extremizers).** For every integer \(m\ge0\),

\[
M_m=\begin{cases}
1,&m=0,1,\\
2,&m=2,\\
6,&m=3,\\
4\,6^{\lfloor(m-1)/3\rfloor}\,2^{\mathbf1_{\{m\equiv0\pmod3\}}},&m\ge4.
\end{cases}
\]

In particular \(\lim_{m\to\infty}M_m^{1/m}=6^{1/3}\). For \(m\ge4\), all maximizing elements have coincident initial and terminal vertices at a degree-four vertex of their Munn tree. Writing \(q=m-1=3k+r\), \(r\in\{0,1,2\}\), a maximizing Munn tree has exactly \(k\) vertices of degree four and, respectively, no extra nonleaf vertices when \(r=0\), one degree-two vertex when \(r=1\), or one degree-three vertex when \(r=2\). Its remaining vertices have degree one. Conversely, every embedded Munn tree with this degree profile and coincident roots at a degree-four vertex is maximizing.

An exact refinement holds in any finitely generated free inverse monoid. Given a finite nonempty tree \(T\), with \(m\ge1\) edges and a chosen ordered pair \(s,t\) of vertices, let \(d_v\) be the degree of \(v\) and \(P(s,t)\) its unique vertex path. The number \(N_T(s,t)\) of geodesic words for the associated birooted Munn element is

\[
N_T(s,t)=\begin{cases}
d_s!\displaystyle\prod_{v\ne s}(d_v-1)!,&s=t,\\[2mm]
\displaystyle\prod_{v\in P(s,t)\setminus\{s,t\}}(d_v-2)!\;
\prod_{v\notin P(s,t)\setminus\{s,t\}}(d_v-1)!,&s\ne t.
\end{cases}
\]

Its minimum word length is \(2m-d_T(s,t)\). For \(m=0\), the empty-word element has exactly one shortest representative. Using the standard Green relations, the complete polynomial enumerating the geodesic words of all the elements in the \(\mathcal D\)-class of \(T\), by their **individual** geodesic lengths, is

\[
G_T(z)=\sum_{s,t\in V(T)}N_T(s,t)z^{2m-d_T(s,t)}.
\]

Consequently, the number of words of **minimum length among that \(\mathcal D\)-class** is

\[
\sum_{\substack{s,t\in V(T)\\d_T(s,t)=\operatorname{diam}(T)}}N_T(s,t),
\]

and the minimum class length is \(2m-\operatorname{diam}(T)\). Analogously, for an \(\mathcal R\)-class rooted at \(s\), the minimum-class multiplicity is \(\sum_{t:d_T(s,t)=\operatorname{ecc}_T(s)}N_T(s,t)\), and the \(\mathcal L\)-class formula exchanges \(s,t\). These refinements are exact for all finite Munn trees, not merely the maximizing trees.

## Assumptions and scope

The two generators and their formal inverses are distinct letters. Word length counts all four types of signed letters, without free cancellation in the input word. A Munn element is the pair consisting of the prefix-visited vertices of a word in the free-group Cayley tree and the freely reduced endpoint; two words represent the same inverse-monoid element precisely when both data coincide. A tree with \(m=0\) edges is the one-vertex tree of the identity. Tree degrees are unweighted undirected degrees. In the refinement, translated copies of a tree are identified when selecting its abstract \(\mathcal D\)-class, but every choice of initial and terminal vertices yields a distinct element. A finite tree is considered embedded in a signed-generator Cayley tree with distinct incident edge labels.

## Proof

**1. Exact words as shortest edge-covering walks.** Let \(T\) be a Munn tree with \(m\ge1\), with starting and ending vertices \(s,t\). Any representing word is a walk from \(s\) to \(t\) traversing every edge of \(T\) at least once and no edge outside \(T\). Deleting an edge partitions the tree into two components. By parity of crossings, every edge of the unique \(s\)-to-\(t\) path is used an odd positive number of times, hence at least once, and every other edge an even positive number of times, hence at least twice. The length is therefore at least \(2m-d_T(s,t)\). Equality is attained: at each path vertex, traverse every off-path rooted subtree by a closed depth-first tour, then advance along the next path edge. Hence equality characterizes walks using every path edge once and every other edge twice.

The above equality forces the first traversal of each off-path edge to be followed eventually by its unique return. At each vertex not internal to \(P(s,t)\), the children of the rooted hanging subtrees can be ordered freely: there are \((d_v-1)!\) such orders, except at a closed-tour root \(s=t\), which has \(d_s!\) orders. At each internal path vertex, the incoming and outgoing path edges are prescribed and there are \((d_v-2)!\) orders of the other excursions. Multiplying these independent local choices gives exactly \(N_T(s,t)\) displayed above. Distinct choices give different label words because signed labels on distinct edges leaving any vertex are different. Conversely every shortest walk determines these local orders. This is a bijective enumeration, not a formal-word simplification argument.

**2. Relation-specific enumerators.** The standard Munn description identifies the \(\mathcal R\)-class by its visited tree and initial vertex, the \(\mathcal L\)-class by its tree and final vertex, and the \(\mathcal D\)-class by its unrooted tree up to translation. In the free inverse monoid, \(\mathcal H\) is equality. A nontrivial left translation cannot preserve a finite nonempty subset of the torsion-free free group (repeated translates would be infinitely many), so different choices of \(s\) give genuinely distinct Munn elements. The length formula from step 1 therefore permits summation over distinct endpoint choices without overcounting. For the \(\mathcal D\)-class, maximizing \(d_T(s,t)\) minimizes the word length; for fixed \(s\), maximizing distance to \(t\) gives the \(\mathcal R\)-case. The \(\mathcal L\)-case is symmetric. These observations prove the polynomial and shortest-class formulas.

**3. Maximal multiplicity for a fixed tree.** For \(m\ge1\), set \(B(T)=\prod_{v\in V(T)}(d_v-1)!\). If \(s\ne t\), every internal-path contribution of \((d_v-2)!\) is at most \((d_v-1)!\), so \(N_T(s,t)\le B(T)\). If \(s=t\), the first formula reads \(N_T(s,s)=d_sB(T)\). Thus \(\max_{s,t}N_T(s,t)=(\max_v d_v)B(T)\). In particular, for \(m\ge2\), maximizing endpoint pairs must be coincident at a vertex of maximum degree, because \(\max_vd_v\ge2\).

**4. Sharp degree optimization.** In the four-regular Cayley tree, let \(A,B,C\) denote the numbers of degree-four, degree-three and degree-two vertices of any finite Munn tree. The handshake identity, with \(|V|=m+1\), yields

\[
3A+2B+C=m-1.
\]

Its degree factorial product is \(B(T)=6^A2^B\), and its largest degree is four if \(A\ge1\), three if \(A=0,B\ge1\), two if \(A=B=0,m\ge2\), and one if \(m=1\). For a given \(A\ge1\), the largest product is attained by \(B=\lfloor(m-1-3A)/2\rfloor\), with any remaining unit assigned to \(C\). Increasing \(A\) by one consumes three units and lowers the maximal allowable \(B\) by at most two; the gain factor six therefore strictly exceeds the loss factor at most four. Hence the best \(A\ge1\) is \(A=\lfloor(m-1)/3\rfloor\). When \(m\ge4\), the candidate with \(A=1\) already exceeds all configurations with \(A=0\): its value is \(24\,2^{\lfloor(m-4)/2\rfloor}\), while any \(A=0\) configuration has value at most \(3\,2^{\lfloor(m-1)/2\rfloor}\), and the former is larger. This proves both the formula for \(m\ge4\) and the asserted strict characterization of maximizing degree counts and roots. For \(m=0,1,2,3\), direct consideration of the available degree lists gives \(1,1,2,6\).

**5. Attainment and limit.** Any finite abstract tree of maximum degree at most four can be embedded in the Cayley tree of \(F(a,b)\): choose a root, assign distinct signed labels to incident child edges, excluding the inverse of the incoming parent-edge label at each nonroot vertex. A degree sequence with \(A=k\), \(B=0\) or \(1\) as above and at most one degree-two vertex can be realized by a tree (its required number of leaves is \(2A+B+2\), and the sum of degrees is twice the edge count). Embedding with any degree-four vertex at the group identity gives a Munn tree attaining the bound using the closed tour based there. Finally \(\lfloor(m-1)/3\rfloor/m\to1/3\) and the remaining factors are bounded, yielding the stated exponential limit.

## Verification

The reproducible Python checker `verification/check.py` independently enumerates every signed word of length at most eight (\(87,381\) words), normalizes its prefix-visited vertices by free reduction, and checks the exact geodesic multiplicity and length for all ordered vertex pairs in eleven sample embedded trees. It separately checks \(\mathcal R\)-, \(\mathcal L\)- and \(\mathcal D\)-class minimal-word counts. A second independent finite experiment exhaustively generates all unlabeled ordinary trees up to ten edges, filters maximum degree four, and compares the maximum over all endpoints with the sharp formula. The recorded stdout is `verification/output.txt`, ending in `EXTREMAL_VERIFY_OK m=0..10`. The finite experiments do not establish arbitrary-rank or arbitrary-size conclusions; those follow from the proofs above.

## Relationship to prior work

Bodart, Carvalho and Monteiro (first public preprint September 28, 2026; arXiv:2609.35251, version 2 inspected) introduce Green geodesic languages of free inverse monoids. Their Theorem 2.4 recalls the Munn-tree characterization of Green relations, and their conditions G10, R4 and D4 give the edge-traversal and farthest-endpoint descriptions. Those known qualitative statements are inputs to the present argument. Neither the exact factorial multiplicity enumerator nor the sharp fixed-edge extremal formula and degree-pattern classification appears in the inspected primary text. The mathematical advance assessed here is the exact numerical optimization and complete maximizing shapes, not discovery of depth-first traversal or of Munn's model. The GAP Semigroups documentation acknowledges nonunique minimal representative words but does not give the extremal count. Mitchell's 1974 *Counting word-trees* counts word-trees as objects; the accessible abstract does not determine geodesic-word multiplicity within a fixed tree. Silva's 2001 paper studies which trees occur as Schützenberger graphs for inverse monoid presentations, not the present maximum-count problem.

## Limitations

The maximum formula is for exactly two free generators with the standard four signed letters and complexity measured by the number of Munn-tree edges, not by the length of a geodesic word. The arbitrary-rank formula counts words for a specified tree and pair of endpoints, but a sharp extremal formula for higher fixed ranks is not claimed. The result is supported by a detailed proof and finite checks; independent mathematical assessment and exhaustive historical-priority certification have not occurred. In particular, an older general counting theorem for shortest edge-covering tree walks could subsume the factorial factorization or the extremal argument. Some older full texts were not accessible in the available research process; their unexamined contents are a residual priority risk.

## References

1. C. Bodart, A. Carvalho, A.-C. C. Monteiro, *Green languages and growth of free inverse monoids*, first arXiv submission 2026-09-28, arXiv:2609.35251. Primary full text, version 2: https://pdfs.assets.alphaxiv.org/2609.35251v2.pdf .
2. W. D. Munn, *Free inverse semigroups*, Proceedings of the London Mathematical Society, 1974, DOI: 10.1112/plms/s3-29.3.385 (foundational Munn representation).
3. J. M. O. Mitchell, *Counting word-trees*, Glasgow Mathematical Journal 15 (1974), 148–149, DOI: 10.1017/S0017089500002317 (counts the trees themselves).
4. P. V. Silva, *Trees associated to inverse monoid presentations*, Journal of Pure and Applied Algebra 165 (2001), 307–335, DOI: 10.1016/S0022-4049(00)00190-0.
5. GAP Semigroups package, *Munn trees and normal forms*, https://fossies.org/linux/gap/pkg/semigroups/doc/chap7_mj.html (examples of nonunique minimum words).
