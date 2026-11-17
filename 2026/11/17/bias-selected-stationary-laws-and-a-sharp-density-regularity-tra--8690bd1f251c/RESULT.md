# Bias-selected stationary laws and a sharp density-regularity transition in random doubling

## Finding
Let \(0<p<1\) and \(0<\alpha<1\). Independently at each step of an interval map, choose the dyadic expansion \(T(x)=2x\pmod 1\) with probability \(p\), the contraction \(B_0(x)=x/2\) with probability \((1-p)(1-\alpha)\), or \(B_1(x)=(x+1)/2\) with probability \((1-p)\alpha\). Write \(F=T_*\) and \(B=(1-\alpha)(B_0)_*+\alpha(B_1)_*\) for the induced Markov operators on Borel probabilities. Let \(\nu_\alpha\) be the distribution of \(\sum_{j\ge1}D_j2^{-j}\), where \(D_j\) are independent Bernoulli variables with \(\Pr(D_j=1)=\alpha\).

**Stationary probability phase transition.** If \(p\le1/2\), \(\nu_\alpha\) is the unique stationary Borel probability. If \(p>1/2\), put \(r=(1-p)/p\in(0,1)\). Every stationary Borel probability has the form
\[
\mathcal M_r(\rho)=(1-r)\sum_{k\ge0}r^k B^k\rho,
\qquad F\rho=\rho,
\]
and the correspondence from all \(T\)-invariant Borel probabilities \(\rho\) is a one-to-one affine correspondence onto all stationary probabilities. For biased branches \(\alpha\ne1/2\), this includes three mutually singular, full-support stationary probabilities: an absolutely continuous probability \(\mathcal M_r(\lambda)\), a singular-continuous probability \(\nu_\alpha\), and a purely atomic probability \(\mathcal M_r(\delta_0)\). Here \(\lambda\) denotes normalized Lebesgue measure and the atomic support is countable and dense.

**Sharp density-regularity diagram.** The absolutely continuous stationary probability \(\mathcal M_r(\lambda)\) is equivalent to \(\lambda\). If \(d_j(x)\in\{0,1\}\) are the ordinary binary digits of \(x\), its density is, almost everywhere,
\[
f_{p,\alpha}(x)=(1-r)\sum_{k=0}^{\infty}\prod_{j=1}^k 2r\,w_{d_j(x)},
\qquad w_0=1-\alpha,\quad w_1=\alpha.
\]
For every real \(s>1\), the exact criterion is
\[
\boxed{f_{p,\alpha}\in L^s(\lambda)\ \Longleftrightarrow\ \frac{[2r(1-\alpha)]^s+[2r\alpha]^s}{2}<1.}
\]
Its essential-boundedness criterion is
\[
\boxed{f_{p,\alpha}\in L^\infty(\lambda)\ \Longleftrightarrow\ 2r\max\{\alpha,1-\alpha\}<1.}
\]
For \(\alpha\ne1/2\), set \(m=\max\{\alpha,1-\alpha\}\) and \(p_\infty=2m/(1+2m)\). In the nonempty interval \(1/2<p<p_\infty\), there is a unique \(s_*>1\) where the displayed \(L^s\) criterion holds with equality; the density lies in \(L^s\) precisely for \(1\le s<s_*\). At the exact boundary \(p=p_\infty\), it belongs to every finite \(L^s\) but is not essentially bounded. Above this boundary it is bounded. For the unbiased case \(\alpha=1/2\), the density is identically one for every \(p>1/2\).

## Assumptions and scope
All measures are Borel probability measures on \([0,1)\), with its dyadic binary representation taking the terminating-zero expansion at dyadic rationals. The map \(T(x)=2x\pmod1\) and two affine contractions are exact, and choices are independent of the current state and across times. Branch weights satisfy \(p\in(0,1)\), \(\alpha\in(0,1)\); endpoint weights are excluded. Stationarity means \(pF\mu+(1-p)B\mu=\mu\), with no assumption that \(\mu\) has a density. Full support refers to topological support relative to \([0,1)\); an atomic distribution may have dense support. The \(L^s\) statement concerns the explicitly selected absolutely continuous law \(\mathcal M_r(\lambda)\), not all stationary laws in the expanding regime.

## Proof
**1. Algebraic identities and the invariant Bernoulli measure.** Applying \(T\) after either inverse branch gives the identity, so \(FB=I\) on signed measures. Under \(\nu_\alpha\), binary digits are independent Bernoulli \((\alpha)\); shifting the digit sequence preserves its distribution, as does prepending an independent digit with the same bias. Thus \(F\nu_\alpha=B\nu_\alpha=\nu_\alpha\), and \(\nu_\alpha\) is stationary for all \(p\).

