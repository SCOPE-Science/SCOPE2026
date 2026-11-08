# Nilpotent-base coronas have exactly threefold dyadic reversible-wave clocks

## Finding

Let \(H\) be any nonempty finite simple graph on \(n\) labelled vertices, and let \(B\) be its adjacency matrix over a finite field \(\mathbb F_q\) of characteristic two, where \(q=2^f\) and \(f\ge1\). Form the corona \(G=H\circ K_1\) by attaching exactly one new private leaf to every vertex of \(H\), and let \(A\) be its \(2n\)-by-\(2n\) adjacency matrix. Consider the reversible wave update

\[
T(u,v)=(Au+v,u),\qquad (u,v)\in\mathbb F_q^{2n}\times\mathbb F_q^{2n}.
\]

**Threefold-clock criterion.** The global permutation order of \(T\) is of the form \(3\cdot2^r\), with \(r\ge1\), **if and only if** \(B\) is nilpotent over \(\mathbb F_2\). (Nilpotence does not depend on the choice of characteristic-two extension field.)

When this criterion holds, let \(s_1,\ldots,s_b\) be the sizes of the nilpotent Jordan blocks of \(B\), and define

\[
r=\lceil\log_2(2\max_i s_i)\rceil,\qquad E_j=2\sum_{i=1}^{b}\min\{2s_i,2^j\}\quad(j\ge0).
\]

Then the order is **exactly** \(3\cdot2^r\). For every positive integer \(k\), the number of states fixed by \(T^k\) is exactly

\[
|\operatorname{Fix}(T^k)|=\begin{cases}1,&3\nmid k,\\q^{E_{\nu_2(k)}},&3\mid k,\end{cases}
\]

where \(\nu_2(k)\) is the exponent of two dividing \(k\). Consequently, the complete least-period census is

\[
P_1=1,\qquad P_3=q^{E_0}-1,\qquad P_{3\cdot2^j}=q^{E_j}-q^{E_{j-1}}\quad(1\le j\le r),
\]

with all other populations zero. Each displayed population is positive.

**Combinatorial criterion for trees.** If \(H\) is a tree, the threefold-clock condition is equivalent to requiring an even number of matchings of every positive size in \(H\). In particular, when \(H=P_{2^a-1}\) for any integer \(a\ge2\), the base adjacency has one nilpotent Jordan block of size \(2^a-1\), and the wave order is \(3\cdot2^{a+1}\). On the other hand, if \(H=Q_d\) is the Boolean cube of any even dimension \(d\ge2\), the wave order is always \(12\), independent of \(d\). Thus two unbounded connected base-graph families exhibit respectively unbounded and constant wave clocks under the same pendant-leaf construction.

For the path family, writing \(m=2^a-1\), its nonzero populations are explicitly

\[
P_1=1,\quad P_3=q^2-1,\quad P_{3\cdot2^j}=q^{2^{j+1}}-q^{2^j}\ (1\le j\le a),\quad P_{3\cdot2^{a+1}}=q^{4m}-q^{2^{a+1}}.
\]

For each even-dimensional cube family, writing \(n=2^d\), the nonzero populations are

\[
P_1=1,\quad P_3=q^n-1,\quad P_6=q^{2n}-q^n,\quad P_{12}=q^{4n}-q^{2n}.
\]

## Assumptions and scope

All graphs are finite, simple, and undirected. Disconnected and single-vertex base graphs are permitted. Every base vertex receives exactly one distinct pendant neighbor; no extra edges are inserted. All matrix arithmetic and dynamical configurations use the same finite field \(\mathbb F_q\) with characteristic two. The zero configuration is included. Least period means the smallest positive integer \(k\) for which \(T^k(u,v)=(u,v)\), with no transient: \(T\) is invertible on every finite field regardless of the nilpotence hypothesis. The equivalence concerns the precise *odd part* of the global order, not the mere fact that this order is finite.

## Proof

**1. Corona block and first Jordan doubling.** Order the old vertices first and their private leaves second. Then

\[
A=\begin{pmatrix}B&I_n\\I_n&0\end{pmatrix},\qquad
A^{-1}=\begin{pmatrix}0&I_n\\I_n&B\end{pmatrix}.
\]

