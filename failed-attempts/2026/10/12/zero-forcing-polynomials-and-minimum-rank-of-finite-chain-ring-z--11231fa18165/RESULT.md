# Zero forcing polynomials and minimum rank of finite chain-ring zero-divisor graphs

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), nilpotency length \(\ell\ge2\), and residue-field order \(q\). Put \(N=q^{\ell-1}-1\) and \(n_i=(q-1)q^{\ell-i-1}\) for \(1\le i\le\ell-1\). Except for the one-vertex boundary \((q,\ell)=(2,2)\), the standard zero-divisor graph satisfies \[\mathcal Z(\Gamma(R);u)=u^{N-(\ell-1)}\prod_{i=1}^{\ell-1}(u+n_i),\qquad Z(\Gamma(R))=M(\Gamma(R))=N-(\ell-1),\qquad \operatorname{mr}(\Gamma(R))=\ell-1.\] Its minimum zero forcing sets are exactly the complements of one vertex from every valuation layer, so their number is \((q-1)^{\ell-1}q^{(\ell-1)(\ell-2)/2}\). For \((q,\ell)=(2,2)\), \(\Gamma(R)=K_1\), \(\mathcal Z=u\), \(Z=M=1\), and \(\operatorname{mr}=0\). In every case the zero forcing polynomial recovers \((q,\ell)\) and hence the zero-divisor graph up to isomorphism within the finite chain-ring class.

The factorization is controlled exactly by the valuation layers of the chain ring.

## Assumptions and scope

Let \(R\) be a finite commutative chain ring with maximal ideal
\[
\mathfrak m=(\pi),
\]
and nilpotency length
\[
\mathfrak m^\ell=0,\qquad \mathfrak m^{\ell-1}\ne0,
\qquad \ell\ge2.
\]
Let
\[
q=|R/\mathfrak m|.
\]

The standard zero-divisor graph \(\Gamma(R)\) has the nonzero zero-divisors as vertices, with two distinct vertices adjacent exactly when their product is zero.

For
\[
1\le i\le\ell-1,
\]
write
\[
V_i=\mathfrak m^i\setminus\mathfrak m^{i+1}.
\]

## Proof

Each quotient
\[
\mathfrak m^i/\mathfrak m^{i+1}
\]
is a simple \(R\)-module and therefore has \(q\) elements. Hence
\[
|\mathfrak m^i|=q^{\ell-i},
\]
so
\[
|V_i|
=
q^{\ell-i}-q^{\ell-i-1}
=
(q-1)q^{\ell-i-1}
=
n_i.
\tag{1}
\]
Thus
\[
N=|V(\Gamma(R))|
=
\sum_{i=1}^{\ell-1}n_i
=
q^{\ell-1}-1.
\tag{2}
\]

If
\[
x=u\pi^i\in V_i,\qquad y=v\pi^j\in V_j,
\]
with \(u,v\) units, then
\[
xy=0
\quad\Longleftrightarrow\quad
i+j\ge\ell.
\tag{3}
\]

Consequently every \(V_i\) is a twin class. It is independent when
\[
2i<\ell
\]
and complete when
\[
2i\ge\ell.
\]
Therefore a zero forcing set can leave at most one white vertex in any \(V_i\): two white twins cannot be separated by a first force.

Conversely, assume at most one white vertex lies in each valuation layer. Let
\[
t
\]
be the largest valuation index of a white layer. Set
\[
s=\ell-t.
\]
A vertex in \(V_s\) is adjacent to a white vertex in \(V_j\) exactly when
\[
s+j\ge\ell,
\]
equivalently
\[
j\ge t.
\]
By maximality of \(t\), the white representative in \(V_t\) is therefore the unique white neighbor of every blue representative in \(V_s\).

Such a blue representative always exists, except in the degenerate case
\[
(q,\ell)=(2,2).
\]
Indeed the only layer of size one occurs when \(q=2\) and \(i=\ell-1\). If \(V_s\) is that singleton and is itself white, then
\[
s=t=\ell-1
\]
and
\[
s=\ell-t,
\]
forcing \(\ell=2\). Outside that single case, \(V_s\) contains a blue vertex and forces the white representative in \(V_t\).

Repeating the argument with the next-largest white layer proves that every coloring with at most one white vertex per valuation layer is zero forcing.

Hence, outside \((q,\ell)=(2,2)\), each layer contributes independently either all its vertices or all but one:
\[
u^{n_i}+n_i u^{n_i-1}
=
u^{n_i-1}(u+n_i).
\]
Multiplying gives
\[
\mathcal Z(\Gamma(R);u)
=
u^{N-(\ell-1)}
\prod_{i=1}^{\ell-1}(u+n_i).
\tag{4}
\]
The smallest exponent yields
\[
Z(\Gamma(R))
=
N-(\ell-1).
\tag{5}
\]

A minimum forcing set omits exactly one vertex from every layer. Its count is therefore
\[
\prod_{i=1}^{\ell-1}n_i
=
(q-1)^{\ell-1}
q^{(\ell-1)(\ell-2)/2}.
\tag{6}
\]

For minimum rank, let \(Q_\ell\) be the \((\ell-1)\times(\ell-1)\) symmetric matrix
\[
(Q_\ell)_{ij}
=
\begin{cases}
1,&i+j\ge\ell,\\
0,&i+j<\ell.
\end{cases}
\]
This includes the diagonal.

Reverse the column order. The resulting matrix is lower triangular with all diagonal entries equal to \(1\). Thus
\[
\det Q_\ell=\pm1,
\]
so
\[
\operatorname{rank}Q_\ell=\ell-1.
\tag{7}
\]

