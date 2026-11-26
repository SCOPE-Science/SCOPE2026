# Independent mathematical audit

## correctness

PASS

Independently checked the finite-state argument with signed even-bath increments in units of 4J and the frozen flip-rate convention. Positivity of each flip rate gives irreducibility on all 16 states. Applying the flip differences to U,V,W,P yields the closed generator equations and stationary moments in RESULT.md. For an even flip, U becomes U−4q, V changes sign, and W is fixed, so h₀ after the flip equals h₀−q/2−bV/4. With f=U/2−a(1+W) and v=1+W−aU/2, this gives v+2L₁h₀=(U−bV−aW)f/4. Expanding with U²=4(1+V)(1+W), UV=UW=U and VW=P gives the stated second-cumulant integrand. The generator equations give Lh₀=j−f; centering h₀ in the simple tilted eigenpair gives k″(0)=E[v+2L₁h₀]−2jE[h₀], equal to (1−ab)/2−(b−a)²/16. Positive rates also give initial-law independence of the limiting cumulant rates. The fixed-mean identity, equilibrium limit, and a=0 crossing and monotonicity follow algebraically. The supplied SymPy checker was read, not rerun; the recorded calculations are symbolic spin identities and rational generator checks, not the basis of the originality verdict.

## originality

FAIL

Bauer and Cornu’s Thermal contact through a two-temperature kinetic Ising chain (arXiv:1712.02273, first posted 2017) gives the full finite-ring heat SCGF and explicitly gives the first two cumulants for precisely this alternating-bath dynamic with more general kinetic rates. Its primary text explicitly evaluates the needed N=2 sums. Taking their 2N=4, ν_e=ν_o=2, γ_e=a, γ_o=b, and Q=Q_e/(4J) gives the two frozen rates exactly. The fixed-mean excess and signed heat dispersion crossing are immediate algebraic consequences with no further model calculation. This is verified prior coverage, not a claim that the frozen four-spin proof is incorrect.

## value

FAIL

Four-site finite-size effects and noise of signed heat are natural quantities. The frozen record specializes an existing exact finite-ring cumulant result at the explicitly evaluated four-spin size. Rearranging its second cumulant at fixed mean and taking a ratio at a=0 do not determine a previously unknown invariant or require a new boundary argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
