# Phase-shifted occupancy counts: positive dependence and a Gaussian circle kernel

## Finding
For an integer \(m\ge2\), draw \(n\ge0\) independent uniform points on the circle of circumference one. At each bin phase \(\theta\in[0,1)\), partition the circle into \(m\) equal, half-open arcs and let \(K_{m,n}(\theta)\) count arcs containing at least one point. For the fractional difference \(\alpha\in[0,1]\) between two phases, put \(q=1/m\). Their exact covariance is
\[
\begin{aligned}
C_{m,n}(\alpha)={}&m\left(1-(1+\alpha)q\right)^n+m\left(1-(2-\alpha)q\right)^n\\
&+m(m-2)(1-2q)^n-m^2(1-q)^{2n}.
\end{aligned}
\]
For every \(n\ge2\), this covariance is uniquely minimized at the half-bin phase \(\alpha=1/2\); it is strictly positive for \(m\ge3\), and for \(m=2\) vanishes only at that half-bin phase. The two occupied-bin counts are in fact exactly independent when \(m=2\) and \(\alpha=1/2\), for **every** sample size. The counts are deterministic when \(n\le1\).

Suppose \(m\to\infty\) and \(n=n_m\) satisfies \(n_m/m\to c\in(0,\infty)\). For any fixed phases \(\theta_1,\ldots,\theta_r\), the centered vector
\[
\left(\frac{K_{m,n_m}(\theta_j)-m[1-(1-1/m)^{n_m}]}{\sqrt m}\right)_{j=1}^r
\]
converges in law to a centered Gaussian vector with stationary covariance \(F_c(\{\theta_i-\theta_j\})\), where
\[
F_c(\alpha)=e^{-c(1+\alpha)}+e^{-c(2-\alpha)}-(2+c)e^{-2c},\quad 0\le\alpha\le1.
\]
This is **finite-dimensional convergence**, not a claimed functional weak-convergence theorem. The phase half-turn is asymptotically optimal and the strictly positive minimum is \(F_c(1/2)=e^{-2c}[2e^{c/2}-2-c]\). With \(\widehat F_c(k)=\int_0^1F_c(\alpha)e^{-2\pi ik\alpha}\,d\alpha\), every spectral coefficient is positive:
\[
\widehat F_c(0)=\frac{2e^{-c}(1-e^{-c})}{c}-(2+c)e^{-2c},\qquad
\widehat F_c(k)=\frac{2ce^{-c}(1-e^{-c})}{c^2+4\pi^2 k^2}\quad(k\in\mathbb Z\setminus\{0\}).
\]
Thus the limiting covariance is strictly positive definite at any finite set of distinct phases.

## Assumptions and scope
The points are iid uniform, the circle is identified with \(\mathbb R/\mathbb Z\), and the arcs are
\[
B_j(\theta)=\big[(j+\theta)/m,(j+\theta+1)/m\big)\pmod 1,
\quad j=0,\ldots,m-1.
\]
All observations use the *same* point sample; only the bin origin changes. The two phases coincide modulo one precisely when \(\alpha=0\) or \(1\). Endpoint conventions affect no probability since point locations are continuous. The exact statements apply for every \(m\ge2\), integer \(n\ge0\), and deterministic \(\alpha\in[0,1]\). In the limit statement, \(c\) is fixed strictly positive and \(r\) is fixed; there are no assertions for growing numbers of phases.

