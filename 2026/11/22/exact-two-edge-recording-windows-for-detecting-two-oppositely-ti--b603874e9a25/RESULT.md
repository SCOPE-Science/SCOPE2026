# Exact two-edge recording windows for detecting two oppositely timed acoustic species

## Finding

Consider two independently calling species with opposite exponential time-of-night activity. Under a fixed recording-time budget, the **unique** (up to changes on null sets) schedule maximizing the probability of recording at least one call of **each** species always consists of an initial and a terminal window; no intermediate recording segment is needed. The optimum has three sharp regimes: terminal only, a unique nonempty window at each end, or initial only. The two one-sided transitions are specified by explicit monotone scalar equations. With equal call amplitudes the two windows have equal length. For any fixed positive amplitudes, the optimal window lengths become asymptotically equal as the recording budget tends to zero.

The precise statement is as follows. Let \(H>0\), \(0<B<H\), \(\kappa>0\), and \(a,b>0\). On \([0,H]\) the two independent inhomogeneous Poisson call processes have intensities
\[
\lambda_1(t)=a e^{-\kappa t},\qquad
\lambda_2(t)=b e^{-\kappa(H-t)}.
\]
For any measurable recording set \(E\subseteq[0,H]\) of Lebesgue measure \(|E|=B\), write \(P(E)\) for the probability that at least one call of each species is recorded in \(E\).

For \(0\le x\le B\), set
\[
E_x=[0,x]\cup[H-B+x,H],
\]
where an interval of zero length is omitted. Define
\[
U(x)=\frac a\kappa\left(1-e^{-\kappa x}+e^{-\kappa H}(e^{\kappa(B-x)}-1)\right),
\]
\[
V(x)=\frac b\kappa\left(1-e^{-\kappa(B-x)}+e^{-\kappa H}(e^{\kappa x}-1)\right).
\]
There is a unique \(x_*\in[0,B]\) maximizing
\[
P(E_x)=(1-e^{-U(x)})(1-e^{-V(x)}),
\]
and \(E_{x_*}\) uniquely maximizes \(P(E)\) among **all** measurable recording sets of measure \(B\), modulo null sets.

Write
\[
h=\frac{1-e^{-\kappa B}}\kappa,\qquad s=e^{-\kappa(H-B)}h,
\qquad \phi_z(u)=\frac{u}{e^{zu}-1}\quad(u,z>0).
\]
For every \(v>0\), let \(A_c(v)\) be the unique positive solution \(u\) of
\[
\phi_s(u)=e^{-\kappa B}\phi_h(v).
\]
Then the *complete, disjoint* optimality classification is:

- \(x_*=0\) exactly when \(a\ge A_c(b)\) (terminal-only recording).
- \(x_*=B\) exactly when \(b\ge A_c(a)\) (initial-only recording).
- Otherwise \(0<x_*<B\), and \(x_*\) is the unique root of
\[
\frac{a e^{-\kappa x}}{e^{U(x)}-1}=\frac{b e^{-\kappa(B-x)}}{e^{V(x)}-1}.
\]

In particular, \(a=b\) implies \(x_*=B/2\). If \(H,\kappa,a,b\) remain fixed as \(B\downarrow0\), then \(x_*/B\to1/2\).

## Assumptions and scope

Calling processes are independent conditional on the given deterministic intensities. A call occurring while the recorder is on is detected and assigned to its correct species, with no false positives, call overlap, temporal dependence, switching cost or minimum segment length. Recording sets can be arbitrary measurable subsets of \([0,H]\). The clock origin is arbitrary; two opposite exponential profiles are idealized rather than inferred from a wildlife data set. The objective is **joint confirmation**, not expected number of total calls, expected richness, parameter-estimation precision, or a survey with uncertain species presence.

## Proof

