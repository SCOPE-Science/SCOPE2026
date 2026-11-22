# Three taxa are the minimum for reentrant species-richness rankings between Poisson-capture methods

## Finding
Suppose two environmental sampling methods A and B are applied to the same community of \(m\ge1\) present taxa. For each taxon \(i\), a sample of effort \(v>0\) produces a Poisson count of mean \(a_i v\) with A or \(b_i v\) with B, with \(a_i,b_i>0\) and perfect detection conditional on one or more captured molecules. Write \(R_A(v)\) and \(R_B(v)\) for the expected number of taxa detected. A **strict ranking reversal** means that \(R_A-R_B\) changes sign at a positive finite effort; the two methods may have different total capture rates.

**Theorem (sharp minimal taxon count and a two-taxon criterion).** For \(m=1\), there are no strict reversals. For \(m=2\), there is at most one, and there is exactly one if and only if
\[
\big((a_1+a_2)-(b_1+b_2)\big)\big(\min\{a_1,a_2\}-\min\{b_1,b_2\}\big)<0.
\]
If the inequality fails, the strict ranking has constant sign for positive effort, or the methods are tied identically. For \(m=3\), the positive rate vectors
\[
(a_1,a_2,a_3)=(2,3,11),\qquad(b_1,b_2,b_3)=(1,6,8)
\]
have **exactly two** strict ranking reversals: method A has higher expected richness for \(0<v<\tfrac12\log\rho\) and for \(v>\log\rho\), whereas B has higher expected richness for \(\tfrac12\log\rho<v<\log\rho\), where \(\rho>1\) is the unique positive root of \(\rho^3=\rho+1\). Ties occur only at the two displayed positive efforts. Thus three taxa are necessary and sufficient for two reversals; for every \(m>3\) the construction extends by adding taxa with identical strictly positive rates in the two methods. The inequalities and crossings persist under sufficiently small independent perturbations of the six rates.

## Assumptions and scope
The community contains \(m\) fixed taxa, each truly present. Conditional capture counts for each method and taxon are Poisson with a constant positive rate per common effort unit; only the indicator of at least one molecule is used. The expected richness is a comparison of alternative methods at the *same nominal effort*, not equal total molecule throughput: \(\sum_i a_i\) and \(\sum_i b_i\) need not agree. The model does not incorporate false positive detections, variable amplification, finite-population depletion, spatial heterogeneity, or multiple-run dependence. The analysis is deterministic at the level of expectations and does not claim that observed richness is ordered with certainty. Absolute scale may be changed by replacing every rate by the same positive multiplier, inversely rescaling the crossover efforts.

## Proof
**1. Capture identity.** The event of zero captured molecules of taxon \(i\) has probability \(e^{-a_iv}\) for A, respectively \(e^{-b_iv}\) for B. Linearity of expectation gives
\[
R_A(v)=\sum_{i=1}^m(1-e^{-a_iv}),\quad R_B(v)=\sum_{i=1}^m(1-e^{-b_iv}),\quad \Delta(v)=R_A(v)-R_B(v)=\sum_i(e^{-b_iv}-e^{-a_iv}).
\]
For one taxon, the sign is constant.

**2. Two-taxon strict one-crossing law.** If the per-taxon differences \(a_i-b_i\) have the same weak sign, all nonzero summands of \(\Delta\) have that sign. Otherwise relabel the two taxa so that \(a_1>b_1\) and \(a_2<b_2\). Put
\[
\alpha=\frac{a_1-b_1}{2}>0,\quad\beta=\frac{b_2-a_2}{2}>0,\quad c=\frac{a_1+b_1-a_2-b_2}{2}.
\]
The sign of \(\Delta(v)\) is the sign of
\[
L(v)=\log\frac{\sinh(\alpha v)}{\sinh(\beta v)}-cv.
\]
As \(v\downarrow0\), \(L(v)\to\log(\alpha/\beta)\). As \(v\to\infty\), \(L(v)/v\to\alpha-\beta-c=a_2-b_1\). Moreover
\[
L''(v)=\frac{\beta^2}{\sinh^2(\beta v)}-\frac{\alpha^2}{\sinh^2(\alpha v)},
\]
which is strictly positive if \(\alpha>\beta\) and strictly negative if \(\alpha<\beta\), since \(u/\sinh(uv)\) strictly decreases with \(u>0\) for fixed \(v>0\).

If \(\alpha>\beta\) and \(a_2<b_1\), the increasing function \(L'\) approaches the negative limit \(a_2-b_1\). Consequently \(L'<0\) throughout, \(L(0+)>0\), and \(L\to-\infty\): there is exactly one transverse root. If \(\alpha>\beta\) and \(a_2\ge b_1\), the identity
\[
\frac{\sinh(\alpha v)}{\sinh(\beta v)}=e^{(\alpha-\beta)v}\frac{1-e^{-2\alpha v}}{1-e^{-2\beta v}}>e^{(\alpha-\beta)v}
\]
gives \(L(v)>(a_2-b_1)v\ge0\), so there is no root. Reversing the strict inequalities treats \(\alpha<\beta\): exactly one transverse root occurs when \(a_2>b_1\), while otherwise \(L<0\). If \(\alpha=\beta\), then \(L(v)=-cv\) and the ranking never reverses (the \(c=0\) case is an identical expected-richness curve). In the opposite-advantage case,
\[
(a_1+a_2)-(b_1+b_2)=2(\alpha-\beta),
\]
and \(\min_i a_i-\min_i b_i\) has the sign of \(a_2-b_1\) (including zero). This proves the displayed necessary-and-sufficient criterion, including boundary and tie cases.

