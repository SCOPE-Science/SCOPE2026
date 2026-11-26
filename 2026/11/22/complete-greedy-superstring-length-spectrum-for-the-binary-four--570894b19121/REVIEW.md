# Independent mathematical audit

## correctness

PASS

The frozen proof does not establish the upper bound: an overlap of length greater than four need not equate the last four letters of the first string to the first four of the second (e.g. 011001 -> 110011 has overlap five with different boundary four-mers). Repaired RESULT.md establishes the missing invariant for all reachable states. Starting substring-free, any newly contained third word would have to cross both copy boundaries at a maximum-overlap merge and give a strictly longer overlap, impossible. The reverse containment would imply a previous containment. An overlap from or to the new component longer than the corresponding terminal or initial copy would also give a previous containment; shorter overlaps already occurred with the original copy. Hence the maximum never increases from its initial bound of three, and original endpoint four-mers indeed determine every overlap. The state DP takes every ordered maximum-overlap merge, with no omissions at zero, and combines bitsets of additional savings; the head and tail labels remain unique across disjoint components. The independently written `python3 /workspace/repairs/2/spectrum_replay.py 16 <frozen witnesses.txt>` ran to completion, caching 2,262,415 states including 208 terminals versus the frozen C++ count of 2,262,207 nonterminals. It returned exactly savings 37..45 and replayed nine literal histories against every then-current ordered-pair overlap, checking coverage and each length 19..27. A word of length L has at most L-3 four-windows, so the replayed length-19 witness is optimal. Frozen C++ and Python programs and recorded outputs were inspected, not executed. The repaired claim has the same exact spectrum; this is not a pass for the frozen proof.

## originality

PASS

The repaired claim credits the endpoint lemma, the standard de Bruijn optimum, and the all-subset census that already computes the maximal endpoint. The supported distinct contribution is the attainable set on the full input, notably all intermediate lengths with legal witnesses. Neither the established extrema nor the scalar exact minimization over future savings asserts there are no gaps.

## value

PASS

The complete read universe is canonical, and the distance from an optimal de Bruijn output to a bad tie resolution motivates asking which intermediate lengths can occur. Exact extrema alone could hide holes. The gapless spectrum with literal legal histories gives a reproducible fixed-input benchmark for comparing tie rules, without advancing a universal ratio claim. This value does not depend on passing off the known endpoint methodology or the scalar all-subset calculation as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
