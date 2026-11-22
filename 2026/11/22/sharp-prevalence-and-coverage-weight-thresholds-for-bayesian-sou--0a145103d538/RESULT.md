# Sharp prevalence and coverage-weight thresholds for Bayesian source localization on a three-building wastewater junction

## Finding

**Theorem (complete submodularity phase diagram).** Consider the binary, noiseless, independent-source junction and the mean Bayes-accuracy-plus-outbreak-coverage objective described below. With three buildings of equal independent outbreak probability \(0<p<1/2\) and any coverage weight \(\lambda\ge0\), the sensor-set objective fails to be submodular whenever \(0<p<1/5\), regardless of how much outbreak coverage is rewarded. This obstruction vanishes at the sharp prevalence \(p=1/5\). For \(1/5\le p<1/2\), the objective is submodular if and only if \(\lambda\ge\lambda_{\mathrm c}(p)\), with the explicit sharp phase boundary

\[
\lambda_{\mathrm c}(p)=
\begin{cases}
(1-3p)/3,&1/5\le p\le(5-\sqrt{17})/4,\\
2p(1-p)/3,&(5-\sqrt{17})/4\le p\le(3-\sqrt5)/2,\\
(p^2-7p+3)/3,&(3-\sqrt5)/2\le p\le(7-\sqrt{37})/2,\\
0,&(7-\sqrt{37})/2\le p<1/2.
\end{cases}
\]

Consequently, the unweighted objective (\(\lambda=1\)) is submodular exactly when \(p\ge1/5\), while for \(p<1/5\) no finite nonnegative coverage weight can restore submodularity. Three buildings are the minimum number for this weight-irreparable phenomenon: with two buildings submodularity holds whenever \(\lambda\ge\max\{0,(1-3p)/2\}\).

At the concrete prevalence \(p=1/10\), the submodularity inequality for the two *leaf* sensors conditioned on the pooled-junction sensor fails by exactly \(3/200\) in objective units, for every \(\lambda\ge0\). Its failure is not affected by the coverage term, because the junction already covers every possible outbreak.

A complementary all-sizes formula quantifies when a pooled-junction sensor can improve *source classification*, despite detecting outbreaks. For \(n\ge1\) buildings and \(k<n\) already observed buildings, the pooled-sensor marginal gain in expected correct-source fraction is

\[
\frac{n-k}{n}(1-p)^k\big[2p-1+(1-p)^{n-k}\big]_+,\qquad [u]_+=\max\{u,0\}.
\]

For every \(n\ge3\), this gain is zero when no leaves are observed and \(0<p\le p_n\), where \(p_n\in(0,1/2)\) is the unique positive solution of \(1-(1-p_n)^n=2p_n\). For \(n=3\), \(p_n=(3-\sqrt5)/2\).

## Assumptions and scope

There are \(n\) upstream building-source indicators \(X_1,\ldots,X_n\), independent and identically Bernoulli\((p)\), with \(0<p<1/2\). An available leaf sensor \(s_i\) reports \(X_i\) perfectly; a single junction sensor \(r\) reports exactly \(R=X_1\lor\cdots\lor X_n\). The candidate sensor universe is \(\{s_1,\ldots,s_n,r\}\); sensor selection has no cost term. No test noise, dilution, false detection, transmission across buildings, or concentration limits are modeled.

Given observations from a chosen sensor set \(W\), predict each individual \(X_i\) by its Bayes-optimal binary decision, \(\widehat X_i=1\) if its posterior exceeds \(1/2\), and \(0\) otherwise (including ties). Define

\[
 A(W)=\frac1n\sum_{i=1}^n\Pr(\widehat X_i=X_i),\quad
 C(W)=\Pr(\text{at least one positive selected sensor}),\quad
 J_\lambda(W)=A(W)+\lambda C(W),\quad\lambda\ge0.
\]

The accuracy is mean *per-building* 0–1 accuracy (Hamming accuracy), not a joint all-labels MAP event, F1 score, mutual information, or a sampled finite-scenario estimate. The coverage term is the probability that any true outbreak is detected; it has no concentration threshold. Submodularity means \(J(S\cup\{a\})+J(S\cup\{b\})\ge J(S)+J(S\cup\{a,b\})\) for all \(S\) and distinct \(a,b\notin S\).

