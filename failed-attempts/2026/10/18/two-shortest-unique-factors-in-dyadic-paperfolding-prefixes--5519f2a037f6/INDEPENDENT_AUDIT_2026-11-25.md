# Independent mathematical audit

## correctness

PASS

The theorem is correct. The frozen proof overstates the boundary translation: t'=16 can make a translated interval exceed the finite prefix if its right offset is positive. Restricting to t'=1,...,15 leaves all offsets of absolute value <q valid and the four parity/bit classes have sizes 3,4,4,4, so the claimed lower bound on repetitions follows unchanged. The same restriction handles unaligned length-(q+1) factors. Independently regenerated all 36 length-nine templates and verified their disjoint start residue sets; even-index decimation then proves the all-k alignment induction. In the 15 aligned starts the triple classes give singleton indices 11 and 12 only. Direct exhaustive counting verifies k=2, including the 60 length-five starts, and corroborates n=7..10. Replay: python3 /workspace/replay/finite_checks.py. The scientific rejection below is not a rejection of the statement's truth.

## originality

FAIL

A distinct published Resultary statement gives exact equivalent coverage of the entire finding, including both starting positions, under the complemented word and zero-based indexing. The visible matching record bears a later date: this establishes present statement-level coverage, not that the frozen work was derived from it, nor any priority or independence finding.

## value

FAIL

Determining the earliest unique scale in finite paperfolding prefixes is a natural occurrence-multiplicity question, and the proof has useful structural ideas. But the submitted narrow invariant and both start positions are already exactly covered in the inspected catalogue; no additional uncovered invariant is established by the finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
