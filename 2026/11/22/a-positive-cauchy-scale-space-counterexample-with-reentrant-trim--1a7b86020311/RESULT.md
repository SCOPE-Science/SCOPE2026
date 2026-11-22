# A positive Cauchy scale-space counterexample with reentrant trimodality

## Finding

Let \(P_h(x)=h/[\pi(x^2+h^2)]\) be the real-line Poisson (Cauchy) kernel, and let \(\mu=\delta_{-1}+\frac{49}{100}\delta_0+\delta_1\) be a positive atomic measure. Define \(U_h=P_h*\mu\). At four strictly increasing smoothing heights,
\[
h\in\left\{\frac1{\sqrt2},\,1,\,\sqrt{\frac65},\,\sqrt{\frac32}\right\},
\]
the numbers of strict local maxima of \(x\mapsto U_h(x)\) on the entire real line are, respectively,
\[
\boxed{3,\quad2,\quad3,\quad1.}
\]
Every critical point at these four heights is nondegenerate. In particular, increasing the Poisson smoothing height from \(1\) to \(\sqrt{6/5}\) **creates** two local critical points and increases the mode count from two to three, despite every mass being positive. Replacing the atoms by \(100\), \(49\), and \(100\) coincident observations gives an ordinary equally weighted Cauchy kernel density estimate on \(249\) data points with the same four mode counts. The counts also persist under sufficiently small arbitrary perturbations of all data-point locations, so distinct data points can be used.

The result is an exact, positive-data counterexample to monotonic mode disappearance under Cauchy/Poisson smoothing; it is not a claim about Gaussian smoothing or monotonicity at every intermediate height.

## Assumptions and scope

All masses are positive. The support consists of three specified real locations. The kernel is the standard upper-half-plane Poisson kernel, normalized to total integral one. The phrase *mode* means a **strict local maximum** of the one-variable smoothed density, not a global maximum. No assumption is made about all smoothing heights beyond the four displayed heights. The positivity multiplier \(h/\pi\) does not affect the locations or number of modes at a fixed height.

Set \(q=h^2\), \(w=49/100\), and
\[
H_q(x)=\frac{w}{x^2+q}+\frac1{(x-1)^2+q}+\frac1{(x+1)^2+q}.
\]
The modes of \(U_h\) and \(H_q\) coincide.

## Proof

