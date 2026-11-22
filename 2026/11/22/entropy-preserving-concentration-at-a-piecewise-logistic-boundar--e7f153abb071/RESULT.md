# Entropy-preserving concentration at a piecewise-logistic boundary crisis

## Finding
For the two-branch continuous interval map
\[
 f_r(x)=\begin{cases}
 r x,&0\le x\le r^{-1},\\
 \dfrac{r^2}{r-1}x(1-x),&r^{-1}\le x\le1,
 \end{cases}\qquad 1<r<\varphi:=\frac{1+\sqrt5}{2},
\]
let \(\mu_r\) be its invariant probability measure of maximal entropy. This measure exists and is unique. Along the natural boundary-crisis curve, the topological and measure-theoretic entropies both equal \(\log 2\), yet \(\mu_r\) concentrates exponentially in \(1/(r-1)\) at the endpoint \(1\) as \(r\downarrow1\). More precisely, for every integer \(n\ge0\),
\[
 \mu_r([0,r^{-n}])=2^{-n},
\]
and for each fixed \(t\in(0,1)\),
\[
 \boxed{\lim_{r\downarrow1}(\log r)\log\mu_r([0,t])=(\log2)\log t.}
\]
Consequently \(\mu_r\) converges weakly to the point mass \(\delta_1\) as \(r\downarrow1\). At the same time its Hausdorff dimension and its exceptional local dimension at the repelling fixed point \(0\) separate in opposite directions:
\[
 \boxed{\dim_H\mu_r\sim\frac{2\log2}{\log(1/(r-1))}\longrightarrow0,\qquad
 \dim_{\mathrm{loc}}\mu_r(0)=\frac{\log2}{\log r}\longrightarrow\infty.}
\]
The first limit refers to the dimension of the measure (the almost-everywhere local dimension), while the second refers to the local dimension at a single exceptional point; there is no contradiction with the ambient dimension being one.

## Assumptions and scope
Throughout, \(1<r<\varphi\), \(a=r^2/(r-1)\), and the state interval is \([0,1]\). At the common branch boundary \(c=1/r\) the two formulas coincide at \(f_r(c)=1\). The branches are increasing on \([0,c]\) and decreasing on \([c,1]\); both map their respective domains onto \([0,1]\). The limit \(r\downarrow1\) remains within the stated expanding parameter interval. Entropy uses natural logarithms. The Hausdorff dimension of an invariant probability is its measure dimension, not the dimension of its support. The local dimension at zero means \(\lim_{t\downarrow0}\log\mu_r([0,t])/\log t\).

