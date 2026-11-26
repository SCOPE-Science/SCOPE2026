# A sharp cross-camp leadership threshold and universal algebraic relaxation

## Finding

Consider the anchored replicator opinion–leadership model of Alutto, Zino, Johansson and Fontan (2026). For every finite nonnegative row-stochastic influence matrix whose two nonempty opinion camps have the same positive cross-camp exposure \(q\), equally strong opposed initial opinions and a common interior initial leadership yield an exact two-dimensional invariant manifold. The critical conviction ratio on this manifold is exactly \(\rho_c=4q^2\): above it every agent becomes a full leader and retains their initial polar opinion; below it all leadership and opinion amplitudes converge to zero, with universal \(t^{-1/2}\) asymptotics; at equality leadership remains fixed and the opinion converges exponentially to a nonzero partial-polarization equilibrium. This is a global-in-time result **within the specified invariant initial-condition class**, not a full-state-space attractor claim.

Precisely, write \(\kappa=2q\). For common initial leadership \(u\in(0,1)\) and common initial opinion magnitude \(a\in(0,1]\), let \(s(t)>0\) be the signed camp opinion amplitude and \(z(t)\in(0,1)\) the common leadership. Then:

* If \(\rho>\kappa^2\), \((s(t),z(t))\to(a,1)\), and \(\lim_{t\to\infty}t^{-1}\log(1-z(t))=-(\rho-\kappa^2)a^2\).
* If \(\rho=\kappa^2\), put \(c=\kappa(1-u)+u\). Then \(z(t)=u\) and \(s(t)=au/c+(a-au/c)e^{-ct}\).
* If \(0<\rho<\kappa^2\), put \(\delta=\kappa^2-\rho\). Then \((s(t),z(t))\to(0,0)\), and
  \[\lim_{t\to\infty}\sqrt{t}\,s(t)=\frac{1}{\sqrt{2\delta}},\qquad \lim_{t\to\infty}\sqrt{t}\,z(t)=\frac{\kappa}{a\sqrt{2\delta}}.\]

The equal-cross-exposure condition is also necessary for this spatially homogeneous, signed-camp and uniform-leadership ansatz to remain invariant for every admissible common interior initial leadership.

## Assumptions and scope

Let \(n\ge2\) and let \(W=(W_{ij})\) be an arbitrary nonnegative row-stochastic matrix, not necessarily symmetric or irreducible. Fix a sign vector \(\sigma\in\{-1,1\}^n\) containing both signs and define the exposure of agent \(i\) to the opposite camp as \(q_i=\sum_{j:\sigma_j\ne\sigma_i}W_{ij}\). Assume \(q_i=q\in(0,1]\) for every \(i\), and let \(\kappa=2q\in(0,2]\). Thus \(W\sigma=(1-2q)\sigma\).

Fix parameters \(a\in(0,1]\), \(u\in(0,1)\), and common \(\rho>0\). Initial opinions are \(x_i(0)=a\sigma_i\), while initial leadership is \(y_i(0)=u\). All agents follow the exact continuous-time model from the cited motivating paper:

\[\dot x_i=-(1-y_i)\bigl(x_i-\sum_jW_{ij}x_j\bigr)-y_i(x_i-x_i(0)),\]
\[\dot y_i=y_i(1-y_i)\left[\rho x_i^2-\bigl(x_i-\sum_jW_{ij}x_j\bigr)^2\right].\]

Time uses the unit coefficients of these equations. No scaling by population size, imitation clock, or other speed coefficient is introduced. All limits are for \(t\to\infty\) with \(n,W,a,u,\rho\) fixed.

## Proof

**1. Exact invariant geometry and necessity.** Since \(W\sigma=(1-\kappa)\sigma\), substitute \(x_i=s\sigma_i\), \(y_i=z\) into the full vector field. Each social disagreement becomes \(x_i-\sum_jW_{ij}x_j=\kappa s\sigma_i\). All opinion derivatives are a common scalar times \(\sigma_i\), and all leadership derivatives are the same. Uniqueness for polynomial ODEs proves preservation of the ansatz and gives

\[\dot s=-c(z)s+az,\quad \dot z=(\rho-\kappa^2)s^2z(1-z),\quad c(z)=\kappa(1-z)+z.\tag{1}\]

Conversely, without equal exposures, the full initial vector field satisfies \(\dot x_i(0)/\sigma_i=-2aq_i(1-u)\). Because \(a>0\) and \(u<1\), this derivative cannot be common across camps when the \(q_i\) differ; thus the proposed common-amplitude ansatz cannot be invariant. This proves the stated necessity, without claiming other possible lower-dimensional invariant sets do not exist.

**2. Bounds and nonvanishing at finite time.** The rectangle \([0,a]\times[0,1]\) is invariant for (1). At \(s=0\) the opinion derivative equals \(az\ge0\), and at \(s=a\) it equals \(-\kappa(1-z)a\le0\); at \(z=0,1\) the leadership derivative vanishes. For positive initial \((a,u)\), uniqueness and variation of constants give \(s(t)>0\), while the logistic logarithm implies \(0<z(t)<1\) for finite \(t\). Also \(c(z)\ge\min\{\kappa,1\}>0\). These bounds ensure global existence.

**3. Above threshold.** If \(\Delta=\rho-\kappa^2>0\), then \(z\) is strictly increasing and \(z(t)\ge u\). Since \(c(z)\le C:=\max\{\kappa,1\}\), equation (1) gives \(\dot s\ge-Cs+au\). Hence \(\liminf s(t)\ge au/C>0\). Consequently \(\frac{d}{dt}\log\frac{z}{1-z}=\Delta s^2\) is eventually bounded below by a positive constant, so \(z(t)\to1\). The stable linear equation \(\dot s=-c(z)s+az\), whose coefficients converge to \(-1\) and \(a\), yields \(s(t)\to a\). Finally, \(\frac{d}{dt}\log(1-z)=-\Delta s^2 z\to-\Delta a^2\). Its Cesàro average proves the claimed logarithmic convergence rate.

