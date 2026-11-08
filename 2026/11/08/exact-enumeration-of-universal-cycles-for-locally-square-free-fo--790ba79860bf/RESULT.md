# Exact enumeration of universal cycles for locally square-free four-letter words

## Finding

Let \(q\ge3\) be an integer and let \(\Sigma_q\) be a fixed, labeled alphabet of \(q\) symbols. A four-letter word \(abcd\in\Sigma_q^4\) is *square-free* if \(a\ne b\), \(b\ne c\), \(c\ne d\), and \((a,b)\ne(c,d)\). Equivalently, it contains neither an adjacent doubled letter nor a square of two letters. Let \(\mathcal F_q\) be the set of such words.

A *universal cycle* for \(\mathcal F_q\) is a circular word of length \(|\mathcal F_q|=q^2(q-1)(q-2)\) whose cyclic four-letter windows give every member of \(\mathcal F_q\) exactly once. Rotations are identified; reversal and alphabet permutations are **not** identified. The circular word itself need not avoid squares longer than four letters.

**Theorem.** For every integer \(q\ge3\), universal cycles for \(\mathcal F_q\) exist. Their exact number is

\[
\begin{aligned}
U_q={}&q^{q-2}(q-1)^{q(q^2-3q+1)-2}(q-2)^{2(q-1)}
\big((q-2)^2+1\big)^{\binom{q-1}{2}}\\
&\cdot\big((q-3)!\big)^{q(q-1)}
\big((q-2)!\big)^{q(q-1)(q-2)}.
\end{aligned}
\]

For \(q=3,4,5,6\), respectively, the first counts are \(12\), \(831979165027663872000\), \(3409844132885373285929406046947552548988950218713525713993051919951275472190739199295488000000000\), and the much larger integer computed by the accompanying verifier.

The key structural identity is a full characteristic-polynomial factorization of the directed overlap-graph Laplacian. Set

\[
A_q=q(q^2-3q+1),\quad B_q=\binom{q-1}{2},\quad
Q_q(x)=x^2-(2q-4)x+(q-2)^2+1,
\]
\[
P_q(x)=x^3-(3q-4)x^2+(3q^2-8q+5)x-q(q-2)^2.
\]

If \(L_q\) is the outgoing Laplacian of the overlap graph, then

\[
\det(xI-L_q)=x(x-q+1)^{A_q}Q_q(x)^{B_q}P_q(x)^{q-1}.
\]

## Assumptions and scope

All graph vertices and edges are labeled by actual words. Repetitions of a letter at distance two (such as \(aba\)) are permitted in three-letter vertices. A four-letter word \(abab\) is excluded, as is any four-letter word with two adjacent equal symbols. The alphabet size is an integer at least three. No identification under symbol relabeling is made. The graph has \(q(q-1)^2\) vertices, \(q^2(q-1)(q-2)\) directed edges, and at most one edge with any particular four-letter label.

## Proof

**1. The overlap graph and connectivity.** Take as vertices all triples \((a,b,c)\) with \(a\ne b\) and \(b\ne c\). A permitted four-letter word \(abcd\) gives an edge from \((a,b,c)\) to \((b,c,d)\). At a vertex \((a,b,a)\), both incoming and outgoing degrees are \(q-2\); at a triple with all symbols distinct both degrees are \(q-1\). Hence the graph is balanced.

For every three-element alphabet subset, the induced subgraph on triples using only its symbols is strongly connected: its six all-distinct triples form two oriented three-cycles; each can enter a repeated-endpoint triple and then the opposite orientation, and every repeated-endpoint triple is reachable from an all-distinct triple. Any two three-element alphabet subsets that share two symbols have overlapping induced subgraphs (the triple \((a,b,a)\) on those shared symbols). The graph of three-element subsets connected by two-symbol overlaps is connected. Every vertex belongs to one of these induced subgraphs. Thus the full overlap graph is strongly connected for every \(q\ge3\), so its balanced edges have Eulerian circuits. Each Eulerian circuit gives exactly one universal cycle and conversely.

**2. Laplacian factorization.** Write \(m=q(q-1)\), and let \(f(a,b,c)\) denote a function on the vertices. Put \(t=q-1-x\), \(s=q-2-x\), \(u_{ab}=f(a,b,a)\), and \(g_{bc}=\sum_{d\ne c}f(b,c,d)\) for distinct \(b,c\). The eigen-equation \((L_q-xI)f=0\) at an all-distinct triple reads

\[t f(a,b,c)=g_{bc},\]

and at a repeated-endpoint triple reads

\[s u_{ab}=g_{ba}-u_{ba}.\]

Thus \(g_{bc}=s u_{cb}+u_{bc}\). Defining \(G_c=\sum_{d\ne c}g_{cd}\) and eliminating the all-distinct coordinates yields

\[(ts+1)u_{cb}+s u_{bc}-G_c=0,\qquad
G_c=\sum_{d\ne c}(s u_{dc}+u_{cd}).\]

Let \(K(x)\) be the \(m\)-by-\(m\) matrix of this system, with rows indexed by ordered pairs \((b,c)\). Direct block elimination, first valid when \(t\ne0\) and then extended as a polynomial identity, gives

\[\det(L_q-xI)=\pm t^{m(q-3)}\det K(x).\]

