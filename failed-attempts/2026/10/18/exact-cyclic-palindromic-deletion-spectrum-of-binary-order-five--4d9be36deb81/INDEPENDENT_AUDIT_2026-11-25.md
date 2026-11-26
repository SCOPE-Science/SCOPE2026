# Independent mathematical audit

## correctness

PASS

The admissible objects are rotation classes, each uniquely rooted at its sole 00000. The two pairings at each of 16 vertices produce permutations of the 32 edges, and precisely the single-orbit permutations represent de Bruijn cycles. Independently, run python3 /workspace/replay/debruijn_review.py: binary extension with no repeated five-window and the four closing-window checks exhausts the same 2048 distinct roots. On doubled words a rolling deletion recurrence and a bit-parallel reversal-LCS implementation agreed on all 65,536 individual cuts; the former recurrence is justified by deleting at least one unequal end, while equal ends can be retained in some optimum by replacing the matching mate of a retained end, or by adding both if both are omitted. The independent run agrees with all CSV rows, both endpoint witnesses, the histogram 76,114,1380,286,192 at levels 25–29, moments 13925/512 and 178215/262144, and the exact reversal/complement subtotals. The frozen verify.py tests equality of maxima, not equality cut by cut, despite the broad trajectory of its documentation; the independent run checked the latter as well. No larger order is tested or inferred.

## originality

FAIL

Distinctness of this standalone claim is not established: a different Resultary record contains its entire cyclewise statistic, all five frequencies by marginalization, and numbers that force every stated orbit subtotal. The catalogue dates alone do not establish relative priority; this is demonstrated mathematical coverage, not a claim that one record predated or copied the other. There is no surviving substantive remainder of the frozen finding to repair.

## value

FAIL

The constrained circular-palindrome distribution is a motivated finite invariant, and the exact replay is useful corroboration. But as a separate finding all its precise numerical information, including the orbit refinement and cyclewise data, is a mechanical extraction from the checked joint census. No additional mathematical invariant or classification is established here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
