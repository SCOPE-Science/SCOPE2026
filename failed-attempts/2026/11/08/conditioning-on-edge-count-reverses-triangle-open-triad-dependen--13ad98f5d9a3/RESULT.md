# Conditioning on edge count reverses triangle–open-triad dependence

## Finding
For each integer \(n\geq 4\), put \(N=\binom n2\). In a simple graph \(G\) on \(n\) labeled vertices let \(T\) be the number of three-vertex sets inducing a triangle, and let \(O\) be the number inducing exactly two edges (an *open triad*, equivalently an induced three-vertex path).

In the uniform fixed-edge model \(G(n,m)\), \(0\leq m\leq N\), put
\[
R_n(m)=(n-1)(n^2-n-4)+m(n^2-3n-8).
\]
Then the exact covariance is
\[
\boxed{\operatorname{Cov}_{G(n,m)}(T,O)=-\frac{4(m)_3(N-m)_2R_n(m)}{(n+1)^2(n+2)(N-5)(N-4)(N-2)^2}.}
\]
Here \((a)_r=a(a-1)\cdots(a-r+1)\). It is **strictly negative** whenever \(3\leq m\leq N-2\) and is zero for \(m\leq2\) or \(m\geq N-1\).

In sharp contrast, if each edge is retained independently with probability \(0<p<1\), then
\[
\boxed{\operatorname{Cov}_{G(n,p)}(T,O)=3\binom n3p^4(1-p)\big[2(n-3)-(3n-8)p\big].}
\]
Thus its sign is positive, zero, or negative according as \(p\) is below, equal to, or above the unique threshold
\[
p_n=\frac{2(n-3)}{3n-8},\qquad \frac12\leq p_n<\frac23.
\]
In particular, whenever \(0<p<p_n\), the unconditioned covariance is positive even though the covariance at **every** feasible fixed edge count is nonpositive. The law of total covariance locates the positive contribution in variation of the edge count across graphs.

For any sequence with \(m/\binom n2\to p\in(0,1)\),
\[
\operatorname{Cov}_{G(n,m)}(T,O)=-p^4(1-p)^2n^3+o(n^3).
\]
For fixed \(p\in(0,1)\), the independent-edge expression has leading term \(\frac12p^4(1-p)(2-3p)n^4+O(n^3)\). The asymptotics are consequences, not substitutes for, the finite-sample identities.

## Assumptions and scope
The graph is simple and undirected with vertex set \(\{1,\ldots,n\}\). In \(G(n,m)\), all \(m\)-subsets of the \(N\) available edges are equally likely; in \(G(n,p)\), all possible edges are independent. Each induced triangle or open triad is counted exactly once by its **unordered vertex triple**. An open triad has exactly two of its three possible edges present. In particular, a triangle contributes no open triads, though it contributes three non-induced wedges. This distinction matters for every formula here.

## Proof
Write \(\mathcal S\) for the \(Q=\binom n3\) three-vertex subsets. For \(S\in\mathcal S\), set \(X_S=\mathbf1\{G[S]\text{ has three edges}\}\) and \(Y_S=\mathbf1\{G[S]\text{ has two edges}\}\). Then \(T=\sum_S X_S\), \(O=\sum_S Y_S\).

First consider \(G(n,m)\). Define \(q_r=(m)_r/(N)_r\) for \(0\leq r\leq6\); when \(m<r\), this value is zero. The expectations are \(\mathbb ET=Qq_3\) and \(\mathbb EO=3Q(q_2-q_3)\). Partition the ordered pairs \((S,U)\in\mathcal S^2\) into three exhaustive classes:

1. \(S=U\): \(X_SY_U=0\), since three and two induced edges are mutually exclusive.
2. \(|S\cap U|=2\): the triples share one possible graph edge. To have \(X_S=Y_U=1\), all three edges of \(S\) must be present and **exactly one** of the other two possible edges of \(U\) must be present. There are two choices for this edge; their joint probability is \(2(q_4-q_5)\). There are exactly \(3Q(n-3)\) ordered pairs of this kind.
3. \(|S\cap U|\leq1\): the two possible-edge sets are disjoint. The joint probability is \(3(q_5-q_6)\), by choosing the two present edges of \(U\), forcing five edges present and the sixth absent. The number of these ordered pairs is \(Q^2-Q-3Q(n-3)\).

Consequently, without any independence approximation,
\[
\begin{aligned}
\operatorname{Cov}_{G(n,m)}(T,O)
={}&6Q(n-3)(q_4-q_5)\\
&+3[Q^2-Q-3Q(n-3)](q_5-q_6)\\
&-3Q^2q_3(q_2-q_3).
\end{aligned}
\tag{1}
\]
Substituting \(q_r=(m)_r/(N)_r\) and \(Q=n(n-1)(n-2)/6\), collecting over a common denominator and canceling common factors yields the boxed factorization. Equation (1), with no canceled denominators, also directly covers every boundary edge count.

