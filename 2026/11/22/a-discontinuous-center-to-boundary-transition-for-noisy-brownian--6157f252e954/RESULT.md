# A discontinuous center-to-boundary transition for noisy Brownian-bridge window averages

## Finding
Let \(B\) be a standard Brownian bridge on \([0,1]\). One sensor returns the uniform average of \(B\) on an interval of fixed width \(0<h<1\), contaminated by independent centered Gaussian noise of variance \(\eta>0\):
\[
Y_{t,h}=h^{-1}\int_t^{t+h} B(u)\,du+\epsilon,
\qquad 0\le t\le1-h,\qquad \epsilon\sim N(0,\eta).
\]
Minimize the integrated posterior path variance
\[
R_{h,\eta}(t)=\int_0^1\operatorname{Var}(B(s)\mid Y_{t,h})\,ds.
\]
**Every global minimizer is one of precisely three candidate starts**, the centered start \((1-h)/2\), the left endpoint start \(0\), or the right endpoint start \(1-h\); no other start is optimal. There is an exact critical width
\[
h_c=\frac{35-\sqrt{105}}{28}=0.8840374726443\ldots.
\]
For \(0<h\le h_c\), the centered start is the unique optimum for every \(\eta>0\). For \(h_c<h<1\), put
\[
\eta_c(h)=\frac{h(35h-14h^2-20)}{60(1+2h-2h^2)}.
\]
If \(0<\eta<\eta_c(h)\), **exactly the two boundary-attached windows** \(t=0\) and \(t=1-h\) minimize risk. If \(\eta>\eta_c(h)\), **only the centered window** minimizes risk. At \(\eta=\eta_c(h)\), all three and no other windows tie. Consequently the optimal start can switch discontinuously, without an intermediate optimal offset.

For example, at \(h=19/20\) the exact threshold is \(\eta_c=779/87600\). Writing \(G(t)=1/6-R(t)\) for posterior-variance reduction, at noise \(\eta=1/200\) the boundary-minus-center gain is \(1023/42780800>0\); at noise \(\eta=1/50\) it is \(-2919/57137600<0\).

## Assumptions and scope
The prior is the **zero-endpoint** Gaussian bridge with covariance \(k(s,u)=\min(s,u)-su\) and unit diffusion scale. The interval is allowed to touch either endpoint; the width \(h\) is fixed in advance and strictly between zero and one. The noise is independent of the process, centered Gaussian and has variance \(\eta>0\) **for the window average**, with no additional scaling by exposure width. The criterion is the unweighted integral of posterior variance over the whole unit time interval, not variance of an integral, pointwise worst-case variance, or a mutual-information design.

Reflection of the bridge implies \(R(t)=R(1-h-t)\), but reflection symmetry alone does not prove that the center or boundaries must win. That exclusion of asymmetric interior maxima is part of the finding.

## Proof
**1. Gaussian reduction.** For \(C_{t,h}(s)=h^{-1}\int_t^{t+h} k(s,u)\,du\) and \(V_{t,h}=\operatorname{Var}(h^{-1}\int_t^{t+h}B(u)\,du)\), Gaussian conditioning gives
\[
R_{h,\eta}(t)=\frac16-\frac{\int_0^1 C_{t,h}(s)^2\,ds}{V_{t,h}+\eta}.
\]
The denominator is strictly positive because \(\eta>0\). For \(s\le t\), the covariance is \(C_{t,h}(s)=s(1-t-h/2)\); for \(s\ge t+h\), it is \(C_{t,h}(s)=(t+h/2)(1-s)\). For \(t<s<t+h\), integrating the two branches of \(\min(s,u)\) gives
\[
C_{t,h}(s)=\frac{(1-s)(s^2-t^2)/2+s[(t+h-s)-((t+h)^2-s^2)/2]}{h}.
\]
Squaring these three polynomials and integrating their respective intervals yields the formulas below; independently, \(V_{t,h}=t+h/3-(t+h/2)^2\).

**2. Reduce location to a single squared displacement.** Write \(y=t-(1-h)/2\) and \(z=y^2\), so \(0\le z\le Z_h=(1-h)^2/4\). Exact integration yields
\[
I_h(z):=\int_0^1 C_{t,h}(s)^2\,ds
=\frac{5-5h^2+2h^3}{240}+\frac{h^2-2}{12}z+\frac{z^2}{3},
\]
\[
V_h(z)=\frac{3-2h}{12}-z.
\]
Thus minimizing risk is equivalent to maximizing \(F(z)=I_h(z)/(M-z)\), where \(M=\eta+(3-2h)/12\). Throughout the permitted interval \(M-z=\eta+V_h(z)>0\).

