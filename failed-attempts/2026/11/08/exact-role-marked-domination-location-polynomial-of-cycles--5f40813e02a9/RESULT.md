# Exact role-marked domination–location polynomial of cycles

## Finding
For every labelled cycle \(C_n\) with \(n\ge5\), let \(P_n(z)\) enumerate ordered complementary pairs \((L,D)\), weighted by \(z^{|L|}\), where \(L\) is a locating-dominating set and \(D\) is a dominating set. Such pairs are in bijection with cyclic binary words avoiding the three factors \(000\), \(111\), and \(00100\), where \(1\) marks \(L\).

Let \(M(z)\) be the explicit 16-state transfer matrix defined below. Then
\[
P_n(z)=\operatorname{tr}(M(z)^n),\qquad
\det(xI-M(z))=x^{10}\bigl(x^6-zx^4-z^2x^3-z^2x^2-z^2x-z^3\bigr).
\]
In particular, for every \(n\ge11\),
\[
P_n(z)=zP_{n-2}(z)+z^2P_{n-3}(z)+z^2P_{n-4}(z)
+z^2P_{n-5}(z)+z^3P_{n-6}(z).
\]
Equivalently, for every \(n\ge5\) the coefficient of \(u^n\) in the rational function
\[
\frac{2zu^2+3z^2u^3+4z^2u^4+5z^2u^5+6z^3u^6}{1-zu^2-z^2u^3-z^2u^4-z^2u^5-z^3u^6}
\]
is \(P_n(z)\). This follows from the trace/log-determinant identity and \(\det(I-uM(z))=1-zu^2-z^2u^3-z^2u^4-z^2u^5-z^3u^6\).

The six initial polynomials are
\[
\begin{aligned}
P_5&=5z^2+5z^3,\\
P_6&=14z^3+3z^4,\\
P_7&=7z^3+14z^4,\\
P_8&=30z^4+8z^5,\\
P_9&=18z^4+36z^5+3z^6,\\
P_{10}&=5z^4+62z^5+25z^6.
\end{aligned}
\]
The smallest and largest possible locating-dominating class sizes are, respectively,
\[
\min |L|=\left\lceil\frac{2n}{5}\right\rceil,
\qquad \max |L|=\left\lfloor\frac{2n}{3}\right\rfloor
\quad(n\ge5).
\]
Writing \(T_n=P_n(1)\), the total number of role-marked partitions obeys
\[
T_n\sim\rho^n,
\]
where \(\rho=1.57014731219605\ldots\) is the unique positive root of
\(x^5-x^4-x^2-1=0\).

## Assumptions and scope
Throughout \(C_n\) is the simple graph on the fixed labelled vertex set \(\mathbb Z/n\mathbb Z\), joining consecutive residues, with \(n\ge5\). A set \(S\) dominates if each vertex outside \(S\) has a neighbor in \(S\). A locating-dominating set \(L\) dominates and assigns distinct nonempty signatures \(N(v)\cap L\) to distinct vertices \(v\notin L\). The complementary set is \(D=V(C_n)\setminus L\). The order of the roles matters: a partition admissible in both orientations contributes twice, once for each choice of locating class. Rotations and reflections of labelled vertices are not identified. Both classes must be nonempty (which the local constraints ensure).

## Proof
**1. Exact local characterization.** Put \(b_i=1\) when \(i\in L\) and \(b_i=0\) when \(i\in D\). The assertion that \(L\) dominates every vertex of \(D\) excludes cyclic \(000\), and the assertion that \(D\) dominates every vertex of \(L\) excludes cyclic \(111\). In \(C_n\) with \(n\ge5\), two distinct vertices have a common neighbor only when their cyclic distance is two; then their common neighbor is unique. Therefore, if two vertices of \(D\) have equal nonempty signatures in \(L\), they must be the two neighbors of some vertex in \(L\), and neither can have its other neighbor in \(L\). This is exactly the cyclic five-bit pattern \(00100\) centered at that selected vertex. Conversely, a cyclic \(00100\) gives two different vertices in \(D\) with the same singleton signature. Thus avoidance of all three listed words is necessary and sufficient.

