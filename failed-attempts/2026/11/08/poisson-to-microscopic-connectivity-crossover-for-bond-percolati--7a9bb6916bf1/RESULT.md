# Poisson-to-microscopic connectivity crossover for bond percolation on wheels

## Finding

Let \(W_{n+1}=K_1\vee C_n\), \(n\ge3\), with each rim edge open independently with probability \(p\in[0,1]\) and each hub spoke open independently with probability \(q\in[0,1]\). Write \(R_n(p,q)\) for the probability that the open graph is connected. Define
\[
s=2p+q-2pq,\qquad u=p^2(1-q),\qquad r_\pm=\frac{s\pm\sqrt{s^2-4u}}2.
\]
For every \(n\ge3\), the exact two-type reliability is
\[
R_n(p,q)=r_+^n+r_-^n-2[p(1-q)]^n. \tag{1}
\]

Fix \(\lambda,\mu\ge0\). For all sufficiently large \(n\), set \(p_n=1-\lambda/n\) and \(q_n=\mu/n\). Let \(X_n\) be the fraction of the \(n\) rim vertices connected by open paths to the hub. Then \(X_n\Rightarrow X_{\lambda,\mu}\), where \(X_{\lambda,\mu}\) is the fraction of the unit circle occupied by components of a rate-\(\lambda\) Poisson cut process that contain at least one mark of an independent rate-\(\mu\) Poisson spoke process. When there are zero or one cuts, the circle is regarded as a single component.

Writing \(\Delta=\sqrt{\mu^2+4\lambda\mu}\), the exact limiting full-connectivity probability is
\[
F(\lambda,\mu):=\lim_{n\to\infty}R_n(p_n,q_n)
=e^{-(\lambda+\mu)}\left(e^{(\mu+\Delta)/2}+e^{(\mu-\Delta)/2}-2\right). \tag{2}
\]
For \(\lambda+\mu>0\), the limiting mean reached fraction is
\[
\mathbb E X_{\lambda,\mu}=1-e^{-(\lambda+\mu)}(1+\lambda)
-\frac{\lambda^2}{(\lambda+\mu)^2}\left[1-(1+\lambda+\mu)e^{-(\lambda+\mu)}\right]. \tag{3}
\]
At \(\lambda=\mu=0\), this mean is \(0\). The limiting law has atoms
\[
\Pr(X_{\lambda,\mu}=0)=e^{-\mu},\qquad
\Pr(X_{\lambda,\mu}=1)=F(\lambda,\mu). \tag{4}
\]
For strictly positive \(\lambda,\mu\), there is also positive mass in \((0,1)\).

A further, nested connectivity transition occurs as \(\lambda\to\infty\): for every sequence \(\mu=\mu(\lambda)\ge0\),
\[
\frac{\mu}{\lambda^2}\to\alpha\in[0,\infty]
\quad\Longrightarrow\quad
F(\lambda,\mu)\to
\begin{cases}0,&\alpha=0,\\e^{-1/\alpha},&0<\alpha<\infty,\\1,&\alpha=\infty.\end{cases} \tag{5}
\]
For \(0<\alpha<\infty\), simultaneously \(\mathbb E X_{\lambda,\mu}\to1\), even though full connectivity has limiting probability strictly between zero and one. This separates macroscopic rim coverage from all-terminal network reliability.

## Assumptions and scope

Every vertex is operational. All \(2n\) edge states are independent, and rim versus spoke edges may have different retention probabilities. The limit \(n\to\infty\) is taken with fixed finite \(\lambda,\mu\); equation (5) is a subsequent \(\lambda\to\infty\) limit of the already-established continuum law, not an unproved uniform simultaneous scaling regime. A spoke at one vertex joins its entire rim component to the hub. Normalizations count only the \(n\) rim vertices in \(X_n\).

## Proof

