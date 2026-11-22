# Sharp within-fruit paternity bounds for variable pollinator residence lengths

## Finding

An idealized pollinator deposits a fixed fraction \(\rho\in(0,1)\) of each flower's carried pollen at every subsequent flower, and consecutive donor-plant residence lengths \(L_1,L_2,\ldots\) are independent copies of a positive-integer-valued random variable \(L\). A recipient is sampled at the first flower visited on a new plant. All donor plants in its preceding itinerary are distinct. Each visited donor flower exports equal pollen mass; infinitely many prior donor flowers are assumed to establish the normalized carryover profile, and seeds choose their father independently in proportion to deposited pollen mass.

Put \(q=1-\rho\), \(\mu=\mathbb E[q^L]\), \(\nu=\mathbb E[q^{2L}]\). For an actual random itinerary, let \(W_i\) be the share of pollen from the \(i\)-th most recent donor plant. Then

\[
\mathbb E[W_i]=(1-\mu)\mu^{i-1},\qquad
H:=\Pr(\text{two offspring from the same donor}\mid\text{one probe})
=\frac{1-2\mu+\nu}{1-\nu}.
\]

If the random itinerary is replaced by its *mean* sire profile before offspring are sampled, its same-father probability is only \(H_{\mathrm{pool}}=(1-\mu)/(1+\mu)\). The exact discrepancy is

\[
\boxed{H-H_{\mathrm{pool}}=\frac{2\operatorname{Var}(q^L)}{(1-\nu)(1+\mu)}\ge0.}
\]

Equality holds if and only if the residence length \(L\) is deterministic. In particular, a geometric-looking *average* sire profile does not imply that individual fruits exhibit that profile or that its paternity-correlation estimate is valid.

There is a sharp distribution-free extremal law at **fixed deposition fraction** \(\rho\) and **fixed observed mean sire profile** \(\mu\). Necessarily \(0<\mu\le q\). If \(0<\mu<q\), choose the unique integer \(k\ge1\) such that \(q^{k+1}<\mu\le q^k\), and define

\[
\nu_-=(q^k+q^{k+1})\mu-q^{2k+1},\qquad \nu_+=q\mu,\qquad
F_\mu(v)=\frac{1-2\mu+v}{1-v}.
\]

The exact set of possible same-father probabilities is

\[
\boxed{F_\mu(\nu_-)\ \le\ H\ <\ F_\mu(\nu_+).}
\]

Every value in this half-open interval is attained. The lower endpoint is attained **only** by the distribution on the two consecutive residence lengths \(k,k+1\) having mean \(\mathbb E[q^L]=\mu\) (with the deterministic limit at \(\mu=q^k\)). The upper endpoint is an unattained supremum approached by distributions on residence lengths \(1,N\) as \(N\to\infty\). When \(\mu=q\), the only possible residence law is \(L\equiv1\), so both bounds coincide and are attained.

For the biologically common geometric residence law \(\Pr(L=\ell)=\tau(1-\tau)^{\ell-1}\), \(\ell\ge1\), \(0<\tau<1\), put \(\alpha=1-\mu\). The two observable statistics \(\alpha\) (mean share of the most recent donor plant) and \(H\) (same-father probability for two independently sampled offspring from a single-probe fruit) determine **both** \(\rho\) and \(\tau\) uniquely:

\[
\boxed{\frac{\alpha}{2-\alpha}<H<\alpha,\qquad
\rho=\frac{2(\alpha-H)}{1-H},\qquad
\tau=\frac{\rho(1-\alpha)}{\alpha(1-\rho)}.}
\]

Conversely, every \(0<\alpha<1\) and \(H\) in that strict interval arise from exactly one \((\rho,\tau)\in(0,1)^2\). A mean sire profile by itself fixes only \(\alpha\), so it does not identify the two mechanisms. These conclusions are population-probability statements, not claims of exact recovery from two genotyped seeds.

## Assumptions and scope

The pollinator's previous visited donor plants are all distinct, so that every run of consecutive flowers on one plant corresponds to exactly one potential father. Within a run, each flower supplies the same amount of viable pollen. All pollen has the same fertilization success, and the carryover fraction does not depend on the current plant, pollen age, or pollen-source identity. The focal recipient is the first flower on a new plant, avoiding self pollen; it receives a single pollinator probe. The model uses an infinite stationary preceding itinerary and therefore does not describe finite donor pools, repeated returns to plants, selfing, extra probes, pollen competition, or changing deposition fractions.

A residence length is a positive integer with no moment assumption: \(q^L\le q<1\), so its needed moments exist. Repeated donor runs are independent and identically distributed. The geometric special case models independently departing after each visited flower with probability \(\tau\).

