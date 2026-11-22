# A three-shape response staircase for fixed-mean reactive transit times

## Finding

**Theorem (complete three-shape ordering).** Let \(a,b,\mu>0\), put \(r=1+a/b>1\) and \(t=b\mu>0\), and let \(T_k\) have the gamma distribution of shape \(k\) and rate \(k/\mu\), for \(k\in\{1,2,3\}\). For the parcel-scale response
\[
q(s)=(1-e^{-as})e^{-bs},\qquad s\geq0,
\]
set \(C_k=\mathbb E[q(T_k)]\). There exist exactly three **distinct, strictly ordered** positive crossover values
\[
0<t_{23}(r)<t_{13}(r)<t_{12}(r)<\infty
\]
with the following exhaustive strict orderings as \(t\) increases:
\[
\begin{array}{c|c}
\text{range}&\text{descending order}\\ \hline
(0,t_{23})&C_3>C_2>C_1\\
(t_{23},t_{13})&C_2>C_3>C_1\\
(t_{13},t_{12})&C_2>C_1>C_3\\
(t_{12},\infty)&C_1>C_2>C_3
\end{array}
\]
At each crossover exactly the indicated pair ties; the third value is strictly separated. Each pair of responses crosses **exactly once** on \(t>0\), and the pairwise crossings remain in this order for *every* \(r>1\). Thus, among these three equally mean-matched transit laws, the maximizing shape changes from \(3\) to \(2\) to \(1\) as mean transit time grows; shape \(3\) and shape \(1\) never exchange the maximizer directly.

The last crossover \(t_{12}\) is the unique positive root of
\[
r^2t^3-8rt-4(r+1)=0.
\]
It decreases strictly with \(r\), approaches \(1+\sqrt5\) as \(r\downarrow1\), and obeys \(t_{12}(r)\sim(4/r)^{1/3}\) as \(r\to\infty\). For the other crossings, the unique equations \(H_{ij}(rt)=H_{ij}(t)\), with rational functions \(H_{ij}\) defined below, provide exact implicit specifications without numerical root-isolation assumptions.

## Assumptions and scope

The same mean \(\mu\) is imposed on the three residence-time distributions; their variances are \(\mu^2/k\). The response \(q\) is a stylized combination of a first-order saturating activation of rate \(a\) and subsequent survival of rate \(b\). It is also proportional to the intermediate-species concentration for a two-step consecutive first-order kinetic model with rates \(a+b\) and \(b\). The result compares **only** the three discrete shapes \(k=1,2,3\), not arbitrary gamma shapes, nonlinear transport, or spatially resolved reactions. Positivity and all strict conclusions require \(a,b,\mu>0\); \(a=0\) produces identically zero responses and is excluded.

The gamma Laplace transform gives the explicit normalization
\[
C_k(t,r)=\left(1+\frac{t}{k}\right)^{-k}-\left(1+\frac{rt}{k}\right)^{-k}.
\]
The field interpretation is a mean-matched comparison of hypothetical transit-time shapes, not a claim that catchment mixing can be independently controlled through the integer shape parameter.

## Proof

**Step 1: exact rational response differences.** Set \(f_k(z)=(1+z/k)^{-k}\) and \(H_{ij}(z)=f_i(z)-f_j(z)\) for \(1\leq i<j\leq3\). Direct rational reduction yields
\[
\begin{aligned}
H_{12}(z)&=\frac{z^2}{(z+1)(z+2)^2},\\
H_{23}(z)&=\frac{z^2(4z+9)}{(z+2)^2(z+3)^3},\\
H_{13}(z)&=\frac{z^2(z+9)}{(z+1)(z+3)^3}.
\end{aligned}
\]
They are positive for every \(z>0\). Moreover,
\[
C_j-C_i=H_{ij}(rt)-H_{ij}(t).
\]
This reduces each crossover to comparing the same positive rational function at two scaled arguments.