**2. Explicit transfer matrix and characteristic polynomial.** Index rows and columns by the sixteen words \(a=(a_0,a_1,a_2,a_3)\in\{0,1\}^4\). The only possible nonzero entry from \(a\) is to \(a'=(a_1,a_2,a_3,t)\) for \(t\in\{0,1\}\). Set that entry to \(z^t\) precisely when \((a_2,a_3,t)\notin\{000,111\}\) and \((a_0,a_1,a_2,a_3,t)\ne00100\), and otherwise set it to zero. A closed walk of length \(n\) uniquely corresponds to a cyclic length-\(n\) binary word with a fixed starting vertex, and its weight is \(z\) raised to the total number of ones. Hence \(P_n(z)=\operatorname{tr}(M(z)^n)\), with no rotational quotient, for all \(n\ge5\). Direct exact expansion of the determinant of this specified 16-by-16 matrix gives the displayed characteristic polynomial. The attached verifier reconstructs its entries and rechecks the determinant by symbolic algebra. The ten zero eigenvalues contribute zero to traces of positive powers; the remaining sextic factor supplies the displayed six-term trace recurrence. Direct trace expansion gives the six initial polynomials. In particular, every coefficient in the recurrence is nonnegative, so there is no cancellation between attainable sizes.

**3. Extremal class sizes.** Let \(m_n\) and \(M_n\) be the least and greatest nonzero degrees of \(P_n\), respectively. The six base polynomials show \(m_n=\lceil2n/5\rceil\) and \(M_n=\lfloor2n/3\rfloor\) for \(5\le n\le10\). Since all recurrence summands have nonnegative coefficients, \(m_n\) is the minimum of \(m_{n-2}+1,m_{n-3}+2,m_{n-4}+2,m_{n-5}+2,m_{n-6}+3\). Every term is at least \(\lceil2n/5\rceil\), and the term indexed by \(n-5\) equals it. Likewise \(M_n\) is the maximum of the same five shifted maxima, every term is at most \(\lfloor2n/3\rfloor\), and the term indexed by \(n-3\) equals it. Induction proves both exact bounds for every \(n\ge5\).

**4. Asymptotic total count.** At \(z=1\), the nonzero characteristic factor is \((x+1)(x^5-x^4-x^2-1)\). Its positive root \(\rho>1\) is unique because \(1=x^{-2}+x^{-3}+x^{-4}+x^{-5}+x^{-6}\) has a strictly decreasing right-hand side for positive \(x\). For any complex root \(w\) of the sextic, the triangle inequality gives \(|w|^6\le |w|^4+|w|^3+|w|^2+|w|+1\), hence \(|w|\le\rho\). Equality in this inequality forces the phases of \(w^4,w^3,w^2,w,1\) to agree; the last two terms force \(w\) to be positive real, whence \(w=\rho\). Thus \(\rho\) is simple and strictly dominant. The trace is the sum of eigenvalue powers, counted with algebraic multiplicity, so \(P_n(1)=\rho^n+o(\rho^n)\).

## Verification
The accompanying standalone `verify.py` specifies the entire matrix and tests its exact symbolic characteristic polynomial. It independently tests every labelled subset against the graph-neighborhood definitions, and independently against the forbidden words, for all \(5\le n\le16\). It compares the full weighted transfer trace against those independent enumerations, verifies the recurrence for \(11\le n\le39\), and verifies the asserted support endpoints. Reproduce with `python verify.py` in an environment with Python 3 and SymPy. The graph-enumeration checks are finite corroboration; the all-order statements follow from the proof above.

## Relationship to prior work
Chakraborty, Foucaud, Henning and Laihonen [1] prove that **every** graph without isolated vertices admits a partition into a dominating set and a locating-dominating set (Theorem 6). Their result is an existence and construction theorem, not a labelled counting polynomial. Foucaud, Maniya, Paul and Pradhan [2] prove existence of partitions into **two locating-dominating sets** for specific graph families. Requiring both parts to locate is stronger than the condition counted here, and the existence result does not determine the count of partitions with one merely dominating side. The present theorem enumerates all role-marked partitions of cycles and determines the entire cardinality spectrum, exact extremal sizes and growth rate. Searches and literature comparisons do not establish exhaustive historical priority.

## Limitations
This result is restricted to labelled simple cycles of order at least five, with the locating-dominating side distinguished. It does not claim results for the special cycles of orders three and four, unmarked bipartitions, automorphism orbits, arbitrary graphs, or two-sided locating partitions. Historical priority remains provisional pending broader independent literature comparison.

## References
[1] D. Chakraborty, F. Foucaud, M. A. Henning and T. Laihonen, “A Note on Partitioning the Vertex Set of a Graph into a Dominating Set and a Locating Dominating Set,” *Electronic Journal of Combinatorics* 33(1), P1.51 (published 2026-03-13), DOI: 10.37236/14049. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i1p51

[2] F. Foucaud, P. V. Maniya, K. Paul and D. Pradhan, “Locating-dominating partitions for some classes of graphs,” *Discrete Mathematics* 349 (2026), 114886, DOI: 10.1016/j.disc.2025.114886. https://perso.limos.fr/ffoucaud/Publications/Papers/J60_Locating-dominating-partitions_DM_2026.pdf
