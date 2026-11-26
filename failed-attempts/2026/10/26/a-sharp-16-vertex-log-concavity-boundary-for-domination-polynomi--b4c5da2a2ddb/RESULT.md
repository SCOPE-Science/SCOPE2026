# A sharp 16-vertex log-concavity boundary for domination polynomials of trivially perfect graphs

## Finding
For a finite simple graph \(G\), write \(D(G;z)=\sum_{j=0}^{|V(G)|}d_j(G)z^j\), where \(d_j(G)\) counts dominating vertex subsets of cardinality \(j\). A coefficient sequence is **log-concave** when \(d_j(G)^2\ge d_{j-1}(G)d_{j+1}(G)\) for all interior indices.

**Theorem (sharp boundary and uniqueness).** Every trivially perfect graph on at most \(15\) vertices has a log-concave domination polynomial. At order \(16\), exactly one isomorphism class fails log-concavity:
\[
G_*=K_1\vee(K_5\sqcup K_5\sqcup K_5).
\]
Here \(\vee\) is graph join, and \(\sqcup\) is disjoint union. The polynomial of this graph is
\[
D(G_*;z)=z(1+z)^{15}+((1+z)^5-1)^3
=z+15z^2+230z^3+1205z^4+\cdots+z^{16}.
\]
Thus \(d_2(G_*)^2=225<230=d_1(G_*)d_3(G_*)\). More generally, for every integer \(m\ge5\), \(K_1\vee(3K_m)\) is a connected trivially perfect graph whose domination polynomial fails log-concavity at index \(2\).

## Assumptions and scope
Graphs are finite, simple, undirected and may be disconnected. A set \(S\subseteq V(G)\) dominates \(G\) when every vertex is in \(S\) or adjacent to some vertex of \(S\). A graph is trivially perfect if it contains no induced \(P_4\) or \(C_4\), equivalently if it is the comparability graph of the ancestor relation of a finite rooted forest. The finite optimality statement is complete for orders \(1\) through \(16\); the infinite counterfamily statement applies only to the displayed clique-bouquet graphs.

## Proof
**Recurrences.** For disjoint vertex sets, \(D(G\sqcup H;z)=D(G;z)D(H;z)\). A connected trivially perfect graph can be represented as \(K_1\vee H\), where \(H\) is a nonempty trivially perfect graph (possibly disconnected), unless the graph is the isolated vertex. When the universal vertex is chosen, every subset of \(V(H)\) may be chosen; when it is omitted, precisely the dominating subsets of \(H\) are allowed. Therefore
\[
D(K_1;z)=z,\qquad
D(K_1\vee H;z)=z(1+z)^{|V(H)|}+D(H;z)\quad (|V(H)|\ge1).
\]
These recurrences give every coefficient exactly over the integers.

**Exhaustive finite cutoff.** Every rooted tree shape consists of one root with a multiset of smaller rooted tree shapes as children; every rooted forest shape is a multiset of rooted tree shapes. Sorting the shapes by their unique creation index gives a canonical nondecreasing list for every such multiset. The supplied `verify.py` constructs all rooted-tree shapes of size \(n\) by rooting every previously constructed forest shape of size \(n-1\), then constructs all forests of size \(n\) by adjoining a rooted-tree type with index at least the previous largest index. Inductively, no rooted forest shape is omitted or counted twice by this enumeration. The two displayed polynomial recurrences evaluate every enumerated shape, including all disconnected graphs. Every trivially perfect graph has a rooted-forest representation, so testing these shapes exhausts the claimed class (even if a graph were to admit more than one representation).

