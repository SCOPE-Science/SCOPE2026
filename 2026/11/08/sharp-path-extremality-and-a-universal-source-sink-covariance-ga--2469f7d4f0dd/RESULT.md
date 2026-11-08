# Sharp path extremality and a universal source–sink covariance gap for randomly oriented trees

## Finding
Let \(T\) be any finite simple tree of order \(n\ge3\). Independently orient each edge in either direction with probability \(1/2\), and let \(S_T\) and \(K_T\) be the numbers of sources (indegree zero) and sinks (outdegree zero), respectively. Write
\[
C(T)=\operatorname{Cov}(S_T,K_T).
\]
Then the path \(P_n\) uniquely maximizes this covariance among all trees on \(n\) vertices, with
\[
C(P_n)=\frac{n-4}{16}.
\]
Moreover, the following stability bound is **sharp and independent of** \(n\): every nonpath tree of order \(n\ge4\) satisfies
\[
\boxed{C(T)\le\frac{n-4}{16}-\frac{13}{64}.}
\]
Equality holds **if and only if** \(T\) has one vertex of degree three, all other nonleaves have degree two, and its three degree-three-neighbors have degree two. Equivalently, \(T\) is a three-arm spider whose three arms each have length at least two edges; this family exists precisely for \(n\ge7\). Thus for \(n\ge7\) it is the complete set of second-best trees. For \(4\le n\le6\) the inequality is strict. The exact degree formula behind the extremum is
\[
\boxed{C(T)=2\sum_{uv\in E(T)}2^{-d(u)-d(v)}-\sum_{v\in V(T)}4^{-d(v)}.}
\]

## Assumptions and scope
The underlying graph is a connected finite simple undirected tree with \(n\ge3\), not a random tree. Orientations of distinct edges are mutually independent and unbiased. Every orientation is acyclic because \(T\) has no undirected cycles. The terms source and sink refer to the in- and out-degrees in the resulting orientation; there are no isolated vertices in the stated range. All inequalities hold exactly over rational numbers for every such tree. This result makes no claim about biased, dependent or conditioned edge orientations, non-trees, or the variance of either marginal count separately. The result's primary classification is MSC2020 60C05 (combinatorial probability).

## Proof
**Step 1: Local covariance identity.** Let \(I_v\) indicate that \(v\) is a source and \(J_v\) that it is a sink. For every vertex \(v\),
\[
\Pr(I_v=1)=\Pr(J_v=1)=2^{-d(v)}.
\]
For \(u=v\), the two events are incompatible, so \(\operatorname{Cov}(I_v,J_v)=-4^{-d(v)}\). For distinct nonadjacent vertices \(u,v\), the events use disjoint sets of independent edge orientations and have covariance zero. For \(uv\in E(T)\), the events \(I_u=1\) and \(J_v=1\) consistently force their shared edge to point from \(u\) to \(v\), so their joint probability is \(2^{-(d(u)+d(v)-1)}\). Their covariance is therefore \(2^{-d(u)-d(v)}\). Summing over all ordered pairs yields the displayed degree formula, with each undirected edge appearing twice.

**Step 2: Positive energy and negative boundary terms.** Define \(a_v=2^{-d(v)}\). The identity \(2a_ua_v=a_u^2+a_v^2-(a_u-a_v)^2\) transforms Step 1 into
\[
C(T)=\sum_{v\in V(T)}(d(v)-1)4^{-d(v)}
      -\sum_{uv\in E(T)}(2^{-d(u)}-2^{-d(v)})^2.\tag{1}
\]
Let \(\ell\) denote the number of leaves. For every internal vertex, \((d-1)4^{-d}\le1/16\), with equality only at degree two. For a leaf edge \(uv\) with \(d(u)=1\), its other endpoint has degree at least two; hence \((2^{-d(u)}-2^{-d(v)})^2\ge1/16\). Leaf edges are distinct for \(n\ge3\). Therefore
\[
C(T)\le\frac{n-\ell}{16}-\frac\ell{16}=\frac{n-2\ell}{16}.\tag{2}
\]
A finite tree has exactly two leaves if and only if it is a path. For a path, each internal vertex has degree two, the only nonzero edge-energy terms are its two leaf edges, and (1) gives \(C(P_n)=(n-4)/16\). For \(\ell\ge4\), (2) gives
\[
C(P_n)-C(T)\ge\frac{\ell-2}{8}\ge\frac14>\frac{13}{64}.
\]

