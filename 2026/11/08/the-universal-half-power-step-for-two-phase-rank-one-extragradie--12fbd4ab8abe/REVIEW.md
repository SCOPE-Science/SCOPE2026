# Independent mathematical audit

## correctness

PASS

Each single-stage T_w fixes its perpendicular neutral vector e_w and has squared singular matrix kI+δ e_w e_w^T, where δ=h²(1−h²), k=1−δ. The product P=T_v T_u gives P^TP=k²I+kδ aa^T+δbb^T with a=e_u and b=T_u^T e_v; its rank-two Gram matrix has trace δ(2k+δc²), determinant δ²k²(1−c²), yielding the three claimed singular values for 0≤h≤1. Independently recomputed exact symbolic characteristic polynomial for rational unit overlap (c,s)=(3/5,4/5), h=1/2. The derivative sign identity (2−δc²)²−c²(4(1−δ)+δ²c²)=4(1−c²)>0 gives unique δ=1/4 at h²=1/2 for c<1. At h>1 each stage σ_min=1 and hence P has σ_min≥1, excluding a better global step; c=1 neutral direction gives norm1. Angular derivative at c=1 is 1/7, giving θ²/14. No Floquet spectral-radius optimality is inferred.

## originality

PASS

Feng et al NeurIPS 2023 treat arbitrary periodic bilinear games using normal one-step maps and spectral/Floquet contraction, but their actual Theorem3.1 and text do not state the sharp singular spectrum or optimize one-period Euclidean operator norm of two noncommuting rank-one 1×2 stages. Earlier fixed-game EG step results and stochastic two-oracle coupling results concern different matrices/objectives. Underlying Gram update is standard; the new part is the closed full singular spectrum and universal optimal step independent of payoff-row angle for this noncommuting period-two class.

## value

PASS

The sharp worst-case one-period contraction factor and universal step are motivated numerical-optimization invariants for a natural minimal noncommuting time-periodic game. The exact angle-dependent defect quantifies loss near common null directions and provides an actionable deterministic tuning principle, while carefully not claiming runtime or asymptotic spectral radius optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
