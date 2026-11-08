# Leaf augmentation stochastically improves random-greedy matching, with an exact decorated-path law

## Finding

**Theorem (augmentation, finite law, and boundary asymptotic).** Let \(H\) be any finite simple graph on \(n\ge1\) vertices, and let \(H^{(q)}\) be obtained by attaching \(q\ge1\) private leaves to each vertex of \(H\). Put independent uniform continuous priorities on the edges and greedily accept an edge exactly when neither endpoint has yet been matched. Let \(M_q(H)\) denote the number of accepted edges. For any integers \(q'>q\ge1\),
\[
M_q(H)\le_{\mathrm{st}}M_{q'}(H).
\]
Moreover, if \(H\) has an edge, this dominance is strict (the two laws are unequal). It holds even under a coupling that retains all priorities on shared edges and adds independent priorities only for new leaf edges.

For the core path \(P_n\), let \(f_{n,q}(z)=\mathbb E[z^{M_q(P_n)}]\), with \(f_{0,q}(z)=1\). Then, for \(n\ge1\),
\[
\big((q+1)n-1\big)f_{n,q}(z)=z\left(q\sum_{i=0}^{n-1}f_{i,q}(z)f_{n-1-i,q}(z)+\sum_{i=0}^{n-2}f_{i,q}(z)f_{n-2-i,q}(z)\right).
\]
(The second sum is empty for \(n=1\).) Equivalently, the formal generating function \(F_q(u,z)=\sum_{n\ge0}f_{n,q}(z)u^n\) is the unique solution with constant term \(1\) of
\[
(q+1)u\partial_u F_q=F_q-1+z(qu+u^2)F_q^2.
\]
Its exact support for every \(n\ge1\) is \(\{\lceil n/2\rceil,\ldots,n\}\), with positive mass at each integer.

For each fixed integer \(q\ge1\), define
\[
\alpha_q=1-\frac{1}{q+1}\int_0^1t^{q/(q+1)}\exp\!\left(-\frac{2(1-t)}{q+1}\right)\,dt.
\]
Then for every fixed real \(R>1\),
\[
\mathbb E M_q(P_n)=\alpha_q n+\left(\frac{q+2}{q+1}\alpha_q-1\right)+O_{q,R}(R^{-n}).
\]
The constant term is exact, and the error is supergeometric in the sense of this quantified \(R\)-dependent statement. The density \(\alpha_1\approx0.769039753456\) coincides with a classical greedy-matching constant; it is not claimed as a new constant.

## Assumptions and scope

All graphs are finite, simple, undirected; isolated core vertices are allowed. Every original vertex has at least one pendant neighbor. Edge priorities are mutually independent with any common continuous distribution, so there are no ties and the induced edge order is uniform. The process accepts an edge if both endpoints are currently unmatched and never rematches either. The statement compares integer numbers of accepted *edges* (not the covered-vertex count). The stochastic order means that every upper-tail probability of the later size is no smaller.

The theorem's general coupling concerns graphs formed by adding pendant edges, without changing shared edge priorities. The exact recurrence, generating function, support, and sharp mean asymptotic require the core to be a simple path; \(P_1\) is allowed. The assertion is not about vertex-order greedy independent sets or a time-continuous process that accepts previously blocked edges.

## Proof

**1. Every original vertex is matched and the accounting identity.** At termination any unmatched original vertex would have at least one adjacent unmatched private leaf, yielding a feasible edge, a contradiction. If \(B_q(H)\) is the number of selected original-to-original edges, exactly \(2B_q(H)\) originals are covered by those edges, and the other \(n-2B_q(H)\) originals each use exactly one selected pendant edge. Therefore
\[
M_q(H)=B_q(H)+\big(n-2B_q(H)\big)=n-B_q(H).
\]

**2. Inserting one pendant edge cannot increase the number of original-original selected edges.** Couple old and enlarged edge orders by independent priorities on their union and delete the new edge to obtain the old order. Up to the new edge, the two matchings agree. If the new edge is rejected, they continue identically. If accepted, the only difference among *old* vertices is that its original endpoint is matched in the enlarged process and unmatched in the old process. Scan subsequent common edges. An edge whose two endpoints have equal status in both processes has the same accept/reject decision. At a first differing decision, the one distinguished unmatched vertex is paired with an endpoint free in both processes; the edge is selected in exactly one process, and the distinguished status moves to its other endpoint, with the direction (old-only versus new-only selection) alternating at each such move. If that endpoint is a leaf, no subsequent difference can occur: it has no other common incident edge. Consequently, the difference between the old and enlarged counts of selected original-original edges alternates between \(0\) and \(1\), and never becomes negative. By the accounting identity, insertion of one private edge cannot decrease the total matching size. Insert the \(q'-q\) leaves one at a time at each core vertex to obtain the claimed coupling.

If the core contains an edge \(uv\), a positive-probability priority event has that original edge first among the old edges, the newly inserted pendant edge at \(u\) earlier than \(uv\), and all remaining old pendant edges earlier than all other original edges. In the old run \(uv\) is selected, whereas in the enlarged run it is rejected and all original vertices are covered by pendants; hence the total matching sizes differ. This gives strict stochastic-order inequality in the sense of unequal laws; repeated insertions preserve the inequality.

**3. First-priority decomposition on the path.** The decorated path has \((q+1)n-1\) edges. If the first edge is one of the \(q\) private edges at path position \(j\), the position and its private leaves can be removed and two independent decorated subpaths of sizes \(j-1\) and \(n-j\) remain. If the first edge joins positions \(j\) and \(j+1\), those two positions are removed and the remaining subpaths have sizes \(j-1\) and \(n-j-1\). Private leaves of removed vertices become isolated and contribute no matching edges. Conditional on the first edge, the relative edge orders in the disjoint subpaths remain independent uniform orders. Each branch contributes one accepted edge. Averaging proves the recurrence. Multiplying by \(u^n\) and summing gives the displayed differential equation. Its coefficient of \(u^n\) has the positive multiplier \((q+1)n-1\), so it determines the solution uniquely.

Every selected original edge consumes two original vertices and there can be at most \(\lfloor n/2\rfloor\) such edges, while the accounting identity gives the total matching size. Conversely, for every integer \(0\le j\le\lfloor n/2\rfloor\), choose a size-\(j\) matching of original path edges, put those edges first, then put all original pendant edges ahead of all remaining original edges. This positive-probability priority event produces exactly \(j\) selected original edges. Hence every stated size occurs and no other size can occur.

**4. The exact mean and supergeometric remainder.** Let \(\mathcal M_q(u)=\partial_z F_q(u,z)|_{z=1}\). The recurrence gives \(F_q(u,1)=(1-u)^{-1}\); differentiation yields
\[
(q+1)u\mathcal M_q'(u)=\mathcal M_q(u)+\frac{qu+u^2}{(1-u)^2}+\frac{2(qu+u^2)}{1-u}\mathcal M_q(u).
\]
Set \(A_q(u)=(1-u)^2\mathcal M_q(u)\). The equation simplifies exactly to
\[
(q+1)uA_q'(u)=(1-2u)A_q(u)+qu+u^2,\qquad A_q(0)=0.
\]
Solving by an integrating factor gives the entire function
\[
A_q(u)=\frac{u}{q+1}\int_0^1(q+ut)t^{-1/(q+1)}\exp\!\left(-\frac{2u(1-t)}{q+1}\right)\,dt.
\]
Indeed, for \(q\ge1\) the endpoint exponent is integrable; on each compact complex \(u\)-set the integrand and its derivatives are uniformly integrable, proving entirety. Integrating by parts establishes \(A_q(1)=\alpha_q\) as given above. Substitution \(u=1\) into the differential equation gives \(A_q'(1)=1-\alpha_q/(q+1)\).

Write the Taylor expansion at \(u=1\) as \(A_q(u)=\alpha_q+A_q'(1)(u-1)+(u-1)^2B_q(u)\), with \(B_q\) entire. Thus
\[
\mathcal M_q(u)=\frac{\alpha_q}{(1-u)^2}-\frac{A_q'(1)}{1-u}+B_q(u).
\]
The coefficient of \(u^n\) is \(\alpha_q(n+1)-A_q'(1)+[u^n]B_q(u)\). For every \(R>1\), Cauchy's estimate on \(|u|=R\) bounds the last coefficient by \(\max_{|u|=R}|B_q(u)|R^{-n}\), yielding the stated expansion, including \(\alpha_q(q+2)/(q+1)-1\) as the boundary constant. The result does not assert one universal implied constant valid simultaneously for all \(R\).

## Verification

The included standalone `verify.py` uses only Python's standard library. Run `python verify.py`; the expected success marker is `VERIFY_OK 541040 exact and seeded checks`. It reconstructs small distributions directly from every edge order, compares them against the independently coded first-edge rational recurrence, verifies support and stochastic inequalities, exhaustively checks the insertion coupling on several tiny core graphs, uses a deterministic-seed sampling of larger cores, and compares coefficients of the differential identity. The proof above, rather than finite sampling, establishes all infinite-family statements. The remainder estimate follows from analytic entirety and Cauchy's bound rather than extrapolation of finite numeric values.

## Relationship to prior work

Random sequential adsorption and greedy matchings have a substantial literature. Penrose and Sudbury (2005) study deposition processes and blocking interactions on general graphs; their forward equations provide broad context, not a claim of a new priority algorithm here. Dyer and Frieze (1991) identify the matching performance constant approximately \(0.7690\) in a forest setting, so the coincident \(q=1\) bulk density is explicitly not claimed as new. Krapivsky (2020) investigates one-dimensional RSA large deviations with a different blocked-site deposition model. Bonnier (1992) treats mixtures of one-dimensional adsorption particles and potentially covers bulk mixtures under equivalent parameterizations; only the abstract could be accessed for this comparison.

The evaluated contribution is the graph-uniform **pathwise stochastic monotonicity under private-leaf insertion**, together with the **complete finite decorated-path matching-size law** and **all-\(R\) sharp boundary remainder**. A general adsorption formalism can imply first-step equations; novelty is not based on renaming that formalism alone. Relevant earlier coverage remains a historical-priority risk as documented in the review.

## Limitations

The exact generating function and entire correction are proved for homogeneous decorated paths, not arbitrary core graphs. The general coupling covers *additional private edges*, not changes to core-edge weights or arbitrary graph edits. The displayed mean is not a variance or large-deviation theorem. Only a self-review and finite checker replay have been conducted; no independent audit. One potentially relevant 1992 paper's full text was inaccessible, so the priority assessment remains qualified.

## References

- M. Dyer and A. Frieze, *Randomized Greedy Matching* (1991), https://doi.org/10.1002/rsa.3240020104.
- M. Bonnier, *Kinetics of Random Sequential Adsorption of Mixtures* (1992), https://doi.org/10.1209/0295-5075/18/4/003.
- M. D. Penrose and A. Sudbury, *Exact and Approximate Results for Deposition and Annihilation Processes on Graphs* (2005), https://arxiv.org/abs/math/0503519.
- P. L. Krapivsky, *Large Deviations in One-Dimensional Random Sequential Adsorption* (2020), https://arxiv.org/abs/2009.08609, first posted 2020-09-18.
