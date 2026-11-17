# Coefficientwise parity reversal of chip-firing two-cycle masses under a Möbius ladder twist

## Finding

For each integer \(n\ge 3\), let \(P_n=C_n\square K_2\) be the labelled cubic prism, with columns indexed by \(\mathbb Z/n\mathbb Z\). Let \(M_n\) denote the labelled cubic Möbius ladder with the same columns and rungs, but with the two rail edges crossing at the seam between columns \(n-1\) and \(0\). Both graphs have \(2n\) vertices and \(3n\) edges. Under ordinary synchronous parallel chip firing, let
\[
C_G(z)=\sum_{\mathcal O\text{ primitive temporal two-orbit}}z^{m(\mathcal O)},
\]
where \(m(\mathcal O)\) is the conserved total nonnegative integer chip mass of either phase, with labelled orbit counted exactly once. Define \(D_n(z)=C_{P_n}(z)-C_{M_n}(z)\). Then the following *exact coefficientwise twist law* holds for all \(n\ge3\):
\[
\boxed{D_n(z)=2\mathbf1_{2\mid n}z^{5n}+(-1)^n\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}\bigl(z^{3n+2j}+z^{5n+2j}\bigr)(1+z)^{2n-4j}.}
\]
The displayed rational-looking binomial factor is always an integer. Consequently, **for every integer chip mass** \(k\) in the entire interval \(3n\le k\le7n\),
\[
\boxed{(-1)^n\bigl([z^k]C_{P_n}(z)-[z^k]C_{M_n}(z)\bigr)>0.}
\]
Outside this interval the discrepancy is exactly zero. Thus the ordinary prism has strictly more primitive two-orbits at *each* such mass for even \(n\); the Möbius ladder has strictly more at *each* such mass for odd \(n\). This is a coefficientwise statement, not just an inequality after summing all masses. Both mass polynomials are reciprocal about total mass \(5n\), and the coefficient of \(z^{5n}\) in their difference is exactly \(4\) for even \(n\) and \(-2\) for odd \(n\).

The first exact checks give orbit totals \((C_{P_n}(1),C_{M_n}(1))=(757,909),(10440,9794),(118681,121409),(1437410,1425852),(17032093,17081045)\) for \(n=3,4,5,6,7\), respectively. The full signed mass-distribution discrepancy is determined by the boxed formula, without a size cutoff.

## Assumptions and scope

All vertices and all rungs are labelled. Both graphs are connected, simple and degree three for \(n\ge3\). The dynamical state is a nonnegative integer number of chips at each vertex. At each synchronous update every vertex with at least three chips sends one chip to each of its three neighbors, simultaneously; all others wait. An orbit is primitive of temporal period two when it consists of two distinct configurations and the second update restores the first. We count one orbit, not its two phases separately. There is no sink, randomization or symmetry quotient. The polynomial variable \(z\) marks the total conserved chip mass. The statement does not count eventual two-cycles reached after a transient, and it does not classify primitive periods other than two.

## Proof

**1. Primitive two-orbits and cut-weighted chip intervals.** Let \(G\) be a finite connected undirected simple graph and let \(f_t(v)\in\{0,1\}\) indicate firing at \(v\) in round \(t\). If a state returns after two rounds, the vector \(f_0+f_1\) is harmonic for the graph Laplacian, hence constant by connectedness. The constant can be \(0,1,2\); if it is \(0\) or \(2\), all vertices respectively wait or fire in both rounds and the first update already fixes the state. For a primitive two-cycle the constant is \(1\), so the firing sets are complementary.

For its first-round firing set \(S\subseteq V(G)\), write \(c_v=|\{u\sim v:\mathbf1_S(u)\ne\mathbf1_S(v)\}|\). The first-round chip number at \(v\) belongs to the independent interval
\[
\begin{cases}
\{d(v),\ldots,d(v)+c_v-1\},&v\in S,\\
\{d(v)-c_v,\ldots,d(v)-1\},&v\notin S.
\end{cases}
\]
Indeed, a firing vertex loses precisely \(c_v\) chips in the first update, while a waiting vertex gains precisely \(c_v\); the opposite second-round threshold produces these inequalities. Conversely every choice from all the intervals guarantees that all vertices reverse their firing status, then return after the next update. A zero cut degree makes its interval empty. The total number of chips remains invariant across the two phases. For our cubic graphs define \([c]_z=1+\cdots+z^{c-1}\) if \(c\ge1\), with \([0]_z=0\). The mass contribution of a single vertex is
\[
h_{f,c}(z)=z^{3f+(1-f)(3-c)}[c]_z.
\]
The exact mass polynomial of the *states* with a specified first firing set is the product of these factors. Every primitive two-orbit contributes exactly twice to the sum over first firing sets, and at the same mass, hence the orbit polynomial is half that sum. This cut parametrization is established background; the new calculation concerns its mass-resolved change under a ladder seam twist.

