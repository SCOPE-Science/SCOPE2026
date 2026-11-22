# A universal one-crossing law for occupancy under accelerated habitat turnover

## Finding

Consider a single habitat location initially unsuitable. Two landscapes have the same stationary fraction of suitable time and the same colonization and population-extinction rates, but different turnover speeds. Under the continuous-time three-state model defined below, the probability of being occupied in the faster landscape is **strictly higher for every sufficiently early positive time and strictly lower for every sufficiently late time, with exactly one crossing at a positive time**. The result holds for every pair of distinct positive turnover speeds, without a parameter-ratio restriction.

More precisely, write \(P_s(t)\) for occupancy under turnover speed \(s\). For every \(0<s_1<s_2\) there exists a unique \(T_*(s_1,s_2)>0\) such that
\[
P_{s_2}(t)-P_{s_1}(t)
\begin{cases}>0,&0<t<T_*,\\=0,&t=T_*,\\<0,&t>T_*.
\end{cases}
\]
There is also a common zero at the initial instant \(t=0\), excluded from the uniqueness assertion.

## Assumptions and scope

A patch has states \(U\) (unsuitable), \(E\) (suitable and empty), and \(O\) (suitable and occupied). Fix \(0<p<1\), \(c>0\), and \(e\ge0\). Its continuous-time Markov transitions are
\[
U\xrightarrow{ps} E,\qquad E\xrightarrow{(1-p)s}U,\qquad O\xrightarrow{(1-p)s}U,
\qquad E\xrightarrow c O,\qquad O\xrightarrow e E.
\]
All parameters are time-homogeneous and \(s>0\); initially \(\Pr(U)=1\). The parameter \(p\) is the stationary suitability probability for the two-state environmental process, and changing \(s\) keeps that fraction fixed while accelerating both habitat creation and destruction. Colonization \(c\) is supplied externally and is independent of other patches. Occupancy means \(\Pr(O)\) at a specified deadline, not regional metapopulation survival.

Let \(q=1-p\), \(\lambda_s=c+e+qs\). When \(\lambda_s\ne s\), the exact solution is
\[
P_s(t)=cp\left[\frac{1-e^{-\lambda_st}}{\lambda_s}
-\frac{e^{-st}-e^{-\lambda_st}}{\lambda_s-s}\right].
\]
For \(\lambda_s=s\), the second quotient is interpreted as its continuous limit \(t e^{-st}\). The late-time occupancy is \(cp/\lambda_s\), strictly decreasing in \(s\).

## Proof

**Step 1 (suitability forcing).** Put \(H_s(t)=\Pr(E)+\Pr(O)\). Since either suitable state becomes unsuitable at rate \(qs\),
\[
H_s'=ps(1-H_s)-qsH_s=s(p-H_s),\qquad H_s(0)=0.
\]
Consequently \(H_s(t)=p(1-e^{-st})\). The occupied probability obeys the scalar forced equation
\[
P_s'=cH_s-\lambda_sP_s,\qquad P_s(0)=0,
\]
which yields the displayed formula by convolution. For every positive time \(H_s,P_s>0\).

**Step 2 (a one-change forcing).** Fix \(s_2>s_1>0\), set \(\delta=s_2-s_1>0\), \(A(t)=e^{-s_1t}-e^{-s_2t}>0\), and \(\Delta(t)=P_{s_2}(t)-P_{s_1}(t)\). Subtracting the two scalar equations gives
\[
\Delta'+\lambda_{s_2}\Delta=R(t),\qquad
R(t)=cpA(t)-q\delta P_{s_1}(t).
\]
We show that \(R\) changes sign exactly once, from positive to negative. First, \(A(t)/H_{s_1}(t)\) strictly decreases. Indeed put \(y=e^{-s_1t}\in(0,1)\) and \(r=s_2/s_1>1\). Then
\[
\frac{A(t)}{H_{s_1}(t)}=\frac{y-y^r}{p(1-y)},
\]
whose derivative with respect to \(y\) has the sign of
\[
1-r y^{r-1}+(r-1)y^r>0 \quad (0<y<1).
\]
The final inequality follows because this expression decreases to zero as \(y\uparrow1\): its derivative is \(-r(r-1)y^{r-2}(1-y)<0\). As \(y\) decreases with time, the ratio decreases strictly.

