# Reentrant attraction of segregated platform equilibria near indifference

## Finding

In the counterfactual-learning, two-opinion/two-platform differential equation of Banisch, Jacob, Willaert and Olbrich [1], the nonzero segregated equilibria can **regain local exponential stability** at high diversity preference, before disappearing at the indifference threshold. The complete hyperbolic stability classification has a sharp exploration-strength boundary.

For \(0<b<1\), put
\[
B(b)=\frac{1}{b(1-b^2)}+\frac{\operatorname{artanh}b}{b},\qquad
N(b)=-1+3b^2+b(1-b^2)-(1-b^2)^2\operatorname{artanh}b.
\]
There is exactly one \(b_*\in(0,1)\) satisfying \(N(b_*)=0\); define \(\beta_*=B(b_*)=3.7309540014225286587\ldots\). When \(1<\beta<\beta_*\), both segregated equilibria are locally exponentially attracting throughout their entire existence interval. At \(\beta=\beta_*\), their transverse eigenvalue vanishes at exactly one parameter, and they are locally exponentially attracting elsewhere. For \(\beta>\beta_*\), \(B(b)=\beta\) has exactly two roots \(0<b_-<b_*<b_+<1\). Define
\[
\mu_{\mathrm{lo}}=1-\frac{\operatorname{artanh}b_+}{\beta b_+},\qquad
\mu_{\mathrm{hi}}=1-\frac{\operatorname{artanh}b_-}{\beta b_-},\qquad
\mu_c=1-\frac1\beta.
\]
Then \(0<\mu_{\mathrm{lo}}<\mu_{\mathrm{hi}}<\mu_c\). Each segregated equilibrium is locally exponentially attracting precisely for
\[
0\le\mu<\mu_{\mathrm{lo}}\quad\text{or}\quad \mu_{\mathrm{hi}}<\mu<\mu_c,
\]
and is a hyperbolic saddle precisely for \(\mu_{\mathrm{lo}}<\mu<\mu_{\mathrm{hi}}\). At either transition the transverse eigenvalue is zero; local exponential stability is not asserted there. For \(\beta\le1\), no nonzero segregated equilibrium exists with \(0\le\mu\le1\).

At the article's \(\beta=8\),
\[
\mu_{\mathrm{lo}}\simeq0.7907998096325710,\qquad
\mu_{\mathrm{hi}}\simeq0.8740987424930559,\qquad
\mu_c=0.875.
\]
Thus \(0.8740987424930559<\mu<0.875\) is a narrow **second stable-segregation window** in the two-dimensional equation. In particular at \(\mu=0.8745\), both segregated fixed points have strictly negative eigenvalues, contradicting the claim of a unique mega-platform attractor across the entire \(0.79<\mu<0.875\) interval if that claim is interpreted for the reduced differential equation. No assertion is made about the four-dimensional frequency-weighted model or the agent-based simulation.

## Assumptions and scope

Let \(\alpha>0\), \(\beta>0\) and \(0\le\mu\le1\). The state is \((X,Y)=(\Delta Q^+,\Delta Q^-)\in\mathbb R^2\), the two groups' platform-2 minus platform-1 learned values. Define
\[
p_1^+=\frac{1}{1+e^{\beta X}},\quad p_1^-=\frac{1}{1+e^{\beta Y}},\quad
p_2^\pm=1-p_1^\pm,\qquad
O_k=\frac{p_k^+-p_k^-}{p_k^++p_k^-}.
\]
All denominators are strictly positive for finite \((X,Y)\). For each platform \(k\in\{1,2\}\), set
\[
r_k^+=(1-\mu)O_k+\mu(1-|O_k|),\qquad
r_k^-=-(1-\mu)O_k+\mu(1-|O_k|).
\]
The governing equation is precisely the counterfactual two-dimensional reduction [1, Eq. (14)]:
\[
\dot X=\alpha(r_2^+-r_1^+-X),\qquad
\dot Y=\alpha(r_2^--r_1^--Y).
\]
An equilibrium is *segregated* if \((X,Y)=(v,-v)\) or \((-v,v)\) for some \(v>0\). Stability always means local exponential attraction in the full **two-dimensional** \((X,Y)\) phase space. The boundaries \(\mu=\mu_{\mathrm{lo}},\mu_{\mathrm{hi}},\mu_c\) are not assigned hyperbolic stability labels.

## Proof

**Invariant segregation line and its unique nonzero equilibrium.** Write \(U=(X+Y)/2\), \(V=(X-Y)/2\). When \(U=0\), \(V>0\), the logistic probabilities give
\[
O_1=-b,\quad O_2=b,\quad b=\tanh(\beta V/2)\in(0,1).
\]
The diversity terms cancel between platforms, hence
\[
\dot U=0,\qquad \dot V=\alpha\left[2(1-\mu)\tanh(\beta V/2)-V\right].
\]
For a positive fixed point, \(V=2(1-\mu)b\) and therefore
\[
\frac{\operatorname{artanh}b}{b}=\beta(1-\mu).\tag{1}
\]
The function \(h(b)=\operatorname{artanh}b/b\) is strictly increasing on \((0,1)\), starting at \(1\) and diverging to infinity: indeed, with \(k(b)=b/(1-b^2)-\operatorname{artanh}b\), \(k(0)=0\) and \(k'(b)=2b^2/(1-b^2)^2>0\), so \(h'(b)=k(b)/b^2>0\). Thus exactly one positive solution of (1) exists iff \(\beta(1-\mu)>1\). The symmetric negative solution follows by interchanging the platforms. This also establishes that \(b\) decreases strictly with \(\mu\) along the branch.

