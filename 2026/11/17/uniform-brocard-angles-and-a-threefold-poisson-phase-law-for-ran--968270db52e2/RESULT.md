# Uniform Brocard angles and a threefold Poisson phase law for random cyclic triangles

## Finding
Choose three independent points uniformly by arclength on a Euclidean circle of arbitrary radius. Their nondegenerate inscribed triangle has Brocard angle \(\omega\), characterized by \(\cot\omega=\cot A+\cot B+\cot C\), with \(A,B,C\) its internal angles. **The Brocard angle is exactly uniform on \((0,\pi/6)\):**
\[
\Pr\{\omega\le t\}=\frac{6t}{\pi}\qquad(0\le t\le\pi/6).
\]
This law is independent of the circle radius. Equivalently, \(K=\cot\omega\) has the truncated Cauchy-type density
\[
 f_K(k)=\frac{6}{\pi(1+k^2)}\mathbf 1_{\{k>\sqrt3\}}.
\]

There is an exact marked refinement. For \(k>\sqrt3\) write \(s=\sqrt{k^2-3}\), and define a phase \(\phi\in[0,2\pi)\) by
\[
\begin{aligned}
\cot A&=\tfrac13(k+2s\cos\phi),\\
\cot B&=\tfrac13(k+2s\cos(\phi+2\pi/3)),\\
\cot C&=\tfrac13(k+2s\cos(\phi+4\pi/3)).
\end{aligned}
\]
For the cyclically ordered angle labels this phase is unique modulo \(2\pi\), apart from the probability-zero equilateral case. The complete joint shape density, with respect to \(dk\,d\phi\), is
\[
\boxed{f_{K,\Phi}(k,\phi)=\frac{9\sqrt3}{\pi^2\left[k^3+9k-(k^2-3)^{3/2}\cos(3\phi)\right]}}
\quad(k>\sqrt3,\;0\le\phi<2\pi).
\]
In particular, \(\Phi\) conditional on \(K=k\) has the threefold wrapped Poisson-kernel density
\[
 f_{\Phi\mid K}(\phi\mid k)=\frac{1-r(k)^2}{2\pi\,[1-2r(k)\cos(3\phi)+r(k)^2]},\qquad
 r(k)=\frac{(k^2-3)^{3/2}}{k^3+9k+3\sqrt3(1+k^2)}.
\]
As \(k\downarrow\sqrt3\), the conditional phase approaches uniform angular measure. As \(k\to\infty\), it converges weakly to three equal point masses at \(0,2\pi/3,4\pi/3\). Consequently \(\mathbb E\omega=\pi/12\), and \(\mathbb E[(\cot\omega)^p]\) is finite for real \(p\ge0\) precisely when \(p<1\).

## Assumptions and scope
The three points are independent and uniform with respect to Euclidean arclength on the same fixed circle. Distinctness and nondegeneracy hold almost surely. Label one of the independently sampled points as the starting point, and proceed counterclockwise to label the other two; the three consecutive angular gaps divided by two give the internal-angle triple \((A,B,C)\), up to cyclic permutation. The two remaining point offsets relative to the starting point are the order statistics of two independent uniform variables; the three gaps are therefore Dirichlet with parameters \((1,1,1)\). Thus \((A,B)\) has constant density \(2/\pi^2\) on \(A>0,B>0,A+B<\pi\), with \(C=\pi-A-B\).

The geometric Brocard angle satisfies \(0<\omega\le\pi/6\), with equality only for an equilateral triangle. The marked phase depends on the orientation/labels, while its threefold conditional density is invariant under cyclic relabeling. Only the stated arclength sampling model is covered; uniform points in the disk or Gaussian-coordinate triangles have different laws.

## Proof
**1. Algebraic coordinates.** Put \(x=\cot A\), \(y=\cot B\), \(z=\cot C\), and \(k=x+y+z\). From \(A+B+C=\pi\), the cotangent addition formula gives \(xy+yz+zx=1\). Also \(x+y=\sin C/(\sin A\sin B)>0\), and similarly for the other two pairs. Hence
\[
 k^2-3=x^2+y^2+z^2-1=\tfrac12[(x-y)^2+(y-z)^2+(z-x)^2]\ge0.
\]
For fixed \(k>\sqrt3\), the intersection of \(x+y+z=k\) with \(xy+yz+zx=1\) is a circle. The displayed cosine parametrization in the finding runs once around that circle. Each of its points has every pairwise sum positive: for example \(x+y=\tfrac23[k+s\cos(\phi+\pi/3)]>0\), since \(s<k\). Consequently \(A=\operatorname{arccot}x\), \(B=\operatorname{arccot}y\), \(C=\operatorname{arccot}z\), all in \((0,\pi)\), satisfy \(A+B+C=\pi\). Thus the parametrization is a bijection off the equilateral point.

