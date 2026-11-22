# A sharp two-pool failure threshold for the environmental RNA:DNA freshness clock

## Finding

Consider the ratio of environmental RNA to DNA after a single, simultaneous release into two noninterconverting molecular pools. Each pool loses its RNA faster than its own DNA. Nonetheless, the aggregate RNA:DNA ratio need not decrease with elapsed time: it can decrease, increase, and decrease, making exactly three different ages consistent with the same observed ratio.

For positive parameters \(A,\kappa,b,q,\Delta,\varepsilon\), set
\[
D(t)=A e^{-bt}+Aq e^{-(b+\Delta)t},\qquad
R(t)=\kappa A e^{-(b+\varepsilon)t}+\kappa Aq e^{-(b+2\Delta+\varepsilon)t},\qquad t\geq0.
\]
Both pools have an initial RNA:DNA ratio \(\kappa\). In the slow and fast pools, respectively, RNA exceeds the matched DNA decay constant by \(\varepsilon>0\) and \(\Delta+\varepsilon>0\). Thus every isolated pool's RNA:DNA ratio is strictly decreasing.

Let \(q>0\) be fixed. Define \(x_*(q)\) as the unique root in \((0,1)\) of
\[
P_q(x)=q^2x^4-4q^2x^3-6qx^2-4x+1=0,
\]
and define the positive threshold
\[
s_*(q)=\frac{qx_*(1-2x_*-qx_*^2)}{(1+qx_*)(1+qx_*^2)}.
\]
Then the following is a necessary-and-sufficient classification, with \(s=\varepsilon/\Delta>0\):

1. If \(s\geq s_*(q)\), the aggregate ratio \(Q(t)=R(t)/D(t)\) is strictly decreasing for all \(t\geq0\). Equality leaves one horizontal tangent but no reversal.
2. If \(0<s<s_*(q)\), \(Q\) has precisely two critical times \(0<t_{\min}<t_{\max}<\infty\): a strict local minimum followed by a strict local maximum. Every ratio between those two positive extrema is achieved at **exactly three distinct nonnegative ages**.

Two pools are minimal for this phenomenon: a one-pool first-order model with strictly faster RNA degradation has a strictly decreasing ratio. The classification is sharp within the stated two-pool model, not a claim about arbitrary decay laws or about all environmental samples.

## Assumptions and scope

All parameters \(A,\kappa,b,q,\Delta,\varepsilon\) are strictly positive and constant. Both molecular pools start simultaneously at time zero; neither receives new molecular input; losses are first order and pools do not exchange material. Signal quantities are exact, positive concentration expectations; there is no analytical noise, limit of detection, molecular production, or transport. The two pools' DNA baseline rates are \(b\) and \(b+\Delta\), and their RNA rates are \(b+\varepsilon\) and \(b+2\Delta+\varepsilon\). Initial RNA amplitudes are proportional to initial DNA amplitudes with the same factor \(\kappa\) in both pools. These coupling restrictions matter: the theorem is not a full classification of arbitrary pairs of exponential mixtures.

The common decay constant \(b\) and concentration scale \(A\) cancel in \(Q\). Only the pool amplitude ratio \(q\), excess-rate ratio \(s=\varepsilon/\Delta\), time scale \(\Delta\), and overall marker scale \(\kappa\) determine the clock shape.

## Proof

Put \(x=e^{-\Delta t}\), so \(x\) decreases from \(1\) toward \(0\). Direct cancellation yields
\[
Q(t)=\kappa e^{-\varepsilon t}\frac{1+qx^2}{1+qx},\qquad
\frac{d}{dt}\log Q(t)=\Delta\bigl(F_q(x)-s\bigr),
\]
where
\[
F_q(x)=\frac{qx}{1+qx}-\frac{2qx^2}{1+qx^2}
=\frac{qx(1-2x-qx^2)}{(1+qx)(1+qx^2)}.
\]
Define \(c_q=(1+\sqrt{1+q})^{-1}\). The numerator of \(F_q\) shows that \(F_q(x)>0\) exactly for \(0<x<c_q\), and \(F_q(x)<0\) for \(c_q<x\leq1\). In particular, the ratio initially decreases and eventually decreases (since \(F_q(0)=0<s\)).

Differentiate and clear positive denominators:
\[
F_q'(x)=\frac{qP_q(x)}{(1+qx)^2(1+qx^2)^2},\qquad
P_q'(x)=4q^2x^3-12q^2x^2-12qx-4<0 \quad(0<x<1).
\]
The final strict inequality holds because \(4q^2x^3-12q^2x^2=4q^2x^2(x-3)<0\). Also \(P_q(0)=1>0\) and \(P_q(1)=-3(q+1)^2<0\). There is exactly one root \(x_*(q)\in(0,1)\), giving the unique global maximum of \(F_q\) on \([0,1]\). Since \(F_q(c_q)=0\) and \(F_q\) is positive just below \(c_q\), this maximum is positive and lies at \(x_*\in(0,c_q)\). Hence \(s_*(q)=F_q(x_*)>0\).

For \(s>s_*\), the logarithmic derivative is strictly negative. For \(s=s_*\), it vanishes only at \(x=x_*\) and is otherwise negative; integration over every nonempty time interval still gives a strictly falling \(Q\). When \(0<s<s_*\), the equation \(F_q(x)=s\) has exactly two solutions \(x_-\in(0,x_*)\) and \(x_+\in(x_*,c_q)\). As time moves forward, \(x\) traverses the larger root first, then the smaller root; the logarithmic derivative is respectively negative, positive, negative. Thus the first turning point is a strict minimum and the second a strict maximum.

