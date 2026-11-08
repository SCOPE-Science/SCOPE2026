# Lambert-\(W\) entropy-optimal resetting on complete graphs

## Finding

Let \(n\ge3\), put \(m=n-1\), and consider the simple random walk on the loopless complete graph \(K_n\). At each discrete time, independently of the past, reset to a fixed vertex \(r\) with probability \(\gamma\in[0,1]\), or make a uniformly chosen ordinary neighbor step with probability \(1-\gamma\). The entropy rate \(h_m(\gamma)\) is that of the **observed vertex sequence**, in natural logarithm units; reset indicators are not included in observations. Define \(p=1-\gamma\), \(u=1+(m-1)\gamma\), and \(d=m+1-\gamma\), with \(0\log0=0\). Then

\[
h_m(\gamma)=\log m+\frac{-u\gamma\log(m\gamma)-mp\log p-pu\log u}{d}.
\]

For every \(m\ge2\), the entropy rate attains a maximum strictly above \(\log m\) and strictly below \(\log(m+1)\), and every maximizer is in \((0,1)\). Let \(W(m)>0\) be the unique solution of \(W(m)e^{W(m)}=m\). For **every** maximizing choice \(\gamma_m\), as \(m\to\infty\),

\[
 m^2\gamma_m=W(m)+o(1),\qquad
 m^3\left(\max_{0\le\gamma\le1}h_m(\gamma)-\log m\right)=\tfrac12W(m)^2+W(m)+o(1).
\]

In particular, the optimal resetting probability has order \(\log m/m^2\), and the optimal entropy improvement has order \((\log m)^2/m^3\). Uniqueness of finite-size maximizers is **not** asserted.

## Assumptions and scope

The graph has \(n\ge3\) vertices and no loops. The ordinary step is uniform among its \(m\) distinct neighbors; a reset to \(r\) is an **alternative transition mechanism**, not a separate observed symbol. Thus a reset and an ordinary step can result in the same observed transition when the current vertex is adjacent to \(r\). The stochastic matrix is \(P_{ij}^{(\gamma)}=(1-\gamma)\mathbf1_{i\ne j}/m+\gamma\mathbf1_{j=r}\). All logarithms are natural. For \(0<\gamma<1\) the chain is irreducible and aperiodic; endpoint entropies are defined by continuity.

## Proof

**1. Exact stationary law and entropy.** Set \(p=1-\gamma\), \(u=1+(m-1)\gamma\), \(d=m+1-\gamma=u+mp\). For every \(i\ne r\), the probability of moving to \(r\) is \(u/m\), while the transition from \(r\) to \(i\) has probability \(p/m\). Detailed balance and normalization give

\[
 \pi_\gamma(r)=\frac{u}{d},\qquad
 \pi_\gamma(i)=\frac{p}{d}\quad(i\ne r).
\]

The outgoing row at \(r\) consists of one probability \(\gamma\) and \(m\) probabilities \(p/m\). Each other row consists of one probability \(u/m\), \(m-1\) probabilities \(p/m\), and a zero diagonal entry. Its entropy therefore equals

\[
 H_r=-\gamma\log\gamma-p\log(p/m),\qquad
 H_o=-\frac um\log(u/m)-(m-1)\frac pm\log(p/m).
\]

Using \(h_m=(uH_r+mpH_o)/d\), with \(u+(m-1)p=m\), gives the displayed exact formula. This derivation uses the entropy of the **merged destination probabilities**; a reset and an ordinary move to \(r\) are observationally indistinguishable.

**2. Strict interior improvement and upper bound.** The no-reset process has \(h_m(0)=\log m\), and full resetting has \(h_m(1)=0\). For fixed \(m\), the numerator of \(h_m(\gamma)-\log m\) is \(-\gamma\log(m\gamma)+O_m(\gamma)\) as \(\gamma\downarrow0\), hence is positive for sufficiently small positive \(\gamma\). An interior maximum therefore exists. For every \(0<\gamma<1\), each non-reset vertex has at most \(m\) possible successors and positive stationary mass, so its row entropy is at most \(\log m<\log(m+1)\), while the reset vertex has at most \(m+1\) successors. Thus \(h_m(\gamma)<\log(m+1)\); this also holds at both endpoints.

**3. Localization of all optimizers.** Let \(H_{\rm b}(\gamma)=-\gamma\log\gamma-p\log p\) be binary entropy, and put

\[
 B_m(\gamma)=H_{\rm b}(\gamma)-\gamma\log m,\qquad
 K_m(\gamma)=\frac{u\log u+(m-1)p\log p}{m}.
\]

