# An all-or-nothing pollen-packet law at fixed mean receipt

## Finding

Consider an idealized flower that sets its full complement of seeds if and only if it receives at least \(r\) effective pollen grains, where \(r\geq2\) is an integer. A pollen dispersal unit (packet) has an integer size \(k\geq1\). With the mean number of grains reaching the stigma held fixed at \(\lambda>0\), assume packets arrive independently in a Poisson count with mean \(\lambda/k\). The probability of meeting the full-seed-set threshold is
\[
S_k(\lambda,r)=\Pr\{kN_k\geq r\}
=\Pr\{\operatorname{Pois}(\lambda/k)\geq\lceil r/k\rceil\}.
\]

**All-or-nothing packet theorem.** Among **all** positive integer sizes \(k\), only a monad, \(k=1\), and a threshold-sized packet, \(k=r\), can maximize \(S_k\). Every other size is strictly inferior to the better of these two. For every \(r\geq2\), there exists exactly one \(\lambda_r>0\) satisfying
\[
\exp\!\left(\frac{r-1}{r}\lambda_r\right)
=\sum_{j=0}^{r-1}\frac{\lambda_r^j}{j!}.
\]
The unique maximizing packet is \(k=r\) when \(0<\lambda<\lambda_r\), and \(k=1\) when \(\lambda>\lambda_r\). Exactly these two sizes tie at \(\lambda=\lambda_r\). As \(r\to\infty\),
\[
\frac{\lambda_r-r}{\sqrt r}\longrightarrow
\Phi^{-1}(1-e^{-1})=0.337474963764\ldots,
\]
where \(\Phi\) denotes the standard normal cumulative distribution function.

## Assumptions and scope

The packet size \(k\) is deterministic and uniform across packet arrivals. Different arriving packets are independent, the count is Poisson, and a received packet deposits all \(k\) effective grains on the same recipient stigma without degradation, incompatibility or excess-capacity losses before threshold evaluation. The receipt budget is a fixed **expected total grain count** \(\mathbb E[kN_k]=\lambda\), rather than a fixed number of packets. The outcome considered is the all-or-none event of reaching the \(r\)-grain threshold, **not** expected seed number below the threshold and not expected paternal diversity. No assumptions are made about grain production cost, plant genotype, pollinator preferences or physical dispersal beyond the stipulated Poisson packet receipt. The result does not cover heterogeneous or randomly varying packet sizes, non-Poisson packet counts, or changing delivery efficiency with size.

All equalities and inequalities are exact for every integer \(r\geq2\), every real \(\lambda>0\), and every integer \(k\geq1\). There is no finite cutoff on the allowed packet sizes.

## Proof

**1. Reduce every intermediate packet to a Poisson tail with a proportionally larger mean.** Put \(a=\lambda/r>0\) and for each positive integer \(n\) define
\[
Q_n(a)=\Pr\{\operatorname{Pois}(na)\geq n\}.
\]
For \(1\leq k\leq r\), set \(m=\lceil r/k\rceil\). Then \(m\leq r\), and \(mk\geq r\) gives \(\lambda/k\leq ma\). Strict monotonicity of the Poisson upper tail in its positive mean implies
\[
S_k(\lambda,r)\leq Q_m(a).
\]
For \(k=1\) the inequality is equality with \(m=r\); for \(k=r\) it is equality with \(m=1\). Every integer \(k\) strictly between \(1\) and \(r\) gives \(2\leq m\leq r-1\). The issue is therefore whether \(Q_m(a)\) can exceed both endpoints \(Q_1(a)\) and \(Q_r(a)\).

