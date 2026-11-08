# A sharp synchrony--rescue threshold for joint occupancy in a two-patch metapopulation

## Finding

In the two-patch immigration--rescue model defined below, increasing the fraction \(\theta\in[0,1]\) of a fixed local catastrophic-extinction hazard that arises from simultaneous rather than independent disasters **strictly decreases regional occupancy and expected occupied-patch count**, but its effect on the probability that **both** patches are occupied changes sign at one exact rescue threshold. Write \(\lambda>0\) for immigration to each empty patch, \(\mu>0\) for each occupied patch's ordinary extinction rate, \(c>0\) for additional donor-to-empty rescue colonization, and \(\kappa>0\) for the fixed per-patch catastrophe hazard. If \(R_\theta\), \(B_\theta\), and \(M_\theta\) respectively denote the stationary probability of at least one occupied patch, both occupied, and the mean number occupied, then for all \(\theta\in[0,1]\):

\[
\frac{dR_\theta}{d\theta}<0,\qquad
\frac{dM_\theta}{d\theta}<0,\qquad
\operatorname{sgn}\!\left(\frac{dB_\theta}{d\theta}\right)
=\operatorname{sgn}(\mu+\kappa+\lambda-c).
\]

Consequently, perfect synchronization maximizes \(B_\theta\) when \(0<c<\mu+\kappa+\lambda\), independent disasters maximize it when \(c>\mu+\kappa+\lambda\), and **every** synchronization level has exactly the same \(B_\theta\) when \(c=\mu+\kappa+\lambda\). The corresponding optimizers are unique in the two strict cases. In contrast, \(\theta=0\) uniquely maximizes both \(R_\theta\) and \(M_\theta\) for every strictly positive parameter choice.

## Assumptions and scope

There are exactly two indistinguishable habitat patches. At any time each is either occupied or empty. Independent mainland immigration occupies an empty patch at rate \(\lambda\). Ordinary local extinction removes each occupied patch at rate \(\mu\). A donor-preserving rescue event from the other occupied patch colonizes a given empty patch at additional rate \(c\), so the total empty-to-occupied transition rate when the other patch is occupied is \(\lambda+c\). Catastrophes arise from mutually independent Poisson clocks: one common clock of rate \(\theta\kappa\), which simultaneously empties all occupied patches, and two patch-specific clocks of rate \((1-\theta)\kappa\) each, which empty only that patch. All clock families are independent. Thus the instantaneous catastrophe hazard faced by either occupied patch is exactly \(\kappa\), irrespective of \(\theta\). A clock ring when its target is empty has no effect. No habitat-suitability state, transient environmental memory, or space-dependent rates are modeled. We consider the unique stationary law, not a finite-horizon probability of survival before global extinction.

Define the aggregate states \(0,1,2\) as the number of occupied patches. Because of symmetry this is a Markov process, with generator, in this order,

\[
Q_\theta=\begin{pmatrix}
-2\lambda&2\lambda&0\\
\mu+\kappa&-(\mu+\kappa+\lambda+c)&\lambda+c\\
\theta\kappa&2\mu+2(1-\theta)\kappa&-2\mu-(2-\theta)\kappa
\end{pmatrix}.
\]

Let \(p_j(\theta)\) denote its stationary probability of \(j\) occupied patches. Then \(R_\theta=p_1+p_2=1-p_0\), \(B_\theta=p_2\), and \(M_\theta=p_1+2p_2\).

## Proof

Set \(h=\mu+\kappa\) and

\[
D_\theta=2[(h+\lambda)^2+\lambda c]+\kappa\theta(c-h-\lambda).
\]

This denominator is strictly positive for every allowed parameter choice. Indeed, it is affine in \(\theta\); its value at \(\theta=0\) is manifestly positive and at \(\theta=1\) equals

\[
(2\lambda+\kappa)c+(h+\lambda)(2h+2\lambda-\kappa)>0.
\]

From the stationary flux equations \(2\lambda p_0=h p_1+\theta\kappa p_2\) and \([2h-\theta\kappa]p_2=(\lambda+c)p_1\), together with normalization, direct elimination yields

\[
\begin{aligned}
p_0(\theta)&=\frac{2h^2+\kappa\theta(c-h+\lambda)}{D_\theta},\\
p_1(\theta)&=\frac{2\lambda(2h-\kappa\theta)}{D_\theta},\\
p_2(\theta)&=\frac{2\lambda(c+\lambda)}{D_\theta}.
\end{aligned}
\]

Every numerator is positive (the first can also be seen as the stationary balance result for an irreducible chain; explicitly, its affine minimum is positive because its endpoint values are \(2h^2\) and \(h(2h-\kappa)+\kappa(c+\lambda)\)). The chain is irreducible because all ordinary extinction, immigration, and rescue rates are positive, hence this is its unique stationary law.

Differentiating the rational expressions gives the **exact** identities

