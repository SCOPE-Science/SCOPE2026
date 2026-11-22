# Sharp lower-mean contest reversals and finite-population consequences under constrained abilities

## Finding

Let an individual's competitive ability be an independent draw \(X\in[0,1]\) from any Borel probability law of a focal species. Let the aggregate competitor have independent ability \(Y\sim\operatorname{Beta}(2,2)\), with density \(6y(1-y)\) on \([0,1]\). In the high-discrimination contest limit, the encounter rule awards a win to the larger ability. This is the limiting case of the logistic fighting-capacity comparison used in trait-based contest simulations as comparison noise decreases to zero; the beta-shaped opponent law is an explicit additional benchmark assumption, not a distribution claimed by the initiating study. The uniform competitor would instead give \(\Pr(X>Y)=\mu\) exactly, making a smaller-mean majority impossible; \(\operatorname{Beta}(2,2)\) is the simplest nonuniform integer-shape symmetric beta opponent, with central unimodality and a cubic win-probability function. Write \(\mu=\mathbb E X\), \(\nu=\mathbb E X^2\), and \(D=\Pr(X>Y)-\Pr(X<Y)\). The following gives a single exact classification of the attainable contest biases, a quantitative robustness result for noisy contests, and consequences under a separately specified finite-community replacement rule.

**Sharp two-moment envelope.** For every \(0<\mu<1\) and \(\mu^2\le\nu\le\mu\), the complete attainable interval is
\[
D_{-}(\mu,\nu)=2\nu-1+\frac{4(\mu-\nu)^2}{1-\mu}
\ \le\ D\ \le\
D_{+}(\mu,\nu)=6\nu-1-\frac{4\nu^2}{\mu}.
\]
For interior moment pairs \(\mu^2<\nu<\mu\), each endpoint has exactly one extremizing law. The upper endpoint is attained at \(\{0,\nu/\mu\}\), putting mass \(\mu^2/\nu\) at the positive point; the lower endpoint is attained at \(\{(\mu-\nu)/(1-\mu),1\}\), putting mass \((\nu-\mu^2)/(1-2\mu+\nu)\) at \(1\). Convex mixtures realize every intervening bias. The width is
\[
D_+-D_-=\frac{4(\mu-\nu)(\nu-\mu^2)}{\mu(1-\mu)}.
\]
Its maximum over all feasible second moments for a fixed \(\mu\) is \(\mu(1-\mu)\), attained at \(\nu=(\mu+\mu^2)/2\).

**Sharp invasion reversal under a smaller mean.** For every \(0<\mu\le1/2\), the maximum over *all* focal ability distributions with mean \(\mu\) is
\[
\sup_{\mathbb E X=\mu}D=\frac94\mu-1,
\]
attained uniquely by the law supported on \(\{0,3/4\}\) with mass \(4\mu/3\) at \(3/4\). Hence a focal species whose mean ability is strictly below the competitor mean \(1/2\) can win encounters more often than it loses **if and only if** \(\mu>4/9\). More sharply, for each \(4/9<\mu<1/2\), and with the *second moment also fixed*, both winning- and losing-biased laws exist precisely when
\[
\nu_-<\nu<\nu_+,
\qquad
\nu_\pm=\frac{3\mu\pm\sqrt{\mu(9\mu-4)}}4.
\]
For \(\nu\) outside this open interval every law in that moment class has \(D\le0\). Inside it the two endpoint laws have \(D_-<0<D_+\), and a mixture is exactly neutral.

**Persistence in the source-style noisy contest mechanism.** Let the focal contest-win probability instead be \(W_\lambda=\mathbb E[1/(1+\exp(-\lambda(X-Y)))]\) for any finite discrimination \(\lambda>0\), and write \(D_\lambda=2W_\lambda-1\). Uniformly over *all* focal ability laws on \([0,1]\),
\[
|D_\lambda-D|\le\frac6\lambda.
\]
In the explicit moment class \(\mu=12/25\), \(\nu=9/25\), the two extremizing laws have hard-contest biases \(2/25\) and \(-11/65\), respectively. For every \(\lambda>75\), the *same two focal laws* therefore have strictly opposite noisy-contest biases despite identical first two moments and a mean smaller than the rival mean. This robustness statement makes no claim that the hard-contest extremizers remain exact optimizers for finite \(\lambda\).

**Finite-population consequences.** For every community size \(J\ge2\), and initial focal count \(1\le k<J\), the no-immigration fixation probability increases strictly with \(D\) and is exactly
\[
u_{J,k}(D)=\begin{cases}
\dfrac{1-\bigl((1-D)/(1+D)\bigr)^k}{1-\bigl((1-D)/(1+D)\bigr)^J},&D\ne0,\\[4pt]
 k/J,&D=0.
\end{cases}
\]
Here \(u_{J,k}\) is the fixation function and \(\nu\) remains the second ability moment. Thus the same two extremizing ability distributions simultaneously bound fixation for *every* community size and initial count.

