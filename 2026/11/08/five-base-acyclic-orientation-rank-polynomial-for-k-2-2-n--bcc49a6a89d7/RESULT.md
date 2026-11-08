# Five-base acyclic-orientation rank polynomial for \(K_{2,2,n}\)

## Finding
For every integer \(n\ge1\), let \(G_n=K_{2,2,n}\) have named independent parts \(A,B,C\) of sizes \(2,2,n\), respectively. Define \(D_n\) to direct every cross-part edge from \(A\) toward \(B\) or \(C\), and from \(B\) toward \(C\). For an acyclic orientation \(O\), let \(\operatorname{rk}_{D_n}(O)\) be the number of directed edges of \(O\) opposite to those of \(D_n\), and put
\[
\Psi_n(t)=\sum_{O\in\mathcal{AO}(G_n)}t^{\operatorname{rk}_{D_n}(O)}.
\]
Set
\[
\begin{aligned}
L_0(t)&=1+t^2+t^4,\\
L_1(t)&=1+t+t^2+t^4,\\
L_2(t)&=1+t+t^3+t^4,\\
L_3(t)&=1+t^2+t^3+t^4,\\
L_4(t)&=1+t+t^2+t^3+t^4.
\end{aligned}
\]
Then the complete acyclic polynomial, including every edge-disagreement coefficient, is
\[
\boxed{
\Psi_n(t)=(1+t^4)\bigl(L_0(t)^n-2L_1(t)^n-2L_3(t)^n\bigr)
-4t^2L_2(t)^n
+4(1+t^2)(1+t+t^2)L_4(t)^n.}
\tag{1}
\]
For example,
\[
\Psi_1(t)=1+6t+9t^2+14t^3+18t^4+14t^5+9t^6+6t^7+t^8.
\]
The specialization \(\Psi_n(1)=24\cdot5^n-12\cdot4^n+2\cdot3^n\) recovers the unweighted acyclic-orientation count. For \(n\ge1\), the specialization \(\Psi_n(-1)=2\cdot3^n-8\cdot2^n+8\) is a signed parity check and is **not** presented as a new signature method: a prior signed-algebra result treats broader complete-multipartite graphs at \(t=-1\). The polynomial (1), not these specializations alone, is the finding.

## Assumptions and scope
The graph is finite and simple, with two specified two-vertex independent parts and one specified \(n\)-vertex independent part. Vertices are labeled; there are exactly \(4+4n\) edges. The reference \(D_n\) is the acyclic part-order orientation described above; the polynomial depends on this reference convention (other reference acyclic orientations give the same polynomial up to the corresponding edge-disagreement transformation only when justified). All identities are in \(\mathbb{Z}[t]\). The source-layer derivation also covers the boundary \(n=0\) when the third part is empty, but (1) is claimed for \(n\ge1\).

## Proof
**Canonical source layers.** In any acyclic orientation of a complete multipartite graph, its nonempty source set is contained entirely in a single part: two sources from different parts would be joined by an edge and cannot both have indegree zero. Iteratively deleting all sources yields an ordered sequence of nonempty vertex blocks. Each block belongs to a single part, and consecutive blocks must have different part labels: if two consecutive blocks lay in the same independent part, all vertices of the later block would already have been sources at the earlier stage. Conversely, any ordered partition into nonempty monochromatic blocks with unequal adjacent part labels uniquely specifies an acyclic orientation, by directing each cross-part edge from its earlier block to its later block. Distinct such ordered block partitions give distinct orientations, since they are recovered as successive source sets.

For a part ordered before another in \(D_n\), every reversed edge corresponds exactly to a pair of vertices whose source blocks appear in the opposite order. Thus each ordered block sequence has weight \(t^I\), where \(I\) is the sum of the products of block sizes over inverted cross-part pairs.