**2. Complete stationary simplex.** Assume first \(p>0\) and write \(r=(1-p)/p\). Stationarity is equivalent to \((1+r)\mu=F\mu+rB\mu\). Applying \(F\) and using \(FB=I\) gives
\[
F^{n+1}\mu-F^n\mu=r(F^n\mu-F^{n-1}\mu),\qquad n\ge1.
\]
In particular,
\[
F^n\mu=\mu+\left(\sum_{j=0}^{n-1}r^j\right)(F\mu-\mu).
\]
If \(r\ge1\), bounded total-variation norms of all probability measures \(F^n\mu\) force \(F\mu=\mu\). Stationarity then forces \(B\mu=\mu\). For any initial probability \(\eta\), the first \(k\) binary digits under \(B^k\eta\) are independent newly prepended Bernoulli digits. Consequently, every fixed finite binary cylinder eventually has exactly its \(\nu_\alpha\)-probability, and a \(B\)-invariant probability must equal \(\nu_\alpha\), since these cylinders generate the Borel sigma-field. This proves uniqueness when \(p\le1/2\), including the equality case and all singular initial laws.

Suppose instead that \(0<r<1\). The geometric recurrence for \(F^n\mu\) converges in signed total variation to a probability \(\rho\) satisfying \(F\rho=\rho\). From the displayed formula,
\[
\rho=\frac{F\mu-r\mu}{1-r},\qquad
\mu=(1-r)\rho+rB\mu.
\]
Iterating the second identity gives \(\mu=(1-r)\sum_{k\ge0}r^kB^k\rho\), because the discarded remainder has total mass \(r^{N+1}\) after \(N+1\) iterations. Conversely, if \(F\rho=\rho\), then the convergent geometric series \(\mathcal M_r(\rho)\) satisfies
\[
F\mathcal M_r(\rho)=(1-r)\rho+r\mathcal M_r(\rho),\quad
\mathcal M_r(\rho)=(1-r)\rho+rB\mathcal M_r(\rho),
\]
which imply stationarity. The inverse \(\rho=(F\mu-r\mu)/(1-r)\) proves uniqueness of the seed. The assertion is an affine bijection of Borel-probability simplices, with no weak-topology continuity assertion at the discontinuities of the interval doubling map.

**3. Three distinct types.** Both \(\lambda\) and \(\delta_0\) are \(F\)-invariant. The measure \(\mathcal M_r(\delta_0)\) is a countable mixture of measures on finite dyadic grids, hence purely atomic; the union of those grids is dense because \(0<\alpha<1\) and \(r>0\). In contrast, \(\nu_\alpha\) has no atoms: its mass on every fixed length-\(k\) binary cell is at most \(\max\{\alpha,1-\alpha\}^k\to0\). It assigns positive probability to each binary cylinder, so has full support. For \(\alpha\ne1/2\), the law of large numbers gives binary-one frequency \(\alpha\) for \(\nu_\alpha\)-almost every point and frequency \(1/2\) for \(\lambda\)-almost every point; hence \(\nu_\alpha\perp\lambda\). The density construction below makes \(\mathcal M_r(\lambda)\) equivalent to \(\lambda\); the atomic law is singular to both nonatomic laws. This gives three pairwise singular stationary types.

**4. Explicit density.** The measure \(B^k\lambda\) is constant on each binary length-\(k\) cylinder: the mass of a cylinder with digits \(d_1,\ldots,d_k\) is \(\prod_{j=1}^k w_{d_j}\) and its length is \(2^{-k}\). Thus its density is \(2^k\prod_{j=1}^k w_{d_j(x)}\) almost everywhere. Inserting these densities in the nonnegative geometric series yields the displayed \(f_{p,\alpha}\). Each summand integrates to \((1-r)r^k\), so monotone convergence shows \(\int_0^1f_{p,\alpha}\,dx=1\) and finiteness almost everywhere. The \(k=0\) summand equals \(1-r>0\), proving equivalence to Lebesgue measure.

**5. Sharp \(L^s\) and boundedness thresholds.** Under \(\lambda\), the binary digits \(d_j\) are independent fair bits. Put \(A_j(x)=2r\,w_{d_j(x)}\) and \(Z_k=\prod_{j=1}^kA_j\), with \(Z_0=1\). For each real \(s>1\), independence gives
\[
\mathbb E_\lambda[Z_k^s]=M_s^k,\qquad
M_s=\tfrac12\big([2r(1-\alpha)]^s+[2r\alpha]^s\big).
\]
If \(M_s<1\), the triangle inequality in \(L^s\) gives
\[
\|f_{p,\alpha}\|_s\le(1-r)\sum_{k\ge0}\|Z_k\|_s
=(1-r)\sum_{k\ge0}M_s^{k/s}<\infty.
\]
If \(M_s\ge1\), for every \(N\) positivity and \((\sum_{k=0}^N Z_k)^s\ge\sum_{k=0}^N Z_k^s\) imply
\[
\int_0^1f_{p,\alpha}^s\,dx\ge(1-r)^s\sum_{k=0}^NM_s^k\longrightarrow\infty.
\]
Thus equality is genuinely excluded. If \(A_{\max}=2r\max\{\alpha,1-\alpha\}<1\), the geometric bound \(f\le(1-r)/(1-A_{\max})\) holds pointwise outside dyadic exceptions. If \(A_{\max}\ge1\), for each \(N\) the cylinder whose first \(N\) bits all have the maximally weighted value has positive Lebesgue measure and on it \(f\ge(1-r)\sum_{k=0}^N A_{\max}^k\). These lower bounds are arbitrarily large, even at \(A_{\max}=1\), proving failure of essential boundedness. When \(\alpha\ne1/2\), \(M_1=r<1\) and \(s\mapsto M_s\) is strictly convex. For \(A_{\max}>1\) it diverges as \(s\to\infty\), giving a unique threshold \(s_*>1\). At \(A_{\max}=1\), the other multiplier is strictly less than one, hence \(M_s<1\) at every finite \(s\); above the threshold both multipliers are strictly less than one. If \(\alpha=1/2\), then \(B\lambda=\lambda\), so \(f\equiv1\). All boundary statements follow.

