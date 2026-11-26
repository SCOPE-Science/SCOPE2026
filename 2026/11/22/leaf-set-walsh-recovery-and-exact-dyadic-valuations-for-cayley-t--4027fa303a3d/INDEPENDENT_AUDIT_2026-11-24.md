# Independent mathematical audit

## correctness

PASS

The Prüfer word has length n−2, and its absent labels are exactly the leaves. Expanding a factor 1−2 for each selected absent label gives the unnormalized inclusion–exclusion sum. At n=2 the sole tree gives (−1)^k (the empty word gives 0^0=1); odd n has odd j=0 term and even remaining terms. At even n≥4 and nonzero character weight k, put s=ν₂(k). The j=1 term is −2k(n−1)^(n−2), of valuation s+1. For j≥2 the identity j binom(k,j)=k binom(k−1,j−1) gives a valuation bound s+j−ν₂(j) before the power of n−j. Odd j≥3 already suffice; even j gain ≥n−2 further powers of two (a zero power-term with positive exponent vanishes). The constant term has valuation (n−2)ν₂(n)≥s+2, directly at n=4 and by n−2≥⌊log₂n⌋+2 for n≥6. Thus only j=1 survives at its valuation. The trivial character is n^(n−2). For n≥3 the gcd of the weight-zero and weight-one multipliers is gcd(n^(n−2),2(n−1)^(n−2)); this is already 1 or 2 as claimed, and all multipliers share that divisor. The 2^(n−1) odd-weight characters are exactly the valuation-one characters at even n≥4. The product of the multipliers is the integer determinant, which is a 2-adic unit exactly in the stated cases; the rational and real diagonalizations give invertibility in every order. An independently written edge-subset tree enumeration, not Prüfer enumeration, agrees with every character through n=6 (replay: python3 /workspace/branches/small_exact_checks.py).

## originality

PASS

The exact prescribed leaf-set distribution and the occupancy representation are prior inputs. The supported distinct result is the all-order arithmetic statement: no vanishing characters and exact 2-adic valuations and their spectral consequences. The strongest distinct catalogue match concerns edge-incidence frequencies, not the leaf projection. No examined source is shown to imply this valuation classification without new arithmetic.

## value

PASS

The multiplicity-weighted leaf law is a natural symmetric but dependent projection of a uniform labelled tree. Knowing exactly which character cancels, and how much power of two each nonzero coefficient carries, determines whether XOR observations can recover every Fourier component and distinguishes the even and odd orders integrally. It is not a recomputation of unsigned counts: symmetries only reduce the number of distinct frequencies, and large terms of opposite sign can in principle cancel. The all-weight classification and exact half-of-modes phenomenon answer that question beyond any finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
