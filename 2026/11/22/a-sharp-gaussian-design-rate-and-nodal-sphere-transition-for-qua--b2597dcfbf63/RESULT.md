# A sharp Gaussian-design rate and nodal-sphere transition for quartic-trap resetting

## Finding
Consider an isotropic overdamped particle confined by a quadratic-plus-quartic potential and independently returned, at Poisson times, to fresh positions drawn from a freely chosen probability law. Fixing a prescribed Gaussian stationary position law determines **both** a unique resetting distribution and a sharp minimum admissible reset rate. At the minimum, the resetting density exhibits a dimension-controlled transition between a positive-radius nodal sphere, a fourth-order zero at the origin, and a quadratic zero at the origin. In high dimension, the minimum rate grows **quadratically** in dimension.

Precisely, for an integer \(d\geq1\), \(a\geq0\), \(c,D,s>0\), define the dimensionless offset and radial coordinate
\[
\theta=\frac{a-D/s}{cs},\qquad y=\frac{\lVert x\rVert^2}{s},
\]
and
\[
G_d(y)=d\theta+(d+2-\theta)y-y^2.
\]
For the target \(p(x)=(2\pi s)^{-d/2}\exp(-\lVert x\rVert^2/(2s))\), an independently refreshed resetting law realizing this *exact* stationary density exists **if and only if**
\[
\boxed{\quad r\geq r_{\min}=cs\left[d\theta+\frac{(d+2-\theta)_+^2}{4}\right]>0,\quad (z)_+=\max(z,0).\quad}
\]
The law is unique and has density
\[
\boxed{\quad q_r(x)=p(x)\left[1-\frac{cs}{r}G_d\!\left(\frac{\lVert x\rVert^2}{s}\right)\right].\quad}
\]
For every finite admissible rate, the resetting distribution is genuinely non-Gaussian even though the stationary one-time position distribution is Gaussian. Notably, **every target variance \(s>0\) is feasible at a sufficiently high finite reset rate**, including \(a=0\) (pure quartic confinement) and \(a<D/s\); in the purely harmonic model with the same drift coefficient \(a\), the latter variance regime is unattainable by any independent full-position reset law. A transparent example is pure quartic confinement in three dimensions: for \(d=3\), \(a=0\), \(c=D=s=1\), the exact threshold is \(r_{\min}=6\) and
\[
q_6(x)=\frac{1}{6}(2\pi)^{-3/2}e^{-\lVert x\rVert^2/2}(\lVert x\rVert^2-3)^2.
\]


**The three exact boundary geometries.** At \(r=r_{\min}\), write \(y_0=(d+2-\theta)/2\). Then:

- If \(\theta<d+2\), the unique zero set of \(q_r\) is the sphere \(\lVert x\rVert^2=sy_0>0\), and \(q_r/p=(cs/r_{\min})(y-y_0)^2\).
- If \(\theta=d+2\), the zero set is the origin, with \(q_r/p=(cs/r_{\min})y^2\), a zero of order four in \(\lVert x\rVert\).
- If \(\theta>d+2\), the zero set is the origin, with \(q_r/p=(cs/r_{\min})y(y+\theta-d-2)\), a zero of order two in \(\lVert x\rVert\).

For every \(r>r_{\min}\), the source density is strictly positive everywhere. For \(0<r<r_{\min}\), the uniquely forced source is strictly negative on a nonempty open set and so is not a probability law.

In particular, holding \(a,c,D,s\) fixed and allowing dimension to grow, once \(d>\theta-2\),
\[
\boxed{\quad r_{\min}=\frac{cs}{4}\left[(d+\theta-2)^2+8d\right]\sim\frac{cs}{4}d^2.\quad}
\]
For \(d\leq\theta-2\), the threshold instead equals \(cs\,d\theta\). Hence increasing dimension can change *where* the extremal reset density vanishes, as well as changing the minimum intervention frequency.

