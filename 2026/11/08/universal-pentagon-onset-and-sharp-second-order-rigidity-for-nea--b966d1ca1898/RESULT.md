# Universal pentagon onset and sharp second-order rigidity for nearly central box sections

## Finding

Let \(B=[-a,a]\times[-b,b]\times[-c,c]\) for arbitrary fixed \(a,b,c>0\), put \(R=\sqrt{a^2+b^2+c^2}\), and let \(U\) be uniformly distributed on the unit sphere \(S^2\). For real \(t\), denote by \(q_5(t)\) the probability that the plane \(\{x:U\cdot x=t\}\) cuts \(B\) in a nondegenerate pentagon. Then, as \(t\to0\),

\[
q_5(t)=\frac{4|t|}{R}-\frac{4t^2}{\pi}\left(\frac1{a\sqrt{b^2+c^2}}+\frac1{b\sqrt{a^2+c^2}}+\frac1{c\sqrt{a^2+b^2}}\right)+O_{a,b,c}(|t|^3).
\]

The first-order coefficient depends only on the length \(2R\) of a body diagonal. More sharply, under the constraint \(a^2+b^2+c^2=R^2\), the coefficient of \(t^2\) is maximal (least negative) **uniquely** at \(a=b=c=R/\sqrt3\), where it equals \(-18\sqrt2/(\pi R^2)\). In particular, at a fixed diagonal length, every fixed noncubical rectangular box has strictly smaller pentagon probability than the cube for all sufficiently small positive offsets (the threshold may depend on the box).

## Assumptions and scope

The box is centered and has three mutually perpendicular pairs of faces; the positive half-lengths are fixed while the offset tends to zero. The normal is uniformly oriented (Haar surface probability on \(S^2\)), **not** sampled from an invariant measure on all affine planes. The section type is counted only for generic directions, excluding a measure-zero set of tangencies and vertex incidences. The statements hold for either sign of the offset because the body is centrally symmetric. No joint limit with degenerating half-lengths is asserted.

## Proof

**1. Reduction to signed vertex heights and section type.** By coordinate-reflection symmetry it is enough to work with \(u_i=|U_i|\ge0\), uniform on the positive spherical octant, with density \(2/\pi\) with respect to spherical area. Write \(x_1=au_1\), \(x_2=bu_2\), \(x_3=cu_3\), \(S=x_1+x_2+x_3\), and \(d_i=S-2x_i\). The eight signed box-vertex heights are \(\pm S,\pm d_1,\pm d_2,\pm d_3\). Set \(E_i(t)=\{|d_i|<t\}\) for \(t>0\).

For \(0<t<\min(a,b,c)/3\), \(S\ge\min(a,b,c)>3t\), so at most two of the \(E_i(t)\) hold: indeed \(d_1+d_2+d_3=S\). The positive-height vertices for the plane at height \(t\) are the vertex of height \(S\) and precisely one vertex from each pair \(\pm d_i\) when \(|d_i|>t\). Hence the number of positive vertices is \(4-k\), where \(k=\sum_i\mathbf1_{E_i(t)}\). A cube edge crosses the section plane iff its endpoints have opposite signs relative to \(t\). If \(k=1\), both other \(d_j\) are \(>t\); the three positive vertices form a two-edge star, and the number of crossing edges is \(3(3)-2(2)=5\). If \(k=2\), the remaining \(d_j>t\) and the two positive vertices are adjacent, giving \(3(2)-2(1)=4\). If \(k=0\), either all three \(d_i>t\) (six crossings), or precisely one \(d_i<-t\) (four crossings). Here the crossing-edge count equals the number of vertices of the section polygon. Therefore the section is pentagonal **if and only if exactly one** of \(E_1,E_2,E_3\) occurs. With no triple overlap,

\[
q_5(t)=\frac2\pi\left(\sum_i\operatorname{area}(E_i(t))-2\sum_{i<j}\operatorname{area}(E_i(t)\cap E_j(t))\right).
\]

**2. First-order spherical strip areas.** The linear form \(d_i=-a_i u_i+a_j u_j+a_k u_k\) has Euclidean coefficient norm \(R\), where \((a_1,a_2,a_3)=(a,b,c)\). Its zero great circle intersects the positive octant in a single arc of length

\[
L_i=\arccos\frac{a_j a_k}{\sqrt{(a_i^2+a_j^2)(a_i^2+a_k^2)}}=\arctan\frac{a_i R}{a_j a_k}.
\]

These endpoint intersections with coordinate great circles are transverse, so the arclength of the nearby level circle \(d_i=s\), restricted to the octant, is a smooth function of \(s\) near zero. The spherical coarea formula has factor \(1/\sqrt{R^2-s^2}\). Integrating symmetrically from \(-t\) to \(t\) eliminates the linear variation of that smooth factor and yields

\[
\operatorname{area}(E_i(t))=\frac{2L_i}{R}t+O_{a,b,c}(t^3).
\]

