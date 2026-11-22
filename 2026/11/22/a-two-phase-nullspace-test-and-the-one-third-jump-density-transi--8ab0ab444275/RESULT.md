# A two-phase nullspace test and the one-third jump-density transition for a missing Fourier pair

## Finding
Let \(n\ge6\) be even, let \(1\le k<n/2\) with \(\gcd(k,n)=1\), and observe every discrete Fourier coefficient of a real \(n\)-periodic signal except the conjugate pair at frequencies \(k\) and \(n-k\). Recover a signal by minimizing cyclic total variation among signals agreeing with the observations.

For \(0\le s\le n\), define the following completely explicit finite quantity. For \(\epsilon\in\{0,1\}\), sort the \(n\) numbers
\[
 z_j^{(\epsilon)}=\left|\cos\frac{(2j+\epsilon)\pi}{n}\right|,\qquad 0\le j<n,
\]
in nonincreasing order as \(z_{(1)}^{(\epsilon)}\ge\cdots\ge z_{(n)}^{(\epsilon)}\), and put
\[
 \rho_n(s)=\max_{\epsilon\in\{0,1\}}
 \frac{\sum_{j=1}^{s}z_{(j)}^{(\epsilon)}}{\sum_{j=1}^{n}z_{(j)}^{(\epsilon)}}.
\]
Then **every** real signal with at most \(s\) nonzero cyclic differences is the **unique** total-variation-minimizing reconstruction if and only if \(\rho_n(s)<1/2\). If \(\rho_n(s)\ge1/2\), an explicit real signal with at most \(s\) jumps fails uniqueness (and is not minimizing when the inequality is strict). The criterion is independent of the primitive missing frequency \(k\).

Writing \(s_n\) for the first failing sparsity level, the exact finite test has the universal sharp asymptotic
\[
 \lim_{\substack{n\to\infty\\n\ \mathrm{even}}}\frac{s_n}{n}=\frac13.
\]
More precisely, whenever \(s/n\to p\in[0,1]\),
\[
 \rho_n(s)\longrightarrow\sin\!\left(\frac{\pi p}{2}\right).
\]
The fraction \(1/3\) separates uniform uniqueness from the existence of adversarial sparse-jump signals in the large-grid limit.

## Assumptions and scope
Indices are modulo \(n\). The discrete Fourier transform is \(\widehat x(\ell)=\sum_{j=0}^{n-1}x_j e^{-2\pi i\ell j/n}\), and \((Dx)_j=x_{j+1}-x_j\). Cyclic variation is \(\operatorname{TV}(x)=\sum_j |(Dx)_j|\). Measurements include the zero frequency, so the mean is fixed. The reconstruction program is
\[
 \min_{u\in\mathbb R^n}\operatorname{TV}(u)
 \quad\text{subject to}\quad
 \widehat u(\ell)=\widehat x(\ell)\ \text{for all }\ell\notin\{k,n-k\}.
\]
The evenness and coprimality hypotheses are substantive; no claim is made for odd grids, nonprimitive missing frequencies, noisy data, or nonperiodic variation.

## Proof
**1. Reduction to the two-dimensional invisible subspace.** A real perturbation preserving the observations has the form
\[
 h_j=A\cos(2\pi kj/n)+B\sin(2\pi kj/n).
\]
Since the discrete-difference multiplier at \(k\) is nonzero, its gradient \(y=Dh\) ranges over all nonzero scalar multiples of \(\cos(2\pi kj/n+\phi)\). Coprimality permutes the sample phases, and \(n\) even implies \(k\) odd and \(y_{j+n/2}=-y_j\).

**2. The exact nullspace condition.** If \(S\) supports \(Dx\), the triangle inequality gives
\[
 \operatorname{TV}(x+h)-\operatorname{TV}(x)
 \ge\|y_{S^c}\|_1-\|y_S\|_1.
\]
The largest possible ratio \(\|y_S\|_1/\|y\|_1\), over every phase and every \(S\) of size at most \(s\), is the concentration ratio \(R_n(s)\) formed from the largest \(s\) absolute samples of \(\cos(2\pi j/n+\phi)\). Thus \(R_n(s)<1/2\) proves strict uniqueness for all such signals.

Conversely, suppose \(R_n(s)\ge1/2\). At a maximizing phase select the \(s\) largest magnitudes, making sure to include an antipodal pair among the largest tied values; this is possible since opposite samples have equal absolute values. The nonzero selected samples therefore contain both signs. Choose a zero-sum gradient \(g\) supported on this set, with signs opposite to the selected nonzero entries of \(y\): for example, give all selected positive-\(y\) sites the same negative magnitude equal to the number of selected negative-\(y\) sites, and vice versa. Every zero-sum cyclic gradient is \(Dx\) for some real \(x\). For sufficiently small \(t>0\),
\[
 \operatorname{TV}(x+th)-\operatorname{TV}(x)
 =t\bigl(\|y\|_1-2\|y_S\|_1\bigr)\le0.
\]
Strict inequality disproves minimization; equality yields a distinct feasible minimizer with the same objective if \(x\) is minimizing, or already disproves the assertion otherwise. For \(s\le1\), only constant signals have at most one nonzero cyclic difference, and \(R_n(s)<1/2\). This proves equivalence of the uniform-recovery statement and \(R_n(s)<1/2\).

