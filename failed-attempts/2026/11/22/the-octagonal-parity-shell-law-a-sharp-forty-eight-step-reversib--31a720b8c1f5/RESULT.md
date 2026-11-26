# The octagonal parity-shell law: a sharp forty-eight-step reversible-wave clock

## Finding

Let \(\mathcal O\) be any finite thick generalized octagon of order \((s,t)\), with \(s,t\ge2\) both even. Let \(G\) be its *point–line incidence graph*, and let \(A\) be its adjacency operator over \(\mathbb F_Q\), where \(Q=2^f\), \(f\ge1\). Define the reversible two-time-level map
\[
T(u,w)=(Au+w,u),\qquad u,w\in\mathbb F_Q^{V(G)}.
\]
The sharp universal adjacency minimal polynomial and global temporal order are
\[
 m_A(X)=X^7(X+1)^2,\qquad \operatorname{ord}(T)=48.
\]
Every positive divisor of \(48\) is realized as the least period of some state, already on a canonical eighteen-dimensional invariant radial-shell module. Thus no smaller common period works, and no exceptional additional periods occur.

There is also an exact *rank-resolved full orbit census*. For each positive integer \(n\), write \(a=v_2(n)\), and define
\[
\nu_0(r)=\dim_{\mathbb F_Q}\ker(A^r),\qquad
\nu_1(r)=\dim_{\mathbb F_Q}\ker((A+I)^r).
\]
Then the number of labelled paired states fixed by \(T^n\) is \(Q^{e(n)}\), with
\[
e(n)=
\begin{cases}
\nu_0(1)+2\mathbf1_{3\mid n}\nu_1(1),&a=0,\\
2\nu_0(2^{a-1})+2\mathbf1_{3\mid n}\nu_1(2^a),&a\ge1.
\end{cases}
\]
The number of primitive temporal orbits of any length \(n\) is
\[
\frac1n\sum_{d\mid n}\mu(n/d)Q^{e(d)}.
\]
It vanishes unless \(n\mid48\). The rank inputs need only \(\nu_0(1),\nu_0(2),\nu_0(4),\nu_0(7)\) and \(\nu_1(1),\nu_1(2)\); higher inputs are determined by nilpotent saturation.

## Assumptions and scope

A generalized octagon means a point–line incidence geometry whose connected bipartite incidence graph has diameter eight and girth sixteen. Every point has degree \(t+1\) and every line degree \(s+1\). The assumption that \(s\) and \(t\) are even makes both degrees odd. Every distance shell \(S_i(v)=\{x:d(v,x)=i\}\) for \(0\le i\le8\) is nonempty. No transitivity, group realization, planarity, or restriction to the smallest parameter pair is imposed. This covers the Ree–Tits generalized octagons of order \((q,q^2)\) and their duals, for suitable even \(q\). The statement is conditional on the existence of a finite generalized octagon with the stated parameters.

This is a characteristic-two, synchronous, linear, reversible dynamical system. The coordinate vector \(u\) is the current field-valued state, and \(w\) is the preceding state. The period of a state is the least strictly positive \(n\) with \(T^n(u,w)=(u,w)\); all states are periodic from time zero.

## Proof

**1. Exact radial-shell annihilator.** Fix an arbitrary vertex \(v\). Write \(\chi_i\) for the indicator of the vertices at graph distance \(i\) from \(v\), regarded as a vector over \(\mathbb F_Q\). Girth sixteen implies that a vertex at distance at most seven has a unique shortest path to \(v\). Thus at intermediate shells the unique backward neighbor contributes one, and the remaining forward neighbors contribute \(0\) modulo two, because every degree minus one is even. The exceptional first and last shells have all neighbors counted and odd degree. Consequently
\[
 A\chi_0=\chi_1,\quad A\chi_1=\chi_0+\chi_2,\quad
 A\chi_i=\chi_{i+1}\ (2\le i\le7),\quad A\chi_8=0.
\]
The identity at shell eight uses the fact that every neighbor of a distance-eight vertex lies in shell seven, so their odd number contributes one to \(A\chi_7\). There are no further shells.

The displayed relations imply
\[
\chi_2=(A^2+I)\chi_0,\qquad
\chi_i=A^{i-2}(A^2+I)\chi_0\ (2\le i\le8),
\]
and hence \(A^7(A^2+I)\chi_0=0\). Since the initial vertex was arbitrary, the same equation annihilates every coordinate basis vector:
\[
 A^7(A+I)^2=0.
\]
The nine vectors \(\chi_0,\ldots,\chi_8\) have nonempty disjoint supports and are linearly independent. The nine polynomials in \(A\) producing them from \(\chi_0\) are monic of distinct degrees zero through eight. Therefore no polynomial of degree at most eight annihilates \(\chi_0\), and the degree-nine annihilator is minimal. Thus \(m_A(X)=X^7(X+1)^2\) exactly. In particular, the generalized zero-primary component contains at least one Jordan block of size seven, and the generalized one-primary component at least one block of size two.

**2. Transfer to reversible temporal blocks.** Consider one adjacency primary block \(\mathbb F_Q[X]/(X^j)\), for \(1\le j\le7\). In the second-order temporal module, the temporal shift variable \(z\) obeys \(z^2+Xz+1=0\), so \(X=z+z^{-1}=(z+1)^2/z\). Since \(z\) is a unit, this yields the single temporal block \(\mathbb F_Q[z]/((z+1)^{2j})\). Its order is \(2^{\lceil\log_2(2j)\rceil}\); the longest adjacency zero-block therefore gives temporal order sixteen.

