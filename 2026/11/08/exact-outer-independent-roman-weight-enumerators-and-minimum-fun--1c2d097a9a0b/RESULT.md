# Exact outer-independent Roman weight enumerators and minimum-function multiplicities on rook graphs

## Finding
For every pair of integers \(m,n\ge2\), set \(R_{m,n}=K_m\square K_n\), \(N=mn\), \(s=\min(m,n)\), and \(R(k)=\binom mk\binom nk k!\). The polynomial \(W_{m,n}(z)=\sum_f z^{\omega(f)}\), summing over **all labelled outer-independent Roman dominating functions**, is

\[
\boxed{W_{m,n}(z)=\sum_{k=0}^{s}R(k)\sum_{t=0}^{k}(-1)^t\binom kt z^{t(m+n-t-1)}(z+z^2)^{N-k-t(m+n-t-1)}.}
\]

Put \(h=\lfloor s/2\rfloor\). The minimum weight is \(N-h\), and the number \(C_{m,n}\) of minimum-weight functions is exactly

\[
\boxed{C_{m,n}=\begin{cases}
R(s)\dfrac{s!}{h!},&s=2h,\\[4pt]
\dfrac{R(s-1)(s-1)!+R(s)s!(m+n-s-1)}{h!},&s=2h+1.
\end{cases}}
\]

For all \((m,n)\ne(2,2)\), the same polynomial enumerates the outer-independent **total** Roman dominating functions. For \((m,n)=(2,2)\), the total-function enumerator is exactly \(W_{2,2}(z)-4z^3-2z^4\). In particular, the full polynomial and the multiplicities strictly refine the previously known scalar minimum. For instance, \(W_{3,3}(z)\) has lowest term \(108z^8\), whereas \(W_{3,4}(z)\) has lowest term \(504z^{11}\).

## Assumptions and scope
The vertices are ordered pairs \((i,j)\), \(1\le i\le m\), \(1\le j\le n\), with two distinct vertices adjacent precisely when they agree in exactly one coordinate. A function \(f:V\to\{0,1,2\}\) is outer-independent Roman dominating when its zero set is independent and every zero has a neighbor labelled \(2\). Its weight is \(\omega(f)=\sum_{v\in V}f(v)\). For the **total** variant, the subgraph induced by all positive-labelled vertices must also have no isolated vertex. All vertices are distinguished; no automorphism quotient is taken. The claimed formulas hold for every integer \(m,n\ge2\), with no asymptotic or parity assumption beyond the displayed cases.

## Proof
**1. Count the zero configurations.** An independent vertex set in the rook graph is exactly a collection of pairwise nonattacking rooks. For any \(0\le k\le s\), exactly \(R(k)=\binom mk\binom nk k!\) zero sets have size \(k\). Once a zero set \(Z\) is fixed, every nonzero vertex receives label \(1\) or \(2\), and each zero must see some label \(2\).

**2. Count simultaneous neighborhood restrictions.** Fix \(t\) distinct zeros. Their rows and columns are all distinct. For each of those zeros, its open neighborhood contains its other \(m+n-2\) row/column vertices. The union of the \(t\) open neighborhoods contains precisely

\[
a_t=t(m+n-t-1)\]

vertices: these are the cells in one of the \(t\) occupied rows or columns, except the \(t\) diagonal zero cells themselves and the additional zeros outside the chosen \(t\) (which lie outside those rows/columns). More directly, the cells in the union of the selected rows and columns number \(tn+tm-t^2\), and deleting the \(t\) selected zeros gives \(t(m+n-t-1)\). The union contains no other zero, since all zeros are pairwise nonattacking. If all these \(a_t\) vertices are forbidden from carrying label \(2\), they are forced to carry label \(1\), contributing \(z^{a_t}\). The remaining \(N-k-a_t\) nonzero vertices independently contribute \(z+z^2\). By inclusion–exclusion over the \(k\) zero vertices, this yields the inner sum in the first displayed formula. Multiplying by \(R(k)\) and summing over \(k\) proves the exact polynomial.

**3. Determine the minimum and all minimizing functions.** A label-\(2\) cell can be adjacent to at most two nonattacking zeros: at most one in its row and one in its column. Thus if there are \(k\) zeros, at least \(\lceil k/2\rceil\) cells must carry label \(2\), and
\[\omega(f)=N-k+|f^{-1}(2)|\ge N-\lfloor k/2\rfloor\ge N-h.\]
The bound is attained by arranging a maximum-size nonattacking zero set and placing labelled-\(2\) cells at the cross-cells of pairs of zeros (and, if necessary, one further neighbor), assigning label \(1\) to all other nonzeros.

