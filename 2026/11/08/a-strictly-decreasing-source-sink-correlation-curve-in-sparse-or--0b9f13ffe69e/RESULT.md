# A strictly decreasing source–sink correlation curve in sparse ordered random DAGs

## Finding

Let \(n\ge2\). On the ordered vertex set \(\{1,\ldots,n\}\), put each directed edge \(i\to j\), \(i<j\), independently with probability \(p\in(0,1)\). A **source** has indegree zero, a **sink** has outdegree zero, and an isolated vertex counts as both. Write \(S_n\) and \(K_n\) for their respective counts and \(q=1-p\). For every finite \(n\),

\[
\mathbb E S_n=\mathbb E K_n=\frac{1-q^n}{p},\qquad
\operatorname{Var}(S_n)=\operatorname{Var}(K_n)
=\frac{1-q^n}{p}-\frac{1-q^{2n}}{p(1+q)},
\]
\[
\operatorname{Cov}(S_n,K_n)
=\frac{q^{n-1}(np-1+q^n)}p>0.
\]

For each fixed \(c>0\), put \(p=c/n\) for sufficiently large \(n\), and center the two counts by their exact common mean \(\mu_n=(1-(1-p)^n)/p\). Then

\[
\frac1{\sqrt n}\begin{pmatrix}S_n-\mu_n\\K_n-\mu_n\end{pmatrix}
\xrightarrow{\mathrm d}N_2\!\left(0,\begin{pmatrix}A(c)&B(c)\\B(c)&A(c)\end{pmatrix}\right),
\]
where
\[
A(c)=\frac{(1-e^{-c})^2}{2c},\qquad
B(c)=\frac{e^{-c}(c-1+e^{-c})}{c}.
\]
The limiting source–sink correlation is therefore
\[
\rho(c)=\frac{B(c)}{A(c)}
=\frac{2e^{-c}(c-1+e^{-c})}{(1-e^{-c})^2}.
\]
It decreases **strictly** from \(1\) to \(0\) as \(c\) increases from zero to infinity. The limit law is nondegenerate for each fixed \(c>0\).

## Assumptions and scope

Every unordered vertex pair \(\{i,j\}\) with \(i<j\) supplies one possible edge in the fixed direction \(i\to j\). Different edge indicators are independent. The result concerns the resulting ordered Bernoulli DAG, **not** a uniform distribution over all labeled DAGs and **not** the independent two-direction digraph conditioned to be acyclic. The stated central limit theorem holds for fixed \(c>0\) with \(n\to\infty\); the endpoint statements about \(\rho\) concern the explicit function, not a joint limit in which \(c\) varies with \(n\). Reversing the total order exchanges sources and sinks without changing their joint distribution.

## Proof

**1. Exact first and second moments.** Set \(Z_{ij}=1\) when the possible edge \(i\to j\) is absent. Then the \(Z_{ij}\), \(i<j\), are independent Bernoulli variables with mean \(q\). Write
\[
U_j=\prod_{i<j}Z_{ij},\qquad V_i=\prod_{j>i}Z_{ij},
\qquad S_n=\sum_j U_j,\quad K_n=\sum_i V_i,
\]
with the empty product equal to one. The \(U_j\) are mutually independent (their edge sets have distinct targets); separately, the \(V_i\) are mutually independent (their edge sets have distinct sources). Thus \(\mathbb E U_j=q^{j-1}\), \(\mathbb E V_i=q^{n-i}\), and the geometric-sum formulas yield the means and variances stated above.

For \(i<j\), the two events \(V_i=1\) and \(U_j=1\) share exactly one required absent edge, namely \(i\to j\), and otherwise involve disjoint edge sets. Hence
\[
\operatorname{Cov}(U_j,V_i)
=q^{n+j-i-2}-q^{n+j-i-1}
=pq^{n+j-i-2}\quad (i<j).
\]
For \(i\ge j\), these event sets are disjoint and the covariance is zero. Therefore, writing \(d=j-i\),
\[
\operatorname{Cov}(S_n,K_n)
=pq^{n-1}\sum_{d=1}^{n-1}(n-d)q^{d-1}
=\frac{q^{n-1}(np-1+q^n)}p.
\]
The first expression proves strict positivity for \(n\ge2\), \(0<p<1\), without a potentially unstable subtraction.

**2. Sparse covariance limits.** Under \(p=c/n\), \(q^n\to e^{-c}\). Substitution into the exact moment formulas gives
\[
\frac{\operatorname{Var}(S_n)}n=\frac{\operatorname{Var}(K_n)}n\to A(c),\quad
\frac{\operatorname{Cov}(S_n,K_n)}n\to B(c).
\]

**3. Joint central limit theorem.** Reveal all edges with target \(j\) at stage \(j\); let \(\mathcal F_j\) contain edges whose target is at most \(j\). For \(i<j\), set
\[
R_{ij}=\prod_{i<\ell<j}Z_{i\ell},\qquad R_j=\sum_{i<j}R_{ij}.
\]
These quantities are \(\mathcal F_{j-1}\)-measurable. The Doob martingale increments for the centered vector \((S_n,K_n)\) are
\[
\Delta S_j=U_j-q^{j-1},\qquad
\Delta K_j=q^{n-j}\sum_{i<j}R_{ij}(Z_{ij}-q).
\]
Consequently their predictable conditional covariance entries are exactly
\[
\begin{aligned}
\mathbb E[(\Delta S_j)^2\mid\mathcal F_{j-1}]&=q^{j-1}(1-q^{j-1}),\\
\mathbb E[(\Delta K_j)^2\mid\mathcal F_{j-1}]&=pq^{2(n-j)+1}R_j,\\
\mathbb E[\Delta S_j\Delta K_j\mid\mathcal F_{j-1}]&=pq^{n-1}R_j.
\end{aligned}
\]
Here \(\mathbb E R_j=(1-q^{j-1})/p\). For fixed \(j\), the variables \(R_{ij}\), as \(i\) varies, depend on disjoint outgoing-edge families, so \(\operatorname{Var}(R_j)\le n\). When \(p=c/n\), the \(L^2\)-distance between each normalized predictable covariance sum and its expectation is bounded by a constant times \(p\sqrt n=O(n^{-1/2})\). The normalized expectations converge to the matrix with entries \(A(c), B(c)\) by the preceding exact moment calculation.

