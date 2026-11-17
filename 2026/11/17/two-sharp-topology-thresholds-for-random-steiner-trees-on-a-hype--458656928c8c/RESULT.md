# Two sharp topology thresholds for random Steiner trees on a hyperbolic horocycle segment

## Finding

Let \(\mathbb H^2\) be the curvature-\(-1\) hyperbolic plane in the upper-half-plane model with metric \(ds^2=(dx^2+dy^2)/y^2\). Independently choose three points uniformly by hyperbolic arclength on the horizontal horocycle segment \(\{(x,1):0\le x\le L\}\), with \(L>0\). Let \(p(L)\) be the probability that their shortest connected geodesic network uses only two segments, equivalently that its Fermat–Torricelli minimizer is one of the sampled points, rather than a distinct degree-three Steiner junction.

Put
\[
 a=\frac{2}{\sqrt3},\quad b=\sqrt3,\quad L_1=2a=\frac4{\sqrt3},\quad L_2=2b=2\sqrt3,\quad I=\frac83\log2-1,\quad B=\frac{\sqrt3}{9}(15-16\log2).
\]
For \(0\le s\le b\), define
\[
 \ell(s)=\begin{cases}s,&0\le s\le a,\\ s-\sqrt{s^2+4s/\sqrt3-4},&a<s\le b.\end{cases}
\]
Then the complete probability law, valid for every \(L>0\), is the finite one-dimensional integral
\[
 \boxed{p(L)=\frac{24}{L^3}\int_0^{\min(L/2,b)}(L-2s)\ell(s)\,ds.}
\]
It has exactly two sharp geometric thresholds:

* **Unconditional absorption:** \(p(L)=1\) if and only if \(0<L\le L_1\). For \(L>L_1\), \(p(L)\) decreases strictly, with
  \[
  \boxed{1-p(L)=\frac{3^{5/4}}{10}(L-L_1)^{5/2}+O((L-L_1)^{7/2})\quad(L\downarrow L_1).}
  \]
* **Exact long-segment law:** For every \(L\ge L_2\), not merely asymptotically,
  \[
  \boxed{p(L)=\frac{24I}{L^2}-\frac{48B}{L^3}.}
  \]
  From below the second threshold,
  \[
  \boxed{p(L)=\frac{24I}{L^2}-\frac{48B}{L^3}+\frac{(L_2-L)^3}{36\sqrt3}+O((L_2-L)^4).}
  \]
  Hence \(p\) is twice continuously differentiable but not three times differentiable at \(L_2\); its third derivative has a positive right-minus-left jump \(1/(6\sqrt3)\).

The topology-conditioned geometry has a simple universal limit. If \(X_1<X_2<X_3\) are the ordered sampled abscissae, let \(U=(X_2-X_1)/2\), \(V=(X_3-X_2)/2\), and \(Z_L=X_1/L\). Conditional on the two-edge event, \((U,V,Z_L)\) converges in total variation as \(L\to\infty\), at rate \(O(1/L)\), to independent \(Z\sim\operatorname{Uniform}[0,1]\) and \((U_\infty,V_\infty)\) uniform on
\[
 D=\left\{u,v\ge0:\arctan u+\arctan v\le\frac\pi3\right\},\qquad |D|=I.
\]
This limit distinguishes the relative two gaps from the macroscopic location of a rare two-edge network.

## Assumptions and scope

The horocycle has intrinsic arclength coordinate \(x\) on \(y=1\); the sample uses independent uniform \(x\in[0,L]\). All geodesic segments and angles are ambient hyperbolic; the segment of the horocycle is not itself geodesic. The three sampled points are almost surely distinct and have a unique geodesic triangle and unique Fermat–Torricelli minimizer. Boundary equalities have probability zero. The 120-degree criterion is for **unweighted** geodesic networks in the complete simply connected curvature-\(-1\) plane; a global hyperbolic isometry makes any horocycle segment of length \(L\) equivalent to the chosen coordinate model.

## Proof

**1. The three-terminal topology criterion.** In the hyperbolic plane, the function \(F(q)=\sum_{i=1}^3d(q,P_i)\) is geodesically convex and attains a unique minimum for three distinct noncollinear terminals. At a terminal \(P_i\), the first-variation subgradient condition for a minimum is that the vector sum of the two outgoing unit tangents has norm at most one, equivalent to the included angle being at least \(2\pi/3\). If no triangle angle reaches \(2\pi/3\), the minimizing junction is interior, and first variation gives three incident geodesics meeting at \(2\pi/3\). Standard three-terminal network reduction shows a shortest connected geodesic tree is precisely this star or the two edges incident to the absorbing vertex. The angle sum of a hyperbolic triangle is less than \(\pi\), so at most one vertex can absorb.

