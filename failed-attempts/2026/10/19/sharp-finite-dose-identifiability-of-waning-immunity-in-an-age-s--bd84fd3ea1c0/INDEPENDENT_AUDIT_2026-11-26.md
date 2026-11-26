# Independent mathematical audit

## correctness

PASS

Yang–Saldaña–Scoglio's Eq. (4) matches the forward map with R=R_0 and a,b the two known means. Indeed the endemic susceptible level is 1/R, the infected and recovered levels are Phi/R times a and K(v), and the vaccinated level is b v times the sum of susceptible and recovered levels. Mass conservation gives the stated transform inversion on the strict subcritical range. For normalized hyperexponentials the Stieltjes-transform difference is O(v^-2); clearing denominators of degree at most 2k gives numerator degree at most 2k-2. Thus 2k-1 distinct samples force equality and poles/residues identify the actual component count, rates and weights. At an interior exactly-k mixture, a dependence of the normalization-and-panel Jacobian would give a Cauchy rational combination with k distinct double zeros and, after clearing denominators, degree at most 2k-2; it must vanish and its coefficients then vanish. The implicit-function theorem yields a nontrivial local fiber of distinct positive mixtures with ordered rates. At k=1 one sample suffices and zero cannot identify the rate. For general densities L=1-vK is analytic on Re v>0; equality on an open subinterval determines the compact moment sequence of e^-T and hence the law. For a finite panel, normalization, first moment and panel Laplace samples are finitely many linear functionals on smooth compactly supported bumps; a nonzero kernel perturbation of the unit exponential, small on its compact support, preserves positivity, finite mean and a smooth positive hazard. This is an analytic proof of the smooth-law case: the archived check.py was inspected, not executed, and its rational example uses atomic durations, illustrative only. All claims are structural under fixed known R,a,b, not stability statements.

## originality

FAIL

The sharp sample boundary is mechanically equivalent to the classical polynomial-moment information boundary for k-node Gaussian quadrature. Combined with the exact, already published forward equilibrium formula, this covers the mathematical core without needing a separately worded epidemiology theorem. The full-curve and equal-mean finite-panel extensions are direct Laplace determination and finite-rank kernel arguments, respectively. This is a finding of mathematical implication and no established distinct remainder, not a claim that the combined SIRVS wording has been previously published.

## value

FAIL

A finite sample boundary for waning is a natural inverse question. However, in the frozen setting the known forward map exactly deconvolves each noiseless measurement, the cutoff is a classical quadrature information boundary in a reweighted basis, and the smooth ambiguity is the usual finite-dimensional kernel obstruction. No substantive new inference phenomenon, stability result, or model constraint beyond these routine consequences is established. The decision is not based on requiring noisy-data results in general.

The dated certificate retains the supplied scientific assessment, sources and limitations.
