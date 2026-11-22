# A unique sequencing-depth sign reversal of co-detection under coupled occupancy

## Finding
For any \(0<p<1\) and positive intensities \(a,b,c\), suppose two target taxa are **always jointly present or jointly absent** at a site, with joint-presence probability \(p\). If present, a library contains exactly \(n\geq1\) independent reads labeled target A, target B, or background, with respective probabilities \(a/(a+b+c)\), \(c/(a+b+c)\), and \(b/(a+b+c)\). If absent, every read is background. Let \(X_n\) and \(Y_n\) indicate whether each target is represented by at least one read. Then:

1. The site-to-site latent covariance is \(\operatorname{Cov}(Z,Z)=p(1-p)>0\), but there is exactly one real depth \(n_*(p)>1\) at which the detected-indicator covariance changes sign: negative for integer \(n<n_*(p)\), zero if \(n=n_*(p)\), and positive for integer \(n>n_*(p)\). Thus increasing fixed sequencing depth permits **only a negative-to-positive reversal**, never the reverse.
2. Define \(u=(b+c)/(a+b+c)\), \(v=(a+b)/(a+b+c)\), and \(w=b/(a+b+c)\). The unique crossing is characterized by
\[
\frac{(uv)^{n_*}-w^{n_*}}{(1-u^{n_*})(1-v^{n_*})}=1-p.
\]
At two reads, the covariance is positive, zero, or negative precisely as \(p\) is less than, equal to, or greater than \(2/[(1+u)(1+v)]\).
3. The real crossing increases strictly with \(p\), tends to \(1\) as \(p\downarrow0\), and satisfies the sharp high-prevalence asymptotic
\[
n_*(p)=\frac{\log(1/(1-p))}{-\log(uv)}+o(1) \quad(p\uparrow1).
\]
In particular a fixed finite read depth need not recover the positive latent co-occurrence sign when sites are nearly all occupied.
4. If instead each library has an **independent Poisson** total read count with any positive mean \(\ell\), while retaining the same conditional read proportions, the detected-indicator covariance is strictly positive for all \(\ell>0\). The sign reversal is therefore specific to the fixed-total multinomial read-budget mechanism.

An exact rational example uses \(a=2\), \(b=1\), \(c=3\), and \(p=4/5\). Here the latent covariance is \(4/25\), the one-read covariance is \(-8/75\), the two-read covariance is exactly zero, and every larger integer depth has positive covariance.

## Assumptions and scope
A site has a Bernoulli occupancy indicator \(Z\) with probability \(p\). Occupancy of both target taxa equals \(Z\); this is perfect positive coupling, **not** biological independence. Site libraries are independent across sites. Conditional on \(Z=1\), each library consists of exactly \(n\) conditionally independent three-category reads with fixed positive probabilities. Conditional on \(Z=0\), all reads are background and neither target can be falsely detected. We compare **population covariances across sites** at each fixed depth, not finite-sample estimators, relative abundances, time series, or causal interactions.

The positive background weight \(b>0\) makes the 'miss both targets' probability strictly positive, and the positive target weights ensure each target can be detected. All statements hold for every real-valued set of positive weights and \(0<p<1\); extension to real depth is an analytic interpolation used only to locate the unique threshold. No physical interpretation is assigned to a fractional read.

## Proof
**1. Exact joint and marginal read-detection laws.** Set \(s=a+b+c\). At an occupied site, the probabilities of missing target A, missing target B, and missing both after \(n\) reads are \(u^n\), \(v^n\), and \(w^n\), respectively, where
\[
u=\frac{b+c}{s},\quad v=\frac{a+b}{s},\quad w=\frac b s =u+v-1.
\]
Since \(0<w<uv<1\) and \(0<u,v<1\), inclusion-exclusion gives
\[
\mathbb E X_n=p(1-u^n),\quad\mathbb E Y_n=p(1-v^n),\quad
\mathbb E[X_nY_n]=p(1-u^n-v^n+w^n).
\]
Consequently
\[
C_n:=\operatorname{Cov}(X_n,Y_n)
=p(1-u^n)(1-v^n)\left(1-p-\Theta(n)\right),
\quad
\Theta(t)=\frac{(uv)^t-w^t}{(1-u^t)(1-v^t)}.
\]
All factors outside the final bracket are strictly positive for every finite integer \(n\ge1\). Thus its sign is exactly that of \(1-p-\Theta(n)\).

