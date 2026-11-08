# Reentrant source–two-step-path covariance in biased biclique orientations

## Finding

Let \(b\ge2\) be an integer, and independently orient each edge of the complete bipartite graph \(K_{2,b}\) from its two-vertex side \(A\) to its \(b\)-vertex side \(B\) with probability \(q\in(0,1)\), and in the reverse direction otherwise. Let \(S\) be the number of sources (vertices of indegree zero), and let \(P\) be the number of ordered directed paths of length exactly two with distinct vertices. A directed path is counted once for its ordered triple, not once for each pair of reachable endpoints. Define

\[
F_b(q)=q^{b-1}\bigl(1-(b+1)q\bigr)+(1-q)\bigl((2b-1)q-b\bigr).
\]

Then, for every such \(b,q\),

\[
\boxed{\operatorname{Cov}(S,P)=2bq(1-q)F_b(q).}
\]

For every \(2\le b\le5\), the covariance is strictly negative on the entire open interval \(0<q<1\). For every \(b\ge6\), there exist exactly two distinct simple roots \(q_-(b),q_+(b)\) of \(F_b\) in \((0,1)\), satisfying

\[
\frac12<q_-(b)<\frac58<q_+(b)<1.
\]

The covariance is strictly negative on \((0,q_-(b))\) and \((q_+(b),1)\), zero precisely at those two roots, and strictly positive on \((q_-(b),q_+(b))\). Thus \(K_{2,6}\) is the first graph in this biclique family exhibiting a negative–positive–negative dependence sequence under bias variation. In particular, for \(b=6\) and \(q=5/8\),

\[
F_6(5/8)=\frac{1641}{262144},\qquad
\operatorname{Cov}(S,P)=\frac{73845}{4194304}>0.
\]

## Assumptions and scope

The host graph is finite, simple, and exactly \(K_{2,b}\), with both vertices in \(A\) distinguished only as members of the two-vertex side. All \(2b\) edge orientations are independent, with the *same* probability \(q\) of the direction \(A\to B\). A source has indegree zero; an isolated vertex is not present in this host. The statistic \(P\) counts directed paths of exactly two edges, not reachability events, paths of arbitrary length, or directed walks with repeated vertices. The classification makes no claim for arbitrary graph families or nonhomogeneous edge probabilities. At \(q=0,1\), all orientation variables are deterministic and covariance is zero, but these endpoints are excluded from the strict sign assertions.

## Proof

For any vertex \(v\), let \(d_v^-\) and \(d_v^+\) denote its indegree and outdegree. Every directed two-step path has a unique middle vertex, so

\[
P=\sum_v d_v^-d_v^+.
\]

Let \(Z_v\) be the indicator that \(v\) is a source. By linearity of covariance and conditional expectation,

\[
\operatorname{Cov}(S,P)=\sum_v \Pr(Z_v=1)\bigl(\mathbb E[P\mid Z_v=1]-\mathbb EP\bigr).
\]

For a fixed \(a\in A\), its source probability is \(q^b\). Conditional on this event all \(b\) edges at \(a\) point outwards. Before conditioning, its expected contribution to \(P\) is \(b(b-1)q(1-q)\); afterward it is zero. At each adjacent \(w\in B\), one of its two incident edges is now forced *into* \(w\). Its chance of having a mixed pair of orientations changes from \(2q(1-q)\) to \(1-q\), an increment of \((1-q)(1-2q)\). All other vertex contributions are unaffected. Therefore

\[
\mathbb E[P\mid Z_a=1]-\mathbb EP
=b(1-q)\bigl(1-(b+1)q\bigr).
\]

For a fixed \(w\in B\), its source probability is \((1-q)^2\); conditioning forces both incident edges from \(w\) to the two vertices of \(A\). Its own expected contribution, originally \(2q(1-q)\), becomes zero. For each of its two neighbors in \(A\), each of the \(b-1\) other edges is now paired with one forced incoming edge. The chance that such a pair is mixed changes from \(2q(1-q)\) to \(q\), an increment of \(q(2q-1)\). Hence

\[
\mathbb E[P\mid Z_w=1]-\mathbb EP
=2q\bigl((2b-1)q-b\bigr).
\]

There are two \(A\)-vertices and \(b\) \(B\)-vertices. Summing their conditional contributions gives

\[
\operatorname{Cov}(S,P)=2q^b b(1-q)(1-(b+1)q)
+b(1-q)^2 2q((2b-1)q-b)
=2bq(1-q)F_b(q).
\]

It remains to classify the sign of \(F_b\). For \(b=2\),

\[
F_2(q)=-2(3q^2-3q+1)=-2\bigl(3(q-1/2)^2+1/4\bigr)<0.
\]

For \(b\ge3\), differentiation gives

\[
F_b''(q)=(b-1)q^{b-3}\bigl((b-2)-b(b+1)q\bigr)-2(2b-1).
\]

