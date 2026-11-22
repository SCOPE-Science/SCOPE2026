# A missing biclique edge switches parity dynamics among extinction, two-cycles and six-cycles

## Finding

Let \(m,n\ge 2\), let \(G=K_{m,n}-uv\) be the complete bipartite graph with exactly one cross-edge \(uv\) deleted, and let \(B\) be its loop-free adjacency matrix over a finite field \(\mathbb F_q\), \(q=2^h\) with \(h\ge1\). At each synchronous time step all vertices replace their states by the sum of their neighbors' states; thus \(x(t+1)=Bx(t)\). Put \(N=m+n\). The full periodic and transient classification depends only on the parities of \(m,n\), as follows.

| Shore parities | Recurrent dimension | Exact possible least periods | Exact global identity | Sharp maximum periodic-entry time |
|---|---:|---|---|---:|
| Even, even | 4 | \(1,3,6\) | \(B^7=B\) | 1, except 0 for \(m=n=2\) |
| Mixed | 2 | \(1,2\) | \(B^5=B^3\) | 3 |
| Odd, odd | 0 | \(1\) | \(B^3=0\) | 3 |

Here an identity does not assert that smaller periods or lower global entry times are impossible: exactness is supplied by the indicated primitive-period counts and sharpness statements below. The recurrent subspace means the set of configurations periodic from time zero.

For **even-even** shore sizes, the counts of primitive temporal orbits of lengths \(1,3,6\) are respectively
\[
 1,\qquad \frac{q^2-1}{3},\qquad \frac{q^4-q^2}{6}.
\]
Exactly \(q^4\) initial configurations are immediately periodic; the other \(q^N-q^4\) first become periodic after one step. Every length-\(\ell\) periodic orbit has an individual attraction basin of size \(\ell q^{N-4}\).

For **mixed** shore parities, the numbers of primitive temporal orbits of lengths \(1,2\) are
\[
 q,\qquad \frac{q^2-q}{2}.
\]
The exact numbers of configurations whose first periodic-entry time is \(0,1,2,3\) are
\[
 q^2,\quad q^{N-2}-q^2,\quad q^{N-1}-q^{N-2},\quad q^N-q^{N-1}.
\]
Every length-\(\ell\) orbit has basin size \(\ell q^{N-2}\).

For **odd-odd** shore sizes, the only recurrent state is zero. The exact first-entry population for times \(0,1,2,3\) is
\[
 1,\quad q^{N-4}-1,\quad q^{N-2}-q^{N-4},\quad q^N-q^{N-2}.
\]

These regimes reverse the behavior of intact \(K_{m,n}\). With both shores even, the intact rule extinguishes in at most two steps, while removal creates six-cycles. With mixed parities, intact dynamics is nilpotent, while removal creates primitive two-cycles. With both shores odd, the intact rule has nonzero periodic configurations, while removal extinguishes every configuration in exactly at most three steps. The statements are valid over every characteristic-two finite field, and the deleted edge is arbitrary.

## Assumptions and scope

All graphs are finite, simple, undirected, without loops. The adjacency matrix is interpreted over \(\mathbb F_q\), not over the integers or Boolean OR/AND semirings. The update is simultaneous and has no self-input. The integers \(m,n\) count the actual vertex sets including distinguished endpoints. An orbit's *least period* is the smallest positive return time of its states. The *first periodic-entry time* of an initial configuration is the smallest nonnegative time at which its subsequent state lies on its eventual periodic orbit, with zero meaning initially periodic. All states and orbits are labelled; no quotient by graph automorphisms is applied. An attraction basin includes its periodic states. The polynomial and similarity calculations below hold over any field of characteristic two, whether or not a displayed quadratic splits over that field.

## Proof

**1. A four-dimensional image for every shore size.** Distinguish the deleted edge's left endpoint \(u\) and right endpoint \(v\), and write \(U=L\setminus\{u\}\), \(V=R\setminus\{v\}\), with \(p=m-1\), \(s=n-1\). Denote the current values at the distinguished endpoints by \(a,c\), and the sums of values in \(U,V\) by \(X,Y\). The synchronous update is exactly
\[
 a'=Y,\qquad x_i'=c+Y\ (i\in U),\qquad c'=X,\qquad y_j'=a+X\ (j\in V).
\]
Thus every updated configuration is constant on each of the four nonempty cells \(\{u\},U,\{v\},V\). Conversely the four functionals \(a,X,c,Y\) can be prescribed independently because both \(U,V\) are nonempty; the displayed formulas then prescribe every four cell value independently. Hence \(\operatorname{rank}B=4\) and \(S=\operatorname{im}B\) is exactly the four-cell-constant subspace of dimension four.

