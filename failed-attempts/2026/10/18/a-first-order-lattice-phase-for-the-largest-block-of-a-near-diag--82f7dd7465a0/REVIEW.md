# Independent mathematical audit

## correctness

PASS

Separate the pair-only profile W0, profiles with only tripletons above size two, profiles with one size-four block, and the remainder. Label counting gives the frozen falling/rising factorial ratio; the uniform log expansion for at most C log r tripletons has first-order term (2ju−j(2j−1))/r, and the bounding exponential series has a superpolynomially small tail. Summing yields 2uλ−2λ²−λ in S/W0. A single four-block multiplies the j-tripleton ratio by (r−2j) falling 3 divided by 3(n−2r+1+j) rising 2; after scaling by r this tends uniformly on compact u ranges to u²/3 for each fixed j, and a bounded exponential series dominates the j sum uniformly. The remaining categories contribute O(r⁻²) since the combined weights of size ≥5 are O(r⁻²) and the size-four weight is O(1/r). Reciprocation gives 2u/3−7u²/9. The floor contributes r(u−t²)=−2t²δ+o(1); the two sequences at t=1 and the stated interval follow. For endpoint phases use n=ceil((m/t)²) and n=ceil((m/t)²)−1, respectively, giving approach from at/above and strictly below the m threshold. The primary conjecture's parameters and fixed-coefficient meaning match. Independently verified selected exact probabilities using coefficient recursion for [(e^z−1)/z]^(n−r); python3 /workspace/reproductions/finite_checks.py 5, at r=40,80,160 on both sequences. Finite checks support, but do not prove, the uniform remainder.

## originality

FAIL

Prior implication is demonstrable, not merely an access risk: Temme's 1993 uniform second-kind Stirling expansion gives the full frozen 1/r coefficient in this regime. Here is the extraction. Put m=n−r, ρ=r/m, B(x)=(e^x−1)/x, and choose x by x(log B)'=ρ, equivalent to Temme (2.5). Equations (2.6)–(2.10) and (4.2) give S(n,m)=(n!/m!)(m^r/r!) exp(A)(f(ρ)+O(1/m)); A=m log B(x)−r+r log(ρ/x). The saddle prefactor is f(ρ)=[ρ/(x dρ/dx)]^(1/2), by differentiating the saddle change of variable. The first correction in (4.2) is bounded in this limit, so m⁻¹=o(r⁻¹), and f(ρ) tends to one. Hence log(S/W0)=m log B(x)−r+r log(2ρ/x)+log f(ρ)−Σ_{j=0}^{r−1}log(1−j/m)+O(m⁻¹). Now log B=x/2+x²/24+O(x⁴) and x=2ρ−2ρ²/3+4ρ³/9+O(ρ⁴). The first three terms combine to mρ²/6−mρ³/18+O(mρ⁴); log f=−ρ/6+O(ρ²); the negative sum is mρ²/2−ρ/2+mρ³/6+O(r⁻²). Together this is 2mρ²/3+mρ³/9−2ρ/3+O(r⁻²)=2u/3+(7u²/9−2u/3)/r+O(r⁻²), uniformly as required. Exponentiating its negative gives the frozen formula. Substituting r=floor(t√n) then gives the entire phase law and the two-subsequence counterexample. I do not claim Temme printed the probability or the later conjecture; the coverage is by implication from the stronger published asymptotic. The profile proof is direct and informative, but the frozen finding claims the expansion and its floor consequence, not a distinct theorem about profile contributions.

## value

PASS

Explaining why a fixed coefficient in a published conjecture fails is worthwhile: changing from a moving intensity to the fixed limiting intensity creates an oscillation at exactly the order the conjecture concerns. The profile proof also exposes the size-four block contribution. This usefulness does not make the implied main expansion original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
