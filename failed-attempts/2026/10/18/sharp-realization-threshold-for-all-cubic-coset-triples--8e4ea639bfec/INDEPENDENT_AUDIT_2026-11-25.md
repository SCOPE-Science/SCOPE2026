# Independent mathematical audit

## correctness

FAIL

RESULT.md lines 8–11 assert the pointwise equivalence full word support iff p≥307. The converse is false: p=73 is eligible and has all 27 words, as does p=97. The exact exception list on lines 12–16 is correct and contradicts the displayed equivalence. The surviving true reading is a sharp eventual cutoff among eligible primes, not a pointwise characterization by an inequality. Independently replayed all 74 eligible primes below 900 with the cubic-character power map and a subgroup/coset cross-check, enumerating every x from 1 to p−3. See /workspace/branches/0aa011e7-3567-48d5-a68e-5f360d9d1731/independent_cubic_words.py (run with Python 3) and independent_cubic_words.out. Output lines 2–3 show p=73 was tested and is not exceptional; lines 14–22 give the unique absent words (2,0,2) at 151 and 163, (0,0,0) at 283, and full support at 307. Independently checked the infinite part: the character expansion over admissible starts contributes p−3 in support size zero; for nonzero support size t the polynomial is not a cube, and restriction costs at most 3−t in addition to (t−1)sqrt(p), with the complete size-one sum zero. The multiplicities 6,12,8 give the lower bound p−28sqrt(p)−27, increasing and positive from 900. Thus the verified computation and proof give the tail statement and exact exceptional set, not the stated biconditional. Frozen VERIFICATION.md and verify.py were inspected, not executed.

## originality

FAIL

The corrected tail theorem, the exact thirteen-prime exceptional set and the proposed additional mixed-word observations are all already covered in a distinct indexed Resultary record, 5a92ab0389ae. The 1962 theorem additionally covers the entire all-cube subproblem. This is equivalent statement coverage in the available record set, not an inference about historical priority from record dates. Fixing the biconditional would not leave a supported distinct claim, so no repaired finding is submitted.

## value

FAIL

The exact all-word cutoff is a worthwhile refinement of the classical single-word question, but the supplied work adds no scientifically distinct cutoff, obstruction or classification beyond the verified indexed result. The invalid pointwise iff cannot supply value, and its correction would duplicate the available exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
