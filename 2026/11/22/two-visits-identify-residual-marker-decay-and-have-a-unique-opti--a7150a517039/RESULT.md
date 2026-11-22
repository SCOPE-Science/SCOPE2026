# Two visits identify residual-marker decay and have a unique optimal revisit gap

## Finding

A pair of independent binary marker observations at a site, at times \(0\) and \(t>0\), suffices to identify the prevalence \(\psi\) of persistent occupancy, the initial residual-marker detection probability \(\alpha\) at empty sites, and its exponential disappearance rate \(\delta\), provided the true-positive probability \(q\) at occupied sites is known, strictly positive, and greater than \(\alpha\). All three unknown parameters have an explicit globally valid inverse from the four two-visit history probabilities. One binary visit at a common time does not suffice to identify all three.

At the important calibrated limit \(q=1\), the *locally D-optimal* separation of those two visits, for joint estimation of \((\psi,\alpha,\delta)\) across independently replicated sites, is unique and equals
\[
 t_*=\frac{2+W\!\left(2e^{-2}(1-\psi)\alpha^2/\psi\right)}{\delta},
\]
where \(W\) is the principal nonnegative real Lambert function satisfying \(W(x)e^{W(x)}=x\). In particular \(t_*>2/\delta\) for every admissible interior parameter point; the optimal gap decreases with occupancy prevalence, increases with initial residual detectability, and satisfies, as \(\psi\downarrow0\) with \(\alpha,\delta\) fixed,
\[
 \delta t_*=\log(1/\psi)-\log\log(1/\psi)+\log(2\alpha^2)+o(1).
\]
This is an exact benchmark for one known-occupied-detector-quality limit, not an assertion that eDNA assays or field conditions actually have perfect detection.

## Assumptions and scope

Independently sampled sites have a latent, time-constant status \(Z\in\{0,1\}\), with \(\Pr(Z=1)=\psi\in(0,1)\). Sites in status \(Z=1\) remain occupied throughout the experiment; their two binary assay outcomes are conditionally independent Bernoulli variables, each with *calibrated known* success probability \(q\in(0,1]\). At sites in status \(Z=0\), biological presence is absent but a residual marker can still trigger a detection. These outcomes are conditionally independent Bernoulli variables with success probabilities \(a_0=\alpha\) and \(a_t=\alpha e^{-\delta t}\), with \(0<\alpha<q\), \(\delta>0\), and prescribed \(t>0\). Conditional independence is an idealization even when a persistent physical marker is present; the assumed decay concerns *binary positive-test probability*, not necessarily the underlying molecular concentration. Sites are independent and use the same design. No new colonization, additional extinction, heterogeneous clearance, sampling depletion, background contamination, detection calibration error, varying sample duration, travel cost, deadline, or assay interaction is modeled.

The observed history is the pair \((Y_0,Y_t)\) rather than only an 'ever positive' flag. The design claim concerns the determinant of the per-site expected Fisher matrix for the **three unknown parameters** \((\psi,\alpha,\delta)\) with \(q=1\) known and both observation durations treated as instantaneous. The selected gap is locally optimal at a nominal parameter point, not a Bayesian or minimax optimum, and does not include any cost of waiting. The biological interpretation is best suited to controlled or approximately closed settings with persistent residual evidence, not rapidly flushed streams.

## Proof

