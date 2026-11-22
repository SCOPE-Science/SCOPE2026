# Sharp first loss of unimodality in classwise-random one-point type spectra

## Finding

Let \(M\) be the Fraïssé limit of finite structures in the relational language \(\{E,R\}\), where \(E\) is an equivalence relation, \(R\) is an irreflexive symmetric graph relation, and \(R(u,v)\) implies \(E(u,v)\). For every nonempty, individually named finite substructure \(A\subset M\), suppose its represented \(E\)-classes have positive sizes \(a_1,\ldots,a_k\), with \(n=\sum_i a_i\). Let \(c_j(A)\) be the number of complete nonalgebraic singleton types over \(A\) in which the new point is \(R\)-adjacent to exactly \(j\) named points, and put \(P_A(z)=\sum_{j\ge0}c_j(A)z^j\).

**Theorem.** For every such \(A\),
\[
P_A(z)=1+\sum_{i=1}^{k}(1+z)^{a_i},\qquad
c_0=k+1,\quad c_j=\sum_{i=1}^k\binom{a_i}{j}\quad (j\ge1).
\]
All these coefficient sequences are unimodal when \(n\le15\). At \(n=16\), the **only** nonunimodal unordered class-size profile is \((6,1,1,1,1,1,1,1,1,1,1)\). Its coefficient sequence is
\[
(12,16,15,20,15,6,1),
\]
with the strict valley \(16>15<20\). For every \(n\ge16\), the profile consisting of one class of size six and \(n-6\) singleton classes is nonunimodal. These assertions hold independently of the graph induced by \(R\) inside each named class.

Here *unimodal* means that the finite coefficient sequence first weakly increases and then weakly decreases; a constant plateau is allowed.

## Assumptions and scope

The equivalence relation and graph relation are part of the language, and every named base is considered pointwise fixed. The age has hereditary and joint embedding properties. For amalgamation, form the equivalence closure of the two existing equivalences over the common part, retaining old edges and adding no cross-amalgam edges; this preserves \(R\subseteq E\). Thus it has a countable homogeneous Fraïssé limit. Each represented equivalence class induces a copy of the countable random graph, and there are infinitely many further classes. Homogeneity in the finite relational language makes finite one-point extension diagrams the complete nonalgebraic singleton types over \(A\).

All class sizes are positive integers; \(n\ge1\). No special assumption is made about internal edges of \(A\). A type's grade is the number of its adjacent named vertices, not the number in its equivalence class.

## Proof

**1. Exact extension count.** A new point either belongs to an entirely new \(E\)-class, which forces nonadjacency to all named points (one type of grade zero), or belongs to exactly one of the \(k\) represented classes. In a represented class of size \(a_i\), every one of the \(2^{a_i}\) choices of neighbors among those \(a_i\) points is realizable, independently of the old graph inside that class; no edge may go to another class. Distinct class choices and distinct adjacency choices give distinct complete types. This proves the polynomial identity and coefficient formulas.

**2. A backward-rise lemma through sixteen points.** Suppose \(n\le16\), \(j\ge3\), and \(c_{j+1}>c_j\). The identity
\[
\binom{a}{j+1}-\binom{a}{j}
=\frac{a-2j-1}{j+1}\binom{a}{j}
\]
shows that some represented class has size \(b\ge2j+2\). Choose a largest such class, and write \(r=n-b\). Its contribution to \(c_j-c_{j-1}\) is at least
\[
\Delta_j(b)=\binom{b}{j}-\binom{b}{j-1}
\ge\binom{2j+2}{j}-\binom{2j+2}{j-1}>0.
\]
The inequality in \(b\) holds since \(\Delta_j(b+1)-\Delta_j(b)=\binom{b}{j-1}-\binom{b}{j-2}>0\) for \(b\ge2j+2\). All other classes together can contribute at worst
\[
-\sum_{i\ne b}\binom{a_i}{j-1}\ge-\binom{r}{j-1},
\]
because subsets lying inside a single other class are among all \((j-1)\)-subsets of the remaining \(r\) named vertices.

For \(j=3\), \(b\ge8\) and \(r\le8\). The distinguished class contributes at least \(28\), versus a potential loss of at most \(\binom82=28\). Equality cannot occur: if \(b=8\) and the other eight points make one class, that class has contribution \(\binom83-\binom82=28>0\); splitting them makes the loss bound strict. If \(b>8\) or \(r<8\), the bound is already strict. For \(j=4\), \(b\ge10\) gives a gain at least \(90\), versus loss at most \(\binom63=20\). For \(j=5\), \(b\ge12\) gives a gain at least \(297\), versus loss at most \(\binom44=1\). For \(j\ge6\), \(b\ge14\), so \(r\le2<j-1\) and there is no possible loss. Hence
\[
\boxed{\ n\le16,\ j\ge3,\ c_{j+1}>c_j\quad\Longrightarrow\quad c_j>c_{j-1}.\ }
\]
The lemma also covers zero coefficients and end ranges by the convention \(\binom{a}{j}=0\) when \(j>a\).

