# Independent mathematical audit

## correctness

PASS

Every start belongs to one residue modulo L. Outside the possible multiple of L the letters are fixed by the valuations of distances to that multiple. At the multiple, the conditional valuation has geometric law modulo q, so the possible integer masses on denominator L(2^q−1) are 1,2,…,2^(q−1) in powers of two; a missing center has mass D=2^q−1. This also proves density existence, since each center-letter condition is a disjoint union of valuation classes with a uniformly vanishing tail. For two phases whose centers differ with valuation t≤log₂L−3, the congruence witness modulo 2^(t+2) in the window has valuations t and t+1 and cannot be either center. Phases can merge only within the four centers sharing a residue modulo M=L/4. In each quartet the distinguished letters A=(log₂L−2) mod q and B=(log₂L−1) mod q have masses 2 and 1. With two visible centers the AA overlap has mass 4, and BA and AB each have 1+D=2^q. With three visible centers the first and third templates merge at BAB with mass 2 while the second merges with the missing fourth at ABA with mass 2^q. With four visible centers, only the opposite template pairs merge, producing two overlaps of mass 2. Counting the untouched masses gives exactly the tables; for q=2 some numerical mass levels coincide, not the symbols A and B themselves (the explanatory sentence in RESULT.md line 61 is misleading on that point). Counting how many quartets have two, three or four visible centers gives a, b and c. For n=1 the geometric valuation law gives the one-letter frequencies; the n=2 templates intersect only at 00 with mass 2. The binary equifrequency criterion follows because the second level vanishes exactly at n=L for n≥3 and n=2 is equifrequent. The recorded formulas are true.

## originality

FAIL

The entire spectrum, including its multiplicities for every q, is a direct consequence of the known factor-multiplicity scaling theorem of Frid for marked uniform substitutions, applied to generalized Thue–Morse, and the equal-mass finite difference quotient. Only the length-2, -3 and -4 seed census is needed; those lengths do not constitute a distinct all-length result. The frozen claim that generalized Thue–Morse is an unrelated family misses this exact relation.

## value

FAIL

The spectrum is a natural invariant and the quartet proof is coherent, but the stated advance is entirely mechanically implied by the earlier group theorem for the difference quotient. Its small seed comparisons and the boundary restatement at n=3L/4 do not leave a separate valuable exact result. No genuinely distinct surviving claim is made by the frozen statement, so no repair is submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