**2. The Jacobian.** Differentiating the cosine parametrization gives
\[
\left|\frac{\partial(x,y)}{\partial(k,\phi)}\right|=\frac{x+y}{\sqrt3}.
\]
Using \(dA=-dx/(1+x^2)\), \(dB=-dy/(1+y^2)\), and the sine addition formula, this yields
\[
\left|\frac{\partial(A,B)}{\partial(k,\phi)}\right|
=\frac{x+y}{\sqrt3(1+x^2)(1+y^2)}
=\frac{\sin A\sin B\sin C}{\sqrt3}.
\]
The cosine expansion gives the exact cubic product
\[
 xyz=\frac{-2k^3+9k+2s^3\cos(3\phi)}{27}.
\]
Expanding \(\cos(A+B+C)=-1\) gives
\[
 k-xyz=\frac1{\sin A\sin B\sin C},
\]
so the Jacobian becomes
\[
\left|\frac{\partial(A,B)}{\partial(k,\phi)}\right|=
\frac{9\sqrt3}{2[k^3+9k-s^3\cos(3\phi)]}.
\]
Multiplication by the uniform-simplex density \(2/\pi^2\) proves the claimed joint density. This is an exact change of variables, not a simulation argument.

**3. Exact marginal.** For real \(a>|b|\), the elementary tangent-half-angle integral is
\[
\int_0^{2\pi}\frac{du}{a-b\cos u}=\frac{2\pi}{\sqrt{a^2-b^2}}.
\]
For \(a=k^3+9k\) and \(b=s^3\), direct polynomial expansion gives
\[
 a^2-b^2=27(1+k^2)^2.
\]
Integrating the joint density over the phase, and noting that \(\cos(3\phi)\) has three periods, yields \(f_K(k)=6/[\pi(1+k^2)]\) on \(k>\sqrt3\). Since \(\omega=\operatorname{arccot}K\) and \(|dk/d\omega|=1+k^2\), its density is constant \(6/\pi\) on \((0,\pi/6)\). The integral of this density is one, completing the distributional proof.

**4. Conditional marks and consequences.** Division by the marginal gives
\[
 f_{\Phi\mid K}(\phi\mid k)=\frac{3\sqrt3(1+k^2)}{2\pi\,[k^3+9k-s^3\cos(3\phi)]}.
\]
Writing \(a=k^3+9k\), \(b=s^3\), \(D=\sqrt{a^2-b^2}=3\sqrt3(1+k^2)\), and \(r=b/(a+D)\), the identity \(D/(a-b\cos u)=(1-r^2)/(1-2r\cos u+r^2)\) proves the Poisson-kernel form. Since \(r\to0\) as \(k\downarrow\sqrt3\) and \(r\to1\) as \(k\to\infty\), the claimed phase limits follow from the normalized Poisson approximate identity. The mean of the uniform Brocard angle is \(\pi/12\). Finally \(f_K(k)\sim 6/(\pi k^2)\), making the \(p\)-th moment integral finite exactly for \(p<1\), for any \(p\ge0\).

## Verification
The accompanying `check_brocard.py` evaluates the joint density's phase integral against the derived Cauchy density, checks the discriminant identity and the Poisson-kernel reduction at several nontrivial parameters, and numerically reconstructs the phase from independent angle triples. A separately coded direct circle-coordinate simulation of 300,000 triples evaluates the Brocard angle from chord lengths and Euclidean triangle area; five empirical CDF values agree with \(6t/\pi\) within their stated binomial tolerances. The executable check ends with `BROCARD_UNIFORM_PHASE_CHECKS_OK`. These finite checks corroborate, but do not replace, the exact algebra and integral above.

## Relationship to prior work
Bényi and Ćurgus (2011, revised 2013) classify Euclidean triangles by their Brocard angle and relate it to a cone angle for squared-side vectors; their Proposition 4.1 gives a deterministic Brocard/cone relation but no sampling distribution or conditional phase law. Edelman and Strang (2015) explicitly contrast uniform-angle triangles with Gaussian-coordinate triangles and develop a general shape-hemisphere representation; neither their uniform-angle description nor their Gaussian shape measure evaluates the Brocard-angle pushforward for circle-sampled triangles. Finch (2014) studies other constrained random-triangle laws. A published fixed-Brocard-angle side-ratio interval determines extremal ratios on individual angle level sets; it does not integrate their sampling weights or imply the wrapped Poisson conditional density. These exact statements were compared, rather than merely their titles.

The new assertion is specifically the uniform Brocard marginal and the explicitly normalized marked joint density, not the classical cotangent formula, the squared-side cone representation, or the existence of a uniform-angle simplex. No definitive exhaustive priority assertion is made.

## Limitations
The theorem requires exactly three independent arclength-uniform points on one circle. The phase mark is defined only away from the probability-zero equilateral case and depends on cyclic labeling; its threefold density is labeling-compatible. This is a population-law statement without finite-sample reconstruction or statistical stability bounds. An unindexed classical treatment of precisely this marginal or an equivalent pushforward remains a residual priority risk. No independent mathematical audit has been performed.

## References
1. Á. Bényi and B. Ćurgus, *Triangles and groups via cevians*, arXiv:1109.0557, first public 2 September 2011; Proposition 4.1 and Section 11. https://arxiv.org/html/1109.0557v2
2. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first public 9 January 2015; Sections 1.1, 2, and 3.6. https://arxiv.org/html/1501.03053v1
3. S. R. Finch, *Uniform Triangles with Equality Constraints*, arXiv:1411.5216, first public 19 November 2014. https://arxiv.org/abs/1411.5216
4. *Sharp side-ratio interval at fixed Brocard angle*, publicly available mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-side-ratio-interval-at-fixed-brocard-angle--f45049753ddd
5. E. W. Weisstein, *Brocard Angle*, MathWorld, classical identity reference. https://mathworld.wolfram.com/BrocardAngle.html
