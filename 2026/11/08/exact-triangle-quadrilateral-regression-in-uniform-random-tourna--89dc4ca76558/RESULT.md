# Exact triangle–quadrilateral regression in uniform random tournaments

## Finding

For every integer \(n\ge4\), choose independently and fairly the directions of all edges of the complete graph on \(n\) labeled vertices. Let \(X_n\) be the number of three-vertex subsets inducing a directed cyclic triangle, and \(Y_n\) the number of four-vertex subsets inducing a strongly connected tournament. Every strongly connected tournament on four vertices has exactly one directed Hamiltonian four-cycle, so \(Y_n\) also counts directed four-cycles without distinguished starting point.

The exact moments are

\[
\begin{aligned}
\mathbb E X_n&=\tfrac14\binom n3,&\operatorname{Var}(X_n)&=\tfrac3{16}\binom n3,\\
\mathbb E Y_n&=\tfrac38\binom n4,&\operatorname{Var}(Y_n)&=\tfrac{3(n-3)(4n-11)}{256}\binom n3,\\
\operatorname{Cov}(X_n,Y_n)&=\tfrac38\binom n4.
\end{aligned}
\]

In particular, the correlation and optimal least-squares explained-variance fraction are exactly

\[
\operatorname{Corr}(X_n,Y_n)=\sqrt{\frac{4n-12}{4n-11}},\qquad
R^2=\frac{4n-12}{4n-11}.
\]

Thus the correlation increases to one, with a precisely known finite-size deficit. More sharply, defining the **centered linear-regression residual**

\[
Z_n=(Y_n-\mathbb E Y_n)-\frac{n-3}{2}(X_n-\mathbb E X_n),
\]

one has

\[
\operatorname{Cov}(Z_n,X_n)=0,\qquad
\operatorname{Var}(Z_n)=\frac{3(n-3)}{256}\binom n3
=\frac{\operatorname{Var}(Y_n)}{4n-11}.
\]

This is an identity of second moments, not an assertion that the full conditional expectation of \(Y_n\) given \(X_n\) is linear or that either standardized count is normally distributed.

## Assumptions and scope

The law is the independent-edge uniform random tournament. Different unordered vertex pairs are oriented independently with equal probabilities; all subgraph counts are **induced** and taken once per unordered vertex set. A directed triangle means a cyclic orientation of all its three arcs. A strongly connected four-vertex tournament is the isomorphism class with outdegree multiset \(\{1,1,2,2\}\), not a transitive tournament and not a tournament with a source or a sink. The formulas hold for each integer \(n\ge4\), without asymptotic assumptions. The natural primary classification is MSC2020 60C05.

## Proof

**Local four-vertex classification.** Fix an oriented triple. A cyclic triple is extended by a fourth vertex to a strongly connected tournament in six of the eight possible sets of incident arc orientations: precisely the two orientations where the new vertex beats all three or loses to all three fail. A transitive triple is extended to a strongly connected tournament in exactly two of eight ways: the new vertex must beat the existing maximal vertex and lose to the existing minimal vertex, and its arc to the intermediate vertex is arbitrary. Since a fair random triple is cyclic with probability \(1/4\),

\[
\Pr(Y_Q=1\mid X_T=1)=\tfrac34,\quad
\Pr(Y_Q=1\mid X_T=0)=\tfrac14\quad(T\subset Q,\ |T|=3,\ |Q|=4),
\]

and hence \(\Pr(Y_Q=1)=3/8\). A four-vertex tournament is strongly connected if and only if it has two cyclic triples; its directed Hamiltonian four-cycle is unique. These elementary four-vertex statements can also be checked directly among the \(2^6=64\) orientations (and are independently checked in the verifier).

**Overlap covariance calculus.** Write \(X_T\) for the cyclic indicator of a triple and \(Y_Q\) for the strong indicator of a quadruple. Whenever their underlying edge sets are disjoint, the indicators are independent. If two triangles share exactly two vertices, condition on the orientation of their common edge. Their remaining arcs are independent, and the probability each is cyclic is \(1/4\), independent of that common orientation. Thus distinct \(X_T\) are pairwise uncorrelated and

\[
\operatorname{Var}(X_n)=\binom n3\cdot\tfrac14(1-\tfrac14)=\tfrac3{16}\binom n3.
\]

If a triple and quadruple intersect in only two vertices, conditioning on their common edge gives \(\Pr(X_T=1\mid\text{edge})=1/4\) and \(\Pr(Y_Q=1\mid\text{edge})=3/8\). Thus the two indicators are uncorrelated. A triple contained in a quadruple instead has

\[
\operatorname{Cov}(X_T,Y_Q)
=\tfrac14\tfrac34-\tfrac14\tfrac38=\tfrac3{32}.
\]