When \(s=2h\), equality forces \(k=s\) and exactly \(h\) defenders, each adjacent to two zeros. For a given zero set, their adjacencies form a perfect matching on its \(s\) zeros. Such a matching has \(s!/(2^h h!)\) choices, and for each paired pair there are two distinct cross-cells in which to place the defender. Hence there are \(s!/h!\) optimal assignments per zero set.

When \(s=2h+1\), equality allows \(k=s-1=2h\) with \(h\) defenders, or \(k=s=2h+1\) with \(h+1\) defenders. The former contributes \(R(s-1)(s-1)!/h!\). For the latter, the graph whose vertices are the zeros and whose edges correspond to the two-zero defenders has \(h+1\) edges, covering all \(2h+1\) zeros with at most one duplicated incidence. There are exactly two disjoint cases:

(a) One zero is covered by a one-zero defender, while the others are paired. The number of choices per zero set is \((s!/h!)(m+n-2s)\): a one-zero defender must occupy a cell in the singleton's row with an unused column, or in its column with an unused row, while the remaining zeros are paired and their cross-cells oriented.

(b) Every defender covers two zeros, so precisely one zero is covered twice; two edges form a length-two path through that zero, and the other \(s-3\) zeros form a matching. Choosing its middle and its two endpoints, pairing the others, and assigning one of the two cross-cells to each edge gives \(2(s!)/(h-1)!=2h(s!/h!)\) choices. Adding (a) and (b) gives \((s!/h!)(m+n-s-1)\). Summing the two possible zero sizes proves the odd case. All cases are disjoint, and every optimal assignment is counted once.

**4. Total version and the smallest boundary.** If \(\max(m,n)\ge3\), every row (when \(n\ge3\)) or every column (when \(m\ge3\)) contains at least two positive-labelled vertices, since it contains at most one zero. Therefore every positive vertex has a positive neighbor. The total condition is automatic. In \(R_{2,2}=C_4\), a positive vertex becomes isolated exactly when the two zeros form an opposite pair and the other two positive vertices also form an opposite pair. There are two possible zero pairs, and each allows the three positive-label assignments \((1,2),(2,1),(2,2)\) with at least one \(2\). Their weights give exactly \(4z^3+2z^4\), as stated.

## Verification
A standalone Python script `verification/verify_rook_outer_independent_roman.py` reconstructs each rook graph and applies the literal labeling conditions. It directly enumerates all \(3^{mn}\) labelings in five small profiles, comparing every weight coefficient with the formula and the minimum multiplicity. It separately checks total-function equivalence and the four-cycle boundary. It also verifies the minimum multiplicity against the symbolic polynomial for 44 additional parameter profiles and samples 60,000 reproducible labelings on larger graphs. Finite tests are consistency checks, not proof of the unrestricted formula. Run with `python3 verification/verify_rook_outer_independent_roman.py` from the extracted package directory.

## Relationship to prior work
Cabrera Martínez, Kuziak and Yero established the scalar outer-independent **total** Roman domination number of \(K_m\square K_n\) in Theorem 3.4 of their work first publicly posted on 2021-12-10: \(mn-\lfloor\min(m,n)/2\rfloor\). Their theorem does not enumerate the functions of each weight or characterize the number attaining the minimum. The exact weight-enumerator and parity-dependent multiplicity formula are the present contribution; the scalar minimum is explicitly treated as prior coverage. Related enumerators for complete multipartite graphs are not equivalent to rook graphs, whose adjacency is by shared row or column rather than between distinct independent parts.

## Limitations
The classification is restricted to Cartesian products of two complete graphs and to the stated Roman variants. It does not classify arbitrary products or general domination polynomials. The 2020 foundational outer-independent Roman article was accessible by abstract and descriptive material but not by complete full text from one route; independent literature verification remains important. Standard rook-polynomial identities and inclusion–exclusion are classical; originality concerns their combined exact weight distribution and minimum multiplicities for this invariant, not the underlying elementary tools. There has been no independent mathematical audit.

## References
1. A. Cabrera Martínez, D. Kuziak and I. G. Yero, *Relating the outer-independent total Roman domination number with some classical parameters of graphs*, arXiv:2112.05476v1 (publicly submitted 2021-12-10), subsequently *Mediterranean Journal of Mathematics* 19, article 144 (2022), DOI:10.1007/s00009-022-02061-y; especially Theorem 3.4 and Section 3.3.
2. A. Cabrera Martínez, S. Cabrera García, A. Carrión García and A. M. Grisales Del Rio, *On the Outer-Independent Roman Domination in Graphs*, *Symmetry* 12 (2020), article 1846, DOI:10.3390/sym12111846.