**Delete the \(C\)-blocks.** Keep the resulting nonempty \(A/B\) *skeleton*. Within each of \(A\) and \(B\), the ordered block-size composition is either \((2)\) or \((1,1)\). Interleaving the two ordered compositions produces exactly \(2+3+3+6=14\) skeletons. For a skeleton \(\beta=((\tau_1,k_1),\ldots,(\tau_s,k_s))\), \(\tau_i\in\{A,B\}\), let
\[
I(\beta)=\sum_{i<j:\,\tau_i=B,\,\tau_j=A} k_i k_j,
\qquad
r_g(\beta)=\sum_{j>g}k_j\quad(0\le g\le s).
\]
The skeleton has labeled-vertex multiplicity
\[
w(\beta)=\frac{(2!)^2}{\prod_{i=1}^s k_i!}.
\]
At each gap \(g\) before, between, or after skeleton blocks, at most one nonempty \(C\)-block can be inserted: two consecutive \(C\)-blocks would merge into one source set. A gap between equal adjacent \(A/B\) labels is *mandatory* for a nonempty \(C\)-block, since otherwise those skeleton blocks would be adjacent and equal-labeled. All other gaps are optional. A \(C\)-block of size \(j\) in gap \(g\) reverses exactly \(jr_g(\beta)\) of the \(C\)-to-\(A/B\) edges relative to \(D_n\), yielding weight \(t^{jr_g(\beta)}\). Since the \(C\)-vertices are labeled, its exponential generating function is \(e^{t^{r_g(\beta)}z}-1\). An optional gap has factor \(e^{t^{r_g(\beta)}z}\).

Consequently the entire exponential generating function, \(H(z;t)=\sum_{n\ge0}\Psi_n(t)z^n/n!\), is the *finite* 14-skeleton sum
\[
H(z;t)=\sum_{\beta}w(\beta)t^{I(\beta)}
\prod_{g=0}^{s(\beta)}e^{t^{r_g(\beta)}z}
\prod_{\substack{1\le g<s(\beta)\\\tau_g=\tau_{g+1}}}
\bigl(1-e^{-t^{r_g(\beta)}z}\bigr).
\tag{2}
\]
The skeleton index in (2) ranges over the two compositions of \(2\) for each of \(A,B\) and all order-preserving interleavings of their blocks; thus (2) is a fully specified finite expression, without a probabilistic or asymptotic step.

**Exact finite simplification.** Expanding the mandatory-gap factors in the 14 terms of (2), then collecting identical exponential bases, yields exactly the following five exponent/coefficient pairs:
\[
\begin{array}{c|c}
\text{exponent }\lambda(t)&\text{coefficient of }e^{\lambda(t)z}\\\hline
L_0(t)&1+t^4\\
L_1(t)&-2(1+t^4)\\
L_2(t)&-4t^2\\
L_3(t)&-2(1+t^4)\\
L_4(t)&4(1+t^2)(1+t+t^2)
\end{array}
\tag{3}
\]
This is an elementary finite polynomial identity, not a fitted sequence: it can be checked by expanding the \(14\) explicitly defined skeletons in (2), or independently by the exact 14-skeleton symbolic reduction included in `artifacts/verify.py`. Equations (2) and (3) imply
\[
H(z;t)=(1+t^4)e^{L_0z}-2(1+t^4)e^{L_1z}-4t^2e^{L_2z}
-2(1+t^4)e^{L_3z}+4(1+t^2)(1+t+t^2)e^{L_4z}.
\]
Taking \(n!\,[z^n]\) proves (1) for each integer \(n\ge0\), in particular \(n\ge1\).

**Basic consequences.** Substitution of \(t=1\) and \(t=-1\) into (1) gives the two displayed evaluations; the \(L_2(-1)^n=0\) term vanishes for \(n\ge1\). Reversing every edge is an involution on acyclic orientations that maps rank \(k\) to rank \(4+4n-k\), so \(\Psi_n(t)\) is palindromic of degree \(4+4n\).