**2. Width-two transfer and seam twist.** Set \(\mathcal B=\{00,01,10,11\}\). For three binary columns \(P,Q,R\in\mathcal B\), put
\[
c_s(P,Q,R)=[Q_s\ne P_s]+[Q_s\ne R_s]+[Q_s\ne Q_{1-s}],\qquad s\in\{0,1\},
\]
and \(w(P,Q,R;z)=\prod_{s=0}^1h_{Q_s,c_s(P,Q,R)}(z)\). The explicit \(16\times16\) polynomial transfer matrix, indexed by ordered column pairs, is
\[
T_{(P,Q),(U,R)}(z)=\mathbf1_{U=Q}\,w(P,Q,R;z).
\]
Let \(J\) exchange the top and bottom entries of *each* column in an ordered column pair. The local rule is row-exchange invariant, so \(TJ=JT\). The ordinary prism closure gives \(\frac12\operatorname{tr}(T(z)^n)\), whereas the crossed seam gives \(\frac12\operatorname{tr}(T(z)^nJ)\): each trace term corresponds to a unique indexed sequence of columns, with exactly its independent chip interval weight. Therefore
\[
C_{P_n}(z)=\tfrac12\operatorname{tr}(T(z)^n),\qquad C_{M_n}(z)=\tfrac12\operatorname{tr}(T(z)^nJ).
\]

**3. Six-dimensional antisymmetric characteristic factorization.** Four of the sixteen pair states are fixed by \(J\); the remaining twelve form six exchanged pairs. The \(-1\) eigenspace has basis \(e_s-e_{Js}\), one for each of these pairs, and is invariant under \(T\). Call the restricted matrix \(T_-(z)\). The exact antisymmetric restriction may be constructed from the preceding entry formula as
\[
(T_-)_{s,t}=T_{s,t}-T_{s,Jt}.
\]
Choose the six representatives, in order, \((00,01),(01,00),(01,01),(01,10),(01,11),(11,01)\). Direct polynomial determinant expansion gives the factorization
\[
\boxed{\det(\lambda I-T_-(z))=(\lambda^2-z^{10})(\lambda^2+\lambda z^3(1+z)^2-z^8)(\lambda^2+\lambda z^5(1+z)^2-z^{12}).}
\]
This is a finite exact polynomial identity, **not** an empirical extrapolation. `verify_symbolic.py` constructs the actual six-state matrix entries symbolically and recomputes its characteristic polynomial from the determinant, with no hard-coded six-state matrix or sampled interpolation. Since the plus/minus row-exchange traces differ by \(2\operatorname{tr}(T_-^n)\),
\[
D_n(z)=\operatorname{tr}(T_-(z)^n).
\]

**4. Trace powers and the explicit nonnegative coefficient expansion.** For a quadratic \(\lambda^2+a\lambda-b\), the sum of the \(n\)th powers of its two roots is \((-1)^nL_n(a,b)\), where \(L_0=2\), \(L_1=a\), and \(L_n=aL_{n-1}+bL_{n-2}\). The exact Lucas-polynomial expansion for \(n\ge1\) is
\[
L_n(a,b)=\sum_{j=0}^{\lfloor n/2\rfloor}\frac{n}{n-j}\binom{n-j}{j}a^{n-2j}b^j.
\]
This identity follows by induction in the displayed recurrence. The pair of linear eigenvalues \(\pm z^5\) contributes \((1+(-1)^n)z^{5n}\); the two remaining quadratics contribute \((-1)^nL_n(z^3(1+z)^2,z^8)\) and \((-1)^nL_n(z^5(1+z)^2,z^{12})\). Substitution in the Lucas expansion gives the first boxed formula verbatim.

