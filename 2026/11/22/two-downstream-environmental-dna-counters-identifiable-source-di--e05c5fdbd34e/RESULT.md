# Two downstream environmental-DNA counters: identifiable source distance and a universal distant-source sensor gap

## Finding

**Theorem (known-pool environmental-DNA source localization).** Let \(m\ge2\), \(0<a_1<a_2<\cdots<a_m\), and \(c_j>0\) be fixed and known. Put
\[
g(u)=\sum_{j=1}^m c_j e^{-a_j u},\qquad u\ge0.
\]
A source is located an unknown distance \(x\ge0\) above an upstream counting station. At two stations separated by a design distance \(h>0\), the counts are independent Poisson variables with means \(Qg(x)\) and \(Qg(x+h)\), respectively, where the total source scale \(Q>0\) is unknown. Under this model:

1. **Two-station identifiability.** For every \(h>0\), the pair of population means uniquely determines both \(x\) and \(Q\). Indeed the downstream/upstream mean ratio strictly increases with \(x\) from \(g(h)/g(0)\) to the unattained upper limit \(e^{-a_1h}\). This assertion concerns the probability law, not error-free recovery from one noisy pair of counts.
2. **Information and optimal separation.** After treating \(Q\) as a nuisance parameter, the local Fisher information for \(x\) is
\[
\mathcal I(x,h)=Q\frac{g(x)g(x+h)}{g(x)+g(x+h)}\left(H(x)-H(x+h)\right)^2,
\qquad H(u)=-\frac{g'(u)}{g(u)}.
\]
It is positive for \(h>0\), vanishes in both limits \(h\downarrow0\) and \(h\to\infty\), and therefore attains its maximum at an interior separation.
3. **Universal distant-source limit.** Write \(a=a_1\) and \(\delta=a_2-a_1>0\). As \(x\to\infty\), uniformly for \(h\) in any compact subset of \((0,\infty)\),
\[
\boxed{\mathcal I(x,h)=Q\frac{c_2^2}{c_1}\delta^2 e^{-(a+2\delta)x}
\left(\frac{(1-e^{-\delta h})^2}{1+e^{a h}}+o(1)\right).}
\]
For all sufficiently large \(x\), there is exactly one globally information-maximizing sensor separation \(h_x\), and \(h_x\to h_*\). The limit \(h_*>0\) is the unique solution of
\[
\boxed{\frac{2\delta}{e^{\delta h_*}-1}=\frac{a}{1+e^{-a h_*}}.}
\]
In particular, the distant-source optimal separation depends only on the two slowest attenuation rates, not on any mixture weights or faster rates. The information itself decays at exponent \(a+2\delta=2a_2-a_1\), strictly faster than the leading mean-count attenuation exponent \(a\).
4. **Sharp assumptions.** A single exponential component gives a constant interstation ratio and exactly zero information about \(x\) when \(Q\) is unknown. Moreover, if the relative source-pool amplitudes are also unrestricted unknown positives, even the *entire* exact downstream concentration curve is compatible with distinct source locations: the shift in \(x\) can be absorbed into the individual pool amplitudes. Thus the calibrated-shape assumption is essential.

## Assumptions and scope

The source is upstream of both sensors on one idealized unidirectional homogeneous reach. Attenuation acts independently on \(m\) strictly distinct noninterconverting pools, with known positive relative weights \(c_j\) and distinct strictly positive loss rates per unit *distance* \(a_j\). The absolute release scale \(Q\) is unknown but constant across the two observations. There is no other contributing source, no additional downstream shedding, and no longitudinally varying dilution, flow or extraction efficiency. The counting efforts are fixed and equal and are included in \(Q\); conditional Poisson sampling is independent at the two sites. The physical location constraint is \(x\ge0\); design separations satisfy \(h>0\). The theorem is a model-conditional, noiseless-parameter identifiability and local-information statement, not a guarantee of accurate inference in field conditions.

## Proof

**Step 1: strict ratio monotonicity.** Define positive weights \(w_j(u)=c_je^{-a_ju}/g(u)\). Then \(H(u)=\sum_j w_j(u)a_j\) and direct differentiation gives
\[
H'(u)=-\left(\sum_jw_j(u)a_j^2-\left[\sum_jw_j(u)a_j\right]^2\right)<0.
\]
The strict inequality holds at every finite \(u\) because at least two distinct rates have positive weight. Hence
\[
\frac{d}{dx}\log\frac{g(x+h)}{g(x)}=H(x)-H(x+h)>0.
\]
Taking \(x=0\) and \(x\to\infty\) proves the stated feasible ratio interval and unique inversion for \(x\), after which \(Q=\mu_0/g(x)\).

**Step 2: nuisance-profile information.** The two mean derivatives in the \(x\) coordinate equal \(-QH(x)g(x)\) and \(-QH(x+h)g(x+h)\); in the \(Q\) coordinate they are \(g(x)\) and \(g(x+h)\). The independent-Poisson Fisher matrix has
\[
\mathcal J_{xx}=Q\sum_{s\in\{0,h\}}g(x+s)H(x+s)^2,\quad
\mathcal J_{xQ}=-\sum_{s\in\{0,h\}}g(x+s)H(x+s),\quad
\mathcal J_{QQ}=\frac{g(x)+g(x+h)}{Q}.
\]
Its Schur complement \(\mathcal J_{xx}-\mathcal J_{xQ}^2/\mathcal J_{QQ}\) is precisely \(\mathcal I(x,h)\). This calculation only prescribes local information about the two-parameter statistical model; it does not claim any finite-sample optimal estimator.

**Step 3: a positive pair expansion.** Define \(z_j=c_j e^{-a_jx}\), \(g_0=\sum_jz_j\), and \(g_1=\sum_jz_je^{-a_jh}\). Direct pairing shows
\[
g_0g_1\bigl(H(x)-H(x+h)\bigr)=
\sum_{1\le i<j\le m}(a_j-a_i)z_i z_j\left(e^{-a_i h}-e^{-a_j h}\right)>0.
\]
Consequently \(\mathcal I\) is strictly positive for \(h>0\). Its limit at \(h=0\) is zero by continuity; as \(h\to\infty\), \(g_1\to0\) and the hazard difference stays bounded, so \(\mathcal I\to0\). Compactness and continuity therefore give at least one maximizer in \((0,\infty)\).

**Step 4: asymptotics.** For fixed \(h>0\), retain the two slowest terms in the pair sum. The leading pair is \((1,2)\), whose contribution equals
\[
\delta c_1c_2e^{-(2a+\delta)x}e^{-ah}(1-e^{-\delta h}).
\]
The denominators satisfy \(g_0=c_1e^{-ax}[1+o(1)]\) and \(g_1=c_1e^{-a(x+h)}[1+o(1)]\), giving the claimed information asymptotic. The expansions hold with their first two \(h\)-derivatives uniformly on compact sets. The remainder is \(O(e^{-\eta x})\), with \(\eta=\delta\) when \(m=2\), and \(\eta=\min\{\delta,a_3-a_2\}\) when \(m\ge3\).

**Step 5: global compactness and eventual uniqueness.** Because \(H(x)-a\le C e^{-\delta x}\) and \(\sup_{u\ge x}|H'(u)|\le C e^{-\delta x}\), uniformly for large \(x\), the normalized information \(e^{(a+2\delta)x}\mathcal I(x,h)\) is bounded by \(C_1 h^2\) near \(h=0\) and by \(C_2e^{-ah}\) for large \(h\). Choose a fixed positive \(h\) for which the limiting profile is positive. These two uniform boundary bounds force every global maximizer, for all sufficiently large \(x\), into one fixed compact subinterval of \((0,\infty)\).

The limiting profile \(f(h)=(1-e^{-\delta h})^2/(1+e^{ah})\) has logarithmic derivative
\[
\frac{f'(h)}{f(h)}=\frac{2\delta}{e^{\delta h}-1}-\frac{a}{1+e^{-ah}}.
\]
Its first term decreases strictly from infinity to zero, and its second term increases strictly from \(a/2\) to \(a\). Thus \(f\) has one positive, nondegenerate strict global maximum \(h_*\). Uniform convergence on the compact and strict separation away from that maximum imply all normalized-information global maximizers converge to \(h_*\). Since \(f''(h_*)<0\), uniform convergence of the second derivatives makes \(\mathcal I(x,\cdot)\) strictly concave in a neighborhood containing all maximizers for sufficiently large \(x\). Hence exactly one global optimizer then exists, proving the remaining assertion.

**Step 6: uncalibrated mixture boundary.** With independently unknown positive source amplitudes \(q_j\), the downstream means are \(\sum_jq_j e^{-a_j(x+s)}\). For any alternative \(x'\ge0\), take \(q'_j=q_j e^{a_j(x'-x)}>0\). Then \(q'_j e^{-a_j(x'+s)}=q_j e^{-a_j(x+s)}\) for all \(s\ge0\), so all downstream sensors produce the same means. For \(m=1\), the ratio itself is \(e^{-a_1h}\), independent of \(x\).

## Verification

The included standard-library-only \(\texttt{verify.py}\) is a supplementary finite checker. Run \(\texttt{python3 verify.py}\) after extracting it. It checks the exact rational example, positive pair expansion against the independent Poisson Schur complement for 2,500 randomly selected heterogeneous cases, ratio monotonicity, numerical optimal separations, and long-source-distance normalization. Finite numerical checks do not establish the theorem; the analytic steps above establish its universal quantifiers.

With \(a_1=1\), \(a_2=2\), \(c_1=c_2=1\), \(x=h=\log2\), and \(Q=16\), the two population means are exactly \(12\) and \(5\), their ratio is \(5/12\), and the efficient Fisher information is \(16/255\). The distant-source optimal gap is
\[
h_*=\log\left(\frac{3+\sqrt{17}}{2}\right)\approx1.27019663313689.
\]

## Relationship to prior work

Van Driessche et al. [1, 2] document strong interactions among eDNA source biomass, river discharge, and distance and experimentally observe nonmonotone downstream concentrations. Their data were publicly deposited before the journal publication. This motivates careful source-location benchmarks but their full article and appendices do **not** establish the calibrated positive multi-exponential model theorem or its two-rate Fisher-optimal separation. Kirtane et al. [3] directly document multiple physical eDNA states with potentially distinct transport and persistence and incomplete state-separation measurements. Augustine et al. [4] identify source location and low concentrations as major ecological challenges and observe early rapid and later slow attenuation; the accessible abstract describes a hierarchical model and extra-Poisson variation, not the claimed optimal-spacing limit. The earlier statistical literature on exponential-mixture Poisson data, for example Esposito et al. [5], studies inference of mixture lifetimes, not this nuisance-amplitude source-distance objective. Pyatkov and Neustroeva [6] discuss source uniqueness and nonuniqueness in much broader advection–dispersion–reaction inverse problems with unrestricted time-dependent source intensities; those results do not determine this stationary two-counter information optimum. Classical log convexity of positive exponential mixtures and the Poisson information formula are prior standard tools, not claimed novel. The contribution assessed here is their *joint* global-identifiability boundary, exact source-location information, and eventually unique universal two-rate sensor-spacing asymptotic in the explicitly restricted ecological observation model.

## Limitations

The model is a minimal calibrated benchmark. The required common positive pool proportions and attenuation rates must be known externally; losing that calibration makes source distance nonidentifiable even with infinitely many downstream stations. Actual rivers can exhibit transient transport, plume formation, lateral mixing, dilution, new downstream source contributions, varying rates, heterogeneous shedding and extra-Poisson measurement noise. In particular, measured downstream eDNA may initially increase with distance [1], contrary to the pure-loss kernel here. The universal sensor gap concerns known-rate long-distance asymptotics of local Fisher information at fixed source scale, not an operational recommendation for a real sampling reach. No observational field validation or independent external mathematical audit is claimed.

## References

1. Van Driessche, C., Everts, T., Neyrinck, S. and Brys, R. *Experimental assessment of downstream environmental DNA patterns under variable fish biomass and river discharge rates*. Environmental DNA 5 (2023), 102–116; online 2022-10-26. https://doi.org/10.1002/edn3.361
2. Van Driessche, C., Everts, T., Neyrinck, S. and Brys, R. *Data from: Experimental assessment of downstream environmental DNA patterns under variable fish biomass and river discharge rates*. Dryad, publicly posted 2022-10-11. https://doi.org/10.5061/dryad.rjdfn2zfc
3. Kirtane, A., Kleyer, H. and Deiner, K. *Sorting states of environmental DNA: Effects of isolation method and water matrix on the recovery of membrane-bound, dissolved, and adsorbed states of eDNA*. Environmental DNA 5 (2023), 582–596; online 2023-04-10. https://doi.org/10.1002/edn3.417
4. Augustine, B. et al. *A hierarchical model for eDNA fate and transport dynamics accommodating low concentration samples*. bioRxiv (2024). https://doi.org/10.1101/2024.03.27.586987
5. Esposito, R., Altucci, C. and Velotta, R. *Analysis of Simulated Fluorescence Intensities Decays by a New Maximum Entropy Method Algorithm*. Journal of Fluorescence 23 (2013), 203–211; online 2012-10-19. https://doi.org/10.1007/s10895-012-1135-0
6. Pyatkov, S. and Neustroeva, L. *Point sources identification problems with pointwise overdetermination*. arXiv:2308.16866 (2023). https://arxiv.org/abs/2308.16866
