# Independent mathematical audit

## correctness

PASS

The only strict order comparisons are root-to-leaf. Write A={i:rRi}, E={i:iRr}, and a=1 for rRr. FC forces every leaf row to include A and, if a=1, to be nonempty. BC makes each E row full and, if a=1, requires every leaf column to be nonempty. If A intersects E, transitivity forces the root loop and then A=E=L, the universal relation. Otherwise an A row is exactly A by transitivity from the root, and a C row, for C=L minus (A union E), cannot hit E or the root; it is A plus its row of S on C. Conversely compositions in a C row either stay in C, where S must be transitive, or end in A, whose rows add nothing. The root, A and E rows also preserve transitivity directly. For a=0 and fixed C the remaining labels can be distributed between A and E in 2^{m-c} ways. With a=1 and c<m, the two all-one-side assignments require exactly row or column nonemptiness on S and give 2U_c, and the others give (2^{m-c}-2)T_c. With c=m the loop imposes both conditions (V_m); without it one has T_m. The universal exception adds exactly one. Summing gives the stated expression for m>=1. Independent full star scans for m=0 through 4 obtained 2,8,38,379,7182; set equality with the normal form was checked for m=0 through 3. Independent exhaustive enumeration of T_c,U_c,V_c through c=5 followed by formula substitution gave 238810 at m=5. The latter is not a direct scan of all six-world star relations.

## originality

FAIL

The distinct published Resultary record d6d8ca79c791 (2026-10-18 UTC) gives an equivalent normal form and all-size formula for the same labelled rooted carrier, optional root loop, transitivity and exact two quantified laws. The earlier case-split sum algebraically equals this finding's formula; the extra explicit m=5 evaluation is a direct substitution. This is verified mathematical coverage, not an inference from titles, index dates, or small equal counts, and makes no historical attribution claim.

## value

FAIL

A structural classification for these frames is worthwhile in itself, but this finding does not add such a classification beyond the existing one. The compact regrouping of the root-loop census adds no new invariant or mathematical range. Its only extra tabulated star size is derived by substituting auxiliary counts into the existing formula, with no independently motivated cutoff or new finite phenomenon at five leaves. The verified finite scans are useful regression evidence, not a distinct scientific finding in this record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