**2. A strict discrete valley lemma.** For fixed \(a>0\), the sequence \((Q_n(a))_{n\geq1}\) has at most one change of successive-difference sign, and that change can only be from negative to positive. In particular, for integers \(1<m<r\),
\[
Q_m(a)<\max\{Q_1(a),Q_r(a)\}.
\]
To prove this, take independent \(X\sim\operatorname{Pois}(na)\) and \(Y\sim\operatorname{Pois}(a)\). As \(X+Y\sim\operatorname{Pois}((n+1)a)\), direct separation according to the value of \(X\) yields
\[
Q_{n+1}-Q_n
=-\Pr\{X=n\}\Pr\{Y=0\}
+\sum_{j=2}^{n+1}\Pr\{X=n+1-j\}\Pr\{Y\geq j\}.
\]
Every denominator \(\Pr\{X=n\}\) is positive. After dividing by it, write the ratio as
\[
R_n(a)=\frac{Q_{n+1}(a)-Q_n(a)}{\Pr\{X=n\}}
=-e^{-a}+
\sum_{j=2}^{n+1}a^{-(j-1)}
\left(\prod_{\ell=0}^{j-2}\left(1-\frac{\ell}{n}\right)\right)
\Pr\{Y\geq j\}.
\]
For fixed \(j\geq2\), the displayed product is nondecreasing with \(n\) whenever \(n\geq j-1\), and strictly increasing for \(j\geq3\). Also, each step from \(n\) to \(n+1\) introduces the strictly positive new term with \(j=n+2\). Hence \(R_{n+1}(a)>R_n(a)\) for all \(n\geq1\). Since \(Q_{n+1}-Q_n\) has the same sign as \(R_n\), the differences can only progress from negative through at most one zero to positive. Consequently, there is no interior maximum, including a tied interior maximum: on each side of a possible minimum the sequence is strictly monotone, except for at most one equality at the minimum. This proves the strict endpoint inequality.

**3. Exclude every other packet size.** For \(1<k<r\), step 1 and the strict valley lemma give
\[
S_k\leq Q_m<\max\{Q_1,Q_r\}
=\max\{S_1,S_r\}.
\]
If \(k>r\), a single packet suffices and \(S_k=1-e^{-\lambda/k}\), strictly less than \(S_r=1-e^{-\lambda/r}\). This proves endpoint-only global optimality without a finite search over packet sizes.