We evaluate \(K\) on the following direct-sum decomposition of the space of functions on ordered unequal pairs:

- Constants, dimension \(1\). The scalar for \(K\) is \(-xt\).
- Functions \(u_{bc}=\alpha z_b+\beta z_c\) with \(\sum_b z_b=0\), giving \(q-1\) copies of a two-dimensional space. On each copy the matrix is
  \[
  \begin{pmatrix}
  s&ts+1\\
  t^2-(q-1)&1-(q-2)s
  \end{pmatrix},
  \]
  whose determinant is \(tP_q(x)\).
- Symmetric pair functions with every row sum zero, dimension \(q(q-3)/2\). Here \(K\) acts as the scalar \(t^2\).
- Antisymmetric pair functions with every row sum zero, dimension \((q-1)(q-2)/2\). Here \(K\) acts as the scalar \(-[s^2+1]\).

The dimensions sum to \(q(q-1)\). In the symmetric and antisymmetric subspaces the column sums vanish as well, so the displayed scalars follow immediately from the definition of \(G_c\). In the standard subspace the row and column sums of \(u_{bc}=\alpha z_b+\beta z_c\) give the displayed two-by-two matrix by direct substitution. Combining the four determinant factors, the remaining power of \(t\) is

\[m(q-3)+1+(q-1)+q(q-3)=q(q^2-3q+1)=A_q.\]

Since \(s^2+1=Q_q(x)\) and both sides are monic polynomials of degree \(q(q-1)^2\), the sign is fixed and the claimed characteristic polynomial follows.

**3. Tree and Eulerian-tour counts.** The directed matrix-tree theorem states that the product of the nonzero Laplacian eigenvalues divided by the number \(q(q-1)^2\) of vertices is the number \(T_q\) of arborescences directed toward any fixed root (the root-independent count uses the balanced symmetry). Evaluating the factorization at zero after removing the leading factor gives

\[
T_q=q^{q-2}(q-1)^{A_q-2}(q-2)^{2(q-1)}
\big((q-2)^2+1\big)^{B_q}.
\]

There are \(q(q-1)\) vertices of outgoing degree \(q-2\), and \(q(q-1)(q-2)\) vertices of degree \(q-1\). The directed BEST theorem gives the number of Eulerian tours with one distinguished edge fixed as

\[
T_q\big((q-3)!\big)^{q(q-1)}
\big((q-2)!\big)^{q(q-1)(q-2)}.
\]

Because every edge corresponds to a distinct permitted four-letter word, fixing one distinguished edge gives exactly one representative per rotation class of universal cycles. This establishes the formula and the existence claim.

## Verification

`verify_tours.py` exhaustively enumerates all twelve ternary Eulerian tours after fixing one four-letter window, checks every reconstructed cycle, and independently calculates exact Laplacian-minor determinants by integer Bareiss elimination for \(q=3,4,5\). It reports `TOUR_AND_BAREISS_VERIFY_OK`.

`verify_spectrum.py` independently forms the full integer Laplacian and compares its characteristic polynomial and exact directed spanning-tree count to the symbolic formulas at \(q=3,4,5,6\), using SymPy. It reports `SPECTRUM_VERIFY_OK`. These finite checks corroborate—but do not replace—the all-alphabet structural argument above. Both programs run with their contents exactly as embedded in this package.

## Relationship to prior work

Classical de Bruijn constructions and the Eulerian BEST and directed matrix-tree theorems are prior tools, not new results. Penne's 2010 study establishes existence for de Bruijn sequences subject to symbol-separation constraints. Alhakim's later construction concerns restricted sequences and uses *square-free* in its subsection for the weaker condition of no immediately repeated letter; that is not the four-letter ordinary square-freeness studied here. Shur's 2010 paper concerns entire ternary circular words avoiding squares of every possible period, whereas the objects here represent all square-free *four-letter windows* exactly once and need not be globally square-free. The new result asserted here is the evaluated all-alphabet overlap-Laplacian factorization and the consequent exact multiplicity of these cycles. General graph theorems imply an unevaluated determinant formulation, but not the displayed closed product without the extra spectral reduction.

## Limitations

The theorem is exclusively about square-freeness of windows of length four; it neither implies nor counts globally square-free circular words, and it says nothing about universal cycles for windows of length five or greater. Reversal and symbol permutations have not been quotiented. Publication-priority research is not exhaustive: the full text of Penne's 2010 short paper was not accessible during the literature comparison; its accessible abstract asserts existence, and a subsequent primary paper describes it as an existence proof, but a previously unindexed count cannot be ruled out. No independent scientific audit is claimed.

## References

1. R. Penne, *A note on certain de Bruijn sequences with forbidden subsequences*, Discrete Mathematics 310 (2010), 966–969. DOI: https://doi.org/10.1016/j.disc.2009.10.009 .
2. A. M. Shur, *On ternary square-free circular words*, arXiv:1009.5759v1, first posted 2010-09-29. https://arxiv.org/abs/1009.5759 .
3. A. M. Alhakim, *Designing preference functions for de Bruijn sequences with forbidden words*, 2020 preprint and Designs, Codes and Cryptography (2022). DOI: https://doi.org/10.1007/s10623-022-01077-5 .
4. Directed BEST theorem and directed matrix-tree theorem (standard counting results).
