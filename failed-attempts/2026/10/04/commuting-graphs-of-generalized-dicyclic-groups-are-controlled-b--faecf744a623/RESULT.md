# Commuting graphs of generalized dicyclic groups are controlled by 2-torsion

## Finding

Let \(A\) be a finite abelian group of even order \(m\), let \(y\in A\) have order \(2\), and let
\[
G=\operatorname{Dic}(A,y)
=
\langle A,\gamma\mid
\gamma^2=y,\ 
\gamma^{-1}a\gamma=a^{-1}\text{ for every }a\in A
\rangle
\]
be nonabelian. Put
\[
T=A[2]=\{a\in A:a^2=1\},
\qquad
t=|T|.
\]

For the full commuting graph, whose vertex set is \(G\) and whose distinct vertices are adjacent exactly when they commute,
\[
\boxed{
\Gamma(G)
\cong
K_t\vee
\left(
K_{m-t}
\mathbin{\dot\cup}
\frac{m}{t}K_t
\right).
}
\]
Equivalently,
\[
\Gamma(G)-Z(G)
\cong
K_{m-t}
\mathbin{\dot\cup}
\frac{m}{t}K_t.
\]

Consequently every nonabelian generalized dicyclic group is an AC-group, and its full commuting graph is both a cograph and a chordal graph.

There is also an exact graph-isomorphism classification inside this family. If
\[
G_1=\operatorname{Dic}(A,y)
\qquad\text{and}\qquad
G_2=\operatorname{Dic}(B,z)
\]
are nonabelian, then
\[
\Gamma(G_1)\cong\Gamma(G_2)
\]
if and only if
\[
\bigl(|A|,|A[2]|\bigr)
=
\bigl(|B|,|B[2]|\bigr).
\]
In particular, the commuting graph is independent of the chosen distinguished involution.

## Assumptions and scope

The group is the standard generalized dicyclic extension of a finite abelian group by an element acting by inversion and squaring to a specified involution.

The nonabelian hypothesis is equivalent here to requiring that \(A\) have an element of order greater than \(2\). It ensures that the center of \(G\) is exactly \(A[2]\), rather than all of \(G\).

An AC-group is a finite group in which the centralizer of every noncentral element is abelian.

For graphs, \(\vee\) denotes graph join and \(\mathbin{\dot\cup}\) denotes disjoint union. The expression \((m/t)K_t\) means a disjoint union of \(m/t\) copies of \(K_t\). Since \(T\le A\), the integer \(t\) divides \(m\).

## Proof

Every element of \(G\) has a unique form \(a\) or \(a\gamma\), with \(a\in A\).

First determine the center. Every element of
\[
T=A[2]
\]
is fixed by inversion, so it commutes with \(\gamma\), and of course it commutes with \(A\). Hence
\[
T\le Z(G).
\]
If \(a\in A\setminus T\), then
\[
\gamma^{-1}a\gamma=a^{-1}\ne a,
\]
so \(a\notin Z(G)\). Since \(G\) is nonabelian, some element \(b\in A\) satisfies \(b\ne b^{-1}\), and no element outside \(A\) can commute with such a \(b\). Therefore
\[
Z(G)=T.
\]

Now take
\[
a\in A\setminus T.
\]
Every element of \(A\) commutes with \(a\). For \(x\in A\),
\[
(x\gamma)a(x\gamma)^{-1}=a^{-1}\ne a,
\]
so no element outside \(A\) centralizes \(a\). Thus
\[
C_G(a)=A.
\]

Next take an element
\[
x=a\gamma\in G\setminus A.
\]
For \(b\in A\),
\[
bx=xb
\]
holds exactly when
\[
b=b^{-1},
\]
that is, exactly when \(b\in T\).

For two elements outside \(A\),
\[
a\gamma
\qquad\text{and}\qquad
c\gamma,
\]
the multiplication rules give
\[
(a\gamma)(c\gamma)=ac^{-1}y
\]
and
\[
(c\gamma)(a\gamma)=ca^{-1}y.
\]
These are equal exactly when
\[
(ac^{-1})^2=1,
\]
or equivalently
\[
ac^{-1}\in T.
\]
Therefore
\[
C_G(a\gamma)
=
T\cup aT\gamma.
\]
This centralizer is abelian: \(T\) is central, and every two elements of the coset \(aT\gamma\) commute by the criterion just proved. Hence the centralizer of every noncentral element is abelian, so \(G\) is an AC-group.

