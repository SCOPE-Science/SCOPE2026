# Independent mathematical audit

## correctness

PASS

For positive r,c,a,b and x0,y0,z0, direct differentiation gives s_dot=s(r-d(q)s-az), q_dot=-(r-c)s q(1-q^2)/2, z_dot=z(bs-1), where d(q)=(r+c+(r-c)q^2)/2. Integrating w.r.t. B(t)=int_0^t s gives q/sqrt(1-q^2)=(q0/sqrt(1-q0^2))exp(-(r-c)B/2), with q0=0 invariant. Positivity and L=s+(a/b)z yield a global upper bound, and B cannot remain finite because that would force z->0 and then positive logistic recovery of s, contradiction. The B-change-of-variable reduces the accumulated penalty to elementary log integrals, giving -log|q0| for c>r unequal, -0.5log(1-q0^2) for r>c, and zero in invariant cases, absolutely convergent. Perturbed Volterra Lyapunov functions with integrable delta=d(q)-d_inf give int(s-s_inf)^2<infinity; uniform continuity and bounded derivatives prove s->s_inf and z->z_inf even on the invasion equality boundary. Independent symbolic derivative algebra and numerical IVP c=2,r=1,b=1.25,a=1 show unequal predator limit 0.2 vs equal predator extinction and correct log penalty; finite IVPs are diagnostic.

## originality

PASS

PASS best-of-knowledge: published same-model general three-species classifications under strict apparent-competition inequality r1 a23 > r2 a13 do not cover this exact exchange-symmetric equality regime. A different 2026 predator-dependent replicator paper has a frequency-dependent system, not the exact two-prey mass clock here. Searches of published mathematical results and primary literature yielded no prior formula for the global log integrated excess-competition functional jointly with the sharp all-initial-states predator persistence discontinuity. Classical competitive exclusion and planar LV Lyapunov methods supply ingredients but not this exact invariant. Residual risk: unindexed older symmetric three-species theory may contain equivalent quantitative separatrix calculations.

## value

PASS

PASS: the exact all-time logarithmic competition penalty is a natural conserved/finite dynamical functional, sensitive only to initial prey composition despite predator coupling; the parameter-sharp, discontinuous infinite-time predator fate along the invariant prey-balance separatrix is an ecologically and mathematically meaningful global basin classification. Not a generic renaming of the replicator equation: it proves a nontrivial quantitative transient invariant and global convergence at the neutral threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
