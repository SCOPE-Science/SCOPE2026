# Two sharp co-detection covariance reversals from at most three template copies

## Finding

**Theorem (finite-template aliquot sign phases).** Let \(N\) be a random integer taking values in \(\{0,1,2,3\}\), with an arbitrary fixed probability law. For each \(t\in(0,1/2)\), conditionally on \(N\), assign each of the \(N\) distinct target molecules independently to one of two labelled, disjoint assay aliquots with probability \(t\) each, or to unused extract with probability \(1-2t\). Define \(Y_j(t)=1\) exactly when aliquot \(j\) contains at least one target molecule; assume perfect amplification of present targets and no false positives. Set \(C(t)=\operatorname{Cov}(Y_1(t),Y_2(t))\).

Then \(C\) has **at most two distinct strict sign reversals** on \((0,1/2)\). If \(\Pr(N=3)=0\), there is at most one, and if \(\Pr(N\ge2)=0\), there are none. Both bounds are sharp with nonnegative laws having strictly positive probability on every integer in their claimed support. In particular, with

\[
\big(\Pr(N=0),\Pr(N=1),\Pr(N=2),\Pr(N=3)\big)
=\left(\frac14,\frac7{16},\frac1{32},\frac9{32}\right),
\]

\[
C(t)= -\frac{t^2}{1024}(9t-1)(9t^3-55t^2+167t-57).
\]

It is strictly negative at \(t=1/12\), zero at \(t=1/9\), strictly positive at \(t=1/8\) and \(t=3/8\), and strictly negative at \(t=2/5\); hence it has **exactly two** positive-aliquot-volume sign reversals, the second strictly between \(3/8\) and \(2/5\). For support restricted to \(\{0,1,2\}\), the law \((3/10,1/5,1/2)\) exhibits exactly one reversal at \(t=2/5\). Thus a maximum of three molecules in the extract is the sharp minimum permitting two reversals.

A complete criterion for exactly two interior reversals when \(\Pr(N\ge2)>0\) is also available: the strictly concave polynomial \(F\) defined below must have \(F(0)<0\), \(F(1/2)<0\), and a positive value at some interior point. These conditions are necessary and sufficient, including when one of the endpoint inequalities fails by equality (then two *strictly interior* reversals do not occur).

## Assumptions and scope

The randomness in \(N\) describes variation in the *finite number of molecules available in the common extract* across otherwise comparable samples; it is not independent resampling of a fresh Poisson population for every technical replicate. Conditional on \(N\), each molecule is physically placed in at most one aliquot. The two equal aliquots together occupy at most the full extract, hence \(0<t<1/2\). One may vary \(t\) across experimental designs while keeping the law of \(N\) fixed. All covariance statements concern the exact probability distribution over repeated independently prepared extracts, not noisy finite-sample estimates.

This is an idealized low-copy molecular-ecology model: no inhibition, shared assay failures, contamination, fragmentation, molecule clustering, PCR amplification competition, or correlated sampling-volume errors. The theorem is about a dependence diagnostic, not the probability of detecting an invasive species in a specific field sample.

## Proof

Let \(G(z)=\mathbb E[z^N]\) denote the probability-generating polynomial, and write

\[
\mu=\mathbb E[N],\qquad
v=\mathbb E[N(N-1)],\qquad
w=\mathbb E[N(N-1)(N-2)].
\]

Since \(N\le3\), the exact expansion is

\[
G(1-t)=1-\mu t+\frac v2t^2-\frac w6t^3.
\]

The probability of an empty specified aliquot is \(G(1-t)\), and the probability both aliquots are empty is \(G(1-2t)\). Inclusion–exclusion and the definition of covariance give the *exact*, nonasymptotic identity

\[
C(t)=G(1-2t)-G(1-t)^2=t^2F(t),
\]

where

\[
\begin{aligned}
F(t)={}&v-\mu^2+(\mu v-w)t
-\left(\frac{\mu w}{3}+\frac{v^2}{4}\right)t^2\\
&+\frac{vw}{6}t^3-\frac{w^2}{36}t^4.
\end{aligned}
\]

For the three-copy law, \(v=2\Pr(N=2)+6\Pr(N=3)\) and \(w=6\Pr(N=3)\), so \(v\ge w\ge0\). Consequently, for \(0\le t\le1/2\),

\[
\begin{aligned}
F''(t)&=-\frac{v^2}{2}-\frac{2\mu w}{3}+vw t-\frac{w^2t^2}{3}\\
&\le-\frac{v(v-w)}{2}-\frac{2\mu w}{3}-\frac{w^2t^2}{3}\le0.
\end{aligned}
\]

If \(\Pr(N\ge2)>0\), then \(F''(t)<0\): for \(w=0\) this follows from \(v>0\); for \(w>0\) it follows from \(\mu>0\). Therefore \(F\) is strictly concave. A strictly concave real function has at most two distinct zeros on any interval: three zeros \(t_1<t_2<t_3\) would contradict \(F(t_2)>0\), forced by strict concavity and \(F(t_1)=F(t_3)=0\). Because \(t^2>0\), the same upper bound holds for strict covariance sign reversals.