The observable \(\alpha\) requires identifying the most recently visited donor plant (for example in controlled marked-donor experiments). The observable \(H\) is a within-recipient *pairwise* match probability; it differs from the match probability between seeds sampled from *different* independently realized pollen histories. Estimators and finite-sample uncertainty are not part of this theorem.

## Proof

**1. Random donor shares and normalization.** Set \(Y_i=q^{L_i}\). The total geometric pollen mass from the nearest donor's \(L_1\) flowers is \(1-q^{L_1}=1-Y_1\). Each earlier donor run is attenuated by \(Y_1\), hence

\[
W_i=(1-Y_i)\prod_{j<i}Y_j,\qquad
\sum_{i=1}^n W_i=1-\prod_{j=1}^nY_j.
\]

Since each \(0<Y_j\le q<1\), the remaining mass vanishes, so \(\sum_{i\ge1}W_i=1\) for every itinerary. Conditional on those shares, independently sampled offspring have the same father with probability \(\sum_iW_i^2\). All expectations below interchange with sums by monotone convergence.

**2. Mean and sibling-concentration identities.** Independence gives \(\mathbb E W_i=(1-\mu)\mu^{i-1}\). Thus the pooled match probability is \(\sum_i(\mathbb EW_i)^2=(1-\mu)/(1+\mu)\). Also \(\mathbb EW_i^2=(1-2\mu+\nu)\nu^{i-1}\), giving

\[
H=\sum_{i\ge1}\mathbb E W_i^2=\frac{1-2\mu+\nu}{1-\nu}.
\]

Subtracting the pooled expression yields \(2(\nu-\mu^2)/[(1-\nu)(1+\mu)]\), which is positive exactly when \(Y=q^L\) is nonconstant, equivalently when \(L\) is nonconstant. More generally, for every positive integer \(m\), the probability that \(m\) conditionally independent offspring from one probe share one father is

\[
H_m=\frac{\mathbb E[(1-Y)^m]}{1-\mathbb E[Y^m]}
=\frac{\sum_{j=0}^m(-1)^j\binom mj\mathbb E[q^{jL}]}{1-\mathbb E[q^{mL}]}.
\]

These residual-allocation moment identities are elementary ingredients; originality is not asserted for their abstract mathematical form.

**3. Sharp integer-residence extrema.** The random variable \(Y=q^L\) takes values in \(\{q,q^2,\ldots\}\), and \(0<\mu=\mathbb E Y\le q\). For \(\mu<q\) let \(k\) be as in the finding and write \(a=q^k\), \(b=q^{k+1}\). For every allowed value \(y=q^\ell\), there is no lattice point strictly between \(b\) and \(a\); hence \((y-a)(y-b)\ge0\). Taking expectations shows

\[
\nu=\mathbb E Y^2\ge(a+b)\mu-ab=\nu_-.
\]

Equality is possible only if \(Y\in\{a,b\}\), giving the unique two-point law with \(\Pr(L=k)=(\mu-b)/(a-b)\), \(\Pr(L=k+1)=(a-\mu)/(a-b)\). At \(\mu=a\) this reduces to deterministic \(L=k\).

On the other hand, \(Y^2\le qY\), with equality only for \(Y=q\) or \(Y=0\). The latter is not an admissible finite residence length, so \(\nu<q\mu=\nu_+\) whenever \(\mu<q\). Fixing \(\mu\) and mixing \(L=1\) with \(L=N\) using \(\Pr(L=1)=(\mu-q^N)/(q-q^N)\), for sufficiently large \(N\), makes \(\nu\to q\mu\) from below. The function \(F_\mu(v)\) has positive derivative \(2(1-\mu)/(1-v)^2\), transferring the sharp variance bounds to \(H\). Convex mixtures of the unique minimizer and any such two-point near-supremum law preserve \(\mu\), and their \(\nu\) ranges are intervals. Taking their union attains every value up to but not including the supremum. At \(\mu=q\), \(Y\le q\) forces \(L=1\) almost surely.

**4. Geometric-residence identification.** When \(\Pr(L=\ell)=\tau(1-\tau)^{\ell-1}\), geometric summation yields

\[
\mathbb E[q^{mL}]=\frac{\tau q^m}{1-(1-\tau)q^m},\qquad
\alpha=1-\mu=\frac{\rho}{\rho+\tau(1-\rho)}.
\]

