# Independent mathematical audit

## correctness

PASS

For the stated deterministic critical ODE, the cube is invariant; at faces with a coordinate equal to 1 its derivative is strictly inward. Each scalar coordinate is a nonnegative input minus a bounded nonnegative multiple of itself. An initially positive coordinate remains positive, and the integrating-factor formula propagates strict positivity along each connected incidence/dyadic path for any positive time, including from environment-only or boundary data. The node effective matrix is irreducible because an incidence two-step gives a positive BBᵀ edge. Direct multiplication gives the stated normalized positive left and right null vectors; L is irreducible Metzler and is also similar to a symmetric matrix (scale the environmental coordinates by √(σ/β_e)), so the orthogonal-to-left-mode part in the spectral splitting decays exponentially. The nonnegative nonlinear loss Q makes a=wᵀz a Lyapunov function; strict positivity at later times excludes nonzero trajectories from the zero-loss invariant set. LaSalle gives global decay. On the cone, z=O(a), so 0≤-a'≤Ca² and a is bounded below by a reciprocal affine function. For late τ≤s, a(τ)≤a(s)exp(Ca(T)(s-τ)); choose T so 2Ca(T) lies below the spectral gap. Variation of constants then gives transverse remainder O(a²), with the earlier convolution exponentially small. The quadratic loss on v has entries γu_i² and (σ²/δ)q_h²; projection against w gives exactly K>0. Thus (1/a)'→K and both coordinate limits follow. The numerator is cubic in Perron coordinates; the amplitude equation is quadratic, not cubic. The frozen example gives W=9/2 and K=5/3 on direct substitution. The package’s numerical checker was inspected, not executed; neither integrations nor the formal verification status are used to prove the universal quantifier.

## originality

PASS

Credit the closure, critical global stability precedents and generic positive-system/spectral reduction methods. The supported distinct result is the explicit spatial leading coefficient, together with its validity from all nonzero cube states, for the fixed heterogeneous two-block deterministic closure. The closest indexed multichannel ODE has a scalar infection variable and substantially overlaps the mechanism but does not cover arbitrary node-level incidence; same-day dating does not decide priority.

## value

PASS

At criticality stability alone says nothing about the leading decay or about the relative sizes of the nonzero compartments. This gives a scale-independent explicit asymptotic on the entire nonzero invariant cube, including heterogeneous and boundary initial data, and identifies how the stable directions drop out. It is a mathematical extinction result in a deterministic closure, not a calibrated forecast or a stochastic extinction-time law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
