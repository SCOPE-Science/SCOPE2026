# Scientific review — two-hub 2-graph polytope outer sphere

## Correctness — PASS

The theorem is fully quantified for integer \(q\ge2\), in the exact standard-coordinate simplex-sum realization \(Q_{K_{2,q},2}\). Its vertex classification follows by assigning each connected singleton, edge or triple simplex to the largest entry of a strict ordering; every original vertex is attained, and each resulting point is exposed. The exact formula for its signed squared-distance gap is reduced to a polynomial with 41 positive monomials after setting \(u=s\), \(v=k-s\), \(w=q-k\), so the radius inequality and its equality cases hold in every dimension. The proposed center belongs to the convex hull of the contacts with explicit positive barycentric weights, proving global optimality and uniqueness. The embedded standard-library checker verifies the formal polynomial identity and separately enumerates all strict total orders for \(2\le q\le6\). The all-dimensional conclusion does not depend on the finite enumeration. Risk: arithmetic transcription errors are mitigated by the independent exact polynomial expansion and direct vertex enumeration but independent audit has not occurred.

## Originality — PASS (provisional historical priority)

Pešović and Stojadinović, arXiv:2209.12053v1 (2022-09-24), Definition 2.1 and Sections 3–4, were materially inspected: their construction, fan and enumerator results neither state nor imply the Euclidean minimum enclosing sphere, its barycentric contact certificate or the two exact orbit counts for \(K_{2,q}\) at \(m=2\). Indexed related results for complete-bipartite graphical zonotopes are about \(m=1\), and those for star interpolation consider \(K_{1,q}\) and inscribed balls; the indexed path 2-graph result concerns Gaussian-exposed vertex inertia for a path, not worst-case Euclidean radius for \(K_{2,q}\). Search comparisons were statement-level and no equivalent mathematical statement was identified in the compared sources. This does not prove global uniqueness of the result: related published records whose full texts could not be retrieved, plus unindexed work, are residual risks. No decisive broader coverage was identified.

## Mathematical value — PASS

This is the exact, natural Euclidean Chebyshev geometry of the first connected-triple stage of the published graph-polytope interpolation on a graph with two interchangeable hubs, not an arbitrary finite subproblem. It classifies the unique enclosing ball and every contact for all sizes; the contact set separates sharply into a factorial leaf-permutation orbit and precisely two hub-order points. The explicit full vertex count shows the share of contacts decreases like \(1/(2e q)\). The positive polynomial certificate is a structural, nontrivial global extremality result rather than a numerical census or a change of notation. The scope remains this precise canonical family, not general graph-associahedra or general weighted hypergraphs.

## Closest prior work and limitations

- M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, arXiv:2209.12053v1, https://arxiv.org/html/2209.12053v1 (full arXiv HTML Sections 2–4 inspected).
- *Inball-contact phase transitions inside the fixed star graph-associahedron fan*, public indexed research record dated 2026-10-18 (indexed summary only, full text unavailable): star, inball, unlike the present biclique outer ball.
- *Exact Gaussian-exposure inertia and a radial central limit law for path 2-graph polytopes*, public indexed research record dated 2026-11-17 (indexed summary only): path rather than biclique and a different metric statistic.
- *Complete multipartite graphical zonotopes have cubic-moment circumspheres*, public indexed research record dated 2026-10-11 (indexed summary only): the \(m=1\) family lacks the connected triples that determine the present realization.

The independent scientific audit is unperformed; the priority comparison does not include all possibly unpublished or unindexed mathematics. The theorem is restricted to unweighted \(m=2\) and \(K_{2,q}\), \(q\ge2\).

Self-review: passed. Independent audit: not yet performed.
