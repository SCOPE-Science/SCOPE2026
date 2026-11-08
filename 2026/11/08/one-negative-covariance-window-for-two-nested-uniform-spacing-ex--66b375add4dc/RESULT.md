# One negative-covariance window for two nested uniform-spacing exceedance counts

## Finding

Take \(n\ge2\) independent uniform points on a circle of circumference one. Their \(n\) cyclic spacings, in cyclic order, are \((G_1,\ldots,G_n)\sim\operatorname{Dirichlet}(1,\ldots,1)\). For every threshold \(u\in(0,1)\), define the number of long spacings by
\[
N_n(u)=\sum_{i=1}^{n}\mathbf1_{\{G_i>u\}}.
\]
For fixed \(0<a\le b<1\) with \(a+b<1\), put \(s=1-a\) and \(t=(1-a-b)/(1-b)\). Then \(0<t<s<1\) and
\[
\operatorname{Cov}(N_n(a),N_n(b))
=n(1-b)^{n-1}\big[1+(n-1)t^{n-1}-ns^{n-1}\big].
\]
**Sign-window theorem.** As integer \(n\) varies over \(2,3,\ldots\), the values with strictly negative covariance form either the empty set or one contiguous finite interval of integers. The same conclusion holds over real exponents \(x=n-1>0\): the negative-sign region is a single bounded open interval or empty. In particular, there are at most two sign changes; equality can occur only at at most two boundary exponents, except that a tangency can produce one zero with no negative region.

Both sign changes can occur. For \(a=3/20\) and \(b=1/4\), the covariance is strictly positive for \(2\le n\le5\), strictly negative for \(6\le n\le13\), and strictly positive for every \(n\ge14\). There are no zero cases for integer \(n\) in this example.

## Assumptions and scope

Spacings are the positive clockwise differences between consecutive points, including the wrap-around gap. All points have an independent uniform distribution on the circle; the circular-spacings vector is uniform on the simplex \(\{g_i\ge0:\sum_i g_i=1\}\). The thresholds are fixed as \(n\) changes; all covariance statements are exact finite-sample statements. The assumption \(a+b<1\) ensures that two distinct spacings can simultaneously exceed the two thresholds and gives the nondegenerate window formula. We do not claim the same window classification for nonuniform sampling or other Dirichlet parameters.

## Proof

**Step 1: exact two-threshold covariance.** Simplex translation gives, for nonnegative \(u_i\) with \(\sum u_i<1\),
\[
\Pr\big\{G_1>u_1,\ldots,G_k>u_k\big\}
=\big(1-\sum_{i=1}^{k}u_i\big)^{n-1}.
\]
Consequently \(\mathbb E[N_n(u)]=n(1-u)^{n-1}\). In the mixed product \(N_n(a)N_n(b)\), the \(n\) terms with matching index have probability \((1-b)^{n-1}\), since \(a\le b\); the \(n(n-1)\) distinct-index terms have probability \((1-a-b)^{n-1}\). Therefore
\[
\operatorname{Cov}(N_n(a),N_n(b))
=n(1-b)^{n-1}+n(n-1)(1-a-b)^{n-1}
-n^2(1-a)^{n-1}(1-b)^{n-1},
\]
which is the asserted formula after factoring.

**Step 2: strict logarithmic concavity of the sign parameter.** Set \(x=n-1>0\), \(\alpha=-\log s>0\), and \(\delta=\log(s/t)>0\). The normalized bracket factors as
\[
1+xt^x-(x+1)s^x=(1-s^x)(1-g(x)),
\qquad
 g(x)=\frac{x(s^x-t^x)}{1-s^x}
 =\frac{x(1-e^{-\delta x})}{e^{\alpha x}-1}.
\]
The prefactor \(1-s^x\) is strictly positive, so negative covariance is equivalent to \(g(x)>1\). Direct differentiation yields
\[
\frac{d^2}{dx^2}\log g(x)
=-\frac1{x^2}
-\frac{\delta^2 e^{\delta x}}{(e^{\delta x}-1)^2}
+\frac{\alpha^2e^{\alpha x}}{(e^{\alpha x}-1)^2}<0.
\]
Indeed \(\alpha^2e^{\alpha x}/(e^{\alpha x}-1)^2=\alpha^2/[4\sinh^2(\alpha x/2)]<1/x^2\) because \(\sinh y>y\) for \(y>0\). Thus \(\log g\) is strictly concave. Furthermore \(g(x)\sim(\delta/\alpha)x\to0\) as \(x\downarrow0\), and \(g(x)\sim xe^{-\alpha x}\to0\) as \(x\to\infty\). Therefore the strict superlevel set \(\{x>0:g(x)>1\}\) is one bounded open interval, possibly empty. Strict concavity also implies the level \(g(x)=1\) has at most two solutions (one if its maximum is exactly one). Intersecting the interval with integer \(x=n-1\) proves the discrete classification.

