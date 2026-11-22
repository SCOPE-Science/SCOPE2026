# Facet feedback converts cube parity dynamics into a universal six-step permutation

## Finding

For every integer \(d\ge2\) and finite field \(\mathbb F_q\) with \(q=2^s\), \(s\ge1\), let \(Q_d\) be the Boolean \(d\)-cube. A configuration assigns a field element to each of its \(2^d\) vertices. Update every vertex simultaneously to the sum of the old values at its ordinary cube neighbors, **plus its own old value if and only if its first coordinate is zero**. Let \(F_{d,q}\) denote this map.

**The complete orbit theorem** is:

1. \(F_{d,q}\) is invertible and has exact global order six, for every \(d\ge2\), without a parity exception. Every configuration is immediately periodic, and the only least periods are one, three, and six.
2. The zero configuration is the unique fixed configuration. The counts of labelled configurations with least periods three and six are respectively
   \[
   P_3=q^{2^{d-1}}-1,\qquad P_6=q^{2^d}-q^{2^{d-1}}.
   \]
   Thus the numbers of distinct primitive temporal orbits are \(1\), \(P_3/3\), and \(P_6/6\), respectively. There are no primitive two-cycles.
3. The rational canonical form over \(\mathbb F_q\) consists of exactly \(2^{d-2}\) companion blocks of the degree-four polynomial \((t^2+t+1)^2\). Equivalently, the entire state space is the direct sum of \(2^{d-2}\) identical four-dimensional cyclic modules.

For comparison, without any self-feedback the open-neighbor sum on \(Q_d\) is square-zero in even dimension and is an involution in odd dimension. Adding feedback to one entire codimension-one cube face therefore turns **both** kinds of originally incompatible dynamics into the same all-periodic, six-step clock.

At \(d=1\), excluded from the six-step assertion, the modified two-vertex map has order three: its zero state is fixed and its remaining \(q^2-1\) states have least period three.

## Assumptions and scope

The vertex set is \(\{0,1\}^d\), adjacency means Hamming distance exactly one, and the distinguished face is \(\{x:x_1=0\}\). Each neighbor contributes coefficient one in \(\mathbb F_q\); each face vertex has one additional **self-input** also of coefficient one. There are no graph-theoretic loop-degree conventions: the update is defined explicitly by
\[
(F_{d,q}u)(x)=\sum_{j=1}^d u(x\oplus e_j)+\mathbf1_{\{x_1=0\}}u(x).
\]
Here \(\oplus\) flips the indicated coordinate; all operations in the displayed update take place in characteristic two. The theorem counts configurations on the labelled vertex set, without quotienting by spatial symmetries, and counts temporal orbits with each periodic cycle counted once.

## Proof

Let \(m=d-1\), let \(H\) be the \(2^m\)-dimensional space of functions on the \(m\)-cube, and denote its ordinary neighbor-sum matrix by \(A_m\). If \(X_j\) flips coordinate \(j\), then \(A_m=\sum_{j=1}^m X_j\). These matrices commute and satisfy \(X_j^2=I\), so in characteristic two
\[
A_m^2=(m\bmod2)I.
\]
Set \(\varepsilon=m\bmod2\) and \(N=A_m+\varepsilon I\). Consequently \(N^2=0\).

Ordering the full cube by its first bit, the dynamics is
\[
F=\begin{pmatrix}A_m+I&I\\I&A_m\end{pmatrix}
 =C\otimes I_H+I_2\otimes N,
\qquad
C=\begin{pmatrix}\varepsilon+1&1\\1&\varepsilon\end{pmatrix}.
\]
Direct multiplication gives \(C^2+C+I_2=0\), \(C^3=I_2\). Because the two tensor summands commute and \(N^2=0\),
\[
F^2=C^2\otimes I_H,\quad
F^3=I+C^2\otimes N,\quad
F^6=I.
\]
Also,
\[
F^2+I=C\otimes I_H,\qquad F^2+F+I=I_2\otimes N.
\]
Since \(C\) is invertible, \(F^2+I\) is invertible. Thus no nonzero state has least period one or two.

It remains to determine the nullity of \(N\). For \(m\ge1\), write \(N=\sum_{j=1}^m(X_j+I)\). Separating the first of these \(m\) coordinates gives
\[
N=\begin{pmatrix}L+I&I\\I&L+I\end{pmatrix},
\qquad L=\sum_{j=2}^m(X_j+I),\quad L^2=0.
\]
An element \((v,w)\) is killed by \(N\) exactly when \(w=(L+I)v\), as the second block equation then holds identically because \((L+I)^2=I\). Therefore \(\dim\ker N=2^{m-1}\) and \(\operatorname{rank}N=2^{m-1}\), valid also when \(m=1\) with \(L=0\).

As \(C^2\) is invertible, \(F^3+I=C^2\otimes N\) has rank \(2^m=2^{d-1}\). Hence its kernel has dimension \(2^{d-1}\) and contains exactly \(q^{2^{d-1}}\) field-valued states. All these states have least period one or three, and exactly one (zero) has period one. Every other state has least period six, because \(F^6=I\) and no nonzero state has period two. This yields both point populations and orbit counts by dividing by the relevant period.

