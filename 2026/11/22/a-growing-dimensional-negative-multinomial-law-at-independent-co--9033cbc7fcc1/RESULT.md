# A growing-dimensional negative-multinomial law at independent coupon completion

## Finding

Independently sample \(q\ge2\) sequences of uniformly distributed labels from \(\{1,\ldots,n\}\), \(n\ge2\). At every integer round each sequence advances one label. Stop at the first time \(T_n\) at which **sequence 1** has seen all \(n\) labels. For \(2\le j\le q\), let \(K_{j,n}\) count labels not yet seen in sequence \(j\) at round \(T_n\). Write \(H_n=\sum_{h=1}^n1/h\). Let \(E\) be exponential of mean one and, conditionally on \(E\), let \(Z_2,\ldots,Z_q\) be independent Poisson variables of mean \(E\). Then for every finite \(n,q\),

\[
d_{\mathrm{TV}}\big(\mathcal L((K_{j,n})_{j=2}^q),\mathcal L((Z_j)_{j=2}^q)\big)
\le \min\left\{1,(q-1)\left[2(1+e)\sqrt{\frac{H_n}{n}}+\frac3n\right]\right\}.
\]

For every fixed \(q\), the joint limiting mass at nonnegative integers \(k_2,\ldots,k_q\), with \(m=\sum_{j=2}^qk_j\), is

\[
\Pr(Z_2=k_2,\ldots,Z_q=k_q)=\frac{m!}{q^{m+1}\prod_{j=2}^q k_j!}.
\]

The total \(\sum_{j=2}^qZ_j\) is geometric on nonnegative integers with parameter \(1/q\). The bound is useful even for increasing numbers of collectors: the joint total variation tends to zero if \(q=q_n=o(\sqrt{n/\log n})\).

## Assumptions and scope

All coupon labels are independent over collectors and rounds; the same full alphabet of \(n\) types and the same uniform label probabilities are used throughout. The stopping clock is that of the distinguished collector 1, not the first completion among all collectors. All laws are unconditional over this stopping time. The total-variation convention is the supremum over measurable events (or half the discrete \(\ell^1\) difference). The exponential variable is shared across all limit coordinates, so these coordinates are conditionally independent, **not marginally independent**.

## Proof

**1. One common stopping time under Poissonization.** Independently attach unit-rate Poisson arrival clocks to each collector, keeping its label sequence unchanged. Let \(S\) denote the continuous completion time of collector 1. It is the sum of its first \(T_n\) independent rate-one exponential waiting times. Let \(N_j(S)\) denote the number of arrivals of collector \(j\) before \(S\), and let \(\widetilde K_{j,n}\) be the missing-label count among the first \(N_j(S)\) labels in the same discrete label sequence. Conditional on \(T_n=t\), \(S\) has the \(\operatorname{Gamma}(t,1)\) distribution, independent of the other collectors, so \(N_j(S)\) has mean \(t\) and variance \(2t\). In particular,
\[
\mathbb E[(T_n-N_j(S))^2]=2\mathbb E T_n=2nH_n,
\]
using the classical decomposition of \(T_n\) into independent geometric waiting times with success probabilities \(h/n\), \(1\le h\le n\).

**2. Coupling synchronized with Poisson time.** Set \(x=1-1/n\) and \(z=x^2\). Conditional on \(T_n=t\), \(N_j(S)=s\), two missing-label counts using the *same* label sequence may differ only if one of the extra \(|t-s|\) draws encounters a label absent in the first \(\min(t,s)\) draws. A union bound and independence of the label sequence from the clock and stopping time give
\[
\Pr(K_{j,n}\ne\widetilde K_{j,n}\mid T_n=t,N_j(S)=s)
\le |t-s|x^{\min(t,s)}\le |t-s|(x^t+x^s).
\]
Let \(F_n(w)=\mathbb E w^{T_n}\). From the independent geometric waiting times,
\[
F_n(w)=\prod_{h=1}^n\frac{h}{h+n(1-w)/w},\qquad 0<w<1.
\]
For \(z=(1-1/n)^2\), \(n(1-z)/z\ge2\), hence \(\mathbb E z^{T_n}\le 2/[(n+1)(n+2)]\). Conditional on \(T_n=t\), the Poisson–Gamma calculation gives \(\mathbb E(z^{N_j(S)}\mid T_n=t)=(2-z)^{-t}\). Setting \(w=(2-z)^{-1}\) in the product formula gives denominator shifts \(n(1-z)=2-1/n\). Therefore,
\[
\mathbb E z^{N_j(S)}\le e^2\frac{2}{(n+1)(n+2)}.
\]
Indeed the ratio to the product with shift \(2\) is \(\prod_{h=1}^n(1-1/[n(h+2)])^{-1}\le e^2\): use \(-\log(1-u)\le u/(1-u)\) and sum at most \(2\) for \(n\ge2\). Cauchy–Schwarz and the preceding second moment now yield
\[
\Pr(K_{j,n}\ne\widetilde K_{j,n})\le 2(1+e)\sqrt{H_n/n}.
\]
A union bound extends this to all \(q-1\) nondistinguished collectors.

