# Sharp bounded-variation stability of three-site Shepard interpolation and its mesh–power boundary layer

## Finding
Let \(x_0<x_1<x_2\) be arbitrary real interpolation sites, \(a=x_1-x_0>0\), \(b=x_2-x_1>0\), and \(p>0\). The positive inverse-distance Shepard interpolant of a real triple \(y=(y_0,y_1,y_2)\) is
\[
(S_py)(x)=\frac{\sum_{j=0}^2 |x-x_j|^{-p}y_j}{\sum_{j=0}^2 |x-x_j|^{-p}},\qquad x\in[x_0,x_2]\setminus\{x_0,x_1,x_2\},
\]
with its continuous nodal extensions \((S_py)(x_j)=y_j\). Write \(V_d(y)=|y_1-y_0|+|y_2-y_1|\) and \(\operatorname{Var}(g)=\operatorname{Var}_{[x_0,x_2]}(g)\). Put
\[
r=\min\{a/b,b/a\}\in(0,1],\qquad c=(1+r^{-1})^{1/(p+1)}.
\]
Then the **exact attained operator seminorm** is
\[
\boxed{K_p(a,b)=\sup_{V_d(y)>0}\frac{\operatorname{Var}(S_py)}{V_d(y)}
=1+\frac{2}{1+[1+r(1+c)]^p(1+c^{-p})}.}
\]
When \(a\le b\), the step data \((0,1,1)\) attain equality; when \(b\le a\), the data \((0,0,1)\) attain equality. In particular, every finite positive mesh has \(1<K_p(a,b)<2\). At fixed \(p>0\), equal spacing uniquely **minimizes** this amplification among all positive three-site meshes, while the sharp supremum \(2\) is approached as a neighboring gap collapses.

The exact limiting relationships are
\[
\lim_{p\downarrow0}K_p(a,b)=\frac53,\qquad
\lim_{p\to\infty}K_p(a,b)=1\quad\text{for fixed }a/b>0,
\]
and, for each fixed positive \(p\), \(\lim_{r\downarrow0}K_p(r)=2\). More precisely, if \(p\to\infty\) and the mesh contrast \(r=r_p\in(0,1]\) satisfies \(pr_p\to\tau\in[0,\infty)\), then the **sharp mesh–power transition law** is
\[
\boxed{K_p(r_p)\longrightarrow 1+\frac{2}{1+e^{2\tau}}.}
\]
If \(pr_p\to\infty\), the limit is \(1\). Thus increasing the inverse-distance exponent does not give a variation-stability guarantee uniform over all nonuniform meshes. For example, the exact formula gives \(K_2(1/100,1)>K_1(1/100,1)\), although the reverse inequality holds at equal spacing.

## Assumptions and scope
All sample values are real and all mesh gaps strictly positive; \(p\) is any positive real number, including noninteger exponents. The domain is the closed interval from the first to last site, not extrapolation to the whole real line. The seminorm of constant data is zero, so the quotient is restricted to \(V_d(y)>0\). The formula is invariant under translating, rescaling and reflecting the sites. No assumption of nodewise monotonic data is required for the upper bound; monotonic step data attain it.

## Proof
Translate so the three sites are \(0,a,a+b\). Let \(w_j(x)\) denote the nonnegative normalized Shepard weight at the site \(x_j\). The weights sum identically to one. Every data triple has the exact decomposition
\[
y=y_0(1,1,1)+(y_1-y_0)(0,1,1)+(y_2-y_1)(0,0,1).
\]
Consequently, because variation is subadditive and constants contribute zero, the sharp operator norm is the maximum of the variations of the two step responses \(1-w_0\) and \(w_2\). Both have unit nodal variation, so no other triple can be worse than the larger step response.

On \([0,a]\), the weight \(w_0\) strictly decreases from one to zero, since both ratios \(x/(a-x)\) and \(x/(a+b-x)\) strictly increase. On \((a,a+b)\), it vanishes at both ends and equals
\[
w_0(x)=\frac{1}{1+(x/(x-a))^p+(x/(a+b-x))^p}.
\]
The derivative of the denominator is \(px^{p-1}\) times
\[
-\frac{a}{(x-a)^{p+1}}+\frac{a+b}{(a+b-x)^{p+1}}.
\]
The displayed bracket strictly increases from negative infinity to positive infinity. Its sole zero obeys
\[
\frac{a+b-x_*}{x_*-a}=\left(\frac{a+b}{a}\right)^{1/(p+1)}=:c_a,
\qquad x_*=a+\frac{b}{1+c_a}.
\]
Thus \(w_0\) has exactly one maximum in the opposite cell, namely
\[
m_p(a/b)=\frac{1}{1+[1+(a/b)(1+c_a)]^p(1+c_a^{-p})},\quad c_a=(1+b/a)^{1/(p+1)}.
\]
The response \(1-w_0\) rises from zero to one on the first cell, drops to \(1-m_p(a/b)\), and returns to one on the second, giving variation \(1+2m_p(a/b)\). Reflection gives variation \(1+2m_p(b/a)\) for \(w_2\). This establishes the sharp formula with the larger of those two terms.