## Assumptions and scope
Between reset events, \(X_t\in\mathbb R^d\) obeys the Itô diffusion
\[
dX_t=-(a+c\lVert X_t\rVert^2)X_t\,dt+\sqrt{2D}\,dW_t.
\]
The drift is the negative gradient of \(U(x)=a\lVert x\rVert^2/2+c\lVert x\rVert^4/4\). At the independent Poisson times of constant rate \(r>0\), the **entire** position vector is replaced by an independent sample from a fixed Borel probability measure \(\mu\), which need not be initially assumed to have a density. There is no position dependence in the reset hazard and no memory between reset draws. The assertion concerns the exact *stationary one-time* density \(p=N(0,sI_d)\), not Gaussianity of the whole stochastic process. The target is centered and isotropic; no claim is made for arbitrary shifted or anisotropic Gaussian targets, or nonquartic potentials.

## Proof
**1. The reset source is distributionally forced.** The unreset generator and forward adjoint are
\[
Lf=-(a+c\lVert x\rVert^2)x\cdot\nabla f+D\Delta f,
\quad
L^*p=\nabla\cdot((a+c\lVert x\rVert^2)x p)+D\Delta p.
\]
Stationarity with independent complete-state resets gives the distributional equation
\[
0=L^*p-rp+r\mu,\qquad\text{so}\qquad \mu=p-r^{-1}L^*p.
\]
Therefore the desired source is unique even among arbitrary probability *measures*: the right-hand side is absolutely continuous for the smooth target \(p\).

**2. The forced density is a quartic radial Gaussian tilt.** Set \(R^2=\lVert x\rVert^2\) and use
\[
\nabla p=-xp/s,\qquad \Delta p=\left(R^2/s^2-d/s\right)p.
\]
Direct differentiation, with every factor retained, yields
\[
\frac{L^*p}{p}
=d(a-D/s)+\bigl[c(d+2)-(a-D/s)/s\bigr]R^2-\frac{c}{s}R^4
=cs\,G_d(R^2/s).
\]
The displayed \(q_r\) follows. The quartic confinement implies Gaussian decay of the adjoint flux, so \(\int L^*p\,dx=0\), and consequently \(\int q_r\,dx=1\) for *all* rates, whether or not \(q_r\) is nonnegative.

**3. A global positivity criterion, including boundaries.** Because \(p>0\), \(q_r\geq0\) exactly when \(r\geq cs\sup_{y\geq0}G_d(y)\). The quadratic \(G_d\) is strictly concave, and its unique maximizing radial coordinate is
\[
y_{\max}=\frac{(d+2-\theta)_+}{2}.
\]
Its maximum is \(d\theta+(d+2-\theta)_+^2/4\), giving the asserted sharp criterion. This maximum is always positive: for \(\theta<d+2\), it equals \(\bigl[(d+\theta-2)^2+8d\bigr]/4>0\); for \(\theta\geq d+2\), it equals \(d\theta>0\). At the threshold, completing the square when \(y_{\max}>0\), or factoring out \(y\) when \(y_{\max}=0\), gives exactly the three specified zero sets and orders. A radial zero represents a sphere for \(d\geq2\) and two points for \(d=1\). For a higher rate, the tilt is strictly positive everywhere; for a lower positive rate, its value at a maximizer is negative and remains negative in a nonempty open neighborhood (including near the origin when the maximizer is at the boundary), so no valid \(\mu\) is possible.

**4. Sufficiency and uniqueness of the stationary law.** The drift is locally Lipschitz and dissipative, since \(x\cdot[-(a+c\lVert x\rVert^2)x]\leq-c\lVert x\rVert^4\), ensuring nonexplosion and a Feller Markov semigroup \(P_t\). Once Step 3 gives a probability density \(q_r\), the last-reset resolvent
\[
\pi=r\int_0^\infty e^{-rt}\,(q_rP_t)\,dt
\]
exists and is stationary. The target \(p\) satisfies its weak stationarity equation and hence equals this invariant distribution. Alternatively, two copies using the same reset event times and reset draws coalesce after their first common reset; therefore their total-variation distance is at most the probability \(e^{-rt}\) of no reset and the invariant law is unique.

