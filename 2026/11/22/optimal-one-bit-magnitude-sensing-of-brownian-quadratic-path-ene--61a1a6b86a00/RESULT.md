# Optimal one-bit magnitude sensing of Brownian quadratic path energy

## Finding
Let \(W=(W_t)_{0\le t\le1}\) be standard real Brownian motion and let \(Q=\int_0^1W_t^2\,dt\). Choose a nonadaptive observation time \(x\in[0,1]\), encode the single observation \(W_x\) into **one bit** by an arbitrary measurable binary encoder (independent randomization is also permitted), and estimate \(Q\) from that bit under squared-error loss. The unique globally optimal time is \(x_*=3/4\). Up to swapping bit labels and changing a null set, its unique optimal binary encoder is
\[
B=\mathbf1_{\{|W_{3/4}|\ge a_*\sqrt{3/4}\}},
\]
where \(a_*=1.4820724357010611922\ldots\) is the unique positive solution of
\[
2a^2=2+a\varphi(a)\left(\frac1{\overline\Phi(a)}-\frac1{\Phi(a)-1/2}\right).
\]
Here \(\varphi(a)=e^{-a^2/2}/\sqrt{2\pi}\), \(\Phi\) is the standard normal distribution function, and \(\overline\Phi=1-\Phi\). The exact optimal Bayes risk and fraction of the prior variance explained by the bit are
\[
R_*=\frac13-\frac9{64}F_*,\qquad
\frac{\operatorname{Var}(\mathbb E[Q\mid B])}{\operatorname{Var}(Q)}=\frac{27}{64}F_*,\qquad
F_*=\frac{a_*^2\varphi(a_*)^2}{\overline\Phi(a_*)[\Phi(a_*)-1/2]}.
\]
Numerically, \(R_*=0.14988946812524375783\ldots\) and the explained fraction is \(0.55033159562426872649\ldots\). The high-energy bit occurs with probability \(0.13832102221257685755\ldots\). Both decoder values are specified exactly below.

## Assumptions and scope
The Brownian motion starts at zero, has \(\mathbb E[W_sW_t]=\min(s,t)\) and unit diffusion scale. The functional \(Q\) is the ordinary Lebesgue integral of the squared sample path. The time \(x\) is fixed before observing the path, exactly one noiseless value \(W_x\) is available to the encoder, and the transmitted alphabet has two values. The encoder may be any Borel map into that alphabet, not necessarily a sign comparator, or a stochastic kernel implemented using random noise independent of \(W\). The decoder may be any two real numbers; an optimal decoder is the conditional mean. The criterion is unconditional expected squared error, not worst-case pathwise error. At \(x=0\), the observation is deterministic and no information is available.

## Proof
**1. Gaussian projection of the energy.** For \(x>0\), put \(Z=W_x/\sqrt{x}\). Gaussian regression gives, for every \(t\in[0,1]\),
\[
\mathbb E[W_t^2\mid W_x]
=t+\frac{\min(t,x)^2}{x^2}(W_x^2-x).
\]
Integrating and using \(\int_0^1\min(t,x)^2dt=x^2(1-2x/3)\) yields
\[
\mathbb E[Q\mid W_x]=\frac12+g(x)(Z^2-1),\qquad
 g(x)=x\left(1-\frac{2x}{3}\right).
\]
By the Gaussian fourth-moment identity, \(\mathbb E[Q]=1/2\) and
\[
\operatorname{Var}(Q)
=2\int_0^1\int_0^1\min(s,t)^2\,ds\,dt=\frac13.
\]
Since a bit depends on \(W_x\) alone, \(\mathbb E[Q\mid B]=1/2+g(x)\mathbb E[Z^2-1\mid B]\). Thus the design separates into maximizing \(g(x)^2\) over time and maximizing the between-cell variance of \(Z^2\) over encoders. The strictly concave quadratic \(g(x)\) is positive for \(0<x\le1\), with its unique maximum \(g(3/4)=3/8\).

