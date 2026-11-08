# A parity-complete characterization of acyclic orientations of complete bipartite graphs

## Finding
Let \(m,n\geq 1\) be integers, let \(G=K_{m,n}\) be the finite simple complete bipartite graph with both parts labelled, and let \(T\subseteq V(G)\). Call an orientation **\(T\)-odd** if the indegree of a vertex is odd exactly at the vertices in \(T\).

**Theorem.** A \(T\)-odd acyclic orientation of \(K_{m,n}\) exists if and only if
\[
|T|\equiv mn\pmod 2\qquad\text{and}\qquad T\ne V(K_{m,n}).
\]
The proof gives a deterministic constructive algorithm using \(O((m+n)^2+mn)\) elementary operations. In particular, the exact number of **distinct feasible labelled indegree-parity signatures** (subsets \(T\), *not* orientations) is
\[
2^{m+n-1}-\mathbf 1_{\{m\equiv n\equiv0\ (\mathrm{mod}\ 2)\}}.
\]
Thus every parity-feasible target is realizable unless both part sizes are even and every vertex is prescribed odd. The stated exclusion is necessary because every acyclic digraph has a source.

## Assumptions and scope
An orientation assigns a direction to each of the \(mn\) edges; directed cycles are prohibited. The part sizes are positive, vertices are distinguished, and indegree is counted in the full orientation. The theorem is a **feasibility classification**; it does not count the number of orientations realizing an individual feasible signature. There are no assumptions of regularity or balance.

For the proof, write the two parts as \(A,B\), with \(|A|=m\) and \(|B|=n\). Let \(p(v)=1\) for \(v\in T\) and \(p(v)=0\) otherwise. A possible source is a vertex with \(p(v)=0\). A possible sink is a vertex for which \(p(v)\equiv\deg_G(v)\pmod2\).

## Proof
**Necessity.** In every orientation, the sum of indegrees equals the number \(mn\) of edges, so \(|T|\equiv mn\pmod2\). A nonempty finite acyclic digraph has a source with indegree zero. Therefore \(T\) cannot contain every vertex.

**Possible sink.** Suppose the two necessary conditions hold. Let \(a\) be the number of vertices of \(A\) with prescribed parity zero and \(b\) the corresponding number in \(B\). Let \(q\) count possible sinks. Since vertices in \(A\) have degree \(n\) and vertices in \(B\) degree \(m\),
\[
q=\begin{cases}a,&n\text{ even},\\m-a,&n\text{ odd}\end{cases}
+\begin{cases}b,&m\text{ even},\\n-b,&m\text{ odd}.\end{cases}
\]
If \(q=0\), then every vertex in \(A\) has prescribed parity \(1-(n\bmod2)\), and every vertex in \(B\) has prescribed parity \(1-(m\bmod2)\). Thus \(|T|\equiv m+n\pmod2\). Together with \(|T|\equiv mn\pmod2\), this forces both \(m\) and \(n\) to be even (check the four parity pairs). But then every vertex has prescribed parity one, contradicting \(T\ne V(G)\). Consequently \(q\ge1\).

**Safe-source lemma.** Assume \(m,n\ge2\), the parity condition, at least one possible source, and \(q\ge1\). There exists a possible source \(v\) such that, after orienting all its incident edges away from \(v\), deleting \(v\), and toggling the prescribed parity of every former neighbor of \(v\), the remaining complete bipartite graph still has both a possible source and a possible sink.

To prove the lemma, deleting an \(A\)-source leaves \(a-1+(n-b)\) possible sources; deleting a \(B\)-source leaves \(b-1+(m-a)\). Any unaffected vertex retains its possible-sink status: vertices not adjacent to the deleted source retain both their degree and target parity, whereas neighbors have both their degree and target parity changed by one. Therefore the new number of possible sinks is \(q-1\) if the deleted source has even degree, and \(q\) if its degree is odd.

First suppose \(q\ge2\). If \(a>0\) and \(a-1+n-b>0\), delete any \(A\)-source. If \(a>0\) but that inequality fails, then \(a=1\) and \(b=n\ge2\), so a \(B\)-source can be deleted while leaving at least \(b-1\ge1\) sources. If \(a=0\), then \(b>0\) and deleting a \(B\)-source leaves \(b-1+m\ge1\) sources. Every such choice retains at least one possible sink because \(q\ge2\).

Now suppose \(q=1\). If both \(m,n\) are even, then \(q=a+b=1\), making \(|T|=m+n-1\) odd, contrary to \(|T|\equiv mn\pmod2\). If both are odd, deleting any possible source preserves the unique possible sink, so use the previous argument to retain a possible source. If \(m\) is even and \(n\) is odd, then \(q=(m-a)+b=1\), hence \(a\ge m-1\ge1\). Delete an \(A\)-source, whose degree is odd, preserving \(q\). The remaining source count \(a-1+n-b\) is positive: when \(a=m\), \(a-1\ge1\); otherwise \(a=m-1\) and \(b=0\), so \(n-b\ge2\). The case \(m\) odd and \(n\) even is symmetric. This proves the lemma.

