# Independent mathematical audit

## correctness

PASS

Differentiating the fixed-mean negative-binomial PGF at q gives R_k/μ=(1+z/k)^(-k-1); no conditional independence of recruitments is needed. At fixed z>0 the endpoint values k→0 and k→∞ are 0 and e^{-z}. With t=z/k and g(t)=(1+t)log(1+t)-t, the log derivative has the sign of H(t)-z. Independently, integration twice using g''(t)=1/(1+t) gives 1/H(t)=∫₀¹(1-u)/(1+tu) du, strictly decreasing from 1/2 to 0. Its expansion gives H(t)=2+2t/3+O(t²), and g(t)~t log t at infinity. These establish the exactly unique optimum, including strict increase at z=2 and nonattainment at every finite shape there. At the interior optimum, t/z~log t~log z, so k_* log z→1 and (1+t)^(-k_*)→e^{-1}, with (1+t)~z log z. For two finite shapes the log ratio derivative is (k₂-k₁)(z-1)/[(k₁+z)(k₂+z)]; for k₂=∞ it is (z-1)/(k₁+z). With log ratio initially zero and tending to positive infinity, there is exactly one positive crossing. The all-shape ordering through z=2 in fact implies the stated crossing is above 2, stronger than the claimed >1. Independently obtained k_*≈0.971897376815 and normalized recruitment ≈0.040005389824 at z=4 by bisection and evaluation. Read the source verification notes and checker without executing it. Conclusions are one-episode expectations under the specified law, not population dynamics or intervention prescriptions.

## originality

PASS

The Hassell shape-response curve is already known and receives no originality credit. The checked closest primary text displays that exact normalized shape curve but does not supply the fixed-input, global real-shape phase diagram in the passages inspected. No examined source preempts the aggregate of optimizer classification, its endpoint asymptotics, and the full pairwise reversal statement. Closely related inaccessible papers leave priority provisional.

## value

PASS

At fixed mean the direction of the effect of excess variation is not constant: the result sharply distinguishes when aggregation can never improve mean recruitment from when there is a single finite optimum. The near-critical divergence and strong-crowding optimum quantify the transition, and the pairwise single-crossing theorem describes comparisons of preset shapes that cannot be freely tuned. These are usable predictions of a specified baseline, not a general recommendation to increase clustering.

The dated certificate retains the supplied scientific assessment, sources and limitations.