This derivative is strictly negative throughout \((0,1)\). Indeed, if \(q\ge(b-2)/(b(b+1))\), its first term is nonpositive. If \(q<(b-2)/(b(b+1))<1/b\), its first term is at most \((b-1)(b-2)/b^{b-3}\), which is less than \(2(2b-1)\): for \(b=3\) this upper bound is \(2<10\); for \(b=4\) it is \(3/2<14\); for \(b\ge5\) it is less than one. Thus \(F_b\) is strictly concave.

For \(b=3,4,5\), concavity and an explicit rational tangent at the respective point \(t_b\) certify negativity on the whole interval:

| \(b\) | \(t_b\) | \(\max_{0\le q\le1}\{F_b(t_b)+F_b'(t_b)(q-t_b)\}\) |
|---|---|---|
| \(3\) | \(11/20\) | \(-459/1000\) |
| \(4\) | \(7/12\) | \(-641/2304\) |
| \(5\) | \(3/5\) | \(-333/3125\) |

Since a differentiable concave function is bounded above by each tangent, all three polynomials are strictly negative on \([0,1]\). These rational tangent evaluations are also reproduced in the checker.

For \(b\ge6\), first observe

\[
F_b(0)=-b,\quad F_b(1)=-b,\quad F_b(1/2)=-\frac14-\frac{b-1}{2^b}<0.
\]

At \(b=6\), direct exact evaluation gives \(F_6(5/8)=1641/262144>0\). The value at \(5/8\) increases strictly with \(b\ge3\), because

\[
F_{b+1}(5/8)-F_b(5/8)
=\left(\frac58\right)^{b-1}\frac{15b-34}{64}+\frac3{32}>0.
\]

Therefore \(F_b(5/8)>0\) for every integer \(b\ge6\). Continuity yields a root in each of \((1/2,5/8)\) and \((5/8,1)\). Strict concavity prohibits three distinct zeros and makes the crossings transverse: the slope at the first is positive and at the second negative (the positive interior point lies above the zero-level chord, so a flat tangent at either zero is impossible). The stated sign classification follows, since the prefactor \(2bq(1-q)\) is positive in \((0,1)\).

## Verification

The standalone Python 3 script `check.py` uses exact integer-weight enumeration of all \(2^{2b}\) orientations of \(K_{2,b}\) for \(2\le b\le7\) at nine rational biases, and checks exact agreement of the empirical joint moments with the formula. It also uses rational arithmetic to check the three tangent-line bounds, the positive explicit witness at \(b=6\), and supplementary rational sign tests. Run `python3 check.py`; no third-party modules are required. The checker reports 645 exact comparisons/sign checks. Exhaustive finite checks are corroboration only: the proof of every unbounded assertion is the argument above.

## Relationship to prior work

The classical literature studies correlation of *reachability events* in random orientations, both on fixed graphs and complete bipartite hosts. Linusson (2009) relates unbiased random orientations to bond percolation and proves correlation inequalities for reachability events. Alm, Janson, and Linusson (2009/2011) study the sign of two reachability events on randomly generated and oriented graphs. Aas (2011) studies joint reachability events on uniformly oriented complete bipartite graphs, with asymptotic class-ratio classifications. Narayanan (2016) gives a reachability-event correlation inequality under independently biased orientations of general graphs. None of their inspected stated results identifies the joint source-count/directed-two-step-path-count covariance or this exact finite biclique threshold. These distinctions do not exclude implicit coverage through more general moment identities in less directly related literature.

## Limitations

The theorem is for one precisely defined homogeneous-bias family \(K_{2,b}\). It does not establish stochastic dominance, independence or conditional-covariance signs, and the root positions other than their ordering are specified implicitly by \(F_b(q)=0\). Historical priority is not independently certified; especially, the result might be derivable from a more general pre-existing formula for moments of oriented-subgraph counts. The analytic argument establishes the signs and uniqueness, while finite enumerations by themselves would not prove those statements. No independent scientific audit has been performed.

## References

1. S. Linusson, *A note on correlations in randomly oriented graphs*, arXiv:0905.2881, first submitted 18 May 2009. https://arxiv.org/abs/0905.2881
2. S. E. Alm, S. Janson and S. Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)*, arXiv:0906.0720, first submitted 3 June 2009; *Random Structures & Algorithms* 39 (2011), 486–506. https://arxiv.org/abs/0906.0720
3. E. Aas, *Path correlations in a randomly oriented complete bipartite graph*, arXiv:1102.1711, first submitted 8 February 2011. https://arxiv.org/abs/1102.1711
4. B. Narayanan, *Connections in randomly oriented graphs*, arXiv:1609.01003, first submitted 5 September 2016; *Combinatorics, Probability and Computing* 27 (2018), 667–671. https://arxiv.org/abs/1609.01003