**4. Prove the unique switching budget and the equality cases.** The two survivors are
\[
S_1=1-e^{-\lambda}\sum_{j=0}^{r-1}\frac{\lambda^j}{j!},
\qquad S_r=1-e^{-\lambda/r}.
\]
Put \(P(\lambda)=\sum_{j=0}^{r-1}\lambda^j/j!\) and \(H(\lambda)=e^{(r-1)\lambda/r}/P(\lambda)\). The sign of \(S_r-S_1\) is the sign of \(1-H(\lambda)\). Differentiating gives
\[
\frac{H'(\lambda)}{H(\lambda)}
=-\frac1r+\frac{\lambda^{r-1}}{(r-1)!P(\lambda)}.
\]
The second term is strictly increasing from zero to one, because its reciprocal is \((r-1)!\sum_{j=0}^{r-1}\lambda^{j-(r-1)}/j!\), a strictly decreasing positive function on \((0,\infty)\). Therefore \(H\) first strictly decreases and then strictly increases. It starts at \(H(0)=1\), initially drops below one and eventually diverges to infinity (exponential divided by polynomial). Thus precisely one positive crossing \(H(\lambda_r)=1\) exists, with \(H<1\) before it and \(H>1\) after it. Combined with step 3, this proves the stated unique maximizer and the exact two-way tie at the crossing.

**5. Locate the high-threshold switching budget.** For each fixed real \(x\), choose \(\lambda=r+x\sqrt r\), which is positive for all sufficiently large \(r\). The Poisson central limit theorem yields
\[
S_1(\lambda,r)=\Pr\{\operatorname{Pois}(\lambda)\geq r\}
\longrightarrow\Phi(x),
\]
while \(S_r(\lambda,r)=1-e^{-\lambda/r}\longrightarrow1-e^{-1}\). The unique positive crossover proven in step 4 has the sign orientation \(S_r>S_1\) below it and \(S_1>S_r\) above it. For any \(\varepsilon>0\), evaluate the two limiting expressions at \(x=\Phi^{-1}(1-e^{-1})\pm\varepsilon\) and apply the sign orientation to bracket \(\lambda_r\) between the corresponding two budgets for all sufficiently large \(r\). Dividing by \(\sqrt r\), and then letting \(\varepsilon\downarrow0\), proves the limit.

## Verification

The reproducible standalone script `verification/check_packet.py` independently evaluates many Poisson threshold tails, verifies the strict endpoint superiority for intermediate packet sizes, checks the exact rational monotonicity of the coefficients of the discrete valley lemma, and brackets the two-way crossover for selected threshold values. It also checks the central-limit scaling numerically as a diagnostic. Run with `python3 verification/check_packet.py` from the directory containing this result; no third-party modules are required. The script reports its assertion count and numerical crossover brackets. Its finite computations are **diagnostic checks only**; the proof above establishes the statements for the full infinite ranges.

## Relationship to prior work

Timerman et al. (2014) document the biological range of aggregated pollen dispersal units, from individual grains to large clusters, including their implications for multiovulate flowers. Their full article provides empirical and biological context but does not give this Poisson receipt-budget theorem. Schreiber et al. (2015; first online in 2014) analyze multiscale variation in pollen receipt and optimal plant resource allocation, rather than the uniform packet-size decision with a fixed mean receipt budget studied here. Heiling et al. (2023) optimize pollen package size using pollinator grooming and reward preferences for male donation; their objective and event model are different from the present full-threshold success probability. Published mathematical comparisons to stochastic packet coupon collection and compound-Poisson concentration concern different payoffs, so their conclusions do not imply the strict monad-versus-quorum-packet endpoint theorem.

The closest general botanical review, Harder and Johnson (2008), discusses the evolution of aggregated pollen. Only its abstract was accessible for the present comparison, so overlap with its uninspected full text and older supporting literature remains a historical-priority risk. The discovery of the theorem is not a claim of exhaustive literature coverage or independent peer review.

## Limitations

The success function deliberately ignores partial seed set, resource investment, pollen incompatibility, pollinator grooming, pollen fragmentation, differential transport of large units, within-flower saturation details, and interactions among competing pollen donors. Any of those may make a different \(k\) optimal. The theorem is not an empirical fit, evolutionary prediction, or field intervention prescription. The asymptotic law concerns the specific fixed-mean Poisson packet model, and no non-Poisson or heterogeneous-packet generalization is established. The self-review is not independent validation.

## References

1. Timerman, D., Greene, D. F., Ackerman, J. D., Kevan, P. G., and Nardone, E. (2014). *Pollen Aggregation in Relation to Pollination Vector*. *International Journal of Plant Sciences*, 175, 681–687. Electronically published May 21, 2014. https://doi.org/10.1086/676301 . Author-manuscript text: https://www.academia.edu/28596633/Pollen_Aggregation_in_Relation_to_Pollination_Vector .
2. Schreiber, S. J., Rosenheim, J. A., Williams, N. W., and Harder, L. D. (2015). *Evolutionary and Ecological Consequences of Multiscale Variation in Pollen Receipt for Seed Production*. *The American Naturalist*, 185, E14–E29. Electronically published December 12, 2014. https://doi.org/10.1086/678982 . Full text: https://rosenheim.faculty.ucdavis.edu/wp-content/uploads/sites/137/2014/09/Schreiber-et-al.-2015.pdf .
3. Heiling, J. M., Irwin, R. E., and coauthors (2023). *Conflicting constraints on male mating success shape reward size in pollen-rewarding plants*. *American Journal of Botany*. https://doi.org/10.1002/ajb2.16158 .
4. Harder, L. D., and Johnson, S. D. (2008). *Function and Evolution of Aggregated Pollen in Angiosperms*. *International Journal of Plant Sciences*. https://doi.org/10.1086/523364 . Full text not inspected.
