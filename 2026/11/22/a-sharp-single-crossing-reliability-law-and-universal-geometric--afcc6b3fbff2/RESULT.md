# A sharp single-crossing reliability law and universal geometric tail for paired Rayleigh–Lindley discretizations

## Finding

**Theorem (joint hazard and survival-order phase transition).** Fix \(\alpha,\theta>0\). Put
\[
R_\theta(x)=\frac{(1+\theta)e^{\theta x}}{1+\theta+\theta x}-1,
\qquad \omega(x)=\frac{R_\theta(x)^2}{2\alpha^2}
\quad (x\geq0).
\]
Define two positive-integer lifetimes \(U,V\) as follows. The survival-discretized lifetime satisfies
\[
\Pr(U>n)=e^{-\omega(n)},\quad n=0,1,2,\ldots,
\qquad a_k=\Pr(U=k\mid U\ge k)
=1-e^{-[\omega(k)-\omega(k-1)]}.
\]
The hazard-discretized lifetime has \(b_k=\Pr(V=k\mid V\ge k)=\exp(e^{-\omega(k)}-1)\) for \(k\ge1\), and therefore
\[
\Pr(V>n)=\prod_{j=1}^n(1-b_j),\quad
\Pr(V=k)=b_k\prod_{j=1}^{k-1}(1-b_j).
\]
These are genuine probability laws on \(\{1,2,\ldots\}\), including the empty-product convention for \(n=0\). Let \(W_0\) be the principal real Lambert function and define
\[
\lambda_0=-\log(1-W_0(1)),\qquad
\alpha_*(\theta)=\frac{R_\theta(1)}{\sqrt{2\lambda_0}}.
\]
The following four assertions hold.

1. The continuous interpolants \(a(x)=1-e^{-[\omega(x)-\omega(x-1)]}\) and \(b(x)=\exp(e^{-\omega(x)}-1)\), defined for real \(x\ge1\), are respectively strictly increasing and strictly decreasing. For \(0<\alpha<\alpha_*(\theta)\), \(a_k>b_k\) at every integer \(k\ge1\). At equality of parameters, \(a_1=b_1\) and \(a_k>b_k\) for \(k\ge2\). When \(\alpha>\alpha_*(\theta)\), there is one and only one real \(x_\alpha>1\) with \(a(x_\alpha)=b(x_\alpha)\); \(a(x)<b(x)\) for \(1\le x<x_\alpha\) and the reverse inequality holds for \(x>x_\alpha\).
2. When \(\alpha<\alpha_*(\theta)\), \(U\) is strictly smaller than \(V\) in first-order stochastic order, i.e., \(\Pr(U>n)<\Pr(V>n)\) for every integer \(n\ge1\). When \(\alpha=\alpha_*(\theta)\) the two survivals coincide at \(n=1\), and the same strict inequality holds at all \(n\ge2\). When \(\alpha>\alpha_*(\theta)\), \(\Pr(U>1)>\Pr(V>1)\), whereas \(\Pr(U>n)<\Pr(V>n)\) for all sufficiently large \(n\). Across increasing integer \(n\), their survival-order sign reverses **exactly once**, allowing equality at its crossing count.
3. For fixed \(\theta>0\), as \(\alpha\to\infty\), the unique real hazard crossing satisfies
\[
x_\alpha=\frac{\log\alpha+\log\log\alpha+
\log\!\big(\sqrt{2w_\theta}/(1+\theta)\big)}{\theta}+o(1),
\]
where \(w_\theta>0\) is the unique solution of
\[
1-e^{-(1-e^{-2\theta})w_\theta}=e^{e^{-w_\theta}-1}.
\]
In particular the transition is delayed on a logarithmic-plus-logarithmic scale.
4. Set \(q_\infty=1-e^{-1}\), and
\[
C_{\alpha,\theta}=
\prod_{j=1}^{\infty}\frac{1-\exp(e^{-\omega(j)}-1)}{q_\infty}.
\]
Then \(0<C_{\alpha,\theta}<1\) and
\[
\Pr(V>n)\sim C_{\alpha,\theta}q_\infty^n,
\qquad \Pr(V=n)\sim C_{\alpha,\theta}e^{-1}q_\infty^{n-1}.
\]
Thus \(\mathbb E e^{tV}<\infty\) **if and only if** \(t<-\log(1-e^{-1})\), independently of \(\alpha,\theta\), while \(\mathbb E e^{tU}<\infty\) for **every** real \(t\). In particular their upper-tail classes differ for all admissible parameters, notwithstanding their common continuous origin.

