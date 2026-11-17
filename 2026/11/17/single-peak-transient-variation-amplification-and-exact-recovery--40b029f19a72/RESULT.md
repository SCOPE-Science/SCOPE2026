# Single-peak transient variation amplification and exact recovery for three-state birth–death heat

## Finding

For positive birth–death rates \(a,b,c,d\), consider the real three-state heat generator
\[
(Qf)_1=a(f_2-f_1),\quad
(Qf)_2=b(f_1-f_2)+c(f_3-f_2),\quad
(Qf)_3=d(f_2-f_3).
\]
For positive edge weights \(w_1,w_2\), define \(V_w(f)=w_1|f_2-f_1|+w_2|f_3-f_2|\). The following is the exact sharp two-input operator seminorm of \(H_t=e^{tQ}\):
\[
\|H_t\|_{V_w\to V_w}=\max\{g_1(t),g_2(t)\},\qquad
 g_j(t)=\frac{(v+\delta_j)e^{-ut}-(u+\delta_j)e^{-vt}}{v-u},
\]
where
\[
\begin{aligned}
\alpha&=a+b,\quad \beta=c+d,\\
\Delta&=\sqrt{(\alpha-\beta)^2+4bc},\\
u&=(\alpha+\beta-\Delta)/2,\quad v=(\alpha+\beta+\Delta)/2,\\
\delta_1&=-\alpha+bw_2/w_1,\quad\delta_2=-\beta+cw_1/w_2.
\end{aligned}
\]
Every norm value is attained by a pair of real inputs differing in a one-edge step.

There is a complete sharp temporal classification. The operator strictly contracts differences in \(V_w\) **at every positive time** if and only if
\[
\boxed{\frac{c}{c+d}\le\frac{w_2}{w_1}\le\frac{a+b}{b}}.
\]
On either boundary, positive-time strict contraction still holds. Otherwise exactly one of the two initial slopes \(\delta_j\) is positive. Writing this slope as \(\delta>0\), the norm first rises strictly above one, reaches its unique global amplification peak at
\[
 t_* = \frac1{v-u}\log\frac{v(u+\delta)}{u(v+\delta)}
\]
with peak factor
\[
\boxed{\frac{v+\delta}{v}\left(\frac{u(v+\delta)}{v(u+\delta)}\right)^{u/(v-u)}},
\]
and then crosses the level one exactly once, at the unique \(T>t_*\) satisfying
\[
(v+\delta)e^{-uT}-(u+\delta)e^{-vT}=v-u.
\]
The norm is above one exactly for \(0<t<T\) and strictly below one for \(t>T\).

For the uniform-rate three-site heat operator, \(a=b=c=d=1\), measured in the asymmetric edge metric \((w_1,w_2)=(1,3)\), the two columns are
\[
g_1(t)=2e^{-t}-e^{-3t},\qquad g_2(t)=\tfrac23e^{-t}+\tfrac13e^{-3t}.
\]
Here the sharp peak is \(\frac43\sqrt{2/3}\) at \(t_*=\frac12\log(3/2)\), and the recovery time is exactly \(\boxed{T=\log((1+\sqrt5)/2)}\).

## Assumptions and scope

All four jump rates and both variation-edge weights are strictly positive; the state space is exactly the ordered path \(\{1,2,3\}\). Heat time is any real \(t\ge0\). The seminorm kills constants and measures differences of arbitrary real pairs, not just nonnegative or monotone inputs. The generator acts on test functions via the displayed row convention. No stationarity normalization, equality of rates, or symmetry of jump intensities is required.

## Proof

**1. Exact gradient intertwining.** Set \(Df=(f_2-f_1,f_3-f_2)^{\mathsf T}\). Direct substitution yields
\[
DQ=BD,\qquad B=\begin{pmatrix}-(a+b)&c\\b&-(c+d)\end{pmatrix}.
\]
Because \(D:\mathbb R^3\to\mathbb R^2\) is surjective, \(D e^{tQ}=e^{tB}D\) implies that the desired quotient-seminorm is precisely the induced norm of \(e^{tB}\) in weighted \(\ell^1\) with coordinate weights \(w_1,w_2\).