**3. Exclude all nontrivial interior maxima.** Set \(H(z)=I_h'(z)(M-z)+I_h(z)\). Then
\[
F'(z)=\frac{H(z)}{(M-z)^2},\qquad
H'(z)=I_h''(z)(M-z)=\frac23(M-z)>0.
\]
Therefore \(H\) is strictly increasing. A change of sign of \(F'\), if one occurs, can only be negative-to-positive; any interior critical point is a strict minimum. Hence the only global maximizing squared displacements are \(z=0\) and \(z=Z_h\), and, if they tie, all \(0<z<Z_h\) are strictly inferior. In terms of actual windows, these are exactly the center and the two reflected boundary windows.

**4. Exact global phase test.** Direct expansion of the endpoint comparison gives
\[
I_h(Z_h)M-I_h(0)(M-Z_h)
=\frac{(1-h)^2}{2880}
\left[h(35h-14h^2-20)-60\eta(1+2h-2h^2)\right].
\]
Since \(M(M-Z_h)>0\), the sign of this expression is the sign of \(F(Z_h)-F(0)\). The quadratic \(35h-14h^2-20\) has exactly one zero in \((0,1)\), namely \(h_c\), and is positive exactly when \(h>h_c\). Also \(1+2h-2h^2>0\) throughout \((0,1)\). The asserted strict regimes and triple tie follow. Both endpoint designs have identical risk by reflection. The indicated rational example follows by substitution.

## Verification
The standalone \(`verify.py`\) reconstructs the observation covariance by three independent integration pieces, confirms the formulas for \(I_h\), \(V_h\), \(H'\), and the global endpoint-comparison polynomial symbolically, checks the exact critical width and critical noise, and verifies the two rational example gains. It also performs 16 independent high-precision numerical quadratures, using the original minimum-kernel integral rather than the derived polynomial formulas. Run \(`python verify.py`\) with Python 3, SymPy, and mpmath. The mathematical argument, not those finite tests, supplies the universal quantifiers over all widths, noises, and window locations.

## Relationship to prior work
Nguyen and Peraire (2014, arXiv:1405.7569v1) develop Gaussian regression with linear-functional observations and conditional covariance calculations, without this fixed-exposure Brownian-bridge placement classification. Ji and Müller (2016, arXiv:1604.05375v1, especially Section 2) introduce integrated posterior trajectory prediction error as a design criterion and optimize **point** observation times; their general criterion alone does not solve the present constrained interval-average problem. The published result *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature* concerns two random, noiseless **point evaluations** and posterior **integral variance**, not one noisy window measurement or integrated **path** variance. These criteria are mathematically different even though they share the Brownian-bridge kernel. Mukherjee's earlier dissertation on sampling designs for random processes is a potentially relevant general source, but its accessible catalog describes point sampling rather than fixed-width averaging; its full text was not available for a decisive whole-document comparison. The paper *An analytical description of the time-integrated Brownian bridge* concerns the time-average of marginal location distributions in movement modeling, not the conditional risk of a sensor that averages a path on one selected window.

## Limitations
There is one freely translated **uniform** window, not several windows or a controllable exposure width. The endpoint and center regimes rely on the exact Brownian-bridge kernel and additive noise with fixed variance for the average. Results for Brownian motion without terminal pinning, different kernels, other window profiles, adaptive observations, or optimal exposure widths are not established. Scholarly novelty is supported by the identified statement comparisons, not proven by exhaustive publication coverage; inaccessible or unindexed equivalent work may affect priority. No independent mathematical audit is claimed.

## References
1. N.-C. Nguyen and J. Peraire, *Functional Gaussian processes for regression with linear PDE models*, arXiv:1405.7569v1, first public 2014-05-29, https://arxiv.org/abs/1405.7569.
2. H. Ji and H.-G. Müller, *Optimal Designs for Longitudinal and Functional Data*, arXiv:1604.05375v1, first public 2016-04-18, https://arxiv.org/abs/1604.05375.
3. B. Mukherjee, *Optimal designs for estimating the path of a stochastic process*, Purdue University dissertation, public catalog https://docs.lib.purdue.edu/dissertations/AAI3043760/.
4. *Unique optimal i.i.d. two-node design for Brownian-bridge kernel quadrature*, published research record (2026), published-finding corpus record 1c7b05ec88c4, https://github.com/published-finding corpus/2026.
5. S. Van Nieuland, J. Baetens, H. De Meyer and B. De Baets, *An analytical description of the time-integrated Brownian bridge*, online 2015, https://doi.org/10.1007/s40314-015-0250-3.
