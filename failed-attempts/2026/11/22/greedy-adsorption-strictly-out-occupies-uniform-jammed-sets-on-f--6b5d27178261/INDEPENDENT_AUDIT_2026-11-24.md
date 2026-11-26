# Independent mathematical audit

## correctness

PASS

A maximal independent set has endpoint omissions in {0,1} and internal omission runs in {1,2}; the binomial count and marked generating function follow by choosing optional omissions. The recurrences for total count F and total size A apply from n=5. The bound F_j<=3F_{j-1}/2 is valid from j=3: check j=3,4,5, then the two previous ratios give F_j<=5F_{j-3}/2 and F_{j-1}>=5F_{j-3}/3. Therefore the size recurrence has at least 2/5 weight on the three-step term and propagates A_n/F_n<=(5n+6)/12 from n=2,3,4. Conditioning on the first inspected vertex gives the greedy mean recurrence and the stated exponential generating numerator over 2(1-x)^2 in its ordinary generating function. Extending the coefficient sum to infinity gives L_n as stated; the n+1 term is zero and from n+2 onward the magnitudes decrease, giving error at most 2^(n+1)/(n+2)!. The partial series for e^2 gives 2327/315, so the lower gap above the flat upper bound for n>=13 exceeds (437n-5670)/27924, greater than the tail error. The exact finite differences through 12 were independently reproduced, including the zeros at 1,2,4 and positives elsewhere; independent permutation enumeration through 8 corroborated the greedy recurrence. Replay files are /workspace/branches/e1fc8654-973b-4293-a3b8-decb64651659/independent_check.py and independent_check.txt. Frozen check.py was inspected, not executed. Finally 1-x^2-x^3 has only its real simple root rho on the smallest-modulus circle, by equality in the triangle inequality and coprime exponents. With local factor rho^2(2+3rho)(1-x/rho), the simple/double pole coefficient ratio yields the stated flat slope and bounded remainder. Subtracting the greedy slope gives delta about 0.0208367697190 and the uniform linear lower bound also implies positivity.

## originality

FAIL

A closely preceding primary theorem on the identical path laws proves stronger all-size stochastic dominance. Its strict auxiliary likelihood-ratio comparison, together with the elementary support calculation, also implies the advertised exact equality set. The residual extensive gap is a direct difference of individual density formulas, not a new independent comparison theorem.

## value

FAIL

The finite comparison is a natural question and the frozen record provides a short independent proof of the mean statement. But as a claimed new scientific result it is strictly weaker than the existing all-path distributional comparison, with its equality set already implied by the prior argument. The elementary density difference and finite base values do not isolate a substantially new question or strengthen that comparison; no distinct valuable repaired claim is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
