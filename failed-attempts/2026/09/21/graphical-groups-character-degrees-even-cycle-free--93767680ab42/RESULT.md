# Character-degree polynomials for graphical groups from even-cycle-free graphs and cycles

Let \(\Gamma=(V,E)\) be a finite simple graph with \(n=|V|\), and let
\(\mathbf G_\Gamma(\mathbf F_q)\) be its graphical group.  For \(i\ge 0\), write
\[
\operatorname{ch}(\Gamma,i;q)
=
\#\{\chi\in\operatorname{Irr}(\mathbf G_\Gamma(\mathbf F_q)):\chi(1)=q^i\}.
\]
Throughout, \(q\) is an odd prime power.

For an edge set \(S\subseteq E\), let \(\nu(V,S)\) be the matching number of the
spanning subgraph \((V,S)\), and define
\[
A_{\Gamma,i}(T)
=
\sum_{\substack{S\subseteq E\\ \nu(V,S)=i}}T^{|S|}
\in\mathbf Z[T].
\]

## Theorem 1: graphs with no even cycle

If \(\Gamma\) contains no even cycle, then for every \(i\ge0\),
\[
\boxed{\operatorname{ch}(\Gamma,i;q)
=
q^{\,n-2i}A_{\Gamma,i}(q-1).}
\]
In particular, every character-degree multiplicity of
\(\mathbf G_\Gamma(\mathbf F_q)\) is polynomial in \(q\) for odd \(q\).

This includes every forest and every graph whose blocks are edges or odd cycles.

## Theorem 2: all cycle graphs

The preceding formula already covers odd cycles.  For the even cycle
\(\Gamma=C_{2r}\), put \(t=q-1\).  Then
\[
\operatorname{ch}(C_{2r},i;q)=q^{2r-2i}N_i(q),
\]
where
\[
N_i(q)=
\begin{cases}
A_{C_{2r},i}(t),&i\notin\{r-1,r\},\\[2mm]
A_{C_{2r},r-1}(t)+t^{2r-1},&i=r-1,\\[2mm]
A_{C_{2r},r}(t)-t^{2r-1},&i=r.
\end{cases}
\]
Thus Rossmann's character-enumeration question has a polynomial answer for every
cycle graph as well as for every even-cycle-free graph.

For example, for \(C_4\),
\[
A_{C_4,1}(T)=4T+4T^2,\qquad
A_{C_4,2}(T)=2T^2+4T^3+T^4,
\]
so
\[
\operatorname{ch}(C_4,1;q)
=q^2\bigl(4t+4t^2+t^3\bigr),
\]
and
\[
\operatorname{ch}(C_4,2;q)
=2t^2+3t^3+t^4.
\]

## Proof

Rossmann records that O'Brien--Voll's character formula reduces
\(\operatorname{ch}(\Gamma,i;q)\), for odd \(q\), to the rank distribution of
the generic antisymmetric matrix \(B_\Gamma(Y)\) supported on the edges of
\(\Gamma\).  More precisely, O'Brien--Voll's Theorem B gives
\[
\operatorname{ch}(\Gamma,i;q)
=
q^{\,n-2i}
\#\{y\in\mathbf F_q^E:\operatorname{rk}B_\Gamma(y)=2i\}.
\tag{1}
\]
Indeed, the abelianization of the graphical group has order \(q^n\).

Fix \(y\in\mathbf F_q^E\), and let
\[
S(y)=\{e\in E:y_e\ne0\}.
\]
Then the graph of the skew-symmetric matrix \(B_\Gamma(y)\) is precisely
\((V,S(y))\).

Suppose first that \(\Gamma\) has no even cycle.  Every support graph
\((V,S(y))\) again has no even cycle.  A theorem of Wang--Zhou says that for a
graph \(H\) with no even cycle, every skew-symmetric matrix with graph \(H\)
has rank \(2\nu(H)\).  For completeness, the relevant mechanism is also
immediate from Pfaffians.  If \(M\) is a maximum matching of \(H\), the
vertices covered by \(M\) induce a graph with a unique perfect matching:
two distinct perfect matchings would have symmetric difference containing an
even cycle.  Hence the Pfaffian of the corresponding principal submatrix has
the single nonzero monomial given by \(M\), giving rank at least
\(2\nu(H)\).  The reverse inequality follows because a nonzero principal
Pfaffian of order \(2s\) supplies a matching of size \(s\).  Consequently,
\[
\operatorname{rk}B_\Gamma(y)=2\nu(V,S(y)).
\]
There are exactly \((q-1)^{|S|}\) vectors \(y\) with support \(S\), and so
\[
\#\{y:\operatorname{rk}B_\Gamma(y)=2i\}
=
\sum_{\nu(V,S)=i}(q-1)^{|S|}
=
A_{\Gamma,i}(q-1).
\]
Equation (1) proves Theorem 1.