**3. Exact continuous-time mixture.** Thinning the rate-one Poisson process of collector 1 by label gives \(n\) independent first-arrival times, each exponential with rate \(1/n\). Consequently \(S\) is their maximum and \(U=e^{-S/n}\) has the exact \(\operatorname{Beta}(1,n)\) distribution: \(\Pr(U>u)=(1-u)^n\) for \(0<u<1\). Given \(U\), different collectors independently miss each coupon with probability \(U\). Thus
\[
(\widetilde K_{j,n})_{j=2}^q\mid U\ \sim\ \bigotimes_{j=2}^q\operatorname{Bin}(n,U).
\]
This identity holds at every finite \(n,q\), not just asymptotically.

**4. Uniform joint Poisson approximation.** Conditional on \(U\), Le Cam's elementary Bernoulli-to-Poisson coupling bounds the distance per coordinate to \(\operatorname{Pois}(nU)\) by \(nU^2\). Since \(\mathbb E U^2=2/[(n+1)(n+2)]\), the joint error is at most \(2(q-1)/n\). To couple the mixed intensity to a mean-one exponential, take \(E\sim\operatorname{Exp}(1)\) and \(U=1-e^{-E/n}\); this has precisely the required beta distribution and \(0\le E-nU\le E^2/(2n)\). Adding an independent Poisson variable of mean \(E-nU\) to each \(\operatorname{Pois}(nU)\) coordinate incurs at most \((q-1)\mathbb E(E-nU)\le(q-1)/n\). Combining the three coupling errors proves the displayed bound.

**5. Joint mass and consequence.** Integrating the shared exponential intensity yields \(\int_0^\infty e^{-qe}e^m\,de/\prod k_j!=m!/[q^{m+1}\prod k_j!]\). Summing the mass over all tuples of total \(m\) gives \(\Pr(\sum Z_j=m)=(q-1)^m/q^{m+1}\). For distinct coordinates \(i,j\), \(\operatorname{Cov}(Z_i,Z_j)=\operatorname{Var}(E)=1\), while \(\operatorname{Var}(Z_i)=2\); the limiting coordinates are positively dependent despite independent sampling at fixed rounds. Finally \(H_n\le1+\log n\) proves the growing-\(q\) assertion.

## Verification

Run `python3 verify.py` using the standard library. It checks exact finite coupon-completion distributions, geometric generating functions and finite beta-binomial masses for \(2\le n\le7\) with rational arithmetic and uses 350 time steps to control the remaining completion tail. The analytic coupling and bounds above prove the statements for all \(n,q\); this finite checker is a consistency check, not an exhaustive or infinite certificate.

## Relationship to prior work

Myers and Wilf studied simultaneous independent collectors, with exact completion ties and ballot-like comparisons; the results inspected do not give the joint full missing-coupon vector at one collector's completion or a uniform growing-dimensional total-variation error. Doumas and Papanicolaou studied **sequential sibling hand-down of duplicates**, a different dependence mechanism whose sibling deficits grow logarithmically, rather than these independent collectors' tight deficits. Poissonization, Poisson approximation for rare categories, negative-multinomial mixtures, and the one-collector Gumbel cover time are classical ingredients and are not claimed to be new. The proposed contribution is their explicit combination into a uniform joint error with a growing number of *independently sampled* albums.

## Limitations

The total-variation error bound is not claimed sharp, and the condition on increasing \(q\) is sufficient rather than known optimal. The result assumes independent synchronized uniform draws and the first collector's completion time; neither nonuniform coupons nor stopping at the first of all collectors is covered. The literature comparison is best-knowledge, and a historical equivalent formulation may exist. Independent mathematical validation has not been performed.

## References

- A. N. Myers and H. S. Wilf, *Some new aspects of the coupon-collector's problem*, arXiv:math/0304229, first public version April 16, 2003. https://arxiv.org/abs/math/0304229 ; full preprint https://arxiv.org/pdf/math/0304229
- A. V. Doumas and V. G. Papanicolaou, *The Siblings of the Coupon Collector*, arXiv:1412.4346, first public version December 14, 2014. https://arxiv.org/abs/1412.4346
- Classical coupon-collector waiting-time decomposition, Poisson thinning and Le Cam's binomial-to-Poisson bound; the relevant identities are derived explicitly above.
