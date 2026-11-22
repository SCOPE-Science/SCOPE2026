# Sharp memory overshoot from thresholded rainfall routing into a linear store

## Finding

For the mass-conserving stationary annual rainfall–runoff model below, an infiltration threshold produces a **unique global maximizer** of streamflow's lag-one correlation and a second, earlier, sharp threshold after which streamflow's lag-one correlation **exceeds the storage's**. This can happen even though rainfall is independent between years.

For every retention \(a\in(0,1)\), the streamflow lag-one autocorrelation \(\rho_a(h)\) as a function of normalized infiltration cap \(h>0\) increases strictly to one global maximum at the unique positive \(h_*(a)\) solving
\[
(1-a)h_*(a)=2(1-e^{-h_*(a)}),
\]
and then decreases strictly to \(a\) from above. In particular, the storage lag-one autocorrelation is exactly \(a\), while
\[
\rho_a(h)>a \quad\Longleftrightarrow\quad h>h_c(a),
\]
where \(h_c(a)\) is the unique positive solution of
\[
(1-a)h_c(a)+e^{-h_c(a)}=1+a.
\]
Always \(0<h_c(a)<h_*(a)\). At every positive integer lag \(k\), streamflow correlation is \(a^{k-1}\rho_a(h)\); thus the same optimal threshold maximizes all positive-lag streamflow correlations.

## Assumptions and scope

Let \((P_t)_{t\in\mathbb Z}\) be independent unit-mean exponential random variables, with observations indexed by discrete annual periods. Fix a positive threshold \(h\), measured in units of mean annual effective precipitation. The annual precipitation splits into quickflow \(F_t=(P_t-h)_+\) and slow recharge \(R_t=\min\{P_t,h\}\), so \(F_t+R_t=P_t\). A deep storage with known annual retention \(a\in(0,1)\) obeys
\[
S_{t+1}=aS_t+R_t,\qquad Q_t=F_t+(1-a)S_t.
\]
The stationary solution is \(S_t=\sum_{j\ge1}a^{j-1}R_{t-j}\), which converges absolutely and in second moment. The balance \(P_t+S_t=Q_t+S_{t+1}\) holds exactly. The infiltration threshold resets independently each year; the long-lived state is \(S_t\), not the annual threshold. Neither observed streamflow nor the two pathways are asserted to equal a physically calibrated watershed.

## Proof

**1. Input moments.** Put \(z=e^{-h}\). Direct integration against the exponential density yields
\[
\operatorname{Var}F=U=2z-z^2,\quad
\operatorname{Var}R=V=1-2hz-z^2,\quad
\operatorname{Cov}(F,R)=W=(h-1)z+z^2.
\]
For example, \(\mathbb EF=z\), \(\mathbb EF^2=2z\), \(\mathbb ER=1-z\), and \(\mathbb E(PF)=(h+2)z\), which give all three identities. Both \(U,V\) are strictly positive at finite \(h>0\), and \(W>0\) because \(h-1+e^{-h}>0\).

**2. Storage and streamflow covariance.** As \(S_t\) is independent of contemporaneous \((F_t,R_t)\), the stationary storage variance is \(V/(1-a^2)\). Consequently
\[
D_a(h):=\operatorname{Var}Q_t=U+\frac{1-a}{1+a}V>0,
\]
\[
N_a(h):=\operatorname{Cov}(Q_t,Q_{t+1})=(1-a)W+\frac{a(1-a)}{1+a}V,
\]
and \(\rho_a(h)=N_a(h)/D_a(h)\). The storage's unit-lag correlation is \(a\). For \(k\ge1\), only the same stationary state and the current recharge can carry covariance forward, yielding \(\operatorname{Cov}(Q_t,Q_{t+k})=a^{k-1}N_a(h)\).

**3. Exact comparison with slow-storage persistence.** Cancelling the shared storage term gives
\[
\rho_a(h)-a=
\frac{z\big((1-a)h-(1+a)+z\big)}{D_a(h)}.
\]
The numerator's sign is the sign of \(G_a(h)=(1-a)h+e^{-h}-(1+a)\). This strictly convex function starts at \(-a\), initially decreases, and tends to positive infinity; its derivative \(1-a-e^{-h}\) increases through zero once. It therefore has exactly one positive zero \(h_c(a)\), is negative below it and positive above it.

