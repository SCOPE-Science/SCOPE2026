# Variance-only rare-acuteness law for slender product measures

## Finding
Let \(X\) have a nonnegative, bounded Lipschitz density \(f\) on a fixed interval \([0,L]\), with \(L>0\) and \(\int_0^L f=1\). Independently let \(Y\) have any probability law \(\mu\) supported on a bounded real interval and with variance \(v=\operatorname{Var}(Y)>0\). Draw three independent copies and form the three Euclidean vertices \((X_i,\varepsilon Y_i)\). Then their strict-acuteness probability satisfies
\[
\boxed{\Pr(\text{acute})=12v\!\left(\int_0^L f(x)^3\,dx\right)\varepsilon^2\log(1/\varepsilon)+O_{f,\mu,L}(\varepsilon^2).}
\]
The law of \(Y\) may be singular or purely atomic; at fixed variance its other moments and its shape do not enter the leading coefficient. At fixed support length \(L\) and transverse variance \(v\), the sharp minimal coefficient is \(12v/L^2\), attained exactly for uniform horizontal sampling.

There is also an explicit **marked total-variation limit**. Order the points by horizontal coordinate and denote the successive horizontal gaps by \(s,t>0\). Let \(J=\mathrm{L}\) when \(s<t\), and \(J=\mathrm{R}\) when \(t<s\); put \(T=\max(s,t)\), \(\Theta_\varepsilon=\log T/\log\varepsilon\), and \(Z_\varepsilon=st/\varepsilon^2\). Write \(x=X_{(2)}\), \(A=|Y_{(2)}-Y_{(1)}|\), \(B=|Y_{(2)}-Y_{(3)}|\), and
\[
\ell_{\mathrm L}=A(B-A)_+,\qquad \ell_{\mathrm R}=B(A-B)_+,
\qquad (u)_+=\max(u,0).
\]
Conditioned on an acute triangle, the joint law of \((J,x,Y_{(1)},Y_{(2)},Y_{(3)},Z_\varepsilon,\Theta_\varepsilon)\) converges in **total variation** to the probability measure with density, relative to counting measure in \(J\), Lebesgue measure in \((x,z,\theta)\), and \(\mu^{\otimes3}\) in the ordinates,
\[
\boxed{
\frac{f(x)^3}{2v\int_0^L f(u)^3\,du}\,
\mathbf1_{0<\theta<1}\,
\mathbf1_{(y_2-y_1)(y_2-y_3)>0}\,
\mathbf1_{\ell_J(y)<z<AB}.}
\]
In particular, the logarithmic scale \(\Theta_\varepsilon\) tends to a uniform \((0,1)\) variable independent of all other marks; the two smaller-gap placements have equal limiting probability; and the middle horizontal location has density \(f(x)^3/\int f^3\). The signed height-order/overshoot marks retain an explicit nontrivial distribution.

## Assumptions and scope
All samples are independent and identically distributed, and each \(X_i\) is independent of each \(Y_i\). A bounded Lipschitz density is understood on \([0,L]\); its extension by zero outside \([0,L]\) is of bounded variation, so endpoints need not have vanishing density. Bounded \(Y\) need not have a density, and ties between ordinates are permitted. Horizontal ties have probability zero. The strict acute-angle condition excludes right and degenerate triangles. Almost surely there are no right angles: conditional on any ordinates, their zero-dot-product horizontal configurations form sets of planar Lebesgue measure zero. The range is \(\varepsilon\downarrow0\) at fixed \(f,\mu,L\). Neither the error constant nor convergence is uniform across arbitrary classes of such laws.

## Proof
**1. Acute-angle inequalities.** Order horizontally, writing the points as \((x,\varepsilon y_1)\), \((x+s,\varepsilon y_2)\), and \((x+s+t,\varepsilon y_3)\), with \(s,t>0\), and put \(\alpha=y_2-y_1\), \(\beta=y_3-y_2\). The ordered-coordinate density is \(6f(x)f(x+s)f(x+s+t)\,dx\,ds\,dt\,\mu^{\otimes3}(d\boldsymbol y)\) on the support. Strict acuteness is equivalent to the three inequalities
\[
 s(s+t)+\varepsilon^2\alpha(\alpha+\beta)>0,\quad
 -st-\varepsilon^2\alpha\beta>0,\quad
 t(s+t)+\varepsilon^2\beta(\alpha+\beta)>0.
\]
Consequently \(\alpha\beta<0\): \(y_2\) must be a **strict** ordinate extremum. Then \(A=|\alpha|\), \(B=|\beta|\), and the middle-angle test reads \(0<st/\varepsilon^2<AB\). Let \(D\) bound all ordinate differences.

