# Opposite signed reciprocity–indegree covariance laws with and without self-loops

## Finding

For each integer \(n\ge3\), let every vertex independently select exactly \(k\) **distinct** allowed outgoing neighbors, uniformly among all such subsets. Let \(R\) be the number of unordered pairs of *different* vertices joined by arcs in both directions. Write \(N_j\) for the number of vertices of indegree \(j\), and \(H(t)=\sum_{j=0}^n N_jt^j\) for the empirical indegree polynomial. The exact covariance with the **entire** indegree histogram is a binomial second difference:

* **Self-loops forbidden** (\(1\le k\le n-1\)): put \(p=k/(n-1)\), \(q=1-p\), \(a(t)=q+pt\). Then
\[
\operatorname{Cov}(R,H(t))=\binom n2\frac{p^2q^2}{n-2}(1-t)^2a(t)^{n-3}.
\]
* **Self-loops permitted** (\(1\le k\le n\)): put \(p=k/n\), \(q=1-p\), \(a(t)=q+pt\). A self-loop contributes one unit to indegree but is never counted as a reciprocal pair. Then
\[
\operatorname{Cov}(R,H(t))=-\frac{k^2q^2}{2(n-1)}(1-t)^2a(t)^{n-2}.
\]

The sign reversal has a concrete consequence at indegree zero. For \(1\le k\le n-2\), respectively \(1\le k\le n-1\),
\[
\begin{aligned}
\operatorname{Cov}_{\mathrm{no\ loops}}(R,N_0)&=\frac{nk^2}{2(n-1)(n-2)}\left(1-\frac{k}{n-1}\right)^{n-1}>0,\\
\operatorname{Cov}_{\mathrm{loops}}(R,N_0)&=-\frac{k^2}{2(n-1)}\left(1-\frac{k}{n}\right)^{n}<0.
\end{aligned}
\]
These covariances vanish in the deterministic full-choice boundary cases, as the displayed polynomials predict.

For fixed integers \(k\ge1\) and \(j\ge0\) as \(n\to\infty\), the coefficientwise limit is
\[
 n\operatorname{Cov}(R,N_j)\longrightarrow
 \pm\frac{k^2}{2}\left[\pi_k(j)-2\pi_k(j-1)+\pi_k(j-2)\right],
\]
where the plus sign is loopless, the minus sign is loop-allowed, \(\pi_k(i)=e^{-k}k^i/i!\) for \(i\ge0\), and \(\pi_k(i)=0\) for \(i<0\). Thus **all** cross-covariances have the same explicit Poisson second-difference profile at the fixed-outdegree scale, with the two loop conventions carrying opposite signs.

## Assumptions and scope

Vertices are labeled; all outgoing subsets of the prescribed size have equal probability; choices made at distinct source vertices are independent. An arc can occur at most once, and reciprocal pairs are unordered and require two distinct endpoints. The indegree of a vertex counts its self-loop when loops are permitted. All covariance identities are polynomial equalities in a real (or formal) indeterminate \(t\), not just numerical evaluations. For a fixed \(k\), the limit is taken through valid integers \(n\) without changing \(j\). No assumption of independence between reciprocal-pair count and indegree histogram is made.

## Proof

Write \(I_{uv}\) for the indicator that both arcs between distinct vertices \(u,v\) are present. In either model \(\mathbb EI_{uv}=p^2\), with \(p\) as above, and
\[
\operatorname{Cov}(R,H(t))=\binom n2p^2\bigl(\mathbb E[H(t)\mid I_{12}=1]-\mathbb EH(t)\bigr).
\]

