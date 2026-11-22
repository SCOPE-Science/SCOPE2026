# Sharp cross-lobe proximity laws at the Cassini–lemniscate separation threshold

## Finding
For \(0\le q<1/2\) put
\[
 K_q=\{(x,y)\in\mathbb R^2:(x^2+y^2)^2\le x^2-y^2-q^2\},\qquad K_q^{\pm}=K_q\cap\{\pm x>0\}.
\]
Independently sample \(X_q\) and \(Y_q\) from normalized planar area on \(K_q^+\) and \(K_q^-\), respectively, and put \(D_q=|X_q-Y_q|\). The two components are disjoint for \(q>0\); for \(q=0\) their closures meet at the lemniscate's double point. The following exact rare-pair and topological critical-window laws hold.

1. At the lemniscate,
\[
 \Pr(D_0<\varepsilon)=\frac12\varepsilon^4+O(\varepsilon^6),\qquad\varepsilon\downarrow0.
\]
Conditional on \(D_0<\varepsilon\), the scaled pair \((X_0/\varepsilon,Y_0/\varepsilon)\) converges in total variation to uniform four-dimensional Lebesgue measure on
\[
 E_0=\{(u,v)\in C_+\times C_-:|u-v|<1\},\quad C_+=\{(x,y):x\ge |y|\},\ C_-=-C_+,\quad |E_0|=\tfrac18.
\]
2. For each fixed \(\lambda\ge0\), the critical two-lobe crossover is
\[
 \lim_{q\downarrow0}q^{-4}\Pr(D_q<q\lambda)=4\Phi(\lambda),
\]
where \(H_+=\{(x,y):x\ge\sqrt{1+y^2}\}\), \(H_-=-H_+\), and
\[
 \Phi(\lambda)=\iint_{H_+\times H_-}{\bf1}_{\{|u-v|<\lambda\}}\,du\,dv
 =\frac12\int_{\mathbb R^2}\left[\sqrt{(\lambda^2-(s-t)^2)_+}-\sqrt{1+s^2}-\sqrt{1+t^2}\right]_+^2\,ds\,dt.
\]
Here \([z]_+=\max(z,0)\). Precisely, \(\Phi(\lambda)=0\) for \(\lambda\le2\), and it is strictly positive for \(\lambda>2\); its sharp edges are
\[
 \Phi(2+\delta)\sim\frac{\pi}{3\sqrt2}\delta^3\quad(\delta\downarrow0),\qquad
 \Phi(\lambda)\sim\frac{\lambda^4}{8}\quad(\lambda\to\infty).
\]
For each fixed \(\lambda>2\), conditional on \(D_q<q\lambda\) the rescaled pair \((X_q/q,Y_q/q)\) converges in total variation to uniform measure on \(\{(u,v)\in H_+\times H_-:|u-v|<\lambda\}\).

## Assumptions and scope
The sampling is by two-dimensional Euclidean area, **one independent point from each specified lobe**; it is not arclength sampling and not a pair conditioned after sampling a different shape. The normalized quartic uses fixed foci at \((\pm1/\sqrt2,0)\). Equivalently \(K_q=\{z:|z-1/\sqrt2|\,|z+1/\sqrt2|\le b_q^2\}\), with \(b_q^4=1/4-q^2\). Thus \(q>0\) is the two-component Cassini regime and \(q=0\) its Bernoulli lemniscate threshold. The minimum cross-lobe distance for \(q>0\) is
\[
 g_q=2\sqrt{\frac{1-\sqrt{1-4q^2}}{2}}=2q+O(q^3).
\]
The first-source posting is the archival March 23, 2013 version of Boyadzhiev–Boyadzhiev, which discusses the same two-component/lemniscate transition without the present random-pair statistics.

## Proof
**Lobe area and localization.** For \(q=0\), polar coordinates \((r,\theta)\) in the right lobe give \(-\pi/4\le\theta\le\pi/4\) and \(0\le r^2\le\cos2\theta\). Therefore
\[
 A_0=\operatorname{area}(K_0^+)=\frac12\int_{-\pi/4}^{\pi/4}\cos2\theta\,d\theta=\frac12.
\]
The opposite lobe has the same area. More generally \(K_q^+\) is contained in the right cone \(C_+\), and its area \(A_q\) tends to \(1/2\) by dominated convergence as \(q\downarrow0\). Explicitly,
\[
 A_q=\frac12\int_{-\theta_q}^{\theta_q}\sqrt{\cos^2(2\theta)-4q^2}\,d\theta,\quad\theta_q=\frac12\arccos(2q).
\]
For \(u\in C_+\), \(v\in C_-\), the scalar product \(u\cdot v\le0\), since the cone's aperture is \(\pi/2\). Hence \(|u-v|^2\ge|u|^2+|v|^2\), so \(|u-v|<R\) forces both \(|u|,|v|<R\). This gives an exact compact localization for all following rescalings.

**Cone coefficient, evaluated exactly.** Scale \(x=\varepsilon u\), \(y=\varepsilon v\) in the unnormalized cross-lobe measure. Its indicator converges to \({\bf1}_{E_0}\), and the complement inside the cone support has rescaled four-dimensional volume \(O(\varepsilon^2)\): indeed the radial condition on the right is \(\cos2\theta\ge\varepsilon^2r^2\), so inside \(r\le1\) each of its two missing angular strips has width \(O(\varepsilon^2)\); the same holds on the left. Thus the pair volume is \(\varepsilon^4(|E_0|+O(\varepsilon^2))\).