**2. One logarithmic boundary layer.** First restrict to \(s<t\). For \(0<t\le D\varepsilon\), the domain \(0<s<t\) has area \(O(\varepsilon^2)\), so its probability is \(O(\varepsilon^2)\). For \(t>D\varepsilon\), put \(z=st/\varepsilon^2\). Then \(0<z<AB\le D^2\), \(s=\varepsilon^2z/t<t\), and \(ds=\varepsilon^2 dz/t\). The rightmost-angle inequality is automatically positive, and the leftmost-angle inequality is
\[
 z(1+\varepsilon^2z/t^2)>A(B-A).
\]
For \(A\le B\) this bounds \(z\) below by a positive quantity; for \(A>B\) the lower bound is zero. Uniformly for \(t>D\varepsilon\), the difference between the admissible \(z\)-interval length and \(A\min(A,B)\) is at most \(C\varepsilon^2/t^2\), where \(C\) depends only on the ordinate bound. Indeed, the strictly increasing map \(z\mapsto z+\varepsilon^2z^2/t^2\) differs from \(z\) by at most \(D^4\varepsilon^2/t^2\) on \([0,D^2]\), so its inverse threshold differs by no more than that amount. This estimate also covers atoms and equalities among the ordinates.

**3. Integrate the horizontal location and the logarithm.** Let \(I_3=\int_0^L f^3\). For any \(s,t\ge0\), extending \(f\) by zero outside its support gives
\[
\left|\int_{\mathbb R}f(x)f(x+s)f(x+s+t)\,dx-I_3\right|
\le C_f(s+t)
\]
when \(s+t\le L\), by the \(L^1\)-translation bound for bounded-variation functions; for larger shifts we use a fixed bound. Thus the leading contribution for \(s<t\), after integrating ordinates, equals
\[
6\varepsilon^2 I_3\int_{D\varepsilon}^{L}\frac{dt}{t}\,
\mathbb E[\mathbf1_{\{Y_2\text{ strict extreme}\}}A\min(A,B)]
+O(\varepsilon^2).
\]
The replacement of the horizontal density costs at most \(C\varepsilon^2\int_0^L(1+\varepsilon^2/t^2)\,dt\) after excluding \(t\le D\varepsilon\), and the threshold replacement costs at most \(C\varepsilon^4\int_{D\varepsilon}^L t^{-3}\,dt=O(\varepsilon^2)\). If necessary, replace \(D\) by a positive constant to handle very small supports, then use \(\varepsilon\) sufficiently small. The logarithmic integral is \(\log(1/\varepsilon)+O_{L,D}(1)\). Reversing the ordered endpoints gives an equal contribution for \(t<s\).

**4. A distribution-free vertical identity.** For any deterministic triple of heights with sorted values \(a\le b\le c\), summing \(\mathbf1_{\{y_2\text{ strict extreme}\}}|y_2-y_1|\min(|y_2-y_1|,|y_2-y_3|)\) over the six permutations gives
\[
 2\bigl((b-a)^2+(c-b)^2+(b-a)(c-b)\bigr)
 =(a-b)^2+(a-c)^2+(b-c)^2.
\]
This identity remains true for repeated heights. By exchangeability, the expectation of the weight is one-sixth of the expected sum of squared pairwise differences, namely \(v\). Therefore each branch contributes \(6vI_3\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2)\), proving the scalar law. Jensen's inequality gives \(I_3\ge L^{-2}\), with equality only for \(f=1/L\) almost everywhere, proving the sharp sampling claim.

