# Equal mean-square risk conceals an atomic-to-singular divide in fresh minibatch reshuffling

## Finding

**Theorem (fresh versus frozen minibatch partitions).** Let \(n=mb\) with integers \(m\ge 2\), \(b\ge1\), and fixed real numbers \(y_1,\ldots,y_n\) satisfying \(\sum_{i=1}^n y_i=0\). Minimize the strongly convex scalar finite sum
\[
F(x)=\frac1n\sum_{i=1}^n \frac12(x-y_i)^2
\]
by constant-step minibatch random reshuffling, with the average component gradient in each batch and \(0<\eta<2\). Compare (A) a uniformly random size-\(b\) partition drawn once and held fixed, with a new uniform batch order each epoch, to (B) a new independent uniform partition and batch order at every epoch. Take the same deterministic epoch-start iterate \(X_0=x_0\).

Write \(q=1-\eta\), \(s^2=n^{-1}\sum_i y_i^2\), \(v_b=s^2(n-b)/[b(n-1)]\), and
\[
\Gamma_m(q)=\frac{m}{m-1}\sum_{j=0}^{m-1}q^{2j}
-\frac1{m-1}\left(\sum_{j=0}^{m-1}q^j\right)^2.
\]
Then for **every** finite epoch count \(k\ge0\), the two protocols have identical unconditional first and second moments:
\[
\mathbb E X_k=q^{mk}x_0,
\qquad
\operatorname{Var}(X_k)=\eta^2 v_b\Gamma_m(q)
\frac{1-q^{2mk}}{1-q^{2m}}.
\]
This equality does **not** imply that their laws agree.

The distinction is sharp already on the smallest data size allowing nontrivial equal-size batches: \(n=4\), \(b=2\), and centers \((y_1,y_2,y_3,y_4)=(1,1,-1,-1)\). Put \(r=(1-\eta)^2\), \(\delta=\eta^2\). At completed epochs protocol B has the exact autoregression
\[
X_{k+1}=rX_k+\delta D_k,
\qquad
\Pr(D_k=0)=\frac23,
\quad\Pr(D_k=1)=\Pr(D_k=-1)=\frac16,
\]
with independent digits, whereas protocol A has probability \(2/3\) of drawing a partition on which the iteration converges deterministically to zero, and probability \(1/3\) of drawing a partition on which the epoch noise is a symmetric \(\pm\delta\) sign.

Both protocols have the same unconditional stationary variance \(\delta^2/[3(1-r^2)]\) and the same expected objective gap \(\delta^2/[6(1-r^2)]\). However, if \(0<r\le1/3\), the *annealed* stationary law of protocol A has an atom of mass exactly \(2/3\) at the true minimizer \(0\), while protocol B has **no atoms**. For \(0<r<1/3\), protocol B has a three-map Cantor support of Hausdorff dimension \(\log3/\log(1/r)\), and its stationary measure is exact-dimensional with dimension
\[
\frac{\log3-\tfrac13\log2}{\log(1/r)}.
\]
At the critical value \(r=1/3\), protocol B instead has **full interval support** \([-3\delta/2,3\delta/2]\), but its stationary measure remains singular continuous, of exact dimension \(1-\log2/(3\log3)\).

Despite this singularity, protocol B has exactly Gaussian centered fourth moment for *every* \(0<\eta<2\):
\[
\mathbb E X_\infty^4=3(\mathbb E X_\infty^2)^2,
\qquad
\kappa_6(X_\infty)=-\frac{2\delta^6}{9(1-r^6)}\ne0.
\]
Here \(\kappa_6\) denotes the sixth cumulant. Thus even a correct variance and zero excess kurtosis do not diagnose this singular stationary distribution.

## Assumptions and scope

A *uniform partition* means the partition induced by uniformly permuting the \(n\) labeled data points, cutting the permutation into consecutive blocks of size \(b\), and forgetting block order; each epoch's subsequent block order is independent and uniform. The frozen protocol samples this partition once; the fresh protocol samples an independent partition each epoch. All conditional expectations under the frozen protocol average over both the initial random partition and the subsequent random block orders. The first- and second-moment equality requires common component curvature \(1\); heterogeneous curvatures are not included. The stationary-law comparison starts from any deterministic \(x_0\) and refers to convergence **in distribution** of completed epoch iterates, not almost-sure convergence of a persistent stochastic trajectory.

For the four-center example, the singularity assertions require \(0<r\le1/3\), equivalently \(\eta\in[1-1/\sqrt3,1)\cup(1,1+1/\sqrt3]\). The exceptional exact-local-solve point \(\eta=1\), where \(r=0\), has a discrete rather than continuous stationary law. The fourth- and sixth-cumulant identities hold throughout \(0<\eta<2\), including that exception.

## Proof