**1. Exact objective and strict concavity within the edge family.** Poisson zero-count probabilities give, for every recording set,
\[
P(E)=(1-e^{-\int_E\lambda_1})(1-e^{-\int_E\lambda_2}).
\]
Integrating the two exponentials over \(E_x\) yields \(U(x)\) and \(V(x)\) above. Put \(c=1-e^{-\kappa(H-B)}>0\). Direct differentiation gives
\[
U'=ac e^{-\kappa x}>0,\qquad V'=-bc e^{-\kappa(B-x)}<0,
\]
\[
U''=-\kappa U'<0,\qquad V''=\kappa V'<0.
\]
For \(z>0\), \(f(z)=\log(1-e^{-z})\) is strictly increasing and strictly concave: \(f'(z)=(e^z-1)^{-1}>0\), \(f''(z)=-e^z/(e^z-1)^2<0\). Thus \(G(x)=\log P(E_x)=f(U(x))+f(V(x))\) is strictly concave on \([0,B]\). It has exactly one global maximizer and
\[
G'(x)=c\left(\frac{a e^{-\kappa x}}{e^{U(x)}-1}
-\frac{b e^{-\kappa(B-x)}}{e^{V(x)}-1}\right).
\]

**2. Why no irregular or interior schedule can beat an edge schedule.** Let \(x_*\) be the maximizer in Step 1; write \(U_*=U(x_*)\), \(V_*=V(x_*)\), and define the positive, strictly convex switching weight
\[
w(t)=\frac{a e^{-\kappa t}}{e^{U_*}-1}+
\frac{b e^{-\kappa(H-t)}}{e^{V_*}-1},
\qquad w''(t)=\kappa^2 w(t)>0.
\]
For \(0<x_*<B\), the first-order condition is exactly \(w(x_*)=w(H-B+x_*)\). Strict convexity shows that these two equal boundary values are lower than all values of \(w\) in the two outer recording intervals and higher than all values in the omitted middle interval. At \(x_*=0\), the endpoint condition \(G'(0)\le0\) is \(w(0)\le w(H-B)\); strict convexity again makes \([H-B,H]\) the top-\(B\)-measure set of \(w\). At \(x_*=B\), the condition \(G'(B)\ge0\) is \(w(B)\ge w(H)\), making \([0,B]\) the top-\(B\)-measure set. In every case, among all measurable sets of measure \(B\), \(E_{x_*}\) uniquely maximizes \(\int_E w(t)\,dt\) modulo null sets; equality at a boundary level holds on at most two points.

For any competing \(E\), concavity of \(f\) gives the supporting-line bound
\[
\log P(E)-\log P(E_{x_*})
\le\frac{\int_E\lambda_1-U_*}{e^{U_*}-1}
+\frac{\int_E\lambda_2-V_*}{e^{V_*}-1}
=\int_E w-\int_{E_{x_*}}w\le0.
\]
The last inequality is strict unless \(E\) equals \(E_{x_*}\) almost everywhere. Hence the candidate is the unique global optimizer over arbitrary measurable sets, not merely among two-window schedules. This supporting-hyperplane argument is a constructive proof of the necessary global reduction, with no finite-grid or simulation assumption.

