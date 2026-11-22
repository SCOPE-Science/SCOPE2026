# A capacity-three correlation threshold in a two-site back-pressure exclusion chain

## Finding

For exactly two sites with common capacity \(c\in\{1,2,3\}\), common arrival and departure rate \(t\in(0,1]\), and unit-rate back-pressure hopping, the stationary occupation covariance \(C_c(t)=\operatorname{Cov}_{\pi_{c,t}}(Q_1,Q_2)\) is

\[
C_1(t)=\frac{1-2t}{(2t+3)^2},\qquad
C_2(t)=-\frac{8t^3+16t^2-8t-11}{(4t^2+6t+5)^2},
\]

\[
C_3(t)=-\frac{2(64t^7+368t^6+552t^5+114t^4-439t^3-467t^2-177t-23)}{(16t^4+32t^3+42t^2+31t+7)^2}.
\]

The capacity-one covariance is positive below \(t=1/2\), zero there, and negative above. The capacity-two covariance has the analogous unique zero at \(t=t_2\), the unique positive root of

\[
8t_2^3+16t_2^2-8t_2-11=0,\qquad 0.885<t_2<0.886.
\]

The capacity-three covariance is **strictly positive** for all \(0<t\le1\). In particular, at the maximal allowed common boundary rates, \(t=1\),

\[
C_1(1)=-\frac1{25},\qquad C_2(1)=-\frac1{45},\qquad C_3(1)=\frac1{1024}.
\]

Thus \(c=3\) is the *smallest positive integer capacity* with positive stationary cross-site occupation covariance at \(t=1\). This is a capacity-driven reversal of the elementary one-floor exclusion anticorrelation. No assertion is made about the sign for arbitrary \(c\ge4\) or longer chains.

## Assumptions and scope

The continuous-time Markov process has occupations \((x,y)\in\{0,\ldots,c\}^2\), with three independent families of attempted transitions:

- Arrival \((x,y)\to(x+1,y)\) at rate \(t\) when \(x<c\).
- Exit \((x,y)\to(x,y-1)\) at rate \(t\) when \(y>0\).
- Rightward hop \((x,y)\to(x-1,y+1)\) at rate one when \(x>y\).

The last condition ensures a hop cannot overfill the receiving site. Only \(0<t\le1\) is considered, with no arrival or departure conditioning beyond the capacity restrictions. \(\pi_{c,t}\) denotes the unique stationary distribution. All covariance statements are about simultaneous stationary occupations, not time-lagged correlations or current correlations.

## Proof

**Recurrent state space.** Starting from the empty state, all transitions preserve \(y\le x+1\), since a permitted hop has \(x\ge y+1\), and hence its resulting occupations satisfy \(y+1\le(x-1)+1\). For each of \(c=1,2,3\), exhaustive directed reachability on the finite graph yields precisely

\[
\Omega_c=\{(x,y):0\le x,y\le c,\ y\le x+1\},
\]

with respective cardinalities \(4,8,13\). Each state communicates with \((0,0)\): choose exits while \(y>0\), hops whenever \(x>y\), and repeat until empty, omitting arrivals. This also drains states outside \(\Omega_c\). Therefore \(\Omega_c\) is the unique closed irreducible class and supports the unique stationary law.

**Exact stationary weights.** Write \(\pi_{c,t}(x,y)=w_c(x,y)/Z_c(t)\). Unlisted weights are zero. The following polynomials yield an exact solution to all stationarity equations \(w_c Q=0\), with \(Q\) the generator specified above.

| State \((x,y)\) | \(w_1(x,y)\) | \(w_2(x,y)\) | \(w_3(x,y)\) |
|---|---:|---:|---:|
| \((0,0)\) | \(1\) | \(1\) | \(3t+1\) |
| \((0,1)\) | \(1\) | \(1\) | \(3t+1\) |
| \((1,0)\) | \(2t\) | \(2t\) | \(2t(3t+1)\) |
| \((1,1)\) | \(1\) | \(2t+1\) | \((2t+1)(3t+1)\) |
| \((1,2)\) | — | \(1\) | \(4t^2+3t+1\) |
| \((2,0)\) | — | \(4t^2\) | \(4t^2(2t+1)\) |
| \((2,1)\) | — | \(2t\) | \(2t(4t^2+3t+1)\) |
| \((2,2)\) | — | \(1\) | \((2t+1)(3t+1)\) |
| \((2,3)\) | — | — | \(3t+1\) |
| \((3,0)\) | — | — | \(8t^3(2t+1)\) |
| \((3,1)\) | — | — | \(4t^2(2t+1)\) |
| \((3,2)\) | — | — | \(2t(3t+1)\) |
| \((3,3)\) | — | — | \(3t+1\) |

