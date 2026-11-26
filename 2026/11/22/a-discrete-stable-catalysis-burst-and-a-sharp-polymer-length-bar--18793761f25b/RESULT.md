# A Sibuya burst law for the first short incidences in Pareto autocatalysis

## Finding

In a forward-ligation network on abstract words, the first short-word to short-reaction incidences appear in a logarithmically shifted length window. At that window, catalytic incidences arrive in Sibuya-distributed groups, and their number has a discrete-stable limit along subsequences tracking the integer cutoff. This is a sharp threshold for **incidences**, not for the shortest RAF. The RAF threshold from prior work, applied to the induced short subsystem, occurs at a strictly larger linear length scale.

Fix alphabet size \(\kappa\ge2\), fixed food length \(t\ge1\), Pareto index \(0<\alpha<1\), and \(0<\beta<(1-\alpha)/\alpha\). Let \(X_m\) consist of the nonempty words of length at most \(m\), with \(N_m=|X_m|\). The \(R_m\) forward ligations in this subsystem are the ordered splits \((u,v;uv)\) with \(|uv|\le m\). At ambient length \(n\), let \(\lambda_n=N_n^{-\beta}\). The weights \(W_x\) are independent, with \(\Pr(W_x>w)=w^{-\alpha}\) for \(w\ge1\). Conditional on all weights, incidences \((x,r)\) are independent with probability \(1-\exp(-\lambda_n W_x/N_n)\).

For an integer cutoff \(2\le\ell\le n\), let \(E_{n,\ell}\) count incidences with catalyst in \(X_\ell\) and product of length at most \(\ell\). Let \(K_{n,\ell}\) be the number of distinct catalysts with at least one such incidence. Define
\[
\theta=\frac{\alpha(1+\beta)}{1+\alpha},\qquad
b_n=\theta n-\frac{\alpha}{1+\alpha}\log_\kappa n,\qquad
C=\Gamma(1-\alpha)\theta^\alpha(\kappa-1)^{\alpha\beta-1}\kappa^{1-\alpha\beta}.
\]

**Incidence-window theorem.** For each fixed \((z,w)\in[0,1]^2\) and uniformly over integer cutoffs with \(|\ell-b_n|\le M\) for every fixed \(M<\infty\),
\[
\mathbb E[z^{E_{n,\ell}}w^{K_{n,\ell}}]=
\exp\!\left[-C\kappa^{(1+\alpha)(\ell-b_n)}\{1-w+w(1-z)^\alpha\}\right]+o(1).
\]
Here the generating function uses \(0^0=1\). Along a sequence with \(\ell-b_n\to c\), \(K_{n,\ell}\) tends to a Poisson variable of mean \(C\kappa^{(1+\alpha)c}\). Conditional on that limiting number of catalysts, the total incidence count is the sum of as many independent Sibuya\((\alpha)\) marks, whose generating function is \(1-(1-z)^\alpha\). The incidence marginal is thus discrete stable. There need not be a single fixed law without tracking the lattice offset.

For any \(h_n\to\infty\) with \(h_n=o(n)\), the probability of at least one short incidence tends to zero at \(\ell_n^-=\lfloor b_n-h_n\rfloor\) and to one at \(\ell_n^+=\lfloor b_n+h_n\rfloor\).

## Proof of the incidence theorem

For a single catalyst \(x\in X_\ell\), let \(J_x\) be its number of short incidences. Write \(R=R_\ell\) and \(u=\lambda_n R/N_n\). Given \(W_x\), \(J_x\) is binomial with \(R\) trials and success probability \(1-e^{-uW_x/R}\). Its generating function is \(H(z)=\mathbb E[(z+(1-z)e^{-uW_x/R})^R]\). The Pareto density gives
\[
u^{-\alpha}(1-H(z))=\alpha\int_u^\infty
\big[1-(z+(1-z)e^{-v/R})^R\big]v^{-\alpha-1}\,dv.
\]
Since \(R_\ell\le nN_n\), \(0<u\le n\lambda_n\to0\). For every \(\ell\to\infty\), \(R\to\infty\), and the bracket tends to \(1-e^{-(1-z)v}\) for every fixed positive \(v\). The bound \(1-(1-d)^R\le\min\{1,Rd\}\) for \(0\le d\le1\), with \(d=(1-z)(1-e^{-v/R})\), majorizes the bracket by \(\min\{1,(1-z)v\}\). As \(0<\alpha<1\), dominated convergence and integration by parts give \(1-H(z)=\Gamma(1-\alpha)(1-z)^\alpha u^\alpha+o(u^\alpha)\); at \(z=1\) the difference is zero exactly. This limit is valid along every sequence with \(R\to\infty\), \(u\to0\).

Different catalysts' counts are independent by the two independence assumptions. The joint generating function for \((J_x,\mathbf1_{\{J_x>0\}})\) is \(H(0)+w[H(z)-H(0)]\), whose deficit from one is
\[
\Gamma(1-\alpha)u^\alpha\{1-w+w(1-z)^\alpha\}+o(u^\alpha).
\]
Raise it to power \(N_\ell\). Whenever \(N_\ell u^\alpha=O(1)\), the quadratic error in taking the logarithm is \(O(N_\ell u^{2\alpha})=o(1)\). If \(N_\ell u^\alpha\) has a limit, the resulting generating function is that of a Poisson number of independent marks, each contributing one to \(K\) and a mark to \(E\). The Sibuya coefficients are \(\alpha\Gamma(j-\alpha)/(\Gamma(1-\alpha)\Gamma(j+1))\) for \(j\ge1\), positive and summing to one by the binomial expansion. The limiting marks have infinite mean, but each prelimit \(J_x\) is bounded by \(R_\ell\). The limiting generating function is continuous at \((1,1)\), giving the claimed distributional convergence.

