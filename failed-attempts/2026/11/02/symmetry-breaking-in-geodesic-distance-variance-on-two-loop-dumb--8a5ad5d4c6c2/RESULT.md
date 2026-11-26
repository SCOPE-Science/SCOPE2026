# Symmetry breaking in geodesic-distance variance on two-loop dumbbell networks

## Finding
Let \(G(a,b,t)\) be the compact metric graph consisting of a circle of length \(a>0\), a circle of length \(b>0\), and one connecting interval of length \(t>0\), attached at one vertex of each circle. All distances are intrinsic shortest-path distances, including between points in edge interiors. For independent points \(X,Y\) distributed uniformly by total arclength, write \(D=d_G(X,Y)\), \(s=a+b\), \(r=t/s\), and \(p=ab/s^2\). Thus \(0<p\le1/4\); \(p=1/4\) means equal circle lengths.

Let \(\alpha\) be the unique positive zero of
\[
C(r)=16r^3+24r^2+30r-3,
\]
and let \(\beta\) be the unique positive zero of
\[
Q(r)=8r^4+16r^3+32r^2-2r-1.
\]
These satisfy
\[
\frac9{100}<\alpha<\frac1{10}<\frac{19}{100}<\beta<\frac15,
\qquad
\alpha=0.092700443813660\ldots,\quad
\beta=0.198388336333870\ldots.
\]

**Sharp fixed-sum variance-minimization law.** Fix \(s>0\) and \(t>0\), and vary \(a,b>0\) subject to \(a+b=s\). Then:

1. If \(0<r\le\alpha\), the unique variance minimizer, up to exchanging the two circles, has \(a=b=s/2\).
2. If \(\alpha<r<\beta\), the unique minimizing unordered pair of positive lengths is asymmetric and is determined by
\[
\frac{ab}{s^2}=p_*(r):=\frac{1+2r-32r^2-16r^3-8r^4}{1+32r-44r^2}\in(0,1/4),
\qquad
\{a,b\}=\left\{\frac{s(1+\sqrt{1-4p_*})}{2},\frac{s(1-\sqrt{1-4p_*})}{2}\right\}.
\]
3. If \(r\ge\beta\), the variance is strictly increasing in \(p\), so the infimum occurs only in the excluded degenerate limit where one circle length tends to zero. There is no minimizer among \(a,b>0\).

The middle regime is a genuine symmetry-breaking window: the variance-minimizing network has unequal loops even though its mean distance is still uniquely minimized by equal loops (since \(r<\beta<1/4\)). As an exact rational witness at \(r=1/10\),
\[
p_*=\frac{1079}{4700},\qquad
\frac{\operatorname{Var}_{p=1/4}(D)-\operatorname{Var}_{p=p_*}(D)}{s^2}
=\frac{384}{17203175}>0.
\]

## Assumptions and scope
The two circles are allowed to be modeled as loop edges. Subdividing either circle at additional vertices does not alter the metric or arclength measure. The sole connecting path is a bridge of positive length; there are no other edges or shortcuts. The total circle length \(s\) and connecting length \(t\) are fixed when optimizing. All sample points are independently arclength-uniform over the **entire** network of length \(s+t\), and \(D\) is a continuous random variable. The variance, not its uncentered second moment, is optimized. Optimization is over strictly positive circle lengths; the zero-length boundary is not admissible.

## Proof
**1. Complete pair-type decomposition.** On a circle of circumference \(u\), the distance of an arclength-uniform point to a fixed attachment vertex is uniformly distributed on \([0,u/2]\). The geodesic distance between two independent uniform points of that circle has the same distribution. Consequently both have first moment \(u/4\) and second moment \(u^2/12\). For a bridge of length \(t\), the distance between two independent uniform bridge points has first moment \(t/3\) and second moment \(t^2/6\).

