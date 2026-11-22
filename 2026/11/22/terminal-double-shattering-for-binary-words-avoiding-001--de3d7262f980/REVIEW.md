# Scientific review

**Correctness (PASS).** The 001 constraint forces every bit after two consecutive zeros to be zero. Thus any queried adjacent pair with a later queried position defeats shattering by the 00...1 trace. Otherwise all unqueried positions may be set to one, unless the unique final queried adjacent pair is 00, when its later suffix is set to zero. The supports partition uniquely into independent sets and a final pair preceded by an independent set. Exact path-polynomial counting and VC rank follow. A wholly independent oracle reproduced all 8,190 support decisions for n=1..12.

**Originality (PASS, qualified).** The all-word forbidden-001 shattering criterion and enumerator differ both from the published forbidden-000/111 VC language theorem and the published forbidden-001 Walsh-stability theorem; the former analyzes another forbidden language, and the latter the same language with Fourier rather than trace invariants. Johnson 2021 studies substrings of a single word, not all words avoiding a fixed factor. The exact all-support assertion is not covered by these inspected statements; historical priority is not certified.

**Value (PASS).** A single forbidden substring defines a canonical regular language and a basic class for VC geometry of constrained words. The theorem supplies complete membership of every possible shattered coordinate support, an exact face series and a structural terminal-double rule, not merely an asymptotic VC bound or a numerical exercise.

Closest sources: Hunter R. Johnson, *Binary strings of finite VC dimension* (arXiv:2101.06490); *A regular shattering complex for binary words with no monochromatic triple*; *A three-phase sharp Walsh stability law for binary words avoiding 001*. No online dimension, cyclic variant or unrestricted forbidden-substring extension is claimed. Unindexed equivalences remain a priority risk.

Self-review: passed. Independent audit: not yet performed.
