# Independent mathematical audit

## correctness

PASS

Passes for the repaired scope in repairs/3/RESULT.md. The fixed-priority theorem was correct, but the frozen scope note extended its m-block counts to varying tie choices without distinguishing aligned from sliding blocks. With m=2 and u=(0,0), choose winner 1 at the initial tie and winner 2 at the tie two steps later. The sequence 1,2,2,1 has aligned blocks (1,2) and (2,1) but the middle length-two sliding block repeats 2. The repair keeps the tie-independent entry and aligned counts, and limits the sliding assertion to fixed priority. The proof counts exactly floor(u_i-delta) stack terms at or above delta+1 for every i, with a term exposed whenever any such term remains and a head at delta throughout. This certifies both strict nonentry before the total count and the exact state upon entry, including integer offsets and tau=0. After entry, a decremented head is below every not-yet-selected head within its aligned round, so every such block selects each index once. Fixed tie priority repeats the same order and hence gives all sliding blocks. The state returns after m steps; recurrence after d steps requires the integer win increment in each coordinate to equal d/m, proving the least period. The exact example u=(0,1) with lowest-index tie rule distinguishes strict-width entry from preperiod. The frozen checker was inspected, not run; its fixed-priority tests are unaffected by the repair and did not address the variable-tie extension.

## originality

PASS

The repaired theorem retains the natural exact threshold formula and the full all-real fixed-priority equal-share result, but does not claim newness for the update rule or the greedy stack device. Earlier results on initialized or projected orbits and general eventual period divisibility do not supply the exact unprojected entry time and state from arbitrary real scores. The known boundedness results do not count threshold selections. The scope repair makes no claim of novelty for the explicit variable-tie counterexample itself.

## value

PASS

The strict-width boundary for the uniform-share dynamics makes the upcoming schedule completely determined, and the exact first-hit time and state quantify recovery from arbitrary score perturbations, including those with arbitrarily long delays. The result is not just a boundedness guarantee or repetition from a standard initialization: it identifies the recovery state and proves the unprojected eventual least period for every real input. It separates entry from shortest preperiod and now specifies exactly what arbitrary tie handling preserves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
