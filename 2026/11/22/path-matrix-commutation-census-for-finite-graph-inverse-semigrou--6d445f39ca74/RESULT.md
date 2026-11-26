# Path-matrix commutation census for finite graph inverse semigroups

## Finding

Let \(E\) be any finite directed acyclic multigraph with vertex set \(V\), permitting parallel directed edges and isolated vertices. In its graph inverse semigroup \(G(E)\), write \(C(a)=\{b\in G(E):ab=ba\}\). Let \(m_{uv}\) denote the number of directed paths from \(u\) to \(v\), including the length-zero path when \(u=v\), and set
\[
p_v=\sum_{u\in V}m_{uv},\qquad Q=\sum_{v\in V}p_v^2,
\]
\[
A_{vw}=p_vp_w-p_wm_{wv}-p_vm_{vw}+\mathbf 1_{v=w}p_v.
\]
Then \(|G(E)|=1+Q\), and the exact number of **ordered commuting pairs**, including pairs involving the zero element, is
\[
\boxed{K(E)=1+2Q-\sum_{v\in V}p_v+\sum_{v,w\in V}A_{vw}^2+2\sum_{v,w\in V}p_vm_{vw}^2.}
\]
Consequently the commutativity probability equals \(K(E)/(1+Q)^2\). The order, pair count, and probability can be obtained from the vertex path-count matrix alone, without enumerating paths, elements, or products of \(G(E)\). The formulas below also answer an individual centralizer query without such enumeration: for a specified nonzero element, they use its two concrete paths in addition to the matrix.

## Assumptions and scope

A path includes a length-zero vertex path. Write \(\mathcal P_v\) for paths ending at vertex \(v\) and \(\mathcal P\) for all paths. Every nonzero element of \(G(E)\) has a unique expression \(\alpha\beta^{-1}\) with \(\alpha,\beta\in\mathcal P_v\) for some \(v\). The other element is \(0\). Define \(\lambda\preceq\gamma\) when \(\lambda\) is an initial subpath (prefix) of \(\gamma\); write \(\lambda\sim\gamma\) for prefix comparability in either direction.

For each path \(\lambda\) and vertex \(w\), put
\[
c_w(\lambda)=\#\{\gamma\in\mathcal P_w:\gamma\sim\lambda\}.
\]
For distinct paths \(\alpha,\beta\in\mathcal P_v\), let \(L(\alpha,\beta)\) count their common prefixes (including length-zero prefixes, if they have the same start vertex). Then the complete centralizer formulas are
\[
\boxed{|C(0)|=1+Q,}
\]
\[
\boxed{|C(\alpha\alpha^{-1})|=1+\sum_{w\in V}\bigl(c_w(\alpha)^2+(p_w-c_w(\alpha))^2\bigr),}
\]
\[
\boxed{|C(\alpha\beta^{-1})|=1+L(\alpha,\beta)+\sum_{w\in V}(p_w-c_w(\alpha))(p_w-c_w(\beta)),\quad\alpha\ne\beta.}
\]
These are explicit from directed-path data: \(c_w(\lambda)=1\) if vertex \(w\) occurs on \(\lambda\), and otherwise \(c_w(\lambda)=m_{r(\lambda),w}\), where \(r(\lambda)\) is the terminal vertex. Acyclicity prevents proper prefixes of \(\lambda\) and proper extensions of \(\lambda\) from ending at the same vertex. Common prefixes are compared as edge sequences with their starting vertices, so distinct parallel edges are distinguished. For instance, in the three-vertex chain \(u\to v\to w\), the idempotents of the vertex path \(w\) and the full path \(u\to v\to w\) have centralizer sizes 11 and 9, respectively, although their paths have the same terminal vertex. The formulas apply for every acyclic multigraph, not only trees or simple graphs; no field is involved.

## Proof

