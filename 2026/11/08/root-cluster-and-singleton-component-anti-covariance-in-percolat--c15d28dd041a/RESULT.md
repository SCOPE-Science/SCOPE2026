# Root-cluster and singleton-component anti-covariance in percolated recursive trees

## Finding

For each integer \(n\geq2\) and retention probability \(p\in[0,1]\), let \(C_n\) be the size of the component containing vertex \(1\), and let \(I_n\) be the number of singleton components, after independent Bernoulli bond percolation on a uniform random recursive tree on \(\{1,\ldots,n\}\). Write
\[
a_n(p)=\prod_{j=1}^{n-1}\left(1+\frac{p}{j}\right),\qquad
u_n(p)=\prod_{j=1}^{n-1}\left(1-\frac{p}{j}\right).
\]
The exact mixed moment and covariance are
\[
\mathbb E[C_nI_n]=u_n(p)+\frac{(1-p)(n-1)}{1+p}a_n(p),
\]
\[
\boxed{\operatorname{Cov}(C_n,I_n)
=u_n(p)-\frac{a_n(p)}{1+p}\bigl(1-p+2p\,u_n(p)\bigr).}
\]
For \(n\geq2\), this covariance is strictly negative at every \(0<p<1\), and it is zero at \(p=0,1\).

For fixed \(0<p<1\), it has the two-term asymptotic
\[
\operatorname{Cov}(C_n,I_n)
=-\frac{1-p}{(1+p)\Gamma(1+p)}n^p
-\frac{2\sin(\pi p)}{\pi(1+p)}+o(1).
\]
Moreover define
\[
\beta_p=\frac{2p(1-p)(p+2)}{(1+p)^2(1+2p)},\qquad
v_p=\frac2{\Gamma(1+2p)}-\frac1{\Gamma(1+p)^2}.
\]
These numbers are positive, and
\[
\lim_{n\to\infty}\sqrt n\,\operatorname{Corr}(C_n,I_n)
=-\frac{1-p}{(1+p)\Gamma(1+p)\sqrt{\beta_pv_p}}.
\]
Finally the same exact covariance gives two distinct high-retention scales. For any fixed \(\lambda>0\), with probabilities restricted to \([0,1]\) for sufficiently large \(n\),
\[
\begin{aligned}
p_n=1-\lambda/\log n &\implies
\frac{\log n}{n}\operatorname{Cov}(C_n,I_n)
\longrightarrow-\frac{\lambda e^{-\lambda}}2,\\
p_n=1-\lambda/n &\implies
\operatorname{Cov}(C_n,I_n)\longrightarrow-\frac\lambda2.
\end{aligned}
\]

## Assumptions and scope

The recursive tree is generated sequentially: vertex \(1\) is the root; each vertex \(t+1\) independently chooses a uniformly random parent from \(\{1,\ldots,t\}\). Independently, its new edge is retained with probability \(p\) and deleted otherwise. All probabilities are unconditional over both the tree and edge retention. A singleton component is a vertex with no *retained* incident edge, not necessarily a leaf of the original tree. An empty product equals one, so the covariance formula also gives zero at \(n=1\). Gamma quotients below assume \(0<p<1\); the endpoint claims follow from the finite products.

## Proof

Let \(\mathcal F_t\) contain the first \(t\) parents and edge states. Let \(A_{t+1}\) indicate retention of the new edge and \(U_{t+1}\) be its parent. Set \(J_t=\mathbf 1_{\{C_t=1\}}\). Increments of the two counts obey
\[
\Delta C_t=A_{t+1}\mathbf1_{\{U_{t+1}\text{ lies in the root component}\}},
\qquad
\Delta I_t=1-A_{t+1}-A_{t+1}\mathbf1_{\{U_{t+1}\text{ is isolated}\}}.
\]
The only possible vertex that is simultaneously isolated and in the root component is the root, and that can occur exactly when \(C_t=1\). Consequently the following are exact conditional expectations:
\[
\begin{aligned}
\mathbb E[\Delta C_t\mid\mathcal F_t]&=pC_t/t,\\
\mathbb E[\Delta I_t\mid\mathcal F_t]&=1-p-pI_t/t,\\
\mathbb E[\Delta C_t\Delta I_t\mid\mathcal F_t]&=-pJ_t/t.
\end{aligned}
\]
The terms containing \(C_tI_t\) cancel when expanding the product:
\[
\mathbb E[C_{t+1}I_{t+1}\mid\mathcal F_t]
=C_tI_t+(1-p)C_t-pJ_t/t.\tag{1}
\]
The first count has mean \(a_t\). Since the root component remains a singleton exactly when no newcomer has yet retained an edge to the root, \(\mathbb EJ_t=u_t\). The singleton count has mean \(b_t=\mathbb EI_t\), satisfying
\[
b_{t+1}=(1-p/t)b_t+1-p,\qquad b_1=1,
\]
so direct substitution gives
\[
b_t=\frac{(1-p)t+2p\,u_t}{1+p}.\tag{2}
\]
Write \(m_t=\mathbb E[C_tI_t]\). Taking expectations of (1) and telescoping,
\[
m_n=1+(1-p)\sum_{t=1}^{n-1}a_t-p\sum_{t=1}^{n-1}u_t/t.
\]
The product recurrences imply
\[
\sum_{t=1}^{n-1}a_t=\frac{(n-1)a_n}{1+p},
\qquad
p\sum_{t=1}^{n-1}\frac{u_t}{t}=1-u_n.
\]
Thus the displayed mixed moment follows; subtracting \(a_nb_n\) using (2) yields the boxed covariance.

