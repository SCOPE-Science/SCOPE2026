# A sharp clustering threshold and unique overdispersion optimum for scramble recruitment

## Finding

At otherwise identical ecological sites with a fixed mean of \(\mu>0\) arriving individuals, let the local count have the negative-binomial law with real shape \(k>0\) and variance \(\mu+\mu^2/k\). If an individual in a site containing \(n\geq1\) individuals has expected recruitment probability \(q^{n-1}\), with \(0<q<1\), the mean recruitment per site is
\[
R_k(\mu,q)=\mathbb E[Nq^{N-1}]=\mu\left(1+\frac{z}{k}\right)^{-k-1},\qquad z=\mu(1-q)>0.
\]
The unclustered Poisson limit is \(R_\infty=\mu e^{-z}\). The **global clustering phase diagram** at fixed \(\mu,q\) is exact:

1. If \(0<z\leq2\), recruitment strictly increases with \(k>0\), so the Poisson limit is the unique maximizer on the extended domain \((0,\infty]\); no finite shape attains it.
2. If \(z>2\), recruitment strictly increases up to one finite shape \(k_*(z)\), then strictly decreases to the Poisson value. Thus the finite optimum strictly improves on both the Poisson limit and the extreme-clustering limit. Defining
\[
H(t)=\frac{t^2}{(1+t)\log(1+t)-t},\qquad t>0,
\]
\(H\) maps \((0,\infty)\) increasingly onto \((2,\infty)\), and the unique optimizer is \(k_*(z)=z/t_*(z)\), with \(H(t_*(z))=z\).
3. The critical and strong-crowding regimes have the **sharp** laws
\[
k_*(z)\sim\frac{4}{3(z-2)}\quad(z\downarrow2),\qquad
k_*(z)\log z\longrightarrow1\quad(z\to\infty),\qquad
\frac{R_{k_*(z)}}{\mu}\sim\frac{1}{e z\log z}\quad(z\to\infty).
\]
4. Any two distinct fixed shapes \(0<k_1<k_2\leq\infty\) have **exactly one positive crowding level** \(z_c(k_1,k_2)>1\) at which their recruitment rankings reverse: \(R_{k_1}<R_{k_2}\) below the level and \(R_{k_1}>R_{k_2}\) above it. Equality at \(z=0\) is outside the stated domain.

All assertions quantify over the complete stated real parameter domain, not only sampled shapes or integer site counts. The dimensionless product \(z\) is the meaningful competition intensity; varying it for the pairwise comparison means changing ecological parameters while the two shape values remain fixed.

## Assumptions and scope

The negative-binomial probability generating function at fixed mean \(\mu\) and positive real shape \(k\) is
\[
P_k(s)=\mathbb E[s^N]=\left(1+\frac{\mu}{k}(1-s)\right)^{-k},\quad 0\leq s\leq1.
\]
Thus \(\mathbb EN=\mu\) and \(\operatorname{Var}N=\mu+\mu^2/k\). Shape \(k\downarrow0\) represents increasingly concentrated local counts with a growing fraction of empty sites, whereas \(k\to\infty\) approaches a Poisson site count. For any site with \(n\ge1\) arrivals, each individual's conditional **expected** recruitment probability is \(q^{n-1}\); independence of survivors is not required for the expectation. The site produces expected recruits \(nq^{n-1}\), and an empty site produces none. No density feedback operates between sites. Only the expected recruits in one recruitment episode are optimized, never stationary population growth or persistence. Fixed-mean comparisons deliberately hold total expected seed pressure constant while varying dispersion, rather than holding the ordinary negative-binomial success probability constant.

The model is applicable as a simplified scramble-competition or density-dependent mortality calculation; it does not claim that the overdispersion parameter is a freely controllable biological management variable. Parameter \(q\) is a per-competitor retention factor, **not** the negative-binomial success probability.

## Proof

**Expected recruitment.** Differentiating the stated generating function gives
\[
P'_k(s)=\mu\left(1+\frac{\mu}{k}(1-s)\right)^{-k-1}.
\]
Evaluation at \(s=q\) gives the displayed formula. By \(\lim_{k\to\infty}(1+z/k)^{-k-1}=e^{-z}\), the Poisson result follows; at fixed \(z>0\), the limit as \(k\downarrow0\) is zero because \((1+z/k)^{-1}\to0\).

