# Sharp degree–birth-time frontier in uniformly recruited batch recursive trees

## Finding

Fix an integer \(m\ge2\). Begin with one root. At step \(t\ge1\), independently choose one of the \(1+m(t-1)\) existing vertices uniformly and attach \(m\) new leaf children to the chosen *recruiter*. After \(n\) steps there are \(1+mn\) vertices. Write \(R_n(v)\) for the number of times vertex \(v\) has been recruited and \(b(v)\in\{0,1,\ldots,n\}\) for its birth step. Thus its number of children is \(mR_n(v)\).

For \(0\le a\le1\), put
\[
H_n(a)=\max_{b(v)\le\lfloor n^a\rfloor}R_n(v),\qquad
u_m=1-\frac{m}{(m+1)\log(m+1)},\qquad x_m^*=\frac1{\log(m+1)}.
\]
Set \(x_m(0)=1/m\). For \(0<a<\nu_m\), let \(x_m(a)\) be the unique \(x>(1-a)/m\) solving
\[
x\log\frac{mx}{1-a}-x+\frac{1-a}{m}=a.
\]
For \(\nu_m\le a\le1\), set \(x_m(a)=x_m^*\). Then, for each fixed \(a\in[0,1]\),
\[
\boxed{\frac{H_n(a)}{\log n}\longrightarrow x_m(a)\quad\text{almost surely}.}
\]
In particular, with \(\Delta_n\) the maximum number of children,
\[
\boxed{\frac{\Delta_n}{\log n}\longrightarrow\frac{m}{\log(m+1)}\quad\text{almost surely}.}
\]
Let \(B_n\) be the smallest birth step among all maximizing vertices. Then
\[
\boxed{\frac{\log(1+B_n)}{\log n}\xrightarrow{\mathbb P}\nu_m.}
\]
For example, \(m=2\) yields asymptotic maximum-child coefficient \(2/\log3\) and peak-recruiter birth exponent \(1-2/(3\log3)\).

## Assumptions and scope

The integer \(m\ge2\) is fixed as \(n\to\infty\); recruiter selection is uniform among **individual vertices**, independent between steps. The \(m\) children added in a single step have a common parent and do not recruit until subsequent steps. Degrees in this statement are **numbers of children**, not undirected total degrees (which differ by at most one). At \(a=0\), the maximum ranges over the root and the \(m\) vertices born at the first recruitment step. The almost-sure assertions hold for each fixed \(a\); no claim of uniform almost-sure convergence over all real \(a\) is made. The birth-location assertion is in probability, not almost surely.

## Proof

**1. Exact recruiter-count laws.** For each vertex \(v\) born at step \(i=b(v)\), recruitment at time \(t\) is possible exactly for \(t>i\). These selection indicators are independent Bernoulli random variables, with success probabilities \(p_t=1/(1+m(t-1))\). Consequently
\[
R_n(v)\overset d=\sum_{t=i+1}^n\operatorname{Ber}\!\left(\frac1{1+m(t-1)}\right).
\]
For the root, \(i=0\), so its recruitment at the first step is certain. The Bernoulli sum has mean \(m^{-1}\log(n/\max\{i,1\})+O_m(1)\) and variance at most its mean. In particular, for every fixed vertex of birth step \(0\) or \(1\), the normalized recruiter count converges almost surely to \(1/m\), by the exponential Chernoff bound on geometric-time subsequences and monotonicity.

**2. Uniform logarithmic large deviations.** For fixed \(0\le u<1\), birth steps \(i\) within a fixed multiplicative factor of \(n^u\) have
\[
\log\mathbb E e^{\theta R_n(v)}=
\frac{1-u}{m}(e^\theta-1)\log n+O_{m,\theta}(1),
\]
where at \(u=0\) finitely old vertices are allowed. Indeed, expand \(\log(1+p_t(e^\theta-1))\); the sum of the quadratic errors is uniformly bounded. For \(x>(1-u)/m\), exponential tilting and Chernoff's inequality give
\[
\Pr\{R_n(v)\ge x\log n\}=n^{-I_u(x)+o(1)},\qquad
I_u(x)=x\log\frac{mx}{1-u}-x+\frac{1-u}{m}.
\]
For the lower bound, choose a tilt with tilted mean \((x+\epsilon)\log n\); its variance is \(O(\log n)\), so a tilted count exceeds \(x\log n\) with probability tending to one. Restrict the tilted count to the interval \( [x\log n,(x+2\epsilon)\log n]\), which has tilted probability tending to one, then reverse the change of measure and let \(\epsilon\downarrow0\). This argument also gives the required bounds uniformly on a fixed birth-exponent interval strictly below one. For an upper bound at arbitrarily recent birth times, use the same Chernoff expression with their smaller means, or simply use a sufficiently large fixed positive tilt.