With immigration probability \(0<m<1\), metacommunity focal fraction \(0<\pi<1\), and encounter probability \(0<c\le1\), the exact finite-chain stationary abundance distribution also increases **strictly in monotone likelihood-ratio order** as \(D\) increases. Consequently those same endpoint laws simultaneously attain the smallest and largest stationary expectations for every nonconstant increasing function of focal abundance and the sharp upper/lower tails for every nontrivial abundance threshold. This is an exact finite-state result, not a diffusion approximation.

## Assumptions and scope

Individuals redraw competitive ability independently at each encounter from fixed ability laws; ability is bounded in \([0,1]\). Opponents' ability has the specified continuous beta law; it never ties with an independent focal ability, including atomic focal laws. Community size \(J\) is fixed. At focal count \(n\), opposite-type encounters occur with probability \(h_n=2n(J-n)/[J(J-1)]\). A decisive encounter, if allowed with probability \(c\), replaces the loser by the winner. When immigration is present, with probability \(m\) an immigrant independently replaces a uniformly sampled individual and is focal with probability \(\pi\); otherwise local competition is attempted. This finite-community replacement chain is a separately defined mathematical extension of the pairwise contest benchmark; it is not the discrete-time demographic model of Morales, Palaoro and Peixoto. The asymptotic noisy-contest bridge uses an inverse-logit comparison whose discrimination \(\lambda\) is varied, whereas their numerical study fixes its own noise scale. No claims are made for evolution of trait distributions, environmental feedback, arbitrary competitor laws, or nonlinear physiological mechanisms.

The focal ability distribution is allowed to have atoms. If one restricts a priori to continuous densities, the extremal atomic laws are not members of that restricted class; the displayed values remain rigorous bounds, but attainment is then not claimed.

## Proof

**1. From noisy competition to a third-moment bias.** As \(\lambda	o\infty\), the inverse-logit \(\sigma_\lambda(X-Y)\) converges almost surely to \(\mathbf 1_{\{X>Y\}}\), because the continuous opponent ability law eliminates ties; dominated convergence establishes the hard-contest limit. The competitor's cumulative distribution is \(F(y)=3y^2-2y^3\). Its continuity eliminates ties. Conditioning on the focal draw gives \(W=\mathbb EF(X)=3\nu-2\mathbb EX^3\) and \(D=2W-1=6\nu-4\mathbb EX^3-1\).

**2. Exactly sharp third-moment bounds.** Cauchy–Schwarz applied to \(X^{3/2}\) and \(X^{1/2}\) gives \((\mathbb EX^2)^2\le(\mathbb EX^3)(\mathbb EX)\); equivalently \(\mathbb EX^3\ge\nu^2/\mu\). Equality requires all positive values of \(X\) to coincide. The prescribed moments force support \(\{0,\nu/\mu\}\) with the stated probabilities. Similarly, Cauchy–Schwarz applied to \(X\sqrt{1-X}\) and \(\sqrt{1-X}\) yields \((\mu-\nu)^2\le(\nu-\mathbb EX^3)(1-\mu)\), so \(\mathbb EX^3\le\nu-(\mu-\nu)^2/(1-\mu)\). Equality requires all values strictly below \(1\) to coincide, giving uniquely the stated \(\{(\mu-\nu)/(1-\mu),1\}\) law. Substitution into \(D\) gives the two endpoints. The boundary cases \(\nu=\mu^2\) and \(\nu=\mu\) have unique one-point and Bernoulli laws, respectively, so their envelopes coincide. Mixtures preserve both moments and interpolate \(D\) affinely. Algebra gives the width formula and its maximum via the arithmetic–geometric mean inequality.

**3. A sharp lower-mean reversal threshold.** On the entire unit interval the elementary polynomial certificate
\[
\frac98x-F(x)=\frac{x(4x-3)^2}{8}\ge0
\]
proves \(W\le9\mu/8\). Equality forces the support of \(X\) to lie in \(\{0,3/4\}\). For \(\mu\le1/2\), the forced mass \(4\mu/3\) at \(3/4\) is admissible, establishing the sharp value and the uniqueness. In particular, the bias can be positive with \(\mu<1/2\) exactly for \(\mu>4/9\). At fixed \(\mu\) and \(\nu\), the inequality \(D_+>0\) is precisely \(4\nu^2-6\mu\nu+\mu<0\), whose discriminant is \(4\mu(9\mu-4)\). The roots are \(\nu_\pm\) displayed above and are feasible in \(\mu^2<\nu<\mu\) for \(4/9<\mu<1/2\). Finally \(D_-(\mu,\nu)\) is convex as a function of \(\nu\) on \([\mu^2,\mu]\). Its two endpoint values are \(2F(\mu)-1\) and \(2\mu-1\), both strictly negative when \(\mu<1/2\). Thus every lower extremizer is losing-biased; the prescribed positive/negative/neutral sign classification follows.