## Proof
**1. Exact second moments.** A specified bin is empty with probability \((1-q)^n\). For ordered bins from the two phase grids, exactly \(m\) pairs have common length \((1-\alpha)/m\), exactly \(m\) have common length \(\alpha/m\), and the remaining \(m(m-2)\) have empty intersection (zero-length boundary contact counts as disjoint). The probability that both bins are empty is \((1-\lvert B\cup B'\rvert)^n\), producing the displayed \(C_{m,n}\) after subtracting the product of the two mean vacancy counts. Passing from vacancies to occupancies does not change covariance.

**2. Universal sign and optimal stagger.** Put \(a=1-2q\ge0\). Binomial expansion gives the nonnegative identity
\[
\frac{C_{m,n}(\alpha)}m=
\sum_{k=2}^{n}\binom nk a^{n-k}q^k
\left[\alpha^k+(1-\alpha)^k-q^{k-1}\right].
\]
For \(k\ge2\), convexity gives \(\alpha^k+(1-\alpha)^k\ge2^{1-k}\ge q^{k-1}\). For \(m\ge3\) and \(n\ge2\), the \(k=2\) summand is strictly positive. When \(m=2\), the formula is zero only for \(\alpha=1/2\) (if \(n\ge2\)). The exact covariance is strictly convex in \(\alpha\) and symmetric about \(1/2\): differentiation twice of the two nonconstant powers gives a strictly positive second derivative for \(n\ge2\). Therefore its unique minimum is \(1/2\). In the \(m=2\) half-shift case, each point's membership in the two partitions gives two independent fair bits (the four quarter-circle intersections are equiprobable). Across independent points the two complete membership sequences are independent, hence so are the two occupied-bin counts.

**3. Gaussian finite-dimensional law.** Poissonize the sample, taking \(N\sim\operatorname{Poisson}(n_m)\), independent of an infinite iid uniform-point sequence, with \(c_m=n_m/m\). Split the circle into \(m\) unshifted elementary cells, retaining each cell's internal point process. These cell processes are independent, identically distributed, with bounded limiting intensity \(c_m\to c\). For any fixed list of phases, the vector of occupancy indicators for shifted bin \(j\), together with its unshifted-cell point count, depends only on elementary cells \(j\) and \(j+1\). It is consequently a stationary cyclic one-dependent triangular array with uniformly bounded moments of all fixed orders. Dropping one boundary term and separating the rest into growing blocks divided by one-cell gaps proves the multivariate central limit theorem by the ordinary independent-block Lyapunov theorem; the discarded centered gaps have variance \(o(m)\) when the block length tends to infinity sublinearly. The corresponding limiting Poisson-sample covariances per cell are
\[
G_c(\alpha)=e^{-c(1+\alpha)}+e^{-c(2-\alpha)}-2e^{-2c},\quad
\lim\frac{\operatorname{Cov}(K_{m,N}(\theta),N)}m=ce^{-c},\quad
\lim\frac{\operatorname{Var}(N)}m=c.
\]
The first formula follows from the two possible overlapping bin pairs; nonoverlapping Poisson-bin void events are independent. The other two follow from \(\operatorname{Cov}(\mathbf1_{\{P>0\}},P)=ce^{-c}\) for \(P\sim\operatorname{Poisson}(c)\).

For fixed phases, the sequential-addition coupling gives, jointly,
\[
K_{m,N}(\theta)-K_{m,n_m}(\theta)
=e^{-c}(N-n_m)+o_p(\sqrt m).
\]
Indeed \(\lvert N-n_m\rvert=O_p(\sqrt m)\); each sequential new point increases the occupied-bin count with conditional probability equal to the current empty-bin fraction. Throughout that window this fraction converges in probability to \(e^{-c}\), uniformly by monotonicity, the mean formula, and the \(O(m)\) vacancy variance. The centered increment martingale has variance at most the number of additions, hence contributes \(o_p(\sqrt m)\). The same argument handles deletion in reverse chronological order. Fixed- and Poisson-sample centering constants differ by \(O(1)\). Subtracting \(e^{-c}(N-n_m)/\sqrt m\) from the Poissonized joint Gaussian vector yields the fixed-size covariance \(G_c(\alpha)-ce^{-2c}=F_c(\alpha)\), as asserted.

**4. Spectrum.** Direct integration of the two exponential terms gives the stated Fourier coefficients. For \(c>0\), the nonzero-frequency coefficients are strictly positive. The zero coefficient is strictly positive because it is the average of \(F_c\), whose minimum \(e^{-2c}(2e^{c/2}-2-c)\) is positive by strict exponential convexity. These positive coefficients imply strict positive definiteness on finite distinct phase sets, by Fourier uniqueness for finite signed point measures.

**5. Phase-averaged occupancy and cyclic gaps.** If \(n\ge1\) and \(S_1,\ldots,S_n\) are the cyclic interpoint gaps, averaging the full-bin vacancy count over one complete phase period yields the deterministic identity
\[
\overline K_{m,n}:=\int_0^1K_{m,n}(\theta)\,d\theta
=m-\sum_{i=1}^n(mS_i-1)_+.
\]
For a gap of length \(S\), the mean number of complete moving bins inside it is precisely \((mS-1)_+\), by averaging lattice-point counts over the origin. Integrating the exact covariance gives
\[
\begin{aligned}
\operatorname{Var}(\overline K_{m,n})={}&\frac{2m^2}{n+1}\left[(1-1/m)^{n+1}-(1-2/m)^{n+1}\right]\\
&+m(m-2)(1-2/m)^n-m^2(1-1/m)^{2n}.
\end{aligned}
\]
In the proportional-load regime this variance divided by \(m\) tends to \(\widehat F_c(0)\), versus single-phase variance density \(F_c(0)=e^{-c}-(1+c)e^{-2c}\). This is a variance statement, not a separate claimed central limit theorem for the phase integral.

## Verification
The accompanying standalone `verify_phase.py` uses only Python's standard library. It enumerates equal-probability microcells to compare exact two-phase covariances with the formula for \(2\le m\le5\), \(0\le n\le4\), and shifts \(0,1/2,1/3,2/3\), checks the two-bin half-shift joint independence directly through six points, checks the circular-gap phase-integral identity on rational configurations, and verifies exact phase-integrated variance and selected limiting-kernel inequalities. Running `python verify_phase.py` reports 325 passed checks. Enumeration verifies only the finite tested cases; the general and asymptotic assertions follow from the proof above.

## Relationship to prior work
Scott's 1985 paper establishes the averaged-shifted-histogram construction and its integrated mean-squared-error theory for density estimation. It does not state the distribution of the **number of nonempty bins** across phase shifts or the dependence classification here. Barbour and Gnedin (first posted 25 September 2008) establish multivariate normal approximations for occupancy-frequency statistics in classical box schemes. Their de-Poissonization and normal-approximation framework is relevant background; their variables index load frequencies in a single fixed allocation and do not directly give a covariance kernel for bin partitions sharing and rearranging the same continuous sample. The present claim is the explicit phase-indexed occupancy law, its strict dependence/exception classification, and its Gaussian spectral limit—not a claim of inventing Poissonization, Gaussian occupancy limits, or averaged histograms. A stronger general occupancy-field theorem elsewhere could imply part of the result; independent priority review is still needed.

## Limitations
The Gaussian result is only finite-dimensional and assumes fixed positive load \(c\), not extreme sparse or dense scaling or growing phase families. Strict finite covariance does not imply distributional independence or association; full independence is proved only for the specified two-bin half-shift configuration. The uniform circle model has no boundaries or nonuniform sampling effects. Positive-definite Fourier coefficients concern the stated limiting kernel and do not by themselves prove sample-path convergence. The phase-average variance does not imply a phase-average central limit theorem. Numerical and exhaustive checks are finite and do not substitute for the asymptotic argument. Novelty is assessed against accessible literature and mathematical records, not independently certified.

## References
1. D. W. Scott, *Averaged Shifted Histograms: Effective Nonparametric Density Estimators in Several Dimensions*, Annals of Statistics 13 (1985), 1024–1040, doi:10.1214/aos/1176349654; full text: https://www.stat.cmu.edu/~rnugent/PCMI2016/papers/ScottASH.pdf.
2. A. D. Barbour and A. V. Gnedin, *Small counts in the infinite occupancy scheme*, arXiv:0809.4387v1, first posted 2008-09-25, https://arxiv.org/html/0809.4387v1.
3. D. W. Scott, *Averaged shifted histogram*, WIREs Computational Statistics 2 (2010), 160–164, doi:10.1002/wics.54.
