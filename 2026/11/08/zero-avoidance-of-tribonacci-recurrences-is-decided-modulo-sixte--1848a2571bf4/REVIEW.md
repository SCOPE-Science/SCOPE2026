# Independent mathematical audit

## correctness

PASS

The determinant-one companion matrix makes every finite state purely periodic. Independently enumerated all 4096 states modulo 16 into primitive cycles: 32 zero-free cycles of length 16, 24 zero-free cycles of length 32 and 72 zero-containing cycles of length 32. Every zero-containing primitive cycle has a zero first coordinate with second coordinate nonzero modulo 4. Independent integer matrix multiplication verified T^16 and (T^16-I)/8 mod4. The matrix lifting induction T^(2^k)=I+2^(k-1)B_k, B_k mod4 constant, flips the next zero-coordinate bit by a shift T^(2^(k+1)) if the second coordinate is odd, otherwise T^(2^k) if 2 modulo4; lower bits and the mod4 seed persist. Hence precisely 1280*8^(r-4) primitive avoiders, plus imprimitive valuation decomposition and small bases P1=1,P2=8,P3=128, gives N_r formula. Bounded direct higher-power enumeration only corroborates the infinite lift.

## originality

PASS

Klaška proves fundamental modular period and matrix congruence results, but the actual zero-coordinate incidence class for all arbitrary initial triples and universal 1280/3584 mod16 criterion does not appear in the relevant primary theorem and examples examined. Bilu et al study p-adic zeros of a distinguished Tribonacci sequence, not the uniform state-space property quantified over all triples. A recurrence-orbit count database tabulates different statistics; exact orbit zero-hit classification appears distinct. Best-of-knowledge with possible disguised period-incidence table risk.

## value

PASS

Global zero avoidance of a natural reversible three-term recurrence over all dyadic moduli is a substantive p-adic recurrence invariant. The finite cutoff mod16 uniformly deciding infinite higher-power avoidance, and the exact 5/14 density, bridge exhaustive finite dynamics to a genuinely quantified infinite lifting theorem, beyond routine orbit counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