Write \(a=\alpha\), \(b=\alpha e^{-\delta t}\), \(p=\psi\). Conditional independence gives four history probabilities, in order \((00,01,10,11)\):
\[
\begin{aligned}
P_{00}&=(1-p)(1-a)(1-b)+p(1-q)^2,\\
P_{01}&=(1-p)(1-a)b+p(1-q)q,\\
P_{10}&=(1-p)a(1-b)+pq(1-q),\\
P_{11}&=(1-p)ab+pq^2.
\end{aligned}
\tag{1}
\]
All are strictly positive on the stated domain. Let \(m_0=\Pr(Y_0=1)=P_{10}+P_{11}\), \(m_t=\Pr(Y_t=1)=P_{01}+P_{11}\), and \(c=P_{11}-m_0m_t\). The law of total covariance yields
\[
 m_0=pq+(1-p)a,\qquad m_t=pq+(1-p)b,\qquad
 c=p(1-p)(q-a)(q-b).
\tag{2}
\]
Because \(q>a>b\), all quantities \(c,q-m_0,q-m_t\) are positive. Define
\[
 R=\frac{c}{(q-m_0)(q-m_t)}.
\]
Then \(R=p/(1-p)\), giving the globally unique inverse
\[
 p=\frac{R}{1+R},\quad
 a=\frac{m_0-pq}{1-p},\quad
 b=\frac{m_t-pq}{1-p},\quad
 \delta=\frac{1}{t}\log\frac{a}{b}.
\tag{3}
\]
Thus two complete labeled binary histories identify all three parameters for any known \(q\in(0,1]\) on the specified domain. One visit at one common fixed date supplies only a Bernoulli probability, and hence cannot identify three continuous parameters on an open set.

For the D-optimum, set \(q=1\). The four cells in (1) simplify to
\[
(1-p)(1-a)(1-b),\quad (1-p)(1-a)b,\quad
(1-p)a(1-b),\quad p+(1-p)ab.
\]
For a strictly positive four-cell multinomial law with three free parameters and a differentiable invertible parameter map, its Fisher determinant equals the squared determinant of the Jacobian of any three independent cell probabilities divided by the product of all four cell probabilities. Direct differentiation of the first three cells with respect to \((p,a,b)\) yields
\[
 \det\frac{\partial(P_{00},P_{01},P_{10})}{\partial(p,a,b)}
 =(a-1)(b-1)(p-1)^2.
\]
Consequently the Fisher determinant for \((p,a,b)\) is
\[
 \frac{1-p}{ab\,[p+(1-p)ab]}.
\tag{4}
\]
The change of variables \((p,a,\delta)\mapsto(p,a,b)\) has Jacobian determinant \(-tb\). Multiplying (4) by \(t^2b^2\) therefore gives
\[
 D(t)=\det I_{(p,a,\delta)}(t)
 =\frac{(1-p)t^2e^{-\delta t}}
 {p+(1-p)a^2 e^{-\delta t}}.
\tag{5}
\]
This is strictly positive for every finite \(t>0\), and tends to zero as \(t\downarrow0\) or \(t\to\infty\). With \(z=\delta t\), \(C=(1-p)a^2/p>0\), differentiating the logarithm of (5) gives
\[
 \frac{d}{dz}\log D(z/\delta)=\frac{2}{z}-\frac{1}{1+Ce^{-z}}.
\tag{6}
\]
The first term strictly decreases from infinity to zero; the second strictly increases from \(1/(1+C)\) to one. Their difference has exactly one positive root, necessarily the unique global maximum. The stationarity equation is \(z=2(1+Ce^{-z})\), or \((z-2)e^{z-2}=2Ce^{-2}\), giving the displayed Lambert-\(W\) expression. Since \(C>0\), it is strictly larger than two. Monotonicity in \(p\) and \(a\) follows because \(C=(1-p)a^2/p\) is respectively strictly decreasing and strictly increasing, while \(W\) is strictly increasing on positive arguments.

For \(p\downarrow0\), the positive solution of \(we^w=x\) obeys \(W(x)=\log x-\log\log x+o(1)\) as \(x\to\infty\). Substituting \(x=2e^{-2}(1-p)a^2/p\), and cancelling the constant \(2\), gives the displayed two-term-with-constant rare-occupancy expansion. No approximation was used for the finite-parameter optimizer.

## Verification

Run `python3 check.py` with Python 3 and only its standard library. The checker uses exact rational arithmetic to reconstruct \((p,a,b)\) from the full two-visit law for known detector probabilities, and independently differentiates the four multinomial cells to verify (4) through a full Fisher-matrix determinant. It performs **1,296 exact rational checks** and **2,415 supplementary floating-point checks** of stationarity, global competitors and parameter monotonicity; it reports `PASS exact_fraction_checks=1296 numeric_checks=2415`. For example, at \(p=0.2\), \(a=0.6\), \(\delta=0.1\) in inverse-time units, the unique normalized optimum is \(\delta t_*=2.291275616944\ldots\), so \(t_*=22.912756169443\ldots\) time units. The proof, not those finite checks, establishes the unrestricted claim.