For \(0<p<1\) and \(n\ge2\), one has \(u_n\le1-p\) and \(a_n\ge1+p\). Therefore \((1+p)u_n-(1-p)a_n\le0\), while \(-2pa_nu_n<0\), proving strict negativity. At either endpoint one of the two counts is deterministic.

For the asymptotics, the gamma-product identities are
\[
a_n=\frac{\Gamma(n+p)}{\Gamma(n)\Gamma(1+p)},\qquad
u_n=\frac{\Gamma(n-p)}{\Gamma(n)\Gamma(1-p)}.
\]
For fixed \(0<p<1\), the standard gamma-ratio estimate gives \(a_n=n^p/\Gamma(1+p)+O(n^{p-1})\), \(u_n=n^{-p}/\Gamma(1-p)+O(n^{-p-1})\), and \(a_nu_n=1/[\Gamma(1+p)\Gamma(1-p)]+O(n^{-1})\). Euler's reflection identity \(\Gamma(1+p)\Gamma(1-p)=\pi p/\sin(\pi p)\) proves the two-term expansion.

For completeness, the variances needed for the correlation limit follow from the same growth process, not from an independence assumption. Let \(f_n=\prod_{t=1}^{n-1}(1+2p/t)\). Since \(\Delta C_t\) is conditionally Bernoulli with success probability \(pC_t/t\), the second-moment recursion gives
\[
\mathbb E C_n^2=2f_n-a_n,
\qquad
\operatorname{Var}(C_n)=2f_n-a_n-a_n^2
\sim v_pn^{2p}.
\]
The limiting coefficient \(v_p\) is positive because \(\Gamma(1+2p)/\Gamma(1+p)^2\) is strictly increasing from one to two as \(p\) runs from zero to one (differentiate its logarithm using the increasing digamma function).

Let \(V_t=\operatorname{Var}(I_t)\). Conditional on \(I_t=i\), the change in \(I_t\) equals \(1\), \(-1\), or \(0\), with respective probabilities \(1-p\), \(pi/t\), and \(p(1-i/t)\). The law of total variance gives
\[
V_{t+1}=\left(1-\frac{2p}{t}\right)V_t
+p(1-p)+\frac{p(3-2p)b_t}{t}-\frac{p^2b_t^2}{t^2}.
\]
As \(b_t/t\to(1-p)/(1+p)\), the additive forcing converges to \(2p(1-p)(p+2)/(1+p)^2\). Writing \(w_t=V_t/t\) and \(q_t\) for the displayed additive forcing gives \(w_{t+1}=(1-(1+2p)/(t+1))w_t+q_t/(t+1)\), with \(q_t\to q=2p(1-p)(p+2)/(1+p)^2\). Put \(b=q/(1+2p)\). Then \(w_{t+1}-b=(1-(1+2p)/(t+1))(w_t-b)+(q_t-q)/(t+1)\). From some finite index onward the first coefficient lies in \([0,1)\); iteration shows that the initial discrepancy decays to zero and that a forcing error eventually bounded by any \(\varepsilon>0\) contributes at most \(\varepsilon/(1+2p)\). Thus \(V_n/n\to\beta_p\). Combining the covariance and the two positive variance limits proves the correlation result.

For the last two limits apply the gamma-ratio estimate uniformly for retention parameters approaching one. When \(p_n=1-\lambda/\log n\), one has \(a_n\sim ne^{-\lambda}\), \(u_n=O((n\log n)^{-1})\), and the first covariance term involving \((1-p_n)a_n\) dominates. When \(p_n=1-\lambda/n\), \(a_n/n\to1\) and \(u_n=O(n^{-2})\), yielding the stated finite limit. The estimates hold for each fixed positive \(\lambda\).

## Verification

Run `python3 verify.py` from this directory. It checks 4,425 exact rational identities, comparing the closed products to independently propagated moment recurrences through size 80 and enumerating *all* parent assignments and edge-retention masks through size seven for three rational probabilities. No finite enumeration is used to claim an infinite theorem. The proof above supplies the all-size identity, strict sign, and limits.

## Relationship to prior work

Baur's 2014 preprint studies Bernoulli percolation on random recursive trees and the limiting tree of cluster sizes, principally in regimes with retention approaching one. Kürsten's 2015 preprint records separate finite formulas for expected root-cluster size, root singleton probability, expected total singleton count (Equation 38), and a second root-cluster moment (Equation 44). These established marginals agree with the intermediate identities here, but do not determine the mixed moment \(\mathbb E[C_nI_n]\) or its covariance. Kürsten's other mixed moment concerns the *numbers of vertices in first-generation child clusters*, not singleton components across every generation. The new argument identifies the exact conditional product cancellation and obtains the two-scale dependence law from it. The earlier percolation results, and an established root-degree/root-cluster covariance result, do not give the displayed identities by their stated conclusions. Historical implicit coverage by a broader cluster-enumeration identity has not been excluded conclusively.

## Limitations

This is a result about a two-variable moment, not a characterization of the complete joint distribution or a stochastic ordering. Correlation asymptotics are claimed only for fixed \(0<p<1\); the two approaching-one regimes concern covariance. The exact formulas are finite-size identities, but the novelty comparison remains limited by the inspected literature and indexed records. No independent audit has been performed.

## References

- E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508, first public version July 9, 2014. https://arxiv.org/abs/1407.2508
- R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275, first public version December 16, 2015. https://arxiv.org/abs/1512.05275
