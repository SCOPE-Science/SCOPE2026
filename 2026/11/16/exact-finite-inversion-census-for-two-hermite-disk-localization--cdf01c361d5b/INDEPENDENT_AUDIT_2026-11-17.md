# Independent mathematical audit

## correctness

PASS

The Hermite-STFT radial density is exp(-t)t^k/k! for h0 and exp(-t)t^(k-1)(k-t)^2/k! for first-Hermite k>=1 (separate k=0). Angular characters diagonalize the centered disk integral for every k. Incomplete-gamma integration gives λ_k=(1+ρ)q_k+(k-s)p_k, and subtraction yields exact sign prefactor p_k/(k+1)>0 multiplying G=(s-k)(s-k-1)+ρs. For ρ>0 negative G is confined to disjoint intervals (k,k+1); for k>=1 its quadratic discriminant (1-ρ)^2-4kρ>0 iff ρ<(sqrt(k+1)-sqrt k)^2, with tangency at sqrt(k(k+1)); k=0 yields 0<s<1-ρ when ρ<1. Number of eligible k is ceil((1-ρ)^2/(4ρ)) for 0<ρ<1, zero if ρ>=1, infinite at ρ=0. The +ρs term is strictly positive for all positive integer s, excluding zero gaps. Independently checked symbolic discriminant and gap polynomial, read full RESULT.md and check_mixed_disk.py; finite numerical quadratures do not carry the all-k claim.

## originality

PASS

The exact finite census of mixed Gaussian/first-Hermite adjacent reversals is a new structural spectral-order result to best of knowledge. General radial mixed-state Hermite eigenvalue formulas and pure first-Hermite order were located, but neither states nor directly subsumes the sharp all-ρ threshold and reversal interval count without further algebraic classification.

## value

PASS

The exact number and locations of spectral-order inversions under adding a second natural observation channel quantify a genuine instability: arbitrarily small Gaussian weight reduces infinitely many reversals to finitely many and removes all positive integer-area degeneracies. The sharp ρ=1 universal threshold and full count can be used in Hermite cutoff selection; this is motivated mixed-state spectral structure rather than a recomputed eigenvalue table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
