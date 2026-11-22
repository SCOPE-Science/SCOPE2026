# A critical likelihood-ratio reversal in the Poisson–Lindley minification chain

## Finding

Consider the stationary Poisson–Lindley minification integer-valued autoregressive chain defined below. Its one-step transition kernel is **strictly stochastically increasing** in the preceding count for every admissible parameter pair. Nevertheless, at every **interior** admissible pair it has a uniquely located reversal of adjacent likelihood-ratio orientation in its two lowest output columns. At the **admissibility boundary** no such reversal occurs in these two columns.

For preceding state \(y\in\mathbb N_0\), write \(K(y,x)=\Pr(X_{n+1}=x\mid X_n=y)\) and define
\[
\Delta_y=K(y,0)K(y+1,1)-K(y+1,0)K(y,1).
\]
Set \(q=a/(1+a)\), \(r=1/(1+a)\), \(U=\Pr(\varepsilon\ge1)\), \(V=\Pr(\varepsilon\ge2)\), and
\[
B_a(z)=qV(1-U)z+UV(2r-1)-U+2qV-UVr^{z+2}\qquad(z\ge0).
\]
Then for all integers \(y\ge0\),
\[
\boxed{\Delta_y=-qr^{y+1}B_a(y).}
\]
At the endpoint \(a=a_c(t)\), \(\Delta_y>0\) for every \(y\). For every \(a>a_c(t)\), the continuous function \(B_a\) has exactly one positive zero \(z_*(a,t)\), and
\[
\boxed{\Delta_y>0\ (y<z_*),\quad \Delta_y=0\ (y=z_*),\quad
\Delta_y<0\ (y>z_*),\quad y\in\mathbb N_0.}
\]
The equality alternative occurs only if \(z_*\) happens to be an integer. Hence the kernel is **not TP2** for any interior admissible pair, although it is strictly stochastically monotone. The crossing moves to infinity at the boundary, with an explicit reciprocal-distance divergence constant proved below. No global TP2 conclusion is asserted at the boundary.

## Assumptions and scope

Let \(a,t>0\), and define the critical value
\[
a_c(t)=\frac12\left[\frac{1-t}{1+t}
+\sqrt{\frac{t^2+3t+6}{(t+1)(t+2)}}\right].
\]
Assume \(a\ge a_c(t)\). Let \(G_1,G_2,\ldots\) be independent geometric counts with
\(\Pr(G_j=k)=r q^k\) for \(k\in\mathbb N_0\), and let independent innovations \(\varepsilon_n\) have the survival law specified below. The transition is
\[
X_{n+1}=\min\left\{\sum_{j=1}^{X_n+1}G_{n+1,j},\,\varepsilon_{n+1}\right\}.
\]
The intended stationary marginal is the discrete Poisson–Lindley law
\[
\pi_k=\frac{t^2(t+k+2)}{(t+1)^{k+3}},\qquad k\in\mathbb N_0.
\]
Write \(s=1/(t+1)\), \(z=a/(a+1-s)\), \(c=s(1-s)\), \(d=s^2(1-z)\), and \(\gamma=s/z\). Define the innovation survival, for every \(k\in\mathbb N_0\), by
\[
E(k):=\Pr(\varepsilon\ge k)
=\gamma^k\frac{1+ck}{1+dk}.
\]
In particular \(U=E(1)\) and \(V=E(2)\). The theorem concerns all finite positive \(a,t\) in the stated admissible range; it does not assume a finite state space, truncate the innovations, or infer infinite-index signs from numerical enumeration.

## Proof

**1. Admissible innovations and the boundary.** The Poisson–Lindley survival is \(S_X(k)=s^k(1+ck)\). The probability-generating function of the geometric sum with a Poisson–Lindley number of summands gives
\[
\Pr\!\left(\sum_{j=1}^{X+1}G_j\ge k\right)=z^k(1+dk).
\]
Consequently \(E(k)=S_X(k)/[z^k(1+dk)]\) is precisely the survival needed for stationarity. Indeed, substituting the Poisson–Lindley generating function \(\Psi_X(u)=t^2(t+2-u)/[(t+1)(t+1-u)^2]\) gives the explicit geometric/shape-two negative-binomial mixture
\[
\frac{r}{1-qu}\Psi_X\left(\frac r{1-qu}\right)
=(1-s^2)\frac{1-z}{1-zu}+s^2\left(\frac{1-z}{1-zu}\right)^2.
\]
Its survival is exactly \(z^k\{1+s^2(1-z)k\}\).