The denominator in the factored expression is positive for \(n\geq4\). For \(n\geq5\), both \(n^2-3n-8>0\) and \((n-1)(n^2-n-4)>0\), so \(R_n(m)>0\). For \(n=4\), \(R_4(m)=24-4m>0\) at the two relevant values \(m=3,4\). Therefore its sign is strictly negative when \((m)_3(N-m)_2>0\), that is, \(3\leq m\leq N-2\). In all other cases this falling-factorial product is zero; direct counting also shows \(T=0\) when \(m\leq2\), and \(T,O\) are deterministic at \(m=N-1,N\).

For \(G(n,p)\), disjoint possible-edge sets are independent. On the same triple, \(\operatorname{Cov}(X_S,Y_S)=-3p^5(1-p)\). For distinct triples sharing a graph edge, \(\mathbb E[X_SY_U]=2p^4(1-p)\), whereas \(\mathbb EX_S\mathbb EY_U=3p^5(1-p)\); their covariance is \(p^4(1-p)(2-3p)\). Summing the \(Q\) same-triple and \(3Q(n-3)\) shared-edge contributions gives the second boxed formula. Its strictly linear bracket in \(p\) proves the sharp threshold. Finally, \(\operatorname{Cov}(T,O)=\mathbb E[\operatorname{Cov}(T,O\mid M)]+\operatorname{Cov}(\mathbb E[T\mid M],\mathbb E[O\mid M])\) for the binomial edge count \(M\), giving the stated source of the sign reversal. The displayed asymptotic expansions follow by taking leading powers in the exact expressions.

## Verification
Run `python3 verify.py` using Python 3.8 or later and no third-party packages. The program independently enumerates **every** labeled graph on \(n=4,5,6\) vertices, compares the directly calculated fixed-edge covariances against both equation (1) and the factorization, and compares six independent-edge rational probabilities against the exact formula. It also checks the two finite formulas and their signs exactly for \(4\leq n\leq35\) and all admissible edge counts. The run reported **14,456 passed exact comparisons**. This enumeration validates boundary cases and implementation but does not prove the universal statement; that is supplied by the exhaustive pair classification and factorization above.

## Relationship to prior work
Alm, Janson and Linusson (arXiv:0906.0720, first public version 2009-06-03) show how covariance signs can depend sharply on the \(G(n,p)\) versus \(G(n,m)\) choice, but their events concern directed reachability after random edge orientations, not induced triad counts. Kunegis (arXiv:1402.5835) gives overlap-based exact means and covariances for ordinary, non-induced graph-pattern counts in \(G(n,1/2)\); that machinery is a close methodological antecedent, not this all-density comparison. Goldschmidt, Griffiths and Scott (arXiv:1902.06830) study asymptotic deviations of path and triangle counts in fixed-edge graphs and their general subgraph consequences; the inspected manuscript does not state this all-finite-parameter induced-triad sign classification. Janson (1990) provides broader functional-limit machinery for induced random-subgraph counts. Its potential implicit consequences are a historical-priority risk rather than evidence of uniqueness.

## Limitations
These are covariance—not stochastic dominance, negative association, or independence—statements. At the isolated \(G(n,p)\) zero threshold, zero covariance need not mean independence. They do not extend automatically to random graphs with a prescribed degree sequence or to non-induced wedge counts. Generic earlier subgraph moment formulas may imply some expressions by specialization; historical claims of novelty for the exact all-parameter sign comparison require independent literature validation. The independent-edge coefficient at \(p=2/3\) has an exceptional lower-order leading term, so a positive \(n^4\)-order claim is not made there.

## References
1. S. E. Alm, S. Janson, S. Linusson, *Correlations for paths in random orientations of \(G(n,p)\) and \(G(n,m)\)*, arXiv:0906.0720 (first posted 2009-06-03), https://arxiv.org/abs/0906.0720.
2. J. Kunegis, *Polcovar: Software for Computing the Mean and Variance of Subgraph Counts in Random Graphs*, arXiv:1402.5835 (first posted 2014-02-24), https://arxiv.org/abs/1402.5835.
3. C. Goldschmidt, S. Griffiths, A. Scott, *Moderate deviations of subgraph counts in the Erdős–Rényi random graphs \(G(n,m)\) and \(G(n,p)\)*, arXiv:1902.06830 (first posted 2019-02-18), https://arxiv.org/abs/1902.06830.
4. S. Janson, *A functional limit theorem for random graphs with applications to subgraph count statistics*, Random Structures & Algorithms 1 (1990), 15–37, https://doi.org/10.1002/rsa.3240010103.