The graph structure now follows directly. The center \(T\) is a clique adjacent to every vertex. The set
\[
A\setminus T
\]
is a clique of size \(m-t\). It has no edges to \(G\setminus A\). Finally, the outside coset \(A\gamma\) splits according to the \(m/t\) cosets of \(T\) in \(A\); each part
\[
aT\gamma
\]
is a clique of size \(t\), and two distinct parts have no edges between them. This proves
\[
\Gamma(G)
\cong
K_t\vee
\left(
K_{m-t}
\mathbin{\dot\cup}
\frac{m}{t}K_t
\right).
\]

A disjoint union of complete graphs is a cograph and a chordal graph, and adjoining a clique of universal vertices preserves both properties. Thus \(\Gamma(G)\) is a cograph and chordal. This also agrees with the general theorem that commuting graphs of AC-groups have both properties.

For the isomorphism classification, the graph has
\[
|G|=2m
\]
vertices, so its order determines \(m\). Its universal vertices are exactly the group center, hence there are exactly \(t\) of them. Thus graph isomorphism forces the same pair \((m,t)\). Conversely, the displayed graph decomposition depends only on \((m,t)\), so equality of those two parameters gives isomorphic commuting graphs.

## Verification

The included replay constructs generalized dicyclic groups directly from products of cyclic groups, with several distinct abelian kernels and several choices of distinguished involution.

For each tested group it verifies from the multiplication law that:

- the center is exactly \(A[2]\);
- every element of \(A\setminus A[2]\) has centralizer \(A\);
- every \(a\gamma\) has centralizer \(A[2]\cup aA[2]\gamma\);
- each noncentral centralizer is abelian;
- the direct commuting relation agrees edge-for-edge with
  \[
  K_t\vee
  \left(
  K_{m-t}
  \mathbin{\dot\cup}
  \frac{m}{t}K_t
  \right).
  \]

The examples include cyclic kernels, noncyclic kernels with the same values of \(m\) and \(t\), and kernels with different \(2\)-torsion ranks. The replay returns `VERIFY_OK`.

Finite computation is not used to prove the universal theorem.

## Relationship to prior work

Lazorec and Tărnăuceanu introduced the arbitrary-abelian-kernel generalized dicyclic family in the form used here. Their work studies subgroup and cyclic-subgroup commutativity probabilities; its full text defines the arbitrary kernel but does not study the element commuting graph.

Arvind, Ma, Cameron, and Maslova study when commuting graphs are cographs and chordal graphs. They prove that every AC-group has both properties. In their family section they prove the result for generalized dihedral groups and for generalized quaternion groups. The generalized quaternion calculation is the cyclic-kernel special case of the decomposition above. Their inspected current full text contains no generalized-dicyclic statement.

Chen and Tang study commuting graphs of the ordinary dicyclic group with cyclic kernel, and later spectral work likewise treats ordinary dicyclic groups. Those results supply important cyclic-kernel context but do not provide the arbitrary-abelian-kernel formula or the graph-isomorphism classification above.

The new contribution is therefore the arbitrary-kernel centralizer calculation and the resulting complete commuting-graph decomposition, which simultaneously proves the AC/cograph/chordal property and shows exactly which two kernel invariants the graph remembers.

## Limitations

The theorem concerns generalized dicyclic groups with abelian kernel and inversion action. It does not classify commuting graphs of arbitrary index-two extensions of abelian groups.

The graph determines only \(|A|\) and \(|A[2]|\) inside this family; it generally cannot be expected to recover the full isomorphism type of \(A\).

The ordinary-dicyclic literature is extensive. The most relevant arbitrary-kernel and cograph/chordal sources were inspected in full, and targeted searches found no equivalent arbitrary-kernel decomposition. An equivalent elementary centralizer calculation could nevertheless exist under different terminology or in unindexed literature.

## References

1. M.-S. Lazorec and M. Tărnăuceanu, “On some probabilistic aspects of (generalized) dicyclic groups,” arXiv:1612.01967v1, first public version 6 December 2016; later published in *Quaestiones Mathematicae* 44 (2021), 129–146, DOI 10.2989/16073606.2019.1673498.
2. V. Arvind, X. Ma, P. J. Cameron, and N. V. Maslova, “Aspects of the commuting graph,” arXiv:2305.07301, first public version 12 May 2023.
3. J. Chen and L. Tang, “The Commuting Graphs on Dicyclic Groups,” *Algebra Colloquium* 27 (2020), 799–806, DOI 10.1142/S1005386720000668.
4. B. A. Rather, F. Ali, N. Ullah, A.-S. Mohammad, A. Din, and Sehra, “\(A_\alpha\) matrix of commuting graphs of non-abelian groups,” *AIMS Mathematics* 7 (2022), 15436–15452, DOI 10.3934/math.2022845.
