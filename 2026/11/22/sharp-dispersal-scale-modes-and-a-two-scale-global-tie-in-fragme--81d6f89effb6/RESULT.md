# Sharp dispersal-scale modes and a two-scale global tie in fragmented habitat

## Finding
Let a disperser start at the origin on a one-dimensional transect and land after an unbiased Gaussian displacement of standard deviation \(\sigma>0\). Suppose the habitable destination set has exactly \(m\) separated *distance bands*, symmetrically placed about the origin:
\[
H=\bigcup_{j=1}^{m}\bigl([-b_j,-a_j]\cup[a_j,b_j]\bigr),\qquad
0<a_1<b_1<a_2<b_2<\cdots<a_m<b_m<\infty.
\]
Write \(P_H(\sigma)=\Pr\{\sigma Z\in H\}\) for \(Z\sim N(0,1)\). Then \(P_H\) has **at most \(m\) distinct strict local maxima** on \(\sigma>0\), and this bound is sharp for every positive integer \(m\): there exist genuine separated bands with exactly \(m\) strict local maxima. In particular, a single distance band has one and only one optimal dispersal scale.

The sharpness includes a global nonuniqueness phenomenon. Put
\[
H_{R,q}=[-2,-1]\cup[1,2]\cup[-Rq,-R]\cup[R,Rq],
\qquad R>2,\quad 3/2\le q\le2.
\]
For **every sufficiently large \(R\)**, there is a **unique** \(q_R\in(3/2,2)\) for which \(P_{H_{R,q_R}}\) has exactly two distinct, equal-height **global** maxima, at a near and a far dispersal scale. Its asymptotic boundary is
\[
q_R=2-\frac{2^{4/3}}{R}+O(R^{-2})\quad(R\to\infty).
\]
The proposition does not assert that this tie is unique over all \(q>1\), nor that a given small \(R\) is in the asymptotic regime.

An elementary concrete witness is \(H=[-12,-8]\cup[-2,-1]\cup[1,2]\cup[8,12]\). It has exactly two strict local maxima, near \(\sigma=1.4710725584\) and \(\sigma=8.0202203469\), separated by a strict local minimum near \(\sigma=3.7783833788\). The corresponding landing probabilities are approximately \(0.32267462\), \(0.28163359\), and \(0.22743038\), respectively (in the order first maximum, second maximum, middle minimum). The existence and count of the stationary points have an exact rational sign certificate below; the displayed coordinates are numerical illustrations.

## Assumptions and scope
Every distance band is closed, strictly separated from its neighbors and from zero, and has positive width. Endpoints have zero Gaussian probability. Only a single dispersal event and its probability of landing in one of the favorable bands are modeled. The landscape is fixed as \(\sigma\) varies, and Gaussian displacement is centered with common scale \(\sigma\). This is not an equilibrium population model, a persistence probability, a multi-generation invasion speed, or a field-calibrated management prescription.

The Gaussian distribution function and density are \(\Phi\) and \(\varphi\). For a symmetric band \([-b,-a]\cup[a,b]\), define
\[
B(s;a,b)=2\bigl[\Phi(b/s)-\Phi(a/s)\bigr],\quad 0<a<b,\ s>0.
\]
Thus \(P_H(\sigma)=\sum_j B(\sigma;a_j,b_j)\), and the two-scale construction is \(P_{H_{R,q}}(\sigma)=B(\sigma;1,2)+B(\sigma/R;1,q)\).

## Proof
**1. Derivative and the universal finite zero bound.** Differentiation gives
\[
P_H'(\sigma)=\frac{2}{\sqrt{2\pi}\,\sigma^2}
\sum_{j=1}^{m}\left[a_j e^{-a_j^2/(2\sigma^2)}-b_j e^{-b_j^2/(2\sigma^2)}\right].
\]
Put \(t=1/(2\sigma^2)\). The bracket is a nonzero linear combination of exactly \(2m\) exponentials with distinct real exponents (because all endpoints are strictly ordered). An \(N\)-term exponential sum with distinct real exponents has at most \(N-1\) distinct real zeros. Here is a self-contained argument: divide by the exponential with smallest exponent, obtaining a nonzero constant plus \(N-1\) exponentials; its derivative has \(N-1\) terms with distinct exponents. Induct on \(N\), using Rolle's theorem between successive zeros. The induction base is a nonzero single exponential. Thus \(P_H'\) has at most \(2m-1\) positive zeros. Between each two strict local maxima of a smooth function on an interval there is at least one distinct intervening stationary minimum (the function is nonconstant analytic here). Hence \(k\) strict local maxima demand at least \(2k-1\) distinct zeros, so \(k\le m\).