**Step 3: Sharp three-leaf case.** The handshake identity \(\ell=2+\sum_{v:d(v)\ge3}(d(v)-2)\) shows that \(\ell=3\) forces one degree-three vertex \(c\), with all other internal vertices of degree two. The first sum in (1) is then \((n-4)/16+1/32\). Each of the three leaf edges costs at least \(1/16=4/64\) in the second sum. In addition, each of the three edges incident with \(c\) incurs at least \(1/64\) beyond those leaf-edge baseline costs: if its other endpoint has degree two then the edge is not a leaf edge and costs exactly \((1/4-1/8)^2=1/64\); if its other endpoint is a leaf then the edge costs \((1/2-1/8)^2=9/64\), an excess \(5/64\) over its leaf-edge baseline. All remaining edge terms are nonnegative. Thus the second sum in (1) is at least \(3/16+3/64\), proving
\[
C(T)\le\frac{n-4}{16}+\frac1{32}-\frac3{16}-\frac3{64}
=\frac{n-4}{16}-\frac{13}{64}.
\]
Equality requires all three neighbors of \(c\) to have degree two; then all leaf edges also have a degree-two endpoint and all remaining edges join degree-two vertices, so equality indeed holds. This is precisely the family of three-arm spiders with every arm length at least two. The smallest member has seven vertices. Since every nonpath tree has at least three leaves, this completes the uniqueness and sharp stability statements.

## Verification
The included standalone Python 3 script `verify.py` uses only the standard library and computes exact rational values. It enumerates all labelled trees via Prüfer codes for orders three through seven; at orders three through six it separately enumerates every possible edge orientation and checks that the direct source–sink covariance equals the degree formula. For orders three through seven it checks the sharp gap and the complete equality condition against every Prüfer-coded tree, and it constructs equality examples at every order from seven through fifty. Its recorded successful output is:

```text
VERIFY_OK 71605 exact assertions; all labelled trees n<=7, orientations n<=6
```

These finite checks are independent corroboration of the complete algebraic proof above, not an exhaustive check of unbounded order. The all-orders bound and equality characterization follow entirely from Steps 1–3.

## Relationship to prior work
Hwang, Jung, Lee, Oh and Yu (2019; arXiv:1910.10920), especially Sections 2–5, develop generating polynomials for sink sets of acyclic graph orientations, deletion–contraction, and graph-distinguishing consequences. The present question instead concerns *joint* source and sink counts on uniformly oriented trees, their mixed covariance, a sharp tree-shape maximum and an exact universal second-best gap; these are not stated by their univariate or multivariate sink-set results. Conte, Grossi, Marino and Rizzi (2018) investigate efficient enumeration of graph orientations with specified sources, rather than this probabilistic mixed moment or extremal stability. Older unique-sink counting results of Gebhard and Sagan do not provide the asserted bound. The local covariance identity uses elementary edge-independence; the claimed distinct contribution is the sharp all-tree extremal inequality and its exact equality family, not a new way to enumerate single-vertex sinks. Searching the relevant published statements, aliases and quantitative stability bounds did not uncover a theorem implying the \(13/64\) loss. This is a best-knowledge priority assessment, not a proof of absolute historical novelty.

## Limitations
The scope is unbiased independent orientations of fixed trees. The scalar covariance does not determine the joint distribution. The statement for \(n\ge7\) characterizes second-best covariance, not a total ordering of all tree shapes. No claim is made that available literature searches are exhaustive; an undiscovered equivalent result is possible. The calculations and proof have not received an independent external mathematical audit.

## References
1. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, first public arXiv version, 24 October 2019, https://arxiv.org/abs/1910.10920 .
2. A. Conte, R. Grossi, A. Marino and R. Rizzi, *Efficient enumeration of graph orientations with sources*, Discrete Applied Mathematics 246 (2018), 22–37, https://doi.org/10.1016/j.dam.2017.08.002 .
3. D. D. Gebhard and B. E. Sagan, *Sinks in acyclic orientations of graphs*, Journal of Combinatorial Theory, Series B 80 (2000), 130–146, https://arxiv.org/abs/math/9907078 .