To identify the scale, \(N_m=\sum_{j=1}^m\kappa^j\sim \kappa^{m+1}/(\kappa-1)\) and \(R_m=\sum_{j=2}^m(j-1)\kappa^j\sim mN_m\). The latter follows because the difference \(mN_m-R_m=\sum_{j=1}^m(m-j+1)\kappa^j\) is \(O(N_m)\). Thus, for \(\ell\sim\theta n\),
\[
N_\ell u^\alpha\sim \ell^\alpha (\kappa-1)^{\alpha\beta-1}\kappa^{1-\alpha\beta}
\kappa^{(1+\alpha)\ell-\alpha(1+\beta)n}.
\]
Using \(\ell=b_n+c_n\) with \(c_n=o(n)\) rewrites this as
\(\theta^\alpha(\kappa-1)^{\alpha\beta-1}\kappa^{1-\alpha\beta}\kappa^{(1+\alpha)c_n}(1+o(1))\): the logarithmic shift cancels the factor \(n^\alpha\). When \(c_n\) stays bounded the error is uniform, since all the preceding sequential limits hold for every sequence of such cutoffs. At the lower and upper diverging offsets, \(N_\ell(1-H(0))\) tends to zero and infinity respectively. The exact zero-incidence probability is \(H(0)^{N_\ell}\); use \(1-H(0)\to0\) and \(x\le -\log(1-x)\le x/(1-x)\) for \(0\le x<1\). This proves both sides of the incidence window without extrapolating a bounded-offset approximation. \(\square\)

## Comparison with the known RAF transition

For a nonempty set of forward reactions to be a reflexively autocatalytic and food-generated set (RAF), each reaction's reactants must be in the food closure of the set and each reaction must have a catalyst in that closure. The food is \(X_t\) and closure means the words generated by repeatedly applying the ligations of the set, ignoring catalysis for this reachability test. For \(\ell\ge t\), there exists an ambient RAF whose closure lies in \(X_\ell\) if and only if the induced short subsystem contains an RAF. Indeed, such an ambient RAF uses only restricted reactions and restricted catalyst witnesses. Conversely any restricted RAF uses the same food and the same reactions and has the same closure when considered as an ambient RAF.

Kim and Sönmez (Theorem 8 and Section 3.3.4) give the RAF zero-one criterion for the diffuse Pareto model with maximum length \(m\), parameter \(\rho_m\) and per-incidence exponent \(-\rho_m W_x/N_m\). Their criterion tends to zero or one for RAF existence as \(\rho_m^\alpha N_m^{1-\alpha}\) tends to zero or infinity. The induced short system has exactly that law with \(m=\ell\) and \(\rho=\lambda_n N_\ell/N_n\). Its RAF criterion is therefore
\[
\left(\lambda_n N_\ell/N_n\right)^\alpha N_\ell^{1-\alpha}
=N_\ell N_n^{-\alpha(1+\beta)}\asymp\kappa^{\ell-\alpha(1+\beta)n}.
\]
The theorem applies to any sequence \(\ell\to\infty\) with the criterion tending to zero or infinity; if cutoffs repeat, any subsequence violating the conclusion has a further subsequence of strictly increasing cutoffs, on which the theorem applies by reindexing (extend to intermediate sizes with the same limiting criterion).

Thus, **as a direct corollary of the prior existence theorem**, the probability of a RAF contained in the induced short subsystem tends to zero at \(\lfloor\alpha(1+\beta)n-h_n\rfloor\) and one at \(\lfloor\alpha(1+\beta)n+h_n\rfloor\) for diverging sublinear \(h_n\). The RAF scale has coefficient \(\alpha(1+\beta)=(1+\alpha)\theta<1\), strictly larger than the incidence coefficient. In particular, at the upper incidence cutoff \(\ell_n^+\), short incidences are present with high probability but no RAF is contained at that length with high probability. Ambient RAF existence follows from the prior criterion at \(\ell=n\). The new assertion concerns the length-resolved incidence law and its exact critical scale, not a new nonformation or formation theorem for RAFs. No limiting RAF probability at bounded offset from its own transition is asserted.

## Related work and limits

Kim and Sönmez, *Can a self-sustaining chemical network emerge due to just a few catalysts?* ([arXiv:2611.06033v1](https://arxiv.org/html/2611.06033v1)), supply the reaction-independent kernel and the bulk RAF transition used above. Theorem 5 treats a single catalyst's degree tail at fixed intensity, with a threshold tending to infinity and a different normalization; it does not give a small-probability incidence-cluster limit at fixed generating-function arguments. Hordijk and Steel, *Autocatalytic sets in polymer networks with variable catalysis distributions* ([arXiv:1605.03919](https://arxiv.org/html/1605.03919)), give general formation criteria and study a model with a power-law draw for the number of reactions assigned to a molecule. Steel, Hordijk and Smith, *Minimal autocatalytic networks* ([arXiv:1212.4450](https://arxiv.org/html/1212.4450)), study RAF reaction-count size, not the short-incidence distribution. The Poisson and discrete-stable laws and the Sibuya distribution are established probability constructions; the contribution is their explicit length-resolved scaling in this random-word model. Historical priority is best-of-knowledge rather than exhaustive.

The model uses only abstract ordered ligations and independent random activity weights, with a fixed food bound, and has no chemical kinetics or empirical claims. The two-scale comparison does not identify the smallest RAF at any finite size. The finite examples in `check.py` are diagnostic and do not certify either asymptotic statement.