**2. One band.** For \(0<a<b\), the stationary equation is \(a e^{-a^2/(2s^2)}=b e^{-b^2/(2s^2)}\), with the unique solution
\[
s(a,b)^2=\frac{b^2-a^2}{2\log(b/a)}.
\]
The derivative is positive for sufficiently small \(s\) and negative for sufficiently large \(s\), so this is the unique strict global maximum. Write \(s(q)=s(1,q)\) and \(M(q)=B(s(q);1,q)\). The envelope theorem, or direct differentiation at a stationary point, yields
\[
M'(q)=\frac{2}{s(q)}\varphi\!\left(\frac{q}{s(q)}\right)>0.
\]
It follows that \(M\) is smooth and strictly increasing for \(q>1\).

**3. Sharpness for all band counts.** Suppose \(m-1\) bands give \(m-1\) strict local maxima. Append one more band \([R,2R]\) on the positive half-line and its reflection, with \(R\) larger than every old endpoint. On every compact positive \(\sigma\)-interval, the new band's probability and first derivative tend uniformly to zero as \(R\to\infty\), so the old derivative sign changes on small disjoint neighborhoods of its \(m-1\) maxima persist. On the new scale \(\sigma=Rs\), the old band's probability and its derivative with respect to \(s\) tend uniformly to zero on compact subsets of \(s>0\), while the new term is precisely \(B(s;1,2)\). Its strict derivative sign change at \(s(2)\) therefore creates another strict local maximum on the large scale. Thus the enlarged landscape has at least \(m\) strict local maxima; Step 1 bounds their count by \(m\). Starting from Step 2 proves attainability for every \(m\), without requiring tuned heights or zero-width intervals.

**4. Equal-height global optimum for two bands.** Fix \(q\) in \(Q=[3/2,2]\), and take \(R\to\infty\). The near-scale maximum of \(B(\sigma;1,2)+B(\sigma/R;1,q)\) is unique and nondegenerate near \(\sigma=s(2)\), with value
\[
N_R(q)=M(2)+O(e^{-cR^2})
\]
for some \(c>0\) uniform in \(q\in Q\). This follows by the strict second derivative at the one-band optimum and the exponentially small distant-band term on a fixed positive neighborhood. On the far scale \(\sigma=Ru\), the same function equals \(B(u;1,q)+B(Ru;1,2)\); the second term has the uniform \(C^2\) expansion
\[
B(Ru;1,2)=\frac{\sqrt{2/\pi}}{Ru}+O(R^{-3})
\]
when \(u\) stays in a positive compact interval. Consequently its unique far-scale maximum has value
\[
F_R(q)=M(q)+\frac{\sqrt{2/\pi}}{R s(q)}+O(R^{-2}),
\qquad F_R'(q)=M'(q)+O(R^{-1}),
\]
uniformly over \(q\in Q\). These expansions follow from the implicit-function theorem at the strict one-band peak; in particular the far maximizing \(u\) equals \(s(q)+O(R^{-1})\).

No third range of scales can compete globally. Indeed choose a large fixed \(K\) and a small fixed \(\varepsilon>0\) so that on \(K\le\sigma\le\varepsilon R\), both \(B(\sigma;1,2)\) and \(B(\sigma/R;1,q)\) are uniformly below an arbitrarily small positive bound; this uses the respective large- and small-argument tails, uniformly for \(q\in Q\). In the remaining near and far ranges the one-band unique peaks persist. Step 1 then precludes any additional local maximum. Accordingly the global maximizer(s) must be the near and/or far peaks.

Now \(F_R(3/2)-N_R(3/2)<0\) for large \(R\), because \(M(3/2)<M(2)\), whereas \(F_R(2)-N_R(2)>0\) because the far peak benefits from the positive \(R^{-1}\) correction. Moreover
\[
\frac{d}{dq}[F_R(q)-N_R(q)]=M'(q)+O(R^{-1})>0
\]
uniformly on \(Q\). Hence there is exactly one crossing \(q_R\in(3/2,2)\), and at the crossing exactly two distinct global peaks tie.

