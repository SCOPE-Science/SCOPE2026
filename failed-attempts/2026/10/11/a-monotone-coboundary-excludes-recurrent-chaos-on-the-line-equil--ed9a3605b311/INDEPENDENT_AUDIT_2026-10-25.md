# Independent mathematical audit

## correctness

PASS

The final theorem is correct for the displayed polynomial ODE on k1=0,k2=g,k3=0, with r>0 and g>0. Independently computed full generator L H = -g*x² +(g-k2)-k3*z +g(1+m)*k1*x*u/r; hence L H=-g*x² identically for all k4,k5,k6. For compactly supported invariant probability mu, d/dt E_mu H=0 gives E_mu x²=0 and supp(mu) subset {x=0}; invariance and uniqueness force y=0 (from xdot=r*y), then v=0 (from ydot=v), then u=0 (from vdot=-u), so supp(mu) lies on the equilibrium line. Conversely any measure supported on the line is stationary. A recurrent point has H(phi_t p) nonincreasing; return times approaching p force its time-integrated dissipation to vanish on every finite time interval, hence x(t) identically zero and the same tangency chain yields p on the line. This does NOT prove all orbits are bounded, nor all complete bounded orbits are equilibria: heteroclinic dynamics can remain. At the published parameters H=z+126*x²/61 and origin is exactly stationary. These conclusions are proved analytically, not from finite experiments.

## originality

FAIL

A distinct, earlier published SCOPE record SCOPE-20261011-dced9fadf5ee (source commit 43952aa5 at 2026-10-11T13:03:06Z; assigned source committed 2026-10-11T13:03:44Z) explicitly gives the identical H, exact derivative, compact invariant-probability classification, recurrence exclusion and numerical correction for the very same Bao–Chen–Liu–Deng vector field. Its displayed formal theorem sets k4=k5=0, while the assigned claim allows arbitrary k4,k5, so the literal statement does extend the stated parameter domain. However reading the *complete prior proof* shows no step uses k4 or k5: the x,z equations and the tangency chain x=0 => y=0 => v=0 => u=0 are exactly the same for arbitrary values. The claimed generalization is therefore a mechanical removal of unused hypotheses, not an independently original construction or proof. The earlier source further proves bounded-forward-orbit convergence, stronger than the current claim on its original slice. The current Resultary hit SCOPE-20261011-ed9a3605b311 is a mirror of the assessed record and is not counted as separate prior art. The original 2019 paper is scientifically inconsistent with the corrected recurrence conclusion for its Section 2.3 example, but this correction had already been published in SCOPE-20261011-dced9fadf5ee.

## value

FAIL

Correcting a published chaotic-regime computation is mathematically motivated, and a global recurrence obstruction is generally of interest. However this particular record reproduces an already published same-system strict Lyapunov function, the exact stationary-measure classification, the exact origin consistency check, and all recurrence consequences. The only enlarged parameter domain comes from leaving k4 and k5 unrestricted: these coefficients never enter the defining Hdot calculation or the invariant-set tangency chain, so the prior published proof passes through verbatim. No new mechanism, independent nontrivial parameter boundary, sharper invariant, new counterexample, or additional classification is established. The earlier record even proved a stronger bounded-orbit convergence statement on the original slice. Under the same scientific value bar, this mechanical deletion of unused hypotheses is not a separately valuable theorem, despite the intrinsic importance of the correction already published.

The dated certificate retains the supplied scientific assessment, sources and limitations.
