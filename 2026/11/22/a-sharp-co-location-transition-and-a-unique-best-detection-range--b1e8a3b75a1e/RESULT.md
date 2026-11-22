# A sharp co-location transition and a unique best detection range for two symmetric ecological cameras

## Finding

**Theorem.** Fix a baseline detection probability \(0<p<1\) and a spatial population scale \(w>0\). Let \(X\) be a random activity centre with isotropic Gaussian law \(N(0,w^2 I_2)\) in the plane. Two independent, identical, nondestructive detectors are placed at \(\pm s e_1\), where \(s\geq0\), and conditional on \(X=x\), detector \(i\) records that individual with probability
\[
 p\exp\!\left(-\frac{\|x-z_i\|^2}{2r^2}\right),\qquad z_i\in\{-s e_1,s e_1\},
\]
with fixed detection width \(r>0\). Let \(C(s;r,p,w)\) be the probability of at least one detection, and put \(k=w^2/r^2\).

1. The unique optimal symmetric half-separation is \(s_*=0\) when \(k\leq k_0(p)\), and otherwise
\[
 s_*^2=\frac{2w^2(1+k)}{k(1+2k)}\log\!\left(\frac{p(1+k)^2}{1+2k}\right),\qquad
 k_0(p)=\frac{1-p+\sqrt{1-p}}{p}.
\]
The threshold is exact, including equality: colocating both detectors at the Gaussian habitat centre is uniquely optimal for all sufficiently wide detectors.

2. At fixed \(p,w\), the optimal physical separation \(2s_*(r)\) is **strictly unimodal** as a function of detection width on the interval where it is positive. It vanishes both for \(r\downarrow0\) and at the finite threshold \(r_c=w/\sqrt{k_0(p)}\), and is zero for all \(r\geq r_c\). Its unique maximizer is \(r_{\mathrm{peak}}=w/\sqrt{k_{\mathrm{peak}}}\), where \(k_{\mathrm{peak}}>k_0(p)\) is the unique solution of
\[
 \log\!\left(\frac{p(1+k)^2}{1+2k}\right)=\frac{2k^2}{2k^2+4k+1}.
\]

3. In the low-baseline-detection limit \(p\downarrow0\), with \(w\) held fixed,
\[
 k_0\sim\frac2p,\qquad k_{\mathrm{peak}}\sim\frac{2e}{p},\qquad
 r_{\mathrm{peak}}\sim s_*(r_{\mathrm{peak}})\sim w\sqrt{\frac{p}{2e}}.
\]
In particular, the best physical separation is asymptotic to twice the best detector width.

For illustration, with \(p=1/2\) and \(w=1\), co-location begins at \(r_c\approx0.6435942529\). The largest optimal physical separation is approximately \(0.6796510696\), attained at \(r\approx0.3738449893\); below and above this width, the optimal separation is smaller.

## Assumptions and scope

The random variable \(X\) is a *single* animal's location or activity centre; an independently sampled population of size \(N\) has expected distinct individuals detected \(N C\). Conditional detections at the two devices are independent Bernoulli trials. The detector amplitude \(p\) does not change as \(r\) changes. The habitat is the entire plane and its spatial Gaussian distribution is known. Both devices are constrained to the symmetric pair \(\pm s e_1\); the theorem does **not** optimize among arbitrary off-centre or unequal placements. Co-location is permitted because two independent sensors can register the same individual. No individual movement, false alarms, trap competition, counts across revisits, or estimation-precision objective is assumed. Detection widths are positive; limits at zero width are limits, not devices of zero width.

## Proof

**Gaussian coverage identity.** Conditional independence yields
\[
 C(s)=\mathbb E\left[g_+(X)+g_-(X)-g_+(X)g_-(X)\right],
 \quad g_\pm(x)=p\exp\!\left(-\frac{\|x\mp se_1\|^2}{2r^2}\right).
\]
Completing squares in the two-dimensional Gaussian integrals gives the exact expression
\[
 C(s)=A\exp(-\alpha s^2)-B\exp(-\beta s^2),
\quad A=\frac{2pr^2}{r^2+w^2},\quad B=\frac{p^2r^2}{r^2+2w^2},
\quad\alpha=\frac1{2(r^2+w^2)},\quad\beta=\frac1{r^2}.
\tag{1}
\]
Here \(A,B,\alpha>0\) and \(\beta>\alpha\). Equation (1) follows directly from the original detection law without a coverage approximation.