For the Lindeberg condition, \(|\Delta S_j|\le1\); given \(\mathcal F_{j-1}\), the other increment is a sum of at most \(n\) centered independent Bernoulli terms of absolute coefficient at most one. Since \(np=c\), the fourth conditional moment is bounded uniformly by \(c+3c^2\). Hence the sum of normalized Lindeberg tails tends to zero by the fourth-moment/Markov bound. The multivariate martingale central limit theorem, or its scalar form applied to every Cramér–Wold combination, now proves the claimed Gaussian limit. The covariance matrix is strictly positive definite because of Step 4.

**4. Sharp correlation monotonicity.** The covariance coefficient satisfies \(B(c)>0\) since \(c-1+e^{-c}>0\) for \(c>0\). Simplifying the ratio and differentiating yields
\[
\rho'(c)=-\frac{2e^c\bigl[c(e^c+1)-2(e^c-1)\bigr]}{(e^c-1)^3}<0.
\]
Indeed, the bracket is positive exactly when \(c>2\tanh(c/2)\), which holds strictly for every positive \(c\). Taylor expansion at zero gives \(\rho(c)\to1\), while exponential decay gives \(\rho(c)\to0\) at infinity. Therefore \(0<\rho(c)<1\) for each \(c>0\); in particular, \(A(c)>|B(c)|\), and the Gaussian covariance matrix is nonsingular.

## Verification

The standalone, standard-library Python program `verify.py` enumerates all edge subsets through six vertices (using exact rational edge probabilities), reconstructs the source and sink indicators without using the derived formulas, and checks all means, variances, site covariances, and total covariance identities. It also checks the conditional martingale covariance equations against independently enumerated incoming-edge patterns for multiple past edge configurations. Controlled floating-point comparisons corroborate the sparse covariance limits and sample the strictly decreasing explicit correlation function. Run it with `python3 verify.py`; it reports the number of assertions. These computations check finite consequences, while Steps 1–4 establish the assertions for all stated parameters.

## Relationship to prior work

The edge model is the ordered random acyclic graph of Barak and Erdős (1984), up to reversing the orientation of every edge; their theorem concerns maximal strongly independent sets, not the two degree-zero counts. Denisov, Foss and Konstantopoulos (arXiv:1005.4806, first posted 2010-05-26) study the same independent directed-edge construction, including its homogeneous case, but their inspected statements and proof sections concern longest paths and regenerative structure. Bollobás and Brightwell (1997) study the associated transitive-closure random graph order and general parameters such as height and linear extensions; a complete-text comparison could not be obtained. Ralaivaosaona (2022) proves source-count and isolated-vertex asymptotics for a **different** law: an independently directed binomial digraph conditioned to be acyclic. Its first-order source-density function, \(e^{-c}\) for \(c<1\) and \(1/(ec)\) for \(c\ge1\), differs from the present ordered model's \((1-e^{-c})/c\), so those distributional results neither equal nor imply the present joint law. This document claims the explicit joint Gaussian covariance and its strictly decreasing density-dependent correlation, not a new central limit theorem for all random DAG models.

## Limitations

No convergence rate in the central limit theorem is asserted. The result does not address \(c=c_n\to0\) or \(c=c_n\to\infty\) jointly with \(n\). Exact source–sink covariance and normality may be derivable implicitly from general degree-count theorems; the 1997 full text and other historical random-order literature remain originality risks. Self-review is not an independent audit or a proof of priority. No claim is made for DAGs sampled uniformly or for digraphs conditioned to be acyclic.

## References

1. A. B. Barak and P. Erdős, *On the Maximal Number of Strongly Independent Vertices in a Random Acyclic Directed Graph*, SIAM J. Algebraic Discrete Methods 5 (1984), 508–514. Author-accessible full text: https://www.renyi.hu/~p_erdos/1984-14.pdf ; doi:10.1137/0605049.
2. D. Denisov, S. Foss and T. Konstantopoulos, *Limit theorems for a random directed slab graph*, arXiv:1005.4806, first public version 2010-05-26; Ann. Appl. Probab. 22 (2012), 702–733. https://arxiv.org/abs/1005.4806 .
3. B. Bollobás and G. Brightwell, *The Structure of Random Graph Orders*, SIAM J. Discrete Math. 10 (1997), 318–335, doi:10.1137/S0895480194281215.
4. D. Ralaivaosaona, *The Number of Sources and Isolated Vertices in Random Directed Acyclic Graphs*, LIPIcs AofA 225 (2022), article 17, doi:10.4230/LIPIcs.AofA.2022.17.
5. P. Hall and C. C. Heyde, *Martingale Limit Theory and Its Application*, Academic Press (1980), multivariate martingale central limit method.