**Full transverse and longitudinal linearization.** Near a segregated equilibrium, \(O_1<0<O_2\), so all absolute values have fixed signs and the vector field is smooth. The equations in \((U,V)\) become
\[
\dot U=\alpha[-\mu(O_1+O_2)-U],\qquad
\dot V=\alpha[(1-\mu)(O_2-O_1)-V].
\]
On \(U=0\), differentiation of the explicit logistic fractions yields
\[
\partial_U(O_1+O_2)=-\beta b(1-b^2),\qquad
\partial_V(O_2-O_1)=\beta(1-b^2).
\]
The two cross derivatives are zero at \(U=0\) by platform-exchange symmetry (or direct differentiation). Consequently the two eigenvalues of the **unrestricted** two-dimensional Jacobian are
\[
\lambda_U=\alpha[\beta\mu b(1-b^2)-1],\qquad
\lambda_V=\alpha[\beta(1-\mu)(1-b^2)-1].\tag{2}
\]
Equation (1) and the strict inequality \(\operatorname{artanh}b<b/(1-b^2)\) give \(\lambda_V<0\) everywhere on the nonzero branch. Substituting \(\beta\mu=\beta-\operatorname{artanh}b/b\) into (2) gives
\[
\frac{\lambda_U}{\alpha}=b(1-b^2)[\beta-B(b)].\tag{3}
\]
Hence only the transverse mode can lose or regain exponential stability.

**Exactly one minimum and two transverse crossings.** Direct differentiation gives
\[
B'(b)=\frac{N(b)}{b^2(1-b^2)^2},\qquad
N'(b)=2b\left[3-b+2(1-b^2)\operatorname{artanh}b\right]>0.
\]
Moreover \(N(0+)=-1\) and \(N(1-)=2\), so \(N\) has exactly one zero \(b_*\), and \(B\) decreases strictly to its global minimum \(\beta_*\) and increases strictly thereafter, diverging at both endpoints. For \(\beta>\beta_*\), this yields exactly two roots \(b_-<b_+\). Both belong to the physical branch: its largest value \(b_{\max}\) at \(\mu=0\) satisfies \(h(b_{\max})=\beta\), whereas \(B(b_+)=\beta>h(b_+)\); thus \(b_+<b_{\max}\), and trivially \(b_-<b_{\max}\). In particular their mapped diversity values are strictly between \(0\) and \(\mu_c\). Since \(b\) decreases with \(\mu\), equation (3) proves the two stable intervals and the intervening saddle interval. For \(1<\beta<\beta_*\), \(\beta<B(b)\) everywhere, so (3) and \(\lambda_V<0\) prove stability. At equality there is exactly one transverse zero.

**Explicit narrow return at \(\beta=8\).** Bisection for the two roots of \(B(b)=8\) yields \(b_-\simeq0.1461245459140042\), \(b_+\simeq0.9088936483736821\) and the stated \(\mu\) thresholds. For \(\mu=0.8745\), solving (1) gives \(b\simeq0.1091517336340213\), and (2) gives \(\lambda_U/\alpha\simeq-0.24547238313503\), \(\lambda_V/\alpha\simeq-0.00796175735913\). Both are strictly negative; the opposite segregated state has identical eigenvalues by symmetry.

## Verification

The accompanying `verify.py` uses only Python's standard library. It reconstructs the exact model reward difference, brackets the minimum and two crossings with bisection, compares the formulae for both eigenvalues against independent finite differences of the original two-dimensional system, checks the equilibrium residuals and tests the stable–saddle–stable sequence. Run `python3 verify.py`. The source algebra and monotonicity proof, not finite numerical tests, establish the uniform parameter classification. Numbers displayed above are rounded; the defining equations give the exact thresholds.

## Relationship to prior work

Banisch, Jacob, Willaert and Olbrich [1] introduce both the four-dimensional learning equation and the counterfactual two-dimensional reduction used here. Their main-text bifurcation discussion reports segregated fixed points stable approximately until \(\mu=0.79\) at \(\beta=8\), then a region \(0.79<\mu<0.875\) in which the mega-platform state is said to be the only stable equilibrium [1, Section "Analytical characterization," Figure 9]. The present result works with **the same reduced equations** and identifies a second, approximately \(0.00090126\)-wide segregated-stability window omitted by that numerical description; their plot sampled diversity at increments of \(0.005\). The transverse threshold and the complete exploration-strength classification are not implied by the previously reported first crossing. Banisch and Olbrich [2] study polarization by reinforcement on fixed social networks, not this two-platform choice equation with the diversity-reward parameter.

## Limitations

This is **local** stability in the two-dimensional counterfactual-learning ODE, not a global phase portrait, a basin-size estimate, or a statement about uniqueness of all other equilibria. It does not establish the same reentrant stability in the frequency-weighted four-dimensional Q-value ODE or stochastic agent-based models. It does not classify nonlinear behavior at the two transverse eigenvalue-zero boundaries. The source's referenced supplemental PDF could not be inspected; an equivalent calculation there or elsewhere cannot be ruled out solely by title/search comparisons.

## References

[1] S. Banisch, D. Jacob, T. Willaert, and E. Olbrich, "The social dilemma of online segregation: A dynamical model of platform choice," *Rationality and Society* 38 (2026), 137–183, first online March 24, 2026. https://doi.org/10.1177/10434631261428850 (full text: https://journals.sagepub.com/doi/full/10.1177/10434631261428850).

[2] S. Banisch and E. Olbrich, "Opinion polarization by learning from social feedback," *Journal of Mathematical Sociology* 43 (2019), 76–103; first online October 10, 2018. https://doi.org/10.1080/0022250X.2018.1517761.