## Proof

**1. Exact Bayesian root gain.** Let \(q=1-p\). When \(k\) direct leaf sensors are observed, each is classified correctly. Each of the remaining \(n-k\) sites is predicted negative without the junction observation, giving \(A=1-p+kp/n\). The junction reading is redundant unless all \(k\) observed leaves are negative, which occurs with probability \(q^k\). Conditional on that event, writing \(m=n-k\), the junction is positive with probability \(u_m=1-q^m\). Each unobserved leaf then has posterior infection probability \(p/u_m\). If \(u_m\ge2p\), the Bayes decision remains negative. Otherwise it flips after a positive junction reading and its *unconditional* expected correctness gain, conditional on the earlier leaf observations, is \(2p-u_m\). Multiply by \(q^k\), by the \(m\) indistinguishable unobserved leaves, and divide by \(n\) to obtain

\[
 G_{n,k}=\frac{n-k}{n}q^k[2p-1+q^{n-k}]_+.
\]

The root coverage gain after \(k\) directly observed leaves is \(q^k-q^n\). Hence, with \(A_k\) any set of \(k\) leaf sensors,

\[
 J_\lambda(A_k)=1-p+\frac{kp}{n}+\lambda(1-q^k),\qquad
 J_\lambda(A_k\cup\{r\})=J_\lambda(A_k)+G_{n,k}+\lambda(q^k-q^n).
\]

For \(k=0\), \(1-q^n=p\sum_{j=0}^{n-1}q^j\). If \(n\ge3\), the sum strictly decreases from \(n>2\) toward \(2-2^{1-n}<2\) as \(p\) rises from zero to one half; therefore it equals 2 at exactly one \(p_n\), and the asserted zero-gain interval follows. For \(n=3\), its defining polynomial is \(p^2-3p+1=0\).

**2. The complete three-leaf table.** Put \(D_k=3G_{3,k}\) for \(0\le k\le3\). The preceding formula gives

\[
 D_0=3p[-1+3p-p^2]_+,\quad
 D_1=2p^2q,\quad D_2=pq^2,\quad D_3=0.
\]

There are only two kinds of submodularity inequalities, because leaves are exchangeable: two leaves with either the root absent or present, and one leaf plus the root. Without the root, \(A(A_k)\) is affine in \(k\), while \(C(A_k)=1-q^k\) is concave, so every leaf–leaf inequality holds. With the root present, coverage is constant at \(1-q^3\), so the remaining inequalities are *exactly*

\[
 D_2-2D_1+D_0\le0,\qquad D_3-2D_2+D_1\le0.
\]

The latter is \(2pq(2p-1)<0\). For \(p\le p_3=(3-\sqrt5)/2\), the former equals \(pq(1-5p)\). For \(p\ge p_3\), it equals \(p(p+2)(2p-1)<0\). Therefore the leaf–leaf conditions are satisfied **if and only if** \(p\ge1/5\). When \(p<1/5\), \(D_2-2D_1+D_0>0\); choosing the pooled sensor as the initial set and comparing the next two leaf sensors violates submodularity by \((D_2-2D_1+D_0)/3=pq(1-5p)/3\), independently of \(\lambda\). For \(p=1/10\), this is \(3/200\).

**3. Root–leaf inequalities and sharp weight.** The root's marginal with \(k\) directly installed leaf sensors is \(D_k/3+\lambda(q^k-q^3)\). Its diminishing-return condition when one further leaf is installed is precisely

\[
 \lambda\ge\frac{D_{k+1}-D_k}{3pq^k},\qquad k=0,1,2.
\]

The \(k=2\) right side is strictly negative. The remaining lower bounds are

\[
 L_0=\frac{2p^2q-D_0}{3p},\qquad L_1=\frac{1-3p}{3}.
\]