Substitution into the formula for \(H\) simplifies to \(H=(2\alpha-\rho)/(2-\rho)\). For fixed \(\alpha\), the interior parameter domain is \(0<\rho<\alpha<1\) and \(\tau=\rho(1-\alpha)/[\alpha(1-\rho)]\). As \(\rho\) runs continuously from zero to \(\alpha\), \(H\) strictly decreases from \(\alpha\) to \(\alpha/(2-\alpha)\), with derivative \(2(\alpha-1)/(2-\rho)^2<0\). Hence the displayed strict feasible interval, two rational inverse formulas, and their uniqueness. The endpoint inequalities are strict for \(\rho,\tau\in(0,1)\). A fixed mean profile \((\mathbb EW_i)\) depends only on \(\alpha\), leaving a one-parameter family of compatible mechanisms.

## Verification

The accompanying `CHECK.py` uses standard-library exact rational arithmetic to test moment and inverse identities across parameter grids, arbitrary three- and four-point run-length distributions, the sharp adjacent and distant-run extremizers, finite-prefix remainder formulas, and deterministic equality cases. A separately coded pseudorandom simulation of realized donor runs checks illustrative moments without forming the averaged profile first. Executing `python CHECK.py` completes 24,637 assertions successfully.

For example, at \(\rho=\tau=1/2\), \(\alpha=2/3\), and \(H_{\mathrm{pool}}=1/2\), whereas the actual stochastic single-probe same-sire probability is \(H=5/9\). Among *all* residence laws with the same deposition fraction \(\rho=1/2\) and mean profile \(\alpha=2/3\), the sharp possible interval is \([11/21,3/5)\). These are exact rational results, not Monte Carlo estimators.

## Relationship to prior work

Galen and Rotenberry (1988) modeled pollen carryover and donor diversity, including random variation in pollen deposition rates. Mitchell et al. (2013) modeled exponential carryover and probabilistic within-plant pollinator visits, deriving *expected* donor sire profiles and simulating seedling paternity from those profiles. Their published framework motivates the present distinction between an average profile and an actual random sequence of donor runs. The present theorem does not claim novelty for their geometric pollen-carryover model or their relationship between mate diversity and carryover.

Cresswell and Hoyle (2006) inferred paternity shadows from field data and pollinator movement observations; their regression question is distinct from the fixed-mean extremal sibling-match problem. Karron et al. (2005) documented multiple paternity and limitations of a one-probe assumption. General residual-allocation theory, including Rodríguez and Quintana (2015), covers abstract independent stick-breaking and species-sampling identities; the general moment summation itself is therefore not presented as a new probabilistic theorem. The specific sharp integer-run optimization, biological two-observable identification, and discrepancy between the pooled and single-probe quantities were not found in the inspected sources.

## Limitations

All claims are exact within the stated idealization. Random residence lengths need not be geometric for the general bounds; the two-parameter identification requires the geometric residence law. Identifiability is a population-law property requiring many independently sampled flowers, not an estimation guarantee. Environmental pollen loads are finite and may be subject to repeat visits, pollen donor revisits, pollen loss during grooming, unequal flower contributions, spatial heterogeneity, selfing, or fertilization selection. Those effects can invalidate the sharp interval and must be modeled separately. The biological implications require field-level validation; no empirical advantage or selection outcome is claimed. Abstract stick-breaking moment methods are established mathematics, and historical priority of the ecological extremal formulation requires outside verification.

## References

1. Galen, C. and Rotenberry, J. T. (1988), *Variance in pollen carryover in animal-pollinated plants: Implications for mate choice*, Journal of Theoretical Biology 135, 419–429. https://doi.org/10.1016/S0022-5193(88)80257-1
2. Karron, J. D. et al. (2005), *Patterns of multiple paternity in fruits of Mimulus ringens (Phrymaceae)*, American Journal of Botany 92, 885–890. https://doi.org/10.3732/ajb.92.5.885
3. Cresswell, J. E. and Hoyle, M. (2006), *A mathematical method for estimating patterns of flower-to-flower gene dispersal from a simple field experiment*, Functional Ecology 20, 245–251. https://doi.org/10.1111/j.1365-2435.2006.01085.x
4. Mitchell, R. J., Wilson, W. G., Holmquist, K. G. and Karron, J. D. (2013), *Influence of pollen transport dynamics on sire profiles and multiple paternity in flowering plants*, PLoS ONE 8, e76312. https://doi.org/10.1371/journal.pone.0076312
5. Rodríguez, A. and Quintana, F. A. (2015), *On species sampling sequences induced by residual allocation models*, Journal of Statistical Planning and Inference 157–158, 108–120. https://doi.org/10.1016/j.jspi.2014.08.008