If \(N\le2\), put \(b=\Pr(N=1)\) and \(c=\Pr(N=2)\). The polynomial simplifies to

\[
F(t)=2c-(b+2c-ct)^2.
\]

For \(c>0\), its derivative \(2c(b+2c-ct)\) is strictly positive throughout \((0,1/2)\). Thus at most one zero is possible. If \(c=0\), \(F(t)=-b^2\le0\), proving no strict reversals for \(N\le1\).

For sharpness with \(N\le2\), choose probabilities \((3/10,1/5,1/2)\). The factorization is \(F(t)=1-(6/5-t/2)^2\), which changes sign from negative to positive exactly at \(t=2/5\).

For three copies, substitute the strictly positive four-point distribution in the Finding into \(G\) and expand to obtain the displayed exact factorization. Rational substitution gives

\[
F(1/12)=-\frac{25033}{2359296}<0,\quad
F(1/9)=0,\quad
F(1/8)=\frac{18927}{4194304}>0,
\]

\[
F(3/8)=\frac{15903}{4194304}>0,\qquad
F(2/5)=-\frac{2561}{640000}<0.
\]

Continuity supplies a second zero in \((3/8,2/5)\); strict concavity forbids any additional zeros. Both changes are genuine because the signs on either side are opposite.

Finally, strict concavity proves the stated complete two-reversal criterion: two strictly interior zero crossings force negative values at both endpoints and a positive interior maximum; conversely, those three signs force one root on either side of the positive interior point, and the two-root bound makes them unique. This proves the theorem for every allowed law, not merely the rational witnesses.

## Verification

The standalone, standard-library-only `check.py` recomputes the generating-function covariance, factorial-moment polynomial and curvature over all rational four-point distributions with denominator at most fifteen, at eight rational aliquot fractions; it also checks both exact witness factorizations, signs, and a per-molecule thinning identity. It reports **102,356 exact-rational assertions passed**. Its finite check is supplementary to the analytic proof above and does not establish the universal quantifiers by enumeration.

Run `python3 check.py` from the directory containing this file and the checker. There are no third-party Python dependencies or external files. The main evidence for strict global concavity is the displayed inequality, not the runtime test log.

## Relationship to prior work

Augustine and colleagues' 2024 eDNA copy-number work models conditional technical-replicate copy counts using Poisson laws and explains low-copy stochasticity, variable detectability, and inhibition. The present theorem instead conditions on a random **finite common-extract stock**, with two mutually exclusive physical aliquots; it determines the number of *volume-driven sign changes in their binary detection covariance*. The inspected model and discussion do not state the finite-three-copy curvature bound, its sharpness, or the two-switch witness.

Digital PCR partitioning theory as reviewed by Basu (2017), and the digital PCR variance analysis by Jacobs, Goetghebeur and Clement (2014), provide important established Poisson/binomial occupancy and measurement-variation machinery. The generating-function empty-aliquot identity is elementary and is **not** claimed as novel. The claimed distinction is the exact, sharp sign-transition classification under arbitrary three-copy input heterogeneity. The general fact that fixed-size multinomial categories may be negatively associated does not imply the result for randomly varying input \(N\), and previously established positive-covariance windows for exact-one occupancy counts under varying total draws use different events and control parameters.

## Limitations

No novelty claim is made for elementary probability-generating-function algebra or the general occupancy method. The finite-copy upper bound \(N\le3\), disjoint equal aliquots, exact binary readout, and fixed underlying \(N\) law are essential to this proof; the result does **not** bound the number of reversals for arbitrary unbounded copy distributions. Independent per-molecule amplification at constant efficiency \(e\in(0,1]\) merely replaces \(t\) by \(et\) in the formula, but may move one or both crossings beyond experimentally feasible aliquot fractions. Real inhibition and common laboratory errors are outside the theorem. A positive covariance window can arise from input-count mixture and should not be used alone to diagnose inhibition or contamination. No field validation, estimator precision, or causal inference is established. Historical priority remains provisional because exact equivalent formulas could exist in older random-occupancy literature that was not exhaustively available or indexed.

## References

1. Augustine, B. C., Hutchins, P. R., Jones, D. N., Williams, J. R., Leinonen, E., and Sepulveda, A. J. (2024). *A hierarchical model for eDNA fate and transport dynamics accommodating low concentration samples*. bioRxiv preprint, doi:10.1101/2024.03.27.586987. An associated public dataset was released 2024-03-27, doi:10.5061/dryad.8gtht76wc. Full study: *Environmental and Ecological Statistics*, doi:10.1007/s10651-024-00632-8.
2. Basu, A. S. (2017). *Digital Assays Part I: Partitioning Statistics and Digital PCR*. *SLAS Technology*, doi:10.1177/2472630317705680.
3. Jacobs, B. K. M., Goetghebeur, E., and Clement, L. (2014). *Impact of variance components on reliability of absolute quantification using digital PCR*. *BMC Bioinformatics* 15:283, doi:10.1186/1471-2105-15-283.
4. Barbour, A. D., and Gnedin, A. V. (2009). *Small counts in the infinite occupancy scheme*. *Electronic Journal of Probability* 14, 365–384, doi:10.1214/EJP.v14-608 (relevant general occupancy background; only abstract verified during comparison).