**4. Strict unimodality.** Differentiate \(N_a/D_a\), retaining \(z'=-z\). Exact algebra gives
\[
\rho_a'(h)=\frac{(1-a)e^{-h}}{(1+a)D_a(h)^2}
\left[2(1-e^{-h})-(1-a)h\right].
\]
The bracket \(H_a(h)\) is strictly concave, zero at \(h=0\), has positive initial derivative \(1+a\), and tends to negative infinity. Thus it has a unique positive zero \(h_*(a)\); the correlation increases strictly before and decreases strictly after it. Also \(G_a'(h_c)>0\), hence \(e^{-h_c}<1-a\). Using the defining equation for \(h_c\),
\[
H_a(h_c)=1-a-e^{-h_c}>0,
\]
so \(h_c<h_*\). Finally, as \(h\downarrow0\), \(F_t\to P_t\), \(R_t\to0\) in \(L^2\), and \(\rho_a(h)\to0\). As \(h\to\infty\), \(F_t\to0\), \(R_t\to P_t\), and \(\rho_a(h)\to a\). Thus the maximum is attained and is strictly greater than \(a\).

## Verification

The companion `verify.py` runs exact rational-algebra identities for the numerator of the derivative, numerical finite-difference checks for the complete correlation formula, and independently bisects both defining equations across a collection of retention values. It also tests the claimed ordering and endpoint limits. These tests supplement rather than replace the mathematical proof. For \(a=1/2\), the roots are approximately \(h_c=2.88870335619319\) and \(h_*=3.92069039487289\), with \(\rho_a(h_*)\approx0.52969248239643\) compared with storage memory \(a=0.5\).

## Relationship to prior work

The motivating 2024 preprint by Berghuijs and colleagues documents annual catchment memory despite nearly uncorrelated annual rainfall, using empirical data and nonlinear/hysteretic storage simulations; its final 2025 paper provides a full accessible formulation. Schuite and colleagues (2019) develop spectral transfer-function analysis to constrain catchment properties, and Weiler and colleagues (2003) use nonlinear rainfall partitioning and parallel-reservoir transfer models for tracer-based hydrograph separation. Those contributions support the model's motivation but do not, in the inspected sections, give the present exponential-rainfall threshold formula, its unique optimizer or the strict runoff-over-storage memory window. Classical covariance and linear-system identities are background mathematics, not claimed to be new.

## Limitations

This is an exact theorem for an idealized single-storage discrete-time model with independent exponential rainfall, a fixed annual cap and an unobserved deep store. It is not a claim about all precipitation distributions, nonlinear groundwater dynamics, observational estimation error or physical streamflow data. Positive runoff-over-storage memory need not be prevalent in real catchments; the motivating field study usually reports the reverse ranking. The classification is for population autocorrelations, not finite-sample estimates. Historical priority remains subject to independent expert review, particularly among older nonlinear quickflow/baseflow and hydrological spectral-memory analyses.

## References

1. W. R. Berghuijs et al., *Annual memory in the terrestrial water cycle*, EGUsphere preprint, first public 25 September 2024, https://doi.org/10.5194/egusphere-2024-2954; final publication, *Hydrology and Earth System Sciences* 29, 1319–1333 (2025), https://doi.org/10.5194/hess-29-1319-2025.
2. J. Schuite et al., *Improving the Spectral Analysis of Hydrological Signals to Efficiently Constrain Watershed Properties*, *Water Resources Research* 55 (2019), https://doi.org/10.1029/2018WR024579.
3. M. Weiler et al., *How does rainfall become runoff? A combined tracer and runoff transfer function approach*, *Water Resources Research* 39 (2003), https://doi.org/10.1029/2003WR002331.
4. J. Ramos, D. Mallants and J. Feyen, *State Space Identification of Linear Deterministic Rainfall-Runoff Models*, *Water Resources Research* 31 (1995), https://doi.org/10.1029/95WR00234.