**5. Non-Gaussianity and dimension dependence.** For every finite \(r\), the factor \(q_r/p\) is a polynomial in \(\lVert x\rVert^2\) of degree two with nonzero quartic coefficient \(cs/r\). A quotient of two nondegenerate Gaussian densities is an exponential of a quadratic, which cannot equal this nonconstant polynomial on \(\mathbb R^d\). Thus the source is genuinely non-Gaussian. The piecewise exact rate formulas and their dimension-asymptotic form follow by expanding the completed-square expression. For comparison, suppressing quartic confinement produces the harmonic source ratio \(1-[d(a-D/s)-(a-D/s)\lVert x
Vert^2/s]/r\): when \(a<D/s\), its linear radial term is negative without bound, so no finite rate yields a valid source; this contrasts with the proven positive quartic radial term here. No approximation is used in the threshold or the nodal classification.

## Verification
The standalone `verify_quartic_reset.py` reconstructs the full drift generator and Gaussian moments by exact rational symbolic arithmetic, then verifies \(\int q_r=1\), the factorized node formulas, and the stationary weak identity \(\int Lf\,p+r(\int f q_r-\int fp)=0\) for every monomial of degree at most six in seven diverse parameter sets, with dimensions \(1,2,3,4\) and all three nodal regimes. It also tests strict negativity of the required source at half the sharp threshold. The script reports **413 passed exact rational checks**. These are finite cross-checks, while the unrestricted-dimensional theorem is proved by Steps 1–5.

To reproduce: install Python 3 and SymPy; execute `python3 verify_quartic_reset.py` in the directory containing this document and the script. The checks require neither simulation nor external data.

## Relationship to prior work
Mori, Olsen and Krishnamurthy (2022) study entropy and Fokker–Planck structure for resetting in general potentials and provide the distributed-reset forward-equation antecedent. Olsen (2023) develops exact moment formulas for resetting to a distribution, prominently in a harmonic Ornstein–Uhlenbeck setting. Goerlich, Keidar and Roichman (2024) study resetting-based swift equilibration in an anharmonic (not quartic Gaussian inverse-design) setting. Existing inverse Gaussian stationary-design results for a *linear* multivariate Ornstein–Uhlenbeck drift already supply a sharp quadratic-source positivity criterion. Their assumptions exclude the present quartic drift, and the linear theorem's source polynomial has lower degree and different dimensional scaling.

The basic adjoint identity \(\mu=p-r^{-1}L^*p\) and the act of maximizing a concave quadratic are standard and not claimed as discoveries. The specific assessed contribution is the **complete sharp Gaussian-target feasibility phase diagram for the natural quartic-trap diffusion**, including its exact source, critical radial node geometry, and asymptotic quadratic intervention-rate growth. Broad general inverse-generator arguments may imply special instances, and checking published literature cannot establish absolute priority.

## Limitations
The reset operation replaces the entire vector independently at a constant Poisson rate. The source law requires exact preparation and may be challenging to realize physically; the threshold describes mathematical feasibility rather than energy cost or an optimized control protocol. The nodal sphere is a zero of the source *density*, not a finite-width prohibited region or a positive-probability absence on a sphere (which already has zero Lebesgue measure). Finite computational checks are not an infinite-dimensional proof. There is no result here on time-dependent marginals away from stationarity, on pathwise Gaussianity, or on nonlinear trap families beyond the specified drift. Originality is a qualified self-review, not independent certification.

## References
1. F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372 (first public version November 28, 2022), https://arxiv.org/abs/2211.15372.
2. K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public version October 7, 2023), https://arxiv.org/abs/2310.04840.
3. R. Goerlich, T. D. Keidar and Y. Roichman, *Resetting as a swift equilibration protocol in an anharmonic potential*, arXiv:2401.09958 (first public version January 18, 2024), https://arxiv.org/abs/2401.09958.
4. *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets*, publicly available mathematical result on Gaussian inverse design for linear multidimensional OU drift, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-gaussian-stationary-state-engineering-by-non-gaussian-stoc--08050fc52754/RESULT.md.
5. Mathematical Subject Classification MSC2020, 82C31, stochastic methods in time-dependent statistical mechanics, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C31.