Second, \(P_{s_1}(t)/H_{s_1}(t)\) strictly increases for \(t>0\). The convolution formula can be written
\[
\frac{P_{s_1}(t)}{H_{s_1}(t)}
=c\int_0^t e^{-\lambda_{s_1}v}
\frac{H_{s_1}(t-v)}{H_{s_1}(t)}\,dv.
\]
For each fixed \(0<v<t\), the ratio in the integrand strictly increases with \(t\), since \((\log H_{s_1})'(u)=s_1/(e^{s_1u}-1)\) strictly decreases in \(u>0\). The integration domain also expands with \(t\), and the integrand is nonnegative. Thus the displayed ratio increases strictly.

Therefore \(A(t)/P_{s_1}(t)\), the quotient of a strictly decreasing positive ratio and a strictly increasing positive ratio, decreases strictly. It diverges as \(t\downarrow0\), because \(A(t)\sim\delta t\) while \(P_{s_1}(t)\sim cps_1t^2/2\), and it tends to zero as \(t\to\infty\). Hence
\[
\frac{R(t)}{P_{s_1}(t)}=cp\frac{A(t)}{P_{s_1}(t)}-q\delta
\]
strictly decreases from positive infinity to \(-q\delta<0\) and has exactly one zero \(T_R>0\), with signs positive before and negative after.

**Step 3 (exactly one occupancy crossover).** Define \(Z(t)=e^{\lambda_{s_2}t}\Delta(t)\). Then \(Z(0)=0\) and \(Z'(t)=e^{\lambda_{s_2}t}R(t)\). Hence \(Z\) strictly increases until \(T_R\) and strictly decreases thereafter; in particular \(Z(T_R)>0\). But
\[
\lim_{t\to\infty}\Delta(t)
=cp\left(\frac1{\lambda_{s_2}}-\frac1{\lambda_{s_1}}\right)<0,
\]
so \(Z(t)\to-\infty\). It follows by continuity and strict decrease after \(T_R\) that \(Z\), and thus \(\Delta\), has exactly one positive zero \(T_*>T_R\), with the claimed signs. This establishes the result for all quantified parameters, including resonant and extinction-free cases. \(\square\)

## Verification

The accompanying standalone \(\texttt{patch_turnover_verify.py}\) evaluates the analytic convolution and an independently constructed three-state matrix exponential. It checks 400 fixed-seed parameter draws (8,800 checks) and 12 additional resonant-case checks, reporting \(8,812\) passing diagnostics. These finite tests are not a proof of universal uniqueness; the proof is the monotone-forcing argument above. For \(p=0.4\), \(c=1.8\), \(e=0.2\), \(s_1=0.5\), \(s_2=4\), the computed unique crossover is \(T_*\approx1.950825084705\), with faster-minus-slower occupancy positive at half that time and negative at twice it. Reproduce with \(\texttt{python patch_turnover_verify.py}\), using NumPy and SciPy.

## Relationship to prior work

Matlack and Monde (2004) analyzed patch creation and destruction at fixed habitat proportion using a spatially explicit lattice model. That study documents long-run occupancy disadvantages from turnover and transient ecological opportunity, but its published model and results do not supply the present all-parameter, single-patch, all-deadline one-crossing classification. DeWoody, Feng, and Swihart (2005) use three landscape states (uninhabitable, habitable, occupied), making their work especially relevant; the accessible abstract and the inspected first manuscript page emphasize spatial persistence thresholds rather than the present two-speed transient probability comparison. Wilcox, Cairns, and Possingham (2006) and Reigada et al. (2015) further motivate environmental disturbance and recovery. The distinction from the cited studies concerns the exact comparison across all positive deadlines, not merely the existence of a transient benefit or an equilibrium decrease.

## Limitations

External, constant colonization ignores spatial dependence, dispersal feedback, correlated patches, density dependence, and time-varying climate. The theorem is only for a patch initially unsuitable; other initial mixtures can lead to different time profiles. Real habitat data cannot be inferred from this idealized rate model without calibration. The literature comparison does not establish exhaustive historical priority: the complete 2005 spatially realistic manuscript and some additional relevant works were not fully accessible for statement-by-statement inspection. A self-contained derivation and supporting numerical checks do not constitute independent verification.

## References

- Matlack, G. R., and Monde, J. (2004). *Consequences of low mobility in spatially and temporally heterogeneous ecosystems*. Journal of Ecology 92, 1025–1035. First published 2004-09-16. https://doi.org/10.1111/j.0022-0477.2004.00908.x
- DeWoody, Y. D., Feng, Z., and Swihart, R. K. (2005). *Merging Spatial and Temporal Structure within a Metapopulation Model*. The American Naturalist 166, 42–55. Online 2005-05-11. https://doi.org/10.1086/430639
- Wilcox, C., Cairns, B. J., and Possingham, H. P. (2006). *The role of habitat disturbance and recovery in metapopulation persistence*. Ecology. https://doi.org/10.1890/05-0587
- Reigada, C., Schreiber, S. J., Altermatt, F., and Holyoak, M. (2015). *Metapopulation Dynamics on Ephemeral Patches*. The American Naturalist. Online 2015-01-08. https://doi.org/10.1086/679502