The elementary difference governing whether \(E\) decreases is
\[
\begin{split}
&(1+ck)(1+d(k+1))-\gamma(1+c(k+1))(1+dk)\\
&\qquad=(1+d)-\gamma(1+c)
 +(1-\gamma)\{(c+d+cd)k+cdk^2\}.
\end{split}
\]
Define
\[
F(a,t)=(t+1)^2(t+2)a^2+(t+1)(t+2)(t-1)a-(t^2+3t+1),
\]
\[
D(a,t)=a(t+1)^2\{a(t+1)^3+t^3+2t^2+2t\}.
\]
Direct simplification yields
\[
1-U=\frac{t^2F(a,t)}{D(a,t)}.
\]
The unique positive root of \(F\) is \(a_c(t)\), and \(F(1/(t+1),t)=-(t+1)<0\), so \(a_c(t)>1/(t+1)\). Thus \(0<\gamma<1\) throughout the admissible range. For \(a\ge a_c(t)\), \(E(0)=1\), \(E(1)=U\le1\), the displayed quadratic difference is strictly positive for all integers \(k\ge1\), and \(E(k)\to0\). Therefore \(E\) is a genuine innovation survival with \(0<V<U\le1\), and \(U=1\) exactly at \(a=a_c(t)\). Stationarity follows from \(S_X(k)=E(k)\Pr(\sum_{j=1}^{X+1}G_j\ge k)\) for every \(k\).

**2. Conditional stochastic ordering.** Coupling the thinned sums for states \(y\) and \(y+1\) by adding one independent nonnegative geometric summand shows that \(\Pr(\sum_{j=1}^{y+2}G_j\ge k)>\Pr(\sum_{j=1}^{y+1}G_j\ge k)\) for each integer \(k\ge1\); the strict inequality follows, for instance, from the event that the shorter sum equals \(k-1\) and the additional summand is positive. Multiplication by \(E(k)>0\) proves strict first-order stochastic monotonicity of \(K(y,\cdot)\).

**3. The exact two-column determinant.** The first two conditional tails of the sum are
\[
\Pr(N_y\ge1)=1-r^{y+1},\qquad
\Pr(N_y\ge2)=1-r^{y+1}[1+(y+1)q].
\]
As \(K(y,x)=E(x)\Pr(N_y\ge x)-E(x+1)\Pr(N_y\ge x+1)\), subtraction yields
\[
K(y,0)=1-U+Ur^{y+1},
\]
\[
K(y,1)=U-V+r^{y+1}[-U+V\{1+(y+1)q\}].
\]
Multiplying these two expressions at consecutive preceding states, and using \(r+q=1\), gives \(\Delta_y=-qr^{y+1}B_a(y)\), exactly as claimed.

**4. A positive-coefficient certificate for the initial sign.** We must show \(B_a(0)<0\), including at arbitrary positive parameters. Since \(2r-1-r^2=-q^2\),
\[
B_a(0)=-N(a,t),\qquad N(a,t)=U(1+Vq^2)-2qV.
\]
Set \(L=a(t+1)+t\), \(H_j=a(t+1)^3+t^3+2t^2+jt\) for \(j=2,3\). Exact rational simplification gives
\[
N(a,t)=\frac{L^2Q(a,t)}{a(a+1)^2(t+1)^6H_2H_3},
\qquad Q(a,t)=\sum_{j=0}^3a^jP_j(t),
\]
where
\[
\begin{aligned}
P_0(t)&=t(t^8+7t^7+21t^6+44t^5+66t^4+64t^3+45t^2+19t+3),\\
P_1(t)&=(t+1)(3t^8+19t^7+47t^6+78t^5+92t^4+60t^3+29t^2+9t+1),\\
P_2(t)&=t^2(t+1)^2(3t^5+17t^4+32t^3+35t^2+29t+6),\\
P_3(t)&=t^2(t+1)^3(t^4+5t^3+6t^2+t+1).
\end{aligned}
\]
Every displayed coefficient is nonnegative, each \(P_j\) is positive at \(t>0\), and the denominator is positive. Thus \(N(a,t)>0\) and \(B_a(0)<0\) for all \(a,t>0\). These are finite rational identities, not experimental extrapolations; `verify.py` verifies them by symbolic reduction.

**5. The unique sign transition.** At \(a=a_c(t)\), \(U=1\), hence
\[
B_a(y)=V-1-Vr^{y+2}<0\qquad (y\ge0),
\]
and every \(\Delta_y\) is strictly positive. At an interior parameter \(a>a_c(t)\), \(0<V<U<1\), and
\[
B'_a(z)=qV(1-U)-UVr^{z+2}\log r>0,
\qquad \lim_{z\to\infty}B_a(z)=+\infty.
\]
Together with \(B_a(0)<0\), this proves existence and uniqueness of a real zero \(z_*>0\), with exactly the asserted signs at integer indices. In particular a negative adjacent minor exists for all sufficiently large integer \(y\), disproving TP2 on the interior of the parameter region.

