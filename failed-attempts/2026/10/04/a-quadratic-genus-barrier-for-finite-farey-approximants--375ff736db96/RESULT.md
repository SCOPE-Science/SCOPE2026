# A quadratic genus barrier for finite Farey approximants
## Finding

Let
\[
n\ge6,
\]
and let \(G\) be a finite simple graph satisfying the finite Farey axioms used by Lockhart:

\[
\varphi_0:
\]
every edge of \(G\) lies in exactly two triangles and every vertex has degree at least \(3\);

and

\[
\psi_n:
\]
every induced subgraph of \(G\) with at most \(n\) vertices has a removable vertex.

Here a vertex is removable when it has degree at most \(1\), or has degree \(2\) and its two neighbors are adjacent.

Then every vertex of \(G\) has degree at least \(n\):
\[
\boxed{\delta(G)\ge n.}
\]

Consequently every connected component \(H\) of \(G\) satisfies
\[
|V(H)|\ge n+1
\]
and
\[
|E(H)|\ge\frac{n(n+1)}2.
\]

If \(G\) embeds in an orientable surface of genus \(g\), then
\[
\boxed{
g\ge
1+
\left\lceil
\frac{(n-6)(n+1)}{12}
\right\rceil.
}
\]

Thus any sequence of finite graphs satisfying
\[
\varphi_0,\psi_6,\psi_7,\ldots
\]
to increasing depth must have orientable genus growing at least quadratically with the depth parameter.

The first forced genus lower bounds are
\[
1,2,3,4,5,6,8,10,11,\ldots
\]
for
\[
n=6,7,8,9,10,11,12,13,14,\ldots.
\]

Lockhart proves that no finite planar graph satisfies \(\varphi_0\) and \(\psi_n\) for \(n\ge6\), and constructs finite approximants on higher-genus surfaces. The theorem above shows that the passage to higher genus is not merely a feature of that construction: every finite approximant is forced to pay a quantitative topological cost.

## Assumptions and scope

Graphs are finite and simple, as in the primary source.

The axiom \(\psi_n\) is interpreted on induced substructures, equivalently on the graph induced by each vertex subset of size at most \(n\).

The orientable genus \(g\) is the least genus of a compact orientable surface into which the abstract graph embeds.

The proof uses only the local Farey axioms and the standard Euler inequality for a simple graph embedded in an orientable surface:
\[
|E|\le3|V|-6+6g
\]
for a connected component with at least three vertices.

No claim is made that the genus bound is optimal, or that Lockhart's triangulation construction attains the same asymptotic constant.

## Proof

Fix a vertex \(v\in V(G)\), and consider its closed neighborhood
\[
N[v]=\{v\}\cup\{w:E(v,w)\}.
\]

We claim that the induced subgraph on \(N[v]\) has no removable vertex.

First, \(\varphi_0\) says that \(v\) has degree at least \(3\) in \(G\). Every neighbor of \(v\) belongs to \(N[v]\), so the degree of \(v\) inside the induced subgraph \(G[N[v]]\) is also at least \(3\).

Now let \(w\) be any neighbor of \(v\). The edge
\[
\{v,w\}
\]
lies in exactly two triangles. Hence there are two distinct vertices
\[
z_1,z_2
\]
such that
\[
\{v,w,z_1\}
\quad\text{and}\quad
\{v,w,z_2\}
\]
are triangles.

Both \(z_1\) and \(z_2\) are adjacent to \(v\), so both lie in \(N[v]\). Therefore, inside \(G[N[v]]\), the vertex \(w\) is adjacent to the three distinct vertices
\[
v,z_1,z_2.
\]
Thus every neighbor \(w\) of \(v\) has degree at least \(3\) in the induced closed neighborhood.

Every vertex of \(G[N[v]]\) consequently has degree at least \(3\). No vertex is removable.

If
\[
|N[v]|\le n,
\]
this contradicts \(\psi_n\). Hence
\[
|N[v]|>n.
\]

Since
\[
|N[v]|=\deg(v)+1,
\]
we obtain
\[
\deg(v)\ge n.
\]

Because \(v\) was arbitrary,
\[
\delta(G)\ge n.
\]

Now take any connected component \(H\) of \(G\). The minimum-degree bound gives
\[
|V(H)|\ge n+1,
\]
because a simple graph on \(m\) vertices has maximum degree \(m-1\).