Adding the weights gives

\[
Z_1=2t+3,\quad Z_2=4t^2+6t+5,\quad
Z_3=16t^4+32t^3+42t^2+31t+7.
\]

Every displayed weight is strictly positive on the recurrent states for positive \(t\). Define the unnormalized moment polynomials

\[
M_1=\sum_{(x,y)\in\Omega_c}xw_c(x,y),\quad
M_2=\sum_{(x,y)\in\Omega_c}yw_c(x,y),\quad
M_{12}=\sum_{(x,y)\in\Omega_c}xyw_c(x,y).
\]

The exact covariance numerator is \(N_c(t)=Z_cM_{12}-M_1M_2\), so \(C_c=N_c/Z_c^2\). Polynomial multiplication and subtraction give

\[
N_1=1-2t,\quad N_2=11+8t-16t^2-8t^3,
\]

\[
N_3=46+354t+934t^2+878t^3-228t^4-1104t^5-736t^6-128t^7.
\]

These are the claimed closed expressions.

**Exact sign classification.** The cubic \(P_2(t)=8t^3+16t^2-8t-11\) has one sign change in the sequence of its nonzero descending coefficients. By Descartes' rule, it has at most one positive root; its values at zero and one have opposite signs, so it has exactly one root in \((0,1)\). The rational evaluations \(P_2(885/1000)<0<P_2(886/1000)\) give the stated enclosure. The septic

\[
P_3(t)=64t^7+368t^6+552t^5+114t^4-439t^3-467t^2-177t-23
\]

also has exactly one sign change; it is negative at zero and positive for sufficiently large arguments, so it has exactly one positive root. Since \(P_3(1)=-8\), that root lies strictly above one. Thus \(N_3(t)=-2P_3(t)>0\) throughout \((0,1]\). The signs at \(t=1\) follow by substituting into the exact fractions, completing the minimum-capacity conclusion.

## Verification

The accompanying self-contained `verify.py` uses integer polynomial arithmetic and exact rational evaluation, with no third-party dependencies. Run `python3 verify.py`. It enumerates all directed graph states for the three capacities, checks irreducibility and the exact polynomial stationarity equations, recomputes all three normalizers and covariance numerators, verifies the three fractions at unit rates, and checks the sign-variation and endpoint certificates. The enumeration is exhaustive for the expressly stated finite capacities and is not claimed as evidence for arbitrary capacities.

## Relationship to prior work

Baryshnikov and Stolyar [1] introduced the multi-floor back-pressure TASEP with capacities and boundary rates used here. Their main analyses concern one-sided and large-length stationary flux and density phases, including high-capacity behavior; those results are not rederived or claimed as new. The complete accessible manuscript was inspected, including model definitions, main theorems, simulation discussion, and concluding conjectures; no two-site finite-capacity covariance formula or this sign classification was found. Stolyar [2] examines back-pressure tandem queues without a finite per-site capacity, primarily their large-length scaling, so neither its assumptions nor its claimed conclusions imply the specified capacity-one-to-three reversal. The classical one-floor matrix-product literature reviewed in [3] applies to \(c=1\); the capacity-one expression here is a baseline, not the novelty claim.

The contribution is the *complete symmetric-boundary finite-capacity correlation sign classification for \(c=1,2,3\)*, especially the previously unreported smallest-capacity sign boundary at maximal boundary rates. Relevant public mathematical-index records concerning site covariance reversals in different exclusion/reset processes and three-site mass exchange were compared by their hypotheses and conclusions; they neither have this back-pressure generator nor provide an implication to the stated formulas.

## Limitations

Only two sites, capacities one through three, equal boundary rates in \((0,1]\), and equal-time stationary covariance are covered. Nothing here proves a universal sign law for higher capacities, unequal boundary rates, finite longer chains, or the infinite-chain limit. The spectral and finite-state calculations are exact for these finite cases; the decimal location of the cubic root is explanatory and is not part of the proof. Literature checking cannot exclude unindexed or otherwise inaccessible earlier two-node queue calculations. The calculations do not certify publication priority or constitute independent scientific validation.

## References

1. Y. Baryshnikov and A. Stolyar, *Multi-floor generalization of TASEP*, arXiv:2603.13610, first public March 13, 2026. https://arxiv.org/abs/2603.13610
2. A. Stolyar, *Large number of queues in tandem: Scaling properties under back-pressure algorithm*, arXiv:1002.3940, first public February 20, 2010. https://arxiv.org/abs/1002.3940
3. R. A. Blythe and M. R. Evans, *Nonequilibrium steady states of matrix-product form: a solver's guide*, arXiv:0706.1678 (2007). https://arxiv.org/abs/0706.1678
