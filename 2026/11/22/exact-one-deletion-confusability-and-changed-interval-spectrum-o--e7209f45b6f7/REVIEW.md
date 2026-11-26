# Independent mathematical audit

## correctness

PASS

For words x,y with matched deletions at p<r respectively, equality of the reads gives agreement outside [p,r] and y_k=x_(k+1) for p<=k<r. Restriction to the first/last disagreement interval [i,j] gives the same relation there and deleting i,j reproduces the common read; exchanging word order gives the other mode. Equal deletion positions give just i=j. For a one-position difference there are binom(q,2) unordered choices. For L>=2, choosing the x block and the final y symbol gives q(q-1)^L ordered left-shift choices; the first mismatch follows from the adjacent-unequal rule, and the last symbol is any of q-1 choices different from x_j. Both shifts are possible exactly for the two opposite phases of an alternating two-symbol block, so subtract q(q-1)/2 for each boundary extension. A nonempty common prefix or suffix must avoid two distinct endpoint letters at its inner end, giving C_t=(q-2)(q-1)^(t-1), independently. Multiplying by C_a C_b and summing via C(z)=(1-z)/(1-(q-1)z) gives the stated generating function and its polynomial-times-geometric coefficients. At n=1 the graph is complete, and q=2 has just the two alternating words joined by one edge for every n. Dividing twice the edge count by q(q-1)^(n-1) gives the stated degree; the independent-set lower bound follows by averaging 1/(degree+1) from a random vertex ordering and rounding up. Fresh direct deletion enumeration matched every cell and total/GF coefficient in 24 (q,n) cases, including the degenerate boundaries. Replay: python3 /workspace/branches/88fa4e85-19d0-4519-85dd-efb346f3094c/record3_check.py.

## originality

PASS

The supported distinct contribution is the exact location-resolved edge law, and hence exact total, for the adjacent-unequal linear language with nonempty one-deletion overlap. Prior work covers the graph framework and alternating double-overlap structure; the audit does not credit those as new. No inspected statement supplies the single-overlap portion and the whole span law in this language.

## value

PASS

The cap-one source is a natural constrained language, and single-deletion collisions are its actual pairwise decoding obstructions, unlike ordinary shift edges or two-read ambiguity. The location-resolved invariant reveals how boundary positions suppress collisions, quantifies graph density exactly, and yields an explicit code-size guarantee without claiming sharpness. Counting all locations and lengths with a structural overlap correction is more informative than a finite case count or the known alternating subclass alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