**Induction.** If one part has size one, the graph is a star. For each leaf, orient its sole edge toward the leaf exactly when that leaf has prescribed parity one. The indegree parity at the center then equals its prescription by the global parity equation. This constructs the required acyclic orientation, including the case \(m=n=1\).

For \(m,n\ge2\), apply the safe-source lemma and remove the selected source. The reduced graph has positive part sizes and remains complete bipartite. The parity equation is preserved: if a source of degree \(d\) is removed, the edge count decreases by \(d\), while the number of prescribed ones changes by \(d\) modulo two because its former neighbors are toggled. The reduced instance has a possible source and sink, so it satisfies the original two conditions (and is eligible for induction). Solve the reduced instance recursively and restore the chosen vertex with all its edges directed outward. Its indegree is zero, each neighbor's prescribed parity is restored, and no directed cycle can include the restored source. Induction establishes sufficiency for all positive \(m,n\).

**Counting signatures and complexity.** Exactly half the \(2^{m+n}\) subsets obey the parity equation. The all-vertex subset obeys this equation exactly when \(m,n\) are both even; it is then the sole forbidden signature. At most \(m+n-2\) safe-source deletions occur before a star remains. Recomputing the four target-parity counts and scanning possible sources costs at most \(O(m+n)\) per deletion, with \(mn\) edges in the output. Hence the stated running-time bound.

## Verification
The standalone `artifacts/verify.py` reconstructs independent directed-edge assignments and tests acyclicity by topological elimination. It checks **every** edge orientation and every prescribed parity vector for each of the 16 part-size pairs \(1\le m,n\le4\), including the even-even exceptional signatures. Separately, it executes the constructive safe-source algorithm on 4,032 parity-count profiles covering all pairs \(1\le m,n\le12\), verifying acyclicity and every prescribed parity by reconstructing all oriented edges. All checks finish with `VERIFY_OK`. These finite computations are corroboration; the proof above is unrestricted.

## Relationship to prior work
Gravier, Petiteau, and Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem* (arXiv:2603.09475v1, publicly submitted 2026-03-10), formulate the prescribed indegree-parity question and study when global parity, source, and sink restrictions suffice. Their publicly indexed abstract identifies Cartesian products of paths and cycles, as well as cliques, as the graph classes studied in detail. The present theorem treats the complete bipartite family for arbitrary target subsets and shows that the sink restriction follows from global parity and the source restriction in that family.

West, *Acyclic orientations of complete bipartite graphs* (Discrete Mathematics 138 (1995), 393–396, DOI:10.1016/0012-365X(94)00222-5), gives an exhaustive alternating-block representation of acyclic orientations and classifies attainable **numbers of independent edges** (edges whose reversal preserves acyclicity). These results concern a different statistic; in particular, they do not state the above image of the indegree-parity map. The complete-block representation is compatible with, but does not on its own state, the new reachability classification.

Das, Ghosh, Ghosh, and Sen, *Oriented bipartite graphs and the Goldbach graph* (Discrete Mathematics 344 (2021), 112497, DOI:10.1016/j.disc.2021.112497), characterize acyclic bitournaments structurally; the parity-feasibility theorem is a separate arithmetic restriction on that class. Searches also considered the earlier 2025 complexity paper of Gravier, Petiteau, and Sivignon (arXiv:2504.20935).

## Limitations
The claim is limited to complete bipartite graphs with both parts nonempty; it does not assert the same necessary-and-sufficient conditions for arbitrary bipartite graphs, Cartesian grids, or partially oriented graphs. It counts feasible **parity assignments**, not acyclic orientations. Historical priority is provisional: the 2026 source's abstract and available initial material were inspected, but its full text could not be retrieved in this execution, so a hidden equivalent special case remains a residual literature risk. No independent mathematical audit has been performed.

## References
1. S. Gravier, M. Petiteau, I. Sivignon, *Some polynomial classes for the acyclic orientation with parity constraint problem*, arXiv:2603.09475v1 (2026-03-10). https://arxiv.org/abs/2603.09475
2. D. B. West, *Acyclic orientations of complete bipartite graphs*, Discrete Mathematics **138** (1995), 393–396. https://dwest.web.illinois.edu/pubs/aobip.pdf
3. S. Das, P. Ghosh, S. Ghosh, S. Sen, *Oriented bipartite graphs and the Goldbach graph*, Discrete Mathematics **344** (2021), Article 112497. DOI:10.1016/j.disc.2021.112497.
4. S. Gravier, M. Petiteau, I. Sivignon, *Note about the complexity of the acyclic orientation with parity constraint problem*, arXiv:2504.20935 (2025-04-29). https://arxiv.org/abs/2504.20935
