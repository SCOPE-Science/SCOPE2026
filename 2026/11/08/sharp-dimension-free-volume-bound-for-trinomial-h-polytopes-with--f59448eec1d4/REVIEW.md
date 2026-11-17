# Independent mathematical audit

## correctness

PASS

Because h*_1=0 for k>=2, P is an empty lattice simplex. Tsuchiya Proposition 4.3 bounds orders of the two height-2k elements to phi(order)<=4, generates the simplex group with them, and yields group order<=144. For each nontrivial dual character psi, coordinate-character Fourier transforms of support indicators are nonpositive, while target normalized heights give 2k(Re psi(x)+Re psi(y)-1), forcing spectral inequality Re psi(x)+Re psi(y)<=1. The included exact-Fraction verifier enumerates every C_m x C_n (m|n, 12<mn<=144), all eligible distinct high pairs, and characters; rational cosine lower bounds exclude 46135 of 46223 candidates. Its remaining 88 pairs lie in three fully enumerated automorphism orbits. Their three dual vectors force v dot normalized target = -1 but v dot every individual fractional character >=0; the audit independently recomputed these 3 negative targets and minimum dual=0 over respectively 16,16,18 characters using Fraction arithmetic, validating the critical separation. The source complete verifier and its 46223-pair result are exact reproducible arithmetic, not an arbitrary incomplete sample. Tsuchiya Example 4.5 achieves a=9 at every k>=2, giving sharp volume 12.

## originality

PASS

The October 2026 Tsuchiya primary paper was inspected with its group reduction Proposition 4.3, equality Example 4.5 and open sharp-volume question. It supplies a much weaker general bound and matching volume-12 examples at b=2 but no sharp universal upper for that slice. The 2015 Higashitani–Nill–Tsuchiya Gorenstein classification applies to palindromic h* vectors, whereas h*=1+9t^k+2t^{2k} is not palindromic. No available earlier theorem in Resultary or these sources implies volume<=12 for all a,k. Historical priority qualified because further literature may exist.

## value

PASS

This determines an exact dimension-independent maximum volume for every k>=2 in a natural h*-trinomial class, meeting an explicit known lower construction and resolving a concrete b=2 slice of a general extremal question. The novel finite-group Fourier/duality obstruction is substantive, not a routine recomputation of source examples, and its exact certificates are mathematically motivated by complete finite reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