For a point on the first circle and a point on the second, the distance is exactly \(R_a+t+R_b\), where the independent radial distances \(R_a,R_b\) are uniform on \([0,a/2]\) and \([0,b/2]\). A point on a circle of length \(u\) and a point on the bridge have distance \(R_u+U\), where \(U\) is uniform on \([0,t]\), measured from the corresponding endpoint. These formulae exhaust all ordered pairs except a measure-zero collection of vertices. No alternative route can shorten them: each circle has one attachment vertex, and the bridge is the only connection between circles.

Multiplying each conditional moment by the product of the relevant component lengths, with factor two for unequal components, and dividing by \((a+b+t)^2\) yields
\[
\begin{aligned}
\mathbb E D={1\over(s+t)^2}\Big[&{a^3+b^3\over4}+2ab\Big(t+{s\over4}\Big)
+2at\Big({a\over4}+{t\over2}\Big)
+2bt\Big({b\over4}+{t\over2}\Big)+{t^3\over3}\Big],\\
\mathbb E D^2={1\over(s+t)^2}\Big[&{a^4+b^4\over12}
+2ab\Big(t^2+{ts\over2}+{a^2+b^2\over12}+{ab\over8}\Big)\\
&+2at\Big({a^2\over12}+{at\over4}+{t^2\over3}\Big)
+2bt\Big({b^2\over12}+{bt\over4}+{t^2\over3}\Big)
+{t^4\over6}\Big].
\end{aligned}
\]

**2. Two symmetric moment polynomials.** Substitute \(r=t/s\), \(p=ab/s^2\), and the identities \(a^2+b^2=s^2-2ab\), \(a^3+b^3=s^3-3sab\), \(a^4+b^4=s^4-4s^2ab+2a^2b^2\). Direct collection gives
\[
{\mathbb ED\over s}={M(r,p)\over(1+r)^2},\qquad
{\mathbb ED^2\over s^2}={N(r,p)\over(1+r)^2},
\]
where
\[
\begin{aligned}
M(r,p)&={1\over4}+{r\over2}+r^2+{r^3\over3}+p\Big(r-{1\over4}\Big),\\
N(r,p)&={1\over12}+{r\over6}+{r^2\over2}+{2r^3\over3}+{r^4\over6}
+p\Big(-{1\over6}+{r\over2}+r^2\Big)+{p^2\over12}.
\end{aligned}
\]
Hence the exact normalized variance is
\[
V(r,p):={\operatorname{Var}(D)\over s^2}
={N(r,p)(1+r)^2-M(r,p)^2\over(1+r)^4}.
\]

**3. Global optimization on the full positive length domain.** Differentiating, and collecting terms, produces the identity
\[
\boxed{\quad
(1+r)^4\frac{\partial V}{\partial p}(r,p)
=\frac{Q(r)+(1+32r-44r^2)p}{24}.\quad}
\]
At the endpoints of the admissible closed parameter interval,
\[
(1+r)^4\partial_p V(r,0)={Q(r)\over24},
\qquad
(1+r)^4\partial_p V(r,1/4)={(2r+1)C(r)\over96}.
\]
The cubic \(C\) is strictly increasing on \([0,\infty)\), with \(C(0)<0\) and \(C(r)\to+\infty\), so it has exactly one positive root \(\alpha\). The coefficients of \(Q\), in descending order, have exactly one sign change; Descartes' rule and \(Q(0)<0<Q(r)\) for sufficiently large \(r\) imply exactly one positive root \(\beta\). Direct exact rational signs at \(9/100,1/10,19/100,1/5\) establish the stated disjoint root brackets.

For \(r\le\alpha\), both endpoint derivatives are nonpositive and the derivative is strictly negative for \(0<p<1/4\), because it is affine in \(p\). Therefore \(V\) decreases strictly as the lengths are balanced; its unique minimum is at \(p=1/4\).

For \(\alpha<r<\beta\), the derivative is strictly negative at \(p=0\) and strictly positive at \(p=1/4\). Because the derivative is affine in \(p\), it crosses zero exactly once, with positive slope. Solving the derivative equation gives precisely \(p_*(r)\). Hence this interior value is the unique minimizer in \(p\); the two ordered length solutions differ only by exchanging the circles.

