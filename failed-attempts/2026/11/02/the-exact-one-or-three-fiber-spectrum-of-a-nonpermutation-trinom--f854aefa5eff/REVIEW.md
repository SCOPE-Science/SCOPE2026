# Independent mathematical audit

## correctness

PASS

With h(u)=u²+tu−1, h has no torus zero: subtracting the conjugate equation multiplied by u² forces u²=1, where h=±t≠0. The lift gives exactly one preimage x=y/h(u) per direction u mapping to v=y^(q−1), and F(0)=0. At v=±1 the remaining quadratics are u²+(t±2)u+1 with respective nonsquare discriminants 2(t±1)²; their conjugate inverse roots lie on the torus, and coincidence with the first root would force t=∓4, impossible since char≠2,3. For v≠±1 set ε=v−v⁻¹, A=ε²=s²−4 and τ=t+εU. Then τ is never zero, x=(y/τ)^q and u=v⁻¹τ^q/τ. Multiplying u−u⁻¹=εU by ττ^q yields AU³−AU²+(2−2ts)U+2=0, so the reduction is reversible. For this monic cubic the discriminant, after reduction by t²=−2, is −16(s+5t)²/A³. Since ε^q=−ε and ε≠0, A is nonsquare in F_q, as is −1. For s≠−5t the Frobenius permutation is even on three distinct roots, giving zero or three rational roots. At s=−5t the cubic is (U−1/3)³ with A=−54≠0. The two critical directions are exactly the roots of v²+5tv+1 with discriminant −54 and character χ_q(3); they belong to the torus iff this character is −1. Multiplying nonzero direction counts by q−1 and adding the singleton at zero yields S, and conservation of the q² inputs gives the two remaining counts. In an independent bounded computation enumerate the norm-one torus by (a+i)/(a−i) for a∈F_q, plus 1, i²=−1, and evaluate u h(u)^q/h(u) directly using conjugation. For q=11,19,1331, the respective direction histograms in multiplicity order (0,1,2,3) are (8,0,0,4), (12,2,0,6), (888,0,0,444), for both signs of t. For q=1331 the base field was represented by F_11[Z]/(Z³+Z+4), irreducible by checking all eleven residues. The singleton directions matched 2 Re(v)+5t=0 in all cases.

## originality

FAIL

The exact trinomial and its cubic reduction already appear in Hou 2013, but the permutation criterion alone is not a multiplicity census. Decisively, the induced direction map is two-sided projectively equivalent over F_q to the already classified cubic f_{−3,1}(X)=(X³−3X+1)/(X(X−1)) in Hou–Peng–Qiang–Zhao, arXiv:2604.18954v2 (2026-05-19), §6.1 and §§6.3, 6.6–6.8. Their Class III and ramification classification supplies exactly the fiber alternatives. Translating its branch values back and counting the q−1 targets per direction gives the claimed histogram and singleton directions by substitution and elementary counting. This is positive prior-coverage evidence in an equivalent formulation, not an exact textual match or an inference from an inaccessible article.

## value

FAIL

The spectrum of this trinomial is a natural invariant, but the narrow exact result is the cyclic cubic representative's known fiber behavior, transferred to F_{q²} by a projective change of coordinates and a scalar counting factor. The printed histogram is a useful specialization, not an independently new exact invariant under this standard. A separate claim about an unclassified map or a genuinely new use of the reduction was not delivered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
