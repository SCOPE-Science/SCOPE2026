# Independent mathematical audit

## correctness

PASS

Lucas digit factorization applied inside the Franel sum gives digit residues (1,2,0,1,1) mod 5 and hence exactly 4^r allowed starts below 5^r. Independently reconstructed all forty carry weight sums by excluding the three forbidden residues of the input digit (2, 2-a-c1 and 2-b-c2 mod 5) and then taking the carries. The zero-digit equations give the claimed tail vector, including q(011)=7/12 and q(111)=1/3. Its boundary is the true infinite acceptance probability: the doubling carry clears on the first zero digit, and after that an addition carry can persist only through consecutive input 4s, with vanishing probability. The tail vector is bounded by w/3; backward induction through the digits by sum of successor weights <=4w preserves this bound. Starting zeros keep 000, and the first nonzero digit has precisely two accepted transitions to states of weight two and zero-tail acceptance 2/3. Single-nonzero-digit shifts therefore achieve 1/3. Before a second nonzero digit the surviving support lies in 000 and the four first-transition states; digits 1–3 give strict weight loss there. For a second digit 4, 000 loses strictly and each other possible state reaches 111 with positive probability, where equality can only maintain 111 on digit 4 (with positive probability); a later non-4 digit exists because h is finite and forces strict loss on that branch. This propagates back to strictness in the total overlap. For 5^r>2h all carries leaving the prefix have t=0 and the unwrapped finite integers have only the extra digits 0 or 1, which are allowed. Thus the finite normalized count agrees there with finite-prefix survival under uniformly sampled allowed digits, and continuity of decreasing events identifies the limit with the infinite survival probability. The counting bound 4^r gives ordinary density zero by trapping between successive powers of five. Read RESULT.md and the frozen verification files; ran only the independent bounded replay `python -B /workspace/independent_replay.py 1` for the full finite certificate and its boundary/equality transitions. No inference about all h is taken from a tested range of shifts.

## originality

PASS

The supported distinct theorem is the complete sharp fixed-integer shift bound for the unsigned threefold overlap of the specified base-five support and its single-nonzero-digit equality cases. The forbidden-digit description, Lucas computation and general carry-automaton methods are not claimed as new. The available same-object catalogue statements test different observables; the retrieved broader primary leads do not establish equivalent coverage. This is a bounded best-of-knowledge decision, not a priority certification.

## value

PASS

Since the ordinary density vanishes, progression counts relative to the natural sparse Franel support are a useful invariant not visible through density or signed pair overlaps. The sharp maximum and full classification tell which shifts preserve the most simultaneous membership, uniformly over all steps; in particular, a second nonzero digit defeats equality even across arbitrarily many intervening zeros. This is more than applying Lucas digit membership or tallying a finite list of shifts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
