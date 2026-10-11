# Sharp score-jet realizability and two-point recovery in Gaussian empirical Bayes
## Finding
Fix a covariate value and consider
\[
Y\mid\theta,x\sim N(\theta,\sigma^2),\qquad \sigma>0.
\]
Let \(m(y\mid x)\) be the conditional marginal density, \(s(y,x)=\partial_y\log m(y\mid x)\), and
\[
r(y,x)=y+\sigma^2s(y,x).
\]
If the posterior \(\theta\mid Y=y,x\) has a finite fourth moment and \(s(\cdot,x)\) is three times differentiable at \(y\), every genuine Gaussian empirical-Bayes marginal satisfies
\[
r'(y,x)\ge0
\]
and
\[
\sigma^2\bigl(r'r'''-(r'')^2\bigr)+2(r')^3\ge0.
\]
Equivalently,
\[
\sigma^4(1+\sigma^2s')s'''-\sigma^6(s'')^2+2(1+\sigma^2s')^3\ge0.
\]
All derivatives are with respect to \(y\) at fixed \(x\).

If \(r'(y,x)>0\), equality at even one observation occurs if and only if the conditional prior \(\theta\mid x\) is supported on exactly two points. In that case equality holds for every observation, and one local score jet reconstructs the prior. Set
\[
v=\sigma^2r',\qquad c=\sigma^4r'',\qquad d=\sqrt{(c/v)^2+4v},\qquad \mu=r(y,x).
\]
Then
\[
a=\mu+\frac{c/v-d}{2},\qquad b=\mu+\frac{c/v+d}{2},
\]
where \(a<b\). The posterior mass at \(b\) is
\[
p_y=\frac{1-c/(vd)}{2},
\]
and the prior odds for \(b\) versus \(a\) are
\[
\frac{\pi_b}{1-\pi_b}
=
\frac{p_y}{1-p_y}
\exp\!\left(-\frac{d\,[y-(a+b)/2]}{\sigma^2}\right).
\]

## Assumptions and scope
The theorem is pointwise in \(x\). The noise variance is known and positive. The finite fourth posterior moment and three score derivatives are required at the observation. The equality characterization assumes \(r'>0\); a one-point prior has \(r'=0\) and is excluded from the reconstruction formulas.

This is a necessary realizability condition for a score intended to arise from Gaussian convolution. It is not a sufficient characterization of globally valid marginal scores.

## Proof
Sugasawa and Zhao derive the posterior moment-generating identity
\[
M_{\theta\mid y,x}(t)
=
\exp\!\left(
yt+\frac{\sigma^2t^2}{2}
+\int_y^{y+\sigma^2t}s(z,x)\,dz
\right).
\]
Differentiating its logarithm at \(t=0\) gives the posterior cumulants
\[
\kappa_1=r,\qquad
\kappa_2=\sigma^2+\sigma^4s'=\sigma^2r',
\]
\[
\kappa_3=\sigma^6s''=\sigma^4r'',\qquad
\kappa_4=\sigma^8s'''=\sigma^6r'''.
\]
Hence \(r'\ge0\) follows from posterior-variance nonnegativity.

For any centered random variable \(X\) with variance \(v>0\), third central moment \(\mu_3\), and fourth central moment \(\mu_4\),
\[
\mathbb E\!\left[
\left(X^2-\frac{\mu_3}{v}X-v\right)^2
\right]
=
\mu_4-\frac{\mu_3^2}{v}-v^2\ge0.
\]
Thus
\[
v\mu_4-\mu_3^2-v^3\ge0.
\]
Since \(\mu_3=\kappa_3\) and \(\mu_4=\kappa_4+3v^2\), this becomes
\[
v\kappa_4+2v^3-\kappa_3^2\ge0.
\]
Substituting the cumulants above gives both score-jet forms.

Equality holds precisely when
\[
X^2-\frac{\mu_3}{v}X-v=0
\]
almost surely. For \(v>0\), the quadratic has two distinct real roots, so the posterior is supported on exactly two points; every nondegenerate two-point posterior attains equality. A Gaussian likelihood is strictly positive for every finite \(\theta\), so posterior and conditional prior have the same support. Equality at one observation therefore characterizes an exactly two-point conditional prior and then persists for every observation.

For posterior mass \(p_y\) at \(b\), mass \(1-p_y\) at \(a\), and \(d=b-a>0\), direct moment calculation gives
\[
v=p_y(1-p_y)d^2,\qquad \frac{c}{v}=(1-2p_y)d.
\]
Consequently
\[
d^2=(c/v)^2+4v,\qquad p_y=\frac{1-c/(vd)}{2},
\]
and the formulas for \(a\) and \(b\) follow by centering at \(\mu\). Bayes' rule gives
\[
\frac{p_y}{1-p_y}
=
\frac{\pi_b}{1-\pi_b}
\exp\!\left(\frac{d\,[y-(a+b)/2]}{\sigma^2}\right),
\]
which yields the prior-odds formula.

## Verification
The standalone verifier uses exact rational arithmetic to check Pearson equality and exact recovery for a two-point posterior, strict inequality for a three-point posterior, and a smooth density that passes the variance check but violates the fourth-order condition.

For the last check, take \(\sigma^2=1\) and the valid density proportional to \(\exp(-y^4/4)\). Its score is \(s(y)=-y^3\). At \(y=0\), the variance surrogate is \(1+s'(0)=1>0\), while the fourth-order expression is
\[
1\cdot1\cdot(-6)-0+2\cdot1=-4<0.
\]
Thus this smooth density cannot be a unit-Gaussian convolution marginal, showing that nonnegative Tweedie variance alone is insufficient.

Run `python VERIFY.py`; the expected terminal line is `VERIFY_OK`.

## Relationship to prior work
Sugasawa and Zhao's 2026 conditional f-modeling paper supplies the posterior moment-generating identity and uses score derivatives for posterior moments. The result here imposes a sharp fourth-moment positivity constraint on that score jet, identifies the equality case globally through conditional-prior support, and gives closed-form recovery of that prior from one local jet.

Pericchi, Sansó, and Smith develop posterior cumulant relationships for exponential-family Bayesian models. Their broader cumulant framework covers the derivative-identities context but, in the material inspected, does not state this Pearson-induced score constraint or the equality-at-one-observation recovery theorem.

Pearson's skewness-kurtosis inequality is classical. Klaassen and van Es give a modern exact treatment and show boundary attainment by two-valued laws. The present theorem maps that moment boundary into Gaussian empirical-Bayes score geometry and uses positivity of the Gaussian likelihood to turn posterior equality into a prior-support characterization.

## Limitations
This is a necessary-condition theorem, not a full characterization of Gaussian-convolution marginals. It does not treat estimation error in fitted derivatives, approximate equality, multivariate latent effects, or simultaneous enforcement over all observations.

The full primary text of the 2026 preprint was not directly retrievable in the literature inspection; its primary abstract was checked and a detailed public exposition was used for the exact posterior-MGF formula. The full 1993 JASA article was also inaccessible. These access limitations leave residual risk that a related higher-order constraint appears under older exponential-family terminology.

## References
1. S. Sugasawa and Z. Zhao, *Beyond Tweedie's Formula: Conditional Score Modeling for Empirical Bayes Inference*, arXiv:2609.11136v1, first public 2026-09-10.
2. L. R. Pericchi, B. Sansó, and A. F. M. Smith, *Posterior Cumulant Relationships in Bayesian Inference Involving the Exponential Family*, Journal of the American Statistical Association 88 (1993), 1419–1426, DOI:10.1080/01621459.1993.10476427.
3. C. A. J. Klaassen and B. van Es, *Inference via the Skewness-Kurtosis Set*, International Statistical Review (2025), DOI:10.1111/insr.70007.