**2. A strict one-crossing lemma for every positive real depth.** Define \(\alpha=-\log u>0\), \(\beta=-\log v>0\), and \(\delta=\log(uv/w)>0\). Multiplying numerator and denominator of \(\Theta(t)\) by \(\exp((\alpha+\beta)t)\) yields
\[
\Theta(t)=\frac{1-e^{-\delta t}}{(e^{\alpha t}-1)(e^{\beta t}-1)},\qquad t>0.
\]
Differentiating its logarithm gives
\[
\frac{d}{dt}\log\Theta(t)
=\frac{\delta}{e^{\delta t}-1}
-\frac{\alpha}{1-e^{-\alpha t}}
-\frac{\beta}{1-e^{-\beta t}}.
\]
For \(x>0\), the strict exponential inequalities \(e^x-1>x\) and \(1-e^{-x}<x\) imply
\(\delta/(e^{\delta t}-1)<1/t\) and
\(\alpha/(1-e^{-\alpha t})>1/t\), \(\beta/(1-e^{-\beta t})>1/t\). Therefore the displayed log derivative is **strictly less than** \(-1/t\). Hence \(\Theta\) is strictly decreasing for all \(t>0\).

Using \(uv-w=(1-u)(1-v)\), we have \(\Theta(1)=1\). From its exponential form, \(\Theta(t)\to0\) as \(t\to\infty\). Thus for every \(0<p<1\), the intermediate value theorem and strict monotonicity supply exactly one \(n_*(p)>1\) solving \(\Theta(n_*)=1-p\). This proves every integer-depth sign claim, including the equality case.

**3. Sharp two-read and prevalence limits.** Factor \(1-u^2=(1-u)(1+u)\) and similarly for \(v\), to obtain
\[
\Theta(2)=\frac{uv+w}{(1+u)(1+v)},\qquad
1-\Theta(2)=\frac{2}{(1+u)(1+v)}.
\]
The sign formula gives the exact two-read threshold. Because \(\Theta\) decreases, its unique inverse applied to \(1-p\) increases strictly as \(p\) increases; its limit as \(p\downarrow0\) is \(1\). As \(t\to\infty\),
\[
\Theta(t)=(uv)^t\,
\frac{1-(w/(uv))^t}{(1-u^t)(1-v^t)}
=(uv)^t(1+o(1)).
\]
Taking logarithms at \(t=n_*(p)\), which diverges as \(p\uparrow1\), proves
\(n_*(p)=\log(1/(1-p))/[-\log(uv)]+o(1)\).

**4. Poissonized total read count.** Let the total reads at an occupied site be independent \(\mathrm{Poisson}(\ell)\), for \(\ell>0\). Poisson thinning makes the target A and target B counts conditionally independent, with means \(\ell a/s\) and \(\ell c/s\). Their conditional detection probabilities are \(d_A=1-e^{-\ell a/s}\) and \(d_B=1-e^{-\ell c/s}\). Unoccupied sites still detect neither target. Therefore
\[
\operatorname{Cov}(X_\ell,Y_\ell)=p(1-p)d_A d_B>0.
\]
This proves that the negative phase cannot occur under that alternative counting convention. It does **not** claim positivity for other random library-size laws.

**5. Exact witness.** With \((a,b,c,p)=(2,1,3,4/5)\), the miss probabilities are \(u=2/3\), \(v=1/2\), \(w=1/6\); hence \(\Theta(2)=1/5=1-p\). Direct substitution into the covariance identity gives \(C_1=-8/75\), \(C_2=0\), and strict \(C_n>0\) for every integer \(n\ge3\). The true-occupancy covariance is \(4/25>0\).