To select the larger term, let \(s>0\) and \(c_s=(1+s^{-1})^{1/(p+1)}\). The factor \(1+s(1+c_s)\) is strictly increasing in \(s\), because
\[
\frac{d}{ds}[s(1+c_s)]=1+c_s\left(1-\frac{1}{(p+1)(s+1)}\right)>0.
\]
Also \(c_s^{-p}\) strictly increases in \(s\). Hence \(m_p(s)\) strictly decreases in \(s\); the larger step gain uses \(s=r=\min\{a/b,b/a\}\). This proves sharpness, the identified maximizers, and the unique optimality of equal spacing at fixed total span.

For fixed \(p\), as \(r\downarrow0\) we have \(c_r\sim r^{-1/(p+1)}\), so \(r(1+c_r)\to0\) and \(c_r^{-p}\to0\), proving \(K_p\to2\). For fixed \(r>0\), as \(p\downarrow0\) both powered factors tend to one, giving \(5/3\). As \(p\to\infty\), \(c_r\to1\) and \([1+r(1+c_r)]^p\to\infty\), giving one.

Finally let \(p\to\infty\) and \(pr_p\to\tau\). When \(\tau>0\) is finite, \(r_p\sim\tau/p\), \(c_{r_p}\to1\), \([1+r_p(1+c_{r_p})]^p\to e^{2\tau}\), and \(c_{r_p}^{-p}\to0\). For \(\tau=0\), the bound
\[
p r_p c_{r_p}=p^{1/(p+1)}(pr_p)^{p/(p+1)}(1+r_p)^{1/(p+1)}\longrightarrow0
\]
proves the same conclusion with \(e^{2\tau}=1\). If \(pr_p\to\infty\), the inequality \(1+r_p(1+c_{r_p})\ge1+2r_p\), together with \(\log(1+2r_p)\ge 2r_p/3\) for \(r_p\le1\), makes the amplification tend to one. This proves the stated transition law and all boundary limits.

## Verification
The complete mathematical proof above uses only the weight identity, two step responses, one-dimensional monotonicity, and elementary limits; no computer-based certificate is needed to establish its unrestricted quantifiers. The accompanying standard-library Python script `checker.py` independently searches for the extrema of both step responses by derivative-free golden-section optimization, tests 220 randomly selected positive gap and exponent triples against the exact formula, checks exact equal-gap simplification at \(p=1\), tests mesh-contrast monotonicity and exponent reversal, and checks the finite-parameter approach to the logistic limit. Run with `python3 checker.py`. Numerical tests corroborate, rather than substitute for, the proof.

## Relationship to prior work
The underlying inverse-distance weighting is classical: D. Shepard's 1968 paper explicitly introduces the normalized positive weighting and discusses the exponent's effect and lack of directional shielding. Our sharp result concerns the first nontrivial real **three-site** case and the output **total-variation seminorm**, not positivity, constant reproduction, pointwise approximation error, or uniform-norm contraction. Literature on local partial shape preservation, including Anastassiou–Gal (2001) and Gal (2005), is particularly relevant: these works discuss local monotonicity/shape properties but their accessible abstracts and contents do not establish the specific full-interval sharp three-site BV coefficient or the mesh–power boundary layer. A full comparison with the two univariate Gal monograph chapters was not possible, so historical priority is not guaranteed. Amato–Della Vecchia (2018) studies a different Shepard–Gupta modification and convergence/error properties. Nearby publicly indexed spline and compact multinode Shepard findings have different operators and norm questions; neither supplies the displayed coefficient by implication.

## Limitations
This theorem treats exactly three distinct collinear interpolation sites, no more; the interval's endpoints coincide with the outer nodes. It is not a statement about higher-dimensional scattered data, modified or compactly supported Shepard schemes, or arbitrary many-node interpolation. Although it characterizes the exact gain and a singular parameter boundary layer, it does not give optimal error-approximation rates for smooth input functions. The full text of Gal's directly relevant monograph chapters could not be inspected; an undiscovered equivalent in historical literature remains possible. Independent validation is not claimed.

## References
1. D. Shepard, “A two-dimensional interpolation function for irregularly-spaced data,” Proceedings of ACM National Conference (1968), pp. 517–524, https://doi.org/10.1145/800186.810616 (original inverse-distance construction; also see full-page transcription at https://djvu.online/file/vrZZeUf7Yh5Ao).
2. G. A. Anastassiou and S. G. Gal, “Partial shape preserving approximations by bivariate Shepard operators,” Computers & Mathematics with Applications 42 (2001), 47–56, https://doi.org/10.1016/S0898-1221(01)00129-8.
3. S. G. Gal, *Global Smoothness and Shape Preserving Interpolation by Classical Operators*, Birkhäuser, 2005, https://doi.org/10.1007/b137115; especially “Partial Shape Preservation, Univariate Case,” https://doi.org/10.1007/0-8176-4401-6_2 (full chapter unavailable for comparison).
4. U. Amato and B. Della Vecchia, “On Shepard–Gupta-type operators,” Journal of Inequalities and Applications (2018), https://doi.org/10.1186/s13660-018-1823-7 (later background on a different variant).