## Proof
**1. Exact crisis family and expansion.** The common branch value is \(r(1-r/a)\). The boundary-crisis identity \(f_r(c)=1\) therefore gives \(a=r^2/(r-1)\) and \(c=1/r\). The right branch ends at \(f_r(1)=0\). Its smallest derivative magnitude occurs at \(c\) and equals
\[
 m_R(r)=a(2c-1)=\frac{r(2-r)}{r-1}.
\]
The left derivative is \(r\). Thus \(\inf_{x\ne c}|f_r'(x)|=\min\{r,m_R(r)\}>1\) exactly when \(1<r<\varphi\). In particular both inverse branches are strict contractions with uniform bounded distortion for each fixed parameter.

**2. Coding and uniqueness of the maximal-entropy law.** The two inverse branches, defined on the entire \([0,1]\), are
\[
 g_L(y)=\frac yr,\qquad
 g_R(y)=\frac{1+\sqrt{1-4y/a}}{2}.
\]
Coding by nested inverse images gives a continuous onto map \(\pi_r:\{L,R\}^{\mathbb N}\to[0,1]\) intertwining the full two-shift and \(f_r\). Its coding ambiguities occur only at the countable set of preimages of the turning point and have zero fair Bernoulli measure. Each of the \(2^n\) length-\(n\) inverse cylinders is a genuine monotonic branch of \(f_r^n\) mapping onto \([0,1]\). The lap-count entropy (or the full two-shift factor plus the two-lap upper bound) is therefore \(\log2\). Pushing forward the fair Bernoulli law gives \(\mu_r\), whose branch itinerary has independent fair symbols and entropy \(\log2\). Every invariant measure of maximal entropy lifts to an invariant measure of the two-shift of the same maximal entropy; the fair Bernoulli law is the unique such shift measure. Therefore \(\mu_r\) is the unique maximal-entropy law.

**3. Exact endpoint cylinders and concentration.** The cylinder corresponding to \(n\) successive left branch choices is exactly
\[
 g_L^n([0,1])=[0,r^{-n}].
\]
It has Bernoulli probability \(2^{-n}\), and its coding boundaries have zero mass. This proves the exact mass identity. Fix \(0<t<1\) and let \(n=\lfloor\log(1/t)/\log r\rfloor\). Then \(r^{-(n+1)}<t\le r^{-n}\), so
\[
 2^{-(n+1)}\le\mu_r([0,t])\le2^{-n}.
\]
Multiply the logarithms of these inequalities by \(\log r>0\); since \(n\log r\to\log(1/t)\) as \(r\downarrow1\), the displayed sharp limit follows. For every fixed \(t<1\), the mass \(\mu_r([0,t])\to0\), which is exactly weak convergence to \(\delta_1\) on the compact interval. For a fixed \(r\), the same cylinder inequalities with \(t\downarrow0\) yield the local dimension at zero.

**4. Dimension of typical points.** Let
\[
 \chi_r=\int_{[0,1]}\log|f_r'(x)|\,d\mu_r(x),
\]
with the derivative defined off the zero-mass switching preimages. By the fair-symbol property, the left and right branches each carry half the measure. On the left \(|f_r'|=r\); on the right \(r(2-r)/(r-1)\le|f_r'|\le r^2/(r-1)\). Hence
\[
 \log r+\frac12\log\frac{2-r}{r-1}\ \le\ \chi_r\ \le\
 \frac32\log r-\frac12\log(r-1).
\]
Both bounds equal \(\frac12\log(1/(r-1))+O(r-1)\) as \(r\downarrow1\). For each fixed \(r\) the map is piecewise \(C^2\), uniformly expanding, and has two full branches with bounded distortion. The standard entropy-over-Lyapunov formula for ergodic uniformly expanding interval measures applies, and gives exact dimensionality and
\[
 \dim_H\mu_r=\frac{h_{\mu_r}(f_r)}{\chi_r}=\frac{\log2}{\chi_r}.
\]
The preceding sharp derivative bounds yield the claimed asymptotic dimension law. This completes the proof.

## Verification
The attached standalone checker reconstructs the branch matching identity, exact inverse endpoints, the expanding parameter condition, the endpoint-cylinder identity, and the Lyapunov brackets for exact rational test parameters. The proof of uniqueness, endpoint concentration, and measure dimension is analytic; finite checker samples are diagnostics, not an infinite certificate. The entropy-over-Lyapunov theorem is invoked under the verified uniform-expansion and bounded-distortion hypotheses.

## Relationship to prior work
Sushko, Agliari and Gardini (2005) already give the exact crisis curve \(a=r^2/(r-1)\), the trapping region, and its interpretation; none of those are claimed as new. Duan, Wei, Li, Su and Grebogi (2024) study the same map's kneading description and construct a golden-mean subshift in a separate period-three parameter window. The present result concerns the *maximal-entropy invariant measure on the entire exact crisis curve in the uniformly expanding regime*, and its exceptional joint limits: an unchanged full symbolic entropy, an exponentially concentrated weak limit, a vanishing typical dimension, and a diverging local dimension at the origin. Classical full-branch coding and the entropy/Lyapunov dimension formula are ingredients, not claimed discoveries. The exact joint degeneration for this specific crisis family was not located in the inspected sources; general thermodynamic-formalism results and unindexed treatments remain priority risks.

## Limitations
The uniform-expansion and dimension conclusions are proved only for \(1<r<\varphi\); no classification is claimed for \(\varphi\le r<2\). The theorem is about the *maximal-entropy measure*, not the physical absolutely continuous invariant measure. The limit \(\delta_1\) does not assert invariant-measure continuity at \(r=1\), where the defining formula is singular. No claim is made for parameter offsets away from the exact crisis curve, non-autonomous switching, numerical floating-point implementations, or uniqueness of physical measures. Independent verification has not been performed.

## References
1. J. Duan, Z. Wei, D. Li, H. Su, and C. Grebogi, *Symbolic dynamics for a kinds of piecewise smooth maps*, Discrete and Continuous Dynamical Systems - S **17** (2024), 2778–2787. First available online April 1, 2024. https://doi.org/10.3934/dcdss.2024042 . Accessible author full text: https://www.researchgate.net/publication/379584093_Symbolic_dynamics_for_a_kinds_of_piecewise_smooth_maps .
2. I. Sushko, A. Agliari, and L. Gardini, *Bistability and border-collision bifurcations for a family of unimodal piecewise smooth maps*, Discrete and Continuous Dynamical Systems - B **5** (2005), 881–897. https://doi.org/10.3934/dcdsb.2005.5.881 . Accessible full text: https://www.researchgate.net/publication/228662883_Bistability_and_border-collision_bifurcations_for_a_family_ofunimodal_piecewise_smooth_maps .
3. Standard uniformly expanding interval-map bounded-distortion, maximal-entropy coding, and one-dimensional entropy/Lyapunov dimension results; used in their classical form under the explicit hypotheses checked above, without asserting a new general theorem.