**3. The only possible first valley.** If \(k=n\), all classes are singletons, and \(P_A(z)=(n+1)+nz\) is decreasing. Otherwise \(k\le n-1\), so \(c_0=k+1\le n=c_1\), ruling out a first descent at grade zero. The backward-rise lemma rules out any first rise after a prior descent at a gap of index \(j\ge3\), since repeated application propagates each such rise backward through all gaps of index at least two. Thus a nonunimodal sequence with \(n\le16\) must have \(c_1>c_2<c_3\).

For \(c_3>c_2\), the identity in step 2 with \(j=2\) forces some class of size at least six. Hence \(c_2\ge\binom62=15\). If \(n\le15\), then \(c_1=n\le15\le c_2\), contradicting the required descent \(c_1>c_2\). This proves unimodality for every \(n\le15\).

For \(n=16\), the simultaneous conditions \(c_1>c_2\) and \(c_3>c_2\) imply \(c_2=15\). Consequently the class of size at least six has size exactly six, and all other classes are singletons, because any further class of size at least two would increase \(c_2\). The sum of class sizes forces exactly ten singleton classes. Substitution yields the displayed polynomial, confirming that this one profile really fails unimodality.

**4. Every larger order.** For \(n\ge16\), take the profile \((6,1^{n-6})\). Its coefficients at grades one, two and three are \(n,15,20\). Therefore it contains the strict valley \(n>15<20\). This is an explicit infinite family, with no inference from finite experiments.

## Verification

Run \(\texttt{python3 VERIFY.py}\) using only Python 3 standard-library facilities. The checker enumerates every integer partition of \(n\) for \(1\le n\le16\) (914 profiles), verifies exactly one nonunimodal profile at \(n=16\), and independently enumerates permissible one-point relational extension diagrams for every profile through \(n=8\), comparing their grade distribution with the formula. It also checks the witness family for orders 16 through 100 and emits \(\texttt{VERIFY\_OK}\). The recorded output is in \(\texttt{VERIFY_OUTPUT.txt}\). This finite verification corroborates the entirely separate all-size proof above; it is not treated as an infinite certificate.

## Relationship to prior work

The polynomial is directly related to the classical independence polynomial of the complete multipartite graph with part sizes \((a_i)\):
\[
P_A(z)=I(K_{a_1,\ldots,a_k};z)+k.
\]
This identity and the individual polynomial coefficients are **not** originality claims. Zhu and Lu's 2015 preprint, published in 2017, gives the complete-multipartite independence-polynomial formula, sufficient conditions for unimodality and log-concavity, and a nonunimodal example with 26 singleton parts and one eight-point part (34 vertices). Its Theorem 3.1 and Remark 3.4 do not determine the least possible order, the unique minimal class profile, or the persistence construction for the type polynomial with its changed constant term. Levit and Mandrescu's earlier work provides other nonunimodal independence-polynomial examples, but not this sharp classwise criterion. The new assertion is only the exact sixteen-parameter threshold and extremal uniqueness for the graded singleton-type spectra, along with the elementary structural explanation.

## Limitations

Only one-point complete types and the particular homogeneous graph-with-equivalence structure are covered. No claim is made about arbitrary complete multipartite graph polynomials beyond the stated shifted correspondence, higher-arity type spectra, or other relational reducts. The historical originality comparison is necessarily provisional; an unindexed equivalent minimal-order theorem could exist. No independent mathematical audit has been carried out.

## References

- B.-X. Zhu and Q. Lu, *Unimodality of the Independence Polynomials of Some Composite Graphs*, arXiv:1507.05754 (initial posting 2015-07-21); *Filomat* 31 (2017), 629–637, doi:10.2298/FIL1703629Z. Particularly Section 3, Theorem 3.1 and Remark 3.4. https://arxiv.org/abs/1507.05754
- V. E. Levit and E. Mandrescu, *Independence polynomials of well-covered graphs: generic counterexamples for the unimodality conjecture*, arXiv:math/0309151 (initial posting 2003-09-08), *European Journal of Combinatorics* 27 (2006), 931–939. https://arxiv.org/abs/math/0309151
- E. W. Weisstein, *Clique Polynomial*, MathWorld (reference for the standard clique/independence-polynomial transformation). https://mathworld.wolfram.com/CliquePolynomial.html