**2. Exact angle along a horocycle.** Sort the abscissae \(0\le X_1<X_2<X_3\le L\), and write \(g=X_2-X_1\), \(h=X_3-X_2\). The hyperbolic geodesic between \((x,1)\) and \((x+d,1)\) is the Euclidean semicircle orthogonal to \(y=0\), with center \((x+d/2,0)\). At its left endpoint the initial tangent makes angle \(\arctan(d/2)\) with the positive horizontal direction; at the right endpoint the inward tangent makes angle \(\pi-\arctan(d/2)\). Conformality of the upper-half-plane model therefore gives
\[
 \theta_{\mathrm{middle}}=\pi-\arctan(g/2)-\arctan(h/2).
\]
The other two triangle angles are each strictly less than \(\pi/2\). Consequently the tree has two edges precisely when \(\arctan(g/2)+\arctan(h/2)\le\pi/3\).

**3. Probability measure and feasible gap sections.** Ordered sampling gives joint density \(6/L^3\) on \(0<X_1<X_2<X_3<L\). Integrating out \(X_1\) leaves density \(6(L-g-h)/L^3\) on \(g,h>0\), \(g+h<L\). Set \(u=g/2\), \(v=h/2\), \(s=u+v\). For nonnegative \(u,v\), the inequality \(\arctan u+\arctan v\le\pi/3\) is equivalent to \(s\le\sqrt3(1-uv)\); in particular it forces \(0\le s\le\sqrt3\). At fixed \(s\), the allowed \(u\)-interval length equals \(s\) until \(s=a=2/\sqrt3\). For \(a<s<b=\sqrt3\), it consists of two endpoint intervals of total length \(s-\sqrt{s^2+4s/\sqrt3-4}\); beyond \(b\) no positive length remains. The Jacobian \(dg\,dh=4du\,dv\) gives the stated \(24/L^3\) integral.

**4. First threshold and its sharp exponent.** Concavity of \(\arctan\) yields \(\arctan(g/2)+\arctan(h/2)\le2\arctan((g+h)/4)\le2\arctan(L/4)\), so absorption is certain exactly while \(L\le4/\sqrt3\). Conversely for larger \(L\), an open set of nearly equal gaps violates the condition. Write \(L=L_1+\delta\), \(s=a+w\); the failing slice of feasible \(u\) has length \(d(s)=\sqrt{s^2+4s/\sqrt3-4}=\sqrt{8w/\sqrt3+w^2}\). Thus
\[
 1-p(L)=\frac{24}{L^3}\int_a^{L/2}(L-2s)d(s)\,ds.
\]
Replacing \(d(a+w)\) by \(\sqrt{8/\sqrt3}\,\sqrt w+O(w^{3/2})\) and integrating \(0<w<\delta/2\) gives \(3^{5/4}\delta^{5/2}/10+O(\delta^{7/2})\). Strict decrease for \(L>L_1\) follows by coupling the same ordered normalized uniform samples as \(L\) grows: the sum of arctangents of scaled positive gaps increases strictly, and the threshold has positive density on each admissible level.

**5. Second threshold, exact constants, and smoothness.** For \(L\ge2\sqrt3\), the length cutoff \(s<L/2\) contains all of \(D\). Elementary one-variable rational integration gives
\[
 \begin{aligned}
 |D|&=\int_0^{\sqrt3}\frac{\sqrt3-u}{1+\sqrt3u}\,du=\frac83\log2-1=I,\\
 \iint_D (u+v)\,du\,dv&=2\int_0^{\sqrt3}\frac{u(\sqrt3-u)}{1+\sqrt3u}\,du=\frac{\sqrt3}{9}(15-16\log2)=B.
 \end{aligned}
\]
Therefore the exact polynomial in \(1/L\) follows. For \(L=L_2-\delta\), comparison against that polynomial gives
\[
 p(L)-\left(24I/L^2-48B/L^3\right)=\frac{24}{L^3}\int_{L/2}^{b}2(s-L/2)\ell(s)\,ds.
\]
Since \(\ell(s)=\frac23(b-s)+O((b-s)^2)\) as \(s\uparrow b\), the right side equals \(\delta^3/(36\sqrt3)+O(\delta^4)\). Thus the third-derivative jump is exactly \(6/(36\sqrt3)=1/(6\sqrt3)\).

