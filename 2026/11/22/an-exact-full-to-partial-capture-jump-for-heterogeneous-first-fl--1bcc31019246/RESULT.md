# An exact full-to-partial capture jump for heterogeneous first-flush wash-off

## Finding

In an ideal single-event stormwater capture model with exponentially decreasing total runoff and a mixture of independent first-order pollutant stocks, the capacity maximizing captured mass minus linear storage cost undergoes a **discontinuous jump from full capture to a uniquely determined partial volume**. This happens for every positive probability law of wash-off rates satisfying a strict mean-versus-runoff condition and a nonzero slow-wash-off component. An exact marginal equation determines the partial-capacity branch, which then decreases continuously to zero as cost rises. At the jump, and only there, full and partial capture are both globally optimal.

This is a statement about an idealized single event and ideal instantaneous diversion of its initial runoff. It does not describe a finite-duration storm, interevent carryover, or engineering tank operations.

## Assumptions and scope

Let \(\gamma>0\) be a runoff decay rate, and let \(K\) be a strictly positive random wash-off rate with a probability law \(\nu\). The law is weighted by the initial pollutant mass carried by each kinetic class, not by the number of classes. Assume

\[
0<\mu:=\mathbb E[K]<\infty,\qquad \mu>\gamma,
\qquad \Pr(K<\gamma)>0.
\]

The idealized runoff hydrograph has normalized cumulative volume \(v(t)=1-e^{-\gamma t}\) for \(t\ge0\), ultimately tending to one. Each pollutant class is fully available at time zero and its remaining mass fraction after time \(t\) is \(e^{-Kt}\). There is no fresh pollutant supply, resuspension, infiltration, or hydraulic feedback. Define the cumulative pollutant-mass fraction captured by an initial runoff volume \(v\in[0,1]\) as

\[
F(v)=1-\mathbb E\big[(1-v)^{K/\gamma}\big]\quad(0\le v<1),
\qquad F(1)=1.
\]

This formula follows by taking \(t=-\log(1-v)/\gamma\); its terminal value uses \(K>0\) almost surely. For each dimensionless marginal storage cost \(c\ge0\), maximize \(J_c(v)=F(v)-cv\) over the entire compact interval \([0,1]\).

Define the positive, finite function

\[
H(t)=\mathbb E[e^{(\gamma-K)t}],\qquad t\ge0.
\]