For \(p\le p_3\), \(L_0=2pq/3\); beyond \(p_3\), \(L_0=(p^2-7p+3)/3\). For \(p\ge1/5\), comparing \(L_0\), \(L_1\), and zero yields the phase boundary shown above: \(L_1=L_0\) at \((5-\sqrt{17})/4\), and \(L_0=0\) at \((7-\sqrt{37})/2\). (The other quadratic roots are outside the prescribed probability interval.) This proves both necessity and sufficiency for all sensor subsets and all \(\lambda\ge0\). The maximum \(\lambda_{\mathrm c}\) is less than 1, so the unweighted conclusion follows.

**4. Minimality.** With two buildings, the analogous table is \(D_0=2p^2\), \(D_1=pq\), \(D_2=0\). The root-present leaf–leaf curvature is \(D_0-2D_1=2p(2p-1)<0\), the sole positive root–leaf lower bound is \((1-3p)/2\), and no other inequality obstructs submodularity. A single building has only two informationally equivalent sensors and no irreparable complementarity. Therefore three is the minimal building count for the identified coverage-weight-irreparable failure.

## Verification

The accompanying `verify.py` independently enumerates each source state, its exact Bernoulli probability, all possible sensor observations, and the optimal per-building binary decision, using rational arithmetic. It compares the result with the closed form for \(n=1,2,3,4,5\) at sampled rational prevalences; checks all set-function submodularity inequalities for the two- and three-source cases across several rational weights; tests sharp thresholds at and on either side of the predicted boundary; and certifies the exact \(p=1/10\) gap. Run using `python3 verify.py` (Python standard library only). These finite tests are reproducibility checks, **not** the proof for all real probabilities and coverage weights, which is in the preceding paragraphs.

## Relationship to prior work

Jakkala and Akella (2023), Sections IV.B–D, introduced a wastewater-flow Boolean OR network with independent Bernoulli building outbreaks, per-building Bayes classification thresholded at 50%, an expected correct-building score, a coverage indicator, and greedy placement. Their Section VI.B describes numerical behavior as supporting submodularity for *another experimentally used* objective with an F1 score and concentration threshold. The present result concerns only the analytically specified expected **accuracy plus unthresholded coverage** objective, not that experimental F1/concentration-dependent objective. Their paper does not present the derived three-source sharp submodularity phase diagram.

Bhattacharya et al. (2020), Appendix D, established by example that a general Gaussian multi-hypothesis transmitter-localization accuracy objective can fail submodularity, so non-submodularity of arbitrary classification objectives is **not** claimed as a new general fact. That counterexample neither implies an OR-gate wastewater classification threshold of \(1/5\) nor gives the sharp coverage-weight boundary or minimality. Submodularity of ordinary detection/coverage is standard; here its exact addition cannot repair low-prevalence posterior-label complementarity once the pooled sensor has already saturated coverage.

## Limitations

No general statement is made for unequal building prevalences, assay noise, transport delays, concentration-dependent detection, arbitrary directed trees, true F1 score, non-Bayesian predictions, or real wastewater data. It is **not** proved that a particular greedy sensor-selection run performs poorly: the result removes a generic submodularity *justification*, not a performance guarantee's factual outcome. The threshold depends on the specified risk and decision rule. Historical priority for this precise special-case classification is provisional; an older general discrete-testing theorem might subsume it. An author webpage describes an earlier 2022 version of the motivating topic without an independently verifiable day-level first-public date; the verified dated source used here is arXiv v1 from 2023-12-27.

## References

1. K. Jakkala and S. Akella, *Bayesian Sensor Placement for Multi-source Localization of Pathogens in Wastewater Networks*, arXiv:2312.16750v1, 2023-12-27, https://arxiv.org/abs/2312.16750 (Sections IV.B–E, VI.B–C).
2. A. Bhattacharya, C. Zhan, A. Maji, H. Gupta, S. R. Das, and P. M. Djurić, *Selection of Sensors for Efficient Transmitter Localization*, IEEE INFOCOM 2020 / extended manuscript, Appendix D, https://faculty.iiitd.ac.in/~arani/assets/pdf/infocom20a-long.pdf.
3. K. Jakkala, *Bayesian Sensor Placement for Multi-source Localization of Viruses in Wastewater Networks*, author publication page describing a 2022 predecessor, https://www.itskalvik.com/publication/wastewater/ (publication-day uncertainty).
