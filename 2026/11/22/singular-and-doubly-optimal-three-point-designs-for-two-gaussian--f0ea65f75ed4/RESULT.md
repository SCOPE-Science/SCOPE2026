# Singular and doubly optimal three-point designs for two Gaussian image sources

## Finding

In a one-dimensional background-dominated *read-noise* imaging model with two point sources of known distinct positions and known common Gaussian width, the three equal-variance measurements made at a fixed central point and two adjustable symmetric points can lose identifiability at a **strictly positive** sampling radius. This happens precisely when the half-separation between the sources exceeds one Gaussian width. For every such source separation the determinant-information curve has positive local maxima on both sides of the singular sampling radius. Moreover, there is **at least one** source separation at which two different sampling radii are both *globally* D-optimal within the specified symmetric three-sample design family.

Specifically, let the normalized source positions be \(-d\) and \(d\), with \(d>0\). For measurements at \(-x,0,x\), let
\[
 a=e^{-(x-d)^2/2},\qquad b=e^{-(x+d)^2/2},\qquad c=e^{-d^2/2},
\]
where \(x>0\). Up to orientation, the determinant of the three-parameter regression matrix is
\[
 \Delta_d(x)=(a-b)(a+b-2c).
\]
Under independent Gaussian measurement noise of common variance \(\nu^2>0\), the Fisher determinant equals \(\nu^{-6}\Delta_d(x)^2\). The following conclusions hold.

1. If \(0<d\le1\), then \(\Delta_d(x)<0\) for every \(x>0\); all noncoincident symmetric sampling designs have full rank.
2. If \(d>1\), there is exactly one \(x_0(d)>0\) with \(\Delta_d(x_0(d))=0\). It is the unique positive solution of
\[
 e^{-x^2/2}\cosh(dx)=1.
\]
The regression matrix has rank exactly two there. As \(d\downarrow1\), the singular radius emerges by the sharp square-root law
\[
 x_0(d)=\frac{\sqrt{6(d^2-1)}}{d^2}+O\bigl((d^2-1)^{3/2}\bigr).
\]
The determinant changes sign from positive to negative across \(x_0(d)\), and \(\Delta_d(x)^2\) has at least one strict local maximum in each of \((0,x_0(d))\) and \((x_0(d),\infty)\).
3. For at least one \(d_\dagger>1\), the largest values of \(\Delta_{d_\dagger}(x)^2\) on those two intervals coincide. Hence at least two distinct positive radii are globally D-optimal in the symmetric three-sample family. A numerical illustration finds such a tie near \(d\approx1.30915604213\), at radii \(x\approx1.24282335\) and \(x\approx2.62070748\). **No uniqueness assertion about \(d_\dagger\) or either maximizing radius is made**; these decimals are numerical illustrations, not certified root enclosures.

In physical coordinates the transition \(d=1\) means that the source-to-source separation is twice the Gaussian standard deviation.

## Assumptions and scope

Let \(\sigma>0\) and let two source centers lie at \(-d\sigma\) and \(d\sigma\). Their unknown flux coefficients are \(F_-\) and \(F_+\), and the unknown spatially constant background coefficient is \(B\). The response at normalized coordinate \(z\) is
\[
 m(z)=F_-e^{-(z+d)^2/2}+F_+e^{-(z-d)^2/2}+B.
\]
The instrument chooses an arbitrary \(x>0\) and reads the ideal point samples at \(-x\), \(0\), and \(x\). The three observations have independent normal errors, all with the same **known positive variance** \(\nu^2\), independent of signal level and sampling coordinate. The PSF width, centers, gain, and sampling-center symmetry are assumed known. Only the three linear coefficients \((F_-,F_+,B)\) are unknown. D-optimality means maximizing the determinant of their \(3\times3\) Fisher information matrix *over this one-parameter symmetric design family*, not over all possible pixel locations or unrestricted observing plans.

The Gaussian regression is an idealization of point sampling; finite pixels, photon-limited Poisson noise, time-varying PSFs, source-position uncertainty, background gradients, nonuniform variances, correlations, and physical signal positivity constraints are outside the theorem.