Now let \(\Gamma=C_{2r}\).  If \(S(y)\ne E\), the support graph is a forest, so
the same matching-number argument applies.  It remains to count full-support
vectors.  When all \(2r\) edge weights are nonzero, the full Pfaffian has
exactly two monomials, corresponding to the two perfect matchings of the
cycle.  Up to an irrelevant sign it has the form
\[
y_1y_3\cdots y_{2r-1}
\ \pm\
y_2y_4\cdots y_{2r}.
\]
Among the \((q-1)^{2r}\) full-support vectors, exactly
\((q-1)^{2r-1}\) make this Pfaffian zero: after choosing any \(2r-1\)
nonzero coordinates, there is a unique nonzero value of the last coordinate
that gives cancellation.

If the Pfaffian does not vanish, the rank is \(2r\).  If it vanishes, the
rank is at most \(2r-2\), while deleting two adjacent cycle vertices leaves
a weighted path on \(2r-2\) vertices with a unique perfect matching, hence a
nonsingular principal submatrix.  The rank is therefore exactly \(2r-2\).
Relative to the support-matching count \(A_{C_{2r},i}(q-1)\), exactly
\((q-1)^{2r-1}\) full-support points move from rank \(2r\) to rank \(2r-2\).
This proves Theorem 2.

## Context

Rossmann (2022) asked how the numbers
\(\operatorname{ch}(\Gamma,i;q)\) depend on \(q\), and noted polynomiality for
edgeless graphs, paths, and complete graphs.  He explicitly reduced the
question, for odd \(q\), to rank counts of the edge-supported generic
antisymmetric matrix \(B_\Gamma\), while observing that such rank-count
problems can be complicated in general.

Wang and Zhou (2014) proved the fixed-support skew-rank theorem for graphs
with no even cycles.  The contribution here is to combine that fixed-support
rank rigidity with the graphical-group character formula, obtaining the
explicit support polynomial above, and then to isolate and count the single
Pfaffian-cancellation locus that completes the cycle family, including even
cycles.

A later paper of Qiao (2024) studies a different \(q\)-analogue associated
with graphical alternating matrix spaces, enumerating totally isotropic
subspaces / abelian subgroups.  Rossmann--Voll (2025) studies ask zeta
functions and graph joins, with applications to conjugacy-class enumeration.
Neither source located in the literature check states the character-degree
formulas above.

## Limitations

- The formulas are stated for odd \(q\), matching the range in which the
  O'Brien--Voll character formula is used for these class-two groups.
- The even-cycle-free result does not assert polynomiality for arbitrary
  graphs.  Even cycles already exhibit weight-dependent Pfaffian cancellation,
  and graphs with several interacting even cycles can have more complicated
  rank loci.
- The cycle correction is special to a graph having one cycle with exactly
  two perfect matchings on full support; no claim is made here for general
  unicyclic or cactus graphs containing even cycles.
- Originality is to the best of our knowledge.  The skew-rank facts and the
  O'Brien--Voll formula are prior results; the claimed contribution is their
  explicit character-enumeration synthesis for even-cycle-free graphical
  groups together with the all-cycle extension.

## References

1. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over
   finite fields*, Bull. Lond. Math. Soc. 54 (2022), 1923--1943.
   https://doi.org/10.1112/blms.12665
2. E. A. O'Brien and Christopher Voll, *Enumerating classes and characters of
   p-groups*, Trans. Amer. Math. Soc. 367 (2015), 7775--7796.
   https://doi.org/10.1090/tran/6276
3. Yanna Wang and Bo Zhou, *On the minimum skew rank of graphs*, ScienceAsia
   40 (2014), 313--316.
   https://doi.org/10.2306/scienceasia1513-1874.2014.40.313
4. Youming Qiao, *A q-analogue of graph independence polynomials with a
   group-theoretic interpretation*, 2024.
   https://arxiv.org/abs/2408.09963
5. Tobias Rossmann and Christopher Voll, *Ask zeta functions of joins of
   graphs*, 2025.
   https://arxiv.org/abs/2505.10263
