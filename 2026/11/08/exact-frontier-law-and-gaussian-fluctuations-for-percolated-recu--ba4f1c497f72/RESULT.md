# Exact frontier law and Gaussian fluctuations for percolated recursive trees

## Finding

**Theorem.** Let \(0<p<1\), put \(q=1-p\), and grow a uniform random recursive tree on vertices \(1,2,\ldots,n\). Independently retain each parent edge with probability \(p\). Let \(C_n\) be the number of vertices connected to root \(1\) by retained edges, and let \(B_n\) be the number of **deleted original-tree edges with exactly one endpoint in this root component**. Thus \(B_n\) is also the number of percolation components immediately descended from the root component in the tree of components.

The entire finite-size joint law is specified by the ordinary generating function

\[
\mathcal G(z;u,v):=\sum_{n\ge1}\mathbb E[u^{C_n}v^{B_n}]z^{n-1}
=\frac{(1-qv)u(1-z)^{-qv}}{1-qv-pu+pu(1-z)^{1-qv}}.
\]

The formula is understood as a formal power series at \(z=0\) with coefficients polynomial in \(u,v\); at removable parameter singularities its continuous analytic limit is taken. For all \(n\ge1\), define

\[
a_n:=\frac{\Gamma(n+p)}{\Gamma(n)\Gamma(1+p)},\qquad
Z_n:=B_n-\frac qp(C_n-1).
\]

Then the following **exact finite-size** moment relations hold:

\[
\mathbb E C_n=a_n,\quad
\mathbb E B_n=\frac qp(a_n-1),\quad
\mathbb E Z_n=0,\quad
\mathbb E Z_n^2=\frac q{p^2}(a_n-1).
\]

Every integer \(k\ge2\) is eventually attained by \(C_n\), almost surely. At the first hitting time \(\tau_k=\inf\{n:C_n=k\}\), the frontier has the **exact negative-binomial law**

\[
\Pr(B_{\tau_k}=b)=\binom{k+b-2}{b}p^{k-1}q^b,
\qquad b=0,1,2,\ldots.
\]

There is a strictly positive, finite random variable \(W_p\) such that \(C_n/n^p\to W_p\) almost surely, and

\[
\frac{B_n}{C_n}\longrightarrow\frac qp\quad\text{almost surely}.
\]

If \(N\) is standard normal independent of \(W_p\), the two-scale fluctuation theorem is

\[
\left(\frac{C_n}{n^p},\frac{Z_n}{n^{p/2}}\right)
\Longrightarrow
\left(W_p,\frac{\sqrt{qW_p}}pN\right),
\qquad
\frac{Z_n}{\sqrt{C_n}}\Longrightarrow N\left(0,\frac q{p^2}\right).
\]

In particular, the deterministic normalization gives a Gaussian variance mixture, whereas normalization by the observed component size removes the mixture.

## Assumptions and scope

The tree is coupled across all sizes: at stage \(j+1\), vertex \(j+1\) chooses a uniform parent among \(1,\ldots,j\), independently of other choices, and its edge is retained by an independent Bernoulli \(p\) mark. Membership in the root component is hereditary along retained parent edges. A *frontier edge* is an original-tree parent edge from a root-component vertex to a child outside that component; its deleted status is permanent. The component graph formed by contracting retained-edge components is a tree, so each frontier edge corresponds to a distinct immediate child component. The theorem fixes \(p\) independently of \(n\). All distributional assertions use this joint infinite-growth coupling.

## Proof

### Exact Markov transitions and generating function

Conditionally on the tree and percolation marks through stage \(n\), a new vertex has its parent in the root component with probability \(C_n/n\). Hence the state \((C_n,B_n)=(c,b)\) moves to \((c+1,b)\), \((c,b+1)\), or remains \((c,b)\), with respective probabilities

\[
\frac{pc}{n},\qquad \frac{qc}{n},\qquad 1-\frac cn.
\]

Let \(P_n(u,v)=\mathbb E[u^{C_n}v^{B_n}]\), so \(P_1=u\). The transition rule gives the exact differential recurrence

\[
n(P_{n+1}-P_n)
=[p(u-1)+q(v-1)]u\,\partial_uP_n.
\]