**Exact co-location transition.** For \(s>0\),
\[
 \frac{C'(s)}{2s}=\beta B e^{-\beta s^2}-\alpha A e^{-\alpha s^2}.
\]
Their initial ratio is
\[
 \frac{\beta B}{\alpha A}=\frac{p(1+k)^2}{1+2k}=\frac{p}{q(k)},
 \qquad q(k)=\frac{1+2k}{(1+k)^2}.
\tag{2}
\]
The ratio of the first exponential term to the second decreases strictly with \(s\). Thus if \(p\le q(k)\), then \(C'(s)<0\) for every \(s>0\), including equality in (2), proving the unique maximum \(s=0\). If \(p>q(k)\), the derivative is initially positive and changes sign exactly once, from positive to negative, at
\[
 s^2=\frac{\log(p/q(k))}{\beta-\alpha}=
 \frac{2w^2(1+k)}{k(1+2k)}\log\!\left(\frac p{q(k)}\right).
\]
Since \(C(s)\to0\) as \(s\to\infty\), this unique positive stationary point is the global maximum. Finally \(q'(k)=-2k/(1+k)^3<0\) for \(k>0\), with \(q(0)=1\) and \(q(k)\to0\). Solving \(p=q(k)\) gives the unique positive root \(k_0(p)=(1-p+\sqrt{1-p})/p\). This proves the first assertion for every admissible parameter, including the boundary.

**One and only one best width.** For \(k>k_0\) define
\[
 H(k)=s_*^2/w^2=a(k)L(k),\quad
 a(k)=\frac{2(1+k)}{k(1+2k)},\quad
 L(k)=\log\!\left(\frac{p(1+k)^2}{1+2k}\right)>0.
\]
The positive quantities
\[
 h(k)=-\frac{a'(k)}{a(k)}=\frac{2k^2+4k+1}{k(1+k)(1+2k)},
 \qquad L'(k)=\frac{2k}{(1+k)(1+2k)}
\]
satisfy
\[
 H'(k)=a(k)h(k)[T(k)-L(k)],
 \quad T(k)=\frac{L'(k)}{h(k)}=\frac{2k^2}{2k^2+4k+1}.
\tag{3}
\]
Put \(J=L-T\). Its derivative has the exact factorization
\[
 J'(k)=\frac{2k\left(4k^4+8k^3+4k^2-2k-1\right)}{(1+k)(1+2k)(2k^2+4k+1)^2}.
\tag{4}
\]
The polynomial in parentheses has coefficients with exactly one sign change, is negative at zero and tends to positive infinity. Descartes' sign rule, together with continuity, proves it has precisely one positive zero. Consequently \(J\) first decreases and then increases on \((0,\infty)\). At the co-location boundary, \(J(k_0)=-T(k_0)<0\); as \(k\to\infty\), \(J(k)=\log(pk/2)-1+o(1)\to\infty\). Therefore \(J\) crosses zero exactly once for \(k>k_0\). Formula (3) shows \(H\) increases until that crossing and decreases afterward. Because increasing detection width \(r\) corresponds to decreasing \(k=w^2/r^2\), the same unique maximum holds as a function of \(r\). At \(k\to\infty\), \(H(k)\sim (\log(pk/2))/k\to0\). At \(k\downarrow k_0\), \(H(k)\to0\). This establishes the claimed strict positive-interval unimodality and both endpoints.

**Rare-detection asymptotics.** As \(p\downarrow0\), the explicit threshold gives \(k_0\sim2/p\), so the unique maximizer satisfies \(k_{\mathrm{peak}}\geq k_0\to\infty\). At its defining equation \(L(k_{\mathrm{peak}})=T(k_{\mathrm{peak}})\), the right side tends to \(1\), while \(L(k)=\log(pk/2)+o(1)\) uniformly along such diverging roots. Hence \(p k_{\mathrm{peak}}/2\to e\). Moreover \(a(k)\sim1/k\); substituting into \(H(k_{\mathrm{peak}})=a(k_{\mathrm{peak}})L(k_{\mathrm{peak}})\) proves \(s_*^2/w^2\sim p/(2e)\), matching \(r_{\mathrm{peak}}^2/w^2=1/k_{\mathrm{peak}}\sim p/(2e)\). All assertions follow.

## Verification

The standalone `verify.py` requires only Python's standard library and writes diagnostic JSON to standard output. Run `python verify.py > verification_certificate.json` from a directory containing the script. The accompanying `verification_certificate.json` records the reproduced output: 11,156 checks, including 598 exact-rational derivative identities, 225 fixed-parameter global-spacing grid tests, 9 independent two-dimensional quadratures of the original integrand, and four rare-detection asymptotic cases. Numerical quadrature is a consistency check, not proof of any global or asymptotic statement. Equations (1)–(4), the one-positive-root sign argument and the limiting calculation supply the infinite-parameter proof. All stated rounding is descriptive only.

## Relationship to prior work

Litvak and coauthors' *Increasing Detection Performance of Surveillance Sensor Networks* (2008, section 5.2.1) treats two sensors with hard one-dimensional coverage intervals and constant in-range detection probability, proving a no-overlap criterion. It frames the overlap-versus-redundancy issue but has no Gaussian-tail kernel, planar normal activity-centre distribution or unique nonmonotonic physical separation as detector width varies. The accessible study-group copy was publicly deposited on 2009-11-09; the exact day of the original 2008 release is not established here.

Rowcliffe and coauthors (2011, full article, detection sensitivity section) fit half-normal or hazard-rate detector sensitivity to empirical camera-trap records; their purpose is estimation of detection-zone dimensions rather than maximizing two-camera distinct-individual coverage. Sun, Fuller and Royle (2014, full article, methods, results and discussion) simulate spatial capture–recapture estimation accuracy under alternative grid and cluster layouts; their target is parameter-estimator performance, not the exact symmetric-pair expected-distinct-count objective. Burton and coauthors (2015, review) document the practical importance of camera spacing and incomplete consideration of detection but do not provide a corresponding analytic phase diagram. Efford and Boulanger (2019, full article, section 3.1) give a general spatial integral for the expected number of detected individuals, logically containing an integral representation of this objective as a special case. Their general formula does **not** assert or establish the derived Gaussian-specific uniqueness of both the co-location threshold and the interior maximum of optimized physical spacing, nor the \(p\downarrow0\) scaling. No claim of novelty is made for inclusion–exclusion or Gaussian convolution alone.

A related published two-trap finite-path model (published-finding corpus, 2026, record `4b47353a8a35`) uses an *integer path*, a *uniform* location distribution, *geometrically* decaying detection and *certain* detection at a trap site; its main theorems classify boundary gaps and noncommuting large-path/long-range limits. Its proved assertions do not imply the planar half-normal, \(p<1\) co-location threshold or unique detection-width peak shown here. Frasca and coauthors (2014, arXiv:1404.7711) instead optimize expected worst distance to a nonfailed sensor in a one-dimensional domain. Generic facility-location and probabilistic-coverage models can subsume the objective definition without giving the particular global-uniqueness and scaling results proved here.

## Limitations

This is a theorem only for two **symmetrically constrained** cameras, not a theorem of global optimality over all planar layouts. The Gaussian habitat and half-normal detector response are idealizations; camera orientation, spatially variable detection, false positives, individual motion and field heterogeneity are excluded. Optimizing expected detected distinct individuals is not equivalent to optimizing abundance-estimator Fisher information or spatial recapture rates, for which overlap may carry separate information. No experiment is claimed to validate the Gaussian model or recommend a numerical field spacing. Historical originality remains provisional because no finite literature search proves priority, and unrestricted continuous probabilistic-coverage research may contain equivalent phase diagrams.

## References

1. N. Litvak et al., *Increasing Detection Performance of Surveillance Sensor Networks*, Proceedings of SWI 2008, pp. 85–116. Full lawful copy: https://miis.maths.ox.ac.uk/268/2/thales-report.pdf ; repository record with the verified public deposit date 2009-11-09: https://miis.maths.ox.ac.uk/miis/268/index.html .
2. J. M. Rowcliffe et al., *Quantifying the sensitivity of camera traps: an adapted distance sampling approach*, Methods in Ecology and Evolution 2 (2011), 464–476, first published 2011-03-01. DOI: https://doi.org/10.1111/j.2041-210X.2011.00094.x .
3. C. C. Sun, A. K. Fuller, J. A. Royle, *Trap Configuration and Spacing Influences Parameter Estimates in Spatial Capture-Recapture Models*, PLOS ONE 9 (2014), e88025, published 2014-02-05. DOI: https://doi.org/10.1371/journal.pone.0088025 .
4. A. C. Burton et al., *Wildlife camera trapping: a review and recommendations for linking surveys to ecological processes*, Journal of Applied Ecology 52 (2015), 675–685, first published 2015-03-21. DOI: https://doi.org/10.1111/1365-2664.12432 .
5. M. G. Efford, J. Boulanger, *Fast evaluation of study designs for spatially explicit capture–recapture*, Methods in Ecology and Evolution 10 (2019), 1529–1535, first published 2019-06-12. DOI: https://doi.org/10.1111/2041-210X.13239 .
6. P. Frasca, F. Garin, B. Gerencsér, J. M. Hendrickx, *Optimal one-dimensional coverage by unreliable sensors*, arXiv:1404.7711, initial public preprint 2014-04-30. https://arxiv.org/abs/1404.7711 .
7. *Noncommuting detection-range and landscape-size limits for two ecological traps*, 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-noncommuting-detection-range-and-landscape-size-limits-for-two-e--4b47353a8a35 .