**6. Critical escape rate.** Fix \(t>0\), and denote \(a_c=a_c(t)\), \(V_c=V(a_c,t)\), \(q_c=a_c/(1+a_c)\). Let
\[
\kappa_t=\left.\frac{\partial(1-U(a,t))}{\partial a}\right|_{a=a_c}
=\frac{t^2(t+1)(t+2)[2a_c(t+1)+t-1]}{D(a_c,t)}>0.
\]
The positivity follows because \(a_c\) is the simple positive root of the upward-opening quadratic \(F\). Since \(B_{a_c}(z)<0\) at every finite \(z\), continuity and uniqueness imply \(z_*(a,t)\to\infty\) as \(a\downarrow a_c\). Substituting \(z_*\) into \(B_a(z_*)=0\), then taking the limit, gives
\[
\lim_{a\downarrow a_c}(1-U(a,t))z_*(a,t)
=\frac{1-V_c}{q_cV_c}.
\]
Since \((1-U(a,t))/(a-a_c)\to\kappa_t\), the sharp divergence law is
\[
\boxed{\lim_{a\downarrow a_c}(a-a_c)z_*(a,t)
=\frac{1-V_c}{q_cV_c\kappa_t}>0.}
\]

## Verification

The accompanying `verify.py` (Python 3 with SymPy) reconstructs the closed innovation survival for indices zero through three, symbolically verifies the exact admissibility factorization and its positive root, checks the all-positive polynomial certificate, and derives the adjacent determinant at four separate symbolic state indices. The latter is independently proved for **all** indices in Step 3. The program additionally provides an exact-rational witness: at \((a,t)=(1,1)\), \(U=45/52\), \(V=81/112\), and
\[
\Delta_3=\frac{225}{458752}>0,\qquad
\Delta_4=-\frac{2277}{3407872}<0.
\]
Run `python verify.py` from the extracted package. The proof, rather than numerical tests, establishes the infinite-state and boundary assertions.

## Relationship to prior work

Stojanović, Bakouch, Bojičić, Alomair and Alghamdi (2024) introduced the PL-MINAR process, its thinning and innovation survival functions, and transition probabilities. The present result **does not claim** those formulas or stationarity as new. Its claim is the explicit adjacent likelihood-ratio sign reversal, the exact boundary without that reversal, strict conditional stochastic ordering, and the critical divergence law. The original article's inspected theoretical and appendix sections address transition probabilities, conditional moments, autocorrelation, and estimation, not a sign classification of adjacent minors.

Qian and Zhu (2022) studied a modified-negative-binomial minification model driven by explanatory variables, focusing on ergodicity, estimation and specification testing; its accessible abstract does not establish this PL-specific sign law, although its full text was unavailable for comparison. Irshad, Aswathy and Maya (2026) treated a different Poisson-weighted-exponential minification marginal and transitions, not this Poisson–Lindley two-column classification. Standard total positivity and stochastic-order criteria are prior mathematical tools, not discoveries asserted here.

## Limitations

The sign classification concerns **only** the two lowest output columns of the kernel, with consecutive preceding states; it does not classify every higher-column minor, establish any global MLR order, or characterize reversibility. At the critical endpoint the displayed minors are positive, but no global TP2 assertion is made. The result is an analytic theorem about a count Markov model, not an empirical finding on financial datasets. The closest general minification source (Qian and Zhu, 2022) was assessed from its accessible publisher abstract rather than its full body; absolute historical priority cannot be certified from the completed literature search. No independent validation has been performed.

## References

1. Stojanović, V. S., Bakouch, H. S., Bojičić, R., Alomair, G., and Alghamdi, S. A. (2024). *Poisson-Lindley minification INAR process with application to financial data*. AIMS Mathematics **9**(8), 22627–22654. First publicly available 22 July 2024. https://doi.org/10.3934/math.20241102. Full text: https://www.aimspress.com/aimspress-data/math/2024/8/PDF/math-09-08-1102.pdf.
2. Qian, L., and Zhu, F. (2022). *A new minification integer-valued autoregressive process driven by explanatory variables*. Australian & New Zealand Journal of Statistics **64**(4), 478–494. First published 28 December 2022. https://doi.org/10.1111/anzs.12379.
3. Aleksić, M. S., and Ristić, M. M. (2021). *A geometric minification integer-valued autoregressive model*. Applied Mathematical Modelling **90**, 265–280. https://doi.org/10.1016/j.apm.2020.08.047.
4. Irshad, M. R., Aswathy, S., and Maya, R. (2026). *The new Poisson weighted exponential minification INAR(1) process*. OPSEARCH, first published 21 October 2026. https://doi.org/10.1007/s12597-026-01308-6.

5. Barreto-Souza, W., Ndreca, S., Silva, R. B., and Silva, R. W. C. (2023). *Non-linear INAR(1) processes under an alternative geometric thinning operator*. TEST **32**, 695–725. https://doi.org/10.1007/s11749-023-00849-y.