## Verification
Run `python3 artifacts/verify.py` from the extracted package; it requires only Python's standard library. It checks the exact 14-skeleton-to-five-exponential identity as polynomial dictionaries with integer coefficients, and independently computes the source-layer recurrence and the five-base expression for every \(0\le n\le12\). It further enumerates all \(2^{4+4n}\) directed-edge assignments for \(0\le n\le4\), tests directed acyclicity using indegrees, and checks every coefficient. Recorded successful output:

```text
EXACT_14_SKELETON_SYMBOLIC_REDUCTION_OK skeletons=14 profiles=5
EXACT_SOURCE_LAYER_AND_FIVE_POWER_FORMULA_OK n=0..12
ALL_EDGE_ORIENTATIONS_OK n=0 edges=4 acyclic=14
ALL_EDGE_ORIENTATIONS_OK n=1 edges=8 acyclic=78
ALL_EDGE_ORIENTATIONS_OK n=2 edges=12 acyclic=426
ALL_EDGE_ORIENTATIONS_OK n=3 edges=16 acyclic=2286
ALL_EDGE_ORIENTATIONS_OK n=4 edges=20 acyclic=12090
VERIFY_OK
```

The exact finite algebra (3), together with the source-layer bijection, proves the unrestricted identity. Bounded graph enumeration is only a secondary check, not a proof for arbitrary \(n\).

## Relationship to prior work
Mühlherr and Poullot (2026) define the acyclic polynomial and study parity/Hamiltonicity. Their Conjecture 1 discusses complete tripartite graphs, and their sample table covers \(K_{2,2,p}\) for a bounded range. The accessible full arXiv HTML, including the acyclic-polynomial discussion and examples, did not state the complete five-base polynomial (1). The present contribution refines their framework with exact information for every rank layer.

Carballosa, Khera and Reyes (2025; preprint 2023) give an encoding and a closed formula for the *total* number of labeled acyclic orientations of general complete multipartite graphs. Their source-set encoding is compatible with our first step, but their unweighted total does not determine the full disagreement polynomial. The \(t=1\) specialization is covered by their more general enumeration in principle.

The published *Factorial acyclic signatures for complete graphs minus a matching* (2026) supplies a general signed algebra and values of the \(t=-1\) signature, including a family containing \(K_{2,2,2}\). Its signed algebra may also yield the \(t=-1\) specialization for related multipartite graphs. Neither that signed specialization nor its Hamiltonicity obstruction is claimed as the core new result. The all-coefficient formula (1) is stronger information and is not implied by a single evaluation at \(t=-1\).

The OEIS complete-tripartite orientation table A372261 records total counts, corroborating \(78,426,2286,12090\), but not the ranked coefficients of (1). Priority of the complete formula is asserted only to the best of current accessible-literature knowledge, not independently certified.

## Limitations
The theorem gives the polynomial for the part-ordered reference \(D_n\), and does not supply a formula for every possible reference orientation or for all general complete multipartite graphs. It is a finite-base enumeration, not a characterization of Hamiltonian paths or cycles in orientation-flip graphs. External priority remains provisional, including the possibility of an older equivalent inversion enumerator under other terminology. Independent mathematical audit has not been performed.

## References
1. L. Mühlherr and G. Poullot, *Hamiltonicity of graphs of acyclic orientations and acyclic polynomials*, arXiv:2609.02249, first posted 2026-09-02. https://arxiv.org/abs/2609.02249
2. W. Carballosa, J. Khera and F. Reyes, *Encoding and enumerating acyclic orientations of graphs*, *Utilitas Mathematica* 125 (2025), 21–41; preprint arXiv:2303.09021. https://doi.org/10.61091/um125-02
3. *Factorial acyclic signatures for complete graphs minus a matching*, published-finding corpus (2026). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-acyclic-signatures-complete-graphs-minus-matching--c164cb9690e5
4. OEIS A372261, total acyclic orientations of complete tripartite graphs. https://oeis.org/A372261