**Loopless model.** Unconditionally, each vertex receives independent incoming arcs from \(n-1\) other source vertices, hence \(\mathbb EH(t)=na(t)^{n-1}\). Condition on arcs \(1\to2\) and \(2\to1\). At either endpoint, the incoming arc from the other endpoint is forced, while the remaining \(n-2\) source vertices contribute independently with probability \(p\), so its conditional indegree PGF is \(t a(t)^{n-2}\). For a third vertex, each of sources \(1,2\), conditioned on having already selected a specified other endpoint, chooses it with conditional probability \(p'=(k-1)/(n-2)\); the remaining \(n-3\) sources independently select it with probability \(p\). Set
\[
b(t)=1-p'+p't=a(t)+\frac{q(1-t)}{n-2}.
\]
It follows that
\[
\mathbb E[H(t)\mid I_{12}=1]=2t a(t)^{n-2}+(n-2)b(t)^2a(t)^{n-3}.
\]
Use the elementary relation \(t=a(t)-q(1-t)\). In the bracket after factoring \(a(t)^{n-3}\), all terms of degree zero and one in \(1-t\) cancel, leaving
\[
2t a(t)+(n-2)b(t)^2-na(t)^2=\frac{q^2}{n-2}(1-t)^2.
\]
Substituting gives the loopless identity, including the boundary \(q=0\).

**Loop-allowed model.** Now \(\mathbb EH(t)=na(t)^n\). Conditioning on the reciprocal pair again fixes arcs \(1\to2\) and \(2\to1\), but **does not fix self-loops**. For each of the two conditioned source rows the probability of any other individual target is \(p'=(k-1)/(n-1)\). Hence define
\[
b(t)=1-p'+p't=a(t)+\frac{q(1-t)}{n-1}.
\]
Each endpoint has conditional PGF \(t b(t)a(t)^{n-2}\), while each of the \(n-2\) other vertices has conditional PGF \(b(t)^2a(t)^{n-2}\). Consequently
\[
\mathbb E[H(t)\mid I_{12}=1]=2t b(t)a(t)^{n-2}+(n-2)b(t)^2a(t)^{n-2}.
\]
Algebra with \(t=a(t)-q(1-t)\) yields
\[
2t b(t)+(n-2)b(t)^2-na(t)^2
=-\frac{nq^2}{(n-1)^2}(1-t)^2.
\]
Multiplication by \(\binom n2p^2a(t)^{n-2}\) and \(p=k/n\) gives the stated negative identity.

**Coefficientwise and limiting consequences.** Taking coefficients of \(t^j\) in either polynomial proves the finite covariance with each \(N_j\). Setting \(t=0\) proves the strict-sign results whenever \(q>0\). At \(t=1\) the exact covariance polynomial has a double zero; this also reflects the deterministic facts \(\sum_jN_j=n\) and \(\sum_jjN_j=nk\). For fixed \(k\), the prefactor in each formula is \(\pm k^2/(2n)+O(n^{-2})\), and \(a(t)^{n-O(1)}\) converges coefficientwise to \(e^{k(t-1)}\). Therefore the coefficientwise limit is the displayed signed second difference of Poisson masses. This uses only elementary finite binomial limits and does not replace any infinite argument with a finite experiment.

## Verification

The included standalone `verify.py` independently enumerates all choices of allowable outgoing subsets in seventeen small parameter instances, with exact integer counts and rational arithmetic. For every indegree coefficient in each instance it compares the directly enumerated covariance to the corresponding coefficient of the claimed polynomial. It reports **86 passing exact coefficient comparisons** for sizes \(3\le n\le5\) and permitted small outdegrees. This checks both loop conventions and deterministic full-choice boundary cases. Run `python3 verify.py` with the Python standard library. The algebraic proof above covers every admissible \(n,k,j\); finite enumeration is not asserted to prove the infinite statement.

## Relationship to prior work

Zlatić and Štefančić (2009) study reciprocity and degree correlations in directed network models, including a reciprocity-driven growing network. Their variables and sampling law are not the independent uniform fixed-outdegree subset ensembles here. McKay and Skerman (2013) analyze the degree-sequence distribution for random binary matrices with prescribed row sums and both loop conventions, but their degree-sequence statistics do not determine the number of reciprocal pairs, and their theorems do not state this mixed covariance polynomial. Durak and colleagues (2012) construct directed null models with reciprocal degree constraints, rather than computing the unconditioned reciprocal-count/indegree-histogram covariance. Hansen and Jaworski (2008) treat one-out random mapping local statistics through exchangeable indegrees; the complete all-outdegree paired reciprocity formulas and loop-convention comparison are not presented in the inspected portions. Peterson and Pittel (2013) and Frieze and Johansson (2014) study other properties of random \(k\)-out digraphs. These are statement-level comparisons, not proofs that no prior derivation exists.

## Limitations

The result requires independently chosen uniform fixed-size outgoing subsets and does not apply unchanged to sampling with replacement, nonuniform target weights, or dependence between source rows. It concerns second moments between one reciprocal-pair statistic and the indegree histogram, not the complete joint probability law or a multivariate central limit theorem. Some older random-mapping literature, particularly Arney and Bender's 1982 work, was not available in inspectable full text; historical priority in the \(k=1\) specialization therefore remains uncertain. No independent audit or claim of universal priority is supplied.

## References

- V. Zlatić and H. Štefančić, *Influence of reciprocal edges on degree distribution and degree correlations*, arXiv:0902.3542v1 (first posted 2009-02-20), later Phys. Rev. E 80, 016117 (2009). https://arxiv.org/abs/0902.3542
- B. D. McKay and F. Skerman, *Degree sequences of random digraphs and bipartite graphs*, arXiv:1302.2446v1 (2013-02-11). https://arxiv.org/abs/1302.2446
- J. C. Hansen and J. Jaworski, *Local properties of random mappings with exchangeable in-degrees*, Adv. Appl. Probab. 40 (2008), 183–205, DOI 10.1239/aap/1208358892. https://doi.org/10.1239/aap/1208358892
- K. Durak et al., *A Scalable Null Model for Directed Graphs Matching All Degree Distributions: In, Out and Reciprocal*, arXiv:1210.5288v1 (2012). https://arxiv.org/abs/1210.5288
- N. Peterson and B. Pittel, *Distance between two random k-out digraphs with and without preferential attachment*, arXiv:1311.5961v1 (2013). https://arxiv.org/abs/1311.5961
- A. Frieze and T. Johansson, *On random k-out subgraphs*, arXiv:1405.2129v1 (2014). https://arxiv.org/abs/1405.2129
- J. Arney and E. Bender, *Random mappings with constraints on coalescence and number of origins* (1982); relevant historical abstract located, full text not verified.
