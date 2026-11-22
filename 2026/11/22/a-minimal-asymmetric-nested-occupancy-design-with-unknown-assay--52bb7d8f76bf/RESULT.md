# A minimal asymmetric nested-occupancy design with unknown assay false positives

## Finding

Consider replicate *site-level units* following the same two-stage occupancy and assay mechanism described below. For each site, take two independent primary samples, run two binary assays on the first primary sample, and one assay on the second. Across independent sites, the resulting three-bit distribution identifies **all four** unknown parameters—site occupancy, conditional primary-sample availability, true assay sensitivity, and false assay-positive probability—without external assay calibration, provided upstream primary-sample contamination is structurally excluded and assay sensitivity exceeds the false-positive probability. The design is sharp: no protocol with at most two assays, or with three assays all on one primary sample or all on distinct primary samples, identifies the four parameters on the stated open domain.

Write the binary assay results as \(X_1,X_2,Y\), where \(X_1,X_2\) interrogate the same primary sample and \(Y\) interrogates a second, conditionally independent primary sample. Define the four observable joint moments
\[
 A=\mathbb E X_1=\mathbb E Y,\quad B=\mathbb E(X_1X_2),\quad
 C=\mathbb E(X_1Y),\quad D=\mathbb E(X_1X_2Y).
\]
Let
\[
 V=C-A^2,\quad L=\frac{D-AB}{V},\quad
 \Delta=L^2-4(LA-B),\quad T=A-\frac{L-\sqrt\Delta}{2}.
\]
Then the unique inverse on the stated open parameter domain is
\[
 f=\frac{L-\sqrt\Delta}{2},\qquad p=\frac{L+\sqrt\Delta}{2},\qquad
 \psi=\frac{T^2}{V+T^2},\qquad
 \theta=\frac{T}{\psi(p-f)}.
\]
Here \(f\) is the unknown assay false-positive probability; \(p\) is its true-positive probability; \(\psi\) is site occupancy; and \(\theta\) is primary-sample availability conditional on an occupied site. In particular, \(V>0\) and \(\Delta=(p-f)^2>0\). The Jacobian of the forward moment map, with parameter order \((\psi,\theta,p,f)\), is
\[
 -\psi^2(1-\psi)\theta^4(p-f)^6.
\]
This gives an exact structural conditioning warning near low availability, near certain site occupancy, and near indistinguishable true and false assay responses.

## Assumptions and scope

Fix four unknown parameters \(0<\psi<1\), \(0<\theta<1\) and \(0<f<p<1\). Different sites are independent and identically distributed, with no site-level covariates or time variation during the survey. Each site's broad occupancy state is \(Z\sim\operatorname{Bernoulli}(\psi)\). Conditional on \(Z=1\), two primary-sample availability indicators \(U_1,U_2\) are independent \(\operatorname{Bernoulli}(\theta)\); conditional on \(Z=0\), both are zero with probability one. The latter is a **known zero probability of upstream contamination**, not an estimated property and not a claim that false assays cannot occur.

Conditional on \(U_1,U_2\), the three assays are independent. Each assay directed at a primary sample with \(U_j=1\) is positive with probability \(p\), and otherwise positive with probability \(f\). Assays of the same primary sample share its latent availability indicator, so they are not independent without conditioning. The three-bit law refers to repetitions of this entire protocol over a population of sites; a single site with three results is insufficient for statistical point estimation. The result concerns **structural identifiability**, not finite-sample precision, an unbiased estimator, clinical assay performance, or ecological closure robustness.

## Proof

**Forward moment identities.** Put \(g=f+\theta(p-f)\) and \(h=f^2+\theta(p^2-f^2)\). If \(Z=0\), the respective conditional mean and within-primary double-positive probability are \(f\) and \(f^2\); if \(Z=1\), they are \(g\) and \(h\). Distinct primary samples are conditionally independent given \(Z\). Therefore
\[
\begin{aligned}
 A&=(1-\psi)f+\psi g,\\
 B&=(1-\psi)f^2+\psi h,\\
 C&=(1-\psi)f^2+\psi g^2,\\
 D&=(1-\psi)f^3+\psi hg.
\end{aligned}
\]
The cross-primary covariance equals
\[
 C-A^2=\psi(1-\psi)(g-f)^2>0.
\]
Likewise
\[
 D-AB=\psi(1-\psi)(h-f^2)(g-f).
\]
As \(h-f^2=\theta(p-f)(p+f)=(g-f)(p+f)\), division gives \(L=p+f\). Moreover \(B=f^2+(A-f)(p+f)=A(p+f)-pf\), so \(LA-B=pf\). The roots of \(u^2-Lu+(LA-B)=0\) are precisely \(f,p\); their order is fixed by \(f<p\). This proves the displayed square-root recovery and \(\Delta=(p-f)^2\).

**Recovering the upper stages.** Since \(T=A-f=\psi\theta(p-f)\), the covariance identity becomes \(V=(1-\psi)T^2/\psi\). Therefore \(\psi=T^2/(V+T^2)\), followed by \(\theta=T/[\psi(p-f)]\). Every denominator is strictly positive under the assumptions. Hence the inverse is global and unique. Differentiating the four forward expressions and expanding the determinant gives \(-\psi^2(1-\psi)\theta^4(p-f)^6\), which is nonzero on the domain.