Let \(X\) be the vertex-by-layer incidence matrix. Then
\[
XQ_\ell X^{\mathsf T}
\]
has nonzero off-diagonal entries exactly where (3) gives an edge. Its rank is \(\ell-1\), so
\[
\operatorname{mr}(\Gamma(R))\le\ell-1.
\]
The standard inequality
\[
M(G)\le Z(G)
\]
and (5) give
\[
\operatorname{mr}(\Gamma(R))
=
N-M(\Gamma(R))
\ge
N-Z(\Gamma(R))
=
\ell-1.
\]
Therefore
\[
\operatorname{mr}(\Gamma(R))=\ell-1,
\qquad
M(\Gamma(R))=Z(\Gamma(R))=N-(\ell-1).
\tag{8}
\]

If
\[
(q,\ell)=(2,2),
\]
there is a single nonzero zero-divisor. Hence
\[
\Gamma(R)=K_1,
\]
so
\[
\mathcal Z(\Gamma(R);u)=u,\qquad Z=M=1,\qquad \operatorname{mr}=0.
\]

Finally, outside the one-vertex boundary, the nonzero roots of (4) have magnitudes
\[
(q-1),\ q(q-1),\ \ldots,\ q^{\ell-2}(q-1).
\]
The number of nonzero roots counted with multiplicity is \(\ell-1\), while the smallest magnitude is \(q-1\). Thus the polynomial recovers
\[
\ell
\quad\text{and}\quad
q.
\]
The boundary polynomial \(u\) uniquely identifies the remaining parameter pair \((2,2)\) within this class.

Since the valuation-layer graph is determined by \((q,\ell)\), the zero forcing polynomial determines the zero-divisor graph up to isomorphism among finite chain rings.

## Verification

The accompanying `verify.py` was read from its packaged path before replay.

It exhausts every valuation-layer white profile for
\[
q\in\{2,3,4,5\},
\qquad
2\le\ell\le10,
\]
and confirms that every at-most-one-white profile forces except the unique one-vertex boundary.

It computes the quotient rank exactly through
\[
\ell=12
\]
and obtains \(\ell-1\) in every case.

For the small parameter pairs
\[
(2,2),\ (3,2),\ (2,3),\ (3,3),\ (2,4),\ (2,5),
\]
the checker exhaustively enumerates every vertex subset and reproduces the complete zero forcing polynomial.

It also constructs the graphs of
\[
\mathbb Z/(2^2),\quad
\mathbb Z/(2^3),\quad
\mathbb Z/(2^4),\quad
\mathbb Z/(3^2),\quad
\mathbb Z/(3^3)
\]
directly from modular multiplication and checks every edge against the valuation rule.

Exact replay output:

```text
PROFILE_THEOREM_OK
QUOTIENT_RANK_OK
(q,ell)=(2,2): sizes=[1], N=1, polynomial={1: 1}
(q,ell)=(3,2): sizes=[2], N=2, polynomial={1: 2, 2: 1}
(q,ell)=(2,3): sizes=[2, 1], N=3, polynomial={1: 2, 2: 3, 3: 1}
(q,ell)=(3,3): sizes=[6, 2], N=8, polynomial={6: 12, 7: 8, 8: 1}
(q,ell)=(2,4): sizes=[4, 2, 1], N=7, polynomial={4: 8, 5: 14, 6: 7, 7: 1}
(q,ell)=(2,5): sizes=[8, 4, 2, 1], N=15, polynomial={11: 64, 12: 120, 13: 70, 14: 15, 15: 1}
Z/4Z direct graph OK: N=1
Z/8Z direct graph OK: N=3
Z/16Z direct graph OK: N=7
Z/9Z direct graph OK: N=2
Z/27Z direct graph OK: N=8
PARAMETER_RECOVERY_OK
VERIFY_OK
```

The finite computations corroborate the symbolic proof; they do not replace it.

## Relationship to prior work

Anderson and Badawi study zero-divisor graphs of chained rings and prove structural results such as the clique behavior of square-zero elements, total disconnectedness outside that core, and diameter at most two. Their full article has primary Mathematics Subject Classification \(13A15\). The inspected full text contains no occurrence of “zero forcing” or “minimum rank.”

Earlier work on the same finite-chain-ring graph family determines its valuation-layer structure, automorphism group, determining number, and metric dimension. That structural result is used here only as overlap context; the forcing polynomial and minimum-rank theorem are different invariants and require a separate force-by-largest-layer argument.

General minimum-rank theory for graph blowups can reduce some blowup rank problems to smaller loop graphs. The rank portion of the present theorem is compatible with that framework, but the complete zero forcing polynomial, the classification of every minimum forcing set, and reconstruction of \((q,\ell)\) from the polynomial are not supplied by the inspected blowup source.

## Limitations

The theorem concerns finite commutative chain rings and the standard zero-divisor graph.

The polynomial determines the graph parameters \(q\) and \(\ell\), but not the ring isomorphism type: nonisomorphic chain rings can have the same residue-field order and nilpotency length.

The minimum-rank statement is over real symmetric graph-pattern matrices.

The one-vertex case \((q,\ell)=(2,2)\) is exceptional because the sole valuation layer has no blue representative when its unique vertex is white.

## References

1. D. F. Anderson and A. Badawi, “On the Zero-Divisor Graph of a Ring,” *Communications in Algebra* 36 (2008), 3073–3092. DOI: 10.1080/00927870802110888. Published online 22 August 2008.
2. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648. DOI: 10.1016/j.laa.2007.10.009.
3. J. C.-H. Lin, “Odd Cycle Zero Forcing Parameters and the Minimum Rank of Graph Blowups,” *Electronic Journal of Linear Algebra* 31 (2016), 42–59. DOI: 10.13001/1081-3810.2836.
4. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” *Discrete Applied Mathematics* 258 (2019), 35–48. arXiv:1801.08910.