Every coefficient in the finite sum after removal of its common sign \((-1)^n\) is nonnegative, and the term \(j=0\) already contains \(z^{3n}(1+z)^{2n}+z^{5n}(1+z)^{2n}\), which has strictly positive coefficients at **every** degree from \(3n\) through \(7n\). All other terms remain in that interval. The even-\(n\) central correction is positive, so the coefficientwise inequalities are strict precisely throughout that interval. At the central exponent, each \(j=0\) term contributes one and all \(j>0\) terms miss it; adding the even correction gives the claimed \(4\) or \(-2\).

**5. Mass reciprocity.** On either cubic graph, every vertex of a primitive two-state has a chip height between zero and five. The map \(x(v)\mapsto5-x(v)\) interchanges its two possible first-round firing patterns while preserving the cut degrees and the two-step dynamics. It sends total chip mass \(k\) to \(10n-k\), establishing \(C_G(z)=z^{10n}C_G(z^{-1})\) for both graphs. The displayed discrepancy expression has the same reciprocity.

## Verification

Run `python3 verify_symbolic.py` with SymPy to construct the complete polynomial sixteen-state transfer and its row-swap antisymmetric restriction, factor the exact characteristic polynomial, and compare symbolic traces against the Lucas formula for lengths three through eight. The script also checks the strict sign of every coefficient on the claimed support for those lengths.

Run `python3 verify_direct.py` using only the Python standard library. It constructs both cubic graphs as explicit adjacency lists, independently enumerates every binary first-round firing set for lengths three through seven, multiplies the allowed chip-height polynomials, and compares the resulting mass histograms against the closed formula. At lengths three and four it additionally enumerates each individual corresponding chip configuration and runs the **original two synchronous chip-firing steps**, checking primitivity, mass conservation and exact recovery. The programs use different representations; their outputs are recorded in `symbolic_output.txt` and `direct_output.txt`. These finite checks corroborate, but do not substitute for, the all-size transfer and exact characteristic-identity proof.

## Relationship to prior work

The foundational parallel chip-firing work of Bitar–Goles introduces periodic behavior of this graph dynamical model. Jiang–Scully–Zhang's 2012 full-text study establishes restrictions on firing patterns, but neither its results nor its period descriptions provide a mass-resolved comparison of the two cubic closures. The previously published *A parity-reversing twist law for period-two chip-firing orbits on cubic ladders* gives the **unweighted** signed difference \(C_{P_n}(1)-C_{M_n}(1)\), with exact opposite signs for odd and even sizes, and supplies the unweighted transfer setup. The present claim is a genuinely stronger energy-resolved statement: it proves the same sign at **each individual chip mass**, specifies all its nonzero coefficients, and shows that even the central coefficient is independent of size. A single evaluated count at \(z=1\) neither determines nor implies these assertions. The separate published maximum-cut support law supplies general mass endpoints and reciprocity, but not coefficientwise inequalities for distinct graphs. Searches for mass-polynomial, fixed-energy, Möbius-twist and equivalent seam-sign formulations found no source dominating the complete claimed coefficientwise comparison. Historical priority remains subject to literature not indexed or available in full text.

## Limitations

Only immediately primitive temporal two-orbits of the undissipated synchronous degree-threshold model are included. The theorem compares orbit populations at equal chip mass, **not** their normalized conditional probability laws, nor the eventual dynamical basins. The general cut decomposition and unweighted twist sign are prior results; originality is asserted only for the exact coefficientwise mass difference. Historical priority and any independent mathematical assessment remain open. The determinant identity is supplied by an explicit small matrix definition and verifiable symbolic computation rather than a separate manual term-by-term expansion.

## References

1. J. Bitar and E. Goles, *Parallel Chip Firing Games on Graphs*, Theoretical Computer Science 92 (1992), 291–300, DOI:10.1016/0304-3975(92)90316-8; indexed publication date 1992-01-20, https://pure.uai.cl/en/publications/parallel-chip-firing-games-on-graphs/.
2. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first arXiv posting 2012-11-29, arXiv:1211.6786, https://arxiv.org/abs/1211.6786.
3. *A parity-reversing twist law for period-two chip-firing orbits on cubic ladders*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-a-parity-reversing-twist-law-for-period-two-chip-firing-orbits-o--3e46c74462fe.
4. *Maximum-cut law for primitive-two chip-firing energy spectra*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-maximum-cut-law-for-primitive-two-chip-firing-energy-spectra--f554059647ef.