**Full observable-law criterion.** Under the required exchangeability \(X_1\leftrightarrow X_2\) and equality of all three one-assay marginals, the entire eight-cell law is determined by \(A,B,C,D\). Its probabilities, indexed by \((X_1,X_2,Y)\), are
\[
\begin{array}{ll}
 P_{111}=D,&P_{110}=B-D,\\
 P_{101}=P_{011}=C-D,&P_{100}=P_{010}=A-B-C+D,\\
 P_{001}=A-2C+D,&P_{000}=1-3A+B+2C-D.
\end{array}
\]
Thus for any genuine three-bit probability law, it belongs to the stated strictly interior model **if and only if** (i) those two exchangeability/marginal constraints hold, (ii) \(V>0\), \(\Delta>0\), and (iii) the displayed inverse yields \(0<f<p<1\), \(0<\psi,\theta<1\). Sufficiency holds because the inverted parameters reproduce \(A,B,C,D\), and these determine every cell. No independent non-negativity assumptions beyond the input's being a probability law are required.

**Sharp sampling boundary.** A single primary sample, however many of its assays are read, reveals only the product \(\psi\theta\), so cannot separate those two parameters. With one assay on each of three independent primary samples, each sample's conditional detection mean given site occupancy is \(g=f+\theta(p-f)\); the joint law therefore depends on \(\psi,f,g\) only, not separately on \(\theta,p\). With at most two assays there are either one or two primary samples. In the former case the preceding product confounding applies. In the latter case the exchangeable two-bit law depends only on the single mean \(A\) and cross moment \(C\): both are unchanged by nontrivial continuous parameter changes keeping \(f\), \(\psi\) and \(\theta(p-f)\) fixed. These exhaust the possible partitions of two or three assays among independent primary samples. Therefore two primary samples with assay counts two and one are minimally sufficient, and three total assays are necessary.

## Verification

The standalone standard-library program `verify_nested.py` enumerates each of the eight assay patterns directly through the hidden occupancy states using exact rational arithmetic, independently computes all four observable moments, reconstructs the full eight-cell law, verifies the algebraic inverse for 1,500 deterministic strictly interior parameter quadruples, and checks a displayed rational example and boundary counterexamples. It reports 12,004 passed exact-rational assertions. The program is a diagnostic replay of the explicit finite algebra; the quantified infinite-domain theorem rests on the proof above, not a finite enumeration.

For the illustrative parameters \((\psi,\theta,p,f)=(2/5,3/5,4/5,1/10)\), the observed moments are exactly
\[
 (A,B,C,D)=\left(\frac{67}{250},\frac{403}{2500},\frac{1427}{12500},\frac{10163}{125000}\right),
\]
and the inverse returns the original four parameters.

## Relationship to prior work

Royle and Link (2006) established false-positive and false-negative single-stage occupancy mixtures and their label-switching issue; it does not provide a two-primary-stage three-assay minimum or its four-moment inverse. Nichols et al. (2008) developed the multiscale occupancy framework using multiple methods under the no-false-positive assumption; its examples concern broader protocols rather than this unknown-\(f\) minimal asymmetric design. Chambert, Miller and Nichols (2015) examined false-positive occupancy designs incorporating known-truth information; the present claim instead uses a restricted error mechanism and three ambiguous outcomes per site.

Guillera-Arroita et al. (2017) developed a **more general** two-stage model with contamination at *both* the primary and assay stages and demonstrated its structural label ambiguities. It explicitly motivates careful identifiability checks. The present result is **not** a claim that their unrestricted five-parameter model can be identified without auxiliary information: it fixes primary-stage contamination at zero and assumes \(p>f\). Neither its general multimodal likelihood analysis nor the other inspected work states the exact minimal two-plus-one protocol, full four-moment inverse and attained-law characterization derived here. A prior derivation using equivalent finite-mixture moment methods is a remaining historical-priority possibility.

## Limitations

The known absence of primary-stage contamination is decisive. If primary samples can become positive at truly empty sites before the assay stage, the extra parameter changes the identifiability problem; the theorem cannot be applied. Shared PCR batch artifacts, correlated field samples, changing rates, unknown sample-specific probabilities, arbitrary site heterogeneity, or pooling of the three results into a single detection indicator also invalidate the stated forward law. Structural identifiability does not establish finite-sample estimability or precision; the exact Jacobian shows potential severe ill-conditioning. No independent scientific audit has been performed.

## References

- Royle, J. A., and Link, W. A. (2006). *Generalized site occupancy models allowing for false positive and false negative errors*. Ecology 87:835–841. First public date 2006-04-01. https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2
- Nichols, J. D., et al. (2008). *Multi-scale occupancy estimation and modelling using multiple detection methods*. Journal of Applied Ecology 45:1321–1329. First public date 2008-08-29. https://doi.org/10.1111/j.1365-2664.2008.01509.x
- Chambert, T., Miller, D. A. W., and Nichols, J. D. (2015). *Modeling false positive detections in species occurrence data under different study designs*. Ecology 96:332–339. https://doi.org/10.1890/14-1507.1
- Guillera-Arroita, G., et al. (2017). *Dealing with false-positive and false-negative errors about species occurrence at multiple levels*. Methods in Ecology and Evolution 8:1081–1091. First public date 2017-01-28. https://doi.org/10.1111/2041-210X.12743
