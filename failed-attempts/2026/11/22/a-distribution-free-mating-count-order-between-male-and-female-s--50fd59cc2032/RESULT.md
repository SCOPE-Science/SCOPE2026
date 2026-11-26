# A distribution-free mating-count order between male- and female-searching trap systems

## Finding
For every integer \(n\ge2\), positive pair-encounter rate \(a\), and arbitrary almost surely finite, nonnegative individual search lifetime \(T\), consider the two sex-search mechanisms specified below. Let \(K_M\) and \(K_F\) be the numbers of distinct females mated when males, respectively females, search. Then
\[
\Pr(K_M\ge1)=\Pr(K_F\ge1)=1-\bigl(\mathbb E e^{-naT}\bigr)^n,
\]
whereas for every \(2\le k\le n\),
\[
\Pr(K_M\ge k)>\Pr(K_F\ge k)
\]
if \(T\) is nonconstant. Thus male searching strictly dominates for all higher mating-count thresholds, but the probability of *any* mating is identical. If \(T\) is deterministic, the entire count laws coincide; for \(n=1\) they coincide for any \(T\). No parametric assumption on the distribution of \(T\) is needed.

## Assumptions and scope
There are exactly \(n\) males and \(n\) females, all initially unmated. Each searching individual has an independent lifetime distributed as \(T\), independent of all encounters and of other lifetimes. All pair-specific encounter streams are mutually independent homogeneous Poisson processes with common rate \(a>0\) while their searcher remains active. A searcher is removed at the end of its lifetime, modeling trap capture or an independent search deadline.

In the **male-searching** mechanism, \(n\) moving males independently encounter each of the \(n\) stationary females. A female mates at the first encounter and is then counted only once; each male remains available to mate other females until his lifetime ends. In the **female-searching** mechanism, \(n\) moving females independently encounter each of the \(n\) stationary males. A female stops searching upon her first encounter or at lifetime expiration; stationary males can mate repeatedly. Mating encounters do not delay subsequent male searches, and no encounter process is altered by previous mating other than removing the mated female from further counting.

A deterministic finite observation horizon is allowed as a component of \(T\), including \(T=\min(S,H)\) for an independent capture time \(S\) and fixed \(H\). Spatial movement, plume camouflage, population renewal, density dependence, mating capacity, and post-mating capture of females are not included.

For \(j\ge0\), set \(L_j=\mathbb E[e^{-jaT}]\) with \(L_0=1\). Write \(q=L_n\). For nonconstant \(T\), \(0<q<1\).

## Proof
Condition on the male search lifetimes \(T_1,\ldots,T_n\), and put \(Y=e^{-a\sum_{i=1}^nT_i}\). Conditional on these lifetimes, independent female-specific Poisson encounter streams imply that each of the \(n\) stationary females remains unmated with probability \(Y\), independently of the other females. Consequently
\[
K_M\mid Y\sim\operatorname{Bin}(n,1-Y),\qquad
\Pr(K_M=k)=\binom nk\mathbb E[(1-Y)^kY^{n-k}].
\]
In the female-searching case, each female has \(n\) independent rate-\(a\) encounter streams, so the probability she remains unmated until her own lifetime expires is \(L_n=q\). The females are independent, hence
\[
K_F\sim\operatorname{Bin}(n,1-q),\qquad
\Pr(K_F=k)=\binom nk(1-q)^kq^{n-k}.
\]
Since \(\mathbb E[Y^n]=L_n^n=q^n\), both zero-mating probabilities are \(q^n\), proving the equality at threshold \(1\).

