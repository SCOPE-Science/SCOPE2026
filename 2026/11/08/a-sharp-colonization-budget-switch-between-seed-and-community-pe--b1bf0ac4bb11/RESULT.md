# A sharp colonization-budget switch between seed and community persistence on three habitats

## Finding

Consider a three-habitat path \(L-C-R\). Each occupied habitat becomes empty at rate one. An empty habitat is recolonized from each occupied neighboring habitat independently, at symmetric per-link rates \(a\ge0\) for \(L-C\) and \(b\ge0\) for \(C-R\). There is no immigration from outside; total extinction is absorbing. Fix a strictly positive colonization budget \(s=a+b\), and let \(\tau\) be the first time all three habitats are empty.

**Sharp optimal-allocation theorem.** If only the center \(C\) is initially occupied, the allocations maximizing \(\mathbb E\tau\) are precisely

\[
\begin{cases}
(a,b)=(s,0)\text{ or }(0,s),&0<s<1,\\
(a,b)=(s,0),(0,s),\text{ or }(s/2,s/2),&s=1,\\
(a,b)=(s/2,s/2),&s>1.
\end{cases}
\]

If **all three** habitats are initially occupied, the unique maximizer is \(a=b=s/2\) for *every* \(s>0\). Thus the same dispersal-budget optimization exhibits a sharp initialization-dependent concentration/diversification transition at \(s=1\). The result includes both boundary allocations, where one corridor receives zero colonization rate.

For contrast, the weighted adjacency matrix of this same path has spectral radius \(\sqrt{a^2+b^2}\), which under the same budget is maximized by the *concentrated* allocations at every \(s>0\). This spectral comparison is an elementary baseline; the newly established assertion is the exact stochastic extinction-time classification and its difference by initial condition. With a common local extinction rate \(e>0\) instead of one, rescaling time gives the switching condition \(a+b=e\).

## Assumptions and scope

The state is the subset \(S\subseteq\{L,C,R\}\) of occupied habitats. For each \(v\in S\), a local extinction transition \(S\to S\setminus\{v\}\) occurs at rate one. For each \(v\notin S\), a recolonization transition \(S\to S\cup\{v\}\) occurs at rate \(c_v(S)=\sum_{w\in S:\,\{v,w\}\in E}w_{vw}\), where \(w_{LC}=a\) and \(w_{CR}=b\). There are no other transitions, no external source, and no distinction between multiple immigrants arriving at an already occupied habitat. Absorption at \(\varnothing\) occurs almost surely for all finite \(a,b\ge0\), because every nonempty state has a positive-probability sequence of local extinctions without intervening recolonizations. We optimize the **unconditional expectation of the time until global extinction**, not the time until the first local loss, the total occupied-habitat time, or a deterministic growth exponent.

The domain of the theorem is \(s>0\), \(a,b\ge0\), and \(a+b=s\). The graph may disconnect at the permitted boundary. All equalities and optimizer statements include the critical value \(s=1\).

## Proof

Write \(t_S=\mathbb E_S\tau\) for nonempty \(S\) and \(t_{\varnothing}=0\). First-step conditioning gives the exact seven-equation Markov reward system

\[
\left(|S|+\sum_{v\notin S}c_v(S)\right)t_S
=1+\sum_{v\in S}t_{S\setminus\{v\}}+
\sum_{v\notin S}c_v(S)t_{S\cup\{v\}},\qquad S\ne\varnothing.
\]

The coefficient matrix is the nonsingular transient negative generator; consequently the system has exactly one solution. Put \(p=ab\) and \(H=(s+1)(s+6)\). Direct elimination of these *specified* seven equations gives the central-seed expectation

\[
T_C(s,p)=t_{\{C\}}=
\frac{(s+2+p)[H+(s+3)p]}{2[H+(2s+7)p]}
\tag{1}
\]

and the full-occupancy expectation

\[
T_F(s,p)=t_{\{L,C,R\}}=
\frac{A(s,p)}{2(s+2)[H+(2s+7)p]},
\tag{2}
\]

where the explicit polynomial is

\[
\begin{aligned}
A(s,p)={}&(s+3)^2p^2+(2s^3+20s^2+60s+56)p\\
&+s^4+12s^3+51s^2+84s+44.
\end{aligned}
\]

These identities can be checked without relying on decimals by substitution into the seven first-step equations, or by executing the exact symbolic and rational checker accompanying this proof. The only dependence on the two allocations is through \(s\) and \(p\), and the budget constraint implies \(0\le p\le s^2/4\), with equality at balanced allocation and \(p=0\) exactly at the two concentrated allocations.

For the central seed, subtracting the concentrated value from (1) gives

\[
T_C(s,p)-T_C(s,0)=
\frac{p[(s+3)p+s-2]}{2[H+(2s+7)p]}.
\tag{3}
\]

When \(0<s<1\), we have

\[
(s+3)p+s-2\le\frac{(s+3)s^2}{4}+s-2
=\frac{(s-1)(s^2+4s+8)}4<0,
\]

so every interior split has strictly smaller expectation than the two concentrated endpoints. At \(s=1\), (3) is negative for \(0<p<1/4\) and zero precisely at \(p=0\) and \(p=1/4\). When \(s>1\), subtraction of the balanced value instead yields the exact identity