Finally, \(Q(0)=\kappa\), while for every \(t>0\), \(e^{-\varepsilon t}<1\) and \((1+qx^2)/(1+qx)<1\), whence \(0<Q(t)<\kappa\). Also \(\lim_{t\to\infty}Q(t)=0\). The first branch drops from \(\kappa\) to the minimum, the second rises to the maximum, and the last drops to zero, each strictly. Every level strictly between the two extrema therefore has exactly three preimages. With just one pool, the ratio is \(\kappa e^{-\delta t}\) for some \(\delta>0\), precluding any reversal. This completes the classification and minimality proof.

## Verification

A particularly transparent exact counterexample takes \(A=\kappa=b=q=\Delta=1\) and \(\varepsilon=1/20\), so
\[
Q(t)=e^{-t/20}\frac{1+e^{-2t}}{1+e^{-t}}.
\]
Here \(Q(0)=1>4/5\) and \(Q(t)\to0<4/5\). Moreover,
\[
Q(\log3)=\frac56\,3^{-1/20}<\frac45,
\qquad
Q(\log16)=\frac{257}{272}\,16^{-1/20}>\frac45.
\]
The two strict inequalities follow from the **integer-only** comparisons \(3\cdot24^{20}>25^{20}\) and \(16\cdot1088^{20}<1285^{20}\). Consequently \(Q(t)=4/5\) has at least three solutions, and the analytic theorem limits the number to exactly three. Numerically, the two-pool threshold at \(q=1\) is \(s_*(1)\approx0.0899798397855>1/20\). The example is a mathematical construction; its numbers are not empirical estimates.

Run `python3 CHECK.py` (standard Python library only). It verifies the two exact inequalities, rational identities for the logarithmic derivative and quartic, strict signs on deterministic parameter grids, numerical localization of the sole positive quartic root and the two critical ages of the example. These finite checks are supplemental; the global statements depend on the proof above, not on sampling a parameter grid.

## Relationship to prior work

Marshall, Vanderploeg and Chaganti (2021) measured declining eRNA:eDNA ratios following experimental shedding and specifically identified the prospect of molecular age inference, while warning that naturally mixed molecular material can complicate interpretation. Jo and coauthors (2022) likewise evaluated differential eRNA and eDNA persistence under water chemistry variation. Kagzi and coauthors (2023) studied environmental nucleic acid decay in a metabarcoding setting. These empirical results motivate the question but do not supply an exact classification for the above coeval two-pool model.

Mixture-induced reversals and nonmonotone survival summaries are a well-established general idea; the generic observation that aggregation can destroy a monotone comparison is **not** claimed as original. Bar-Lev and Letac (2010) develop mixture-hazard mathematics for natural exponential families, a distinct hazard objective. Classical exponential-polynomial zero bounds (a consequence of the Rolle induction for real exponentials) already bound the possible number of solutions of a four-term ratio level equation by three. That general fact alone neither supplies the sharp monotonicity threshold nor constructs triple-age solutions under strictly faster matched RNA decay. The narrow proposed contribution here is the rate-coupled necessary-and-sufficient threshold and the exact integer-certified triple-age example. A historical-priority comparison with the broad survival-paradox literature remains incomplete, particularly where only an abstract or metadata was accessible.

## Limitations

The rate structure is constrained; different amplitudes across molecular types, transport, replenishment, exchange, thresholding, chemical-state transitions, and measurement noise can alter the shape or identifiability. Exact three-age ambiguity does not establish practical three-way ambiguity at a finite instrument resolution. The formula is a warning about model-based age inference, not a claim that field data exhibit a rebound or that RNA is generally a worse indicator than DNA. The nonzero threshold can be arbitrarily small as parameters vary. No independent external validation has been performed.

## References

1. Marshall, N. T., Vanderploeg, H. A., and Chaganti, S. R. (2021). *Environmental (e)RNA advances the reliability of eDNA by predicting its age.* Scientific Reports 11, 2769. First publicly available 2021-02-02. https://doi.org/10.1038/s41598-021-82205-4 . Full text: https://repository.library.noaa.gov/view/noaa/58652/noaa_58652_DS1.pdf .
2. Jo, T., Tsuri, K., Hirohara, T., and Yamanaka, H. (2022). *Warm temperature and alkaline conditions accelerate environmental RNA degradation.* Environmental DNA 5, 836–848. First published 2022-07-15. https://doi.org/10.1002/edn3.334 .
3. Kagzi, K., et al. (2023). *Assessing the degradation of environmental DNA and RNA based on genomic origin in a metabarcoding context.* Environmental DNA 5, 1016–1031. First published 2023-06-06. https://doi.org/10.1002/edn3.437 .
4. Bar-Lev, S. K., and Letac, G. (2010). *Increasing hazard rate of mixtures for natural exponential families.* https://arxiv.org/abs/1004.4258 .
5. Scarsini, M., and Spizzichino, F. (1999). *Simpson-type paradoxes, dependence, and ageing.* Journal of Applied Probability. https://doi.org/10.1239/jap/1032374234 . Abstract examined; full-text priority comparison remains unresolved.
