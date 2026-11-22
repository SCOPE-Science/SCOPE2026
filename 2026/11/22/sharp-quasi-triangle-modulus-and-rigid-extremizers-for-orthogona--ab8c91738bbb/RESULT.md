# Sharp quasi-triangle modulus and rigid extremizers for orthogonally stretched ellipse gauges

## Finding
Let \(a\ge b>0\). On the real plane define the continuous, absolutely homogeneous gauge
\[
q_{a,b}(s,t)=\min\left\{\sqrt{\frac{s^2}{a^2}+\frac{t^2}{b^2}},\sqrt{\frac{s^2}{b^2}+\frac{t^2}{a^2}}\right\}.
\]
Its sharp binary quasi-triangle modulus is
\[
\boxed{K(a,b)=\sup_{(x,y)\ne(0,0)}\frac{q_{a,b}(x+y)}{q_{a,b}(x)+q_{a,b}(y)}=\frac{a^2+b^2}{2ab}.}
\]
For \(a>b\), put \(L=\sqrt{a^2+b^2}\), \(e=(a^2,b^2)/L\), and \(f=(b^2,a^2)/L\). Every equality pair, up to interchanging the two vectors, is exactly
\[
(x,y)=(\tau(\epsilon_1e_1,\epsilon_2e_2),\tau(\epsilon_1f_1,\epsilon_2f_2)),
\qquad \tau>0,\quad\epsilon_1,\epsilon_2\in\{-1,1\}.
\]
If \(a=b\), the gauge is a rescaled Euclidean norm, with modulus one and the usual nonnegative-collinearity equality condition (including a zero input).

Writing \(C=\operatorname{conv}(\{q_{a,b}\le1\})\) and \(p_C\) for its Minkowski gauge, the exact convexification distortion is likewise
\[
\sup_{z\ne0}\frac{q_{a,b}(z)}{p_C(z)}=K(a,b).
\]
More explicitly, for \(a>b\), write \(M=\max\{|s|,|t|\}\) and \(m=\min\{|s|,|t|\}\). The entire convexified norm is
\[
p_C(s,t)=\begin{cases}
\sqrt{M^2/a^2+m^2/b^2},&m\le(b^2/a^2)M,\\
(M+m)/L,&(b^2/a^2)M\le m\le M.
\end{cases}
\]
For \(a=b\) this reduces to the rescaled Euclidean norm. The two branches agree continuously on their dividing rays.

In the anisotropy ratio \(r=a/b\ge1\) this is \((r+r^{-1})/2\), with an exact quadratic departure \(K-1=(r-1)^2/(2r)\) from convexity and linear growth in \(r\) at high anisotropy.

## Assumptions and scope
The scalars and vectors are real, the dimension is exactly two, and the ellipses are centered, have aligned axes and have the swapped semiaxes \((a,b)\) and \((b,a)\). The result does not assert a corresponding formula for arbitrary rotated or translated ellipses or for higher-dimensional ellipsoids. All suprema are over two inputs with a nonzero denominator; the gauge vanishes only at the origin. The convexified gauge \(p_C\) is a norm because \(C\) is a compact centrally symmetric convex body with interior.

## Proof
Define \(E_1=\{(s,t):s^2/a^2+t^2/b^2\le1\}\) and \(E_2=\{(s,t):s^2/b^2+t^2/a^2\le1\}\). Then the unit ball \(B=E_1\cup E_2\), and \(C=\operatorname{conv}(E_1\cup E_2)\). The support functions are
\[
h_1(u)=\sqrt{a^2u_1^2+b^2u_2^2},\qquad h_2(u)=\sqrt{b^2u_1^2+a^2u_2^2}.
\]
For \(a>b\), their squares differ by \((a^2-b^2)(u_1^2-u_2^2)\). If \(|u_1|>|u_2|\), the support point of \(C\) is uniquely the \(E_1\)-support point \((a^2u_1,b^2u_2)/h_1(u)\); it satisfies \(|s|>|t|\), and hence \(q_{a,b}=\sqrt{s^2/a^2+t^2/b^2}=1\) there. The analogous claim applies to the \(E_2\)-support points when \(|u_2|>|u_1|\). Thus all exposed curved portions of \(\partial C\) have \(q_{a,b}=1\).

The remaining supporting directions have \(|u_1|=|u_2|\ne0\). In each signed quadrant their exposed face is the segment joining the two points obtained by applying the corresponding coordinate signs to \(e=(a^2,b^2)/L\) and \(f=(b^2,a^2)/L\). There are four such segments, one per signed diagonal. On the positive one, its midpoint is \(m=(L/2,L/2)\), for which
\[
q_{a,b}(m)=\frac{L}{2}\sqrt{a^{-2}+b^{-2}}=\frac{a^2+b^2}{2ab}=:K>1.
\]
At either endpoint the gauge equals one. On the half segment where \(s\ge t\), the squared gauge equals the strictly convex quadratic \(s^2/a^2+t^2/b^2\); on the other half it equals the strictly convex quadratic with \(a,b\) interchanged. Consequently the maximum on each half is at an endpoint of that half; since \(K>1\), each half has the unique maximum \(m\). Coordinate-sign symmetries give exactly four global maximizing boundary points of \(C\), namely \((\pm L/2,\pm L/2)\).

