# A sharp one–two–three crest law for three equally spaced Nash runoff impulses

## Finding

Consider three equal, instantaneous rainfall-excess volumes separated by the same positive time gap \(d\), routed through a linear cascade of exactly three identical reservoirs with reservoir time constant \(k>0\). Write \(\delta=d/k\) and normalize time to \(t/k\). Apart from an irrelevant positive discharge multiplier, the downstream hydrograph is
\[
H_\delta(t)=g(t)+g(t-\delta)+g(t-2\delta),\qquad
g(u)=\begin{cases}u^2e^{-u},&u\ge0,\\0,&u<0.\end{cases}
\]
There is a unique \(\delta_0\in(3/2,8/5)\) satisfying
\[
2-\delta_0+4(1-\delta_0)e^{-\delta_0}=0,
\quad\delta_0=1.537805488887\ldots.
\]
**Theorem.** For every \(\delta>0\), the number of *strict local maxima* of \(H_\delta\) on \((0,\infty)\) is exactly
\[
\begin{cases}
1,&0<\delta\le\delta_0,\\
2,&\delta_0<\delta\le2,\\
3,&\delta>2.
\end{cases}
\]
At \(\delta=\delta_0\) a stationary shoulder at the third arrival is not a strict local maximum. At \(\delta=2\) the first arrival-related stationary shoulder similarly does not add a third maximum. In particular, three equal rainfall impulses can give **two distinct discharge crests even with gaps shorter than the individual three-reservoir impulse's modal lag**, \(2k\); two such equal impulses cannot create two strict crests below that lag.

## Assumptions and scope

Each reservoir is linear, initially empty, and identical; discharge is the linear convolution of rainfall excess with the three-reservoir Nash kernel \(u^2e^{-u}/2\) in dimensionless time. Inputs are three positive equal point impulses at \(0,d,2d\), with no infiltration or other nonlinear production model. The common impulse volume and normalization by \(k\) do not affect the number of maxima. The theorem concerns exact deterministic discharge curves and strict, positive-time local maxima, not statistically detectable peaks under noise. At impulse arrival boundaries the total hydrograph is continuously differentiable, though its second derivative may be discontinuous.

## Proof

