# Two-stock rigidity and a sharp three-stock onset of repeated aggregate catch-rate reversals

## Finding

For independent harvested Schaefer fish stocks under constant fishing effort, let total biomass and aggregate catch per unit effort (CPUE) each be divided by their own value at the beginning of observation. With **two** surviving stocks, these normalized indicators either agree at every time or intersect at most once at a strictly positive time, and any such intersection changes their ordering. This holds for arbitrary strictly positive initial stock sizes, including states away from either the unharvested or harvested equilibria.

The two-stock restriction is sharp in number of species: **three** strictly surviving stocks can exhibit *exactly two* changes in the ordering between normalized aggregate CPUE and normalized total biomass during one constant-effort episode. An exact integer-parameter witness and a complete real-root count are given below. No upper bound is claimed for arbitrary larger assemblages.

## Assumptions and scope

Fix an integer \(m\ge 2\), effort \(E>0\), and strictly positive \(r_i,q_i,K_i,B_i\), for \(i=1,\ldots,m\). Assume \(r_i>q_iE\). Abundances satisfy the independent Schaefer equations

\[
\frac{dN_i}{dt}=\left[r_i\left(1-\frac{N_i}{K_i}\right)-q_iE\right]N_i,
\qquad N_i(0)=B_i.
\]

The aggregate indicators are \(B(t)=\sum_iN_i(t)\) and \(Q(t)=\sum_iq_iN_i(t)\), with \(Q(t)\) equal to the total catch divided by effort. Compare their normalized values using

\[
D(t)=\frac{Q(t)}{Q(0)}-\frac{B(t)}{B(0)},\qquad t\ge0.
\]

The result concerns *time intersections of the normalized indicator levels*. It does not claim a statement about derivatives, elasticity of a regression slope, the sign of a stock-assessment error at any one time, or stochastic catch data. Every stock is independently logistic with strictly positive post-harvest growth; there is no recruitment interaction, immigration, effort adaptation, or measurement noise.

## Proof

**Two-stock bound.** Put \(a_i=r_i-q_iE>0\), \(L_i=K_ia_i/r_i>0\), \(c_i=L_i/B_i-1>-1\), and \(F_i(t)=N_i(t)/B_i\). Logistic solution gives

\[
F_i(t)=\frac{1+c_i}{1+c_i e^{-a_it}}.
\]

For two stocks, direct cancellation of the common weighted means yields

\[
D(t)=\frac{(q_1-q_2)B_1B_2}{(q_1B_1+q_2B_2)(B_1+B_2)}[F_1(t)-F_2(t)].
\]

If \(q_1=q_2\), the normalized indicators agree identically. Otherwise, their intersections are those of \(F_1\) and \(F_2\). All denominators are positive, so their difference has the same sign as

\[
H(t)=c_1-c_2+(1+c_1)c_2e^{-a_2t}-(1+c_2)c_1e^{-a_1t}.
\]

Here \(H(0)=0\). Its derivative is a linear combination of at most two exponentials with positive decay rates. Unless identically zero, it has at most one zero on \((0,\infty)\): dividing by one exponential leaves an affine function of the strictly monotone exponential \(e^{-(a_1-a_2)t}\); if the rates coincide, it is a single exponential. By Rolle's theorem, \(H\) therefore has at most one strictly positive zero. A strictly positive zero must be simple: if it were multiple, Rolle's theorem between zero and that zero would produce a second, distinct zero of \(H'\), in addition to its zero at the multiple root. If \(H'\equiv0\), then \(H\equiv0\), since \(H(0)=0\). Thus every isolated strictly positive indicator intersection changes sign, as claimed.

**Three-stock exact witness.** Choose \(E=1\) and

\[
(q_1,q_2,q_3)=(3,2,1),\quad
(r_1,r_2,r_3)=(20,3,4),\quad
(K_1,K_2,K_3)=(B_1,B_2,B_3)=(3,4,6).
\]

The net positive growth rates are \((17,1,3)\). Let \(z=e^{-t}\), which bijectively maps \(t\in(0,\infty)\) onto \(z\in(0,1)\). The normalized individual abundances are

\[
F_1=\frac{17}{20-3z^{17}},\qquad
F_2=\frac{1}{3-2z},\qquad
F_3=\frac{3}{4-z^3}.
\]

Here \(B(0)=13\), \(Q(0)=23\). Direct expansion gives

\[
299D=48F_1+12F_2-60F_3
=\frac{P(z)}{(20-3z^{17})(3-2z)(4-z^3)},
\]

