# Parity-resolved central-chord laws for regular polygons

## Finding
Fix an integer \(n\ge3\), a circumradius \(R>0\), and a centered regular \(n\)-gon \(P_n\). Select an **unoriented line through its center** with uniform angular direction on \([0,\pi)\), and let \(L_{n,R}\) be the length of the intersection with \(P_n\). Set \(b=\pi/n\) and \(r=R\cos b\). With \(U\) uniform on \([0,1]\), the complete chord laws are
\[
L_{n,R}\overset{\rm d}=\begin{cases}
2r\sec(bU),&n\text{ even},\\
r\{\sec(bU)+\sec[b(1-U)]\},&n\text{ odd}.
\end{cases}
\]
For the odd case the right-hand side has the same law as \(r\{\sec[b(1+U)/2]+\sec[b(1-U)/2]\}\). Both displayed one-parameter functions using the second odd form are strictly increasing on \((0,1)\), hence furnish exact quantile functions. In particular, if \(n\) is odd and both polygons have the same circumradius, then a monotone rational transport determines the **entire** odd-polygon chord law from the even-polygon law:
\[
L_{n,R}\overset{\rm d}=T_{n,R}(L_{2n,R}),\qquad
T_{n,R}(z)=\frac{z\cos b}{1-z^2\tan^2(b/2)/(4R^2)}.
\]
The transport is strictly increasing throughout the support of \(L_{2n,R}\), namely \([2R\cos(b/2),2R]\).

The mean is the same algebraic function for both parities:
\[
\mathbb E L_{n,R}=\frac{2r}{b}\log(\sec b+\tan b).
\]
The second moment distinguishes parity:
\[
\mathbb E L_{n,R}^2=\begin{cases}
\displaystyle\frac{4r^2}{b}\tan b,&n\text{ even},\\[4pt]
\displaystyle\frac{2r^2}{b}\left(\tan b-\frac{2\log(\cos b)}{\sin b}\right),&n\text{ odd}.
\end{cases}
\]
Consequently the exact variance equals this second moment minus the square of the displayed mean.

A singularly informative difference appears when the polygons approach the unit circle. Along the even and odd subsequences separately, the rescaled diameter deficiency has the following **nondegenerate distributional limits**, with convergence of every finite polynomial moment:
\[
\frac{n^2}{\pi^2R}(2R-L_{n,R})\Longrightarrow
\begin{cases}1-U^2,&n\text{ even},\\[2pt]
\displaystyle\frac12+U-U^2,&n\text{ odd}.
\end{cases}
\]
In particular,
\[
\lim_{\substack{n\to\infty\\n\text{ even}}}
\frac{n^4\operatorname{Var}(L_{n,R})}{\pi^4R^2}=\frac4{45},
\qquad
\lim_{\substack{n\to\infty\\n\text{ odd}}}
\frac{n^4\operatorname{Var}(L_{n,R})}{\pi^4R^2}=\frac1{180}.
\]
The variance constants differ by a factor of sixteen, despite the identical limiting circular chord length \(2R\).

## Assumptions and scope
The polygon is a full-dimensional Euclidean regular polygon, with \(n\ge3\), not an arbitrary cyclic polygon. The center is its circumcenter, and all chosen lines **must pass through that center**. A direction is selected using normalized Lebesgue measure on unoriented angles; this is *not* the translation-invariant random-line law in which the line's offset is also randomized. Endpoint directions passing through vertices have angular measure zero and the formulas extend there continuously. All moments concern chord length, not distance between independently sampled interior points.

## Proof
Choose outward normals \(\nu_j\) for the polygon sides at angular increments \(2\pi/n\). Every side line has signed distance \(r=R\cos(\pi/n)\) from the origin. Along a ray whose direction differs by \(t\in[-b,b]\) from its nearest side normal, the first boundary intersection is at radial distance \(r\sec t\). The nearest-normal signed gap for a uniformly random direction is uniform on \([-b,b]\). Its magnitude is consequently uniform on \([0,b]\).

For even \(n\), antipodal side normals exist; the two ray lengths along any unoriented line are both \(r\sec t\). This proves the even distributional identity.