## Relationship to prior work

Royle and Link (2006) develop two-component occupancy mixtures with false-positive and false-negative observations; the **mixture representation itself is prior work**, not claimed new. The new assertion concerns an explicit inverse for time-varying *decaying* residual false positives from exactly two **labeled** visits when the occupied-site detection probability is calibrated, together with a full three-parameter determinant and its unique exact globally optimal revisit interval. Pilliod et al. (2013) document that residual eDNA can persist and decline over time in retained water, with substantial light- and temperature-dependence; their empirical design is not the statistical model (1) nor the derived design rule. Lahoz-Monfort, Guillera-Arroita and Tingley (2015) examine identifiability and bias in eDNA false-positive occupancy analysis with repeated assays and additional calibration; their author-hosted full text discusses time-constant replicate error assumptions, not a two-date exponential residual-marker design.

Two distinct nearby mathematical results also address different experiments. A published stationary two-state occupancy study optimizes a gap for estimating **Markov turnover** with imperfect true detections and no false detections; it does not estimate marker disappearance. A stationary deposition/clearance study optimizes the marker's **physical clearance rate** for instantaneous classification, rather than the time gap for estimating prevalence and the residual-decay rate. A separate two-visit detection-allocation result optimizes within-visit durations for unknown live-detection rates and constant false alarms; it does not impose the temporally decaying residual law (1). These comparisons are based on actual claims and material inspected, not shared vocabulary.

## Limitations

The true-positive assay probability \(q\) must be externally calibrated and must exceed the empty-site baseline \(\alpha\). The optimal revisit formula specifically requires \(q=1\); it is **not** claimed optimal for other fixed \(q\). Estimating \(q\) jointly would add an unknown parameter, so the three-parameter two-visit inverse need not survive. The ideal model's independent Bernoulli replicates may underestimate correlation caused by shared residual DNA. Exponential *detection probability* is stronger than the empirically better-supported exponential decay of DNA *concentration*, and saturation, thresholding, hydrological flushing and temperature can violate it. The time-constant occupancy assumption fails if colonization or extinction occurs between visits. Infinitely many independent sites are implicit in local Fisher-design interpretation; finite sample estimates may be unstable even though the distribution is identifiable. The model omits the cost of survey delay, which may override the formal optimum. Published general false-positive mixture theory might contain unnoticed equivalent specializations; accessible relevant full texts were inspected where available, but the 2006 foundational article's complete text was not obtained. The mathematical conclusions do not establish field-performance validity or exhaustive historical priority.

## References

1. Royle, J. A., and Link, W. A. (2006). *Generalized site occupancy models allowing for false positive and false negative errors.* Ecology 87, 835–841. First online 2006-04-01. https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2
2. Pilliod, D. S., Goldberg, C. S., Arkle, R. S., and Waits, L. P. (2013). *Factors influencing detection of eDNA from a stream-dwelling amphibian.* Molecular Ecology Resources 14, 109–116. First online 2013-08-12. https://doi.org/10.1111/1755-0998.12159
3. Lahoz-Monfort, J. J., Guillera-Arroita, G., and Tingley, R. (2015). *Statistical approaches to account for false-positive errors in environmental DNA samples.* Molecular Ecology Resources 16, 673–685. First online 2015-11-12. https://doi.org/10.1111/1755-0998.12486
4. *Detectability-dependent optimal revisit interval for a two-state ecological occupancy process.* Public result, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-detectability-dependent-optimal-revisit-interval-for-a-two-state--10edd02a8758
5. *A geometric-mean clearing law for indirect ecological occupancy markers.* Public result, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-geometric-mean-clearing-law-for-indirect-ecological-occupancy--a8b4c9a7e7cd