**Exact finite reliability.** Put \(d=1-p\), \(v=1-q\). If there are no failed rim edges, the rim is one component, and the probability the hub attaches is \(p^n(1-v^n)\). If \(k\ge1\) rim edges fail, the rim breaks into \(k\) cyclically ordered path components of positive vertex lengths \(\ell_1,\ldots,\ell_k\) summing to \(n\). Connectivity is equivalent to having at least one retained spoke in every component. The weighted one-component generating function is
\[
A(z)=d\sum_{\ell\ge1}p^{\ell-1}(1-v^\ell)z^\ell
=\frac{dqz}{(1-pz)(1-pvz)}.
\]
Choosing a marked cut and correcting for the \(k\) possible marked cuts gives exactly
\[
R_n(p,q)=p^n(1-v^n)+n[z^n]\sum_{k\ge1}\frac{A(z)^k}{k}.
\]
The identity
\[
1-A(z)=\frac{(1-r_+z)(1-r_-z)}{(1-pz)(1-pvz)}
\]
then reduces the coefficient of \(-\log(1-A(z))\) to \(r_+^n+r_-^n-p^n-(pv)^n\), proving (1). This formal power-series derivation remains valid at \(p,q\in\{0,1\}\) by polynomial continuity.

**Finite mean reachability.** Let \(S_n\) be the size of the open rim component of a uniformly selected rim vertex, ignoring spokes. For \(1\le j<n\), exactly \(j\) cyclic intervals of length \(j\) contain that vertex, giving
\[
\Pr(S_n=j)=jd^2p^{j-1};\qquad
\Pr(S_n=n)=p^n+ndp^{n-1}.
\]
Conditional on \(S_n=j\), the rim vertex is not connected to the hub precisely when all \(j\) spokes fail. Exchangeability thus gives the exact formula
\[
\mathbb E X_n=1-d^2\sum_{j=1}^{n-1}jp^{j-1}v^j-(p^n+ndp^{n-1})v^n. \tag{6}
\]

**Circle limit.** Under the prescribed scaling, the processes of failed rim edges and retained spokes, positioned at their normalized cyclic locations, converge jointly to independent homogeneous Poisson point processes on the unit circle, with mean counts \(\lambda\) and \(\mu\). Their points are almost surely distinct. The total length of cut intervals with at least one spoke is a continuity functional at these realizations; finite-grid versus arc-length discrepancy is at most the number of cuts divided by \(n\). Hence \(X_n\Rightarrow X_{\lambda,\mu}\); boundedness yields convergence of its mean.

If there are at least two cuts, the arc lengths conditional on their count are uniformly Dirichlet on the simplex. The interval containing a uniform rim point has length \(S\) with density \(\lambda^2 s e^{-\lambda s}\) for \(0<s<1\), and an atom \(e^{-\lambda}(1+\lambda)\) at \(s=1\). Indeed, conditional on \(k\ge2\) cuts, its density is the beta density \(k(k-1)s(1-s)^{k-2}\); mixing over a Poisson count sums to the stated density. Thus \(S\) has the distribution of \(\min(1,G)\) for a Gamma variable \(G\) of shape two and rate \(\lambda\), with the natural degenerate interpretation for \(\lambda=0\). Since a length-\(s\) interval receives no spoke with probability \(e^{-\mu s}\), evaluating \(\mathbb E[e^{-\mu S}]\) gives (3).

**All-terminal limit.** Full connectivity means there is at least one spoke and that every cyclic interval between successive cuts contains at least one spoke. Superpose the two limiting point processes. Conditional on a total of \(j\ge1\) points, ordered cyclically, every assignment of a cut or spoke to these positions has relative Poisson weight \(\lambda\) or \(\mu\). Valid words have no two consecutive cuts, with cyclic adjacency; a single cut and no spoke is invalid, and the empty word is invalid. The weighted cyclic-word sum is \(\operatorname{tr}(T^j)\), for
\[
T=\begin{pmatrix}\mu&\lambda\\\mu&0\end{pmatrix}.
\]
Summing \(j\ge1\) with the Poisson factor gives
\[
F=e^{-(\lambda+\mu)}\bigl(\operatorname{tr}(e^T)-2\bigr),
\]
whose eigenvalues yield (2). Independently, expanding the roots \(r_\pm\) in (1) to first order in \(1/n\) gives the same expression. No fixed-size simulation is used to infer this limit.