**Derivative sign and the exact optimizer.** Put \(t=z/k>0\) and \(g(t)=(1+t)\log(1+t)-t\). Here \(g(0)=0\) and \(g'(t)=\log(1+t)>0\), so \(g(t)>0\) for \(t>0\). For the log normalized recruitment \(L(k)=\log(R_k/\mu)\), direct differentiation at fixed \(z\) yields
\[
L'(k)=-\log(1+t)+\frac{(k+1)t}{k(1+t)}
=\frac{1}{1+t}\left(\frac{t^2}{z}-g(t)\right)
=\frac{g(t)}{z(1+t)}\bigl(H(t)-z\bigr).
\]
The required global monotonicity of \(H\) is not assumed: differentiation gives
\[
H'(t)=\frac{t\bigl((t+2)\log(1+t)-2t\bigr)}{g(t)^2}>0.
\]
Indeed, if \(F(t)=(t+2)\log(1+t)-2t\), then \(F(0)=0\) and \(F'(t)=\log(1+t)-t/(1+t)>0\) for \(t>0\), since this derivative of \(F\) vanishes at zero and has positive derivative \(t/(1+t)^2\). The series \(g(t)=t^2/2-t^3/6+O(t^4)\) shows \(\lim_{t\downarrow0}H(t)=2\), and \(H(t)\sim t/(\log t-1)\to\infty\) as \(t\to\infty\). Thus \(H\) is a strictly increasing bijection from \((0,\infty)\) to \((2,\infty)\). Since \(t=z/k\) decreases as \(k\) increases, the sign of \(L'\) is always positive for \(z\leq2\), and for \(z>2\) changes exactly once from positive to negative. The endpoint limits imply global and strict optimality as stated; in particular the finite peak exceeds \(R_\infty\).

**Critical and large-\(z\) behavior.** Taylor expansion gives \(H(t)=2+2t/3+O(t^2)\) as \(t\downarrow0\). Inverting at \(z\downarrow2\) yields \(t_*(z)\sim3(z-2)/2\), hence \(k_*(z)=z/t_*(z)\sim4/[3(z-2)]\). As \(z\to\infty\), monotonicity forces \(t_*(z)\to\infty\). Since \(z=H(t_*)\sim t_*/\log t_*\), the logarithm relation \(\log t_*\sim\log z\) implies \(k_*(z)=z/t_*\sim1/\log z\). Finally
\[
\frac{R_{k_*}}\mu=(1+t_*)^{-1}(1+t_*)^{-k_*},
\]
where \(1+t_*\sim z\log z\) and \(k_*\log(1+t_*)\to1\), yielding the asserted \(1/(e z\log z)\) law.

**All pairwise ranking reversals.** Fix \(0<k_1<k_2<\infty\). Write \(D(z)=\log(R_{k_1}/R_{k_2})\), with common \(\mu\) suppressed. We have \(D(0)=0\), and
\[
D'(z)=\frac{(k_2-k_1)(z-1)}{(k_1+z)(k_2+z)}.
\]
Consequently \(D\) strictly decreases on \((0,1)\) and increases on \((1,\infty)\). Since \(D(z)\sim(k_2-k_1)\log z\to\infty\) as \(z\to\infty\), it has exactly one zero in \((1,\infty)\). For \(k_2=\infty\), the same argument holds with \(D'(z)=(z-1)/(k_1+z)\) and \(D(z)\to\infty\). This proves the complete pairwise single-crossing statement, including strict signs on either side.

## Verification

The bundled `verify.py` runs under Python 3 with only the standard library. It directly sums independent negative-binomial terms for moderate parameters and checks them against the generating-function formula, verifies finite-grid derivative signs, samples shape values on both sides of seven interior optimizers, locates five independent pairwise crossings, and tests near-critical and large-crowding asymptotic predictions. The retained source reported `PASS: 263 deterministic diagnostic assertions`. For the illustrative mean \(\mu=8\), competitor retention \(q=1/2\), hence \(z=4\), the root is \(k_*\approx0.971897376815\), with predicted recruitment \(R_{k_*}/\mu\approx0.040005389824\) against Poisson \(e^{-4}\approx0.018315638889\). These finite numerical checks are supplementary diagnostics; the universal proof is the analytic argument above.

## Relationship to prior work

Brännström and Sumpter (2005), especially equations (2.3), (3.3) and (3.4), already derive negative-binomially aggregated scramble recruitment and the underlying Hassell function. This generating function and the associated response curve **are not claimed as new**. The additional exact claim here is the fixed-mean optimization **over the real shape parameter**, its sharp change at \(z=2\), the unique pairwise clustering-rank reversal, and the two asymptotic optimizer laws. Their paper emphasizes mechanistic derivation and model classification rather than this entire shape-optimization theorem. Anazawa (2009) displays the Hassell functional form and studies competition mechanisms, not the full fixed-mean shape phase diagram. The abstract of Anazawa (2010) describes a two-parameter mechanistic model with resource partitioning, spatial aggregation, and stability, but its complete text was not accessible for a conclusive overlap comparison.

Beckman, Neuhauser and Muller-Landau (2012) use negative-binomial seed clumping in a spatially explicit model with insect predation and pathogen dynamics. Their full-text model and result sections compare seedling establishment across predator/pathogen regimes and dispersal patterns, not a universal fixed-mean single-site \(q^{n-1}\) shape optimum. In some of their regimes clumping raises establishment because of enemy satiation, so their qualitative conclusion cannot be transferred to this different competition mechanism. White (2010) and Anazawa (2019) offer related spatial aggregation and density-dependence discussions, but the inspected material does not establish a dominating version of the theorem.

The already published Hassell seasonal-order theorem addresses compositions of deterministic maps across seasons at fixed feedback exponent, rather than optimizing a negative-binomial shape at fixed mean and fixed individual-interference probability. The previously published negative-multinomial shape-mode theorem varies shape at fixed cell probability parameters, not at fixed mean or for the expectation \(\mathbb E[Nq^{N-1}]\). The prey-aggregation allocation staircase optimizes deterministic biomass distribution under Holling-II loss, and neither its objective nor constraints reduce to the negative-binomial shape family. These explicit statement-level distinctions avoid claiming novelty merely from a different title. General probability-transform, Hassell-model and allocation literature could still contain an equivalent optimization, so historical priority is **provisional**.

## Limitations

The proof is exact only for a fixed mean negative-binomial distribution with positive real shape, one-step expected density-dependent recruitment \(nq^{n-1}\), and \(0<q<1\). It does not apply to heterogeneous patch means, spatial correlations, other functions of local crowding, finite-sample calibration, predator saturation, long-run population stability, or uncertainty in model parameters. Extreme clustering drives expected recruitment to zero in this specified scheme, not in all ecological competition models. A maximal mean may have small practical value if its associated shape is biologically unattainable. Numerical checks alone do not verify the infinite-domain statements, and no independent audit or empirical validation is claimed.

## References

1. Å. Brännström and D. J. T. Sumpter, “The role of competition and clustering in population dynamics,” *Proceedings of the Royal Society B* **272** (2005), 2065–2072. First public date 2005-08-23. DOI: https://doi.org/10.1098/rspb.2005.3185. Author-hosted full text: https://www2.math.uu.se/~davsu428/web/BrannstromSumpter05a.pdf.
2. N. G. Beckman, C. Neuhauser and H. C. Muller-Landau, “The interacting effects of clumped seed dispersal and distance- and density-dependent mortality on seedling recruitment patterns,” *Journal of Ecology* **100** (2012), 862–873. DOI: https://doi.org/10.1111/j.1365-2745.2012.01978.x.
3. M. Anazawa, “The mechanistic basis of population models with various types of competition,” *RIMS Kôkyûroku* **1663** (2009), pp. 176–181. Open full text: https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1663-31.pdf.
4. J. W. White, “Can inverse density dependence at small spatial scales produce dynamic instability in animal populations?”, *Theoretical Ecology* **4** (2011), 357–370. DOI: https://doi.org/10.1007/s12080-010-0083-z.
5. M. Anazawa, “The mechanistic basis of discrete-time population models: The role of resource partitioning and spatial aggregation,” *Theoretical Population Biology* **77** (2010), 213–218. DOI: https://doi.org/10.1016/j.tpb.2010.02.005. Abstract inspected; full text not obtained.
6. M. Anazawa, “Inequality in resource allocation and population dynamics models,” *Royal Society Open Science* **6** (2019), 182178. Open text: https://pmc.ncbi.nlm.nih.gov/articles/PMC6689590/.