Let \(T_i=\tan L_i=a_iR/(a_j a_k)\). One has \(T_1+T_2+T_3=T_1T_2T_3\), since \(a^2+b^2+c^2=R^2\), and \(1-(T_1T_2+T_2T_3+T_3T_1)<0\). The tangent addition formula and \(0<L_i<\pi/2\) imply \(L_1+L_2+L_3=\pi\). Thus the sum of individual strip areas is \(2\pi t/R+O(t^3)\).

**3. Pairwise intersections and the quadratic term.** For distinct \(i,j\) let \(k\) be the remaining index. The two arcs \(d_i=0\), \(d_j=0\) meet in the positive octant at the boundary point \(u_k=0\) and \(a_i u_i=a_j u_j\); their intersections with small strips are confined to a neighborhood of this point. Set \(\delta=a_j u_j-a_i u_i\) and \(w=u_k\ge0\). Then \(d_i=\delta+a_kw\) and \(d_j=-\delta+a_kw\), so their simultaneous strip inequalities are exactly \(|\delta|+a_kw<t\). The spherical area measure near this point satisfies

\[
d\Omega=\left(\frac1{\sqrt{a_i^2+a_j^2}}+O_{a,b,c}(t)\right)d\delta\,dw.
\]

The triangle \(\{w\ge0:\ |\delta|+a_kw<t\}\) has Euclidean coordinate area \(t^2/a_k\). Consequently,

\[
\operatorname{area}(E_i(t)\cap E_j(t))=\frac{t^2}{a_k\sqrt{a_i^2+a_j^2}}+O_{a,b,c}(t^3).
\]

Summing the three pairs, inserting the individual strip areas, and using \(q_5(-t)=q_5(t)\) proves the claimed expansion.

**4. Sharp shape rigidity.** Put \(v_i=a_i^2/R^2\), so \(v_i\in(0,1)\) and \(\sum_i v_i=1\). The positive quadratic penalty is

\[
\sum_i\frac1{a_i\sqrt{R^2-a_i^2}}=R^{-2}\sum_i\frac1{\sqrt{v_i(1-v_i)}}.
\]

The function \(f(v)=[v(1-v)]^{-1/2}\) is strictly convex on \((0,1)\) (its logarithm has strictly positive second derivative). Jensen's inequality gives \(\sum_i f(v_i)\ge3f(1/3)=9/\sqrt2\), with equality iff \(v_1=v_2=v_3=1/3\). This proves optimality, uniqueness, and the fixed-noncube comparison: the two boxes have identical first-order coefficients but strictly different second-order coefficients, while their respective remainders are \(O(t^3)\).

## Verification

An independent numerical checker enumerates all 12 edges of each sampled rectangular box and counts intersections with the offset plane, rather than using the derived strip formula to classify polygon type. It confirms the exact equivalence between five section vertices and precisely one strip event in 16,800,000 normal/offset/box trials. For four boxes and twelve offset configurations, Monte Carlo probabilities agree with the first two analytic terms within recorded sampling uncertainty and cubic remainder tolerance. Run `python check_near_center.py` with Python 3 and NumPy installed. This is a finite diagnostic, not the proof of the asymptotic expansion or global equality classification; those are proved above.

## Relationship to prior work

Lonke's 1998 work derives expected face counts for Haar-random **central** sections of a cube in arbitrary dimensions, including three-dimensional benchmark values. Existing results for central sections of rectangular boxes provide a formula for their hexagon probabilities and cubic extremality. Those statements apply at offset zero, where the pentagon event has probability zero: they do not supply the one-sided derivative or the shape-sensitive second-order coefficient for translated planes. Zhang's 2020 cube-section solution also concerns central sections. Coleman's random probes through boxes are one-dimensional chord-length distributions under different sampling mechanisms. This finding studies a different measurable statistic on a fixed-offset Haar family of planes; the claimed contribution is specifically the two-term pentagon onset and its sharp second-order optimizer, not the central-section polygon law.

## Limitations

The \(O_{a,b,c}(|t|^3)\) bound is local for each fixed box and is not uniform over degenerating aspect ratios. The first-order coefficient alone cannot recover individual dimensions. The second-order coefficient distinguishes cubes from noncubes at a fixed diagonal length but does not determine all three lengths from one scalar coefficient. The source search is not an exhaustive historical priority proof. The numerical tests do not replace the coarea and edge-graph arguments.

## References

- Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, submitted 1998-12-21; later *Discrete & Computational Geometry* 23 (2000), 157–169. https://arxiv.org/abs/math/9812123
- Y. Zhang, *A purely 3-D geometrical solution to Mathematics Magazine Problem 2065*, arXiv:2010.12349, first posted 2020-10-20. https://arxiv.org/abs/2010.12349
- R. Coleman, *Intercept lengths of random probes through boxes*, *Journal of Applied Probability* 18 (1981), 276–282. https://doi.org/10.2307/3213189