**2. Exact norm formula.** The real matrix \(B\) is irreducible Metzler; hence \(e^{tB}\) has strictly positive entries for \(t>0\). Its eigenvalues are \(-u,-v\), with \(0<u<v\) because \((a+b)(c+d)>bc\). For each of its two weighted column sums \(g_j(t)\), the initial value is one and the initial slope is respectively \(\delta_1,\delta_2\). The characteristic polynomial forces the scalar equation \((\partial_t+u)(\partial_t+v)g_j=0\). These two initial conditions uniquely give the displayed two-exponential formula. The weighted \(\ell^1\) norm of a positive matrix is its largest weighted column sum. Taking step inputs \((0,1,1)\) or \((0,0,1)\) realizes the corresponding columns and their ratio exactly.

**3. One unstable edge at most.** The inequalities \(\delta_1\ge0\) and \(\delta_2\ge0\) cannot both hold: their product would require \(bc\ge(a+b)(c+d)\), a strict impossibility. Equivalently the no-positive-slope weight ratios are exactly the stated closed interval. Also \(v\ge\max\{a+b,c+d\}\), so \(v+\delta_j>0\) for each column.

**4. Shape of each positive column.** Write \(g_j(t)=A e^{-ut}+(1-A)e^{-vt}\) with \(A=(v+\delta_j)/(v-u)>0\). If \(\delta_j\le0\), the derivative \(g'_j(t)\) is strictly negative for every \(t>0\): when \(A\le1\) both exponential coefficients are nonnegative, whereas for \(A>1\) the only positive derivative contribution decays at the faster rate and cannot overtake an initially nonpositive derivative. Hence \(0<g_j(t)<1\) for \(t>0\).

When \(\delta_j>0\), necessarily \(A>1\), and the derivative changes sign exactly once from positive to negative. Solving \(g'_j(t)=0\) gives \(t_*\), and substitution using the derivative identity yields the displayed sharp peak factor. Since \(g_j(0)=1\) and \(g_j(t)\to0\), strict unimodality gives a unique second level-one crossing at \(T>t_*\). The other column strictly contracts at all positive times, so the operator norm has exactly the asserted amplification and recovery interval, and the global peak comes from the unstable column.

**5. Explicit symmetric-rate witness.** For \(a=b=c=d=1\), one has \(u=1,v=3\). With \((w_1,w_2)=(1,3)\), the unstable column is \(2e^{-t}-e^{-3t}\). Writing \(q=e^{-T}\) gives \(q^3-2q+1=0\). Its nontrivial root in \((0,1)\) is \(q=(\sqrt5-1)/2\); hence \(T=\log((1+\sqrt5)/2)\). Differentiation yields the peak and time above. The step difference \((0,1,1)\) attains the unstable column at every time.

## Verification

The included `check_three_site_heat.py` independently constructs the three-state Markov semigroup by uniformization and compares its two step-input variation ratios with the spectral formulas for 350 deterministic randomized positive-rate cases. It also tests one-peak and unique-root behavior and checks the golden-ratio identity. Execution: `python3 check_three_site_heat.py`. All tests passed. The analytical steps above, not the finite tests, establish the theorem for arbitrary positive real parameters and times.

## Relationship to prior work

Chafaï and Joulin, *Intertwining and commutation relations for birth-death processes* (first public preprint 2010), establish general gradient intertwinings and Lipschitz/Wasserstein contraction tools. Cloez and Delplancke (first public preprint 2016) further study first- and second-order discrete gradient intertwinings. These underpin gradient positivity and are not claimed new. The present result concerns the exact **weighted \(\ell^1\) gradient norm**, its complete single-peak temporal classification and recovery threshold on three states, rather than the weighted \(\ell^\infty\) gradient contraction emphasized in those sources. Related finite-graph heat results give all-time contraction criteria or different graph profiles, not the stated fully resolved three-state recovery law. Full historical priority is not asserted.

## Limitations

This is a finite three-state theorem, not an all-dimensional birth–death classification. In general the unique positive recovery time is specified by an exact two-exponential equation and need not have an elementary expression. Four or more states may have different branch-switching or multi-peak behavior. The comparison with several related indexed finite-graph heat results is based on their available descriptions rather than full-text inspection, so unrecognized coverage remains a priority risk. External independent validation has not been performed.

## References

1. D. Chafaï and A. Joulin, *Intertwining and commutation relations for birth-death processes*, arXiv:1011.2331v1 (first public 2010-11-10), https://arxiv.org/abs/1011.2331.
2. B. Cloez and C. Delplancke, *Intertwinings and Stein's magic factors for birth-death processes*, arXiv:1609.08390v1 (first public 2016-09-27), https://arxiv.org/abs/1609.08390.
