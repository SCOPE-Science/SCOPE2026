# An exact reciprocal-time law and relaxation-rate resonance in inhibitory SIS–activity dynamics

## Finding

For a homogeneous susceptible–infected–susceptible (SIS) model coupled to a linearly relaxing activity variable and *inhibitory rational* transmission feedback, the invasion threshold has an exact integrable resonance. Write
\[
\dot x=x\left(\frac{\eta(1-x)}{1+s y}-\zeta\right),\qquad
\dot y=\kappa(kx-y).
\]
When \(\eta=\zeta\), the threshold is globally attractive for every \(x(0)\in(0,1]\), \(y(0)\ge0\), and
\[
x(t)\sim\frac{1}{\zeta(1+s k)t},\qquad
y(t)\sim\frac{k}{\zeta(1+s k)t}.
\]
If and only if the activity-relaxation rate equals the recovery rate, \(\kappa=\zeta\), the particular reciprocal observable
\[
V(t)=\frac{1+s y(t)}{x(t)}
\]
is **exactly affine for all positive states and all times**:
\[
\boxed{V(t)=V(0)+\zeta(1+s k)t.}
\]
More precisely, among reciprocal-affine observables \(U_{c,d}=(c+d y)/x\) with \(c>0\) and real \(d\), the identity \(dU_{c,d}/dt=\text{constant}\) at *every* state in the positive interior holds precisely when \(\eta=\zeta\), \(\kappa=\zeta\), and \(d=cs\). Thus this exact linearization is rigid up to a positive scalar multiple.

Away from the matched-rate resonance, at the same invasion threshold, the reciprocal prevalence has the global sharp expansion
\[
\boxed{
\frac1{x(t)}=\zeta(1+s k)t+
 s k\left(\frac{\zeta}{\kappa}-1\right)\log t+C+o(1)
\qquad(t\to\infty),
}
\]
with a finite initial-condition-dependent constant \(C\). In particular, the leading extinction coefficient is independent of activity response speed, but the logarithmic correction changes sign exactly at matching, where it vanishes for an *exact dynamical reason*.

## Assumptions and scope

All parameters \(\eta,s,k,\zeta,\kappa\) are strictly positive, \(x(0)\in(0,1]\), and \(y(0)\ge0\). The primary critical-extinction assertions assume \(\eta=\zeta\); the rigidity assertion allows arbitrary \(\eta>0\) before showing that criticality is necessary. The model is the homogeneous regular-network mean-field SIS–activity system with the activity response \(H(x)=kx\) and the monotone inhibitory feedback \(\Phi(a+y)=\Phi(a)/(1+s y)\) on its invariant physical domain. This positive rational response can be smoothly extended as a positive function outside \(y\ge0\) without changing any physical trajectory. An arbitrary \(\kappa\) is equivalent to the unit-activity-rate convention after a uniform time rescaling. Set \(M=\zeta(1+s k)\).

These are deterministic finite-dimensional mean-field statements, not probabilistic extinction-time laws for individual stochastic SIS realizations. No claims are made for inhomogeneous initial states, heterogeneous graphs, or positive equilibria away from the threshold.

## Proof