**2. Arbitrary binary encoders reduce to magnitude thresholds.** Write \(Y=Z^2\), with its continuous \(\chi^2_1\) law. A randomized encoder may be described by \(r(y)=\mathbb P(B=1\mid Y=y)\in[0,1]\); conditioning on \(Y\) loses nothing because the target projection depends on \(Z\) only through \(Y\). Set \(p=\mathbb E[r(Y)]\) and \(m=\mathbb E[(Y-1)r(Y)]\). For \(0<p<1\), direct two-cell conditioning gives
\[
\operatorname{Var}(\mathbb E[Y\mid B])=\frac{m^2}{p(1-p)}.
\]
Exchanging bit labels changes \(m\) to \(-m\) without changing the objective, so assume \(m\ge0\). For any fixed \(p\in(0,1)\), the rearrangement (bathtub) argument uniquely maximizes \(m\) over all \(0\le r\le1\): choose exactly the top \(p\)-probability tail of \(Y\). Indeed, for the unique upper-tail cutoff \(c\) satisfying \(\mathbb P(Y\ge c)=p\),
\[
\mathbb E[(Y-c)(\mathbf1_{\{Y\ge c\}}-r(Y))]\ge0,
\]
with equality only when \(r(Y)=\mathbf1_{\{Y\ge c\}}\) almost surely, since \(Y\) has no atom at \(c\). Therefore every nontrivial globally optimal binary encoder, up to bit swapping, must be a magnitude threshold \(\mathbf1_{\{|Z|\ge a\}}\), \(a=\sqrt c\). A constant bit explains no variance and cannot be optimal.

**3. Exact threshold objective and conditional decoding.** Write \(q=\overline\Phi(a)\) and \(b=\Phi(a)-1/2\), so the upper and lower bit probabilities are \(2q\) and \(2b\). Gaussian integration by parts gives
\[
\mathbb E[(Z^2-1)\mathbf1_{\{|Z|\ge a\}}]=2a\varphi(a).
\]
Consequently the explained variance of \(Y\) is exactly
\[
F(a)=\frac{a^2\varphi(a)^2}{q b}.
\]
The corresponding conditional means of \(Y\) are
\[
\mu_+(a)=1+\frac{a\varphi(a)}q,\qquad
\mu_-(a)=1-\frac{a\varphi(a)}b.
\]
For the optimal time, the optimal estimate is \(\widehat Q=1/2+(3/8)(\mu_+(a_*)-1)\) if the bit is one and \(\widehat Q=1/2+(3/8)(\mu_-(a_*)-1)\) otherwise. These values are \(1.5690062644358755\ldots\) and \(0.3283977640627816\ldots\), respectively.

**4. A unique global threshold.** Let \(c=a^2>0\) and \(\mu_-(c)=\mathbb E[Y\mid Y<c]\), \(\mu_+(c)=\mathbb E[Y\mid Y\ge c]\). The within-cell mean-square error is \(D(c)=\mathbb E[(Y-\mathbb E[Y\mid B])^2]\); differentiating by the cell boundary (the derivatives of the optimal cell centroids cancel) gives
\[
D'(c)=f_Y(c)[\mu_+(c)-\mu_-(c)] [2c-\mu_-(c)-\mu_+(c)],
\]
where \(f_Y(c)>0\). Thus \(F=\operatorname{Var}(Y)-D\) increases when \(\mu_-/c+\mu_+/c>2\), and decreases when the sum is below two.

