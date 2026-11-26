# Independent mathematical audit

## correctness

PASS

For A=I₂ the corrected residual is (I−zzᵀ)E_D. Maximizing zᵀE_DE_Dᵀz leaves the smaller squared diagonal defect, α² min(S₁²,S₂²)/D². Centered programming maps one step to the full Cartesian product of two fair signs under (S₁+S₂,S₁−S₂), so the two D-step walks are independent and the minimum is one fourth of the squared difference of their absolute values. This gives (D−m_D²)/2 before rescaling. In the one-sided model S₁+S₂=D and the minimum is (D−|U_D|)²/4. Conditioning on the walk location gives m_{n+1}−m_n=Pr(U_n=0); the two stated binomial formulas satisfy this recursion at each parity and m₀=0. Stirling gives m_D=√(2D/π)(1+O(1/D)), yielding both limits and the stated remainder. D=1 gives zero; at D=2 distinct directions occur with probability 1/2 and give loss α²/4. At every D≥2 the event of all positive signs and both coordinates selected has positive probability, establishing strict expected loss, not almost-sure rank two. Directly summing the diagonal second moments gives the two decreasing uncorrected risks.

## originality

PASS

Pass only the exact finite-copy two-sign-regime oracle Frobenius-risk laws and their quantitative consequences. Shah et al. already have the projection identity, bias/variance decomposition and warning about corrected error nonmonotonicity. The frozen record acknowledges these, and the inspected prior does not state or mechanically supply the nonlinear order statistics in this oracle model.

## value

PASS

The exact risk distinguishes a centered defect that decays at a known 1/D constant from a biased defect with a positive floor, even though the uncorrected risk decreases in both. The single-to-double-copy comparison demonstrates the failure of exact correction even with perfect information and no read noise. Together these are a quantitative benchmark for deciding what copy averaging and a fixed correction rank can accomplish, not simply the previously known nonmonotonicity caveat.

The dated certificate retains the supplied scientific assessment, sources and limitations.
