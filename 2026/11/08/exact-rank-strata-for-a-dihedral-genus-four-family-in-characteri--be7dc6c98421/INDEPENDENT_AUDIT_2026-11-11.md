# Independent mathematical audit

## correctness

PASS

For smooth x(T^4+aT^3+bT^2+aT+1)|_{T=x^2} of degree 9, the genus is four. Direct coefficient extraction from f(x)^3 verifies M_{ij}=c_{7i-j} in the differential basis. Its permuted 2x2 anti-diagonal blocks have common determinant D=uw-v and each a unit entry, so Cartier rank is 4 if D!=0 and exactly 2 if D=0; the a-number is 0 or 2. Crucially the semilinear Cartier iterate is tested with Frobenius twist: on D=0 the twisted products are rank two for E=1+u^7*w!=0 and nilpotent for E=0, giving stable 7-ranks 2 and 0. An independent GF(7) SymPy symbolic reconstruction in this audit checked all 16 Cartier matrix entries, determinant D^2, and lex Groebner elimination of (D,E) giving degree-22 P(a) with squarefree part degree 20. The discriminant after the unique b substitution is coprime to P, so all twenty geometric solutions are smooth; the 20 count is not merely GF(7) or GF(49) sample evidence. The examined verification scripts independently compute the F49 sample and characteristic-7 algebra. Limitation: coefficient-marked parameter points, not isomorphism classes or Newton polygons.

## originality

PASS

The 2026-10-18 same-family SCOPE theorem already gives the entire Cartier a-number/nonordinary divisor, after the exact parameter substitution s=a,t=b-2; that part is NOT original. It only determines p-rank on the two F7-rational exceptional pairs, whereas the present result establishes p-rank across the full geometric D=0 divisor and identifies exactly 20 geometric zero-rank parameters by new elimination. The broader original dihedral normal form and superspeciality literature likewise do not supply this remaining geometric 7-rank census. This precise surviving all-geometric stratification is best-of-knowledge original; an unindexed earlier table may still overlap.

## value

PASS

A natural full two-parameter automorphism-rich genus-four curve family has standard Jacobian invariants 7-rank and a-number. The new step separates geometric rank-two and rank-zero loci inside the previously known nonordinary divisor and counts exactly 20 smooth marked rank-zero fibers, a finite exceptional stratum of intrinsic arithmetic interest. Unlike a small-field recomputation, the exact geometric census uses elimination over the algebraic closure and proves an all-parameter classification; it does not pretend already-known nonordinary divisors themselves are new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