## Verification
Run `python3 check.py` from the extracted file directory; it uses Python's standard library only. The program independently enumerates every three-category read word of lengths one through six over each of the 27 positive integer weight triples \((a,b,c)\in\{1,2,3\}^3\), with three rational prevalence choices; this gives exact rational agreement with the expectation-derived covariance. It then checks monotonicity and covariance sign classification for 2,300 pseudorandom parameter sets across 40 depths, tests the exact rational tie and Poissonized sign, and checks the high-prevalence limit numerically. The complete script produced `PASS 271685 assertions` on execution. Enumeration and floating-point tests corroborate the stated formulas; the proof above alone establishes the all-parameter and infinite-depth claims.

## Relationship to prior work
Courtaillac et al. (2024) study how eDNA metabarcoding replication and pooling affect taxon detection and provide the motivating field-monitoring context. Fukaya et al. (2021) explicitly construct a multinomial read-count observation component conditional on sequencing depth and occupancy. Their general model encompasses the fixed-depth sampling mechanism, but their reported results concern single-species detectability, estimation, and allocation of surveying resources; they do not report the present **unique change of sign in a two-taxon detected-indicator covariance**. Boshuizen and te Beest (2022), Gloor et al. (2017), and Kurtz et al. (2015) document compositional biases and potentially spurious associations; they do not give this two-state, fixed-total, all-depth threshold or its Poissonization contrast.

The closest identified mathematical result for incidence-based co-detection, *An irreversible co-detection sign switch under incidence-based rarefaction* (published-finding corpus, 2026), uses fixed incidence sets and sampling of distinct sites **without replacement**; its permitted switch direction is positive-to-negative. Here the random mechanism is fixed-count **within-site multinomial reads**, mixed over a shared latent Bernoulli site state, and the permitted direction is negative-to-positive. Neither sampled-object law is the other's specialization. Other indexed multinomial covariance studies concern counts or different occupancy functionals, not this sign threshold.

## Limitations
The model idealizes two perfectly co-occurring species with fixed conditional read proportions, a positive background category, no false-positive reads, and independent samples. It does not encompass unequal or partially correlated occupancies, overdispersed amplification, primer bias that varies by site, compositional preprocessing, random library sizes other than the specified Poisson comparison, or temporal dependence. It concerns covariance sign, not inferential statistical significance. Even if observed covariance turns positive at high depth, positive co-occurrence is **not evidence of ecological causation**. No empirical sequencing-depth recommendation is claimed; historical priority against unexamined sampling and microbiome literature remains open.

## References
1. Courtaillac, K.-L., Landschoff, J., Hull, K., and von der Heyden, S. (2024). *The Effect of Spatio-Temporal Sampling and Biological Replication on the Detection of Kelp Forest Fish Communities Using eDNA Metabarcoding*. Environmental DNA 6:e70023. First public release 2024-10-14. https://doi.org/10.1002/edn3.70023
2. Fukaya, K., Kondo, N. I., Matsuzaki, S. S., and Kadoya, T. (2021). *Multispecies site occupancy modelling and study design for spatially replicated environmental DNA metabarcoding*. Methods in Ecology and Evolution 13:183-193. First public release 2021-10-04. https://doi.org/10.1111/2041-210X.13732
3. Boshuizen, H. C., and te Beest, D. E. (2022). *Pitfalls in the statistical analysis of microbiome amplicon sequencing data*. Molecular Ecology Resources 23:539-548. First public release 2022-11-04. https://doi.org/10.1111/1755-0998.13730
4. Kurtz, Z. D., et al. (2015). *Sparse and Compositionally Robust Inference of Microbial Ecological Networks*. PLoS Computational Biology 11:e1004226. https://doi.org/10.1371/journal.pcbi.1004226
5. Gloor, G. B., et al. (2017). *Microbiome Datasets Are Compositional: And This Is Not Optional*. Frontiers in Microbiology 8:2224. https://doi.org/10.3389/fmicb.2017.02224
6. *An irreversible co-detection sign switch under incidence-based rarefaction* (2026), published-finding corpus record https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-irreversible-co-detection-sign-switch-under-incidence-based-r--37418c61ba8c
