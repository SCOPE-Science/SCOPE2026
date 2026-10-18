# Independent mathematical audit

## correctness

PASS

The polar dynamics are dr/dt=lambda r(1-r²), dtheta/dt=omega+c(1-r²). For r>0, Phi=theta-(c/lambda)log r has exact derivative omega; r=1 is hyperbolically attracting with radial exponent -2lambda and common orbital frequency omega. Its gradient on the unit circle is e_theta-(c/lambda)e_r; the tangent component is fixed and the radial coefficient arbitrary. Thus all exact cycle data coincide while full phase-response curves differ. Independently simplified the phase derivative symbolically to omega and verified on-cycle shear argument. This is a structural non-identifiability claim, not a numerical failure of any particular ML model.

## originality

FAIL

FAIL: Yawata–Fukami–Taira–Nakao, Chaos 2024, Equations (29)–(31), ALREADY presents the same parametric Stuart–Landau normal form, frequency omega=alpha-beta, global phase theta-beta log r, and explicit phase response vector e_theta-beta e_r. Choosing alpha=omega+beta and varying beta fixes on-cycle states and velocities but varies radial PRC; this is the submitted counterfamily at lambda=1. The full same-orbit/different-PRC conclusion follows immediately from those published equations even without a matching titled theorem. The later Zhang et al. 2026 focal machine-learning paper was not fully accessible, but the older full-text mathematical coverage is decisive.

## value

FAIL

FAIL: The concern about on-cycle identifiability has applied relevance, but its exact witness is a straightforward reparameterization of the published textbook Stuart–Landau phase response formula with alpha-beta fixed. It adds no independent dynamical invariant, nonstandard construction, boundary proof, or new sharpness fact beyond making an already obvious parameter nonidentifiability observation. Motivation alone cannot turn a known normal-form substitution into a distinct valuable mathematical finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
