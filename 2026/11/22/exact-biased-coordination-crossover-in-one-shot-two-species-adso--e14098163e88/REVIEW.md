# Independent mathematical audit

## correctness

PASS

At fixed finite degree z, a dependency path of length n must have n+1 strictly decreasing iid continuous times. Its union bound is z(z−1)^(n−1)/(n+1)! and tends to zero; countability gives simultaneous almost-sure construction. Conditioning on the root's own proposal makes its branches independent with the parent absent. Thus the cavity absence probabilities u=1−a and v=1−b satisfy u' = −p v^(z−1), v' = −q u^(z−1) with u(0)=v(0)=1, and full-root acceptance rates are p v^z and q u^z. The derivative of p v^z−q u^z is zero, giving the stated imbalance. Also (uv)'=−p v^z−q u^z, so total occupation is 1−uv. At balance u=v, and the scalar equation gives the displayed z=2 exponential and z>2 power law, with terminal asymptotic 2 log(z/2)/z. For fixed δ=p−q>0, p v^z=δ+q u^z and v≤1 give u(1)≤1−δ. Changing the minority integral to r=u^z gives zρ_B(1)=∫(q/p) r^(1/z)((δ+qr)/p)^(−(z−1)/z) dr from u(1)^z to 1. The lower endpoint tends to zero and the integrand extended by zero is bounded by q/δ, with pointwise limit q/(δ+qr) for r>0. Integrating gives log(p/δ); symmetry handles the other bias and p=0,1 are trivial. This is an infinite-volume proof, not a fit to the finite-depth simulation.

## originality

PASS

The originality supported for the combined finding is the arbitrary-bias regular-tree characterization with its signed-density invariant and sharp fixed-bias minority limit. The line law is previously established. The balanced all-degree closed form and its elementary degree asymptotic are also covered by homogeneous monomer RSA via an exact parameter reduction, and must not be credited independently as new.

## value

PASS

On the natural regular-tree extension of the one-shot line model, the signed invariant identifies precisely how much of the majority bias survives blocking, and the positive logarithmic coefficient resolves the smaller minority density at fixed bias. Together they distinguish order-one total density at nonzero fixed bias from vanishing balanced density and separate this effect from the different rare-minority retry regime. Value does not rely on the already covered balanced formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