**3. Negative correlation of distinct high-recruitment indicators.** Fix distinct vertices \(v,w\), their birth steps, and a threshold \(r\). Conditioning on the independent time-by-time recruitment indicators of \(v\), the possible indicators for \(w\) remain independent across time. At any time when both are eligible, the conditional chance of recruiting \(w\) is \(0\) if \(v\) was selected, and \(p_t/(1-p_t)\) if it was not; at times when only \(w\) is eligible the chance is unchanged. Thus the conditional probability of \(\{R_n(w)\ge r\}\) decreases coordinatewise as the indicators of \(v\) increase. The indicator \(\mathbf1_{\{R_n(v)\ge r\}}\) increases in these independent coordinates. The elementary product-measure covariance inequality for an increasing and a decreasing function therefore gives
\[
\operatorname{Cov}\!\left(\mathbf1_{\{R_n(v)\ge r\}},\mathbf1_{\{R_n(w)\ge r\}}\right)\le0.
\]
The deterministic root-only first recruitment causes no difficulty. Consequently, if \(Z\) counts vertices exceeding a common threshold in any deterministic birth cohort, then \(\operatorname{Var}Z\le\mathbb EZ\), so \(\Pr(Z=0)\le1/\mathbb EZ\) whenever \(\mathbb EZ>0\). This avoids any unproved independence assumption between vertices.

**4. The age–degree variational problem.** There are \(\Theta(n^u)\) vertices born at steps in \([n^u/2,n^u]\), for \(0<u\le1\). For a target normalized recruiter count \(x\), the exponent of the expected number of successful vertices in such a cohort is
\[
\Phi(u,x)=u-I_u(x)=u-x\log\frac{mx}{1-u}+x-\frac{1-u}{m}.
\]
For fixed \(x>0\),
\[
\partial_u\Phi(u,x)=\frac{m+1}{m}-\frac{x}{1-u},\qquad
\partial_{uu}\Phi(u,x)=-\frac{x}{(1-u)^2}<0.
\]
Its unique interior maximizer is \(u=1-mx/(m+1)\), and substitution there yields \(\max_u\Phi(u,x)=1-x\log(m+1)\), whenever that maximizer lies in \([0,1]\). Hence the global zero is \(x=x_m^*\), attained at the unique exponent \(u=\nu_m\). Restricting to \(0\le u\le a<\nu_m\) forces the optimizing exponent to the boundary \(u=a\) at its zero. This produces the displayed equation defining \(x_m(a)\); it has a unique solution above its cohort mean because the rate function is strictly increasing there. For \(a\ge\nu_m\), the unrestricted optimizer is accessible and the frontier saturates. When \(a=0\), finitely many old vertices give the separate endpoint \(1/m\).

**5. Almost-sure frontiers.** Fix \(a\) and \(x>x_m(a)\). Partition the permissible birth steps into finitely many bins of the form \(n^u\le i<n^{u+\delta}\), and apply the preceding uniform Chernoff upper bound in each bin. The strict negativity of \(\max_{u\le a}\Phi(u,x)\), and a sufficiently small mesh \(\delta\), give \(\Pr(H_n(a)\ge x\log n)\le Cn^{-c}\) for constants \(C,c>0\). The finitely many oldest steps and the last bin are included using the same Chernoff estimate. The probabilities are summable along \(n_j=\lceil e^j\rceil\).

For \(0<a\le1\) and \(x<x_m(a)\), choose a birth exponent \(0<u\le a\) with \(x>(1-u)/m\) and \(\Phi(u,x)>0\), taking \(u\) just below \(a\) when needed. The indicated birth cohort contains \(\Theta(n^u)\) vertices, and the tilted lower bound gives \(\mathbb EZ\ge n^c\) for some \(c>0\). Part 3 then yields \(\Pr(H_n(a)<x\log n)\le n^{-c}\), again summable along \(n_j\). If \(x\) is below the mean of all old vertices, their individual concentration already gives the lower bound; this removes the temporary \(x>(1-u)/m\) restriction. At \(a=0\) use Part 1. Borel–Cantelli gives convergence along \(n_j\), and monotonicity of \(H_n(a)\) in \(n\), together with \(\log n_{j+1}/\log n_j\to1\), gives almost-sure convergence for all \(n\).