**1. Prefix multiplication and acyclicity.** In the standard normal form, the product of \(\alpha\beta^{-1}\) and \(\gamma\delta^{-1}\) vanishes unless \(\beta\sim\gamma\). If \(\gamma=\beta\eta\), the product is \((\alpha\eta)\delta^{-1}\); if \(\beta=\gamma\eta\), the product is \(\alpha(\delta\eta)^{-1}\). If two distinct paths with the same terminal vertex were comparable, their difference would be a nonempty directed closed path. Since \(E\) is acyclic, distinct members of the same \(\mathcal P_v\) are incomparable. Hence every non-idempotent nonzero element has square zero, while the nonzero idempotents are precisely \(\lambda\lambda^{-1}\).

**2. Nonzero commuting products.** Suppose \(a=\alpha\beta^{-1}\) and \(b=\gamma\delta^{-1}\) are non-idempotents and \(ab=ba\ne0\). Nonvanishing gives \(\beta\sim\gamma\) and \(\delta\sim\alpha\). Equality of the two nonzero normal forms additionally forces \(\alpha\sim\gamma\) by comparing their numerator prefixes, and \(\beta\sim\delta\) by comparing their denominator prefixes. A path comparable to two mutually incomparable paths must be a common prefix of them. Thus \(\gamma\) and \(\delta\) are both common prefixes of the incomparable paths \(\alpha,\beta\), so \(\gamma\sim\delta\), contradicting that they are distinct paths ending at the same vertex. Therefore two non-idempotents can commute only with common product zero.

**3. Centralizers.** Consider an idempotent \(e=\lambda\lambda^{-1}\) and \(b=\gamma\delta^{-1}\), with \(\gamma,\delta\) ending at \(w\). The equality \(eb=be\) holds exactly when either both \(\gamma,\delta\) are comparable to \(\lambda\), or neither is. In the first case the two products are equal and nonzero; if \(\gamma\ne\delta\), both extend \(\lambda\). Indeed if one is a prefix of \(\lambda\), the other would have to be another prefix ending at the same vertex or an extension returning to that vertex, neither possible for distinct paths in a DAG. This gives \(c_w(\lambda)^2+(p_w-c_w(\lambda))^2\) choices for \(b\) in the class indexed by \(w\).

For \(a=\alpha\beta^{-1}\) non-idempotent, step 2 shows that a commuting \(b\) either satisfies \(ab=ba=0\) or is an idempotent with a nonzero common product. The zero-product case consists of \(b=0\), and nonzero \(b=\gamma\delta^{-1}\) with \(\gamma\not\sim\beta\) and \(\delta\not\sim\alpha\), counted by \((p_w-c_w(\beta))(p_w-c_w(\alpha))\) for each \(w\). In the other case \(b=\lambda\lambda^{-1}\), and nonzero commutation occurs exactly when \(\lambda\) is a common prefix of \(\alpha\) and \(\beta\). This proves all three centralizer formulas.

**4. Aggregation into a vertex-matrix formula.** For each \(v,w\in V\), count prefix-comparable paths as
\[
B_{vw}:=\sum_{\alpha\in\mathcal P_v}c_w(\alpha)
=p_wm_{wv}+p_vm_{vw}-\mathbf 1_{v=w}p_v.
\]
The first summand selects a prefix ending at \(w\) followed by a path to \(v\); the second selects \(\alpha\) ending at \(v\) followed by a path to \(w\). Their overlap consists only of the \(p_v\) equal-prefix cases when \(v=w\). Thus \(A_{vw}=p_vp_w-B_{vw}=\sum_{\alpha\in\mathcal P_v}(p_w-c_w(\alpha))\).