For the canonical form, \(N^2=0\) and its rank is half its dimension. Thus its Jordan form over \(\mathbb F_q\) consists entirely of \(2^{m-1}\) size-two zero blocks. Each block is stable under \(F\) after tensoring with the two-dimensional \(C\)-space and produces a four-dimensional \(F\)-module of characteristic polynomial \(p(t)^2\), where \(p(t)=t^2+t+1\). On that block \(p(F)=I_2\otimes N\ne0\), but \(p(F)^2=0\); hence the minimal polynomial is also \(p(t)^2\), of degree four. Its module is therefore cyclic, similar to the companion of \(p(t)^2\). The number of such blocks is \(2^{m-1}=2^{d-2}\).

Finally, the unmodified \(d\)-cube neighbor operator \(A_d\) satisfies \(A_d^2=(d\bmod2)I\) by the same commuting-involution calculation. This proves the claimed sharp contrast for even and odd dimension. For \(d=1\), the displayed matrix \(C\) alone has order three and no nonzero fixed vectors, giving the stated boundary case.

## Verification

The standalone program `verify_direct.py` constructs successors independently from the explicit neighbor rule and exhaustively checks every field-valued state for \((d,q)=(1,2),(2,2),(3,2),(4,2),(1,4),(2,4),(3,4)\); it counts the least period without using the tensor proof. Its recorded execution is `verify_direct_output.txt`. The characteristic-two field of four elements is represented by two-bit coefficients, whose field addition is bitwise XOR; multiplication is unnecessary because the update coefficients are only zero and one.

The separate `verify_algebra.py` constructs the full binary update matrices directly, verifies \(F^6=I\), the square-zero relation \((F^2+F+I)^2=0\), all predicted ranks of \(F^2+F+I\) and \(F^3+I\), and the parity-dependent identity for the unmodified adjacency, for \(1\le d\le8\) using integer-bitset Gaussian elimination. Its recorded execution is `verify_algebra_output.txt`.

For \(q=2\), the least-period state populations at dimensions two, three, and four are respectively \((1,3,12)\), \((1,15,240)\), and \((1,255,65280)\) in period order \((1,3,6)\). These finite checks corroborate the all-dimension argument above; they are not substituted for it.

## Relationship to prior work

The general algebraic approach to finite additive cellular automata is classical. The early study of XOR network dynamics by Ciandrini and coauthors establishes general matrix and periodicity methods for directed random Boolean networks, not a face-localized feedback theorem for the cubical family. A published one-site feedback result for Boolean cubes computes a different phenomenon: one modified vertex yields nonreversible even-dimensional dynamics and four possible least periods in odd dimensions, whereas the present modified set contains \(2^{d-1}\) vertices and gives a reversible operator in both parities. A published two-site feedback theorem also treats exactly two modified vertices (and dimensions at least three), so it does not cover a facet with at least four sites. A published single-edge-deletion cube theorem removes an ordinary undirected edge and again has nontrivial transient or parity-dependent behavior, rather than a facial diagonal perturbation. Neither finite-rank perturbation result logically implies this higher-rank face calculation or its full canonical decomposition.

The comparison does not claim that standard tensor algebra is new or establish absolute publication priority. It concerns the explicit face-induced reversibility theorem, identical four-dimensional primary blocks, and full orbit distribution on all cube dimensions and all finite characteristic-two fields.

## Limitations

The result is for exactly one codimension-one face with self-inputs of coefficient one, the ordinary cube, synchronous linear neighbor sums, and finite fields of characteristic two. It does not classify feedback on arbitrary vertex subsets, arbitrary coefficients, nonlinear Boolean rules, or the number of cycles after quotienting by cube automorphisms. Literature discovery is not an exhaustive proof of priority. Independent validation has not been performed.

## References

1. L. Ciandrini, C. Maffi, A. Motta, B. Bassetti, and M. Cosentino Lagomarsino, *Feedback topology and XOR-dynamics in Boolean networks with varying input structure*, arXiv:0809.1526 (first submitted 2008-09-09), https://arxiv.org/abs/0809.1526 ; *Physical Review E* 80 (2009), 026122, DOI: 10.1103/PhysRevE.80.026122.
2. O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic properties of cellular automata*, *Communications in Mathematical Physics* 93 (1984), 219–258, DOI: 10.1007/BF01223745. General additive-cellular-automaton methodology.
3. *A one-site feedback defect creates periods three and six on Boolean hypercubes*, public mathematical record `a9a2b0b84ed9` (2026).
4. *An adjacency threshold for two-site feedback on Boolean hypercube automata*, public mathematical record `444c4754c134` (2026).
5. *One missing hypercube bond creates six-cycles or four-cycles in binary parity dynamics*, public mathematical record `4fb7fb6660f5` (2026).
