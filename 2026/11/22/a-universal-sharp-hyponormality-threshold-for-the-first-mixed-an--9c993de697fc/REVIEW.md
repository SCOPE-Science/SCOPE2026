# Independent mathematical audit

## correctness

PASS

For q=α+1>0 the ratio of consecutive squared monomial norms is x_n=(n+1)/(n+q+1). With S=T_z, the second term is S*²S, giving the backward coefficient x_n√x_{n-1} and zero at n=0. Expanding the commutator gives diagonal |a|²A_n+|b|²B_n and distance-two entries with modulus |ab|C_n as stated. The diagonal bound can be verified independently of the polynomial certificate by the identity -B_n=x_n²(A_n+A_{n+1})+x_n x_{n+1}A_{n+1}. All x_n lie strictly between 0 and 1 and A_n>0 decreases, including A₀ with x_{-1}=0. Thus -B_n<3A_n, while C_n+C_{n-2}<2A_n, with the missing negative-index entries taken as zero. At t=|a|/|b|≥3 the row margin is greater than |b|²A_n(t-3)(t+1), giving nonnegative quadratic form by 2|v_n v_{n+2}|≤|v_n|²+|v_{n+2}|² and density; boundedness follows from bounded symbols. In particular the proof includes equality, not a claim of a uniform spectral gap. If b=0 the commutator is the nonnegative diagonal |a|²A_n. For b≠0 the limits (n²/q)(A_n,B_n,C_n)=(1,-3,1) follow from the same identities. On L consecutive points of one parity in a far-tail block, phases can make all off-diagonal contributions nonpositive and attain the lower sign. The rescaled form tends to L(t-3)(t+1)+2t, negative for large fixed L when t<3; t=0 needs no phase choice. This proves exact necessity for each α, including -1<α<0, and all complex a,b. Replay: RESULT.md §§1–3; CHECK.py was inspected, not executed. Its finite rational and floating checks do not replace the tail or all-weight proof.

## originality

PASS

The weighted commutator framework and unweighted opposite-shift comparison precede the record. The distinct supported claim is the sharp iff threshold, with equality, for the specific symbol throughout the power-weighted analytic scale α>-1. This is not a claim of a new commutator method or applicability to arbitrary weights.

## value

PASS

The opposite-step pair is a natural minimal case in which mixed terms make the diagonal test inadequate. The exact cutoff, including equality and negative Bergman exponents, is useful as a benchmark for necessary tests on nonharmonic symbols; it separates a genuine phase-coherent obstruction from scalar moment estimates. It is a narrow classification, not a general solution of weighted Toeplitz hyponormality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
