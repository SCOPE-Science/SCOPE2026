# Independent mathematical audit

## correctness

PASS

Expand W_n(S)=sum_{T subset S}(-2)^|T| F_n(T) where F counts admissible graphs containing fixed edge set T. Mod 16 only |T|<=3 matters. For n=7 the nine small edge-pattern degree/isomorphism types cover exactly 1+21+210+1330=1562 patterns. Enumerated exact supergraph counts are (1014888,581464,335060,320432,194284,185444,172568,177322,168096) with the nine specified orbit multiplicities and sufficient divisibility: empty 8 mod16, one-edge 0 mod8, two-edge 0 mod4, three-edge 0 mod2. Hence every W7≡8 mod16, and signed witness mask 2396 has W=8; analogous n6 forced-edge counts and mask107=-8. For n4,5 one-edge even and total 2 mod4; n3 sole triangle. Independent C++ code computed membership by deletion-connectivity, all 2^21 Walsh coefficients, all 1562 incidence counts via full superset zeta, all witnesses, parseval, min, zero count. Output exactly 1014888 graphs, 0 zero multipliers, min8, sum squares 2128374398976; this is exhaustive FINITE enumeration, not a theorem for n>=8. Fourier diagonalization of counting convolution gives exact inverse norm and condition number.

## originality

PASS

Known enumerations give unsigned counts and biconnected recursions; the exact 2-adic ALL-frequency signed edge Walsh obstruction is a different invariant. Cross-check of primary literature and Resultary did not identify a prior all-frequency statement. Best-of-knowledge PASS with narrow historically searchable finite scope.

## value

PASS

An exact finite all-character nonvanishing certificate at 21 edge coordinates is a natural recoverability threshold, not a random subfamily. Nine low-edge orbit moments explain an otherwise opaque exhaustive Fourier result and give sharp inverse norm/condition number at the first large biconnected example; this nontrivial structural finite cutoff is mathematically useful independent of an n>=8 theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
