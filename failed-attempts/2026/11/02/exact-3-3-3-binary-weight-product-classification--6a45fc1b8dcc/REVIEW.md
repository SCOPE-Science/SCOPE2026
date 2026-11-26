# Independent mathematical audit

## correctness

PASS

Kaneko–Stoll Thm. 2.2 assumes both factor weights at least two, their maximum at least three, odd positive factors, and product weight three. The proof text should retain the first condition when paraphrasing the general theorem, but the actual 3,3 application satisfies it and gives the strict global cutoff 2^23. Every admissible product and factor is then of the form 1+2^i+2^j with 1≤i<j≤22. The independent integer replay `python3 /workspace/replay_binary_weight_3.py` built the 231-element set, excluded a>sqrt(2^23−1), bounded b by floor((2^23−1)/a), and tested all 3672 remaining unordered pairs including equal factors. Membership in the set returned precisely (7,7,49), (7,19,133), (7,37,259), (11,35,385), (13,21,273), (21,49,1029). Thus 1029 is the unique maximum. Exhaustion relies on the inspected published theorem, not on a finite search alone.

## originality

FAIL

A distinct indexed Resultary record explicitly gives the identical six unordered pairs, products, cutoff and bound-plus-exhaustion approach. The sharp maximum and unique attaining pair follow immediately from its exact list. That record has an earlier catalogue date, but direct identity of content is decisive without checking first-online chronology. No genuinely distinct surviving claim is established.

## value

FAIL

The symmetric three-bit classification is a natural invariant and would be useful if not already supplied in precisely the same form. The frozen record adds no new list entry, extension, sharper bound, or structural method to the exact earlier classification; another bounded enumeration alone is redundant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