To compute \(|E_0|\) exactly, put \(w=-v\in C_+\). For any \(u,w\in C_+\) introduce the linear cone coordinates \(a=x+y\), \(b=x-y\), so \(a,b\ge0\) and \(dx\,dy=\tfrac12 da\,db\). If the two transformed vectors have sums \(A=a_1+a_2\) and \(B=b_1+b_2\), then \(|u+w|^2=(A^2+B^2)/2\). Integrating first over \(a_1\in[0,A]\) and \(b_1\in[0,B]\),
\[
 |E_0|=\frac14\int_{\substack{A,B\ge0\\ A^2+B^2<2}}AB\,dA\,dB
 =\frac14\left(\int_0^{\sqrt2}\rho^3\,d\rho\right)
 \left(\int_0^{\pi/2}\cos\alpha\sin\alpha\,d\alpha\right)=\frac18.
\]
Dividing by \(A_0^2=1/4\) proves the probability coefficient \(1/2\) and the stated error. The bounded and almost-everywhere-convergent indicator densities also give \(L^1\), hence total-variation, convergence to the uniform law on \(E_0\).

**Critical blow-up and the two-dimensional formula.** Put \((x,y)=q(u,v)\) in the Cassini inequality. It becomes
\[
 u^2-v^2\ge1+q^2(u^2+v^2)^2.
\]
For positive and negative \(u\) this converges pointwise away from boundaries to \(H_+\) and \(H_-\), respectively. Compact localization from the cone inequality permits dominated convergence of the four-dimensional integrals for any fixed \(\lambda\), including \(\lambda\le2\). The unnormalized probability numerator is \(q^4(\Phi(\lambda)+o(1))\); since \(A_q^2\to1/4\), the displayed crossover follows, as does conditional total-variation convergence when \(\lambda>2\).

For the explicit integral, write a point in \(H_+\) as \((\sqrt{1+s^2}+h,s)\) and a point in \(H_-\) as \((-\sqrt{1+t^2}-k,t)\), with \(h,k\ge0\). The metric inequality is
\[
 h+k<\sqrt{\lambda^2-(s-t)^2}-\sqrt{1+s^2}-\sqrt{1+t^2}.
\]
For each \((s,t)\), the triangular \((h,k)\) domain has area half the positive part of the right side squared. This proves the formula, including finiteness and positivity precisely when \(\lambda>2\).

**Sharp crossover edges.** At \(\lambda=2+\delta\), pairs necessarily approach the two tips \((\pm1,0)\). Writing \(h,k\ge0\) as above and \(s,t=O(\sqrt\delta)\), the distance deficit relative to \(2\) is
\[
 |u-v|-2=h+k+Q(s,t)+o(\delta),\qquad Q(s,t)=\frac34(s^2+t^2)-\frac12 st.
\]
The positive quadratic form \(Q\) has eigenvalues \(1/2\) and \(1\). The scaled compact domain and dominated convergence therefore give
\[
 \Phi(2+\delta)\sim\frac12\int_{\mathbb R^2}(\delta-Q(s,t))_+^2\,ds\,dt
 =\frac{\pi}{3\sqrt2}\delta^3.
\]
Finally, with \(u=\lambda a\), \(v=\lambda b\), the sets \(\lambda^{-1}H_\pm\) converge to \(C_\pm\). The same localized dominated-convergence argument shows \(\lambda^{-4}\Phi(\lambda)\to|E_0|=1/8\). This completes all quantifiers and boundary cases.

## Verification
The exact cone calculation uses only linear changes of variables and elementary integrals. The two-dimensional integral is derived by integrating out two nonnegative tip-depth variables, not by fitting numerical data. The accompanying `verify.py` independently evaluates the cone coefficient by numerical quadrature, checks the lobe-area normalization, and approximates the critical crossover and its cubic onset for decreasing offsets. These finite numerical checks are diagnostics; they are not substituted for the limiting proofs.

## Relationship to prior work
Boyadzhiev and Boyadzhiev (2013) explicitly study the same two-lobe Cassini / Bernoulli-lemniscate transition, but not independently sampled random cross-component distances. Gečiauskas (1966) develops distance distributions for planar convex ovals, whose convexity assumption excludes the doubly lobed geometry. Lellouche and Souris (2019) give a general compact-set distance-distribution framework; it provides background identities but does not evaluate the cone coefficient, the hyperbolic critical crossover, or its cubic onset. Earlier short-pair contact laws for smoothly tangent convex bodies have exponent \(7/2\), whereas these opposite transverse cones give exponent \(4\), and are not implication-equivalent. The novelty assessment is a documented literature comparison, not a claim of independently certified historical priority.

## Limitations
The result is for the specifically normalized Cassini family and area-uniform **cross-lobe** pairs; it is not a universal law for arbitrary touching domains, nor a statement about boundary-arclength distances. The critical asymptotic is pointwise for each fixed \(\lambda\), not a uniform error estimate over unbounded \(\lambda\), and the cubic onset is a second limit of the limiting crossover, not a fully uniform joint \((q,\lambda)\)-limit. The historical-literature comparison is necessarily nonexhaustive and independent review remains outstanding.

## References
- K. N. Boyadzhiev and I. A. Boyadzhiev, *Harmonic motion and Cassini ovals*, arXiv:1303.5876, first posted 2013-03-23. https://arxiv.org/abs/1303.5876
- E. Gečiauskas, *Distribution function of a distance between two random points in an oval*, Lithuanian Mathematical Journal 6 (1966), 245–248. https://doi.org/10.15388/LMJ.1966.19722
- S. Lellouche and M. Souris, *Distribution of Distances between Elements in a Compact Set*, Stats 3 (2020), 1–15, first online 2019-12-26. https://doi.org/10.3390/stats3010001