**1. Exact epoch noise.** A batch whose center average is \(z\) makes the update \(x\mapsto qx+\eta z\). For the ordered batch means \(Z_1,\ldots,Z_m\), one epoch therefore gives
\[
X_{k+1}=q^m X_k+N_k,
\quad
N_k=\eta\sum_{j=1}^m q^{m-j}Z_j.
\]
The batch means sum to zero and are exchangeable under a uniform order. Let \(v_{\mathcal P}=m^{-1}\sum_{j=1}^m Z_j^2\) for a fixed partition \(\mathcal P\). Then, conditional on \(\mathcal P\), \(\mathbb E Z_j=0\), \(\operatorname{Var}(Z_j)=v_{\mathcal P}\), and for distinct positions \(i,j\), \(\operatorname{Cov}(Z_i,Z_j)=-v_{\mathcal P}/(m-1)\), the last identity following by taking the variance of \(\sum_j Z_j=0\). Consequently
\[
\mathbb E[N_k\mid\mathcal P]=0,
\qquad
\operatorname{Var}(N_k\mid\mathcal P)=\eta^2 v_{\mathcal P}\Gamma_m(q).
\]

**2. Exact partition average and all-horizon equality.** For independent positions of a random size-\(b\) subset drawn without replacement from centered data, pair inclusion probabilities are \(b/n\) and \(b(b-1)/[n(n-1)]\). Expanding the square of the batch mean gives
\[
\mathbb E_{\mathcal P} v_{\mathcal P}
=\frac{n-b}{b(n-1)}\,\frac1n\sum_{i=1}^n y_i^2=v_b.
\]
For a frozen partition, uniform orders in distinct epochs are conditionally independent given \(\mathcal P\). Their mean is zero and their conditional variance is the constant above. For a fresh partition, the epoch noises are independent, centered, and have variance \(\eta^2v_b\Gamma_m(q)\). Applying the affine recursion and averaging the frozen conditional second moment over \(\mathcal P\) gives in both cases
\[
\mathbb E X_k=q^{mk}x_0,
\quad
\operatorname{Var}(X_k)
=\eta^2v_b\Gamma_m(q)\sum_{j=0}^{k-1}q^{2mj}.
\]
Because \(|q|<1\), summing the geometric series proves the finite-time identity and its stationary limit. This calculation does not equate any higher moments or full distributions.

**3. The four-center noise laws.** There are exactly three equiprobable unordered pair partitions: one pairs the two \(+1\) centers and the two \(-1\) centers, and two pair opposite centers in each block. In the latter two partitions every batch gradient is \(x\), hence \(X_{k+1}=rX_k\) and the stationary law is \(\delta_0\). In the first partition, two uniform orders of batch centers \((+1,-1)\) yield
\[
X_{k+1}=rX_k+\delta \xi_k,
\qquad\Pr(\xi_k=1)=\Pr(\xi_k=-1)=1/2.
\]
Fresh repartitioning independently draws one of all six partition/order outcomes each epoch, giving the displayed three-digit distribution. Uniqueness of invariant laws and convergence in distribution follow by iterating affine contractions with \(0\le r<1\). Explicitly, the fresh stationary law is
\[
X_\infty\stackrel d=\delta\sum_{j=0}^{\infty}r^jD_j.
\]
The frozen annealed stationary law is \((2/3)\delta_0+(1/3)\mathcal L(\delta\sum_{j\ge0}r^j\xi_j)\). As \(\mathbb ED^2=1/3\), both stationary variances are \(\delta^2/[3(1-r^2)]\). Since \(F(x)-F(0)=x^2/2\), their stationary expected objective gaps are also equal.

**4. Support and singularity.** Let \(K_r\) be the fresh support and \(M=\delta/(1-r)\). It is the unique compact invariant set for the three contractions \(x\mapsto rx-d\), \(x\mapsto rx\), \(x\mapsto rx+d\), where \(d=\delta\), within \([-M,M]\). Adjacent images of this enclosing interval are separated by an open gap of length
\[
\delta-2rM=\delta\frac{1-3r}{1-r}.
\]
Thus for \(0<r<1/3\) all three images are disjoint; standard elementary similarity coverings (or the open-set condition) give \(\dim_H K_r=\log3/\log(1/r)\). For the Bernoulli weights \((1/6,2/3,1/6)\), the strong law applied to the symbolic cylinder probabilities yields the exact local measure dimension \(H/\log(1/r)\), where
\[
H=-\frac13\log\frac16-\frac23\log\frac23
=\log3-\frac13\log2.
\]
The maximal depth-\(k\) cylinder mass is \((2/3)^k\), proving nonatomicity under separation.