On this invariant space, take coordinates \((a,b,c,d)\), where \(b\) and \(d\) are the constant values on \(U,V\). Reduction modulo two of \(p,s\) gives
\[
 M_{p,s}(a,b,c,d)=(s d,\ c+s d,\ p b,\ a+p b).
\]
Its matrix, with two coordinates per shore, is
\[
 M_{p,s}=\begin{pmatrix}0&C_s\\ C_p&0\end{pmatrix},
 \qquad C_z=\begin{pmatrix}0&z\\1&z\end{pmatrix},
 \qquad p,s\in\{0,1\}.
\]
For every integer \(t\ge1\), \(\operatorname{rank}B^{t+1}=\operatorname{rank}M_{p,s}^t\). In particular all higher ranks are determined by the displayed four-dimensional matrix, without extrapolation from examples.

**2. Three exact module types.** Set \(H=C_1\) and \(J=C_0\). In characteristic two, \(H^2+H+I=0\), \(H^3=I\), and \(J^2=0\).

If \(m,n\) are even, then \(p=s=1\) and \(M=\begin{psmallmatrix}0&H\\H&0\end{psmallmatrix}\). Consequently \(M^3\) exchanges the two two-dimensional shores, \(M^6=I\), and \(M^3\ne I\). Furthermore \(\ker(M+I)=0\); indeed, the equation \(M(a,b)=(a,b)\) implies \(H^2a=a\), while \(H^2+I=H\) is invertible. The degree-four characteristic polynomial is \((t^2+t+1)^2\), and \(M^3\ne I\) makes this also the minimal polynomial. Therefore the rational canonical decomposition of \(B\) is one companion block for \((t^2+t+1)^2\) plus \(N-4\) zero singleton blocks. The ranks of \(B^t\), starting with \(t=0\), are \(N,4,4,4,\ldots\).

If \(m,n\) are odd, \(p=s=0\), so \(M^2=0\) and \(\operatorname{rank}M=2\). Thus the ranks of powers of \(B\) are \(N,4,2,0,0,\ldots\), forcing the exact nilpotent Jordan partition
\[
  J_3(0)^{\oplus2}\oplus J_1(0)^{\oplus(N-6)}.
\]
In particular \(B^3=0\), and \(B^2\ne0\).

For mixed parities, by interchanging shores take \(p=1,s=0\). Then \(M^2=\operatorname{diag}(JH,HJ)\). Each of \(JH,HJ\) is a rank-one idempotent, so \(M^2\) is a rank-two projection. On its image the map \(M\) interchanges two one-dimensional summands, giving one two-dimensional unipotent block \(J_2(1)\). The kernel of \(M^2\) is a two-dimensional nilpotent block \(J_2(0)\), since \(\operatorname{rank}M=3\). Therefore the full map \(B\), whose successive ranks are \(N,4,3,2,2,\ldots\), has rational/Jordan decomposition
\[
  J_2(1)\oplus J_3(0)\oplus J_1(0)^{\oplus(N-5)}.
\]
It follows directly that \(B^5=B^3\), with \(B^4\ne B^3\). The unipotent two-block supplies nonzero two-cycles.

**3. Primitive orbit counts and exact first-entry times.** For even-even shores, the periodic space is four-dimensional. On it the fixed spaces of the first, third and sixth powers have dimensions \(0,2,4\), respectively. Since the order is six, the numbers of periodic *states* of least periods \(1,3,6\) are \(1,q^2-1,q^4-q^2\); dividing by period gives the stated orbit counts. The zero component is killed by one application of \(B\), so exactly \(q^4\) configurations are initially periodic and all the rest enter at time one.

For mixed parity the periodic component is \(J_2(1)\), with \(q^2\) points and \(q\) fixed points, so the others have least period two. Its nilpotent complement is one block of length three plus \(N-5\) singleton zero blocks. The cumulative number of configurations periodic by times \(0,1,2,3\) is thus \(q^2,q^{N-2},q^{N-1},q^N\), since each nilpotent kernel dimension grows by \(N-4,1,1\). Successive differences yield the stated exact first-entry populations.

For odd-odd parity there is no nonzero periodic component. The nilpotent partition gives cumulative first-entry counts \(1,q^{N-4},q^{N-2},q^N\) at times \(0,1,2,3\), again giving the displayed successive differences. In mixed and odd-odd cases the last shell is nonempty because \(q\ge2\); in even-even the time-one shell is nonempty unless \(N=4\), which under the hypotheses means \(m=n=2\).

