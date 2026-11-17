# Sharp two-input graph-variation stability of the centered maximal operator on stars

## Finding

Let \(S_m=K_{1,m}\) be the unweighted star with center \(o\), leaves \(v_1,\ldots,v_m\), and integer \(m\ge1\). For real vertex functions define the graph-total-variation seminorm
\[
\operatorname{TV}(h)=\sum_{i=1}^m|h(v_i)-h(o)|.
\]
For nonnegative vertex functions, the centered Hardy–Littlewood maximal operator is
\[
(Mh)(v)=\max_{r\ge0}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}h(w).
\]
Its *two-input perturbation constant* is the least \(C\) such that \(\operatorname{TV}(Mf-Mg)\le C\operatorname{TV}(f-g)\) for every nonnegative pair. The exact answer is
\[
\boxed{C_m=\begin{cases}\tfrac12,&m=1,\\[2pt]\tfrac{2m}{m+1},&m\ge2.\end{cases}}
\]
Every value is attained by nonnegative inputs with nonzero input variation. In particular, for \(m\ge2\) the constants increase strictly from \(4/3\) toward \(2\). Although each nonnegative signal separately obeys the known sharp single-input bound \(\operatorname{TV}(Mf)\le m\operatorname{TV}(f)/(m+1)\), differences between two outputs may have strictly more variation than the difference between their inputs.

The *nonnegative-input condition is essential* for the classical absolute-value maximal operator \(M^{\mathrm{abs}}h=M|h|\). On the unrestricted real signal space, no finite two-input variation constant exists, for every \(m\ge1\). Thus the finite sharp stability formula and the signed-data obstruction describe two sides of one stability phenomenon.

## Assumptions and scope

The graph is finite, simple and unweighted. The vertex measure is counting measure, and the balls use the ordinary graph distance; radii \(0,1,2\) give all distinct balls for \(m\ge2\). The input pair \(f,g\) is nonnegative at every vertex in the finite-constant assertion. No normalization of their common offsets is imposed. The output is measured in graph total variation, not vertex \(\ell_1\) variation. The parameter \(m=1\) is treated separately. For signed inputs the operator includes \(|h|\) *inside* the ball averages.

Because averaging of nonnegative functions is translation covariant, \(M(h+c)=Mh+c\) wherever \(h\) and \(h+c\) are both nonnegative. Thus a zero-seminorm input difference (a constant difference) always produces a zero-seminorm output difference on the stated domain.

## Proof

**1. Exact edge-coordinate map.** Extend the maximum-of-ball-averages expression formally to all real functions without taking absolute values. It is translation covariant and agrees with \(M\) on nonnegative functions. Write \(b=h(o)\), \(x_i=h(v_i)-b\), and
\[
\mu=\frac{1}{m+1}\sum_{j=1}^m x_j.
\]
The maximal values at the center and at leaf \(i\) are respectively
\[
Mh(o)=b+\max\{0,\mu\},\qquad Mh(v_i)=b+\max\{x_i,x_i/2,\mu\}.
\]
Consequently, the output edge increments are the components of the continuous piecewise-linear map
\[
F_i(x)=\max\{x_i,x_i/2,\mu\}-\max\{0,\mu\}.
\]
For two inputs, \(\operatorname{TV}(h-k)=\|x(h)-x(k)\|_1\) and \(\operatorname{TV}(Mh-Mk)=\|F(x(h))-F(x(k))\|_1\). Any real vectors of edge increments can be represented by nonnegative vertex signals after adding a sufficiently large constant, without changing either quotient. Thus the required constant is the global \(\ell_1\)-Lipschitz modulus of \(F\) on \(\mathbb R^m\).

**2. Upper bound on every affine cell.** Put \(a=1/(m+1)\). At a differentiability point with \(\mu>0\), the center selects \(\mu\). Each leaf selects either \(x_i\) or \(\mu\); the term \(x_i/2\) cannot win. Let \(s\) be the number of self-selected leaves. For a column indexed by a self-selected leaf, the absolute Jacobian column sum of \(F\) is \(1+(s-2)a\); for a column not self-selected it is \(sa\). As \(0\le s\le m\), each is at most \(2m/(m+1)\) for \(m\ge2\).

At a differentiability point with \(\mu<0\), the center selects \(0\). Every positive leaf selects \(x_i\); a negative leaf selects either \(x_i/2\) or \(\mu\). Let \(u\) denote the number selecting \(\mu\). Necessarily \(u\le m-1\) when \(m\ge2\): if all leaves selected \(\mu<0\), then \(x_i/2<\mu\) for every \(i\), which on summing gives \((m+1)\mu/2<m\mu\), impossible for negative \(\mu\) and \(m>1\). The absolute Jacobian column sums are, according to the input leaf's active type, exactly \(1+ua\), \(1/2+ua\), or \(ua\). Every one is bounded by \(1+(m-1)/(m+1)=2m/(m+1)\).