**4. Uniform noisy-contest robustness.** Define \(\sigma_\lambda(z)=[1+\exp(-\lambda z)]^{-1}\). For every \(x,y\in[0,1]\) with \(x\ne y\),
\[
|\sigma_\lambda(x-y)-\mathbf1_{\{x>y\}}|=\frac{1}{1+e^{\lambda|x-y|}}\le e^{-\lambda|x-y|}.
\]
Since the beta opponent's density never exceeds \(3/2\), conditioning on \(X=x\) and extending the integral to the real line yields a uniform win-probability difference at most \((3/2)\int_{-\infty}^\infty e^{-\lambda|z|}\,dz=3/\lambda\). Thus \(|D_\lambda-D|\le6/\lambda\). The positive benchmark bias \(2/25\) remains positive whenever \(\lambda>75\). The negative benchmark bias \(-11/65\) remains negative whenever \(\lambda>390/11\), hence certainly at the same \(\lambda>75\). With either stochastic win probability, the finite-community birth–death comparison below continues to hold upon substituting the relevant encounter bias.

**5. Exact fixation monotonicity.** Without immigration, the transitions at every interior count are \(p_n^+=c h_n (1+D)/2\), \(p_n^-=c h_n(1-D)/2\). The absorbing harmonic equation has a unique solution at \(0\) and \(J\): successive increments form a geometric progression with ratio \(r=(1-D)/(1+D)\), yielding the fixation formula. For \(0<k<J\), rewrite it as \(\sum_{i=0}^{k-1}r^i/\sum_{i=0}^{J-1}r^i\). This is the lower-tail probability of a truncated geometric distribution on \(0,\ldots,J-1\); its likelihood ratio is strictly increasing in the index as \(r\) increases. Therefore fixation strictly decreases in \(r\), and strictly increases in \(D\), including across \(D=0\) by continuity.

**6. Exact immigrating stationary ordering.** Under the stated parameter restrictions, the upward and downward transition probabilities are
\[
q_n^+=(1-m)c h_n\frac{1+D}{2}+m\pi\frac{J-n}{J},\qquad
q_n^-=(1-m)c h_n\frac{1-D}{2}+m(1-\pi)\frac nJ.
\]
They define an irreducible finite birth–death chain with a unique full-support invariant law \(P_D\) satisfying detailed balance \(P_D(n+1)/P_D(n)=q_n^+/q_{n+1}^-\). Every one of these adjacent ratios increases strictly with \(D\): the numerator is nondecreasing (strict except at \(n=0\)); the denominator is nonincreasing (strict except at \(n+1=J\)); at each edge at least one change is strict. Hence for \(D_2>D_1\), the stationary likelihood ratio \(P_{D_2}(n)/P_{D_1}(n)\) is strictly increasing in \(n\). A crossing-of-one argument for normalized positive probability vectors gives strictly larger upper tails at each \(1\le k\le J\), and strictly larger expectations for all nonconstant increasing observables.

A reproducible closed stationary expression is available: write \(a=2(1-m)cW/(J-1)\), \(b=2(1-m)cL/(J-1)\), \(\alpha=m\pi/a\), and \(\beta=m(1-\pi)/b\), where \(W=(1+D)/2\), \(L=(1-D)/2\). Then
\[
P_D(n)=\frac{1}{Z}\binom Jn(\alpha)_n(\beta)_{J-n}(a/b)^n,
\qquad Z=\sum_{n=0}^J\binom Jn(\alpha)_n(\beta)_{J-n}(a/b)^n.
\]
The rising factorial \((z)_n=z(z+1)\cdots(z+n-1)\), with \((z)_0=1\), makes every adjacent detailed-balance ratio immediate. The law is exact for every finite \(J\); no large-population limit is used.

## Verification

The accompanying standalone Python script \(`verify.py`\) uses exact rational arithmetic to check: the two atomic extremizers and their moments; the sharp polynomial identity and example; fixation harmonic equations for community sizes \(2\) through \(12\); detailed balance and strict stationary-tail order for multiple positive immigration, mixing, and abundance parameters; the sharp sign-reversal example below, and the exact \(\lambda=75\) uniform robustness margins that imply the stated strict signs for all \(\lambda>75\). These finite checks support the algebra but do not replace the universally quantified inequalities and birth–death arguments in the proof.