Direct substitution gives \(h_m-\log m=(u B_m-mpK_m)/d\). Here \(K_m\ge0\) is the Kullback--Leibler divergence of the non-reset row from a uniform distribution on its \(m\) possible successors. It satisfies \(K_m(0)=K'_m(0)=0\) and

\[
 K_m''(\gamma)=\frac{m-1}{pu}.
\]

Since \(-(1-\gamma)\log(1-\gamma)\le\gamma\), \(B_m\le\gamma(1-\log(m\gamma))\). If \(h_m(\gamma)>\log m\), then \(B_m>0\), so \(\gamma<e/m\). In that range \(u\le1+e\), \(K_m(\gamma)\ge(m-1)\gamma^2/[2(1+e)]\) by integrating the lower bound on \(K_m''\). For all sufficiently large \(m\), also \(u/d\le(1+e)/m\) and \(mp/d\ge1/3\). Consequently, writing \(x=m^2\gamma\), whenever \(x\ge1\) and \(h_m(\gamma)>\log m\),

\[
 m^3(h_m(\gamma)-\log m)
 \le(1+e)x(1+\log m)-\frac{(m-1)x^2}{6m(1+e)}.
\]

For all sufficiently large \(m\) this is negative when \(x\ge200\log m\). Thus every global maximizing \(\gamma_m\) obeys \(0<m^2\gamma_m\le200\log m\) for sufficiently large \(m\).

**4. Uniform scaling analysis.** Write \(x=m^2\gamma\) and extend \(x\log x\) continuously as zero at zero. Taylor expansion of \(\log(1-\gamma)\) and \(\log(1+(m-1)\gamma)\) in the exact formula, with uniform remainder estimates for \(0\le x\le200\log m\), yields

\[
 \sup_{0\le x\le200\log m}
 \left|m^3\bigl(h_m(x/m^2)-\log m\bigr)-f_m(x)\right|
 =O\!\left(\frac{(\log m)^4}{m}\right)=o(1),
\quad f_m(x)=x\bigl(1+\log m-\log x\bigr)-\frac{x^2}{2}.
\]

For completeness, the numerator before division by \(d\) equals \(\gamma(1-\log(m\gamma))-(m^2/2)\gamma^2+O(m\gamma^2[1+|\log(m\gamma)|]+m^3\gamma^3)\). Multiplication by \(m^3/d\) gives the stated uniform remainder: \(x^2|\log x|\) remains bounded near zero and is at most polylogarithmic on the stated range.

For \(x>0\), \(f'_m(x)=\log(m/x)-x\) and \(f''_m(x)=-1/x-1\le-1\). Its unique maximum occurs at \(x=W(m)\), with value \(f_m(W(m))=W(m)+W(m)^2/2\). For large \(m\), \(W(m)\) belongs to the localized interval. If \(x_m=m^2\gamma_m\) maximizes the exact entropy, uniform approximation and strong concavity imply

\[
 \tfrac12(x_m-W(m))^2\le f_m(W(m))-f_m(x_m)=o(1).
\]

Hence \(x_m=W(m)+o(1)\); the asymptotic optimal gain follows from the same uniform approximation.

## Verification

The accompanying standalone \(verify.py\) constructs the actual \(n\times n\) resetting transition matrices, calculates invariant distributions by iteration, and independently calculates row entropies. It checks 126 graph/parameter combinations with \(3\le n\le20\), including the exact formula, detailed-balance stationary law, and the merged-transition entropy deficit. The finite tests check algebra and implementation; the global asymptotic conclusion rests on the proof above, not on finite sampling. Run with \(python verify.py\) using the Python standard library.

## Relationship to prior work

Wang and Chen (2022) give the general reset transition matrix and stationary-resolvent formalism, and an entropy formula for regular networks based on treating a reset as an additional disjoint outcome. For the entropy of **observed vertex transitions**, this separation does not apply when a normal step can also reach the reset vertex. Their general transition-matrix relation is consistent with the exact formula above when the row probabilities are combined before taking entropy; their reported regular-graph optimum \(1/(m+1)\) and peak \(\log(m+1)\) are not the optimal observed-vertex values on \(K_{m+1}\). The new contribution is the all-size exact entropy formula together with the nontrivial all-maximizer Lambert-\(W\) scaling and optimal entropy gain. Riascos and Mateos (2021) supply general stationary-chain entropy methodology; Zelenkovski and collaborators (2023) analyze reset walks for first-passage optimization rather than the present entropy asymptotics.

## Limitations

Only fixed-target reset on the loopless unweighted clique is analyzed. The entropy of the pair (next vertex, reset indicator) is a different observable and has a different optimum. The theorem does not claim finite-size uniqueness of maximizers, monotonicity for arbitrary graphs, or an optimal reset scale on noncomplete regular graphs. Historical priority of this precise asymptotic awaits independent review.

## References

1. Y. Wang and H. Chen, *Entropy rate of random walks on complex networks under stochastic resetting*, arXiv:2208.05665, first submitted 2022-08-11; Phys. Rev. E 106, 054137 (2022). https://arxiv.org/abs/2208.05665
2. A. P. Riascos and J. L. Mateos, *Random walks on weighted networks: a survey of local and non-local dynamics*, Journal of Complex Networks 9, cnab032 (2021). https://academic.oup.com/comnet/article/9/5/cnab032/6386451
3. K. Zelenkovski, T. Sandev, R. Metzler, L. Kocarev, and L. Basnarkov, *Random Walks on Networks with Centrality-Based Stochastic Resetting*, Entropy 25, 293 (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC9955709/