The support-point transition gives the full convexified norm formula: in the wedge \(s\ge t\ge0\), the radial boundary is the \(E_1\)-arc while \(t/s\le b^2/a^2\) and the tangent segment \(s+t=L\) while \(b^2/a^2\le t/s\le1\). Its radial gauge is respectively \(\sqrt{s^2/a^2+t^2/b^2}\) and \((s+t)/L\). Reflections and coordinate interchange give the displayed \(M,m\)-formula globally.

Every nonzero interior point of \(C\) scales radially to a boundary point, so homogeneity gives \(\max_{C}q_{a,b}=K\). Now let \(x,y\) be two vectors with \(q(x)+q(y)>0\), and write \(s=q(x), t=q(y)\). If both are nonzero, \(x/s,y/t\in B\), and
\[
\frac{x+y}{s+t}=\frac{s}{s+t}\frac{x}{s}+\frac{t}{s+t}\frac{y}{t}\in C.
\]
Hence \(q(x+y)\le K(s+t)\). If either vector vanishes, the ratio is one. The explicitly displayed pair \((e,f)\) has \(q(e)=q(f)=1\) and \(q((e+f)/2)=K\), proving the sharp constant.

For equality with \(a>b\), the normalized sum \((x+y)/(s+t)\) must equal one of the four strict maximizing midpoints. Its unique supporting line is the common tangent, whose intersection with \(B\) consists of precisely the two ellipsoidal contact points at the segment endpoints: strict convexity of each ellipse rules out any further points. Therefore \(x/s,y/t\) are those endpoints, in some order. Their convex combination is the midpoint only when \(s/(s+t)=1/2\), so \(s=t>0\). This proves the complete equality classification. For \(a=b\), ordinary Euclidean triangle equality settles the remaining case.

Finally, for \(z\ne0\), \(q(z)/p_C(z)=q(z/p_C(z))\). The normalized point belongs to \(\partial C\), and the sharp maximum is \(K\); thus the convexification ratio is exactly \(K\).

## Verification
The proof above is analytic in the continuous parameters. The standalone Python standard-library checker at `scripts/check.py` independently tests explicit contact points with exact rational arithmetic for Pythagorean semiaxes, the predicted constant across multiple real parameters, coordinate-sign rigid extremizers, and the global inequality on deterministic pseudorandom rational input pairs. Execute with `python scripts/check.py` from the package root. Numerical tests are diagnostics only: they do not prove the inequality or exhaust all inputs. The support-function and exposed-face arguments supply the infinite-quantifier proof.

## Relationship to prior work
Unser's 4 November 2026 preprint, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines* (arXiv:2611.06212), characterizes continuous positive homogeneous quasi-norms, describes their star-shaped unit balls, and distinguishes general quasi-triangle bounds from sharp moduli. It does not classify the sharp modulus or equality cases of the two swapped-axis Euclidean ellipse gauges. Kwun et al. (2016) study generalized von Neumann–Jordan and James constants on quasi-Banach spaces; their normalizing quasi-triangle parameter is assumed, rather than evaluated for this family. Public published-finding corpus summaries of an exact four-weight octagonal conic-spline modulus (17 November 2026) and a convex-hull area law for equal-area ellipses (18 October 2026) concern respectively polyhedral unit balls and area, not the exact smooth-ellipse gauge distortion or its equality pairs. These comparisons are distinctions of statements and hypotheses, not an assertion that keyword searches certify novelty.

## Limitations
The theorem concerns only swapped-axis centered planar ellipses over the reals. It makes no claim about arbitrary pairs of ellipsoids, regularization performance, numerical optimization algorithms, or full bibliographic uniqueness. An equivalent statement may be embedded in an unindexed general treatment of nonconvex Minkowski gauges; one relevant public geometric finding was available only as an indexed summary rather than a complete inspected manuscript. No independent audit has been carried out.

## References
1. Michael Unser, *Quasi-norms on \(\mathbb R^d\): Characterization and Approximation by Conic Splines*, arXiv:2611.06212v1 (first posted 4 November 2026), https://arxiv.org/abs/2611.06212 .
2. Young Chel Kwun, Qaisar Mehmood, Waqas Nazeer, Absar Ul Haq and Shin Min Kang, *Relations between generalized von Neumann–Jordan and James constants for quasi-Banach spaces*, Journal of Inequalities and Applications 2016:171, https://doi.org/10.1186/s13660-016-1115-z .
3. Published published-finding corpus finding, *Exact twelve-branch quasi-triangle modulus of four-weight octagonal conic splines* (17 November 2026), identifier `886effdf11c1`.
4. Published published-finding corpus finding, *An affine-invariant exact convex-hull area law for equal-area ellipses* (18 October 2026), identifier `ff4feeef7ef8`.