For a block \(\mathbb F_Q[X]/((X+1)^j)\), with \(1\le j\le2\), the same substitution gives \(X+1=(z^2+z+1)/z\). Its temporal module is \(\mathbb F_Q[z]/((z^2+z+1)^j)\). The polynomial \(z^2+z+1\) divides \(z^3+1\), and its square divides \(z^6+1\) but not \(z^3+1\); the largest such block has exact order six. Direct sum gives \(\operatorname{lcm}(16,6)=48\), with sharpness from the two required maximal blocks.

**3. Every primitive period and all counts.** The radial subspace spanned by \(\chi_0,\ldots,\chi_8\) is an invariant cyclic module \(\mathbb F_Q[X]/(X^7(X+1)^2)\). Its two-time-level copy decomposes into a fourteen-dimensional unipotent temporal block and a four-dimensional cubic-root temporal block. The unipotent block contains states with least periods \(1,2,4,8,16\), while the second contains states of least periods \(3,6\). Their direct sums realize every divisor \(1,2,3,4,6,8,12,16,24,48\) of forty-eight.

If \(n=2^a m\), \(m\) odd, then on the zero-primary adjacency blocks the dimension fixed by \(T^n\) is \(\sum_j c_j\min(2j,2^a)\), where \(c_j\) counts adjacency blocks of length \(j\) at zero. This equals \(\nu_0(1)\) when \(a=0\), and \(2\nu_0(2^{a-1})\) otherwise. On the one-primary blocks, fixed vectors exist only if \(3\mid n\), and their dimension is then \(2\sum_j d_j\min(j,2^a)=2\nu_1(2^a)\). Adding the two gives \(e(n)\), and a finite vector space of dimension \(e(n)\) has \(Q^{e(n)}\) elements. Möbius inversion subtracts smaller divisors to yield primitive states and division by the least period counts their orbits.

## Verification

Two independent self-contained Python scripts accompany this statement and require no external packages. Run with `python3 check_shell.py` and `python3 check_polynomial.py`.

`check_shell.py` represents the exact radial-shell operator by nine binary column masks, constructs the eighteen-dimensional wave map, proves the degree-nine minimal polynomial by exact rank tests and checks \(T^{48}=I\) while \(T^{24}\ne I\) and \(T^{16}\ne I\). It compares the derived fixed-space formula with exact kernel calculations for all divisors of forty-eight, then checks positive primitive-orbit counts for all ten possible periods. `check_polynomial.py` independently works in the quotient \(\mathbb F_2[X]/(X^9+X^7)\), uses a polynomial recurrence for temporal powers, and verifies the fixed-space formula by a different elimination implementation. Both return `PASS`.

These checks confirm the finite algebraic consequences of the *proved* incidence axioms. They are not an exhaustive enumeration of the vertices or the enormously many dynamical states of a Ree–Tits octagon; the general statement rests on the shell proof, not on finite sampled geometries. For the universal radial witness module over \(\mathbb F_2\), primitive-orbit counts by periods \(1,2,3,4,6,8,12,16,24,48\) are respectively \(2,1,2,3,9,30,15,1008,150,5040\). Those are witness-module counts, **not** full-octagon populations.

## Relationship to prior work

Finite generalized octagons and their even-order Ree–Tits instances are classical geometries. Schneider and Van Maldeghem (2007) define the relevant incidence geometry and show its structural context; De Bruyn (2015) proves a characterization of the order-\((2,4)\) example. Vlasov (2013) establishes the general second-order reversible construction, without the octagonal parity-shell identity or an octagonal temporal census. Other known finite incidence-graph wave classifications concern projective planes, partial geometries, quadrangles, or hexagons; their assertions about smaller incidence diameter do not determine the exact octagonal minimal polynomial. The combined period forty-eight is shared by some hexagonal systems, but the octagonal zero-primary Jordan chain has length seven rather than five. Consequently the rank-resolved fixed-state profiles can differ although the global clock coincides. This is a genuine dyadic clock plateau at two distinct incidence diameters.

## Limitations

The theorem assumes both incidence parameters even. It does not classify possible generalized octagons with other parameter parity, establish existence or uniqueness of any generalized octagon, or give closed parameter-only formulas for every code-dependent kernel rank. Those ranks are legitimate input invariants in the exact census, not unspecified conjectural values. An exhaustive historical-priority claim is not made: an earlier unindexed equivalent modular-incidence identity or wave classification may exist. Independent mathematical audit has not been performed.

## References

1. C. Schneider and H. Van Maldeghem, *Primitive flag-transitive generalized hexagons and octagons*, arXiv:0704.2845, first posted 21 April 2007. https://arxiv.org/abs/0704.2845
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first posted 18 November 2013. https://arxiv.org/abs/1311.4297
3. B. De Bruyn, *The uniqueness of a certain generalized octagon of order (2,4)*, Discrete Mathematics 338 (2015), 2125–2142, DOI:10.1016/j.disc.2015.04.022. https://biblio.ugent.be/publication/7140135