**Microscopic-gap crossover.** For \(\lambda+\mu>0\), rewrite (2) exactly as
\[
F(\lambda,\mu)=
\exp\left(-\frac{2\lambda^2}{\Delta+\mu+2\lambda}\right)
+e^{-\lambda-\mu/2-\Delta/2}-2e^{-\lambda-\mu}.
\]
The last two terms vanish as \(\lambda\to\infty\). If \(\mu/\lambda^2\to\alpha\in(0,\infty)\), then \((\Delta+\mu+2\lambda)/\lambda^2\to2\alpha\). If this ratio tends to zero or infinity the first term tends respectively to zero or one, proving (5). For finite positive \(\alpha\), the disconnected fraction in (3) is bounded by \(e^{-(\lambda+\mu)}(1+\lambda)+\lambda^2/(\lambda+\mu)^2\), which tends to zero.

## Verification

Run `python3 verify.py` with the Python standard library. The program independently enumerates all retained-edge configurations for \(3\le n\le7\) at rational retention probabilities, comparing union-find all-terminal connectivity and hub-root reachability against (1) and (6) as exact rational numbers. It also checks finite-to-continuum scaling, singular crossover values and seeded Poisson-circle Monte Carlo consistency. The recorded replay produced `PASS 36 checks`. The exhaustive computations cover only those finite sizes; the general and asymptotic results follow from the proofs above.

## Relationship to prior work

Newman and Watts (arXiv:cond-mat/9904419, first publicly available April 28, 1999) examined distances, scaling and approximate site-percolation behavior on a ring with randomly placed *pairwise* shortcuts. Moore and Newman (arXiv:cond-mat/0001393, January 26, 2000) subsequently obtained exact outbreak distributions for random-endpoint small-world models at fixed bond density. These models do not impose a single common hub on every shortcut, nor report the joint Poisson-cut/Poisson-spoke wheel window and its nested \(\lambda^2\) connectivity scale. Their one-dimensional local-cluster distribution is an important antecedent of the tagged-component calculation here.

Classical wheel reliability polynomials and their single-parameter recurrences are already tabulated (MathWorld, *Reliability Polynomial*). Equation (1) is used as an independently established finite bridge, not presented as an independently novel single-parameter reliability polynomial. Tanguy's arXiv:cs/0612143 gives exact transfer formulas for simple ladder networks, which do not have the wheel's common-hub architecture. The proposed new mathematical content is the explicitly identified two-parameter wheel scaling law, distributional hub-reachability limit and distinct microscopic all-terminal scale.

## Limitations

The result does not give the thermodynamic phase transition for an infinite fixed-density small-world network, nor uniform error bounds when \(\lambda\) or \(\mu\) grows jointly with \(n\). The continuum description specifies the full limiting law constructively but not a closed elementary density for the mass in \((0,1)\). Claims of historical originality remain provisional against unindexed wheel-specific reliability literature and possible equivalent marked-circle arguments. No independent scientific validation has been performed.

## References

1. M. E. J. Newman and D. J. Watts, *Scaling and percolation in the small-world network model*, arXiv:cond-mat/9904419 (first public version April 28, 1999), https://arxiv.org/abs/cond-mat/9904419.
2. C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, arXiv:cond-mat/0001393 (first public version January 26, 2000), https://arxiv.org/abs/cond-mat/0001393.
3. C. Tanguy, *Exact solutions for the two- and all-terminal reliabilities of a simple ladder network*, arXiv:cs/0612143 (December 28, 2006), https://arxiv.org/html/cs/0612143v1.
4. E. W. Weisstein, *Reliability Polynomial*, MathWorld, https://mathworld.wolfram.com/ReliabilityPolynomial.html (historical univariate wheel recurrence).
