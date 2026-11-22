# Three sharp six-patch colonization layouts under an endpoint-refuge reward

## Finding

**Theorem (complete integer design phase diagram).** A permanently occupied source connects to two independent directed, outward-only habitat chains. There are exactly six additional patches, divided into two nonempty chains of integer lengths \(m\) and \(6-m\). The last patch of each chain is a designated terminal refuge. Every colonization event, once its immediate predecessor is occupied, occurs after an independent exponential waiting time of common rate \(\lambda>0\); colonies never disappear. At a fixed deadline \(T>0\), reward one unit per occupied non-source patch plus \(R\ge0\) extra units if **at least one** of the two terminal refuges has been reached. Let \(\tau=\lambda T\).

Up to exchange of the two arms, all global maximizers are classified by two explicit, strictly ordered positive reward thresholds:
\[
\begin{aligned}
R_{23}(\tau)&=\frac{2\tau e^{\tau}}{\tau^2+4\tau+6},\\
R_{12}(\tau)&=\frac{\tau e^{\tau}(\tau^2+4\tau+12)}{3(\tau+2)(\tau^2+2\tau+4)},\\
&0<R_{23}(\tau)<R_{12}(\tau)\qquad(\tau>0).
\end{aligned}
\]
For \(0\le R<R_{23}\), the unique optimal unordered split is \((3,3)\); at \(R=R_{23}\), exactly \((3,3)\) and \((2,4)\) tie. For \(R_{23}<R<R_{12}\), exactly \((2,4)\) is optimal. At \(R=R_{12}\), exactly \((2,4)\) and \((1,5)\) tie; for \(R>R_{12}\), exactly \((1,5)\) is optimal. No triple tie or other maximizer occurs.

Consequently **for every positive deadline there is a nonempty reward interval in which the strictly intermediate, unequal \((2,4)\) allocation beats both the most balanced and the most concentrated two-arm layouts**. Six is the least number of non-source patches for which an unordered positive two-arm split can be neither extreme nor most balanced.

## Assumptions and scope

The source is occupied at time zero. The two terminal refugia are *different* patches and either one suffices for the reward; the extra reward is not paid twice if both are occupied. Arms contain \(m\) and \(6-m\) susceptible patches, respectively, where \(m\in\{1,2,3,4,5\}\). Each site can receive a first successful colonist only from the immediately previous site in its own arm; the successive exponential waiting times are independent across edges and across arms. After colonization a patch remains occupied through the deadline. Each colonized patch contributes one unit even if it is an endpoint. The optional refuge credit \(R\) is dimensionless in patch-equivalent units. There is no competition for a shared finite propagule pool, no failures, extinction, backward dispersal, unequal transition rates, habitat quality variation or spatial travel-time calibration. The objective is **expected terminal occupied patch count plus a weighted terminal-reach probability**, not a survival quantile or asymptotic population growth measure. We do not assume or claim that adding a physical stepping stone would slow movement in a real landscape; a modeled link is one obligatory sequential establishment stage.

## Proof

**1. Exact arrival and reward law.** On an uncapped chain, independent rate-\(\lambda\) exponential interarrival times generate a Poisson counting process. Thus, writing \(Z\sim\operatorname{Pois}(\tau)\), the number of occupied sites in an arm of length \(k\) at time \(T\) has law \(\min(Z,k)\). The independent arms have independent counts \(Z_1,Z_2\), because their edge clocks are disjoint and independent. Put
\[
p_j=e^{-\tau}\frac{\tau^j}{j!},\quad Q_k=\sum_{j=0}^{k-1}p_j=\Pr(Z<k),\quad H_k=\sum_{j=1}^k(1-Q_j)=\mathbb E\min(Z,k).
\]
With an arm-length split \((m,6-m)\), expected reward is exactly
\[
U_m(\tau,R)=H_m+H_{6-m}+R\bigl(1-Q_m Q_{6-m}\bigr).
\tag{1}
\]
The last term is the probability that at least one arm has reached its terminal site, using independence. Symmetry \(U_m=U_{6-m}\) reduces every possible design to \(m=1,2,3\).

**2. The only two adjacent comparisons.** Let \(A_1=\sum_{j=2}^4p_j\), \(A_2=p_3\), and
\[
B_1=Q_2Q_4-Q_1Q_5,\qquad B_2=Q_3^2-Q_2Q_4.
\]
Subtracting (1) gives exactly
\[
U_2-U_1=A_1-RB_1,\qquad U_3-U_2=A_2-RB_2.
\tag{2}
\]
The two expected-coverage increments \(A_i\) are strictly positive. Direct expansion of the finite Poisson sums, with no approximation, yields
\[
\begin{aligned}
A_1&=e^{-\tau}\frac{\tau^2(\tau^2+4\tau+12)}{24},\\
A_2&=e^{-\tau}\frac{\tau^3}{6},\\
B_1&=e^{-2\tau}\frac{\tau(\tau+2)(\tau^2+2\tau+4)}{8},\\
B_2&=e^{-2\tau}\frac{\tau^2(\tau^2+4\tau+6)}{12}.
\end{aligned}
\tag{3}
\]
All are strictly positive for \(\tau>0\). Equations (2) and (3) show that \(U_2-U_1\) changes sign exactly at \(R=A_1/B_1=R_{12}\), and \(U_3-U_2\) exactly at \(R=A_2/B_2=R_{23}\).