The finitely many affine cells cover \(\mathbb R^m\), their formulas agree on boundaries, and the map is continuous. Splitting a generic line segment at its finitely many boundary crossings and applying the induced matrix \(\ell_1\) bound on each subsegment proves the global inequality. Arbitrary line segments follow by approximation and continuity. This establishes the upper bound for all nonnegative pairs.

**3. Sharpness for \(m\ge2\).** Take an input \(f\) with center value \(3\), one leaf value \(3+(m-1)/2\), and each other leaf value \(2\). Its relative global mean is \(\mu=-(m-1)/(2(m+1))\). Thus the center selects its own value, the distinguished leaf selects itself, and all other leaves select the global mean (strictly). Define \(g\) by adding \(\varepsilon\) to the distinguished leaf, with \(0<\varepsilon<(m-1)/2\), leaving every other value fixed. No maximizing branch changes. Exactly one output leaf changes by \(\varepsilon\), all other output leaves change by \(\varepsilon/(m+1)\), and the output center is unchanged. Hence
\[
\frac{\operatorname{TV}(Mg-Mf)}{\operatorname{TV}(g-f)}
=1+\frac{m-1}{m+1}=\frac{2m}{m+1}.
\]
Both \(f,g\) are strictly nonnegative, so this proves attainment for the standard maximal operator.

**4. The two-vertex case.** If \(m=1\), direct evaluation gives \(F_1(x)=x/2\) for both signs of \(x\). Hence every nontrivial nonnegative pair attains the exact constant \(1/2\).

**5. Signed-input obstruction.** For arbitrary real inputs the standard maximal function averages absolute values. Let \(f(o)=1\) and \(f(v_i)=-1\) for all leaves, so \(M^{\mathrm{abs}}f\) is the constant function \(1\). For \(0<\varepsilon<1\), let \(g(o)=2\), \(g(v_1)=\varepsilon\), and \(g(v_i)=0\) for \(i\ge2\). Then \(\operatorname{TV}(g-f)=\varepsilon\), while the maximal values of \(g\) are \(2\) at the center, \(1+\varepsilon/2\) at the first leaf, and \(1\) at the others. Consequently
\[
\frac{\operatorname{TV}(M^{\mathrm{abs}}g-M^{\mathrm{abs}}f)}{\operatorname{TV}(g-f)}
=\frac{m-\varepsilon/2}{\varepsilon}\longrightarrow\infty.
\]
Thus no finite signed-input two-input seminorm bound exists.

## Verification

The accompanying `check_star_maximal.py` is a standalone Python 3 program using only the standard library and exact rational arithmetic. Run `python check_star_maximal.py`. It checks explicit equality witnesses through \(m=64\), small integer-grid perturbations, pseudorandom exact-rational input pairs, active-branch Jacobian column budgets, and signed-input divergence examples. Finite computations are corroborative; the bounds for all \(m\) and all signals follow from the proof above, not finite sampling.

## Relationship to prior work

Soria and Tradacete (2014 preprint) establish sharp vertex \(\ell_p\) estimates and extremal graph families for finite-graph maximal functions; their norm is not the two-input graph-variation modulus here. González-Riquelme and Madrid (2020 preprint) establish the *single-input* star \(p=1\) variation constant \(m/(m+1)\) and qualitative continuity with restrictions for general signed inputs. The factor \(2m/(m+1)\) here measures the differential amplification of *differences of outputs*, which the cited single-input inequality does not imply. Their companion 2020 paper handles other \(\ell_p\) and single-input \(p=2\) norms, while González-Riquelme–Kovač–Madrid (2026) address single-input graph variation on other graph families. The signed obstruction clarifies the restriction needed to obtain a finite seminorm modulus, consistent with the continuity issue noted in the 2020 study.

## Limitations

The finite sharp constant is asserted only for nonnegative real vertex signals on unweighted stars. For signed data it is infinite, as separately proved. Weighted stars, uncentered maximal operators, fractional maximal operators, and larger graph families are not covered. The equality witness is not claimed to classify every maximizing pair. The literature comparison is not a guarantee of absolute historical priority; related nonlinear-maximal continuity results may contain implicit special cases.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204v1, first publicly posted 2014-10-22, https://arxiv.org/abs/1410.6204 .
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, first posted 2020-05-06, https://arxiv.org/abs/2005.03146 .
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630v1, first posted 2020-11-05, https://arxiv.org/abs/2011.02630 .
4. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first posted 2026-03-12, https://arxiv.org/abs/2603.12462 .
5. F. Liu and Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collectanea Mathematica 72 (2021), 333–349, DOI:10.1007/s13348-020-00290-6 (abstract/bibliographic record considered).
