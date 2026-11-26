# Independent mathematical audit

## correctness

PASS

At primes of Q(zeta_p) over the distinct radicands, the valuations are one on the matching radicand and zero on the others, giving independent Kummer classes. The resulting monomial basis both separates the root sums and permits the cyclotomic coefficient automorphisms fixing the radicals; the translations and these automorphisms act faithfully by t -> ut+v. This proves integrality, irreducibility and the splitting-field identification. At discriminant-good primes the root reductions are distinct, so the Frobenius cycles give the factor degrees. In particular a radicand prime is necessarily bad (vary its tag at fixed other tags to see a collision); p is bad since all reduced roots coincide. Thus the nonzero residue test at good q congruent to 1 mod p is legitimate. A nonzero translation has only p-cycles; a scalar u != 1 gives a unique fixed point after translating and all other cycles of length ord(u). The counts are conjugacy-stable and yield the claimed natural densities. At bad primes no squarefree pattern is asserted: characteristic p gives (X - sum ell_j)^(p^n), and for other q all reduced roots lie in F_(q^ord_p(q)) or F_(q^p), as appropriate, including when a radicand reduces to zero. The degree bound is sharp at good translation primes and only implies all-prime reducibility when n >= 2. As an independent check on the example, (X^3-7)^3-270X^3 gives the stated degree-nine polynomial: cube X^3-7=3*2^(1/3)*5^(1/3)*X at its roots. The supplied VERIFICATION.md and VERIFY.py were inspected; the stated 265 finite tests are package evidence, not a rerun and not the proof. Replay the analytical check in RESULT.md Steps 1–5.

## originality

PASS

Credit the explicit factor-degree and residue-test classification of these radical-sum polynomials, with exact prime densities and a sharp bound across all reductions. Neither the root-product construction nor existence of irreducible polynomials reducible at every prime is new. The searches and actual statements inspected did not show the specific splitting law or a published result already giving it in this family. This is a best-of-knowledge finding, not a priority guarantee.

## value

PASS

For the natural odd-exponent extension of the Swinnerton–Dyer family, this gives more than another example of global irreducibility with locally reducible reductions: it determines the complete squarefree factor-degree spectrum and its frequencies and gives an arithmetic test on the radicands with no need to construct or factor the degree-p^n polynomial. In particular the contrast between no linear factors versus exactly one, and the uniform bound even at collisions, make it usable as an explicit family with very different local behaviors. The standard ingredients and the already-known existence phenomenon are not credited independently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