where the denominator is strictly positive for \(0<z<1\) and

\[
P(z)=36z^{20}-1080z^{18}+1476z^{17}+1632z^4-2688z^3+672z-48.
\]

Exactly \(P(1)=0\). Factor \(P(z)=12(z-1)R(z)\), where \(R\) has degree 19. Map \(0<z<1\) to \(y=z/(1-z)>0\), and set \(S(y)=(1+y)^{19}R(y/(1+y))\). Its integer coefficients in *descending* degree order are

```text
459, 5049, 26333, 87924, 202912, 318784, 288864,
-33592, -611728, -1166880, -1382576, -1179256,
-752352, -360128, -126752, -31212, -4792, -304,
24, 4
```

The sign sequence has **exactly two** variations. Descartes' rule of signs bounds the number of positive roots of \(S\), including multiplicity, by two; therefore \(P\) has at most two zeros in \((0,1)\). Conversely, exact rational substitution gives

\[
P(9/10)<0,\qquad P(1/3)>0,\qquad P(1/100)<0.
\]

The intermediate value theorem forces a zero in each of the disjoint intervals \((1/3,9/10)\) and \((1/100,1/3)\). Thus there are **exactly two** distinct positive-time intersections and both reverse the ordering. For orientation only, the crossing times are approximately \(0.54010285\) and \(2.61852563\) in the time units of the model.

## Verification

The accompanying stand-alone `checker.py` uses only the Python standard library and exact rational integer arithmetic. Run `python3 checker.py`. It verifies the exact polynomial identity after clearing positive denominators, the polynomial factorization, all 20 transformed coefficients, the two sign variations, the three strict sign evaluations, and rational-point checks of the original Schaefer differential equations. The checker reports 40 exact assertions. The infinite-time and all-parameter statements rely on the proof above, **not** on numeric sampling or finite assertions.

## Relationship to prior work

Kleiber and Maunder (2008) specifically established aggregate-CPUE bias and its early and equilibrium behavior in multispecies fisheries. Their Fig. 2 displays two-stock examples including a single intersection, while their Section 5 reports 5,000 two-stock Schaefer simulations and their appendices analyze initial rates and eventual equilibria. Those results are background, not claimed here. Neither that source's full examined text nor its displayed formulas establish the *global at-most-one positive-time intersection for all two-stock initial states* or the *three-stock exact two-intersection witness*. A picture containing one intersection alone does not imply a maximum of one.

Jensen (1991) treats two independently productive Schaefer species with fishery applications and is a close model-level antecedent. Its available abstract concerns sustainable-yield and equilibrium questions; its full text was not available for a complete comparison. Ellis and Wang (2006) address the relationship between spatial density and fishing effort, not the independent-stock, fixed-effort temporal indicator crossing count. Nesslage and Wilberg (2012) examine aggregated multispecies surplus-production assessment with time-varying parameters, but their accessible abstract does not resolve the exact transient crossing count; this is a residual priority risk. The historical literature may contain equivalent exponential-sum crossing results under different terminology.

## Limitations

The three-stock witness is a mathematical construction, not a fit to observed fisheries. Large catchability and productivity contrasts were selected to expose the phenomenon; practical frequency or empirical plausibility are not estimated. The result fails to address time-varying catchability or effort, correlated stocks, predator–prey coupling, extinction at negative net growth, or measurement error. It does not establish that every three-stock fishery has two reversals, nor a maximum count for arbitrary numbers of stocks. Earlier mathematical or fishery work may prove an equivalent statement; independent literature-priority assessment has not been performed.

## References

- Jensen, A. L. (1991), *Multiple species fisheries with no ecological interaction: two-species Schaefer model applied to lake trout and lake whitefish*. ICES Journal of Marine Science 48(2), 167–171. https://doi.org/10.1093/icesjms/48.2.167
- Ellis, N., and Wang, Y.-G. (2006), *Effects of fish density distribution and effort distribution on catchability*. ICES Journal of Marine Science 64(1), 178–191. https://doi.org/10.1093/icesjms/fsl015
- Kleiber, P., and Maunder, M. N. (2008), *Inherent bias in using aggregate CPUE to characterize abundance of fish species assemblages*. Fisheries Research 93, 140–145. https://doi.org/10.1016/j.fishres.2008.03.013
- Nesslage, G. M., and Wilberg, M. J. (2012), *Performance of Surplus Production Models with Time-Varying Parameters for Assessing Multispecies Assemblages*. North American Journal of Fisheries Management. https://doi.org/10.1080/02755947.2012.720646