**3. The two changes have strict order for every deadline.** Cancel common positive exponentials in the cross product. A fully explicit polynomial certificate is
\[
\begin{split}
R_{12}-R_{23}
=\frac{\tau e^{\tau}(\tau^4+2\tau^3+10\tau^2+24\tau+24)}
{3(\tau+2)(\tau^2+2\tau+4)(\tau^2+4\tau+6)}>0.
\end{split}
\tag{4}
\]
Every factor in the denominator and every coefficient in the numerator are strictly positive on \(\tau>0\), proving both that the intermediate-reward interval is nonempty and that there cannot be a triple tie.

**4. Exhaustion and equalities.** If \(R<R_{23}<R_{12}\), both differences in (2) are positive and \(U_3>U_2>U_1\). If \(R_{23}<R<R_{12}\), the first is positive and the second negative, so \(U_2\) exceeds both alternatives. If \(R>R_{12}>R_{23}\), both differences are negative and \(U_1>U_2>U_3\). At the two thresholds, (2) gives exactly the two adjacent ties and strict inequality against the third. Symmetry and the complete finite list \(m=1,2,3\) show global optimality without assuming a priori that a local optimum must be global.

**5. The sharp smallest layout count.** For every total non-source site count \(N\le5\) and both arms required positive, the only unordered splits are \((m,N-m)\) with \(1\le m\le\lfloor N/2\rfloor\). There are at most two such splits. If there are two, they are precisely the extreme \((1,N-1)\) and the most balanced \((\lfloor N/2\rfloor,\lceil N/2\rceil)\); thus a distinct interior layout cannot exist. At \(N=6\), \((2,4)\) is a third distinct layout and is uniquely optimal for the nonempty interval in (4), proving sharpness. \(\square\)

## Verification

At \(\tau=1\), the two thresholds are
\[
R_{23}(1)=\frac{2e}{11}=0.494233059720\ldots,\qquad
R_{12}(1)=\frac{17e}{63}=0.733504620378\ldots.
\]
For the exact refuge credit \(R=3/5\), the three expected rewards, in order \((1,5),(2,4),(3,3)\), are approximately \(2.011511800830\), \(2.058940000562\), and \(2.045818834977\), giving a strict \((2,4)\) winner.

The standalone Python standard-library checker `verify.py` performs independent exact rational-polynomial arithmetic on the unnormalized Poisson sums. It verifies all four identities in (3) and the positive-coefficient cross-product certificate used in (4), then checks all three optimality regimes and both two-design tie cases across nine positive deadlines by direct evaluation of (1). The completed checker reports 124 assertions passing. Finite numerical tests are supplemental; the universal statement for every real \(\tau>0\) and \(R\ge0\) follows from the exact algebra and sign argument in the proof.

## Relationship to prior work

Seymour and Altermatt (2014) experimentally compared active colonization in linear and dendritic aquatic microcosms with fixed total network volume and length; they did not optimize the allocation of an integer number of serial establishment stages between two arms or an explicit endpoint-access reward. Hock and Mumby (2015) developed multiplicative dispersal-path reliability and assessed maximum-reliability routes in networks with stochastic links. Their full text discusses stochastic successive colonization and target access, but the objective is identifying likely paths, not combining expected finite-time occupancy and a union-of-terminal-reach bonus under a fixed six-patch arm-length allocation.

The general Poisson-arrival/Erlang identity and the finite-network model are standard tools and are not claimed novel. The contribution claimed here is the global three-regime integer design phase diagram (2)–(4), with its strict nonextreme, nonbalanced optimum at all positive deadlines. Distinct previous analyses of optimizing directional colonization rates to delay extinction, stochastic reliability of fixed habitat configurations and continuous gap lengths for founding-quorum establishment do not imply this fixed-deadline six-stage design tradeoff without a new comparison. Complete historical coverage of general network-reliability optimization remains a limitation.

## Limitations

The result is exact only for six non-source sites split into two strictly positive directed chains, equal memoryless colonization rates, independent edge clocks, irreversible occupancy and a linear scalarization of two objectives. It does not claim optimality under common-source propagule competition, multi-target correlated dispersal, different edge rates, alternative site values, or any larger number of sites. The sharpness at six refers to the first **combinatorially possible third unordered positive split**, not a claim of nontrivial impossibility for smaller graphs under other topology classes. The model does not supply an empirical recommendation for constructing habitat corridors; the assumption that each extra site entails one extra sequential colonization stage is a modeling choice. Historical originality is based on the sources inspected and may be superseded by an equivalent general stochastic-network design theorem. Independent validation has not been performed.

## References

1. M. Seymour and F. Altermatt, “Active colonization dynamics and diversity patterns are influenced by dendritic network connectivity and species interactions,” *Ecology and Evolution* 4 (2014), 1243–1254. First publicly available 2014-03-12. https://doi.org/10.1002/ece3.1020 . Full text: https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.1020 .
2. K. Hock and P. J. Mumby, “Quantifying the reliability of dispersal paths in connectivity networks,” *Journal of the Royal Society Interface* 12 (2015), article 20150013. https://doi.org/10.1098/rsif.2015.0013 . Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC4387532/ .