**3. Three-taxon exact witness.** Set \(y=e^{-v}\in(0,1)\). Direct substitution of the integer vectors gives
\[
\Delta(v)=y+y^6+y^8-y^2-y^3-y^{11}=-y(y-1)(y^3+y^2-1)(y^6+y^4-1).
\]
The prefactor \(-y(y-1)\) is positive on \((0,1)\). Both polynomials \(p(y)=y^3+y^2-1\) and \(q(y)=y^6+y^4-1=p(y^2)\) are strictly increasing on \((0,1)\), each from \(-1\) to \(+1\). Let \(r\in(0,1)\) be the unique root of \(p\). The unique root of \(q\) is \(\sqrt r\), with \(r<\sqrt r\). Therefore the sign of \(\Delta\), as \(y\) decreases from 1 to 0, is positive, negative, positive, with no other positive-effort zeros. Since \(\rho=1/r\) obeys \(\rho^3=\rho+1\), the two crossing efforts are exactly \(\tfrac12\log\rho\) and \(\log\rho\). Both roots are simple because both polynomials have positive derivatives and distinct roots; continuity proves robustness under small perturbations of the six parameters. Identical-rate appended taxa cancel exactly in \(\Delta\), establishing existence for every larger \(m\).

## Verification
Run `python3 checker.py` in the directory containing the attached checker. Its standard-library-only calculations independently multiply the polynomial factors, bracket both positive \(y\)-roots with rational signs, check three alternating richness rankings at rational \(y\), and test the one-crossing prediction on a finite grid of two-taxon positive integer rate vectors. Exact algebra and the monotonicity proof, not finite-grid output, establish the infinite-parameter theorem. The positive efforts are approximately \(0.14059978716148\) and \(0.28119957432296\) in the units determined by the given rates.

## Relationship to prior work
Kirtane and coauthors' environmental-DNA capture-method study, publicly archived with data in August 2024, directly motivates comparison of method-specific detected diversity and reports different taxa recovered by grab and tow-net sampling. It does **not** provide or test the Poisson-rate-versus-effort phase statement here; its journal article appeared in December 2024. Classical Poisson/Coleman species-accumulation models establish the expectation formula, and Chase and coauthors document empirical multiple crossings of rarefaction rankings. The published research note *Four species are necessary and sufficient for two reversals in expected species accumulation rankings* establishes a different sharp threshold under equally normalized probability vectors and the **same number of iid individuals** for both communities. Under Poisson sampling this gives equal total capture-rate normalization, whereas the distinct technologies here can have \(\sum_i a_i\ne\sum_i b_i\). Its four-species obstruction therefore does not imply the present three-taxon witness; conversely the witness does not contradict the normalized result. General exponential-polynomial zero-count arguments and elementary hyperbolic inequalities are established mathematics, not claimed as new standalone tools. The contribution is the sharp minimum under separately calibrated method-specific positive Poisson capture rates, its complete two-taxon crossover criterion, and the exact reentrant three-taxon example.

## Limitations
This is an idealized expectation-level illustration, not an estimate of eDNA detection rates in the Kirtane dataset and not a proposed field operating volume. Sampling methods with the same total capture intensity fall into a more restrictive class, and the three-taxon example uses unequal totals, \(16\) versus \(15\). A method's expected richness approaches \(m\) as effort tends to infinity, so the final strict advantage exists at every finite effort above the second crossover but vanishes in the limit. The theorem establishes the minimum species count permitting **two** reversals, not the maximal number of reversals for all larger counts. Broad earlier ecological curve-crossing theory leaves a residual historical-priority risk for this specialized threshold.

## References
1. Kirtane, A., Howard, L., Beaver, C., Hunter, M., Luikart, G., and Deiner, K. (2024). *How, What, and Where You Sample Environmental DNA Affects Diversity Estimates and Species Detection.* Environmental DNA 6, e70042. Full open-access article https://doi.org/10.1002/edn3.70042 (journal first published 2024-12-16). First public research data available 2024-08-27: https://doi.org/10.5061/dryad.bzkh189jt.
2. Colwell, R. K., et al. (2012). *Models and estimators linking individual-based and sample-based rarefaction, extrapolation and comparison of assemblages.* Journal of Plant Ecology 5, 3–21. https://doi.org/10.1093/jpe/rtr044.
3. Chase, J. M., et al. (2018). *Embracing scale-dependence to achieve a deeper understanding of biodiversity and its change across communities.* Ecology Letters 21, 1737–1751. https://doi.org/10.1111/ele.13151. Lawful full text: https://sciences.ucf.edu/biology/d4lab/wp-content/uploads/sites/23/2020/08/Chase-etal-2018.pdf.
4. Chao, A. and Jost, L. (2012). *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size.* Ecology 93, 2533–2547. https://doi.org/10.1890/11-1952.1.
5. *Four species are necessary and sufficient for two reversals in expected species accumulation rankings* (2026). Published research note, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-four-species-are-necessary-and-sufficient-for-two-reversals-in-e--4a0966e867d7/RESULT.md.