## Assumptions and scope

Every quantified parameter \(\alpha,\theta\) is strictly positive. Lifetimes have support on positive integers, and the discrete failure hazard is defined by \(\Pr(T=k\mid T\ge k)\). The \(U\)-law is the survival-discretized count law shifted up by one, so its hazard is a probability rather than an odds ratio. The \(V\)-law is constructed explicitly from the positive-index hazard sequence through its survival product. This normalization is essential: the source's printed expression assigning mass one at index zero in addition to positive-index masses cannot be read literally as a normalized mass function. No claim is made about that unnormalized expression as a probability distribution. The theorem does not rely on its printed zero-mass assignment.

The first public source for this construction is Ahmad (22 April 2024), Section 2, equations (2), (5), (7), (9), and (12). The two discretization *methods* and the underlying continuous model are prior work; the proposed result is their sharp comparative reliability classification, survival-order reversal, crossing asymptotics and exact moment-domain separation.

## Proof

**(i) Validity, convexity and ordering.** Write \(Q(x)=R_\theta(x)+1\). Direct differentiation shows
\[
\frac{d}{dx}\log Q(x)=\theta-\frac{\theta}{1+\theta+\theta x}>0,
\qquad
\frac{d^2}{dx^2}\log Q(x)=\frac{\theta^2}{(1+\theta+\theta x)^2}>0
\]
for all \(x\ge0\). Consequently \(R_\theta(0)=0\), \(R_\theta\) is strictly increasing and strictly convex, and \(R_\theta(x)>0\) at \(x>0\). Since
\[
\omega'(x)=\alpha^{-2}R_\theta(x)R_\theta'(x),\qquad
\omega''(x)=\alpha^{-2}\big(R_\theta'(x)^2+R_\theta(x)R_\theta''(x)\big)>0,
\]
\(\omega\) is strictly increasing and strictly convex. Therefore \(\omega(x)-\omega(x-1)\) increases strictly with \(x\ge1\), so \(a(x)\) increases strictly. The strict increase of \(\omega\) makes \(b(x)\) decrease strictly. Note \(a(x)\in(0,1)\), \(b(x)\in(e^{-1},1)\) for every finite \(x\ge1\). Also \(\omega(x)-\omega(x-1)\to\infty\), hence \(a(x)\to1\), while \(b(x)\to e^{-1}\).

Thus \(d(x)=a(x)-b(x)\) is strictly increasing and tends to \(1-e^{-1}>0\). At \(x=1\), write \(u=e^{-\omega(1)}\in(0,1)\). Then \(a(1)=1-u\), \(b(1)=e^{u-1}\); their equality is \(z=e^{-z}\) for \(z=1-u\in(0,1)\), or \(z=W_0(1)\). Equivalently \(\omega(1)=\lambda_0\), which after substituting \(\omega(1)=R_\theta(1)^2/(2\alpha^2)\) is precisely \(\alpha=\alpha_*(\theta)\). Moreover \(a(1)-b(1)\) increases strictly with \(\omega(1)\), so it decreases strictly with \(\alpha\). This proves the trichotomy and uniqueness of the real root; the exact-integer tie possibility is allowed.

**(ii) Survival-order crossing.** Define \(T_n=\Pr(U>n)/\Pr(V>n)\), a strictly positive ratio for each finite integer \(n\). Since the survival recursion for a positive-integer hazard is \(\Pr(T>n)=\Pr(T>n-1)(1-h_n)\),
\[
\frac{T_n}{T_{n-1}}=\frac{1-a_n}{1-b_n},\qquad T_0=1.
\]
If \(\alpha\le\alpha_*\), part (i) gives \(T_n\le1\) for every \(n\ge1\), with the stated strictness. If \(\alpha>\alpha_*\), then \(T_1>1\), and the successive factors are greater than one until the unique hazard crossing, at most one equal to one, and strictly less than one thereafter. Thus \((T_n)\) first increases and later strictly decreases (possibly with one plateau). It remains to show it eventually falls below one: by the product estimates in part (iv) and the formula for \(U\), \(T_n\to0\). Hence there is exactly one passage from \(T_n>1\) to \(T_n<1\) in the ordered integer sequence, with at most one intermediate equality. This is a single survival-order reversal, not a claim of global stochastic ordering in the large-\(\alpha\) regime.

**(iii) Large-scale root.** At any fixed \(x\ge1\), as \(\alpha\to\infty\), \(a(x)\to0\) and \(b(x)\to1\); thus \(x_\alpha\to\infty\). As \(x\to\infty\),
\[
R_\theta(x)\sim\frac{1+\theta}{\theta x}e^{\theta x},\qquad
\frac{R_\theta(x-1)}{R_\theta(x)}\longrightarrow e^{-\theta}.
\]
Put \(v_\alpha=\omega(x_\alpha)\) and \(\rho_\alpha=\omega(x_\alpha-1)/\omega(x_\alpha)\). Then \(\rho_\alpha\to e^{-2\theta}\), and the crossing identity reads
\[
1-e^{-(1-\rho_\alpha)v_\alpha}=e^{e^{-v_\alpha}-1}.
\]
For each \(0\le\rho<1\), the left side is strictly increasing in \(v>0\) from zero to one and the right side strictly decreases from one to \(e^{-1}\); hence the positive crossing is unique, depends continuously on \(\rho\), and stays between two finite positive bounds near \(e^{-2\theta}\). It follows that \(v_\alpha\to w_\theta\), with \(w_\theta\) uniquely specified above. Thus \(R_\theta(x_\alpha)=\alpha\sqrt{2v_\alpha}=\alpha\sqrt{2w_\theta}(1+o(1))\). Substituting its exponential-over-linear asymptotic gives
\[
\theta x_\alpha=\log\alpha+\log(\theta x_\alpha)+\log\!\big(\sqrt{2w_\theta}/(1+\theta)\big)+o(1).
\]
The same relation first implies \(\theta x_\alpha/\log\alpha\to1\), so \(\log(\theta x_\alpha)=\log\log\alpha+o(1)\). This yields the asserted formula, including the constant term. No unproved uniformity in \(\theta\) is asserted.

**(iv) Tail constant and moment domains.** From the asymptotic for \(R_\theta\),
\[
\omega(n)\sim\frac{(1+\theta)^2}{2\alpha^2\theta^2n^2}e^{2\theta n},
\]
so \(\sum_{n\ge1}e^{-\omega(n)}<\infty\). Set \(s_n=e^{-\omega(n)}\). Then
\[
b_n=e^{-1}e^{s_n},\qquad
\frac{1-b_n}{q_\infty}
=1-\frac{e^{-1}}{q_\infty}(e^{s_n}-1).
\]
All factors lie strictly between zero and one. Their deficits from one sum to a finite number because \(e^{s_n}-1=O(s_n)\) and \(\sum s_n<\infty\). The standard elementary convergence criterion for infinite products gives a positive limit \(C_{\alpha,\theta}\in(0,1)\). Thus \(\Pr(V>n)=q_\infty^n\prod_{j\le n}(1-b_j)/q_\infty\sim C_{\alpha,\theta}q_\infty^n\). The mass equivalent follows from \(\Pr(V=n)=b_n\Pr(V>n-1)\) and \(b_n\to e^{-1}\).

Because the positive masses of \(V\) are asymptotically positive multiples of \(q_\infty^{n-1}\), the series \(\sum_{n\ge1}e^{tn}\Pr(V=n)\) converges exactly when \(e^tq_\infty<1\), diverging also at equality since its terms do not vanish. For \(U\), the survival \(\Pr(U>n)=e^{-\omega(n)}\) decreases faster than every exponential, and \(\Pr(U=n)\le\Pr(U>n-1)\), so \(\sum e^{tn}\Pr(U=n)<\infty\) for all finite real \(t\). Finally \(T_n=e^{-\omega(n)}/(C_{\alpha,\theta}q_\infty^n(1+o(1)))\to0\), as used in part (ii). This completes the proof.

## Verification

Run `python3 check.py` in the extracted package directory. The checker uses only the Python standard library and probes distinct \(\theta\)-values, parameter values below, at and above \(\alpha_*\), strict hazards before floating-point saturation, the crossing equation, survival-order signs, the asymptotic constant, and convergence of the product factor. It is a **finite numerical stress test**, not an infinite proof. The preceding analytic argument supplies the all-index and limiting claims. Its computations do not certify machine-independent numerical error bounds; the threshold is defined exactly via \(W_0(1)\), not by a rounded decimal.

## Relationship to prior work

Ahmad (2024, Section 2, especially equations (2), (5), (7), (9) and (12)) introduced the two Rayleigh–Lindley discretization formulas and described the decreasing shape of the second hazard. Chakraborty (2015) surveys survival- and hazard-based discretization as established techniques. Ahmad, Ramadan and Almetwally (2024) study another, generalized-Rayleigh count model, not the paired Rayleigh–Lindley hazard-and-survival comparison. The new assertion is the **joint** exact parameter threshold, unique cross-over including survival-order implications, asymptotic crossover location, positive geometric tail constant and universal moment-domain boundary. The reported source's raw hazard-odds expression for the first construction and its index-zero mass assignment for the second are not adopted as probability claims here; the proof uses correctly normalized distributions from the source's survival and positive-index hazard formulas. No claim of invention of the discretization schemes is made.

## Limitations

This is a theoretical classification, not a fit to new data. Its crossing-location asymptotic holds with \(\theta\) fixed; it is not uniform as \(\theta\to0\) or \(\theta\to\infty\). The survival comparison at large \(\alpha\) gives one reversal, not a single parameter-free stochastic order. The second count law is the coherent positive-support normalization from the cited survival product; it must not be confused with the article's inconsistent printed index-zero probability. Historical priority beyond the checked sources remains a research risk, and independent expert validation has not been performed.

## References

1. H. Haj Ahmad, *The Efficiency of Hazard Rate Preservation Method for Generating Discrete Rayleigh–Lindley Distribution*, **Mathematics** 12(8):1261 (2024), first published 22 April 2024, DOI: https://doi.org/10.3390/math12081261; full text: https://www.mdpi.com/2227-7390/12/8/1261.
2. S. Chakraborty, *Generating discrete analogues of continuous probability distributions—A survey of methods and constructions*, **Journal of Statistical Distributions and Applications** 2:6 (2015), DOI: https://doi.org/10.1186/s40488-015-0028-6; full text: https://link.springer.com/article/10.1186/s40488-015-0028-6.
3. H. Haj Ahmad, D. A. Ramadan and E. M. Almetwally, *Evaluating the Discrete Generalized Rayleigh Distribution: Statistical Inferences and Applications to Real Data Analysis*, **Mathematics** 12(2):183 (2024), DOI: https://doi.org/10.3390/math12020183; full text: https://www.mdpi.com/2227-7390/12/2/183.
