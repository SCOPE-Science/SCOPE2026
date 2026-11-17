# Sharp perturbation-stability transition for two-site bilateral smoothing

## Finding

Consider two real observations and a symmetric normalized bilateral filter
\[
 F_w(x_1,x_2)=\left(\frac{x_1+w(|x_1-x_2|)x_2}{1+w(|x_1-x_2|)},\frac{x_2+w(|x_1-x_2|)x_1}{1+w(|x_1-x_2|)}\right),
\]
where the self-weight is one and the neighbor weight \(w:[0,\infty)\to[0,1]\) is continuous and nonincreasing. Equip two observations with variation \(V(x)=|x_1-x_2|\). The following are equivalent:

1. \(F_w\) is nonexpansive **between two inputs** for \(V\).
2. \(F_w\) is nonexpansive for every vector \(\ell^q\)-norm, \(1\le q\le\infty\).
3. The function \(H(s)=s w(s)/(1+w(s))\) is nondecreasing on \([0,\infty)\).

If \(s w(s)\to0\) as \(s\to\infty\) and \(w\) is positive somewhere at a positive argument, these equivalent properties fail. In particular, fast-decaying range affinities necessarily admit two-input variation amplification, even though each individual input's variation never increases.

For \(c\in(0,1]\), \(\sigma>0\), and \(p>0\), specialize to the inverse-power range affinity
\[
 w_{c,\sigma,p}(s)=\frac{c}{1+(s/\sigma)^p}.
\]
The exact, sharp global Lipschitz coefficient in the variation seminorm, **and independently in every** \(\ell^q(\mathbb R^2)\), \(1\le q\le\infty\), is
\[
 \boxed{L_{c,p}=\begin{cases}
 1,&0<p\le1,\\
 1+\dfrac{c(p-1)^2}{2p(1+c)},&p>1.
 \end{cases}}
\]
It is independent of \(\sigma\). For \(p>1\), the greatest derivative amplification occurs at the two contrast magnitudes
\[
 |x_1-x_2|=\sigma\left[\frac{(1+c)(p+1)}{p-1}\right]^{1/p}.
\]
For \(p>1\), the sharp coefficient is a supremum, not attained by any distinct pair of inputs. For \(p\le1\), variation has sharp supremum one, also not attained by distinct finite input pairs; full vector \(\ell^q\) norms attain one through nonzero common shifts.

For the classical Gaussian affinity \(w(s)=c\exp[-s^2/(2\sigma^2)]\), the sharp coefficient in all the same metrics is
\[
 L_c^{\mathrm G}=1+\frac{2v_*(2+v_*)}{1-v_*^2},\qquad
 v_*=c e^{-u_*},
\]
where \(u_*>3/2\) is the **unique** solution of
\[
 2u_*(1-ce^{-u_*})=3(1+ce^{-u_*}).
\]
The coefficient is strictly greater than one and is not attained by distinct input pairs. At \(c=1\), \(u_*=1.9803582797688\ldots\) and \(L_1^{\mathrm G}=1.6016389300117\ldots\).

## Assumptions and scope

All input values and parameters are real. Both sites have equal self-weight one and equal, symmetric coupling; the formula uses exactly one simultaneous filtering step. The rank-free range weight is continuous and nonincreasing and lies in \([0,1]\). There are no assumptions about bounded signal amplitude, nor do the two inputs have to share a mean. The symbol \(\ell^q\) refers to the ordinary unweighted two-coordinate vector norm; variation is the edge seminorm on the two-vertex path and ignores constant shifts.

## Proof

**1. Contrast reduction.** Put \(m=(x_1+x_2)/2\), \(d=x_1-x_2\), and
\[
 \phi(d)=d\frac{1-w(|d|)}{1+w(|d|)}.
\]
Direct substitution gives \(F_w(x_1,x_2)=(m+\phi(d)/2,m-\phi(d)/2)\). Thus the two-input variation quotient is exactly \(|\phi(d)-\phi(e)|/|d-e|\), with any \(d\ne e\). Because \(w\) is nonincreasing and lies in \([0,1]\), \(\phi\) is odd, continuous, and nondecreasing. On \([0,\infty)\),
\[
 \phi(s)=s-2H(s),\qquad H(s)=\frac{s w(s)}{1+w(s)}.
\]
For \(s\ge t\ge0\), nonexpansivity of \(\phi\) is equivalent to \(\phi(s)-\phi(t)\le s-t\), hence to \(H(s)\ge H(t)\). Oddness and \(0\le\phi(s)\le s\) handle opposite signs. This establishes equivalence of the first and third statements.

**2. All coordinate norms.** For any distinct inputs \(a,b\), monotonicity allows the scalar slope \(\theta=(\phi(d_a)-\phi(d_b))/(d_a-d_b)\ge0\), with any \(\theta\in[0,\infty)\) permitted when the contrasts agree. Their filtered difference is the matrix
\[
 A_\theta(a-b),\qquad
 A_\theta=\frac{1+\theta}{2}I+\frac{1-\theta}{2}S,
\]
where \(S\) swaps the two coordinates. For every \(1\le q\le\infty\), the swap is an isometry, so
\[
 \|A_\theta\|_{q\to q}\le\frac{1+\theta+|1-\theta|}{2}=\max\{1,\theta\}.
\]
Equality holds by applying \(A_\theta\) to either \((1,1)\) or \((1,-1)\), its eigenvectors with eigenvalues one and \(\theta\). Conversely, any contrast pair is realized by taking both input means zero. Consequently, the full-vector sharp coefficient is \(\max\{1,\operatorname{Lip}(\phi)\}\), and the variation coefficient is \(\operatorname{Lip}(\phi)\). The latter is at least one in the two families below because \(\phi(s)/s\to1\). This proves the second equivalence as well.