Summing with weights \(z^{n-1}\), the ordinary generating function \(\mathcal G=\sum_{n\ge1}P_nz^{n-1}\) therefore solves

\[
(1-z)\partial_z\mathcal G-\mathcal G
=[pu+qv-1]u\partial_u\mathcal G,
\qquad \mathcal G(0;u,v)=u.
\]

Set \(r=1-qv\). The method of characteristics, or direct substitution into the last equation and the initial condition, gives

\[
\mathcal G(z;u,v)=\frac{ru(1-z)^{r-1}}{r-pu+pu(1-z)^r},
\]

which is the claimed formula. Since the recurrence uniquely determines every polynomial \(P_n\) from \(P_1\), direct substitution and the boundary condition certify the solution as an identity of formal power series. The removable case \(r=0\) is assigned its formal limit.

### Exact moments and stopped frontier law

Write \(\mu_n=\mathbb EC_n\). The transition probabilities give \(\mu_{n+1}=(1+p/n)\mu_n\), with \(\mu_1=1\), yielding \(\mu_n=a_n\). Define \(Z_n=B_n-(q/p)(C_n-1)\), so \(Z_1=0\). Its increment is \(-q/p\) on a retained root-parent birth, \(+1\) on a deleted root-parent birth, and zero otherwise. Thus \(Z_n\) is a mean-zero martingale and

\[
\mathbb E[(Z_{n+1}-Z_n)^2\mid\mathcal F_n]
=\frac qp\frac{C_n}{n}.
\]

Taking expectations and using \(\mu_{n+1}-\mu_n=p\mu_n/n\) yields

\[
\mathbb E Z_n^2=\frac qp\sum_{j=1}^{n-1}\frac{\mu_j}{j}
=\frac q{p^2}(a_n-1).
\]

The same conditional transition gives \(\mathbb EB_n=(q/p)(a_n-1)\).

Enumerate only those birth times at which the parent belongs to the currently retained root component. At every such time the independent edge mark is retained with probability \(p\), regardless of the preceding history. These selected marks therefore form an independent Bernoulli \(p\) sequence. The root component hits size \(k\) at the \((k-1)\)-st retained mark, and \(B_{\tau_k}\) is precisely the number of deleted marks preceding it. Counting strings with \(k-2\) retained marks and \(b\) deleted marks before the final retained mark proves the negative-binomial mass function. Finiteness of \(\tau_k\) follows from the positive growth limit proved next.

### Positive component-size limit and frontier proportion

Embed the recursive tree in a continuous-time Yule tree: each existing vertex gives birth at rate one. The total population \(N(t)\) is a Yule process of rate one, and the root-retained population \(C(t)\) is a Yule process with per-capita rate \(p\) by independent thinning of births. The standard Yule martingale limits satisfy

\[
e^{-t}N(t)\longrightarrow V>0,
\qquad e^{-pt}C(t)\longrightarrow U>0
\quad\text{almost surely},
\]

where both limits are finite. The child of a uniform parent in discrete birth order reproduces exactly the recursively grown tree. If \(T_n\) is the time of the \(n\)-th total birth, \(N(T_n)=n\), so

\[
\frac{C_n}{n^p}
=\bigl(e^{-pT_n}C(T_n)\bigr)
\bigl(e^{T_n}/n\bigr)^p
\longrightarrow W_p:=U/V^p\in(0,\infty)
\quad\text{almost surely}.
\]

Let \(H_n\) be the total number of births up to stage \(n\) whose parent was in the root component. By the selected-mark representation, \(C_n-1\) equals the number of retained marks among the first \(H_n\), and \(B_n\) equals the number of deleted marks. Since \(H_n\ge C_n-1\to\infty\), the ordinary strong law for the independent marks implies \((C_n-1)/H_n\to p\) and \(B_n/H_n\to q\) almost surely. Division gives \(B_n/C_n\to q/p\).

### Joint Gaussian fluctuations

The predictable quadratic variation of the martingale is

\[
\langle Z\rangle_n=\frac qp\sum_{j=1}^{n-1}\frac{C_j}{j}.
\]

The preceding almost-sure size limit and the elementary estimate \(\sum_{j<n}j^{p-1}\sim n^p/p\) give