Assume \(B\) is nilpotent with blocks \(J_{s_i}(0)\). A simultaneous basis change in the two \(n\)-vertex layers reduces \(A\) to a direct sum of matrices \(\begin{psmallmatrix}J_s(0)&I_s\\I_s&0\end{psmallmatrix}\). For one such summand the characteristic polynomial is \(\det((z^2+1)I_s+zJ_s(0))=(z+1)^{2s}\). Moreover, a vector \((x,y)\) is fixed by this summand exactly when \(y=x\) and \(J_s(0)x=0\). Its eigenspace therefore has dimension one. Since all its eigenvalues are one, its Jordan form consists of **one** block \(J_{2s}(1)\). Thus attaching a private leaf to every vertex doubles every nilpotent Jordan-block length and shifts the eigenvalue to one, without merging distinct blocks.

**2. Second Jordan lift.** The wave matrix is \(T=\begin{psmallmatrix}A&I_{2n}\\I_{2n}&0\end{psmallmatrix}\). Restrict to a Jordan block \(J_{2s}(1)\) of \(A\). Its wave companion has characteristic polynomial \((z^2+z+1)^{2s}\). The quadratic \(p(z)=z^2+z+1\) has two distinct roots \(\omega,\omega^2\) in a splitting field; both have multiplicative order three. For either root, the eigenspace equations give \(y=z^{-1}x\) and \(Ax=(z+z^{-1})x=x\), so the eigenspace is one-dimensional. Therefore, over the splitting field the wave companion has precisely one Jordan block of size \(2s\) for \(\omega\) and one of the same size for \(\omega^2\). This is a statement about Jordan chains, not just eigenvalue multiplicities.

**3. Order and all fixed spaces.** A nonzero characteristic-two Jordan block \(J_t(\omega)\) has order \(3\cdot2^{\lceil\log_2 t\rceil}\): its semisimple part has order three, while its unipotent part has exact order the smallest power of two at least \(t\). Taking the largest \(t=2s_i\) gives the asserted global order. If \(3\nmid k\), neither semisimple eigenvalue becomes one, so only the zero vector is fixed. If \(3\mid k\) and \(2^j\) is the exact power of two dividing \(k\), each of the two Jordan blocks of size \(2s_i\) contributes exactly \(\min\{2s_i,2^j\}\) to the nullity of \(T^k-I\). Extension of the field does not alter matrix rank. Hence the fixed-space dimension over \(\mathbb F_q\) is \(E_j\), giving the fixed-state formula.

**4. Exact primitive populations.** Every nonzero state has period divisible by three, and the order bound restricts it to one of \(3,6,12,\ldots,3\cdot2^r\). The zero vector is the unique fixed point. Since the periods are nested by divisibility, subtraction of consecutive fixed-state populations gives the displayed formulas. Strict increase of \(E_j\) until \(j=r\) follows from the largest Jordan block, so no listed population vanishes.

**5. Converse.** Both block companions satisfy the exact matrix identities

\[
A+A^{-1}=\operatorname{diag}(B,B),\qquad T+T^{-1}=\operatorname{diag}(A,A).
\]

Suppose \(T\) has order \(3\cdot2^r\) for some \(r\ge1\). In an algebraic closure all eigenvalues of \(T\) are cube roots of unity. Its eigenvalue cannot be one: that would force an eigenvalue zero of \(A\) by the second identity, whereas \(A\) is always invertible. Its eigenvalues are therefore exactly among \(\omega,\omega^2\), and every eigenvalue of \(A\) equals \(\omega+\omega^{-1}=1\). Thus \(A\) is unipotent. Then \(A+A^{-1}\) is nilpotent, so the first identity shows that \(B\) is nilpotent. This proves the equivalence even for disconnected base graphs.