At \(r=1/3\), the three image intervals touch end-to-end and cover \([-3\delta/2,3\delta/2]\), hence this interval is the entire support. Under the affine normalization from that interval to \([0,1]\), the stationary law has a ternary expansion with independent digits \(0,1,2\) of probabilities \((1/6,2/3,1/6)\). By the strong law, its typical digit frequencies differ from \((1/3,1/3,1/3)\), which are the digit frequencies of Lebesgue-almost every point; therefore it is singular. At most two ternary codes represent any point, each cylinder mass tends to zero, so it has no atoms. The same cylinder-frequency argument gives exact dimension \(H/\log3\). The frozen aligned two-sign law has no atom at zero when \(r\le1/3\), because its first sign dominates the remaining tail whenever \(r<1/2\). Therefore the frozen annealed atom at zero has mass exactly \(2/3\).

**5. Gaussian fourth moment without Gaussianity.** The centered three-digit law has \(\mathbb ED^2=\mathbb ED^4=\mathbb ED^6=1/3\) and odd moments zero. Hence \(\kappa_4(D)=1/3-3(1/3)^2=0\) and \(\kappa_6(D)=1/3-15(1/3)^2+30(1/3)^3=-2/9\). Cumulants of independent summands add and scale homogeneously. Applying this to the absolutely convergent bounded series gives \(\kappa_4(X_\infty)=0\) and
\[
\kappa_6(X_\infty)=\delta^6\kappa_6(D)\sum_{j\ge0}r^{6j}=-\frac{2\delta^6}{9(1-r^6)}.
\]
Since the mean vanishes, the vanishing fourth cumulant is exactly the displayed Gaussian fourth-moment identity. The negative sixth cumulant proves that the law is not Gaussian, independently of its singular-support classification.

## Verification

The companion standard-library checker `verify.py` enumerates all ordered balanced batchings of three centered datasets of sizes four and six, including two- and three-batch configurations. It verifies the exact epoch-noise mean and variance, the all-horizon geometric second-moment formula on rational test steps, the six partition/order outcomes in the minimal four-component example, and the rational interval separation criterion. Run `python3 verify.py`; it prints `VERIFY_OK 236`. These 236 exact arithmetic checks guard the finite formulas only. Existence and uniqueness of invariant laws, the infinite series, fractal dimensions, and singularity at the critical value follow analytically from the proof, not from finite enumeration.

## Relationship to prior work

Kumar (2026) studies **frozen partitions** with a new random order each epoch, proving a batch-variance identity and transferring random-reshuffling convergence bounds; its conclusion expressly identifies **fresh partitioning each epoch** as a distinct open problem. The finite-population identity in Step 2 is not claimed new. Ying, Yuan, Vlaski and Sayed (2018) establish mean-square performance of constant-step reshuffling, without a fresh-versus-frozen partition distribution theorem. Published mathematical records on two- and three-sample Bernoulli-convolution laws for **unbatched** reshuffling establish related self-similar support transitions, but do not imply the four-sample partition mixture or the equality of all finite-epoch second moments across the two partition policies. The self-similar-set and entropy-dimension principles themselves are standard and are not claimed new. The claim here is the explicit fresh-versus-frozen stochastic optimization separation, including the minimal four-component realization and its full-support singular threshold despite matched second moments and Gaussian kurtosis.

## Limitations

This is an exact benchmark, not a general answer to the 2026 open problem of convergence-rate dominance under fresh repartitioning. The all-horizon equality uses scalar equal curvature; different sample Hessians need not share it. The qualitative singularity classification is established for the four-center construction only and for \(0<r\le1/3\). It concerns laws of completed epochs, not within-epoch iterates or pathwise convergence to a fixed random point. Fixed partition probabilities average over a partition chosen once; conditioning on a particular partition produces a different risk. The results have not undergone independent mathematical audit or exhaustive historical-priority verification.

## References

1. R. Kumar, *Minibatch Random Reshuffling for Smooth Convex Optimization: Batch-Size Dependence, Finite-Population Variance, and Quadratic Growth*, Optimization Online, first public listing 2026-11-11. https://optimization-online.org/wp-content/uploads/2026/11/minibatch_rr.pdf
2. B. Ying, K. Yuan, S. Vlaski and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964, first posted 2018-03-21. https://arxiv.org/abs/1803.07964
3. C. Domingo-Enrich, *Computing the Variance of Shuffling Stochastic Gradient Algorithms via Power Spectral Density Analysis*, arXiv:2206.00632, first posted 2022-06-01. https://arxiv.org/abs/2206.00632
4. *Random reshuffling has a Cantor-to-interval stationary-support transition*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-random-reshuffling-has-a-cantor-to-interval-stationary-support-t--ec57811b8333
5. *Exact separation and interval-filling thresholds for three-sample random reshuffling*, published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-separation-and-interval-filling-thresholds-for-three-sampl--1bb9343a7e6c
6. J. E. Hutchinson, *Fractals and self-similarity*, Indiana University Mathematics Journal 30 (1981), 713–747.