The exact integer census has, at respective orders \(1,\ldots,16\), the following numbers of rooted-tree shapes:
\[
1,1,2,4,9,20,48,115,286,719,1842,4766,12486,32973,87811,235381.
\]
The numbers of rooted-forest shapes are
\[
1,2,4,9,20,48,115,286,719,1842,4766,12486,32973,87811,235381,634847.
\]
For every shape at every order, the program checks the exact integer inequalities \(d_j^2\ge d_{j-1}d_{j+1}\) without floating point. It finds zero violations for all forests of order at most \(15\), and exactly one violating rooted-forest shape of order \(16\). That shape is connected: its rooted tree has a root with three identical children, each a five-vertex chain. Transitive closure produces exactly \(G_*\), proving both the cutoff and the uniqueness assertion.

**Witness and infinite extension.** All dominating sets of \(K_1\vee(3K_m)\) either include its central universal vertex or omit it and meet each of the three cliques. Consequently
\[
D(K_1\vee(3K_m);z)=z(1+z)^{3m}+((1+z)^m-1)^3.
\]
Its coefficients of degrees \(1,2,3\) are respectively \(1\), \(3m\) and \(\binom{3m}{2}+m^3\). Thus the index-\(2\) log-concavity defect is
\[
d_1d_3-d_2^2=\frac{m}{2}(2m^2-9m-3),
\]
which is positive for every integer \(m\ge5\) (and is negative for \(1\le m\le4\)). Taking \(m=5\) yields the stated \(16\)-vertex witness.

## Verification
Execute `python3 verify.py` with Python \(3.8\) or later. The standalone script generates all \(1{,}011{,}310\) rooted-forest shapes of orders \(1\) through \(16\), evaluates the exact recurrence, verifies their cardinality census, and checks every interior coefficient inequality. It also independently enumerates all \(2^{16}\) labelled vertex subsets of \(G_*\), checks domination directly from closed-neighborhood bitmasks, and compares its complete polynomial with the recurrence result. Expected output is stored in `verify_output.txt`; the first line starts `VERIFY_OK`. The independent brute-force check confirms the witness polynomial but does not prove minimality; that relies on the exhaustive rooted-forest generator and its completeness argument.

## Relationship to prior work
Bilal Ahmad Rather, *On domination polynomials of some graphs* (2025), gives the general join-of-cliques polynomial in Theorem 2.16 and explicitly leaves log-concavity and unimodality for unequal-size generalized friendship constructions as a question. That polynomial already implies the displayed \(G_*\) coefficient values by substitution; **the new content is the sharp minimum order and uniqueness among all trivially perfect graphs**, not a claimed new formula for this particular join. Mohamed Omar, *New Perspectives on the Unimodality of Domination Polynomials* (2026), proves coefficient-shape results for the smaller class of threshold graphs. The present boundary shows that extending log-concavity to all trivially perfect graphs fails, and pinpoints the first order at which it fails. Earlier examples of non-log-concave domination sequences for general trees do not establish this subclass-specific cutoff or uniqueness.

## Limitations
The finite cutoff is established by an exhaustive exact-arithmetic computation whose correctness depends on the stated enumeration argument and on the supplied script. It is not a short noncomputational classification proof. The result does **not** disprove unimodality for trivially perfect graphs, nor does it determine every larger-order exception. A pre-existing independently published first-counterexample census under an alternative class name remains a bibliographic risk; no such matching census was located in the specified searches. Independent mathematical validation has not been performed.

## References
1. Bilal Ahmad Rather, *On domination polynomials of some graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing **126** (2025), 279–289, DOI: 10.61091/jcmcc126-19, first verified public date 2025-06-24; see Theorem 2.16 and the subsequent open question. https://combinatorialpress.com/jcmcc-articles/volume-126/on-domination-polynomials-of-some-graphs/
2. Mohamed Omar, *New Perspectives on the Unimodality of Domination Polynomials*, arXiv:2601.14494, first submitted 2026-01-20; see Section 5 and Theorem 19. https://arxiv.org/html/2601.14494
3. Iain Beaton and Sam Schoonhoven, *On the unimodality of nearly well-dominated trees*, arXiv:2411.02288, first submitted 2024-11-04. https://arxiv.org/abs/2411.02288