For odd \(n\), rotating a ray by \(\pi\) sends the side-normal grid into the same grid shifted by half a normal spacing, namely \(b\). Thus if the first ray has unsigned angular gap \(t\), the opposite ray has gap \(b-t\). Here \(t\) is uniform on \([0,b]\). Their radial lengths add, proving the odd law. The function \(\sec(bu)+\sec[b(1-u)]\) is symmetric under \(u\mapsto1-u\), strictly decreases for \(u\in(0,1/2)\), and strictly increases for \(u\in(1/2,1)\), since \(\sec'(x)=\sec x\tan x\) strictly increases on \([0,b]\). Folding \(u\) about \(1/2\) produces the uniform variable \(|2U-1|\) and the increasing odd quantile function. The even quantile is plainly increasing.

For odd \(n\), write \(c=\cos(b/2)\) and \(s=\sin(b/2)\). The odd quantile at \(u\) is, by adding the two secants,
\[
2R\cos b\,\frac{c\sec(bu/2)}{1-s^2\sec^2(bu/2)}.
\]
The even \(2n\)-gon's quantile is \(z=2Rc\sec(bu/2)\). Substituting this \(z\) gives exactly \(T_{n,R}(z)\). Its denominator is positive on the stated support: there it is at least \(1-\tan^2(b/2)>0\), since \(b/2\le\pi/6\). Differentiation gives \(T'(z)=\cos b(1+az^2)/(1-az^2)^2>0\) with \(a=\tan^2(b/2)/(4R^2)\). This proves the transport as an equality of quantile functions, not merely an equality of individual moments.

For the mean, integrate each quantile from zero to one, using \(\int\sec x\,dx=\log(\sec x+\tan x)\). For the second moment, use \(\int_0^b\sec^2x\,dx=\tan b\) and the cross-term integral
\[
\int_0^b\sec x\sec(b-x)\,dx
=\frac{1}{\sin b}\int_0^b\{\tan x+\tan(b-x)\}\,dx
=-\frac{2\log(\cos b)}{\sin b}.
\]
Substitution gives the displayed formulas in each parity.

For the limit laws, use the **same** uniform \(U\) in the exact identities for each \(n\). Uniform Taylor expansions on \([0,1]\) yield
\[
\frac{2R-2R\cos b\sec(bU)}{Rb^2}=1-U^2+O(b^2)
\]
when \(n\) is even, and
\[
\frac{2R-R\cos b\{\sec(bU)+\sec[b(1-U)]\}}{Rb^2}
=\frac12+U-U^2+O(b^2)
\]
when \(n\) is odd. Both error bounds are uniform in \(U\). Therefore the variables converge almost surely in the displayed coupling and in every finite \(L^p\), implying the claimed weak convergence and convergence of polynomial moments. Finally \(\operatorname{Var}(U^2)=1/5-1/9=4/45\) and \(\operatorname{Var}(U-U^2)=1/30-1/36=1/180\). Restoring \(Rb^2=R\pi^2/n^2\) proves both variance constants.

## Verification
The companion standard-library `verify.py` computes each chord independently by intersecting its line with **every polygon edge**, and compares it to the nearest-side-normal formula. It independently integrates quantiles to check both moments, checks the odd-to-even rational transport at many angles, and evaluates scaled limit means for four large polygon orders. On execution it reports `VERIFY_OK` and 1,958 deterministic diagnostics. These are finite checks supporting, not replacing, the proof for all integers \(n\).

## Relationship to prior work
Harutyunyan and Ohanyan (2009) obtain the regular-polygon chord-length distribution under motion-invariant measure \(dp\,d\phi\) on line **offsets and angles**. Bäsel (2012), in a distinct derivation of that same offset-randomized distribution, derives random-point distance laws as well. Their complete accessible papers were inspected, including definitions, main results, and appendices/references. Neither investigated distribution is the law of center-constrained angular chords, and a marginal distribution integrating over offsets does not determine a conditional law at offset zero. The parity-specific quantile coupling, rational odd-to-double-side transport, and fluctuation limit established here therefore are not consequences of their stated chord distribution functions. Existing polygon-center symmetrization and discrete vertex metric results concern different functionals; their statements do not imply this angular chord law. These distinctions are mathematical implication comparisons, not a claim of exhaustive historical priority.

## Limitations
The analysis is confined to uniform **angular** randomness with the line passing through the center. It does not describe motion-invariant lines, off-center lines, arbitrary polygon perturbations, random segment endpoints, or fluctuations in dimensions greater than two. Numerical tests are finite and cannot certify historical originality or infinite quantifiers. Literature searches can miss older results expressed with different geometric terminology, and the present comparison does not establish priority over inaccessible or unindexed work. Independent audit has not been performed.

## References
1. H. S. Harutyunyan and V. K. Ohanyan, *The chord length distribution function for regular polygons*, Advances in Applied Probability (SGSA) 41 (2009), 358–366. DOI: 10.1239/aap/1246886615. Full-text URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B6106C113723976E5F1DDDF89FB47D58/S0001867800003335a.pdf/the-chord-length-distribution-function-for-regular-polygons.pdf.
2. Uwe Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707, first public 12 April 2012 (version 1); later Acta Math. Univ. Comenianae 83 (2014), 1–18. Full-text URL: https://arxiv.org/pdf/1204.2707.