**6. Tree and infinite-family consequences.** For a tree, the Leibniz expansion of \(\det(zI-B)\) contains only permutations made of fixed points and disjoint transpositions, which correspond to matchings. In characteristic two the polynomial is \(\sum_{j\ge0}m_jz^{n-2j}\), where \(m_j\) counts \(j\)-edge matchings. It equals \(z^n\) exactly when all \(m_j\) with \(j>0\) are even. For \(P_{2^a-1}\), the number of \(j\)-matchings is \(\binom{2^a-1-j}{j}\). When \(j>0\), the upper argument is the bitwise complement of \(j\) in \(a\) binary digits, so Lucas's binomial parity criterion makes each coefficient even. The path adjacency has one-dimensional kernel, hence exactly one nilpotent Jordan block of size \(2^a-1\). For an even-dimensional cube \(Q_d\), decompose its adjacency as \(B=\begin{psmallmatrix}C&I\\I&C\end{psmallmatrix}\), with \(C\) the \((d-1)\)-cube adjacency. Every cube adjacency satisfies \(C^2=(d-1)I\) in characteristic two, so \(C^2=I\) and \(B^2=0\). Solving \(B(x,y)=0\) gives \(y=Cx\), hence \(\operatorname{rank}(B)=2^{d-1}\); all its Jordan blocks therefore have size two. The general formulas give the two stated orders.

## Verification

The two separately implemented Python programs `checks/check_matrix.py` and `checks/check_orbits.py` use only the standard library and operate over the prime subfield \(\mathbb F_2\). The first enumerates **all 1,099 labelled simple graphs with one through five vertices**, identifies all 278 having nilpotent binary adjacency, and checks the entire claimed fixed-space formula by exact binary matrix powers and elimination at nine relevant times; it also checks the sharp operator order and examples \(P_3,P_7,P_{15},C_4,Q_4\). The second independently simulates **all 69,648 two-time-level states** of the leaf-decorated isolated vertex, \(P_3\), and \(C_4\), confirming their primitive-period histograms. All checks passed and their exact outputs are included. These finite tests check implementation and boundary cases but do not establish the general infinite-family theorem, which is proved above.

To reproduce, from the document root run `python3 checks/check_matrix.py` and `python3 checks/check_orbits.py`; compare stdout with the corresponding `.out` files. Field-extension values \(q=2^f\) require no separate rank calculation because extending a binary matrix's coefficient field preserves its rank.

## Relationship to prior work

Macfarlane (2004) established a matrix-based treatment of reversible second-order binary cellular automata; Steeb and Hardy (2007, especially their reversible-rule construction and discrete-wave example) similarly describe second-order wave rules on one-dimensional networks. Neither inspected accessible text supplies the corona-specific nilpotence criterion or full arbitrary-base primitive-period census. Barik, Pati and Sarma (2007), in Lemma 2.1 and Theorem 3.1, established adjacency and spectral transfer properties for graph coronas over the usual real spectrum. Their full accessible paper analyzes eigenvalues, reciprocal spectra, tree characterizations and Laplacian eigenvalues, but does not address characteristic-two Jordan chains or reversible-wave least-period populations. The exact matrix identity for the corona and its real-spectrum antecedent are acknowledged rather than claimed as new. A previously obtained dyadic-sunlet instance is subsumed here; its special-case count does not establish the general converse or the arbitrary nilpotent Jordan-block census.

## Limitations

The theorem requires characteristic two and exactly one private leaf per base vertex. It does not classify all possible orders when the base adjacency is not nilpotent; it only proves that no order of the specific form \(3\cdot2^r\) occurs then. The Macfarlane (2004) full text could not be independently obtained from accessible public copies, so a literature-priority risk remains; its publisher abstract, not an unread manuscript, supports the stated comparison. A search of publications and indexed mathematical findings cannot establish absolute priority, and algebraically equivalent presentations may exist elsewhere. No external independent mathematical validation is claimed.

## References

1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A: Mathematical and General **37** (2004), 10791–10814. DOI: 10.1088/0305-4470/37/45/006. First publisher availability: 28 October 2004.
2. S. Barik, S. Pati and B. K. Sarma, *The Spectrum of the Corona of Two Graphs*, SIAM Journal on Discrete Mathematics **21** (2007), 47–56. DOI: 10.1137/050624029. Published online: 12 January 2007.
3. W.-H. Steeb and Y. Hardy, *One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations*, Zeitschrift für Naturforschung A **62** (2007), 569–572. DOI: 10.1515/zna-2007-10-1103. Print publication: 1 November 2007.
4. R. Frucht and F. Harary, *On the Corona of Two Graphs*, Aequationes Mathematicae **4** (1970), 322–325. DOI: 10.1007/BF01844162.