\[
T_C(s,p)-T_C(s,s^2/4)=
\frac{(4p-s^2)[(s+3)(2s+3)p+(s-1)(s+1)(s+6)]}
{8(2s+3)[H+(2s+7)p]}.
\tag{4}
\]

Its numerator is strictly negative whenever \(p<s^2/4\), since the first factor is negative and the second is positive. This proves all central-seed regimes including uniqueness/ties.

For full occupancy, differentiation of (2) with respect to \(p\), at fixed \(s\), gives

\[
\frac{\partial T_F}{\partial p}=
\frac{N(s,p)}{2(s+2)[H+(2s+7)p]^2},
\tag{5}
\]

where

\[
\begin{aligned}
N(s,p)={}&(2s^3+19s^2+60s+63)p^2\\
&+(2s^4+26s^3+114s^2+198s+108)p\\
&+3s^4+26s^3+71s^2+76s+28.
\end{aligned}
\]

Every coefficient is strictly positive for \(s>0\), hence (5) is positive throughout the full feasible interval. As \(p\) is uniquely maximized by \(a=b=s/2\), so is \(T_F\). Finally, the weighted adjacency matrix has characteristic polynomial \(z(z^2-a^2-b^2)\); thus its spectral radius is \(\sqrt{s^2-2p}\), strictly decreasing in \(p\). This establishes the stated contrast. Changing the local extinction rate to \(e\) and dividing every transition rate by \(e\) proves the final rescaling assertion. \(\square\)

## Verification

The included `verify.py` constructs the seven-state transient generator from the transition definition, symbolically inverts it, and checks (1), (2), (3), (4) at the endpoints, and (5). Separately, an independently written rational Gaussian solver checks the expected extinction times for 240 initial-state/rate configurations. Seven exact budget values are used for 21 endpoint/threshold comparisons. All checks passed on the packaged source path. The symbolic calculations verify the algebraic identities; the inequalities and global optimizer classifications above are proved for the full continuous parameter domain, not inferred from the finite test grid.

One exact comparison: at \(s=2\) the central-seed concentrated lifetime is \(T_C(2,0)=2\), while the balanced choice gives \(T_C(2,1)=29/14\), strictly larger. At \(s=1/2\) the balanced choice is worse than concentration by exactly \(1/256\). At \(s=1\) balanced and both concentrated choices tie at \(3/2\), while every strictly intermediate split is worse.

## Relationship to prior work

Artzy-Randrup and Stone (2010) study connectivity, cycles and persistence thresholds of an age-structured *linear deterministic* metapopulation, with network spectral radius as a central threshold quantity. Their analysis does not determine finite stochastic absorption times or seed-sensitive optimal budget divisions. Ross and Pollett (2009 conference article, 2010 journal version) study expected metapopulation extinction time and allocation between aggregate colonization and extinction-rate improvement, but their materially inspected 2009 model uses a single homogeneous colonization parameter rather than an optimally split pair of fixed-sum link rates with different initial occupancy sets. Mountford et al. (2016) develop asymptotic contact-process extinction-time bounds for large finite graphs started from all occupied; those bounds do not classify the exact three-site link-budget optimum. Etienne and Heesterbeek (2001) offer broader metapopulation-management rules; the available abstract does not state the present sharp threshold, but complete-text historical coverage remains a risk. The supplied seven-state calculation is not a restatement of the cited papers' general spectral or homogeneous-budget conclusions.

## Limitations

The stochastic model is a deliberately small, fully specified three-patch benchmark with memoryless local losses, constant colonization strengths and no exogenous immigrants. The optimal rate can be zero, disconnecting the network; if both corridors must remain strictly positive, the concentrated optimum for \(s<1\) is a supremum rather than an attained optimum. Mean absorption time is only one persistence criterion; optimizing a quantile or fixed-deadline survival probability is not addressed. The linear spectral radius belongs to a different deterministic persistence proxy, so no equivalence between these objectives is claimed. Historical priority is provisional because some relevant full journal texts were not accessible; the theoretical result does not itself justify any field conservation intervention.

## References

1. Artzy-Randrup, Y., and Stone, L. (2010). *Connectivity, Cycles, and Persistence Thresholds in Metapopulation Networks*. PLOS Computational Biology 6(8), e1000876. First published online 2010-08-05. https://doi.org/10.1371/journal.pcbi.1000876 . Full article: https://pmc.ncbi.nlm.nih.gov/articles/PMC2916855/ .
2. Ross, J. V., and Pollett, P. K. (2009). *Rules of thumb for metapopulation management*. MODSIM09 conference, pp. 1795–1801. https://www.maths.uq.edu.au/MASCOS/MODSIM09/RossPollett.pdf .
3. Ross, J. V., and Pollett, P. K. (2010). *Simple rules for ranking and optimally managing metapopulations*. Ecological Modelling 221, 2515–2520. https://doi.org/10.1016/j.ecolmodel.2010.02.016 .
4. Etienne, R. S., and Heesterbeek, J. A. P. (2001). *Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model*. The American Naturalist 158, 389–407. https://doi.org/10.1086/321986 .
5. Mountford, T., Mourrat, J.-C., Valesin, D., and Yao, Q. (2016). *Exponential extinction time of the contact process on finite graphs*. Stochastic Processes and their Applications 126, 1974–2013. https://doi.org/10.1016/j.spa.2016.01.001 .
