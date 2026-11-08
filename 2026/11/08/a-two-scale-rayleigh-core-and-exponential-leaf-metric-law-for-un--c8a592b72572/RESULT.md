# A two-scale Rayleigh-core and exponential-leaf metric law for unbalanced bipartite first-passage percolation

## Finding
Fix an integer \(a\ge2\). Assign independent unit-rate exponential lengths to all edges of the complete bipartite graph \(K_{a,b}\), with fixed vertex class \(A=\{1,\ldots,a\}\) and growing class \(B_b\). Distances are minimum sums of edge lengths. Put
\[
M_{ij}^{(b)}=\min_{w\in B_b}(X_{iw}+X_{jw}),\qquad i,j\in A,\ i<j.
\]
**Two-scale joint limit.** The random vector \((\sqrt b M_{ij}^{(b)})_{i<j}\) converges to independent Rayleigh variables \((R_{ij})_{i<j}\) of scale one, with \(\Pr(R_{ij}>t)=e^{-t^2/2}\). If \(d_R\) is the shortest-path metric on the complete graph with these independently weighted edges, then
\[
(\sqrt b\,d_b(i,j))_{i<j\in A}\ \Longrightarrow\ (d_R(i,j))_{i<j\in A}.
\]
For any fixed \(s\ge0\) and any \(s\) distinct labelled peripheral vertices \(z_1,\ldots,z_s\), this convergence holds jointly with
\[
\bigl(d_b(z_\ell,i),d_b(z_\ell,z_h)\bigr)_{\ell,i,\ell<h}
\ \Longrightarrow\
\bigl(W_\ell,W_\ell+W_h\bigr)_{\ell,i,\ell<h},
\]
where \(W_1,\ldots,W_s\) are mutually independent \(\operatorname{Exp}(a)\) variables, **independent of all the limiting Rayleigh core weights**. In the peripheral limit the entire core contracts to a single hub and the marked leaves form an exponential-edge star, while its vanishing internal geometry retains a nontrivial Rayleigh metric after magnification.

## Assumptions and scope
All graphs are finite, simple, undirected, and edge weights are independent \(\operatorname{Exp}(1)\). The fixed integer \(a\ge2\), the number of labelled peripheral vertices \(s\ge0\), and any finite thresholds are held fixed as the integer \(b\to\infty\), with \(b\ge\max\{1,s\}\). The limiting variables \(R_{ij}\) are independent, not the core distances \(d_R(i,j)\), which can be correlated and are shortened by multihop routes. Paths may traverse an arbitrary number of alternating bipartite edges. There is no assertion uniform in growing \(a\) or in the full peripheral vertex set.

## Proof
**1. Exact finite metric reduction.** Every walk with endpoints in \(A\) alternates through \(B_b\), so its consecutive two-edge segments \(i-w-j\) cost at least \(M_{ij}^{(b)}\). Hence the original shortest-path distance is at least the shortest-path closure of the complete graph on \(A\) with pair costs \(M_{ij}^{(b)}\). Conversely each abstract edge \(ij\) can be realised by a two-edge bipartite walk through a minimising \(w\); concatenating these walks gives a bipartite walk with the abstract total cost. Removing loops cannot increase a nonnegative-weight walk's cost. This establishes equality without an approximation.

**2. Independent Rayleigh pair minima.** Fix nonnegative real thresholds \(t_{ij}\). For one peripheral vertex \(w\), the probability that a given pair satisfies \(X_{iw}+X_{jw}\le t_{ij}/\sqrt b\) equals
\[
1-e^{-t_{ij}/\sqrt b}(1+t_{ij}/\sqrt b)
=\frac{t_{ij}^2}{2b}+O(b^{-3/2}).
\]
Two different pair events at the same \(w\) require at least three distinct spoke weights, each at most \(T/\sqrt b\) for \(T=\max_{i<j}t_{ij}\), so their intersection has probability \(O(b^{-3/2})\); disjoint pairs have the even smaller order \(O(b^{-2})\). As \(a\) is fixed, inclusion-exclusion yields the probability of no such small two-edge pair at one \(w\):
\[
1-\frac{1}{2b}\sum_{i<j}t_{ij}^2+O(b^{-3/2}).
\]
The \(b\) sets of spoke weights are independent. Therefore
\[
\Pr\bigl(\sqrt b\,M_{ij}^{(b)}>t_{ij}\ \forall i<j\bigr)
=\left(1-\frac{\sum t_{ij}^2}{2b}+O(b^{-3/2})\right)^b
\longrightarrow\prod_{i<j}e^{-t_{ij}^2/2}.
\]
The upper-orthant limits determine joint weak convergence to independent continuous Rayleigh variables. Shortest-path closure on finitely many vertices is a continuous function of the edge weights (each coordinate is the minimum of finitely many simple-path sums); the continuous-mapping theorem proves the magnified core metric limit. In particular, its diameter is \(O_{\Pr}(b^{-1/2})\).