**4. At threshold.** If \(\rho=\kappa^2\), the second equation vanishes identically, so \(z(t)=u\); the first is a constant-coefficient affine scalar ODE and integrates to the displayed exact solution. The limiting polarization is \(au/[\kappa(1-u)+u]\), strictly between zero and \(a\).

**5. Below threshold and the exact power law.** If \(\delta=\kappa^2-\rho>0\), then \(z\) decreases to some \(\ell\ge0\). If \(\ell>0\), the first equation, with convergent coefficients, forces \(s\to a\ell/c(\ell)>0\); therefore \(\frac{d}{dt}\log(z/(1-z))=-\delta s^2\) is bounded above by a negative constant at large times, contradicting \(\ell>0\). Hence \(z\to0\), and the same stable linear equation implies \(s\to0\).

For all finite \(t\), set \(r(t)=s(t)/z(t)>0\). Differentiate (1):

\[\dot r=\bigl[-c(z)+\delta s^2(1-z)\bigr]r+a.\tag{2}\]

The coefficient tends to \(-\kappa<0\). A scalar comparison for sufficiently large times bounds \(r\), and variation of constants in (2) yields \(r(t)\to a/\kappa\). Thus

\[\frac{d}{dt}z^{-2}=2\delta\,r^2(1-z)\longrightarrow\frac{2\delta a^2}{\kappa^2}.\tag{3}\]

Integrating (3) and dividing by \(t\) shows \(z(t)^{-2}/t\to 2\delta a^2/\kappa^2\). Taking positive square roots proves the leadership asymptotic; multiplying by \(s/z\to a/\kappa\) proves the opinion asymptotic. None of these steps infers infinite-time behavior from finite simulation.

## Verification

The independent file `verify.py` uses only the Python standard library. Execute `python verify.py` from the directory containing this report and the script. It compares the **full** four-agent vector field with (1) at 108 exact-rational combinations, checks noninvariance when cross-camp exposures differ, compares a critical trajectory against the exact closed form, and tests two distinct subcritical asymptotic amplitudes and the supercritical limit with fourth-order numerical integration. The exact algebra and infinite-time conclusions are established in the proof, not by the numerical tests.

For a transparent special case, take two camps with cross-exposure \(q=1/2\), so \(\kappa=1\), and take \(a=1\), \(u=1/2\). At \(\rho=1/2\), the theorem predicts \(s(t)\sim t^{-1/2}\) and \(z(t)\sim t^{-1/2}\); at \(\rho=1\), it gives \(s(t)=(1+e^{-t})/2\), \(z(t)=1/2\); at \(\rho=2\), both coordinates tend to one. These illustrate all three phases without supplying the general proof.

## Relationship to prior work

Alutto, Zino, Johansson and Fontan (2026), arXiv:2606.05825, introduce exactly the coupled replicator model used here (their equation (4)), give a general equilibrium partition (Lemma 3), and prove agentwise sufficient leader and follower conditions (Theorems 1–2), including restrictions for leader emergence involving \(\rho_i>1\) and sufficiently large initial leadership. Their paper explicitly notes these conditions need not be necessary (Remark 5). Those results do not assert the necessary-and-sufficient cross-camp threshold \(\rho=4q^2\), an exhaustive global trajectory classification on the invariant manifold, or the universal \(t^{-1/2}\) amplitudes. The proof here does not claim the general leadership model or its basic equilibrium characterization as new.

The earlier paper by the same authors, arXiv:2603.24381, studies a different leadership equation with separate birth and loss terms; its time-scale-separated analysis is not a theorem for this replicator equation. Standard Friedkin–Johnsen dynamics are recovered when leadership is constant, and so account for the elementary critical scalar solution but not the two noncritical leadership regimes. Equitable partitions and invariant network modes are established background, used rather than newly introduced here.

## Limitations

The theorem concerns exactly equal **initial leadership**, equal signed magnitudes of initially opposed opinions, common conviction parameter, and equal cross-camp weight exposure. It does not prove transverse stability in the full \(2n\)-dimensional system; in particular, the reduced-system attraction to \(z=0\) need not imply attraction from generic nonsymmetric initial conditions. The result does not extend automatically to negative influence weights, heterogeneous behavioral parameters, time-dependent networks, additive noise, or the different quadratic birth–loss leadership model. Mathematical priority outside the inspected references may warrant further independent review.

## References

1. Martina Alutto, Lorenzo Zino, Karl H. Johansson and Angela Fontan, *On Leadership Emergence in Opinion Dynamics on Social Networks*, arXiv:2606.05825v1 (first public 2026-06-04), https://arxiv.org/abs/2606.05825 . Author-shared full text: https://www.researchgate.net/publication/406039711_On_Leadership_Emergence_in_Opinion_Dynamics_on_Social_Networks .
2. Martina Alutto, Lorenzo Zino, Karl H. Johansson and Angela Fontan, *On a Co-evolving Opinion-Leadership Model in Social Networks*, arXiv:2603.24381 (first public 2026-03-25), https://arxiv.org/abs/2603.24381 . This earlier model has a different leadership law.
3. N. E. Friedkin and E. C. Johnsen, *Social Influence and Opinions*, The Journal of Mathematical Sociology (1990), foundational anchored opinion dynamics.