\[
\frac{\langle Z\rangle_n}{n^p}\longrightarrow
\frac{qW_p}{p^2}\quad\text{almost surely}.
\]

Every martingale increment is bounded in absolute value by \(\max\{1,q/p\}\); therefore the conditional Lindeberg condition at scale \(n^{p/2}\) holds identically for sufficiently large \(n\). The stable martingale central limit theorem for arrays with convergent predictable quadratic variation (applied to the increments \((Z_{j+1}-Z_j)/n^{p/2}\)) yields a normal variable independent of the terminal sigma-field, multiplied by the square root of the displayed random quadratic-variation limit. Since \(W_p\) is measurable with respect to that terminal field, it gives the asserted joint convergence. The continuous-mapping theorem and \(C_n/n^p\to W_p>0\) give the self-normalized limit. No Gaussian assertion is made at \(p=0\) or \(p=1\).

## Verification

`check_frontier.py` uses exact rational arithmetic to construct the independent two-dimensional Markov recursion and compare its moments, the original-tree enumeration for small orders, coefficient extraction from the closed generating function, and finite negative-binomial counting identities. Running `python3 check_frontier.py` produced **883 passing exact tests**. An optional independent Monte Carlo diagnostic at \(p=4/5\) checks only finite-size plausibility: it is not a proof of the asymptotic normal limit. The proof above covers all integer \(n\ge1\), every integer \(k\ge2\), and every fixed real \(0<p<1\); no finite enumeration substitutes for these quantifiers.

## Relationship to prior work

Baur (arXiv:1407.2508, July 9, 2014) already defines the generation-one cluster count and realizes the model through Yule neutral mutations, but studies a regime with retention approaching one and the *sizes* of descendant clusters; it does not state the fixed-retention frontier generating function, exact residual second moment, or Gaussian law. Desmarais, Holmgren and Wagner (arXiv:2110.15050, first posted October 28, 2021) establish the root-cluster size scaling law and investigate global coloured-tree observables. Their root-cluster theorem is used here as context, but the first-generation **number of adjacent components**, its exact joint generating function with root size, stopped negative-binomial law, and its Gaussian fluctuation are distinct observables. Kürsten (arXiv:1512.05275, December 16, 2015) computes the total **number of vertices** in first-generation child components and its moments; that is not the number of those components. Bansaye, Gu and Yuan (arXiv:2109.05760, September 13, 2021) analyze a different dynamic process with edge degradation after birth, fragmentation and isolation. Their active-cluster-size theorems do not directly yield the fixed-birth-mark frontier law above. These comparisons do not assert a literature-wide priority certification.

## Limitations

The result assumes homogeneous independent birth-edge retention on a uniform random recursive tree; it does not give a variance law for arbitrary attachment kernels or fixed-vertex-count graphs. The negative-binomial stopping identity extends as a marking argument to other growing-tree models only if every target size is attained and parent-choice events are predictable before independent edge marks. The centered Gaussian limit is a fixed-\(p\) theorem; it does not address varying retention probabilities, continuously decaying edges, or independent validation of historical priority.

## References

- E. Baur, *Percolation on random recursive trees*, arXiv:1407.2508v1 (July 9, 2014), https://arxiv.org/abs/1407.2508.
- C. Desmarais, C. Holmgren and S. Wagner, *Broadcasting induced colourings of random recursive trees and preferential attachment trees*, arXiv:2110.15050v1 (October 28, 2021), https://arxiv.org/abs/2110.15050.
- R. Kürsten, *Random Recursive Trees and the Elephant Random Walk*, arXiv:1512.05275v1 (December 16, 2015), https://arxiv.org/abs/1512.05275.
- V. Bansaye, C. Gu and L. Yuan, *A growth-fragmentation-isolation process on random recursive trees and contact tracing*, arXiv:2109.05760v1 (September 13, 2021), https://arxiv.org/abs/2109.05760.
- C. Gu and L. Yuan, *Size distribution of clusters in site-percolation on random recursive tree*, arXiv:2408.12515v1 (August 22, 2024), https://arxiv.org/abs/2408.12515 (related site-percolation model).