## Verification
The accompanying standalone Python 3 checker, `checks/checker.py`, evaluates stationarity on every binary cylinder through length eight for six rational parameter pairs, using exact fractions. Its two cylinder computations independently use (i) the complete geometric-mixture distribution and (ii) the expansion and biased-prepending Markov transitions. It also checks normalization, one-digit masses, moment multipliers, and the rational \(L^\infty\) boundary \((p,\alpha)=(8/13,4/5)\). The generated output `checks/output.txt` records 3,066 exact cylinder equalities plus auxiliary algebraic tests, all passing. These finite checks are diagnostic only: the infinite stationary-simplex and integrability claims are proved in Steps 1–5, not established by finite cylinders.

## Relationship to prior work
Homburg and Kalle (arXiv:2207.09987v1, 2022) introduced the expanding/contracting interval model and explicitly restricted inverse-branch selections to equal weights. Their Section 4.2 identifies general selection probabilities and determining stationary measures as natural questions. Their analysis focuses on two-point motions and related invariant measures, not the branch-biased one-point density-regularity phase diagram proved here. The original model and its equal-branch Haar stationarity are credited to them.

An earlier published treatment, *Sharp stationary-simplex collapse for forward/inverse circle dynamics* (2026), gives a complete stationary-measure classification for the **uniform** inverse-branch averaging kernel, including its geometric-series parametrization. Its recurrence and stationary-simplex mechanism are explicitly acknowledged; neither that mechanism nor the unbiased specialization is claimed novel here. The distinct contribution is the biased branch-selection family, its coexisting regularity types, and especially the exact moment threshold and finite-\(L^s\)/unbounded-density boundary. Another related study, *Time-reversal covariance duality and a critical Gaussian crossover in affine random maps* (2026), treats the uniform-branch coordinate covariance, not biased stationary-density integrability. A published study of random symmetric doubling maps (2026) analyzes biased switching between different *expanding* maps and zero-digit cylinder laws, not the present expansion/biased-inverse process.

Homburg, Kalle, Ruziboev, Verbitskiy and Zeegers (2021 preprint/2022 journal) treat a distinct superattracting random intermittent map and its density \(L^s\) irregularity; that result does not cover the present binary-prepending Markov kernel. General multiplicative-product and Markov-operator techniques underlie the proof, and wider uncatalogued transfer-operator results could implicitly subsume portions of it; this is a remaining priority risk.

## Limitations
The classification applies only to the stated exact dyadic expansion and independently biased binary inverse branches; unequal expansion/contraction bases, state-dependent switching, nonstationary noise and two-point motions are not covered. The pointwise density formula ignores the Lebesgue-null ambiguous binary-expansion set. The extremal stationary probabilities correspond bijectively to ergodic \(T\)-invariant seed measures, but no explicit enumeration is claimed. Regularity conclusions concern the canonical absolutely continuous selected law, not every stationary law. The proof uses standard product-moment estimates, and priority relative to all possible general operator theory is not established by database searches alone. Independent mathematical review remains outstanding.

## References
1. A. J. Homburg and C. Kalle, *Iterated function systems of affine expanding and contracting maps on the unit interval*, arXiv:2207.09987v1, first public 2022-07-20, Sections 1 and 4.2. https://arxiv.org/abs/2207.09987
2. *Sharp stationary-simplex collapse for forward/inverse circle dynamics* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-stationary-simplex-collapse-for-forward-inverse-circle-dyn--71b02d2fe828 .
3. *Time-reversal covariance duality and a critical Gaussian crossover in affine random maps* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-time-reversal-covariance-duality-and-a-critical-gaussian-crossov--06e9a4996e78 .
4. *Exact eventual geometric zero cylinders and a bias-driven logarithmic edge transition* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-eventual-geometric-zero-cylinders-and-a-bias-driven-logari--559e8ce0b358 .
5. A. J. Homburg, C. Kalle, M. Ruziboev, E. Verbitskiy and B. Zeegers, *Critical intermittency in random interval maps*, arXiv:2107.02556 (2021). https://arxiv.org/abs/2107.02556