Sum the baseline \(1+\sum_w(p_w-c_w(\alpha))(p_w-c_w(\beta))\) over every ordered pair \(\alpha,\beta\in\mathcal P_v\), for every \(v\). The total is \(Q+\sum_{v,w}A_{vw}^2\). For each diagonal pair \(\alpha=\beta\), add the missing \(\sum_w c_w(\alpha)^2\). For each off-diagonal pair, add \(L(\alpha,\beta)\). The total diagonal correction is
\[
D=\sum_{\alpha\in\mathcal P}|\alpha|+\sum_{v,w}p_vm_{vw}^2,
\]
because a proper prefix of \(\alpha\) contributes \(1\) at each of the \(|\alpha|\) vertices preceding the terminal vertex, and the remaining terms count extensions of \(\alpha\), including \(\alpha\) itself. The total off-diagonal common-prefix correction is
\[
H=\sum_{v,w}p_v(m_{vw}^2-m_{vw}):
\]
for each prefix ending at \(v\), there are \(m_{vw}(m_{vw}-1)\) ordered distinct extensions ending at \(w\). Finally,
\[
\sum_{\alpha\in\mathcal P}|\alpha|=\sum_{v,w}p_vm_{vw}-\sum_vp_v,
\]
since a path of length \(\ell\) has precisely \(\ell+1\) prefix–suffix decompositions. Therefore \(D+H=2\sum_{v,w}p_vm_{vw}^2-\sum_vp_v\). Including the \(|G(E)|=1+Q\) commuting partners of zero gives exactly the displayed formula for \(K(E)\).

## Verification

The standalone standard-library Python program `verify.py` constructs the actual path-pair semigroup, directly multiplies all pairs, checks the centralizer of every element, and separately evaluates the vertex-matrix formula. The recorded run passed all \(1099\) forward-oriented simple acyclic graphs with one through five vertices, all \(681\) tested acyclic multigraphs on two through four vertices with edge multiplicities at most two and no more than eight edges, and four explicit regression examples. Sample values \((|G(E)|,K(E))\): one directed edge \((6,22)\); directed three-vertex chain \((15,125)\); four-vertex diamond \((35,817)\); two parallel edges on two vertices \((11,71)\).

These finite tests corroborate, but do not substitute for, the proof for arbitrary finite acyclic multigraphs. The path-count matrix can be built by topological dynamic programming; evaluating the displayed aggregate formula requires only polynomially many integer operations in \(|V|\), rather than enumerating the potentially exponentially many paths and quadratically more ordered element pairs.

## Relationship to prior work

Jones–Lawson [1, p. 9] and Mesyan–Mitchell [3, §2.3] supply the path-pair normal form and prefix-product formalism. Araújo–Bentz–Konieczny [2, Proposition 2.2] give a commutation criterion in the full symmetric inverse semigroup, rather than a centralizer or ordered-pair count for graph inverse subsemigroups. Bardyla [4, Theorem 11] identifies a vertex-indexed Green class with zero as a Brandt matrix-unit semigroup and describes some cross-class products: incomparable classes multiply to zero, and products of comparable classes lie in the lower class. This does not count equality of the two product orders within that lower class, or give the complete centralizer and ordered-pair formulas above. The zero path semigroup under concatenation-or-zero has different nonzero elements and products from the graph inverse semigroup, even on the same directed graph.

## Limitations

The theorem concerns finite acyclic directed graphs. Directed cycles can create nonzero elements with nonzero square and invalidate the non-idempotent centralizer argument. The formula counts ordered pairs and includes zero; it is not a formula for commuting tuples of arbitrary length or for the cardinality of the center. No claim of exhaustive historical novelty is made.

## References

1. D. G. Jones and M. V. Lawson, *Graph inverse semigroups: their characterization and completion*, arXiv:1106.3644, first submitted 2011-06-18; https://arxiv.org/abs/1106.3644.
2. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664, first submitted 2012-05-08; https://arxiv.org/abs/1205.1664.
3. Z. Mesyan and J. D. Mitchell, *The Structure of a Graph Inverse Semigroup*, arXiv:1409.4380, first submitted 2014-09-15; https://arxiv.org/abs/1409.4380.
4. S. Bardyla, *An alternative look at the structure of graph inverse semigroups*, arXiv:1806.09671 (2018), *Matematychni Studii* 51 (2019), 3–11; https://arxiv.org/abs/1806.09671.
