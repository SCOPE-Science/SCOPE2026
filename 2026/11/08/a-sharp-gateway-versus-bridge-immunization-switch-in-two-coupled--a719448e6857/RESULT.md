# A sharp gateway-versus-bridge immunization switch in two coupled communities

## Finding

Let \(G_m\) consist of two disjoint complete graphs \(K_m\), \(m\ge2\), with distinguished vertices \(a,b\) in different cliques and an additional degree-two gateway \(g\) adjacent exactly to \(a,b\). Before an independent-edge Reed–Frost outbreak, immunize (delete) exactly one vertex, seed one uniformly random surviving vertex, and let \(E_v(m,p)\) be the expected final number infected, when each remaining edge independently transmits with probability \(p\in[0,1]\).

There are three vaccine-location types: gateway \(g\), bridge endpoint \(a\) or \(b\), and an ordinary clique vertex. For all \(m\ge2\) and \(p>0\), vaccinating a bridge endpoint is strictly preferable to vaccinating any ordinary clique vertex. For every \(m\ge3\), a bridge endpoint is strictly better than the gateway for sufficiently small positive \(p\), whereas the gateway is strictly better near \(p=1\). These last statements assert existence of a switch, **not uniqueness**, for general \(m\).

The first nontrivial member \(m=3\), two triangles joined by a gateway (seven vertices), has an exact global classification. There is a unique \(p_*\in(0,1)\), approximately \(0.678963183759250\), satisfying

\[
2p_*^3-5p_*^2+p_*+1=0.
\]

For \(0<p<p_*\), exactly the two bridge endpoints minimize expected outbreak size. For \(p=p_*\), the two bridge endpoints and gateway tie. For \(p_*<p\le1\), only the gateway is optimal. Every ordinary clique vertex is strictly inferior throughout \(0<p\le1\). All strategies tie at \(p=0\). In contrast, \(m=2\) (the five-vertex path with a central gateway) always optimally vaccinates its gateway for \(p>0\); hence \(m=3\) is the first switch **within this equal-clique gateway family**, not among all graphs.

Writing \(E_G=E_g(3,p)\), \(E_B=E_a(3,p)\), the exact polynomial certificate is

\[
E_G=1+2p+2p^2-2p^3,\qquad
E_B=1+\frac{5p+5p^2-p^3-2p^4}{3},
\]
\[
\boxed{E_G-E_B=\frac p3(2p^3-5p^2+p+1).}
\]

## Assumptions and scope

The contact graph is finite, simple, undirected, and fixed. One vertex is removed perfectly before a single outbreak. All other vertices are equally likely to be the unique initially infected source. Edge transmission outcomes are independent Bernoulli variables of common parameter \(p\), sampled once for the entire event. A vertex is ultimately infected exactly if it belongs to the source's connected component of open edges in the retained graph. No false protection, recovery timing, repeated introduction, or heterogeneous transmission is included. All comparisons use **unconditional expected infected count among the \(2m\) surviving vertices**, not a conditional outbreak size or largest-component fraction.

For every integer \(r\ge1\), define \(q_r(p)\) as the probability that two fixed distinct vertices in independently edge-percolated \(K_r\) are connected, with \(q_1(p)=0\). The expectation for any retained graph on \(N\) vertices equals \(N^{-1}\sum_C |C|^2\), averaged over percolation, or equivalently \(1+(2/N)\sum_{\{x,y\}}\Pr(x\leftrightarrow y)\).

## Proof

**1. Reduction to two candidate types.** Under graph automorphisms, immunization locations fall into gateway, bridge-endpoint and ordinary-clique classes. Deleting a bridge endpoint leaves \(K_{m-1}\) isolated from the component consisting of the opposite \(K_m\) plus the gateway linked to its distinguished vertex. Deleting an ordinary vertex leaves an isomorphic graph *plus one edge* from the surviving distinguished vertex in its clique to the gateway. Using a coupling which shares all other independent bond outcomes, every cluster of the bridge-endpoint-deleted graph is a subset of a corresponding cluster after ordinary-vertex deletion. The extra edge increases mean cluster size with positive probability whenever \(p>0\): for \(0<p<1\), require the extra edge open and all other edges closed; for \(p=1\), the extra edge joins nonempty components. Thus ordinary-vertex deletion is strictly worse.

**2. Formula for arbitrary clique size.** Removing the gateway leaves two independent \(K_m\) components. Counting unordered connected vertex pairs gives

\[
E_G(m,p)=1+(m-1)q_m(p).
\]

Removing \(a\) leaves \(K_{m-1}\), \(K_m\), and the gateway linked by one retained edge to distinguished vertex \(b\). Pairs within each clique contribute \(\binom{m-1}{2}q_{m-1}(p)\) and \(\binom m2 q_m(p)\). Pairs from the gateway to \(b\) and the remaining opposite-clique vertices contribute \(p[1+(m-1)q_m(p)]\). There are \(2m\) surviving vertices, so

\[
E_B(m,p)=1+\frac{1}{m}\left[\binom{m-1}{2}q_{m-1}(p)
+\binom m2 q_m(p)+p\{1+(m-1)q_m(p)\}\right].
\]

