# Independent mathematical audit

## correctness

PASS

On the fixed plane of simultaneous patch and species interchange, internal migration cancels in the biomass sum, yielding F(s,d)=s−(a+1)s²/2+(a−1)d²/2 and the stated positive stationary root s(d). Reflection by either interchange alone maps the two partners to one another. In the contrast G(s(d),d), write k=aξ/2. The centered tanh difference supplies kd−k³d³/12 and the sum supplies k(s−s₀) to the required order; the biomass-shift corrections in the two migration terms cancel. This recovers λ_seg(ξ) and h(ξ) in RESULT.md lines 54–60. The derivative of λ_seg is positive, h(ξ_c)>0, and the implicit function in d² gives the stated one-sided branch and amplitude at positive ξ_c. To check the full stability argument, at a branch point the plane Jacobian has determinant F_s (d/dd)G(s(d),d), by differentiating F(s(d),d)=0. Both factors are negative: F_s=−√(1+(a²−1)d²), and the reduced derivative is −2λ_seg+O((ξ−ξ_c)²). Its trace stays near −1. The four full-system eigenvalues at onset are simple and real (the second negative eigenvalue is strictly below −1), hence stay real; the positive uniform-composition eigenvalue and the negative transverse eigenvalue persist. This gives exactly one positive and three negative eigenvalues on each branch locally. The worked rational example gives ξ_c=6, h(ξ_c)=5/2 and slope 2/45. Replay the scalar reduction and block/determinant test at RESULT.md lines 31–67; the frozen numerical verifier was inspected, not executed. The proven branch classification is on the invariant plane, with full-system instability of those equilibria, not a global persistence or exhaustive full-space equilibrium result.

## originality

PASS

The supported contribution is the centered equal-competition sigmoid pitchfork with its cubic amplitude and full-space saddle index, not the mobility law or the observation of segregation in the model. The exact-model paper's closest two-patch calculation assumes unequal strong competition. The inspected adjacent regimes and alternative mobility laws do not establish the joint local claim. This is a literature-bounded judgment.

## value

PASS

The centered sigmoid is a natural local regime in which competitor sensitivity can be varied without moving the uniform coexistence state. The theorem separates the birth of stationary spatial segregation from stable coexistence: the new states are attracting within their segregation plane, but perturbing population composition in the unconstrained system exposes a persistent unstable direction. The exact threshold and amplitude let a modeller distinguish and locate that onset; the result does not rule out distant attracting coexistence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