Finally, the Fitting direct sum decomposes every configuration uniquely into its periodic component and a nilpotent component. Exactly \(q^{N-r}\) states share a fixed periodic component, where \(r\in\{4,2,0\}\) is the periodic dimension; taking the union over \(\ell\) states of an orbit yields its individual basin size \(\ell q^{N-r}\). For the intact graph, its rank is two and the matrix satisfies \(A^3=(mn\bmod2)A\); if both sizes are odd, its two-dimensional image is a period-two permutation module, while otherwise it is nilpotent. This proves the stated three-way contrast. \(\square\)

## Verification

Two separately structured, self-contained Python programs are included: `verify_ranks.py` constructs binary adjacency matrices and checks exact ranks and power identities for all 225 ordered pairs \(2\le m,n\le16\), comparing the intact and edge-deleted graphs. `verify_orbits.py` constructs neighbor lists independently and exhaustively follows all configurations for nine binary pairs and six additional cases over \(\mathbb F_4\); it checks period populations, every exact entry-time shell and the basin size of every individual orbit. The latter enumerates 15,376 configurations in total. For \(\mathbb F_4\), neighbor coefficients are only zero or one, so field addition is precisely two-bit XOR; this is an exact representation for these updates. Both programs require only the Python standard library. Reproduction: `python3 verify_ranks.py` and `python3 verify_orbits.py`; their observed terminal output is in `verification_output.txt`. These finite checks test the theorem but do not replace its all-parameter proof.

## Relationship to prior work

The 2006 finite-dynamical-systems work of Moreno, Bollman and Aviño-Diaz develops finite-field linear-system methods and state-diagram equivalence, but not a missing-edge biclique. Ciandrini and coauthors (first public preprint 2008) establish general XOR dynamics and basin-size expressions for linear Boolean networks; their focus is random fixed-in-degree networks, and their formulas do not state the biclique defect's parity-dependent four-cell image and exact cycle structure. Bulitko (2008) studies isomorphism classes of additive cellular automata on finite groups rather than edge deletion in an undirected bipartite support.

Two especially close published calculations concern a missing edge of a Johnson graph under binary neighbor XOR, and a missing hypercube edge under the same update. Both exhibit a four-dimensional six-periodic block in their respective parameter ranges, so that abstract block and its period counts are not claimed intrinsically new. Neither theorem covers the three biclique shore-parity regimes, their sharp different transient strata, or the odd-odd collapse from oscillation to extinction. The related complete-bipartite one-edge majority calculation has the same graph operation but a nonlinear threshold rule; a separate biclique calculation adding an intra-shore edge uses a different graph modification and has different recurrent spectra. The present claim is precisely the complete classification for a deleted *cross-edge* under the characteristic-two neighbor-sum rule.

## Limitations

The graph must have two nonempty residual shores, hence \(m,n\ge2\); the conclusion is not stated for stars, fields of odd characteristic, multiple deleted edges, self-feedback or asynchronous updates. The six-periodic four-dimensional module is known in other graph settings, while the graph-specific three-regime phase diagram and exact transient and basin distributions are the present contribution. The literature comparison is finite and cannot rule out obscure or unindexed equivalent prior results. Computational tests are finite; no independent external validation is asserted.

## References

- O. Moreno, D. Bollman and M. A. Aviño-Diaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1, publicly submitted 2006-04-25, https://arxiv.org/html/math/0604534v1.
- L. Ciandrini, C. Maffi, A. Motta, B. Bassetti and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526v1, publicly submitted 2008-09-09, https://arxiv.org/html/0809.1526v3.
- V. Bulitko, *Isomorphisms of Additive Cellular Automata on Finite Groups*, arXiv:0812.0111v1, publicly submitted 2008-11-29, https://arxiv.org/abs/0812.0111.
- *One-edge defects create universal six-cycles in nilpotent Johnson parity dynamics*, publicly indexed research record ending `6ee185cd61fc` (2026), for comparison of a distinct graph family's periodic module.
- *A missing-edge parity transition in hypercube XOR dynamics*, publicly indexed research record ending `0ddebf65b6fe` (2026), for comparison of characteristic-two edge defects in another graph family.
- *A one-edge majority defect has three exact basin responses*, publicly indexed research record ending `4c37e2b972d1` (2026), for comparison with a nonlinear rule on the same graph family.