## Proof

**1. Information determinant.** Define the response matrix \(M_d(x)\) by taking at each of \(z=-x,0,x\) the row \((e^{-(z+d)^2/2},e^{-(z-d)^2/2},1)\). Its rows are \((b,a,1)\), \((c,c,1)\), and \((a,b,1)\). Expansion by the central row gives \(|\det M_d(x)|=|(a-b)(a+b-2c)|\). With the stipulated homoscedastic Gaussian noise the Fisher information is \(I_d(x)=\nu^{-2}M_d(x)^{\mathsf T}M_d(x)\), so \(\det I_d(x)=\nu^{-6}\Delta_d(x)^2\).

**2. Sharp rank threshold.** For every \(x,d>0\), \(a-b>0\), and
\[
 a+b-2c=2c\bigl(f_d(x)-1\bigr),\qquad
 f_d(x)=e^{-x^2/2}\cosh(dx).
\]
The elementary inequality \(\log\cosh u<u^2/2\) for every \(u>0\) follows by integrating \(u-\tanh u>0\). If \(d\le1\), then \(\log f_d(x)<(d^2-1)x^2/2\le0\), proving the first assertion.

If \(d>1\), then
\[
 \frac{d}{dx}\log f_d(x)=x\left(\frac{d\tanh(dx)}{x}-1\right).
\]
The quotient \(d\tanh(dx)/x\) strictly decreases from \(d^2>1\) to zero: the derivative of \(\tanh u/u\) is negative for \(u>0\) because \(\tanh u-u\operatorname{sech}^2u>0\), whose derivative is \(2u\operatorname{sech}^2u\tanh u>0\). Thus \(f_d\) first strictly increases above \(f_d(0)=1\), then strictly decreases to zero. The intermediate value theorem gives exactly one positive return to level one, \(x_0(d)\), with \(f_d(x)>1\) to its left and \(f_d(x)<1\) to its right. At \(x_0(d)\), the matrix has determinant zero but has rank at least two because its two Gaussian source columns have unequal outer entries \(a\ne b\). Its rank is therefore exactly two. For the onset expansion, write \(y=x^2\) and expand
\[
 \frac{\log f_d(\sqrt{y})}{y}=\frac{d^2-1}{2}-\frac{d^4y}{12}+O(y^2)\quad (y\downarrow0).
\]
The implicit function theorem applied at \(y=0,d=1\) gives the unique small positive root \(y=6(d^2-1)/d^4+O((d^2-1)^2)\); taking square roots proves the displayed asymptotic.

**3. Both local information peaks.** For \(d>1\), \(\Delta_d\) is continuous, is positive on \((0,x_0(d))\), negative on \((x_0(d),\infty)\), and vanishes at \(0\), at \(x_0(d)\), and in the limit \(x\to\infty\). Each of the two open intervals therefore contains a strictly positive attained maximum of \(\Delta_d(x)^2\); the maxima are strict local maxima because the objective is real analytic and nonconstant, and hence cannot be constant on a nondegenerate interval.

**4. Global tie must occur.** Let \(L(d)=\max_{0\le x\le x_0(d)}\Delta_d(x)\) and \(R(d)=\max_{x\ge x_0(d)}(-\Delta_d(x))\) for \(d>1\). Both are positive and continuous in \(d\). Indeed, the strictly descending positive root \(x_0(d)\) depends continuously on \(d\); maxima over the compact left branch vary continuously, and the right branch has uniformly vanishing tails on each compact range of \(d\), so its supremum is likewise continuous.

As \(d\downarrow1\), the positive root \(x_0(d)\to0\). To justify boundedness, observe that \(f_d(x)<e^{-x^2/2+dx}<1\) for \(x>2d\), so \(x_0(d)<2d\); any nonzero limit point would contradict Step 2 at \(d=1\). Hence \(L(d)\to0\). On the other hand, at \(d=1\), \(x=2\) gives \(a=c=e^{-1/2}\), \(b=e^{-9/2}\), and \(-\Delta_1(2)=(c-b)^2>0\); hence \(\liminf_{d\downarrow1}R(d)>0\).