**6. Birth time of a maximizing vertex.** At \(x=x_m^*\), \(\Phi(u,x)\) has its *unique* zero at \(u=\nu_m\) and is strictly negative at every other exponent. For any fixed \(\delta>0\), compactness and continuity allow a sufficiently small \(\epsilon>0\) such that \(\Phi(u,x_m^*-\epsilon)<0\) for all birth exponents outside \((\nu_m-\delta,\nu_m+\delta)\). Apply the same finite-bin union-Chernoff argument to show that, with probability tending to one, no vertex outside that birth range has recruitment count at least \((x_m^*-\epsilon)\log n\). The global maximum exceeds that threshold with probability tending to one by Part 5. Every maximizing vertex is therefore inside the indicated birth range with probability tending to one; in particular the smallest maximizing birth time has the asserted exponent limit in probability.

## Verification

The standalone science-only script `verify_max_degree.py` checks finite-time marginal and two-vertex joint laws exactly with rational arithmetic for \(1\le m\le4\), \(2\le n\le10\), all ordered distinct birth steps, and all tested upper-tail thresholds. It verifies normalization, exact marginals, and pairwise negative upper-tail covariance. It separately checks the analytic saddle-point and frontier identities numerically for \(1\le m\le20\). Reproduce with `python3 verify_max_degree.py`; the observed result was `PASS: 11030 exact rational and numerical assertions`. Finite checks are diagnostic, not a proof of the asymptotic theorem; Parts 1–6 are the proof.

## Relationship to prior work

Bhutani, Kalpathy, Lesny, Mahmoud and Neininger (2026, arXiv:2609.33636, originally public September 27) define this exact simultaneous-leaf-growth process, and their publicly accessible abstract describes distances, height, Wiener index and internal path length. The full source manuscript was not available for a complete textual comparison, so overlap with an uninspected appendix or result remains possible. The ordinary recursive-tree special case \(m=1\) has known maximum-degree and high-degree-location theory, which is not claimed as new. Desmarais and Holmgren's general hooking-network work addresses degree frequencies of block-growth trees, whereas Bhutani, Kalpathy and Mahmoud's earlier *Degrees in random m-ary hooking networks* uses a capped number of hookings per available position. Work on weighted recursive graphs with multiple parent edges per single arriving vertex, including Lodewijks, is not the same as recruiting one vertex to receive several fresh children. The present statement concerns the full age-restricted maximum curve and its exact birth-time saddle for the simultaneous-leaf process.

## Limitations

This is a first self-review, not an independent audit. Priority is provisional: the full 2026 source text was inaccessible during this investigation, and unrecognized equivalent statements in earlier general block-tree theory remain possible. The theorem fixes \(m\) and does not determine second-order fluctuations, extremal multiplicities, or almost-sure localization of the maximizing birth step. Some finite checks include \(m=1\) to recover known special cases. They do not certify infinite-population conclusions.

## References

1. K. Bhutani, R. Kalpathy, F. Lesny, H. Mahmoud and R. Neininger, *Distances in m-ary recursive trees*, arXiv:2609.33636 (first public September 27, 2026). https://arxiv.org/abs/2609.33636
2. A. Desmarais and C. Holmgren, *Normal limit laws for vertex degrees in randomly grown hooking networks and bipolar networks*, Electronic Journal of Combinatorics 27 (2020), P2.45. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i2p45/pdf/
3. K. Bhutani, R. Kalpathy and H. Mahmoud, *Degrees in random m-ary hooking networks* (2023). https://compositionality.episciences.org/13525/pdf
4. B. Lodewijks, *Location of high-degree vertices in weighted recursive graphs with bounded random weights*, Advances in Applied Probability (2024). https://www.cambridge.org/core/journals/advances-in-applied-probability/article/location-of-highdegree-vertices-in-weighted-recursive-graphs-with-bounded-random-weights/3D398DDDA00010338C15B9A3F8C6A6FE
5. W. Goh and E. Schmutz, *Limit distribution for the maximum degree of a random recursive tree*, Journal of Computational and Applied Mathematics 142 (2002), 61–82. https://doi.org/10.1016/S0377-0427(01)00460-5