**3. Why only two phases suffice.** For any fixed subset and fixed signs of the cosines, both the sum of its absolute cosines and the full absolute-cosine sum are linear combinations of \(\cos\phi\) and \(\sin\phi\). Their positive-denominator quotient has derivative of constant sign on each interval where the ordering and signs remain fixed. Such intervals can end only at a cosine zero or at a magnitude tie. Writing \(\theta_j=2\pi j/n\), the nonidentical ties obey
\[
 \sin(2\phi+\theta_j+\theta_\ell)=0,
\]
and zeros obey \(\phi+\theta_j\equiv\pi/2\pmod\pi\). Because \(n\) is even, every such breakpoint is an integer multiple of \(\pi/n\). The phase shift \(2\pi/n\) merely permutes the samples. Hence the global maximum occurs at \(\phi=0\) or \(\phi=\pi/n\), exactly giving \(R_n(s)=\rho_n(s)\).

**4. The sharp one-third limit.** For any sequence \(s/n\to p\), the equally spaced absolute cosines converge in empirical distribution to \(|\cos\Theta|\) with \(\Theta\) uniform on \([0,2\pi]\). This also controls sums of the largest \(s\) values: use the identity
\[
 \sum_{j=1}^s z_{(j)}=
 \min_{0\le a\le1}\left(sa+\sum_{j=1}^n(z_j-a)_+\right).
\]
The Riemann sums converge uniformly in \(a\), as \((|\cos\theta|-a)_+\) is uniformly Lipschitz in both \(a\) and \(\theta\). The upper \(p\) fraction of \(|\cos\Theta|\) has threshold \(\cos(\pi p/2)\); its share of the total absolute-cosine integral is \(\sin(\pi p/2)\). The same limit holds for the two endpoint phases, giving the asserted limit of \(\rho_n(s)\). Since \(\sin(\pi p/2)\) is strictly increasing and equals \(1/2\) precisely at \(p=1/3\), the first failure index satisfies \(s_n/n\to1/3\).

## Verification
The standalone standard-library script `checker.py` independently computes both endpoint ratios, tests random intermediate phases, checks that primitive missing frequencies permute the sample magnitudes, examines representative large-grid limits, and constructs explicit signed zero-sum gradients witnessing non-recovery at finite thresholds. In one execution it completed 89,056 finite consistency comparisons. These checks are not an infinite proof; the exact reduction and limit follow analytically above.

For illustration, at \(n=6\), \(k=1\), the invisible gradient with phase zero is \((1,1/2,-1/2,-1,-1/2,1/2)\). Its two antipodal unit-magnitude entries carry exactly half its \(\ell_1\)-mass, so uniform uniqueness already fails at two jumps.

## Relationship to prior work
Candès, Romberg and Tao (2006) derive random partial-Fourier sparse/TV recovery guarantees; Cai and Xu (2013 preprint) study total-variation recovery under Gaussian measurements and general phase transitions; Poon (2014 preprint) studies (mostly random) partial Fourier sampling and gradient-sparse recovery. This result instead treats a deterministic, almost-complete Fourier measurement set with exactly one deleted conjugate frequency pair, obtaining an exact finite nullspace test and an explicit sharp limiting jump density. A direct published-equivalence search did not establish that these specific conclusions are consequences of the compared statements. The underlying nullspace inequality is standard; the two-phase reduction and sharp single-erasure law are the asserted contribution.

## Limitations
The theorem is about **uniform noiseless uniqueness**, not stochastic recovery, reconstruction error under noise, or the optimal recovery of a particular signal beyond its jump count. It gives an exact finite trigonometric criterion and the asymptotic critical density, but does not assert a simplified closed-form integer threshold at every finite dimension. Potential unindexed or inaccessible treatments of the same deterministic erasure case remain a historical-priority risk. No independent mathematical audit has been performed.

## References
1. C. Poon, *On the role of total variation in compressed sensing*, arXiv:1407.5339 (initial posting 2014-07-20); SIAM J. Imaging Sci. 8 (2015), 682–720, DOI: https://doi.org/10.1137/140978569.
2. J.-F. Cai and W. Xu, *Guarantees of Total Variation Minimization for Signal Recovery*, arXiv:1301.6791 (initial posting 2013-01-28); Inform. Inference 4 (2015), 328–353, DOI: https://doi.org/10.1093/imaiai/iav009.
3. Q. Sun, *Sparse approximation property and stable recovery of sparse signals from noisy measurements*, arXiv:1107.5203 (2011), for classical sparse-recovery context.
4. E. J. Candès, J. Romberg and T. Tao, *Robust Uncertainty Principles: Exact Signal Reconstruction from Highly Incomplete Frequency Information*, IEEE Trans. Inform. Theory 52 (2006), 489–509, DOI: https://doi.org/10.1109/TIT.2005.862083.