**3. Sharp one-sided transition equations.** Put \(h=(1-e^{-\kappa B})/\kappa\) and \(s=e^{-\kappa(H-B)}h\). Evaluating the derivative at the boundaries yields
\[
\frac{G'(0)}c=\phi_s(a)-e^{-\kappa B}\phi_h(b),\qquad
\frac{G'(B)}c=e^{-\kappa B}\phi_h(a)-\phi_s(b).
\]
For every fixed \(z>0\), \(\phi_z\) is continuous and strictly decreasing in its positive argument from \(1/z\) to \(0\); differentiation reduces strict negativity to \(e^v(1-v)-1<0\) for \(v>0\). Moreover \(\phi_s(0+)=1/s=e^{\kappa(H-B)}/h>e^{-\kappa B}/h>e^{-\kappa B}\phi_h(v)\), so each critical equation has exactly one positive root \(A_c(v)\). Strict concavity then gives \(G'(0)\le0\) exactly in the terminal-only regime, \(G'(B)\ge0\) exactly in the initial-only regime, and otherwise a unique interior root of \(G'\). These regimes cannot overlap because \(G'\) strictly decreases.

**4. Symmetry and small-budget limit.** If \(a=b\), reflection \(x\mapsto B-x\) exchanges \(U\) and \(V\); strict concavity forces \(x_*=B/2\). For fixed positive \(a,b,\kappa,H\), take \(x=By\), \(0\le y\le1\), and \(r=e^{-\kappa H}\in(0,1)\). Uniformly in \(y\), as \(B\downarrow0\),
\[
U(By)=aB[r+(1-r)y]+O(B^2),\quad
V(By)=bB[1-(1-r)y]+O(B^2),
\]
so
\[
\frac{P(E_{By})}{abB^2}
\longrightarrow[r+(1-r)y][1-(1-r)y]
\]
uniformly. This limiting quadratic is strictly concave and has its unique maximum at \(y=1/2\). Uniform convergence and uniqueness imply \(x_*/B\to1/2\).

## Verification

The included standalone `check.py` can be run with Python 3, NumPy and SciPy. It tests the analytic edge-window optimum over 350 randomized parameter cases, evaluates the intensity integrals independently by midpoint quadrature, exhaustively compares all \(\binom{14}{5}\) five-cell sets for four finite discretizations, checks the two one-sided and symmetric regimes, and checks the small-budget limit. All 11,846 diagnostics passed in the reviewed execution. These are **finite checks only**; the proof in the preceding section establishes the continuous, all-parameter assertion.

For \(H=2\), \(B=1\), \(\kappa=1\) and \(b=1\), the boundary amplitude is \(A_c(1)=15.717171299688\ldots\). At \(a=20\), the unique optimal recording set is the final unit interval, with joint-confirmation probability \(0.464060390886\ldots\). With \(a=b=1\), the unique optimum records one half-unit at each end, with probability \(0.145922770364\ldots\).

## Relationship to prior work

Skalak, Sherwin and Brigham (2012) measured how night-of-sampling and effort change acoustically recorded bat species richness, documenting distinct early and late detections. Stahlschmidt and Brühl (2012) considered standardization and temporal/spatial bat-activity sampling. Petitot and colleagues (2014) optimized amphibian occupancy survey dates and modality using empirical detection probabilities. Balantic and Donovan (2019) developed a discrete, adaptive multi-species acoustic recording algorithm using externally weighted hourly vocalization probabilities. These support the need for effort allocation but do not, in their inspected full-text methods and results, prove the global edge-window shape, unique continuous split, and sharp one-sided thresholds for the **product** of two independent Poisson species' at-least-one-call probabilities.

The proof uses familiar supporting-hyperplane and strictly convex threshold-set principles; the mathematical method itself is not claimed as new. The contribution is the complete nontrivial three-regime classification for this explicit joint-species detection objective and its sharp one-sided and small-budget laws. Historical priority is provisional: nonindexed scheduling literature, more general extremal-set results, or alternate formulations may cover aspects of this statement.

## Limitations

No measurement confirms that any particular species follows the assumed opposite exponential call profiles. Rates are treated as known and constant across nights; independent Poisson calling, perfect classification, continuous switchability, zero storage cost and absence of weather/observer variation may fail in practice. The theorem does not optimize expected species count for larger communities, uncertainty in species occupancy, robust design under rate miscalibration, finite switching overhead or required contiguous minimum recording blocks. A general convex-threshold-set argument underlies the proof, so novelty is a priority claim only relative to inspected sources; independent review is outstanding.

## References

- S. L. Skalak, R. E. Sherwin and R. M. Brigham (2012), *Sampling period, size and duration influence measures of bat species richness from acoustic surveys*, *Methods in Ecology and Evolution* 3, 490–502. First online 2012-01-04. https://doi.org/10.1111/j.2041-210X.2011.00177.x
- P. Stahlschmidt and C. A. Brühl (2012), *Bats as bioindicators – the need of a standardized method for acoustic bat activity surveys*, *Methods in Ecology and Evolution* 3, 503–508. First online 2012-02-17. https://doi.org/10.1111/j.2041-210X.2012.00188.x
- M. Petitot, N. Manceau, P. Geniez and A. Besnard (2014), *Optimizing occupancy surveys by maximizing detection probability: application to amphibian monitoring in the Mediterranean region*, *Ecology and Evolution* 4, 3538–3549. https://doi.org/10.1002/ece3.1207
- C. Balantic and T. Donovan (2019), *Temporally adaptive acoustic sampling to maximize detection across a suite of focal wildlife species*, *Ecology and Evolution* 9, 10582–10600. https://doi.org/10.1002/ece3.5579
