# Exact minimum-generator independence degrees of finite nilpotent groups

## Finding

Let
\[
G=\prod_{p\in\pi(G)}G_p
\]
be a finite nilpotent group, with \(G_p\) its Sylow \(p\)-subgroup. Put
\[
\Phi_p=\Phi(G_p),
\qquad
V_p=G_p/\Phi_p,
\qquad
d_p=\dim_{\mathbf F_p}V_p,
\qquad
d=\max_p d_p=d(G).
\]

For \(g=(g_p)_p\in G\), let \(\Gamma_d(G)\) be the graph whose vertices are the elements of \(G\), with distinct vertices adjacent when they occur together in a minimal generating set of cardinality \(d\).

Define
\[
A_p(g)=
\begin{cases}
0, & d_p=d\ \text{and}\ g_p\in\Phi_p,\\
p^d-p, & d_p=d\ \text{and}\ g_p\notin\Phi_p,\\
p^{d-1}-1, & d_p=d-1\ \text{and}\ g_p\in\Phi_p,\\
p^{d-1}, & d_p=d-1\ \text{and}\ g_p\notin\Phi_p,\\
p^{d_p}, & d_p\le d-2.
\end{cases}
\]

Then
\[
\boxed{
\deg_{\Gamma_d(G)}(g)
=
|\Phi(G)|\prod_{p\in\pi(G)}A_p(g).
}
\]

Consequently,
\[
\boxed{
|g|\mid \deg_{\Gamma_{d(G)}(G)}(g)
}
\]
for every \(g\in G\), with the usual convention that every positive integer divides \(0\).

Thus Question 21 in Lucchini's 2020 paper on the independence graph has an affirmative answer for the entire class of finite nilpotent groups.

## Assumptions and scope

For a finite group \(X\), \(\Gamma_u(X)\) denotes the graph in which two distinct elements are adjacent if they occur together in a minimal generating set of size \(u\). The parameter
\[
d(X)
\]
is the minimum size of a generating set.

For a finite \(p\)-group \(P\), Burnside's basis theorem identifies minimal generating sets with bases of
\[
P/\Phi(P).
\]
For a finite nilpotent group,
\[
G=\prod_p G_p,
\qquad
\Phi(G)=\prod_p\Phi(G_p),
\]
and a tuple generates \(G\) exactly when its projections generate every Sylow subgroup.

The theorem concerns \(\Gamma_{d(G)}(G)\), not the full independence graph \(\Gamma(G)\). These graphs can differ for nilpotent groups whose Sylow subgroups have unequal generator ranks.

## Proof

Consider distinct \(x,y\in G\). Their images in
\[
V_p=G_p/\Phi_p
\]
will be denoted by \(\overline x_p,\overline y_p\).

A set of \(d\) elements generates \(G\) if and only if, for every prime \(p\), its images span \(V_p\). Since \(d=d(G)\), every generating set of cardinality \(d\) is automatically minimal.

After fixing \(x\) and \(y\), there remain \(d-2\) positions. Over \(\mathbf F_p\), the pair
\[
\overline x_p,\overline y_p
\]
can be extended by \(d-2\) vectors to span the \(d_p\)-dimensional space \(V_p\) if and only if
\[
\operatorname{rank}\langle\overline x_p,\overline y_p\rangle
\ge d_p-(d-2).
\]
Hence the adjacency conditions are exactly:

\[
\begin{array}{c|c}
d_p & \text{condition on }\overline x_p,\overline y_p\\
\hline
d & \text{linearly independent}\\
d-1 & \text{not both zero}\\
\le d-2 & \text{no condition}.
\end{array}
\]

The completions can be chosen independently in every Sylow quotient and then combined componentwise in \(G\). Because at least one \(d_p\) equals \(d\), a completed \(d\)-tuple has \(d\) distinct elements: in a maximal-rank Sylow quotient its \(d\) images form a basis.

Now fix \(g\in G\) and count its neighbors.

If \(d_p=d\), then a nonzero vector \(\overline g_p\) has
\[
p^d-p
\]
vectors outside its one-dimensional span, while \(\overline g_p=0\) has no independent partner.

If \(d_p=d-1\), then every vector is allowed when \(\overline g_p\ne0\), giving
\[
p^{d-1}
\]
choices; when \(\overline g_p=0\), the partner must be nonzero, giving
\[
p^{d-1}-1
\]
choices.

If \(d_p\le d-2\), all
\[
p^{d_p}
\]
vectors are allowed.

Every quotient choice has exactly
\[
|\Phi_p|
\]
lifts to \(G_p\). Multiplying over the primes gives
\[
\deg_{\Gamma_d(G)}(g)
=
|\Phi(G)|\prod_p A_p(g).
\]

It remains to prove divisibility by \(|g|\).

