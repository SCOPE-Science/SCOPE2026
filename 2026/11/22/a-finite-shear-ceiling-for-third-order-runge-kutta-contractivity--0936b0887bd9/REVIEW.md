# Independent mathematical audit

## correctness

PASS

For the stated three-stage, third-order explicit methods, N²=0 gives T=rI+γhpN. For a real 2×2 block aI+dN, testing positivity of the Gram defect gives determinant (1−a²)²−d² and leading diagonal 1−a². If 1−a²>0 its Schur complement gives the criterion a²+|d|≤1; if 1−a²=0 it requires d=0; if a²>1 the scalar mode already fails. Thus the criterion includes all equality cases. Since r'=−p<0, only [0,β] is admissible, and at β only γ=0 works. On the positive interval the bound is γ≤G(h); the rational derivative is −hF(h)/(18(h²−2h+2)²). The verified sum of positive squares and constant for F' gives exactly one zero of F, in (0,1) and hence before β. G starts at 2, strictly increases to G(θ)>2, then strictly decreases to 0, yielding exactly the four stated cases. At θ its second derivative is strictly negative, so analytic expansion and inversion give the two fold signs, the width prefactor and the claimed O(γ_*−γ) endpoint errors. The expansion G=2+h²/3−h³/4+O(h⁴) similarly gives the square-root onset. Exact identities and constants are replayable with python3 /workspace/reviews/replay-2-3.py (SymPy); the independent exact check also found γ=101/50,h=1/2 feasible with slack 43/11520 in inequality (1). The decimal approximations of θ and h_+(2) have minor last-digit drift; they are 0.479811179914856486… and 0.692694281922297491… from the exact equations. The generator has top symmetric eigenvalue −1+γ/2, fixing the all-time physical threshold. The manuscript correctly distinguishes infinitesimal expansion from expansion at the same positive timestep. In the RK4 comparison, at the zero α∈(0,2) of P_4'(−h)=r(h), P_4(−α)=α⁴/24<1 and the off-diagonal vanishes for all shear, verifying the qualitative contrast. The supplied verifier was inspected, not executed.

## originality

PASS

Bounded best-of-knowledge credit for the sharp cubic ceiling, single-fold geometry and quantitative endpoint laws. Neither the triangular norm formula nor the general method of substituting the stability polynomial on a Jordan block is new. Merely proving that the cubic shear is bounded is straightforward from compactness of the scalar interval and positivity of p after removing the h=0 singularity; that weaker fact is not the basis of the originality assessment.

## value

PASS

This gives a precise one-step energy boundary for a minimal nonnormal linear test equation: scalar absolute stability persists while all positive contractive steps disappear at the shear cutoff. The meaningful features are the full level-set topology, the exact isolated positive step at the cutoff and the two onset/collapse laws, not the small numerical improvement above γ=2 in isolation. The contrast with RK4 identifies the role of the nilpotent coefficient and does not assert numerical accuracy or a general theorem for other matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
