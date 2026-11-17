# Independent mathematical audit

## correctness

PASS

From the actual frozen graph-polynomial proof, A²=(k-μ)I+(λ-μ)A+μJ puts all powers of L=kI-A in three entry classes. Edge entries of the complete RK4 endpoint are hF(h) with cubic F=1-ah/2+(a²-b)h²/6-[a³-b(2a+μ)]h³/24, a=2k-λ and b=(k-λ-1)(k-μ). The nonedge-entry quadratic has strictly negative discriminant and positive value, while R4(-hL) is positive definite, so diagonals remain positive. With t=b/a²<1/4 and u=μ/a<1, the inequality 5-(10+9u)t-4t²>0 makes F strictly decreasing, and its sole positive zero τ is the exact *global* horizon, not just a first safe cutoff. At h=1/k the stochastic-matrix positive expansion gives all entries positive, so τ>1/k. Independent rational adjacency-matrix checks on Petersen, K3,3 and C5 total 981 assertions. No claim of stagewise positivity or extension to non-SRG graphs.

## originality

PASS

Best-knowledge assessment against mathematically matching and broader prior claims; explicit boundaries and uninspected-source risks retained. A complete graph-parameter-dependent positivity barrier for a widely used high-order diffusion time step, including nonreentrance, persistent nonedge positivity and guaranteed strict forward-Euler improvement. Those structural properties are not automatically returned by a generic numerical first-root algorithm.

## value

PASS

A complete graph-parameter-dependent positivity barrier for a widely used high-order diffusion time step, including nonreentrance, persistent nonedge positivity and guaranteed strict forward-Euler improvement. Those structural properties are not automatically returned by a generic numerical first-root algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