For fixed \(m\), every distinct pair in \(K_m\) is directly connected with probability \(p\), and paths with two or more edges contribute \(O(p^2)\); hence \(q_m(p)=p+O(p^2)\) for \(m\ge2\). Subtracting yields

\[
E_G(m,p)-E_B(m,p)=\frac{m-2}{m}p+O(p^2).
\]

At \(p=1\), all clique edges open, giving \(E_G(m,1)=m\), \(E_B(m,1)=m+1/m\). Thus the difference is negative at one, and for \(m\ge3\) positive near zero, proving at least one crossover by continuity. No number or monotonicity of crossovers is claimed for larger \(m\).

**3. Exact smallest family member.** At \(m=2\), \(q_2=p\) and \(q_1=0\), which gives \(E_G(2,p)=1+p\) and \(E_B(2,p)=1+p+p^2/2\). The gateway strictly wins over the bridge endpoints for every \(p>0\), hence over all ordinary vertices by Step 1.

At \(m=3\), connectivity of a pair within a triangle arises from either its direct edge being open or both other edges being open while that edge is closed, so \(q_3=p+(1-p)p^2=p+p^2-p^3\). Inserting it into Step 2 yields the two polynomials and their factorized difference displayed above.

Set \(f(p)=2p^3-5p^2+p+1\). The increasing bijection \(p=t/(1+t)\) between \(p\in(0,1)\) and \(t\in(0,\infty)\) gives

\[
(1+t)^3 f\!\left(\frac{t}{1+t}\right)=1+4t-t^3.
\]

By Descartes' rule of signs, \(t^3-4t-1\) has **at most one positive root**; it has **at least one** because its value is negative at zero and tends to positive infinity. Consequently \(f\) has exactly one zero in \((0,1)\). Since \(f(0)=1\), \(f(1)=-1\), the difference is positive before this root and negative after it. Step 1 proves global optimality against all other vaccination vertices. The stated numerical root is enclosed by \(0.678963<p_*<0.678964\), with both polynomial signs checked exactly.

## Verification

Execute `python3 verify.py` using only the Python standard library. The checker independently enumerates all open/closed edge configurations after every possible single-vertex deletion in \(G_2\) and \(G_3\), computes the exact expected cluster size with rational arithmetic, constructs a polynomial in \(p\), and checks all orbit equalities, the explicit formulas, factorization and sign witnesses. It reports **32 exact identities/rational inequalities and 412 exhaustive percolation configurations**, all passing. The exhaustive enumeration is finite supporting evidence; the proof above, including its arbitrary-\(m\) statement, is analytical. The checker does not prove that earlier literature lacked the result.

## Relationship to prior work

Pastor-Satorras and Vespignani (2001 preprint; 2002 journal) analyze broad targeted network immunization, especially degree-based schemes for large scale-free networks [1]. Newman (2002) provides the independent-bond epidemic/percolation connection [2]. Masuda (2009), particularly Sections 2.2–2.3 and the conclusions, discusses bridge-conscious immunization of modular networks through a coarse-grained importance score and component-fragmentation objective [3]. Altarelli et al. (2013 preprint) develop a general approximate message-passing approach for vaccine allocation and expected infection [4]. Gupta, Singh and Cherifi (2014) compare community-based heuristics [5]; the accessible abstract was checked, but its full text was not re-inspected for the final comparison. The inspected full-text materials [1–4] motivate the question without stating the sharp seven-vertex exact polynomial and unique root under the defined one-seed, independent-bond objective. General algorithms for optimizing outbreaks do not by themselves assert the explicit unique-root characterization for this graph. Kenah and Robins [6] warn that generic continuous-time SIR epidemics need not have independent-edge percolation laws; this theorem avoids that model mismatch by assuming independent bonds from the outset.

## Limitations

The graph family is very special, symmetric and finite. The exact uniqueness assertion holds for \(m=3\) only; the arbitrary-\(m\) result establishes existence of at least one crossover, not uniqueness. This is not a claim of earliest possible switching among all seven-vertex or five-vertex graphs, or of novelty of degree-versus-bridge tradeoffs in general. Outbreak risk and immunization costs may change under multiple seeds, partial immunity, edge dependence, heterogeneous probabilities, variable infectious periods, or alternative risk objectives. Exhaustive checking is not historical priority certification. The ecological/epidemiological significance is mathematical, not an empirical recommendation.

## References

[1] R. Pastor-Satorras and A. Vespignani, *Immunization of complex networks*, arXiv:cond-mat/0107066 (first public 2001-07-03), https://arxiv.org/abs/cond-mat/0107066.

[2] M. E. J. Newman, *Spread of epidemic disease on networks*, arXiv:cond-mat/0205009 (2002), https://arxiv.org/abs/cond-mat/0205009.

[3] N. Masuda, *Immunization of networks with community structure*, arXiv:0909.1945 (2009), https://arxiv.org/abs/0909.1945.

[4] F. Altarelli et al., *Containing epidemic outbreaks by message-passing techniques*, arXiv:1309.2805 (2013), https://arxiv.org/abs/1309.2805.

[5] N. Gupta, A. Singh, and H. Cherifi, *Community-based Immunization Strategies for Epidemic Control*, arXiv:1411.6276 (2014), https://arxiv.org/abs/1411.6276.

[6] E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057 (2006), https://arxiv.org/abs/q-bio/0610057.