**3. General fast-tail obstruction.** If \(s w(s)\to0\), then \(H(s)\to0\). Since \(H(s)>0\) somewhere, \(H\) cannot be nondecreasing. Therefore there are finite \(s>t\ge0\) with \(\phi(s)-\phi(t)>s-t\); no limiting-only counterexample is needed.

**4. Inverse-power family.** Set \(a=1+c\) and \(z=(|d|/\sigma)^p\). Direct substitution yields
\[
 \phi(d)=d\left(1-\frac{2c}{a+z}\right).
\]
It is differentiable also at \(d=0\), with derivative \((1-c)/(1+c)\). Away from zero,
\[
 \phi'(d)=1+\frac{2c((p-1)z-a)}{(a+z)^2}.
\]
For \(0<p\le1\), this derivative is strictly less than one at every finite contrast and approaches one as \(|d|\to\infty\). For \(p>1\), differentiating the displayed rational function in \(z\) gives a strictly positive derivative up to \(z_*=a(p+1)/(p-1)\), and a strictly negative derivative afterwards. Substituting the unique maximizer gives \(1+c(p-1)^2/[2p(1+c)]\). The mean value theorem proves that the supremum of secants equals the supremum of these derivatives. No distinct finite secant can attain a strictly isolated derivative maximum; when \(p\le1\), all finite secants have slope strictly less than one.

**5. Gaussian family.** Let \(u=d^2/(2\sigma^2)\) and \(v=ce^{-u}\). Then
\[
 \phi'(d)=1-\frac{2v}{1+v}+\frac{4uv}{(1+v)^2}.
\]
The derivative of this expression with respect to \(u\) is
\[
 \frac{2v\,[3(1+v)-2u(1-v)]}{(1+v)^3}.
\]
The bracket is strictly decreasing from \(3(1+c)>0\) to negative infinity: its derivative equals \(-(3+2u)v-2(1-v)<0\). It therefore has exactly one zero \(u_*>3/2\). Substitution of \(2u_*(1-v_*)=3(1+v_*)\) in \(\phi'\) gives the stated exact coefficient. Since \(\phi'(d)>1\) at some nonzero contrasts, nonexpansivity fails. As before, the strict isolated derivative maximum prevents attainment by distinct input pairs.

## Verification

Run `python3 check_bilateral.py` with the Python standard library. It independently evaluates original two-coordinate filtering, contrast reduction, explicit derivative formulas, the stationary contrast, and random two-input quotients. Rational-family checks span exponents on both sides of one, four coupling strengths, three scales, and Gaussian cases span four couplings and three scales. Additional checks compare the induced bounds directly in \(\ell^1\), \(\ell^{3/2}\), \(\ell^2\), \(\ell^4\), and \(\ell^\infty\). These finite tests are corroborative; Steps 1–5 are the unrestricted proof.

## Relationship to prior work

Tomasi and Manduchi's bilateral-filter paper establishes the normalized spatial/range weighting mechanism and its original Gaussian form, rather than a two-input operator Lipschitz threshold. Pianykh analyzes several inverse-power and Gaussian range functions, including exponents one, two and four, by comparing the **one-input** standard-deviation reduction of representative distributions; those calculations do not determine the worst-case **difference between two filtered inputs**. Pan, An and He's treatment of arbitrary range kernels primarily studies fast numerical approximation, not the sharp stability criterion. The present statement supplies a complete minimal two-site perturbation classification and exact sharp gains; it is not a stability theorem for general image grids.

## Limitations

No assertion is made for neighborhoods with three or more pixels, unequal self-weights, asymmetric affinities, repeated filtering, empirical denoising effectiveness, or arbitrary nonlinear kernel families beyond the monotonicity criterion. The constants are global worst-case perturbation bounds, not noise-distribution averages. The historical literature search cannot rule out all unindexed prior derivations, particularly those formulated as scalar contrast-response derivatives.

## References

1. C. Tomasi and R. Manduchi, *Bilateral Filtering for Gray and Color Images*, ICCV 1998, pp. 839–846. DOI: https://doi.org/10.1109/ICCV.1998.710815 . Lawful full text: https://projects.iq.harvard.edu/sites/projects.iq.harvard.edu/files/imagenesmedicas/files/tomasi1998kg.pdf .
2. O. S. Pianykh, *Bilateral filters: what they can and cannot do*, first public arXiv version dated 2010-07-06, arXiv:1007.1016v1. https://arxiv.org/pdf/1007.1016 .
3. S. Pan, X. An and H. He, *Optimal O(1) Bilateral Filter with Arbitrary Spatial and Range Kernels Using Sparse Approximation*, Mathematical Problems in Engineering (2014), DOI: https://doi.org/10.1155/2014/289517 .