**3. Peripheral star bounds.** Let \(W_\ell=\min_{i\in A}X_{i z_\ell}\). For distinct tags these are independent \(\operatorname{Exp}(a)\) variables for every \(b\). Let \(\Delta_b=\max_{i,j\in A}d_b(i,j)\). Positivity, the definition of \(W_\ell\), and concatenation through the two minimising core vertices give the deterministic inequalities
\[
W_\ell\le d_b(z_\ell,i)\le W_\ell+\Delta_b,\qquad
W_\ell+W_h\le d_b(z_\ell,z_h)\le W_\ell+W_h+\Delta_b \quad(\ell\ne h).
\]
Since \(\Delta_b\to0\) in probability, all tagged distances have the claimed star approximation jointly.

**4. Independence at different scales.** Remove the \(s\) marked peripheral vertices and construct \(\widetilde M_{ij}^{(b)}\) using the remaining \(b-s\) vertices. The deleted-free pair-minimum array is independent of all tagged spoke weights, and \(\sqrt b\,\widetilde M^{(b)}\) has the same joint Rayleigh limit by step 2 (since \((b-s)/b\to1\)). For a fixed \(L\), the probability that some tagged vertex creates a two-edge pair path of cost at most \(L/\sqrt b\) is at most
\[
s\binom a2\left(1-e^{-L/\sqrt b}(1+L/\sqrt b)\right)=O(b^{-1}).
\]
By tightness, choose \(L\) so that all the untagged pair minima are at most \(L/\sqrt b\) with probability arbitrarily close to one for large \(b\). On this event, except for the preceding \(O(b^{-1})\) probability, tagged vertices cannot change any pair minimum. Thus the full scaled core array equals an independent-of-tags array with probability tending to one. Together with the deterministic star bounds this proves full joint convergence and independence.

## Verification
Run `python verify.py` using Python 3's standard library. The checker uses a fixed seed and positive integral edge weights to compare all-pairs distances on the bipartite graph against its two-step reduced metric closure for hundreds of small instances; it separately checks both deterministic peripheral inequalities and the exact two-hub gamma-minimum tail at multiple finite sizes. The finite tests exercise identities, not the proof of the infinite probability limit. The checker reports its own assertion count; the analytic proof above handles all integers \(a\ge2\) and \(b\ge1\) in the finite identity, and all fixed \(a,s\) in the limit.

## Relationship to prior work
Mountford and Saliba [1] study first-passage percolation on **random configuration-model graphs** with bounded degree-moment assumptions and asymptotics of flooding time and graph diameter, not the full marked metric geometry of a deterministic highly unbalanced complete bipartite graph. Their Section 2 Condition 1 requires minimum degree at least three and bounded \((2+\delta)\)-degree moments; the growing hubs of \(K_{a,b}\) violate the moment assumption and the result is neither a model reduction nor an implication. Gerke, Mezei and Sorkin [2], especially Theorems 1.1–1.2 and Section 2.2, study successive shortest paths and flow costs on the **complete graph** with random edge lengths. Janson [3] studies the shortest-path metric on the complete graph. None of these theorems gives the fixed-hub, growing-periphery bipartite two-scale metric law: their host graphs, statistics and/or regimes differ. Ross [4] reports a general exact joint shortest-path distribution for exponential network edges, but the accessible abstract alone does not permit a whole-document exclusion; its exact finite formulas do not state the present asymptotic joint independent-Rayleigh and exponential-star law. The finite closure identity is elementary, but it does not by itself imply either asymptotic independence assertion.

## Limitations
The limit is finite-dimensional for a fixed number of marked peripheral vertices, not convergence of a metric on every peripheral vertex. The claim does not cover growing \(a\), non-exponential spokes, dependent lengths, or convergence rates for the joint law. The core distances are a metric closure of independent Rayleigh *edge costs*, not independent Rayleigh distances for \(a\ge3\). The full text of Ross [4] was not available for direct scientific comparison; its general exact distribution is a residual historical priority risk. No external mathematical audit has been performed.

## References
[1] T. Mountford and J. Saliba, *Flooding and Diameter in General Weighted Random Graphs*, arXiv:1909.04563 (first public 2019-09-10), *Journal of Applied Probability* 57 (2020), 956–980. Primary MSC 60C05. https://arxiv.org/abs/1909.04563 ; https://doi.org/10.1017/jpr.2020.45 .

[2] S. Gerke, B. F. Mezei and G. B. Sorkin, *Successive shortest paths in complete graphs with random edge weights*, arXiv:1911.01151 (first public 2019-11-04), *Random Structures & Algorithms* 57 (2020), 1205–1247. https://arxiv.org/html/1911.01151v2 ; https://doi.org/10.1002/rsa.20962 .

[3] S. Janson, *One, Two and Three Times log n/n for Paths in a Complete Graph with Random Weights*, *Combinatorics, Probability and Computing* 8 (1999), 347–361. https://doi.org/10.1017/S0963548399003892 .

[4] S. M. Ross, *Distribution of Minimal Path Lengths when Edge Lengths are Independent Heterogeneous Exponential Random Variables*, *Journal of Applied Probability* 49 (2012), 895–900. https://doi.org/10.1239/jap/1346955343 .