By the handshaking lemma,
\[
2|E(H)|
=
\sum_{x\in V(H)}\deg_H(x)
\ge
n|V(H)|.
\]
Therefore
\[
|E(H)|\ge\frac{n|V(H)|}{2}
\ge
\frac{n(n+1)}2.
\]

Suppose \(G\) embeds in an orientable surface of genus \(g\). Then \(H\) also embeds there. The Euler inequality for a finite connected simple graph on an orientable genus-\(g\) surface gives
\[
|E(H)|
\le
3|V(H)|-6+6g.
\]

Combining this with the minimum-degree estimate,
\[
\frac{n|V(H)|}{2}
\le
3|V(H)|-6+6g.
\]

Multiplying by \(2\),
\[
n|V(H)|
\le
6|V(H)|-12+12g.
\]

Thus
\[
(n-6)|V(H)|
\le
12(g-1).
\]

For
\[
n\ge6,
\]
the left coefficient is nonnegative, and
\[
|V(H)|\ge n+1.
\]
Hence
\[
(n-6)(n+1)
\le
12(g-1).
\]

Since \(g\) is an integer,
\[
g
\ge
1+
\left\lceil
\frac{(n-6)(n+1)}{12}
\right\rceil.
\]

This proves the theorem.

## Verification

The load-bearing local step was checked directly against the axioms reproduced in Lockhart's Theorem 3 and against the definition of removable vertex.

The argument needs exactly the following facts:

- every vertex has degree at least \(3\);
- every edge has two distinct common neighbors forming the two required triangles;
- every induced subgraph of size at most \(n\) must have a removable vertex.

For each vertex \(v\), those facts imply that every vertex of the induced closed neighborhood \(G[N[v]]\) has degree at least \(3\), so \(G[N[v]]\) has no removable vertex. The conclusion
\[
|N[v]|>n
\]
is therefore forced by \(\psi_n\).

The genus calculation was independently replayed from
\[
2|E|\ge n|V|,
\qquad
|V|\ge n+1,
\qquad
|E|\le3|V|-6+6g.
\]

The bundled checker evaluates the exact integer lower bound over a range of \(n\) and verifies the algebraic implication from the three displayed inequalities.

No finite computation is used to infer the arbitrary-\(n\) theorem.

## Relationship to prior work

Lockhart proves pseudofiniteness of the Farey graph by constructing finite graphs that satisfy increasingly large finite portions of the Tent--Mohammadi axiomatization. The construction uses highly connected, highly representative triangulations of orientable surfaces.

Lockhart also proves the planar obstruction:
for
\[
n\ge6,
\]
no finite planar graph satisfies \(\varphi_0\) and \(\psi_n\). The proof picks a vertex of degree at most \(5\), observes that its closed neighborhood has at most \(6\) vertices and no removable vertex, and contradicts \(\psi_6\).

The present theorem extracts the latent general statement behind that argument:
\[
\varphi_0+\psi_n
\Longrightarrow
\delta(G)\ge n.
\]
Combining this with the Euler edge bound on an orientable surface gives a quadratic lower bound on the genus of every finite approximant, not only a planar impossibility result.

Tent and Mohammadi give the underlying axiomatization and the removable-vertex notion. Their model-theoretic paper classifies models of the complete Farey theory but does not discuss finite approximate models or quantitative genus lower bounds.

Targeted searches for Farey pseudofiniteness together with minimum degree, orientable genus, quadratic genus growth, and finite approximants did not locate this bound.

## Limitations

The genus estimate is a lower bound and is not claimed sharp.

The argument uses the orientable Euler inequality. A corresponding nonorientable estimate can be derived from the appropriate Euler characteristic bound, but it is not included here.

The theorem concerns finite approximate models of the local axiom package \(\varphi_0+\psi_n\). Infinite models of the complete Farey theory have a different global structure and are not assigned a finite graph genus by this statement.

The source's construction imposes stronger hypotheses, including high connectivity and representativity. No upper bound on the minimum genus required to realize \(\varphi_0+\psi_n\) is established here.

## References

[1] Connor M. Lockhart, “Pseudofiniteness of the Farey Graph,” arXiv:2603.23900, first posted 25 March 2026.

[2] Zahra Mohammadi Khangheshlaghi and Katrin Tent, “On the model theory of the Farey graph,” arXiv:2503.02121, first posted 3 March 2025, revised 15 April 2026.

[3] Erin W. Chambers, “Surface embedded graphs,” lecture notes, 2017. The notes record the standard orientable-surface edge inequality \(|E|\le3|V|-6+6g\).
