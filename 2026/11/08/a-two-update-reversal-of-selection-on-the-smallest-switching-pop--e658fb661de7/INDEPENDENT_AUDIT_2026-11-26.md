# Independent mathematical audit

## correctness

PASS

I reconstructed the one-step matrices by enumerating ordered parent-neighbor pairs and lumping masks by the hub type and number of mutant leaves. The uniform single-mutant average weights a leaf twice and the hub once. With row probabilities the periodic product is S^tau K^tau, not its reverse. From each transient configuration a sequence of at most two resident reproductions can extinguish the mutants, with strictly positive probability along the prescribed schedule because both graphs are connected. For fixed r>0 the finite state/phase space then gives a uniform positive absorption chance over a bounded block, justifying the inverse. The Moran comparator is the gambler's-ruin formula for bias r and equals 1/3 at neutrality. For independent exact replay I formed the integer kernels scaled by d=2(r+2)(2r+1), used Laplace expansions of the four-by-four Cramer determinants, and checked every coefficient of (N(1+r+r²)-Dr²)D_tau-D Delta_tau, where N/D is the single-mutant average and Delta_tau is the signed numerator in Finding. All coefficients vanish modulo each of 100003, 100019, 100043, 100049, 100057, 100069, 100103, 100109. The scaled row polynomial l1 norms sum to d(1)=18; each entry of the Cramer matrices has l1 norm at most 2·18^4, so each cross-identity coefficient has magnitude at most 3·24·(2·18^4)^4·(4·2e8+2e6), below the modulus product. This is an integer identity check, not fitness sampling. The listed positive polynomials and factors give opposite strict signs at tau=1 and matching strict signs at tau=2 relative to r-1, proving the first amplifying integer dwell and the neutral equality.

## originality

PASS

Credit Bhaumik–Masuda with the exact model and phase order, the general periodic-chain method, the reported tau=1 suppression and the reported later reversal. Their range calculations do not give the all-fitness certificate or classify tau=2. The supported distinction is the sharp onset at the second update, with strict signs on the entire nonneutral fitness domain, not the observation that a reversal can occur.

## value

PASS

The motivating literature had already found reversal but left a gap between the first dwell and the displayed later dwells. The array of possible schedules starts at integer 1, and the exact boundary at 2 identifies what one extra update per phase can do on this minimal graph pair. The result controls both disadvantageous and advantageous mutants, including fitness extremes and arbitrary proximity to neutrality; it is not a numerical refinement at one chosen fitness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
