# Scientific review

## Correctness — PASS
A trajectory-residue argument shows that some state must traverse at least \(2m-1\) advancing defect commands, with \(2m-1\) rotations between successive advancing commands. The forbidden \(aaa\) factor forces at least \(m-1\) extra defect commands per intervening segment. This supplies the all-state lower bound. The displayed \(2m-2\)-block witness has exactly that length, contains no forbidden factor, and provably alternates between explicit odd/even image sets until it reaches the singleton \(\{0\}\). The standalone program independently checks the construction through 100 states and exact shortest paths for even state counts through 16. The all-parameter claim relies on the induction, not a finite extrapolation.

## Originality — PASS, qualified
The underlying unrestricted Černý threshold is classical and fully credited. A previously published mandatory-scattered-subsequence theorem gives a strong necessary condition on reset words; the present result uses a constrained-run counting argument and a nontrivial parity-sensitive construction to attain the new lower bound. Hoffmann's primary paper on constrained synchronization proves polynomial-time existence decisions, not an explicit optimal constrained length for this automaton family. The closest rank-threshold and weighted-cost results do not bound the longest consecutive run of a specified command. published-finding corpus searches under constraint aliases, exact formulas and equivalent word restrictions did not find a statement covering this theorem. Residual risk: a nonindexed older calculation for this exact family and regular input language.

## Mathematical value — PASS
A maximum consecutive-command limit is a natural control restriction on a synchronization sequence; the exact minimum reset latency, rather than mere existence, is the required invariant. The result demonstrates a genuine asymptotic \(3/2\) multiplicative latency cost in a canonical extremal automaton and supplies a uniform construction at every even state count. It is not a one-off machine census, a trivial alphabet relabeling or a routine one-parameter increment.

## Limits
Only the even-state family and the exact no-`aaa` input constraint are settled. Odd-state optimal lengths, other constraints, and counts of all optimum words remain open in this result. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