**1. Reduction to a quartic in squared position.** Put \(y=x^2\). Direct rational differentiation gives
\[
H'_q(x)=-\frac{2xP_q(x^2)}{(x^2+q)^2((x-1)^2+q)^2((x+1)^2+q)^2},
\]
where
\[
\begin{aligned}
P_q(y)={}&(w+2)y^4+4(qw+2q-w+1)y^3\\
&+2(3q^2w+6q^2-2qw+2q+3w-3)y^2\\
&+4(q+1)(q^2w+2q^2-3q-w)y\\
&+(q+1)(q^3w+2q^3+3q^2w-6q^2+3qw+w).
\end{aligned}
\]
The denominator is strictly positive on the real axis. Since \(H_q\) is even and \(H'_q\) has the sign of \(-xP_q(x^2)\) for \(x>0\), the positive roots of \(P_q\) determine all noncentral critical points.

**2. Four exact rational sign certificates.** Multiplication of \(P_q\) by a positive rational scalar and removal of common integer factors gives the following primitive integer quartics. The coefficient signs are read from highest to lowest degree.

| \(q\) | Primitive integer quartic in \(y\) | Positive roots |
|---|---|---|
| \(1/2\) | \(1328y^4+3744y^3+904y^2-4376y+323\) | Exactly 2 |
| \(1\) | \(249y^4+1200y^3+1392y^2-800y-16\) | Exactly 1 |
| \(6/5\) | \(155625y^4+874500y^3+1306350y^2-277420y+4609\) | Exactly 2 |
| \(3/2\) | \(3984y^4+27168y^3+53784y^2+9800y+3625\) | Exactly 0 |

For \(q=1/2\), the coefficient sequence has two sign changes, so Descartes' rule bounds the positive roots by two, counted with multiplicity. The polynomial has signs \(+,-,+\) at \(y=0,1/10,1\), producing two distinct positive roots by the intermediate-value theorem. For \(q=1\), there is exactly one coefficient sign change and the values at \(y=0,1\) have signs \(-,+\), producing exactly one positive root. For \(q=6/5\), there are two sign changes and the signs at \(y=0,1/20,1/5\) are \(+,-,+\), producing exactly two distinct positive roots. For \(q=3/2\), every coefficient is positive, so there is no positive root. These arguments simultaneously prove simplicity of all positive roots, since the number of distinct roots equals the Descartes bound. In all four cases \(P_q(0)\ne0\), so the central critical point is also nondegenerate.

**3. Classification of maxima.** At \(q=1/2\) and \(q=6/5\), \(P_q(0)>0\) and there are exactly two positive simple roots. On \(x>0\), the derivative has signs \(-,+,-\), giving one central maximum and one symmetric pair of outer maxima: three in total. At \(q=1\), \(P_q(0)<0\), and there is exactly one positive simple root. The derivative has signs \(+,-\) on \(x>0\), giving a central minimum and two symmetric maxima. At \(q=3/2\), \(P_q(y)>0\) for every \(y\ge0\), so \(H_q\) decreases strictly for positive \(x\), giving one central maximum. This proves all four counts.

**4. Positive equal-weight and distinct-data realizations.** Multiplying \(\mu\) by \(100\) makes its masses \((100,49,100)\), which is the counting measure of \(249\) observations with repetitions at the three locations. Normalization by \(249\) does not change modes. Every critical point at the four fixed heights is simple and the derivative has a fixed outward sign for sufficiently large \(|x|\). Uniform continuity of rational derivatives on compact intervals, together with the uniform tail sign for configurations in a small neighborhood of the fixed locations, ensures that sufficiently small independent perturbations of all \(249\) observation locations preserve every critical-point count. They may be chosen pairwise distinct. No explicit perturbation radius is asserted.

## Verification

The standalone `check_exact.py` artifact uses exact rational algebra via SymPy. It reconstructs the rational derivative identity, all four primitive integer quartics, the coefficient sign-variation bounds, and the rational sign brackets. Run `python check_exact.py` with SymPy installed. The output lists exact positive-root counts \(2,1,2,0\) and mode counts \(3,2,3,1\), and finishes with `PASS`. No numerical root-finding is needed for the proof.

## Relationship to prior work

Chaudhuri and Marron (2000), in *Scale Space View of Curve Estimation*, demonstrated Cauchy-kernel noncausality for signed three-point regression weights but explicitly reported no example with all weights positive, suggesting Cauchy causality might survive for density estimation. The present positive measure gives a concrete counterexample to that specific possibility. Hall, Minnotte and Zhang (2005) treat nonmonotone mode counts for compactly supported smoothing kernels; those mechanisms do not directly settle the unbounded-support Cauchy kernel. Chaubey (2018) studies wrapped Cauchy/Poisson density smoothing on the circle, not this real-line positive-data counterexample. Vila and collaborators (2022) analyze trimodality in a different constructed density family, rather than reentrant scale changes of a three-atom Cauchy mixture. An earlier equal-weight three-atom Poisson peak threshold classifies \(\delta_{-1}+\delta_0+\delta_1\), which has no such reentrant phase and does not imply the unequal central-weight result. Carreira-Perpiñán and Williams (2003, §2.1) anticipate mode creation for non-Gaussian kernels but illustrate other kernel profiles and note the difficulty of Cauchy examples. Carreira-Perpiñán (2015, p. 8) states in general that Cauchy kernel density estimates can gain modes with bandwidth; consequently **the broad possibility of positive-data Cauchy noncausality is not claimed as new**. The precise contribution here is the elementary rational-mass, exact four-height \(3,2,3,1\) witness, with exact proof and finite equally weighted realizability. The 2015 remark is a historical-priority risk for any novelty asserted for the qualitative phenomenon alone.

## Limitations

This is an exact four-height witness, not a complete all-height bifurcation diagram or a minimal-sample-size theorem. The sharp range of positive center weights exhibiting reentrant mode counts is not determined. Although published and indexed results inspected did not imply this positive-data example, historical novelty remains provisional pending wider independent review. Distinct-site robustness is existential, not quantitatively optimized. The modal distinctions are mathematical, not a statistical significance test on observed data.

## References

1. P. Chaudhuri and J. S. Marron, *Scale Space View of Curve Estimation*, Annals of Statistics 28 (2000), 408–428, https://doi.org/10.1214/aos/1016218224, author manuscript https://www.marronwebfiles.sites.oasis.unc.edu/OldResearch/papers/scaspa2c.pdf.
2. Y. P. Chaubey, *Smooth Kernel Estimation of a Circular Density Function: A Connection to Orthogonal Polynomials on the Unit Circle*, Journal of Probability and Statistics (2018), Article 5372803, first public 2018-04-01, https://doi.org/10.1155/2018/5372803.
3. R. Vila, V. Serra, M. N. Çankaya and F. Quintino, *A General Class of Trimodal Distributions: Properties and Inference*, first public 2022-04-07, arXiv:2204.03602, https://arxiv.org/html/2204.03602v1.
4. P. Hall, M. C. Minnotte and C. Zhang, *Bump Hunting with Non-Gaussian Kernels*, arXiv:math/0503676 (2005), https://arxiv.org/abs/math/0503676.