Set \(h(x)=x^2e^{-x}\) for \(x\ge0\), zero before zero. Then \(h'(x)=x(2-x)e^{-x}\) for \(x\ge0\). On the intervals containing respectively one, two, or three active impulses,
\[
H_\delta'(t)=e^{-t}P_j(t),\qquad
P_j(t)=\sum_{i=0}^{j-1}e^{i\delta}(t-i\delta)(2-t+i\delta),\quad j=1,2,3.
\]
Every \(P_j\) is a strictly concave quadratic, since \(P_j''=-2\sum_{i=0}^{j-1}e^{i\delta}<0\). A quadratic's sign changes are consequently determined by a few exact boundary evaluations.

At the third impulse's arrival, using \(h'(0)=0\),
\[
H_\delta'(2\delta)=\delta e^{-\delta}F(\delta),\quad
F(\delta)=2-\delta+4(1-\delta)e^{-\delta}.
\]
On \((0,2]\), \(F'(\delta)=-1+4(\delta-2)e^{-\delta}<0\). In addition, \(F(1)>0\), \(F(2)<0\), and \(F(\delta)<0\) whenever \(\delta\ge2\). Therefore \(F\) has precisely one positive zero \(\delta_0\) in \((1,2)\). Direct endpoint substitutions put the zero strictly between \(3/2\) and \(8/5\).

For sign witnesses after a new impulse, note that the maximum magnitude of the *negative* portion of \(h'\) is
\[
M=\sup_{x\ge2}\{-h'(x)\}=2(1+\sqrt2)e^{-2-\sqrt2}.
\]
This follows by differentiating \(x(x-2)e^{-x}\), whose unique maximum over \([2,\infty)\) is at \(x=2+\sqrt2\). Furthermore \(2M<e^{-1}\). Indeed the last inequality is equivalent to \(e^{1+\sqrt2}>4(1+\sqrt2)\); the fourth-order Taylor lower bound for the exponential yields the positive difference \(11/8-2\sqrt2/3\). Consequently, for every \(\delta>1\),
\[
H_\delta'(2\delta+1)=h'(2\delta+1)+h'(\delta+1)+h'(1)
\ge e^{-1}-2M>0.
\]
Similarly, the two-active-impulse derivative satisfies \(h'(\delta+1)+h'(1)>0\) whenever \(\delta>1\).

**Case \(0<\delta\le\delta_0\).** Since \(\delta_0<2\), \(h'>0\) on \((0,\delta)\). The concave quadratic \(P_2\) is positive at \(t=\delta\) and nonnegative at \(t=2\delta\); hence it is strictly positive throughout \((\delta,2\delta)\). On \((2\delta,\infty)\), \(P_3\) starts nonnegative and tends to negative infinity, so it has exactly one positive-to-negative crossing. At the equality endpoint \(P_3(2\delta)=0\), its value is positive at \(2\delta+1\); strict concavity makes it positive immediately to the right as well. Thus there is precisely one strict local maximum and no extra maximum at the third arrival.

**Case \(\delta_0<\delta<2\).** The derivative is positive before the second impulse; on \((\delta,2\delta)\), \(P_2\) starts positive and finishes negative, so it has exactly one positive-to-negative crossing. On \((2\delta,\infty)\), \(P_3\) starts negative, is positive at \(2\delta+1\), and tends to negative infinity. Strict concavity implies exactly two roots, with derivative signs negative–positive–negative. This supplies exactly two strict maxima. At \(\delta=2\), \(P_2(2)=0\) but it is positive immediately after the second impulse (it is positive at \(3\)); it crosses once before \(4\). The third-impulse argument is unchanged, yielding exactly two strict maxima; the stationary point at \(2\) is not a maximum.

**Case \(\delta>2\).** The isolated first impulse attains its strict maximum at \(t=2<\delta\). The two-impulse polynomial \(P_2\) is negative at \(t=\delta\), positive at \(t=\delta+1<2\delta\), and negative at \(t=2\delta\); strict concavity gives a trough and then a second strict maximum in \((\delta,2\delta)\). Finally, \(P_3\) is negative at \(2\delta\), positive at \(2\delta+1\), and ultimately negative, giving a trough and a third maximum. No other maxima are possible because each active-impulse interval is governed by one quadratic. This completes the proof.

For comparison, with just two equal impulses and \(0<\delta\le2\), \(h'\) is positive on \(0<t<\delta\). The strictly concave quadratic \(P_2\) is nonnegative at \(t=\delta\) and tends to negative infinity, so it has exactly one positive-to-negative root after \(\delta\). When \(\delta=2\), it is strictly positive just to the right of \(2\) (as shown by the positive witness at \(\delta+1\)); hence the stationary point at arrival does not introduce an additional extremum. Thus exactly one maximum occurs for two equal impulses in this range, establishing the stated collective-resolution contrast.

## Verification

The self-contained standard-library file `CHECKER.py` enumerates stationary candidates using the quadratic formulas separately on the three impulse-activity intervals. It verifies the exact polynomial coefficient expansion by rational arithmetic, checks the inequality used to bound negative impulse slopes, and compares predicted and computed strict peak counts on 708 distinct dimensionless gaps including both sides of the first transition. Run `python CHECKER.py`. The checker reports 2,297 passed diagnostic assertions and \(\delta_0\approx1.537805488887\). As examples, the crest counts are one at \(\delta=1\), two at \(\delta=1.8\), and three at \(\delta=2.2\). The finite checker is supplementary; the proof above covers every real \(\delta>0\).

## Relationship to prior work

Nash (1957) derived the serial-linear-reservoir impulse-response model. Singh (2004) developed computational applications of gamma/Nash hydrographs for complicated storms. Boufadel (1998) discussed parameter estimation and finite-duration unit hydrographs. Muneepeerakul et al. (2010) used overlapping gamma-shaped streamflow pulses, whereas Gnecco, Palla and La Barbera (2018) analyzed peak discharge for a *single rectangular hyetograph* in a gamma-kernel framework. These model foundations and general superposition are not new.

Earlier published mathematical notes establish exact **two-pulse** crest thresholds for three and four serial reservoirs; the stronger relevant three-reservoir note shows two impulses cannot produce two crests below the isolated mode at two time constants. That result does not establish the present three-impulse, three-phase classification or the earlier sharp emergence of two crests at \(\delta_0<2\). Classical results on mixtures of two gamma densities (Ahmed, Goria and Hussein, 2008; Došlá, 2009) concern two components with different gamma parameters but common starting support and do not by themselves imply the exact three-**translated**-component crest count. General sign-variation results can bound oscillations without yielding the explicit transition \(\delta_0\). The complete triple-impulse classification should be assessed against historical work on modal geometry of positive shifted kernels; historical priority is not independently certified.

## Limitations

The exact values rely on equal instantaneous effective-rainfall volumes, equally spaced arrivals, a three-reservoir kernel, and linear time-invariant routing. For real storms of positive duration, nonlinear abstraction, unknown reservoir shape or observational smoothing, the transition values change and very small mathematical shoulders may not be empirically resolved. This result says nothing about global flood-peak magnitudes or field-calibrated flood risk. The online full texts of certain closest older hydrologic studies and the earlier relevant mathematical notes were not all accessible; originality remains a best-evidence assessment, not proof of global novelty.

## References

- Nash, J. E. (1957). *The Form of the Instantaneous Unit Hydrograph*. International Association of Scientific Hydrology, 3, 114–121. https://ponce.sdsu.edu/FIUH_Nash_1957.pdf
- Boufadel, M. C. (1998). *Unit Hydrographs Derived from the Nash Model*. Journal of the American Water Resources Association 34(1), 167–177. https://doi.org/10.1111/j.1752-1688.1998.tb05969.x
- Singh, S. K. (2004; first online 15 April). *Simplified Use of Gamma-Distribution/Nash Model for Runoff Modeling*. Journal of Hydrologic Engineering 9(3), 240–243. https://doi.org/10.1061/(ASCE)1084-0699(2004)9:3(240)
- Ahmed, S. E., Goria, M. N., and Hussein, A. (2008). *Gamma Mixture: Bimodality, Inflexions and L-Moments*. Communications in Statistics—Theory and Methods 37, 1147–1161. https://doi.org/10.1080/03610920701713286
- Došlá, Š. (2009). *Conditions for bimodality and multimodality of a mixture of two unimodal densities*. Kybernetika 45(2), 279–292. https://dml.cz/dmlcz/140075
- Muneepeerakul, R., Azaele, S., Botter, G., Rinaldo, A., and Rodriguez-Iturbe, I. (2010). *Daily streamflow analysis based on a two-scaled gamma pulse model*. Water Resources Research 46. https://doi.org/10.1029/2010WR009286
- Gnecco, I., Palla, A., and La Barbera, P. (2018). *A dimensionless approach for the runoff peak assessment: effects of the rainfall event structure*. Hydrology and Earth System Sciences 22, 943–956. https://doi.org/10.5194/hess-22-943-2018