**Step 3: a certified pair of sign reversals.** For \(a=3/20\), \(b=1/4\), the parameters become \(s=17/20\) and \(t=4/5\). The four exact normalized bracket values \(F_n=1+(n-1)(4/5)^{n-1}-n(17/20)^{n-1}\) are
\[
\begin{aligned}
F_5&=4539/160000>0,\\
F_6&=-38131/1600000<0,\\
F_{13}&=-100389363459021/4096000000000000<0,\\
F_{14}&=180270269513333/8192000000000000>0.
\end{aligned}
\]
The superlevel interval in Step 2 contains every integer exponent corresponding to \(6\le n\le13\) and excludes all integers with \(n\le5\) or \(n\ge14\). This proves the sharp complete witness sign diagram, including the absence of integer zeros.

## Verification

The accompanying self-contained standard-library Python script `covariance_check.py` computes the exact rational formula, obtains the same covariance independently from direct simplex interval/polygon integration for \(n=2,3\), verifies the four exact rational transition certificates, checks the witness signs for \(2\le n\le120\), and runs supplementary numerical diagnostics for the strict hyperbolic-sine inequality. The script prints `PASS 627 exact assertions or diagnostic inequalities` when successful. The all-\(n\) theorem rests on the analytic proof above, not on bounded enumeration or the diagnostic samples.

Reproduce with `python3 covariance_check.py` from a directory containing the file; no third-party package is needed.

## Relationship to prior work

Holst's 1980 work on uniformly broken sticks provides exact single-threshold spacing-count and order-statistic tools. Bairamov, Berred, and Stepanov's study of ordered uniform spacings explicitly gives the joint translation identity for several individual gaps, from which the first displayed covariance identity can be recovered. Schlemm's 2014 moment approach studies the maximum circular gap and its limit law. The contribution here is not a new simplex joint probability or a new formula for one marginal count: it is the global strictly-concave sample-size sign classification for **two nested fixed-threshold gap counts**, with a certified two-reversal instance. These inspected primary results do not state that classification; an implicit consequence elsewhere in the broader spacings literature remains a priority risk.

## Limitations

The strictly negative-covariance set may be empty, and the theorem does not locate its real-valued endpoints in elementary closed form for arbitrary thresholds. The sign-window statement does not imply independence at its zero-covariance boundaries. The exact rational example is a finite-family witness; its classification for every larger integer is provided by the analytic sign-window theorem. Literature inspection does not constitute independent historical-priority certification.

## References

- L. Holst (1980), *On the Lengths of the Pieces of a Stick Broken at Random*, Journal of Applied Probability 17, 623–634. DOI: https://doi.org/10.2307/3212956. Accessible full text: https://imprs-gw-lectures.aei.mpg.de/wp-content/uploads/2023/12/Holst_StickBreakingDistributions.pdf.
- I. Bairamov, A. Berred and A. Stepanov (online 10 April 2008), *Limit results for ordered uniform spacings*, Statistical Papers 51 (2010), 227–240. DOI: https://doi.org/10.1007/s00362-008-0134-3. Accessible full text: https://dm.ieu.edu.tr/Ism/BaiBerredStep_StatisticalPapers.pdf.
- E. Schlemm (first posted 23 May 2014), *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114v1. https://arxiv.org/abs/1405.6114.