An exact example for both hard and sufficiently discriminatory logistic contests fixes \(\mu=12/25<1/2\) and \(\nu=9/25\). The positive-bias law puts probability \(16/25\) on ability \(3/4\), and \(9/25\) on ability \(0\): it has \(D_+=2/25\). The negative-bias law puts probability \(169/250\) on ability \(3/13\), and \(81/250\) on ability \(1\): it has \(D_-=-11/65\). Both have exactly the same mean and variance. For another class, \(\mu=1/2\), \(\nu=3/8\), the extreme biases are \(\pm1/8\), so with \(J=10\) and \(k=5\) the maximum and minimum closed-community fixation probabilities are \(59049/75856\) and \(16807/75856\), respectively.

## Relationship to prior work

Morales, Palaoro and Peixoto (2025) study randomly paired animals whose composite fighting capacities derive from potentially correlated phenotypic traits. Their contest outcome uses a logistic function of the capacity difference. Their full published Methods, Results, and Discussion concern inferred trait importance and correlations, not sharp ability-distribution bounds or the fixed-community persistence law here. We take the high-discrimination limit of their pairwise logistic comparison, replace the composite-score distribution by an explicitly chosen \(\operatorname{Beta}(2,2)\) opponent law, and ask a distinct ecological question: can a focal population that is weaker **on average** win most contests and gain a finite-population advantage, even when its first two moments are known? Their source does not assert this threshold or analyze the present bounded moment class. The paper's joint normal trait model and fixed logistic-noise coefficient are *not* retained in the theorem.

Sharp third-moment envelopes on \([0,1]\) arise from classical Hausdorff moment inequalities; the Cauchy–Schwarz inequalities in this proof are not claimed to be new general results. Exact two-type fixation laws and birth–death detailed balance are likewise classical. Rychtář and Taylor (2020/2021) discuss fluctuating fitness in Moran/Wright–Fisher processes, and Braha and de Aguiar (2026) analyze selected Moran stationary laws under different, fixed fitness update mechanisms. McCandlish, Epstein and Plotkin (2013) study fixation identities. None of those inspected source claims covers the **specific joint classification** of beta-opponent pairwise contest outcomes with a sharp lower-mean reversal, full fixed-variance sign window, finite-logistic persistence, and simultaneous all-population consequence for the explicitly defined pairwise winner-replacement mechanism. This is a bounded model-specific application and not a new general moment-problem or stochastic-ordering theorem.

## Limitations

The \(\operatorname{Beta}(2,2)\) competitor and the unit-bounded trait scale are explicit benchmark choices, different from the empirical source's bivariate normal trait distribution; the numerical \(4/9\) threshold does not apply to arbitrary background abilities. The focal laws attaining the bounds are atomic; density-only parameterizations have not been shown to attain them. Immigration must satisfy \(0<m<1\) for strict stationary comparison; at \(m=1\) encounters play no role. The finite-chain model specifies a separate winner-replacement update and does not validate a real population or reconstruct the source simulations. The exact hard-contest envelope is **not** asserted for arbitrary finite logistic discrimination; the explicit \(\lambda>75\) comparison only proves sign robustness for two stated laws. The result addresses fixed trait distributions, not evolving traits, spatial interaction, environmental disturbances, actual species fitness, or measured invasion data. Existing general moment theory and undiscovered model-specific sources remain historical-priority risks. Independent validation has not been performed.

## References

1. M. Morales, A. V. Palaoro and P. E. C. Peixoto, *Simulating contests to determine the relative importance of correlated traits on the winning chances*, Behavioral Ecology 36(6), araf119 (first published 6 October 2025), https://doi.org/10.1093/beheco/araf119 .
2. J. Rychtář and D. T. Taylor, *Moran process and Wright–Fisher process favor low variability*, Discrete and Continuous Dynamical Systems B 26 (2021), 3491–3504 (first online 20 August 2020), https://doi.org/10.3934/dcdsb.2020242 .
3. D. Braha and M. A. M. de Aguiar, *Selection Mechanisms, Stationary Distributions, and Reversibility in Multiallelic Moran Models*, arXiv:2607.06732 (first released 7 July 2026), https://arxiv.org/abs/2607.06732 .
4. D. M. McCandlish, C. L. Epstein and J. B. Plotkin, *Formal properties of the probability of fixation: identities, inequalities and approximations*, arXiv:1312.1673 (2013), https://arxiv.org/abs/1312.1673 .