There is a unique \(t_*\in(0,\infty)\) solving \(H'(t_*)=0\). Put

\[
v_*=1-e^{-\gamma t_*},\qquad c_*=H(t_*).
\]

Then \(0<v_*<1\) and \(0<c_*<1<\mu/\gamma\). The **complete global optimizer set**, including all equality cases, is

\[
\operatorname{argmax}_{0\le v\le1}J_c(v)=
\begin{cases}
\{1\},&0\le c<c_*,\\
\{v_*,1\},&c=c_*,\\
\{v_c\},&c_*<c<\mu/\gamma,\\
\{0\},&c\ge\mu/\gamma.
\end{cases}
\]

Here \(v_c=1-e^{-\gamma t_c}\in(0,v_*)\) and \(t_c\in(0,t_*)\) is the unique solution to

\[
c=\frac1\gamma\mathbb E\big[K e^{(\gamma-K)t_c}\big].
\]

The function \(c\mapsto v_c\) is strictly decreasing and continuous on \((c_*,\mu/\gamma)\), with one-sided limits \(v_*\) and \(0\), respectively. The optimizer jumps by \(1-v_*>0\) when \(c\) increases through \(c_*\). The upper concave envelope of \(F\) is exactly \(F\) on \([0,v_*]\) and \(1-c_*(1-v)\) on \([v_*,1]\).

The mass-versus-volume flush surplus has exactly one interior sign change: \(F(v)>v\) for \(0<v<v_{\mathrm{cross}}\) and \(F(v)<v\) for \(v_{\mathrm{cross}}<v<1\), where \(v_{\mathrm{cross}}>v_*\) corresponds to the unique solution \(H(t)=1\) with \(t>0\).

## Proof

**Regularity and unique critical time.** For every \(t>0\), differentiating \(H\) under the expectation is justified because \((\gamma-K)^j e^{(\gamma-K)t}\) is bounded on \(K>0\) for \(j=1,2\) locally away from \(t=0\). At zero, the first derivative exists by \(\mathbb E[K]<\infty\). Consequently

\[
H(0)=1,\qquad H'(0+)=\gamma-\mu<0,\qquad
H''(t)=\mathbb E[(\gamma-K)^2e^{(\gamma-K)t}]>0\quad(t>0).
\]

Strictness follows because \(\Pr(K<\gamma)>0\). There exists \(\varepsilon>0\) with \(\Pr(K\le\gamma-\varepsilon)>0\); hence \(H(t)\to\infty\) as \(t\to\infty\), and the positive slow-rate contribution also makes \(H'(t)>0\) for all sufficiently large \(t\). Thus \(H'\) has exactly one root \(t_*\), the unique strict global minimum, giving \(0<c_*<1\).

**Supporting chord and exact envelope.** For \(t=-\log(1-v)/\gamma\),

\[
1-F(v)=\mathbb E[e^{-Kt}]=e^{-\gamma t}H(t)=(1-v)H(t).
\]

Since \(H(t)\ge c_*\), it follows for \(0\le v<1\) that

\[
F(v)\le 1-c_*(1-v)=:\ell(v).
\]

Equality occurs for finite \(t\) if and only if \(t=t_*\), corresponding to \(v=v_*\). At \(v=1\), equality holds by the terminal definition. The slope for finite \(t\) is

\[
F'(v)=\frac{\mathbb E[K e^{(\gamma-K)t}]}{\gamma}
=H(t)-\frac{H'(t)}\gamma.
\]

Its derivative with respect to \(t\) on \((0,t_*]\) is \(H'(t)-H''(t)/\gamma<0\). Hence \(F\) is strictly concave on \([0,v_*]\), and \(F'(0+)=\mu/\gamma\), \(F'(v_*)=c_*\). Joining this concave segment to the line \(\ell\) gives a concave majorant of \(F\), tangent at \(v_*\). Every concave majorant must dominate the chord between the two points \((v_*,F(v_*))\) and \((1,F(1))\). Therefore this piecewise function is exactly the least concave majorant (upper concave envelope).

**All global maxima.** If \(0\le c<c_*\), the supporting line gives

\[
J_c(v)\le 1-c_*+(c_*-c)v\le1-c=J_c(1),
\]

with strict inequality unless \(v=1\). At \(c=c_*\), equality holds precisely at \(v=v_*\) or \(v=1\). For \(c>c_*\), any \(v>v_*\) is worse than \(v_*\) by the same supporting-line inequality; hence the unique maximum is the unique maximum over \([0,v_*]\). On this interval \(F'\) decreases strictly from \(\mu/\gamma\) to \(c_*\). Thus, for \(c_*<c<\mu/\gamma\), there is a unique interior solution of \(F'(v)=c\), and it is the unique global maximum. For \(c\ge\mu/\gamma\), strict decrease of the derivative makes \(v=0\) the unique maximum. The continuous, strictly decreasing inverse of \(F'\) proves the branch and limit statements, including the jump.

**Unique first-to-last-flush crossing.** For \(0\le v<1\), \(F(v)-v=(1-v)(1-H(t))\). The strictly convex function \(H\) starts at one with negative right derivative, has its unique minimum below one at \(t_*\), and diverges to infinity. It therefore returns to one exactly once at a finite \(t>t_*\), establishing the strict sign classification.

**Explicit two-rate witness.** Take \(\gamma=1\), \(\Pr(K=1/2)=1/4\), \(\Pr(K=3/2)=3/4\). Then \(\mu=5/4\),

\[
F(v)=1-\tfrac14\sqrt{1-v}-\tfrac34(1-v)^{3/2},\qquad
H(t)=\tfrac14e^{t/2}+\tfrac34e^{-t/2}.
\]

Direct differentiation gives \(t_*=\log3\), \(v_*=2/3\), and \(c_*=\sqrt3/2\). The unique positive flush crossing occurs at \(t=2\log3\), corresponding to \(v_{\mathrm{cross}}=8/9\). For \(\sqrt3/2<c<5/4\), the unique partial optimum is exactly

\[
v_c=1-\frac1{(4c-\sqrt{16c^2-9})^2}.
\]

All rates and weights are strictly admissible. The finite two-class case is a nontrivial instance of the arbitrary-law theorem.

## Verification

Run `python3 checker.py` using only the Python standard library. It prints `PASS: 111355 deterministic assertions` with a fixed random seed. These checks compare objective values on deterministic grids for a two-rate exact witness and 110 heterogeneous finite-support laws, in addition to checking the derivative thresholds. They do **not** prove the theorem for arbitrary laws: that proof is the inequalities and derivative arguments above. Independently check the identities \(H'(\log3)=0\), \(H(\log3)=\sqrt3/2\), and \(H(2\log3)=1\).

## Relationship to prior work

Urban-runoff engineering has long used cumulative mass versus runoff volume, or \(M(V)\), curves to assess first flush and size runoff-retention structures. Balistrocchi, Grossi, and Bacchi (2009) give a full analytical probabilistic tank-efficiency method built around a power-law typical \(M(V)\) curve and stochastic storms. Their full-text results do not provide the arbitrary-wash-off-rate distribution, its exact tangent threshold, or a complete four-regime *single-event linear-cost* optimizer. Kang's (2005) thesis documents physically motivated short-term and long-term pollutant sources and a two-phase washoff model, but with different hydraulics and erosion rules rather than this exponential-flow idealization. Guo and Urbonas (2002; open 2000 precursor report) develop normalized runoff **event-frequency** capture and delivery curves for water-quality basins, not this **within-one-event pollutant mass** objective.

These comparisons do not establish absolute historical novelty: general least-concave-majorant arguments are classical, published variants of multi-rate wash-off or economic design may include overlapping special cases, and Millar (1999) was accessible only via its article abstract. The stated contribution is the explicit mathematical classification for the defined assumptions, not a claim that convex geometry or first-flush modeling originated here.

## Limitations

The total runoff volume is normalized to one and is reached only in the infinite-time limit. Accordingly, the full-capture solution represents an ideal asymptotic tank volume, not a claim of finite event completion. The pollutant stock rates are constant in clock time and no new pollutant enters during the event; realistic erosion coefficients often depend on local shear, discharge or rainfall. The cost is linear in normalized captured volume and fixed across a single specified event. Changing to nonlinear costs, a finite storm termination, non-exponential hydrographs or delayed stock activation can destroy the classification. This result establishes no empirical fit, uncertainty interval, multi-storm design optimum, or tested field operating policy. It does not prove originality against every inaccessible relevant article or engineering report.

## References

1. Balistrocchi, M., Grossi, G., and Bacchi, B. (2009). *An analytical probabilistic model of the quality efficiency of a sewer tank*. Water Resources Research 45, W12420. First public date 2009-12-29. https://doi.org/10.1029/2009WR007822
2. Kang, J. (2005). *Modeling First Flush and Particle Destabilization: Implications for Design and Operation of Stormwater BMPs*. UCLA dissertation. https://www.seas.ucla.edu/stenstro/d/d39.pdf
3. Guo, J. C. Y., and Urbonas, B. (2002). *Runoff Capture and Delivery Curves for Storm-Water Quality Control Designs*. Journal of Water Resources Planning and Management 128, 208–215. https://doi.org/10.1061/(ASCE)0733-9496(2002)128:3(208); publicly accessible precursor https://mhfd.org/wp-content/uploads/2019/12/RunoffCaptureCRV-GuoBen.pdf
4. Millar, R. G. (1999). *Analytical Determination of Pollutant Wash-Off Parameters*. Journal of Environmental Engineering 125, 989–992. https://doi.org/10.1061/(ASCE)0733-9372(1999)125:10(989) (published online 1999-10-01; abstract inspected; full text not obtained).