For \(r\ge\beta\), the derivative is positive for every \(p>0\) (also at \(r=\beta\)); the variance increases strictly toward balance, and its infimum at \(p\downarrow0\) is not attained in the required positive-length domain. These cases exhaust all \(r>0\), including both transition values.

Finally \(\partial_p(\mathbb ED/s)=(r-1/4)/(1+r)^2\), so mean distance is strictly minimized at \(p=1/4\) throughout the symmetry-breaking window. At \(r=1/10\), substituting the rational \(p_*=1079/4700\) into \(V\) gives the displayed exact variance improvement.

## Verification
The accompanying `verify_barbell.py` is executable with Python 3 and the standard library only. Execute `python3 verify_barbell.py` from the directory containing this document. It independently combines the four conditional pair-type moment formulas for 343 rational triples of positive lengths, compares the results to the symmetric polynomials, checks the exact rational critical-root sign brackets, checks the derivative endpoint factorization at nine rational bridge ratios, verifies the rational interior-minimizer witness, and performs separate direct midpoint integration of geodesic distances on 360-point arclength grids in three examples. The check returned `PASS` with maximum grid discrepancies below \(3.2\cdot10^{-5}\). The finite checks are supplementary; the proof of the universal statement is the exact pair-type integration and derivative sign argument above.

## Relationship to prior work
Doyle and Graver introduced mean distance of graph-shaped networks, including some special examples; their 1982 article was not accessible in full. Bose and collaborators (arXiv:1304.1909, first posted 2013-04-06) developed farthest-point diagrams for continuous network distances, not pair-distance variance optimization. Garijo, Márquez, and Silveira (arXiv:2103.11676; 2023 journal version), especially Section 4, give continuous **first-moment** computation for arbitrary weighted cactus graphs, including the present topology as an algorithmic special case, but do not derive a variance-minimizing loop-length allocation. Baptista, Kennedy, and Mugnolo (arXiv:2312.04952), especially Sections 3–5, investigate the **first-moment** geometric extremals and surgery rules, including flowers, rather than this second-moment symmetry-breaking transition. The new claim is the complete centered-variance allocation phase diagram at fixed circle sum and bridge length; the moment decomposition is its proof, not an assertion that the general continuous mean-distance theory was previously unknown.

## Limitations
Historical priority is not conclusively established, particularly because the full 1982 Doyle–Graver paper could not be inspected. The theorem is restricted to precisely two loop edges and one connecting interval; it does not classify general cactus graphs, arbitrarily weighted barbell graphs with additional cycles, or optimized bridge length. It concerns two independent arclength-uniform points and centered variance, not vertex-only distances, commute times, or resistance distances. For \(r\ge\beta\), the best value is a **nonattained infimum** within the strictly positive circle-length domain; it is not a realizable minimizer.

## References
1. P. Bose et al., *Network Farthest-Point Diagrams*, arXiv:1304.1909v1, posted 2013-04-06, https://arxiv.org/abs/1304.1909.
2. D. Garijo, A. Márquez, R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, arXiv:2103.11676v1 (2021); *Results in Mathematics* 78 (2023), article 139, https://arxiv.org/abs/2103.11676 and https://doi.org/10.1007/s00025-023-01902-w.
3. L. N. Baptista, J. B. Kennedy, D. Mugnolo, *Mean Distance on Metric Graphs*, arXiv:2312.04952v1 (2023); *Journal of Geometric Analysis* 34 (2024), article 137, https://arxiv.org/abs/2312.04952 and https://doi.org/10.1007/s12220-024-01574-0.
4. J. K. Doyle, J. E. Graver, *Mean Distance for Shapes*, *Journal of Graph Theory* 6 (1982), 453–471, https://doi.org/10.1002/jgt.3190060410 (full text not inspected).
