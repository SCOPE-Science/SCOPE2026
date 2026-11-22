# Independent mathematical audit

## correctness

PASS

The graph windmill has no simple cycles between cliques. Acyclic orientations correspond bijectively to independent total orders of the m K_k petals, yielding (k!)^m distinct vertices. In each clique the hub rank H_i is iid uniform on {j−(k−1)/2}; C_k is the clique score squared norm, σ_k²=E H_i². The common hub coordinate sums the H_i, whereas leaf coordinates remain disjoint, so Q=mC_k+(ΣH_i)^2−ΣH_i²=mC_k+2Σ_{i<j}H_iH_j. Multiplying by four and grouping counts of each b_j=2j−(k−1) gives the complete integer shell polynomial with weight ((k−1)!)^m m!/Πa_j!. Independence and centering give E Q=mC_k and Var(Q)=4 binom(m,2)σ_k⁴=2m(m−1)σ_k⁴; distinct pair cross covariances vanish. CLT and SLLN yield Q/m ⇒ C_k−σ_k²+σ_k²χ₁² for fixed k. Maximal common same-sign hub ranks uniquely provide R²=mC_k+m(m−1)(k−1)²/4, contact count 2((k−1)!)^m. This is a full analytic proof rather than an extrapolation of finite ranks.

## originality

PASS

The full uniform discrete-vertex radial polynomial and shifted chi-square law are distinct from known global outer radius/contact and continuous-volume inertia; the latter are credited, not presented as new. No prior complete distribution was established by indexed search and inspected sources.

## value

PASS

The all-shell multiplicity polynomial for a natural infinite family of graph zonotopes gives exact vertex inertia fluctuations and a counterintuitive nonconcentrating χ₁² radial law despite exponentially many independent clique choices. Exact variance, asymptotic law, and contact rarity separate typical geometry from known worst-case radius, a motivated and independently useful invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