**6. Marked long-segment law.** In variables \((u,v,z)=(g/2,h/2,X_1/L)\), the unconditioned joint density is \(24/L^2\) on the set \(u,v\ge0\), \(0\le z\le1-2(u+v)/L\). Conditioning on absorption restricts \((u,v)\) to \(D\). For \(L\ge L_2\), the conditional density is therefore exactly
\[
 \frac{24}{L^2p(L)}\mathbf1_D(u,v)\mathbf1_{0\le z\le1-2(u+v)/L}.
\]
Because \(D\) is bounded, its normalizing denominator satisfies \(L^2p(L)/24=I-2B/L\), and the displayed density differs in \(L^1\) by \(O(1/L)\) from \(I^{-1}\mathbf1_D(u,v)\mathbf1_{0\le z\le1}\). This proves total-variation convergence, independence, and the stated rate.

## Verification

The standalone standard-library script `verify_horocycle_steiner.py` separately evaluates the gap-section integral, the first-threshold complementary integral, the post-threshold closed expression, and the second-threshold correction. It independently reconstructs the middle angle using the hyperbolic cosine rule rather than tangent slopes, verifies the exact elementary constants, checks both singular coefficients, and directly simulates 120,000 random triples at each of five segment lengths. On the included script, the output ends `HOROCYCLE_STEINER_TWO_THRESHOLDS_CHECKS_OK`. Finite checks do not prove any infinite statement; the proof above supplies the all-length result.

## Relationship to prior work

Cieslik, Ivanov, and Tuzhilin [1] study global Steiner ratios on Riemannian manifolds rather than random terminals restricted to a horocycle segment. Dimond [2] proves a deterministic hyperbolic three-terminal Steiner statement for *three equidistant points*, a distinct condition from our independently sampled horocycle points. The source's landing page and abstract were accessible; its full manuscript was not (download returned access denied), so this historical comparison carries residual risk. Zachos [3] treats deterministic weighted Fermat–Torricelli solutions on the unit sphere, not the stated random hyperbolic horocycle topology law. The HyperSteiner presentation [4] describes computational hyperbolic Steiner trees with the standard 120-degree junction condition, but not exact segment-length topology probabilities, two singular thresholds, or a conditional marked law. An accessible earlier hyperbolic-circumcircle acuteness result concerns different point sampling and a 90-degree angle threshold, and neither it nor an earlier conditional-obtuseness law for points on a *geodesic circle* implies this distribution for noncompact horocycles. Standard upper-half-plane angle identities, 120-degree Steiner conditions, and elementary random-spacing densities are not claimed as new.

The contribution is the complete finite-segment probability, its two nonanalytic transition laws, its exact post-threshold inverse-length polynomial, and its joint location-and-gap asymptotic. Although reviewed published results did not identify a covering theorem, independent historical-priority verification has not been performed.

## Limitations

This is a three-terminal, unweighted result in a complete curvature-\(-1\) hyperbolic plane, with independent uniform *horocyclic arclength* sampling on one finite segment. It does not imply comparable laws for geodesic-circle sampling, general curves, higher terminal counts, arbitrary sampling density, or intrinsic arc networks constrained to the horocycle. The convergence statement concerns the specified marks under absorption as \(L\to\infty\), not a distribution of the actual Steiner-junction position. Numerical checks are corroborative only.

## References

[1] D. Cieslik, A. O. Ivanov, A. A. Tuzhilin, *Steiner Ratio for Riemannian Manifolds*, first public arXiv submission 17 January 2011. https://arxiv.org/abs/1101.3144

[2] D. Dimond, *Another Proof of the Steiner Result for Three Equidistant Points in Euclidean Space and an Analogous Proof in Hyperbolic Space*, Rose-Hulman Undergraduate Mathematics Journal 5(2), article 1 (2004). https://scholar.rose-hulman.edu/rhumj/vol5/iss2/1/

[3] A. N. Zachos, *An analytical solution of the weighted Fermat-Torricelli problem on the unit sphere*, first public arXiv submission 27 August 2014. https://arxiv.org/abs/1408.6495

[4] A. García Castellanos et al., *HyperSteiner: Computing Heuristic Hyperbolic Steiner Minimal Trees*, presentation, 2025. https://agarciacast.github.io/publication/garcia-2024-hypersteiner/hyperSteinerSlides.pdf