There are exactly \(4\binom n4\) such nested pairs, so

\[
\operatorname{Cov}(X_n,Y_n)=\tfrac3{32}\cdot4\binom n4=\tfrac38\binom n4.
\]

For two distinct quadruples with three common vertices, conditioning on the common triple makes their remaining random arcs independent. Their conditional strong probabilities are \(3/4\) for a cyclic common triple, \(1/4\) for a transitive one. The variance of this conditional probability equals

\[
\tfrac14\tfrac34(\tfrac34-\tfrac14)^2=\tfrac3{64},
\]

which is exactly the covariance of their two strong indicators. Distinct quadruples meeting in at most two vertices instead have zero covariance: after conditioning on the at-most-one common arc, each conditional strong probability remains \(3/8\), by vertex-swap symmetry. There are \(\binom n3\binom{n-3}2\) unordered pairs of quadruples with exactly three shared vertices. Therefore

\[
\begin{aligned}
\operatorname{Var}(Y_n)
&=\tfrac{15}{64}\binom n4
+2\cdot\tfrac3{64}\binom n3\binom{n-3}2\\
&=\tfrac{3(n-3)(4n-11)}{256}\binom n3.
\end{aligned}
\]

The expectations follow by summing the local indicator probabilities. Since \(\binom n4=(n-3)\binom n3/4\), the least-squares slope is

\[
\frac{\operatorname{Cov}(X_n,Y_n)}{\operatorname{Var}(X_n)}=\frac{n-3}{2}.
\]

Substituting the exact moments and subtracting the projection yields

\[
\operatorname{Var}(Z_n)=\operatorname{Var}(Y_n)-\frac{\operatorname{Cov}(X_n,Y_n)^2}{\operatorname{Var}(X_n)}
=\tfrac{3(n-3)}{256}\binom n3.
\]

Dividing gives the exact correlation square \((4n-12)/(4n-11)\), finishing the proof. Strict positivity of all relevant variances follows from \(n\ge4\).

## Verification

Run `python verify.py` with a standard Python 3 interpreter. The source uses exhaustive enumeration of all \(2^{\binom n2}\) labeled tournaments for \(n=4,5,6\) (respectively \(64\), \(1024\), and \(32768\) orientations), independently testing strong connectivity by graph reachability, and compares means, second moments, regression residual variance and correlation square using exact rational arithmetic. All enumerated cases passed. The direct overlap calculations above, not finite enumeration, prove the claims for every \(n\ge4\).

## Relationship to prior work

Andersson (1998) studies general asymptotic distributions of random-tournament subgraph counts; available bibliographic material establishes a relevant general framework, but its inaccessible full text could contain related formulas. Linial and Morgenstern (2014) give the deterministic four-vertex counting relation and extremal constraints for cyclic triangles and four-cycles; their Observation 1.2 relates four-vertex type frequencies but does not supply moments under the independent orientation law. Coregliano (2015) studies four-vertex tournament isomorphism types, especially the unique strongly connected type, and their deterministic asymptotic densities. Chan, Grzesik, Král' and Noel (2019) analyze the extremal feasible relation between directed triangle and directed four-cycle densities in arbitrary large tournaments. These are close *objects* but not the same *statement*: the result here is the exact joint finite-order covariance matrix, optimal regression and residual variance under independent fair orientations. The 2014 deterministic cycle-density identities and extremal inequalities do not imply these random finite moments; the general variance theory could in principle provide a route to them and remains a historical-priority uncertainty.

## Limitations

No assertion is made about conditional regression beyond orthogonal projection, a central limit theorem, nonuniform tournament models, or extremal deterministic tournaments. The proof is self-contained. Historical originality is qualified because the full text of Andersson (1998) could not be inspected; absence of an explicit formula in the accessible sources is not proof of publication priority. The exact formulas and asymptotic correlation follow independently of that provenance question.

## References

1. Pontus Andersson, *On the asymptotic distributions of subgraph counts in a random tournament*, Random Structures & Algorithms 13 (1998), 249–260, first published 1998-12-07. https://doi.org/10.1002/(SICI)1098-2418(199810/12)13:3/4%3C249::AID-RSA4%3E3.0.CO;2-V
2. Nati Linial and Avraham Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576, initially public 2014-05-07. https://arxiv.org/abs/1405.1576
3. Leonardo Nagami Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124, initially public 2015-03-13. https://arxiv.org/abs/1503.04124
4. Timothy F. N. Chan, Andrzej Grzesik, Daniel Král' and Jonathan A. Noel, *Cycles of length three and four in tournaments*, arXiv:1902.00572, initially public 2019-02-01. https://arxiv.org/abs/1902.00572