Suppose \(n\ge2\) and \(T\) is nonconstant. Define the tilted probability law \(dQ=Y^n\,dP/q^n\) and the nonnegative random variable
\[
Z=\frac{q(1-Y)}{(1-q)Y}.
\]
For \(k=0,\ldots,n\), the probability-mass ratio is the moment
\[
R_k:=\frac{\Pr(K_M=k)}{\Pr(K_F=k)}=\mathbb E_Q[Z^k],\qquad R_0=1.
\]
All these moments are finite because under the tilt their integrands are proportional to \((1-Y)^kY^{n-k}\). At index \(1\),
\[
R_1=\frac{L_{n-1}^{\,n}-q^n}{q^{n-1}(1-q)}<1.
\]
Indeed, strict Hölder (or strict log-convexity of the Laplace transform), with \(T\) nonconstant, gives
\[
L_{n-1}<L_n^{(n-1)/n}=q^{(n-1)/n}.
\]
The moment sequence \((R_k)_{k=0}^n\) is log-convex by Cauchy–Schwarz: \(R_k^2\le R_{k-1}R_{k+1}\) for \(1\le k<n\). Since \(R_0=1\) and \(R_1<1\), log-convexity implies that the signs of \(R_k-1\), for \(k\ge1\), can switch only once, from negative to positive (with a possible equality at the switch). They must switch: the two distributions each have total mass one, so \(\sum_k\Pr(K_F=k)(R_k-1)=0\), while the term at \(k=1\) is strictly negative and the term at \(k=0\) vanishes. Thus the two probability-mass functions have one negative-to-positive sign change after index zero.

For threshold \(k=2\), equality of zero mass together with the strict negative difference at mass one gives a strict positive upper-tail difference. For every \(k\ge3\), either its entire upper tail is on the positive side of the sign change, or the omitted lower masses from indices \(1\) through \(k-1\) have strictly negative total difference. In either case the upper-tail difference is strictly positive. This proves the assertion for all \(2\le k\le n\).

If \(T=t\) almost surely, then \(Y=e^{-nat}=q\) is deterministic, and the two conditional binomial laws are identical. The \(n=1\) equality follows directly from the two encounter mechanisms. These include \(t=0\).

## Verification
The standalone script `check.py` uses only the Python standard library and computes exact rational distributions of \(U=e^{-aT}\) on finite supports. It verifies normalization, the common zero-mating mass, every stochastic-tail inequality, and strictness for nondegenerate laws across a fixed, reproducible family of discrete distributions. Running `python check.py` returns `EXACT ASSERTIONS: 13754`.

As a hand-checkable illustration, let \(n=2\), \(a=1\), and \(T\sim\operatorname{Exp}(1)\). Then \(L_1=1/2\), \(L_2=1/3\), and the masses at \(K=0,1,2\) are \((1/9,5/18,11/18)\) for male searching versus \((1/9,4/9,4/9)\) for female searching. The two models agree at the any-mating threshold but differ by \(1/6\) at the two-mating threshold. Finite checks are diagnostics, not the proof of the universal statement.

## Relationship to prior work
Byers (2012) compares male- and female-searching insects with competitive pheromone traps using spatial correlated-random-walk simulations and reports somewhat less mating in the female-searching system. The present simplified, independent Poisson-encounter model yields an all-threshold stochastic ordering for every independent lifetime law, including an exact *equality* at the any-mating threshold; the spatial simulations neither imply nor test this full distributional statement. Byers (2007) simulates male-searching moths under trapping and disruption, without comparing the two sex-search mechanisms. Barclay and van den Driessche (1983) study discrete population-control models and deterministic demographic conditions, a different outcome and modeling scale. The proof uses classical Laplace-transform convexity and moment log-convexity; no priority is claimed for those inequalities themselves.

## Limitations
This is a theorem for idealized homogeneous, pairwise independent Poisson encounters and equal starting sex counts with reusable males. Its strict order need not extend to finite-capacity males, sex-specific encounter rates or lifetime distributions, dependent search lifetimes, spatially correlated paths, density-dependent encounters, or females trapped after mating. The result does not estimate parameters from field data and does not predict actual trapping efficacy. This comparison has not received independent scientific validation; uninspected historical work may still affect novelty assessment.

## References
- J. A. Byers, "Modelling female mating success during mass trapping and natural competitive attraction of searching males or females," *Entomologia Experimentalis et Applicata* **145** (2012), 228–237. First published October 11, 2012. https://doi.org/10.1111/eea.12006 ; open full text https://www.chemical-ecology.net/pdf/Byers_2012_EEA.pdf
- J. A. Byers, "Simulation of Mating Disruption and Mass Trapping with Competitive Attraction and Camouflage," *Environmental Entomology* **36** (2007), 1328–1338. https://doi.org/10.1603/0046-225X(2007)36[1328:SOMDAM]2.0.CO;2 ; open full text https://www.chemical-ecology.net/pdf/Byers2007.pdf
- H. Barclay and P. van den Driessche, "Pheromone trapping models for insect pest control," *Researches on Population Ecology* **25** (1983), 105–115. https://doi.org/10.1007/BF02528786