For large \(d\), evaluating the inner branch at \(x=d\) yields
\[
 \Delta_d(d)=(1-e^{-2d^2})(1+e^{-2d^2}-2e^{-d^2/2})\longrightarrow1.
\]
This point lies in the positive branch for sufficiently large \(d\). Conversely, everywhere on the outer branch, \(-\Delta_d(x)=(a-b)(2c-a-b)\le2c\), because \(0<a-b<1\). Consequently \(R(d)\le2e^{-d^2/2}\to0\), so \(L(d)>R(d)\) for sufficiently large \(d\). By continuity, some \(d_\dagger>1\) satisfies \(L(d_\dagger)=R(d_\dagger)\). Because \(\Delta_d(x)^2\) equals the squared positive-branch and negative-branch maxima, two distinct global optimizers exist at this separation.

## Verification

Run `python checker.py` with Python, NumPy and SciPy installed. The program compares the closed determinant with direct \(3\times3\) matrix determinants and Fisher Gram determinants; numerically finds the unique rank-defect radius for a range of separations; checks representative lobe signs; and locates an illustrative equal-height configuration. A successful replay prints `diagnostic_checks_passed 323` followed by numerical values. These finite diagnostics are corroboration only; the proof above establishes the quantified assertions for all permitted real parameters.

## Relationship to prior work

The 2013 full-text analysis by Méndez, Silva and Lobos develops Fisher/Cramér–Rao theory for a **single** Gaussian point source's unknown position in a noisy one-dimensional detector. It does not give the three-parameter two-source/background symmetric design's singular curve or double optimum. King and colleagues' 2013 observational study deals with optimal extraction in crowded near-infrared fields; the accessible abstract does not supply a comparable all-separation D-design classification. Prasad's 2014 full-text analysis considers binary hypothesis discrimination of one source versus an equally bright *pair*, not D-optimal selection of three locations for two unknown fluxes and background. Primini and Kashyap's 2014 full-text work derives simultaneous source/background photometric inference, including overlapping apertures, under a Poisson photon-count model and evaluates several aperture choices; it does not classify D-optimal symmetric *point measurements with homoscedastic Gaussian errors*.

The result is restricted to its stated design family, so it neither contradicts nor purports to improve general unrestricted optimal-design theorems. Its novelty lies in the closed Gaussian overlap rank-defect threshold and the existence of two distinct global symmetric layouts under exact three-sample information budgeting, as opposed to a generic statement that an optimizer exists.

## Limitations

This is not a claim about all three-pixel layouts, all Gaussian point-spread imaging systems, Poisson-counting sensors, nor about achievable precision with any particular finite CCD pixel size. The mathematical existence of a tied pair does not imply uniqueness of the transition separation; the numerical approximation is not a certificate of unique criticality. The Gaussian constant-noise assumption approximates read-noise-dominated measurements; using photon-dependent variances can change the optimum. Source centers and width must be known, and no empirical validation or claim of established historical priority is made.

## References

- Méndez, R. A., Silva, J. F., and Lobos, R. (2013), *Analysis and interpretation of the Cramér–Rao lower-bound in astrometry: One dimensional case*, arXiv:1304.6361, first public April 23, 2013. https://arxiv.org/abs/1304.6361
- King, R. R., Naylor, T., Broos, P. S., Getman, K. V., and Feigelson, E. D. (2013), *The Wide-Field Near Infrared Data: Optimal Photometry in Crowded Fields*, arXiv:1309.4487, first public September 17, 2013. https://arxiv.org/abs/1309.4487
- Prasad, S. (2014), *Asymptotics of Bayesian Error Probability and 2D Pair Superresolution*, arXiv:1403.4919, first public March 19, 2014. https://arxiv.org/abs/1403.4919
- Primini, F. A. and Kashyap, V. L. (2014), *Determining X-Ray Source Intensity and Confidence Bounds in Crowded Fields*, arXiv:1410.2564, first public October 9, 2014. https://arxiv.org/abs/1410.2564