**Step 2: exactly one crossing for each pair.** Define the logarithmic elasticity \(D_{ij}(z)=zH'_{ij}(z)/H_{ij}(z)\). Differentiation and simplification give
\[
\begin{aligned}
zD'_{12}(z)&=-\frac{z[(z+2)^2+4(z+1)^2]}{(z+1)^2(z+2)^2},\\
zD'_{23}(z)&=-\frac{z(172z^4+1536z^3+5193z^2+7884z+4536)}{(z+2)^2(z+3)^2(4z+9)^2},\\
zD'_{13}(z)&=-\frac{z(z^4+132z^3+1062z^2+2052z+1377)}{(z+1)^2(z+3)^2(z+9)^2}.
\end{aligned}
\]
Every numerator inside a negative sign is strictly positive at \(z>0\). Hence \(D_{ij}\) strictly decreases. For \(r>1\), the derivative with respect to \(\log t\) of \(\log[H_{ij}(rt)/H_{ij}(t)]\) is \(D_{ij}(rt)-D_{ij}(t)<0\). The ratio strictly decreases from \(r^2>1\) at \(t\downarrow0\) to \(r^{-i}<1\) as \(t\to\infty\) (because \(H_{ij}(z)\) has order \(z^{-i}\) at infinity). It therefore crosses one exactly once, from above. Consequently \(C_j>C_i\) before \(t_{ij}\) and \(C_j<C_i\) after \(t_{ij}\).

**Step 3: ordering of the crossover points.** For \((i,j)=(1,2)\), direct reduction gives
\[
C_2-C_1=-\frac{t^2(r-1)F(t,r)}{(t+1)(t+2)^2(rt+1)(rt+2)^2},\qquad F(t,r)=r^2t^3-8rt-4(r+1).
\]
Step 2 already guarantees one positive root; the formula identifies it as \(t_{12}\). Define
\[
R(z)=\frac{H_{23}(z)}{H_{12}(z)}=\frac{(z+1)(4z+9)}{(z+3)^3}.
\]
A polynomial identity, valid at all positive \(r,t\), is
\[
R(rt)-R(t)=-\frac{t(r-1)P(t,r)}{(t+3)^3(rt+3)^3},
\]
where
\[
\begin{split}
P={}&4r^2t^4+13r^2t^3+9r^2t^2+13rt^3+18rt^2\\
&-27rt+9t^2-27t-108.
\end{split}
\]
More importantly, the exact division identity
\[
\begin{aligned}
P={}&\frac{4rt+13r+13}{r}\,F(t,r)\\
&+\frac{(9r^3+50r^2+9r)t^2+(93r^2+93r)t+52r^2-4r+52}{r}
\end{aligned}
\]
has a strictly positive remainder for every \(r>1,t>0\). At \(t=t_{12}\), therefore, \(P>0\), so \(R(rt)<R(t)\). Since \(H_{12}(rt)=H_{12}(t)\) at this point, we obtain \(H_{23}(rt)<H_{23}(t)\); equivalently \(C_3<C_2=C_1\). By Step 2 this forces \(t_{23}<t_{12}\). At \(t_{23}\), \(C_3=C_2>C_1\); at \(t_{12}\), \(C_3<C_1=C_2\). Continuity and the unique \((1,3)\) crossing imply \(t_{23}<t_{13}<t_{12}\). The four stated permutations and isolated ties follow immediately.

**Step 4: variation of the last crossover.** At the unique positive root of \(F=0\), \(r^2t^3>8rt\), hence \(F_t=3r^2t^2-8r>0\). Replacing \(F/r\) by \(rt^3-8t-4(1+r^{-1})\), its partial derivative with respect to \(r\) is \(t^3+4/r^2>0\). Implicit differentiation gives \(t'_{12}(r)<0\). Taking \(r\downarrow1\) gives the unique positive root of \(t^3-8t-8\), namely \(1+\sqrt5\). Scaling \(t=r^{-1/3}y\) in \(F/r\) gives \(y^3-4+o(1)=0\), proving \(t_{12}\sim(4/r)^{1/3}\). This completes the proof.

## Verification

A standalone Python/SymPy checker named `checker.py` symbolically rederives the three rational differences, each of the three logarithmic-curvature identities, the cubic response difference, and both ordering identities. It additionally tests exact rational evaluations of the three responses and high-precision numerical brackets for six distinct rate ratios. Running `python checker.py` gives `PASS 438 deterministic assertions`. The proof of all-parameter existence, uniqueness and ordering is the analytical argument above, **not** numerical enumeration.

For \(r=2\), the three thresholds are approximately \(t_{23}=1.8623734889527381\), \(t_{13}=2.1319963351774577\), and \(t_{12}=2.3027756377319946\). At \(t=1\), responses are \(C_1=1/6\), \(C_2=7/36\), \(C_3=1647/8000\), whereas at \(t=4\) they satisfy \(C_1>C_2>C_3\). These are illustrative checks, not the proof of the global assertions.

## Relationship to prior work

Gamma and exponential transit-time laws are established catchment representations, not introduced here; see Hrachowitz et al. (2010). Reactive nitrate behavior under heterogeneous mixing and age-dependent reactions is studied by Green et al. (2010), van der Velde et al. (2010, 2012), and Frei et al. (2019). The response formula also has the classical *consecutive first-order reaction intermediate* interpretation, and the same gamma laws are the established equal-volume stirred-tank-in-series residence-time models. Standard reaction-kinetic and tank-cascade formulas thus cover **the constituent ingredients**. The specific result assessed here is the universal, strict, fully ordered three-shape crossover classification at fixed mean and for all positive kinetic ratios, with explicit one-crossing and nonadjacent-crossing exclusion proofs. No equivalent theorem was identified in the inspected relevant sources; priority beyond those sources is not established.

In particular, Mongelli (2018) optimizes the allocation of **three unequal stirred-tank volumes** for a given two-reaction system, not the global orderings of equal-mean, equal-stage one-, two-, and three-tank models over all positive residence times. Broader chemical-engineering comparison theorems remain an explicit residual originality risk.

## Limitations

This is a self-contained theorem for a stylized scalar, linear two-rate response and exactly three gamma shapes. It does not establish that real nitrate concentrations, hyporheic transformations, age-dependent reaction parameters, reaction-mixing coupling, non-Gaussian environmental heterogeneity, or practical tank design follow this staircase. The strict analysis excludes degenerate rates and does not optimize arbitrary continuous shape parameters. The model assumes a response can be averaged over a parcel travel-time distribution; heterogeneous groundwater reactions may violate that simplification. A literature comparison is not proof of global historical novelty, and no independent scientific audit has been performed.

## References

- Green, C. T. et al. (2010), *Mixing effects on apparent reaction rates and isotope fractionation during denitrification in a heterogeneous aquifer*, Water Resources Research, https://doi.org/10.1029/2009WR008903 (first online 2010-08-13).
- Hrachowitz, M. et al. (2010), *Gamma distribution models for transit time estimation in catchments*, Water Resources Research, https://doi.org/10.1029/2010WR009148.
- van der Velde, Y. et al. (2010), *Nitrate response of a lowland catchment*, Water Resources Research, https://doi.org/10.1029/2010WR009105.
- van der Velde, Y. et al. (2012), *Quantifying catchment-scale mixing and its effect on time-varying travel-time distributions*, Water Resources Research, https://doi.org/10.1029/2011WR011310.
- Frei, S. et al. (2019), *Quantification of Hyporheic Nitrate Removal at Reach Scale: Exposure Times Versus Residence Times*, Water Resources Research, https://doi.org/10.1029/2019WR025540.
- Mongelli, G. F. (2018), *Maximizing the Intermediate Product for 3 CSTRs in Series*, https://doi.org/10.31031/RDMS.2018.05.000621.
