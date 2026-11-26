# Independent mathematical audit

## correctness

PASS

At a carry starting at digit i the change in f is its suffix sum S_i. For first nonzero coefficient at r, any carry with i>r has a freely varying digit x_r; exactly a 1/p fraction start at zero if S_i=0, and none qualify otherwise. At the remaining carry positions, all digits after r are terminal and the start values of x_r run once per earlier-digit choice through the p residues, including the terminal value at the cyclic higher carry. Since all earlier coefficients vanish, this gives p^(r-1) zero pairs if S_r=0, independent of the intercept. Suffix sums are independent coordinates subject to S_r!=S_(r+1); counting their allowed zero/nonzero configurations gives the factored polynomial. With H_m the nonconstant-word polynomial divided by p(p-1), H_1=1 and H_m=(p-1+u^((p-1)p^(m-2)))H_(m-1)+u^(p^(m-2)). This verifies the disjoint supports, maximal proper exponent with normalized coefficient 1, and constant coefficient (p-1)^(m-1). Adding constants gives all stated counts and weights. Independent exact check `python /workspace/checks.py 2` recovers the complete distributions from direct cyclic endpoint histograms for (p,m)=(3,2),(3,3),(3,4),(5,2),(5,3),(7,2). The proof covers arbitrary odd prime and dimension; those finite tests do not.

## originality

FAIL

The minimum distance already follows from Pan–Ling–Liu (2023), Theorem 4.6. A distinct indexed theorem on the same digit-ordered code determines the complete distribution for all cyclic window widths; its b=2 specialization gives every claimed multiplicity and even reduces algebraically to the frozen recurrence. This material coverage is not a priority finding against the frozen Oct. 18 date-key; the indexed all-width record has a Nov. 8 date-key and no derivation relationship is asserted.

## value

FAIL

The lexicographic cyclic multiplicity question is well-motivated, but this claim supplies no independently needed exact invariant beyond the indexed wider-window classification. The attractive factorization simplifies its presentation at b=2, but it reduces by elementary polynomial algebra to that classification and no separate mathematical gain is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