**1. Invariance and extinction.** The vector field preserves \(0<x\le1\) and \(y\ge0\): at \(x=1\) the infection derivative is \(-\zeta\); at \(y=0\) the activity derivative is \(\kappa kx\); and the scalar multiplicative infection equation preserves strict positivity at every finite time. Also \(y(t)\le B=\max\{y(0),k\}\). At \(\eta=\zeta\),
\[
\dot x=-\zeta x\frac{x+s y}{1+s y}\le -\frac{\zeta}{1+sB}x^2<0.
\]
Hence \(x\downarrow0\), and the convolution representation for \(\dot y+\kappa y=\kappa kx\) implies \(y\to0\). Let \(q=-\dot x/x=\zeta(x+s y)/(1+s y)\to0\). The ratio \(r=y/x\) satisfies
\[
\dot r=\kappa k-(\kappa-q)r.
\]
Eventually \(\kappa-q>\kappa/2\), and the variation-of-constants formula gives \(r\to k\). Therefore \(\dot x=-Mx^2+o(x^2)\), which by integration of \((1/x)'\) yields \(x(t)\sim1/(Mt)\) and \(y(t)\sim k/(Mt)\).

**2. Exact identity and rigidity.** Direct differentiation without approximation gives, for \(\eta=\zeta\),
\[
\frac{d}{dt}\frac{1+s y}{x}
=M+s(\zeta-\kappa)\left(\frac yx-k\right).
\]
Thus matched rates give the affine law exactly. For the converse consider \(U_{c,d}=(c+d y)/x\). Evaluating its derivative at \(y=0\), with arbitrary positive \(x\), gives
\[
\left.\dot U_{c,d}\right|_{y=0}
=d\kappa k+c\eta+\frac{c(\zeta-\eta)}x.
\]
Constancy in \(x\) forces \(\eta=\zeta\). Then its \(1/x\) coefficient at \(y>0\) is
\[
y\left[-d\kappa+\frac{\zeta s(c+d y)}{1+s y}\right].
\]
The bracket must vanish for every \(y>0\). Coefficient comparison in \(y\) gives \(d=cs\) and \(\kappa=\zeta\); these conditions suffice by the identity already proved.

**3. Exact solution by quadrature in the matched case.** Set \(V_0=(1+s y(0))/x(0)\). When \(\kappa=\zeta=\eta\), take \(V(t)=V_0+Mt\), and define
\[
E(t)=e^{\zeta t}\left(\frac{V(t)}{V_0}\right)^{-s k/(1+s k)}.
\]
Then the entire trajectory is reconstructed without solving an implicit nonlinear problem:
\[
y(t)=E(t)^{-1}\left[y(0)+\zeta k\int_0^t\frac{E(u)}{V(u)}\,du\right],
\qquad x(t)=\frac{1+s y(t)}{V(t)}.
\]
Indeed the first identity solves the linear equation \(\dot y+[\zeta-\zeta ks/V(t)]y=\zeta k/V(t)\), and the second enforces the exact reciprocal law. Consequently \(x(t)^{-1}=Mt+V_0-sk+O(t^{-1})\).

**4. Sharp correction off resonance.** Put \(\delta=y-kx\). It obeys
\[
\dot\delta+\kappa\delta=-k\dot x.
\]
Since \(x\sim1/(Mt)\) and \(-\dot x=O(x^2)\), splitting its exponential convolution at \(t/2\) yields \(\delta=O(x^2)\); the early half is exponentially small and the late half is uniformly \(O(t^{-2})\). Therefore \(\dot x=-Mx^2+O(x^3)\). With \(a=kM/\kappa\), the residual \(e=\delta-a x^2\) satisfies \(\dot e+\kappa e=O(x^3)\), because \(\dot x=-Mx^2+O(x^3)\); applying the same convolution estimate gives
\[
\delta=\frac{kM}{\kappa}x^2+O(x^3).
\]
Substituting into the exact derivative of \(V=(1+s y)/x\) gives
\[
\dot V=M+s(\zeta-\kappa)\frac{kM}{\kappa}x+O(x^2).
\]
As \(x\sim1/(Mt)\), first \(V=Mt+O(\log t)\), and then \(1/x=V-sk+O(x)\) implies \(x=(Mt)^{-1}+O(\log t/t^2)\). Hence
\[
\dot V=M+\frac{s k(\zeta/\kappa-1)}t
+O\left(\frac{\log t}{t^2}\right).
\]
The remainder is integrable on a tail, so \(V=Mt+sk(\zeta/\kappa-1)\log t+C_V+o(1)\), and \(1/x=V-sk+O(1/t)\) proves the claimed expansion, with \(C=C_V-sk\). All error estimates are for each fixed admissible initial state and positive parameter tuple.

## Verification

The standalone script `verify.py` verifies the differentiated identity, the rigidity algebra, the cubic expansion responsible for the logarithmic coefficient, exact non-unit rational parameter examples, and DOP853 trajectories at \(\kappa/\zeta=1/2,1,2\). Its numerical experiments merely cross-check the analytic theorem. With \(s=k=\zeta=1\), the predicted logarithmic coefficients are respectively \(1,0,-1/2\), and all three are confirmed within the prescribed numerical tolerance. For \(s=2\), \(k=3\), \(\zeta=\kappa=5\), the exact observable is \(V(t)=5/2+35t\) when \(x(0)=3/5\), \(y(0)=1/4\).

## Relationship to prior work

Alexandersen and Bassett (2026, arXiv:2608.26528v1) introduce the general SIS–activity feedback system, identify local invasion bifurcations, and analyze homogeneous polynomial feedback, endemic multiplicity, and absence of homogeneous periodic orbits. The present result uses a smooth inhibitory rational feedback within that general model and addresses **global critical-time trajectories**, an exact reciprocal integrability identity with a sharp uniqueness condition, and an explicit logarithmic finite-time correction in relation to activity speed. The source's local center-manifold calculations are related but do not themselves state the global affine observable or the rate-resonance classification. Classical SIS critical slowing and early-warning analyses cover different uncoupled or differently coupled equations; they establish neither this observable nor the threshold-specific sharp correction. Unindexed equivalent identities remain an originality risk.

## Limitations

The rational feedback and linear activity response are special, albeit physically meaningful, members of a wider model family. The result applies to homogeneous deterministic critical trajectories and makes no stochastic-network, off-critical, heterogeneous, finite-population extinction-time, or global multi-equilibrium claim. The constant \(C\) is an initial-data-dependent limit, not a closed elementary formula in general. No independent external scientific audit has been performed.

## References

1. C. G. Alexandersen and D. S. Bassett, “Hysteresis and multistability in network spreading with neuronal activity feedback,” arXiv:2608.26528v1 (first public 2026-08-27), https://arxiv.org/abs/2608.26528 .
2. S. M. O’Regan and J. M. Drake, “Theory of early warning signals of disease emergence and leading indicators of elimination,” *Theoretical Ecology* (2013), https://doi.org/10.1007/s12080-013-0185-5 .
3. C. G. Alexandersen et al., “Activity-dependent epidemic spreading on multiscale brain networks predicts Alzheimer’s disease progression,” arXiv:2608.12647 (2026), https://arxiv.org/abs/2608.12647 . Only abstract-level material was accessible for this comparison.
