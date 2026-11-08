# Three even-distance moments give an exact and minimal inverse theorem for Euclidean parallelograms

## Finding
Let \(P\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram and let \(X,Y\) be independent points distributed uniformly with respect to **area** on \(P\). Write \(D=\|X-Y\|_2\) and
\[
M_2=\mathbb E D^2,\qquad M_4=\mathbb E D^4,\qquad M_6=\mathbb E D^6.
\]
**The three numbers \((M_2,M_4,M_6)\) determine \(P\) uniquely up to Euclidean congruence, including squares, rectangles, rhombi, and parallelograms with unequal sides and oblique angles.** The reconstruction is rational followed by one quadratic-root extraction and one angle extraction. Two initial even-distance moments do not suffice, even for strictly positive-area parallelograms.

The theorem also supplies an exact semialgebraic characterization of which real triples can arise. Given candidate \((M_2,M_4,M_6)\), define
\[
\begin{aligned}
S&=6M_2,\\
X_*&=90\left(M_4-\frac{S^2}{15}\right),\\
Y_*&=\frac{420}{S}\left(M_6-\frac{S^3}{28}\right),\\
p&=\frac{5Y_*-28X_*}{41},\\
\eta&=\frac{X_*+7p}{10p}.
\end{aligned}
\]
The triple arises from a nondegenerate parallelogram **if and only if**
\[
\boxed{S>0,\qquad 0<p\le\frac{S^2}{4},\qquad 0\le\eta<1.}
\]
For such a triple the **unordered squared side lengths** are
\[
\boxed{\left\{\frac{S+\sqrt{S^2-4p}}{2},\frac{S-\sqrt{S^2-4p}}{2}\right\},}
\]
and the acute angle between the two unoriented edge lines is \(\arccos\sqrt\eta\). Hence the conditions above are both necessary and sufficient and the recovered congruence class is unique.

## Assumptions and scope
The parallelogram is a genuine, positive-area, closed planar parallelogram. Let adjacent side-vector lengths be \(a,b>0\), and choose vector orientations so their dot product is nonnegative. Let their angle \(\phi\in(0,\pi/2]\) be the **acute unoriented edge-line angle**; swapping or reversing generating vectors changes neither the shape nor the data. Put \(u=a^2\), \(v=b^2\), and \(\eta=\cos^2\phi\in[0,1)\). Different side lengths and \(\phi\) specify one Euclidean congruence class after unordered interchange of \(a,b\). We use independent **interior area-uniform** points; choosing two boundary points, a midpoint, or a Crofton chord defines different experiments. The measurements are exact population moments, not noisy estimates.

## Proof
**1. Uniform-coordinate reduction.** Write \(P=x_0+\{s e+t f:0\le s,t\le1\}\), where \(\|e\|=a\), \(\|f\|=b\), and \(|e\cdot f|=ab\cos\phi\). The constant Jacobian of this affine map shows that a uniform point has independent uniform coordinates. For two independent points the coordinate differences \(U,V\) are independent and have common symmetric triangular density \(1-|x|\) on \([-1,1]\). Thus
\[
D^2=uU^2+vV^2+2ab\cos\phi\,UV
\]
(up to an inconsequential choice of sign of \(V\)). Direct integration gives, for nonnegative integers \(j\),
\[
\mathbb E U^{2j}=\frac{2}{(2j+1)(2j+2)},\qquad \mathbb E U^{2j+1}=0.
\]
In particular \(\mathbb E U^2=1/6\), \(\mathbb E U^4=1/15\), and \(\mathbb E U^6=1/28\).

**2. All required moments.** Expand the first three powers of \(D^2\), discard odd monomials in either \(U\) or \(V\), and integrate by independence. With \(s=u+v\), \(p_0=uv\), and \(\eta=\cos^2\phi\), the results are exactly
\[
\begin{aligned}
M_2&=\frac{s}{6},\\
M_4&=\frac{s^2}{15}+\frac{p_0(10\eta-7)}{90},\\
M_6&=\frac{s^3}{28}+\frac{s p_0(56\eta-31)}{420}.
\end{aligned} \tag{1}
\]
For example, the mixed terms in the sixth moment are \(3uv(u+v)\mathbb E U^4\mathbb E V^2=uv(u+v)/30\) and \(3(u+v)(2ab\cos\phi)^2\mathbb E U^4\mathbb E V^2=(u+v)(2ab\cos\phi)^2/30\). The pure terms contribute \((u^3+v^3)/28\), giving (1) without further assumptions.

**3. Exact inverse and feasibility.** From (1), \(S=s\),
\[
X_*=p_0(10\eta-7),\qquad Y_*=p_0(56\eta-31).
\]
Subtracting \(28X_*\) from \(5Y_*\) yields \(41p_0\) exactly. Therefore \(p=p_0=uv>0\) and \(\eta=(X_*+7p)/(10p)\). Since \(u,v>0\), \(s>0\), \(p\le s^2/4\), and positive area means \(\eta<1\). The displayed feasibility conditions follow. Conversely, if the three feasibility conditions hold, the quadratic \(z^2-Sz+p=0\) has two positive real roots \(u,v\), and choosing \(a=\sqrt u\), \(b=\sqrt v\), and \(\phi=\arccos\sqrt\eta\in(0,\pi/2]\) constructs a genuine parallelogram. Its moments coincide with the proposed triple by (1). Any other generating vectors with the same unordered \(u,v\) and \(\phi\) give a congruent parallelogram. This proves necessity, sufficiency, and uniqueness, without genericity conditions or omitted equality cases.

**4. Two-moment obstruction.** Consider two parallelograms with squared side lengths and squared edge-line cosine, respectively,
\[
(u,v,\eta)=\left(1,4,\frac12\right),\qquad
(u',v',\eta')=\left(\frac52,\frac52,\frac{143}{250}\right).
\]
Both have positive area; the first has unequal sides, the second equal sides, so they are not congruent. Yet both have \(s=5\) and \(p_0(10\eta-7)=-8\). Consequently, by (1),
\[
\boxed{(M_2,M_4)=\left(\frac56,\frac{71}{45}\right)}
\]
for both shapes. Their sixth moments differ exactly:
\[
M_6=\frac{121}{28}\quad\text{versus}\quad M'_6=\frac{2543}{560}.
\]
Thus no reconstruction procedure based only on \(M_2,M_4\) can distinguish all nondegenerate parallelograms. Three are sufficient and two are not.

## Verification
The standalone file `verify.py` uses only the Python standard library. Run `python3 verify.py` after extraction into the same directory. It checks the rational reconstruction on 1,200 independent exact rational parameter triples, separately integrates four fully expanded two-variable polynomials with nonzero cross terms, verifies the exact noncongruent two-moment collision, compares four further cases against 600,000 directly simulated pairs, and tests a convex-order consistency inequality at 35,000 pairs of absolute coordinate differences. Its successful marker is `VERIFY_OK exact_parameter_reconstructions=1200 random_configurations= 600000 convex_order_test_points= 35000`. The proof above, not any finite computation, establishes the universal assertion. The script relies on pseudorandom sampling solely for numerical checks; its identities and exact collision use rational arithmetic.

## Relationship to prior work
T. K. Sheng's 1985 article gives a broad integral-geometric treatment of random distances and formulas for integer distance moments in parallelograms. These **forward** formulas are foundational prior work; the new statement is the exact **inverse** classification and minimum initial even-moment count, including an explicit feasibility test and an exact two-moment collision. The complete Sheng article was not available for a decisive full-text comparison, so possible earlier inverse observations remain a priority risk. Zhuang and Pan (2011) derive an explicit distribution for a fixed \(60^\circ\) unit rhombus and its first two distance moments; their report does not address shape reconstruction over all parallelograms. Aharonyan (2012) calculates mean distances by chord-length integration, including a rhombus case, not the three even-moment inverse. Tong and Pan (2016) give a forward distribution algorithm for general polygons, not a finite-measurement identifiability theorem.

Related published mathematical findings recover parallelograms from a mean, second moment, and maximum of **direction-unlabeled projection widths**, and analyze the ratio of **boundary-to-interior fourth-distance moments**. Those observables and implications are different from obtaining a parallelogram from \(M_2,M_4,M_6\) of independent area-uniform point pairs. In particular, formulas for a fourth moment alone cannot recover the unknown three shape parameters; neither referenced result supplies the linear elimination in (1) or the two-moment nonidentifiability example. A separate boundary-arclength antipodal sampling problem also admits a three-moment inversion, but its sampling law, moments and inverse equations differ from the independent interior-point law here. The common broad identifiability theme does not make the present observations interchangeable.

## Limitations
Only genuine Euclidean parallelograms are covered. The classification does not imply uniqueness for general quadrilaterals, arbitrary convex sets, boundary-point sampling, or non-Euclidean distances. No uniform numerical stability is claimed as a shape approaches a segment, and the moment reconstruction is not a statistical finite-sample estimator. The historical claim of priority is necessarily provisional: Sheng's plausible 1985 full text was unavailable through checked channels, and an equivalent reconstruction hidden in an unindexed appendix or older source remains possible. No independent mathematical audit has been performed.

## References
1. T. K. Sheng, *The distance between two random points in plane regions*, Advances in Applied Probability **17** (1985), 748–773. DOI: https://doi.org/10.2307/1427086. Full article not accessible for this comparison; abstract and reference list examined.
2. Y. Zhuang and J. Pan, *Random Distances Associated with Rhombuses*, arXiv:1106.1257v1, first public 2011-06-07, https://arxiv.org/abs/1106.1257. Sections I–IV inspected in full text.
3. N. G. Aharonyan, *Mean Distance Between Two Points in a Domain*, Proceedings of the Yerevan State University: Physical and Mathematical Sciences **46** (2012), 3–8, https://doi.org/10.46991/PYSUA.2012.46.3.003. Sections 2, 5, and 7 inspected in open PDF.
4. F. Tong and J. Pan, *Random Distances Associated with Arbitrary Polygons: An Algorithmic Approach between Two Random Points*, arXiv:1602.03407v1, first public 2016-01-21, https://arxiv.org/abs/1602.03407. Abstract accessible.
5. *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-unlabeled-width-statistics-reconstruct-a-parallelogram-wit--dcfda0360928. Full RESULT.md examined.
6. *Fourth-chord moment amplification and angular phase transition for parallelograms*, published research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-fourth-chord-moment-amplification-and-angular-phase-transition-f--45b0568cfb6e. Full RESULT.md examined.
