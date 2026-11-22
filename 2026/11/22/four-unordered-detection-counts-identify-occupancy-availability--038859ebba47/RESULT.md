# Four unordered detection counts identify occupancy, availability persistence, and sensitivity

## Finding

For the stationary, positively autocorrelated two-state site-use model defined below, the **distribution of the total number of detections in four consecutive equally spaced surveys**, without the order of those detections, uniquely determines the four unknown probabilities: site occupancy, conditional site-use prevalence, detection sensitivity, and site-use temporal memory. Four surveys are sharp: three surveys admit distinct strictly interior parameter quadruples with **exactly the same complete count distribution**. The inverse is explicit up to two nested strictly monotone scalar equations, with a computable exact feasibility test. The two moment-shape invariants have an everywhere nonzero Jacobian inside the positive-memory parameter domain, whose determinant vanishes quadratically as persistence approaches one.

## Assumptions and scope

A randomly chosen site is occupied for the entire survey sequence with probability \(\psi\in(0,1)\); if unoccupied, it generates no detections. Conditional on occupancy, let \(W_j\in\{0,1\}\) indicate local availability for survey \(j\). This stationary first-order Markov chain has availability probability \(\pi\in(0,1)\) and positive memory \(r\in(0,1)\), with
\[
\Pr(W_{j+1}=1\mid W_j=0)=\pi(1-r),\qquad
\Pr(W_{j+1}=1\mid W_j=1)=\pi+(1-\pi)r.
\]
Conditional on the entire availability history, survey detections are independent; the detection probability is \(p\in(0,1)\) if \(W_j=1\), and zero otherwise. Parameters and survey conditions are homogeneous across sites and occasions. One observes only \(N_n=\sum_{j=1}^nY_j\), the count per site, and knows its exact distribution across independent sites. A site identifier is retained only to accumulate its total number of detections across occasions; the within-site temporal order is then discarded. This is population-level structural identifiability, not an assertion about finite-sample estimability.

For \(n=4\), set \(q_k=\Pr(N_4=k)\) for \(k=0,\ldots,4\), and define four positive binomial moments
\[
E_k=\mathbb E\binom{N_4}{k}=\sum_{j=k}^4\binom jkq_j,\qquad k=1,2,3,4.
\]
The bijective reparameterization \(t=r(1-\pi)/\pi>0\) and \(z=\pi p>0\) gives
\[
\begin{aligned}
E_1&=\psi zF_1,&F_1&=4,\\
E_2&=\psi z^2F_2,&F_2&=6+t(3+2r+r^2),\\
E_3&=\psi z^3F_3,&F_3&=2(1+t)(2+t(1+r)),\\
E_4&=\psi z^4F_4,&F_4&=(1+t)^3.
\end{aligned}
\]
For a candidate exact count histogram define
\[
R=\frac{E_1E_3}{E_2^2},\qquad U=\frac{E_2E_4}{E_3^2}.
\]
An exact feasibility-and-identification procedure is: (i) require \(4/9<R<8/9\); (ii) solve \(R=4F_3/F_2^2\), \(U=F_2F_4/F_3^2\) for \((t,r)\in(0,\infty)\times(0,1)\); (iii) require the recovered probabilities
\[
z=\frac{4E_2}{E_1F_2},\quad \pi=\frac{r}{r+t},\quad
p=\frac z\pi,\quad \psi=\frac{E_1}{4z}
\]
to all lie strictly between zero and one. Then the histogram is feasible and the solution is unique. The two shape equations have **at most one** interior solution; if neither exists, the histogram is infeasible. This procedure does not assert that every histogram with \(4/9<R<8/9\) is feasible.

## Proof

**Moment identities.** Under the stationary chain, for ordered indices \(i_1<\cdots<i_k\),
\[
\mathbb E\!\left[\prod_{h=1}^kW_{i_h}\right]
=\pi\prod_{h=1}^{k-1}\left[\pi+(1-\pi)r^{i_{h+1}-i_h}\right].
\]
Multiplying by \(\psi p^k\) yields the detection-product moments. Summing over all \(k\)-subsets of \(\{1,2,3,4\}\) gives the displayed \(E_k\). In particular the six pairs have gaps occurring with multiplicities \(3,2,1\), the four triples consist of two consecutive triples and two with one gap of length two, and the fourfold event is consecutive. These observations establish every coefficient of \(F_1,\ldots,F_4\) without an asymptotic approximation.

**Global uniqueness of the shape.** Write \(L_1=\log(4F_3/F_2^2)\) and \(L_2=\log(F_2F_4/F_3^2)\), and abbreviate \(B=2+t(1+r)\), \(C=6+t(r^2+2r+3)\). Direct differentiation gives
\[
\frac{\partial L_1}{\partial t}=
\frac{(1-r)[r^2t+6rt+4r+3t+6]}{(1+t)BC}>0
\]
and the exact Jacobian determinant
\[
J=\frac{\partial(L_1,L_2)}{\partial(t,r)}
=-\frac{3t(1-r)^2}{(1+t)BC}<0.
\]
For each fixed \(r\in(0,1)\), \(R(t,r)\) strictly increases from \(4/9\) as \(t\downarrow0\) to
\[
R_\infty(r)=\frac{8(1+r)}{(r^2+2r+3)^2}
\]
as \(t\to\infty\). The function \(R_\infty\) strictly decreases from \(8/9\) to \(4/9\) as \(r\) ranges from zero to one: its derivative has numerator proportional to \(-3r^2-6r-1\). Thus, for any attainable fixed \(R\), the admissible \(r\)-values form one connected interval \((0,r_*)\), where \(R_\infty(r_*)=R\), and there is exactly one smooth \(t=t(r)>0\) on that interval.