\[
\begin{aligned}
p_0'(\theta)&=\frac{2\kappa\lambda(c+\lambda)(c+h+\lambda)}{D_\theta^2}>0,\\
p_2'(\theta)&=-\frac{2\kappa\lambda(c+\lambda)(c-h-\lambda)}{D_\theta^2},\\
M_\theta'&=-\frac{4c\kappa\lambda(c+\lambda)}{D_\theta^2}<0.
\end{aligned}
\]

The identity \(R_\theta'= -p_0'(\theta)\) proves strict deterioration of regional occupancy. The sign of \(p_2'\) is strictly positive, zero identically, or strictly negative according as \(c<h+\lambda\), \(c=h+\lambda\), or \(c>h+\lambda\). Since the signs hold throughout the compact interval \([0,1]\), all optimizer and equality assertions follow, including the boundary values. This is an algebraic proof for every positive real rate, not an inference from finite sampling.

As an exact example, with \(\lambda=\mu=\kappa=1\) and \(c=1\), \(B_0=1/5\) and \(B_1=2/9\) while \(R_0=3/5\) and \(R_1=5/9\). With the same base rates and \(c=5\), \(B_0=3/7\) and \(B_1=2/5\), whereas \(R_0=5/7\) and \(R_1=3/5\). At \(c=3\), \(B_\theta=1/3\) for every \(\theta\in[0,1]\). These examples confirm the qualitative switch but are not used as proof.

## Verification

The accompanying Python 3 program `verify.py` independently constructs the four-state generator on \(\{00,10,01,11\}\), solves its invariant law with exact rational Gaussian elimination, aggregates the singleton states, and compares the result to all three closed-form probabilities. It also checks endpoint comparisons and the exact critical equality across rational parameter grids. Running `python3 verify.py` prints `PASS 5000 exact rational assertions; 4-state independent generator.` No third-party Python packages are required. The script checks a finite grid; the proof above establishes all universal statements. The code and all inputs needed to rerun the checks are embedded in this package.

## Relationship to prior work

Johst and Drechsler (2003) directly investigate correlated versus uncorrelated disturbance regimes, but their reported outcome is mean time to irreversible extinction in spatially explicit dynamic landscapes. That is not the stationary all-sites-occupied probability in an immigration-supported two-patch Markov chain. Their accessible abstract indicates that correlated disturbances reduce regional persistence, consistent with the regional metric here, but does not imply the joint-occupancy sign reversal. The full text could not be inspected, and priority therefore remains provisional.

Wilcox, Cairns and Possingham (2006) study stochastic habitat disturbance and recovery, with emphasis on metapopulation persistence and quasistationarity. The accessible material does not establish these three exact stationary derivative identities at fixed per-patch catastrophe hazard. The full text could not be inspected; any stronger implicit coverage remains a residual risk.

Keeling (2000) develops a stochastic population-size model and moment closure for dispersal coupling, not the finite two-state-per-patch synchronized catastrophe chain; the available full paper's equations, finite-metapopulation section, and discussion were compared. Cornell and Ovaskainen (2008) give an asymptotic, spatially explicit analysis of *correlated habitat creation* and mean patch occupancy; their accessible complete manuscript explicitly lists spatially correlated extinction among mechanisms **omitted**. Neither framework implies the present fixed-hazard exact all-parameter classification by taking a parameter limit. Literature and mathematical-record searches found no established implication that dominates the stated result. This is not a proof of historical novelty.

## Limitations

The conclusion is exact for two symmetric occupancy states with independent Poisson immigration and rescue, and instantaneously clearing catastrophes under the specified interpolation. It makes no claim about closed metapopulations, mean time to global extinction, finite deadlines, unequal patches, three or more patches, stochastic habitat suitability, delayed recolonization, or empirical outcomes. Because external immigration is positive, state zero is not absorbing; the term *regional occupancy* means positive stationary occupancy, not indefinite persistence. Some highly relevant older primary full texts were not accessible, so historical priority has not been independently established. No independent mathematical audit has been performed.

## References

1. Johst, K., and Drechsler, M. (2003). Are spatially correlated or uncorrelated disturbance regimes better for the survival of species? *Oikos* 103, 449–456. https://doi.org/10.1034/j.1600-0706.2003.12770.x (first public online date verified 2003-10-21).
2. Wilcox, C., Cairns, B. J., and Possingham, H. P. (2006). The role of habitat disturbance and recovery in metapopulation persistence. *Ecology* 87, 855–863. https://doi.org/10.1890/05-0587.
3. Keeling, M. J. (2000). Metapopulation moments: coupling, stochasticity and persistence. *Journal of Animal Ecology* 69, 725–736. https://doi.org/10.1046/j.1365-2656.2000.00430.x.
4. Cornell, S. J., and Ovaskainen, O. (2008). Exact asymptotic analysis for metapopulation dynamics on correlated dynamic landscapes. *Theoretical Population Biology* 74, 209–225. https://doi.org/10.1016/j.tpb.2008.07.003. Authorized author manuscript: https://eprints.whiterose.ac.uk/id/eprint/4943/1/cornells1.pdf.
