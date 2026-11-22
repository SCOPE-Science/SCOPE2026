# A sharp two-band wildlife curtailment criterion at turbine rated power

## Finding

**Theorem (two-band classification and strict one-cutoff loss).** Let \(R:(0,\infty)\to(0,\infty)\) be continuously differentiable and let its logarithmic wind-speed elasticity
\[
\mathcal E(v)=\frac{vR'(v)}{R(v)}
\]
be continuous and strictly decreasing, with \(\lim_{v\downarrow0}\mathcal E(v)>3\) and \(\lim_{v\to\infty}\mathcal E(v)<0\). These extended limits may be infinite. Write \(v_3\) and \(v_0\) for the unique solutions of \(\mathcal E(v_3)=3\) and \(\mathcal E(v_0)=0\), so \(0<v_3<v_0\). For any rated wind speed \(v_r>0\), put \(P(v)=\min\{v^3,v_r^3\}\) and \(q(v)=R(v)/P(v)\).

Let \(w(v)>0\) be a measurable wind-speed density almost everywhere, with \(\int_0^\infty w(v)\,dv=1\) and finite positive integrals of \(P(v)w(v)\) and \(R(v)w(v)\). Under a nonzero risk cap \(0<B<\int_0^\infty R(v)w(v)\,dv\), choose any measurable operating fraction \(u(v)\in[0,1]\) to maximize
\[
\mathcal P(u)=\int_0^\infty P(v)w(v)u(v)\,dv
\qquad\text{subject to}\qquad
\mathcal R(u)=\int_0^\infty R(v)w(v)u(v)\,dv\le B.
\]
There is exactly one cutoff \(c\in(0,\max q)\) satisfying \(\int_{\{q<c\}}Rw=B\), and the unique optimal policy up to \(w\)-null sets is \(u_c(v)=\mathbf1_{\{q(v)<c\}}\). Thus the curtailed wind speeds are exactly \(\{q>c\}\) up to finitely many boundary points.

**Sharp topology law.** Two disjoint nonempty curtailed intervals occur for a nonempty open interval of risk caps **if and only if**
\[
\boxed{v_3<v_r<v_0}\quad\text{or, equivalently,}\quad \boxed{0<\mathcal E(v_r)<3}.
\]
Under this condition the two-band regime is exactly
\[
q(v_r)<c<\min\{q(v_3),q(v_0)\}.
\]
The four boundary wind speeds lie in \((0,v_3)\), \((v_3,v_r)\), \((v_r,v_0)\), and \((v_0,\infty)\). Outside this sharp rated-speed range, the curtailment set is empty or one interval for every risk cap. Whenever the two-band regime occurs, every single cut-in operating policy \(u(v)=\mathbf1_{\{v\ge h\}}\) meeting the same cap has strictly lower expected power than \(u_c\).

## Assumptions and scope

The operation decision is a measurable function of wind speed alone, with no intertemporal switching cost or minimum on/off duration. The idealized power curve grows cubically up to rated speed and is constant thereafter, with no hard cut-in or high-speed cut-out. The collision-risk proxy \(R\) is **conditional risk during operation**, not an empirically fitted fatality law; it is zero when the turbine is curtailed. The distribution \(w\) is positive almost everywhere and is unaffected by operating decisions. Positive multiplicative constants in \(P\), \(R\) merely rescale the units and budget. This theorem does not assert that any observed turbine or species has the hypothesized elasticity pattern.

A hard physical cut-in speed below the first of the four crossings can be added in the two-band example without changing either curtailment interval; operation below that speed then contributes neither power nor risk. This is a boundary robustness observation, not a different primary theorem.

## Proof

**1. Critical speeds and exact geometry.** Strictly decreasing continuous \(\mathcal E\) with endpoint limits crossing \(3\) and \(0\) yields unique \(v_3<v_0\). Logarithmic differentiation gives, for \(v\ne v_r\),
\[
\frac{vq'(v)}{q(v)}=
\begin{cases}\mathcal E(v)-3,&0<v<v_r,\\
\mathcal E(v),&v>v_r.
\end{cases}
\]
Hence on the lower-power branch \(q\) increases until \(v_3\) and then decreases; on the rated branch it increases until \(v_0\) and then decreases, with branches joined continuously at \(v_r\). If \(v_3<v_r<v_0\), \(q\) has strict maxima at \(v_3,v_0\) and a strict minimum at \(v_r\). Otherwise the joined curve is strictly increasing up to one maximum and strictly decreasing afterward (possible stationary junctions do not create a second maximum). Therefore the strict superlevel set \(\{q>c\}\) has exactly two connected components precisely for the stated nonempty interval of \(c\); otherwise it has at most one.

The endpoint conditions guarantee \(q(v)\to0\) at both ends. Indeed, choose \(\epsilon>0\) so that \(\mathcal E(v)>3+\epsilon\) for sufficiently small \(v\). Integrating \(d\log(R/v^3)/d\log v=\mathcal E-3\) toward zero gives \(q(v)=O(v^\epsilon)\). For sufficiently large \(v\), \(\mathcal E(v)<-\epsilon\); integrating \(d\log R/d\log v=\mathcal E\) gives \(R(v)=O(v^{-\epsilon})\), and the rated power is constant. Thus \(q(v)\to0\) as \(v\to\infty\).

**2. Existence and uniqueness of the budget cutoff.** Define \(M(c)=\int_{\{q<c\}}Rw\) for \(0<c<\max q\). Since \(q\) is strictly monotone on finitely many branch segments, each interior level set is finite and has measure zero. Dominated convergence makes \(M\) continuous. For any \(0<c_1<c_2<\max q\), the set \(\{c_1<q<c_2\}\) contains an open interval; hence positivity of \(R,w\) makes \(M(c_2)>M(c_1)\). Its endpoint limits are \(0\) and \(\int Rw\), by dominated convergence and the absence of a positive-measure maximum level set. Thus each permitted budget gives exactly one \(c\).

**3. Global optimality and strictness.** Write \(u_*=\mathbf1_{\{q<c\}}\). Since \(P-R/c\) is positive exactly where \(u_*=1\) and negative exactly where \(u_*=0\), for any feasible \(u\)
\[
\mathcal P(u_*)-\mathcal P(u)
=\int (u_*-u)(P-R/c)w
+\frac{\mathcal R(u_*)-\mathcal R(u)}{c}\ge0.
\]
The first term is strictly positive if \(u\ne u_*\) on a set of positive \(w\)-measure away from the finite level set \(q=c\). Hence the optimizer is unique almost everywhere. In the two-band regime, no single cut-in policy can agree with the two separated curtailed intervals, so its expected power is strictly smaller whenever it satisfies the risk cap. Both the sharp converse and all boundary cases follow from the geometry in step 1.

**4. Exact attainability.** Take \(R(v)=v^4e^{-v}\), \(v_r=2\), and \(w(v)=e^{-v}\). Then \(\mathcal E(v)=4-v\), so \(v_3=1\), \(v_0=4\). The ratio is \(q(v)=ve^{-v}\) below rated speed and \(q(v)=v^4e^{-v}/8\) above. At the exact ratio cutoff \(c=3/10\), the four boundaries are the unique solutions of \(q(v)=3/10\) in \((0,1)\), \((1,2)\), \((2,4)\), and \((4,\infty)\), respectively. Indeed \(q(2)=2e^{-2}<3/10<e^{-1}=q(1)\) and \(3/10<32e^{-4}=q(4)\). These inequalities follow without numerical approximation from \(8/3<e<3\). Thus two separated curtailment bands are certified analytically.

## Verification

The preceding steps prove the result for **every** stated \(R,v_r,w,B\); no finite sampling is used to infer a universal claim. The accompanying standalone `CHECK.py` implements bisection and elementary exponential antiderivatives using Python's standard library. For the exact example its four wind-speed boundaries are approximately \(0.489402227180\), \(1.781337023422\), \(2.108568625354\), and \(6.781072167850\). With \(w(v)=e^{-v}\), the resulting exact-cap policy has risk about \(0.099673738415\) and power about \(0.353085030152\). The best pure cut-in policy at that risk cap starts at wind speed approximately \(3.744279531455\) and yields power about \(0.189221311286\). The higher power is a property of this stylized example, not an estimated field gain. Here the total all-on risk is exactly \(3/4\), and numerical values are supplementary to the analytic strict inequality.

## Relationship to prior work

Whitby et al. (2024) report the measured effectiveness of low-wind curtailment at wind facilities, without giving the elasticity classification above. Peterson et al. (2021) link nacelle-acoustic activity to fatalities and study low-wind cut-in treatments, not the present exact shape theorem. Maclaurin et al. (2022) simulate energy losses for blanket and smart cut-in strategies. Rogers (2020) treats general environmental curtailment using dynamic programming; that optimization framework is acknowledged and is not claimed as new. Behr et al. (2016) describe bat-friendly algorithms prioritizing high predicted fatality risk and low energy yield, a substantial conceptual predecessor. Their full report was not inspectable here; the source's public summary was read. These works motivate the specific question of when a single monotone speed cutoff cannot represent the optimum, but the accessible inspected text does not state the rated-power elasticity criterion or its necessary-and-sufficient two-band conclusion.

The familiar exchange/likelihood-ratio rule for maximizing one integral under another integral constraint is likewise **not** claimed as new. The claimed contribution is the sharp topological characterization for any continuously decreasing risk elasticity across a cubic-to-rated power curve, plus the precise nonempty budget window and example. Public bibliographic searches and available prior mathematical records found no equivalent theorem. This is evidence-limited originality, not proof of historical priority.

## Limitations

Actual bat collision risk often concentrates at relatively low wind speeds; the theorem's two-band regime requires a particular elasticity relationship to rated speed and is not asserted for the empirical sites in the references. It ignores cut-out speeds, stochastic forecasts, operating wear, species-specific ecological weighting, law and permitted fatality caps, temporal correlation, switching constraints, and multi-turbine wake effects. The 2016 RENEBAT II report was relevant but accessible only through its public summary; a complete priority comparison against it remains a residual risk. The analytic classification also inherits the assumed linear additivity of energy and conditional risk over wind speeds.

## References

1. Whitby, M. D., O'Mara, M. T., Hein, C. D., Huso, M., and Frick, W. F. (2024). *A decade of curtailment studies demonstrates a consistent and effective strategy to reduce bat fatalities at wind turbines in North America.* Ecological Solutions and Evidence 5:e12371. First public 2024-08-23. https://doi.org/10.1002/2688-8319.12371
2. Peterson, T. S., McGill, B., Hein, C. D., and Rusk, A. (2021). *Acoustic Exposure to Turbine Operation Quantifies Risk to Bats at Commercial Wind Energy Facilities.* Wildlife Society Bulletin 45:552–565. https://doi.org/10.1002/wsb.1236
3. Maclaurin, G., Hein, C., Williams, T., Roberts, O., Lantz, E., Buster, G., and Lopez, A. (2022). *National-scale impacts on wind energy production under curtailment scenarios to reduce bat fatalities.* Wind Energy 25:1514–1529. https://doi.org/10.1002/we.2741
4. Rogers, J. (2020). *Optimal strategies for wind turbine environmental curtailment.* Wind Energy 23:1331–1350. https://doi.org/10.1002/we.2489
5. Behr, O. et al. (2016). *Reducing the Collision Risk for Bats at Onshore Wind Turbines (RENEBAT II).* Public summary. https://tethys.pnnl.gov/publications/reducing-collision-risk-bats-onshore-wind-turbines-renebat-ii
6. Neyman, J. and Pearson, E. S. (1933). *On the Problem of the Most Efficient Tests of Statistical Hypotheses.* Philosophical Transactions of the Royal Society A 231:289–337. The exchange principle is acknowledged as classical.