Finally, the crossing equation and smoothness imply \(q_R-2=O(R^{-1})\). Taylor expansion at \(q=2\) gives
\[
0=M'(2)(q_R-2)+\frac{\sqrt{2/\pi}}{Rs(2)}+O(R^{-2}).
\]
Since \(s(2)^2=3/(2\log2)\) and \(M'(2)=2\varphi(2/s(2))/s(2)\), the coefficient is
\[
\frac{\sqrt{2/\pi}}{s(2)M'(2)}
=\frac{\varphi(0)}{\varphi(2/s(2))}
=e^{2/s(2)^2}=2^{4/3}.
\]
This proves the claimed asymptotic.

**5. Exact two-band witness.** For \((a_1,b_1,a_2,b_2)=(1,2,8,12)\), substitute \(z=e^{-1/(2\sigma^2)}\), which increases strictly from zero to one with \(\sigma\). The derivative has the sign of
\[
p(z)=z-2z^4+8z^{64}-12z^{144}.
\]
Exact rational arithmetic gives \(p(3/5)>0\), \(p(7/8)<0\), \(p(49/50)>0\), and \(p(199/200)<0\). Thus there are at least three distinct derivative zeros in \(0<z<1\). Step 1 bounds them by three, so there are exactly three, with the signs alternating \(+,-,+,-\): two strict maxima and one strict minimum. The corresponding numerical roots and probability values displayed above are only approximations.

## Verification
Run \(python3 checker.py\) in the directory containing this result to reproduce exact rational sign tests, the numerical witness and the asymptotic coefficient checks. The exact polynomial sign evaluations and the analytic exponential zero bound establish the witness's complete stationary-point count. Numerical root finding and sampled asymptotics are diagnostics only; they do not certify the quantified statements for all \(m\) or all sufficiently large \(R\).

## Relationship to prior work
Dewhirst and Lutscher (2009) study invasion and average dispersal success in fragmented habitats using integrodifference equations, whereas this result concerns a single fixed-source landing probability optimized over the Gaussian standard deviation. Skelsey, With and Garrett (2012) demonstrate intermediate optimal spatial *habitat scaling* for a source–target pair; their varied quantity includes habitat size and gap, unlike the fixed multi-band landscape here. Lindström, Håkansson and Wennergren (2010 online) investigate kernel shape and width in patchy invasion simulations, a different objective.

The exponential-sum zero bound is a classical consequence of Rolle's theorem and is **not claimed as new**. The potentially new statement is its sharp attainability for Gaussian landing probabilities on separated habitat distance bands, together with the existence, uniqueness (in the stated range) and first-order shift of the equal-global-optimum two-scale boundary. The latter is not implied by the zero-count bound alone.

## Limitations
The result does not describe fitness, effective population size, stochastic establishment, survival during movement, movement costs, directional dispersal, multi-generation dynamics, or optimization over distributions other than centered Gaussian kernels. Uniform quality within each suitable band and a point release are essential modeling assumptions. This exact idealized benchmark may help diagnose nonconvex dispersal-scale optimization; it is not a validated prediction for a particular organism. Historical-priority checks were limited by incomplete access to some earlier kernel-shape studies and by the possibility of an equivalent result in Gaussian scale-space or exponential-polynomial literature.

## References
- Dewhirst, S. and Lutscher, F. (2009). *Dispersal in heterogeneous habitats: thresholds, spatial scales, and approximate rates of spread.* Ecology 90, 1338–1345. First published 2009-05-01. https://doi.org/10.1890/08-0115.1
- Lindström, T., Håkansson, N. and Wennergren, U. (2010 online; 2011 volume). *The shape of the spatial kernel and its implications for biological invasions in patchy environments.* Proceedings of the Royal Society B. https://doi.org/10.1098/rspb.2010.1902
- Skelsey, P., With, K. A. and Garrett, K. A. (2012 online; 2013 volume). *Why dispersal should be maximized at intermediate scales of heterogeneity.* Theoretical Ecology. First published 2012-09-27. https://doi.org/10.1007/s12080-012-0171-3