We prove that the ratio sum decreases strictly from infinity to one. For \(0<Y<c\), the conditional density of \(Y/c\) on \((0,1)\) is proportional to \(u^{-1/2}e^{-cu/2}\); increasing \(c\) produces a strict decreasing exponential tilt, so \(\mu_-(c)/c\) strictly decreases. For \(Y\ge c\), the conditional survival function of \(Y/c\) at \(u>1\) is \(\overline\Phi(\sqrt{cu})/\overline\Phi(\sqrt c)\). It decreases strictly with \(c\) because the positive normal upper-tail hazard \(h(z)=\varphi(z)/\overline\Phi(z)\) is strictly increasing: \(h'(z)=h(z)(h(z)-z)>0\) for \(z>0\), using the standard strict Gaussian tail inequality \(\overline\Phi(z)<\varphi(z)/z\). Hence \(\mu_+(c)/c\) strictly decreases. As \(c\downarrow0\), the first ratio tends to \(1/3\) and the second diverges. As \(c\to\infty\), the first tends to zero and the second tends to one (e.g., from Gaussian Mills asymptotics). By continuity there is exactly one solution \(\mu_-+\mu_+=2c\), and the objective strictly increases before it and strictly decreases after it. Substitution of the exact conditional means gives the displayed scalar equation for \(a_*\). This proves existence, uniqueness, and globality without assuming numerical optimization or checking only comparator thresholds.

**5. Risk and the comparison to other bits.** For any time and encoding, the Bayes risk is \(1/3-g(x)^2\operatorname{Var}(\mathbb E[Y\mid B])\), and the preceding steps yield the claimed optimum. A zero-threshold sign bit \(\mathbf1_{\{W_x>0\}}\) has zero explained variance for every \(x\), since \(Y\) is independent of the sign of a centered normal. By comparison, observing the complete real value \(W_{3/4}\) yields explained variance \(2(3/8)^2=9/32\), or \(27/32\) of the prior \(1/3\). The optimal one-bit fraction is strictly between these two benchmarks.

## Verification
A standalone Python 3 verifier (`verify.py`) requires `mpmath`; it checks rational identities for the Brownian covariance projection and prior variance, evaluates the unique-root equation and Gaussian tail integrals at high precision, verifies the two decoder conditional means, and checks sample monotonicity inequalities. Execute `python verify.py` with mpmath available. Its observed output is in `verification_output.txt`. The mathematical quantifiers (all \(x\), all measurable randomized encoders, uniqueness of the threshold) are established by the preceding analytic arguments, not inferred from finite tests.

## Relationship to prior work
Foster, Lyons and Oberhauser (arXiv:1904.06998; first public 2019-04-15), *An optimal polynomial approximation of Brownian motion*, develops Brownian path approximation and conditional expectations of quadratic Wiener functionals; its Theorem 3.7 uses full Gaussian observations including endpoint and area. It does not state an unrestricted one-bit energy-observation design or this exact threshold and risk. Fesl, Koller and Utschick (arXiv:2212.04470; first public 2022-12-08), *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, studies conditional-mean estimation for sign-quantized Gaussian linear channels, a materially different target and encoder class. Guo and Kostina (arXiv:1909.01317; first public 2019-09-03) optimize causal rate-constrained sampling to track the Wiener path itself; their freely informative stopping times and pathwise tracking loss are different from one preselected snapshot used to estimate a single quadratic integral. General binary scalar Lloyd–Max quantization and the conditional-mean decoder are classical; they are used here rather than claimed as inventions. The optimized **full-valued** one-point Brownian energy time is also known; the asserted distinction concerns the unrestricted one-bit magnitude encoder, its unique threshold and sharp loss of information.

## Limitations
This theorem applies to a single preselected noiseless snapshot, standard Brownian motion, integrated quadratic path energy, a two-symbol message, and mean-square Bayes risk. It does not optimize variable-rate encoders, multiple observations, adaptive observation times, extra external sensor information, independent observation noise, non-Gaussian paths, or a Brownian bridge. The first-public-source date identifies motivating literature, not the date this theorem became public. Independent scrutiny of historical priority remains necessary; general two-level quantizer optimality is acknowledged prior art.

## References
- James Foster, Terry Lyons, Harald Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998, initial submission 2019-04-15, https://arxiv.org/abs/1904.06998 . Relevant material: introduction, Section 3 and Theorem 3.7.
- Benedikt Fesl, Michael Koller, Wolfgang Utschick, *On the Mean Square Error Optimal Estimator in One-Bit Quantized Systems*, arXiv:2212.04470, initial submission 2022-12-08, https://arxiv.org/abs/2212.04470 . Relevant material: Sections I–III and one-bit conditional mean model.
- Nian Guo, Victoria Kostina, *Optimal Causal Rate-Constrained Sampling of the Wiener Process*, arXiv:1909.01317, initial submission 2019-09-03, https://arxiv.org/abs/1909.01317 . Relevant material: introduction, observation model and distortion criterion.
- S. P. Lloyd, *Least Squares Quantization in PCM*, IEEE Transactions on Information Theory 28 (1982), 129–137 (originally circulated 1957); DOI:10.1109/TIT.1982.1056489 . General two-cell scalar quantization context.