Fix a prime \(p\), and write
\[
|\Phi_p|=p^{f_p},
\qquad
|g_p|=p^{a_p}.
\]
If \(g_p\in\Phi_p\), then
\[
a_p\le f_p.
\]
If \(g_p\notin\Phi_p\), the image of the cyclic group \(\langle g_p\rangle\) in the elementary abelian quotient has order \(p\), so
\[
|\langle g_p\rangle\cap\Phi_p|
=
p^{a_p-1}.
\]
Therefore
\[
a_p\le f_p+1.
\]

Assume first that the displayed degree is nonzero. If \(g_p\notin\Phi_p\), the \(p\)-part contributed by the \(p\)-factor beyond \(|\Phi_p|\) is at least one power of \(p\): it is \(p\) when \(d_p=d\), at least \(p\) when \(d_p=d-1\), and \(p^{d_p}\) when \(d_p\le d-2\). Thus
\[
v_p(\deg(g))\ge f_p+1\ge a_p.
\]
If \(g_p\in\Phi_p\), the factor \(|\Phi_p|\) alone gives
\[
v_p(\deg(g))\ge f_p\ge a_p.
\]
Hence the \(p\)-part of \(|g|\) divides the degree for every prime \(p\), proving
\[
|g|\mid\deg_{\Gamma_d(G)}(g).
\]

If the degree is zero, the divisibility statement is immediate.

## Verification

The included replay performs two independent finite checks.

First, it constructs the groups
\[
C_2^2\times C_3,\qquad
D_8\times C_3,\qquad
D_8\times C_3^2,\qquad
C_4\times C_2\times C_3
\]
from explicit multiplication laws. Each has \(d(G)=2\). For every element \(g\), the program enumerates every \(h\), generates the subgroup
\[
\langle g,h\rangle
\]
directly from multiplication, and therefore computes the degree in \(\Gamma_2(G)\) without using the formula. It checks equality with the theorem and verifies
\[
|g|\mid\deg(g)
\]
element by element.

These examples exercise all relevant rank-two branches: equal maximal Sylow ranks, unequal ranks, nontrivial Frattini subgroups, and elements both inside and outside those Frattini subgroups.

Second, the replay exhaustively checks the rank-three quotient profile
\[
\mathbf F_2^3\times\mathbf F_3^2.
\]
For each ordered pair of quotient elements, it searches all possible third vectors and determines directly whether the pair can be completed to a generating triple. The resulting degrees agree with the quotient factors in the theorem.

The replay returns `VERIFY_OK`.

Finite checks are not used as the proof of the universal statement.

## Relationship to prior work

Lucchini introduced the independence graph and the fixed-cardinality graphs \(\Gamma_u(G)\). In Question 21 he asks whether
\[
|g|
\]
always divides the degree of \(g\) in
\[
\Gamma_{d(G)}(G).
\]

The same paper proves a Hamiltonicity theorem for finite noncyclic nilpotent groups using the full independence graph \(\Delta(G)\). Its proof observes that for a non-isolated element \(g\),
\[
\deg_{\Delta(G)}(g)
=
|G|-|\langle g\rangle\Phi(G)|.
\]
That statement concerns the union over all sizes of minimal generating sets.

For a finite \(p\)-group, every minimal generating set has cardinality \(d(G)\), so the \(p\)-group slice of the present theorem is already implicit in that argument. The new content is the mixed-prime nilpotent case, where minimal generating sets can have different cardinalities and \(\Gamma_{d(G)}(G)\) is generally a proper subgraph of the full independence graph. The Sylow rank profile
\[
(d_p)_p
\]
then creates the three different local adjacency regimes appearing in the formula.

A later classification paper on the independence property studies a different question: whether every pair of distinct elements is either independent or power-related. Targeted searches for the exact degree formula, the minimum-generator graph of nilpotent groups, and the divisibility question did not locate a solution of Question 21 for the full nilpotent class.

## Limitations

The theorem settles Question 21 only for finite nilpotent groups; it does not address arbitrary soluble or nonsoluble groups.

The formula uses the Sylow generator ranks and Frattini membership of the components of \(g\). It does not claim that the degree determines the isomorphism type of \(G\).

The finite \(p\)-group specialization is not claimed as new: it is implicit in the nilpotent argument already present in the 2020 source. The originality claim is the exact mixed-prime formula and the resulting all-nilpotent divisibility theorem.

An equivalent mixed-prime formulation may exist under generating hypergraph, matroid-like generation, or Frattini-quotient terminology not located by the searches.

## References

1. A. Lucchini, “The independence graph of a finite group,” arXiv:2004.14651v1, first public version 30 April 2020; *Monatshefte für Mathematik* 193 (2020), 845–856, DOI 10.1007/s00605-020-01445-0.
2. S. D. Freedman, A. Lucchini, D. Nemmi, and C. M. Roney-Dougal, “Finite groups satisfying the independence property,” arXiv:2208.04064v1, first public version 8 August 2022; *International Journal of Algebra and Computation* 33 (2023), 1419–1444, DOI 10.1142/S021819672350025X.