Along this curve,
\[
\frac{dL_2}{dr}\bigg|_{L_1\text{ fixed}}
=\frac{J}{\partial L_1/\partial t}<0.
\]
Consequently two distinct points cannot have the same \((R,U)\). The displayed formulas then recover \(\pi,p,\psi\) uniquely. Four binomial moments are an invertible linear transformation of the four independent probabilities \(q_1,\ldots,q_4\), with \(q_0=1-\sum_{k=1}^4q_k\); thus the same recovered moments also reproduce the entire count law. These observations prove the identification and feasibility statements.

**Sharp three-survey obstruction.** For \(n=3\) the corresponding moments are
\[
E_1^{(3)}=3\psi z,\qquad
E_2^{(3)}=\psi z^2[3+t(2+r)],\qquad
E_3^{(3)}=\psi z^3(1+t)^2.
\]
The two strictly interior parameter choices
\[
(\psi,\pi,p,r)=\left(\tfrac35,\tfrac25,\tfrac34,\tfrac12\right)
\quad\text{and}\quad
(\psi,\pi,p,r)=\left(\tfrac{48}{65},\tfrac{13}{38},\tfrac{57}{80},\tfrac35\right)
\]
have **exactly** the same three moments \(\left(27/50,1053/4000,3969/80000\right)\), hence the same full law of \(N_3\), but different four-survey laws. More generally, fixing an interior three-survey law leaves a local continuous ambiguity: with \(K=\sqrt{E_1^{(3)}E_3^{(3)}/(3(E_2^{(3)})^2)}\), choose nearby \(r\) and set
\[
t=\frac{1-3K}{K(2+r)-1},\quad z=\frac{3E_2^{(3)}}{E_1^{(3)}[3+t(2+r)]},\quad
\psi=\frac{E_1^{(3)}}{3z},\quad \pi=\frac r{r+t},\quad p=\frac z\pi.
\]
All probabilities remain interior for sufficiently small changes, and the three binomial moments remain fixed. Counts from one or two occasions have fewer than four degrees of freedom and cannot globally identify an open four-parameter family. Therefore four consecutive count-only surveys are sharp.

**Boundary qualification.** If \(r=0\), conditional site-use states are independent, and the observation law depends on \(\pi,p\) only through their product \(z=\pi p\); they cannot be separated by any number of these count-only surveys. If \(r=1\), the availability state never switches and the observation law depends on occupancy and availability through \(\psi\pi\); again distinct parameter sets are observationally equivalent. These two boundary cases are excluded. The Jacobian identity quantifies loss of invertibility as \(r\uparrow1\) (holding \(t\) fixed), and as \(r\downarrow0\) along physical paths with fixed interior \(\pi\).

## Verification

The standalone standard-library program `check.py` directly enumerates the latent Markov path distribution, verifies the moment identities with exact rational arithmetic, checks the strict three-survey ambiguity by exact rational equality, tests four-survey inversion on a reproducible set of interior parameter tuples, and checks the rational Jacobian formula on an exact grid. Its run reported 4,768 successful supplementary assertions. The analytic proof above, rather than finite tests, establishes uniqueness for all interior parameters. To reproduce, run `python check.py` alongside this document.

## Relationship to prior work

Goldstein et al. (2024) analyze temporally correlated camera-trap detection using a latent Markov site-use process and emphasize biases from ignoring serial dependence. Hines et al. (2010, 2014) developed correlated-replicate occupancy models. Cole (2019) studies structural identifiability of general hidden Markov models using complete ordered data. These models and methods are relevant precursors; the present result specifies the exact *unordered count-only*, four-occasion global injectivity and sharp obstruction for the homogeneous positive-memory, zero-inflated occupancy model. It does not claim to invent the ecological model, hidden Markov parameterization, factorial moments, or the general idea of identifiability.

A separate published three-count result for a **known-occupied** site concerns only availability and detector parameters, without the additional unknown structural occupancy probability. Published full-history identifiability results use more information than the per-site count. Neither statement, as identified in the accessible materials, supplies the present four-count theorem. An earlier equivalent special case elsewhere in algebraic statistics or Markov-binomial mixture theory remains possible.

## Limitations

Only the exact distribution of counts in four homogeneous successive survey occasions is treated; finite samples introduce uncertainty, especially near zero memory, near unit persistence, or small probabilities. The proof assumes no false positives, conditional independence of detectors, stationary availability given occupancy, positive serial correlation, and constant site-level parameters. It does not cover heterogeneous populations, arbitrarily spaced occasions, negative autocorrelation, observation noise in probabilities, or robustness of plug-in estimates. No ecological field data have been used to validate the model or the inverse. The mathematical conclusion concerns structural identifiability, not finite-data sample size or sampling-cost optimality.

## References

1. Goldstein, B. R., et al. (2024), *Guidelines for estimating occupancy from autocorrelated camera trap detections*, Methods in Ecology and Evolution 15, 1177–1191. First online 31 May 2024. https://doi.org/10.1111/2041-210X.14359
2. Hines, J. E., et al. (2010), *Tigers on trails: occupancy modeling for cluster sampling*, Ecological Applications 20, 1456–1466. https://doi.org/10.1890/09-0321.1
3. Hines, J. E., Nichols, J. D., and Collazo, J. A. (2014), *Multiseason occupancy models for correlated replicate surveys*, Methods in Ecology and Evolution 5, 583–591. https://doi.org/10.1111/2041-210X.12186
4. Cole, D. J. (2019), *Parameter redundancy and identifiability in hidden Markov models*, METRON 77, 105–118. https://doi.org/10.1007/s40300-019-00156-3
5. Schönhuth, A. (2011/2013), *Generic identification of binary-valued hidden Markov processes*, arXiv:1101.3712. https://arxiv.org/abs/1101.3712