**5. Marked total variation.** The horizontal mark in the finding is the middle abscissa \(X_{(2)}\), which differs from the leftmost abscissa used in the preceding coordinate integral by the smaller gap. This difference tends to zero on the limiting logarithmic scales; the bounded-variation translation estimate also justifies replacing one by the other in total variation. In the \(s<t\) branch put \(T=t\), and in the \(t<s\) branch put \(T=s\). On both branches define \(z=st/\varepsilon^2\) and \(\theta=\log T/\log\varepsilon\). The Jacobian magnitude in \((s,t)\mapsto(z,\theta)\) is \(\varepsilon^2\log(1/\varepsilon)\). For every fixed \(0<\theta<1\) and \(z>0\), \(T=\varepsilon^\theta\to0\), the other gap equals \(\varepsilon^{2-\theta}z\to0\), and the three angle tests tend pointwise (in the base measure) to \(\mathbf1_{y_2\text{ strict extreme}}\mathbf1_{\ell_J<z<AB}\). The rightmost/leftmost conditions select respectively the lower thresholds \(\ell_{\mathrm L}\) and \(\ell_{\mathrm R}\). For fixed \(\theta\notin[0,1]\) and \(z>0\), eventually either \(T\) exceeds the fixed horizontal support or the other gap is not the smaller gap; hence the limiting density vanishes. The Jacobian densities, divided by \(\varepsilon^2\log(1/\varepsilon)\), therefore converge almost everywhere on the common measure space \(\{\mathrm L,\mathrm R\}\times[0,L]\times\mathbb R^3\times\mathbb R_+\times\mathbb R\). Their total masses converge to \(12vI_3\) by Steps 2–4, and the proposed limiting density has that same mass before division by \(12vI_3\): the two \(z\)-interval lengths each integrate to \(v\), each with horizontal factor \(6I_3\). Scheffé's lemma implies \(L^1\) convergence of the unnormalized densities; normalization gives the asserted **total-variation** conditional convergence. The density factors in \(\theta\), making \(\theta\) uniform and independent. The exchange \(y_1\leftrightarrow y_3\) swaps the \(J\)-branches, proving the fair branch marginal. Integrating the other marks yields the \(f^3/I_3\) horizontal marginal.

## Verification
The accompanying standalone `check_product_acuteness.py` verifies the exact six-permutation identity for generic heights and samples with ties; evaluates an exact finite-\(\varepsilon\) formula in a Bernoulli-height model at four thinning scales; and independently simulates all three angle inequalities for three distinct height laws of equal variance, with both uniform and nonuniform horizontal densities. It concludes `PRODUCT_ACUTENESS_CHECKS_OK`. The exact Bernoulli calculation gives a ratio tending toward \(12\), while finite-width simulations exhibit the expected logarithmically slow convergence. These are diagnostic computations and do not establish a limit or substitute for the analytic proof.

## Relationship to prior work
Langford (1969) gives the classical rectangular uniform-point obtusity problem; the scalar uniform-rectangle special case is not claimed as new. A published general convex-body thin-direction theorem determines the leading probability for **area-uniform points within a convex body**, through the fifth moment of its vertical chord lengths; its rectangular specialization is the same scalar special case. An independently published marked-rectangle theorem identifies a conditional weak limit for **uniform rectangle heights**. Another published study determines the full acute-probability profile for **planar Gaussian vertices** under covariance anisotropy. These statements do not imply the present arbitrary independent product-density theorem: the vertical law may have atoms, its leading coefficient depends only on variance, its horizontal density enters cubically, and the full joint marked limit is in total variation. The horizontal-density optimization is likewise a consequence of the new coefficient rather than a restatement of the uniform-domain result. The closest sources and overlaps are explicitly documented; no assertion of exhaustive historical priority is made.

## Limitations
The density \(f\) must be bounded and Lipschitz on a compact interval, and the transverse law must have bounded support and positive variance. Without additional tail control, the stated \(O(\varepsilon^2)\) error and total-variation result are not asserted for unbounded Gaussian heights. Atomic transverse laws are allowed, but \(X\) remains continuous. The population law and asymptotic sampling optimum are exact-model statements; no finite-sample statistical inference bound is proved. Related classical papers may contain unindexed variants and historical priority requires further checking. Independent mathematical audit has not been performed.

## References
1. S. R. Finch, *Pins, Stakes, Anchors and Gaussian Triangles*, arXiv:1410.6742, first posted 2014-10-24. https://arxiv.org/abs/1410.6742
2. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first posted 2015-01-09. https://arxiv.org/abs/1501.03053
3. E. Langford, *The probability that a random triangle is obtuse*, Biometrika 56 (1969), 689–690. https://doi.org/10.1093/biomet/56.3.689
4. *Fifth-chord-moment law for acute triangles in thin convex bodies*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-fifth-chord-moment-law-for-acute-triangles-in-thin-convex-bodies--6f181af2eba0
5. *A marked logarithmic scaling law for acute triangles in collapsing rectangles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-marked-logarithmic-scaling-law-for-acute-triangles-in-collapsi--5b2cafd49dff
6. *Exact anisotropy law for acute Gaussian triangles*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-anisotropy-law-for-acute-gaussian-triangles--91f2e9bf092d
