# Independent mathematical audit

## correctness

PASS

Maximality on an open path is exactly independence plus domination: end gaps are at most one and successive chosen vertices are two or three apart. The resulting unsigned recurrence has parity word (1,1,0,0,1,0,1), with the defining triple returning at 7. Since each character contributes a sign, odd count gives only odd multipliers. For the even-count residues the signed recurrence tracks partial selections ending at j and W_n=F_{n-1}+F_n. Independently multiplying e=(1,1,0) on the right by A_+, A_-, then five A_+ gives (1,1,1), (1,0,-1), (0,0,1), (0,1,0), (1,0,0), (0,1,1), and e; this verifies invariance in the correct reverse order for the appended signs. Direct independence and domination tests on binary words give (total count, count containing the specified vertex) = (2,1), (2,1), (4,2), (12,6) at lengths 2, 3, 5, 9 respectively, certifying the four seeds. The block applies from length 3 on, and the n=2 seed is handled separately. At n=1 the multipliers are ±1. Exact Walsh diagonalization gives the stated result over C or R. The frozen checker was read, not executed; the finite checks are not used to prove periodicity or the extension identity.

## originality

FAIL

A distinct published-corpus record, 294497a01d79, already states and proves the same all-length criterion for n≥2 and constructs witnesses for precisely the same residues. The n=1 addition follows immediately from the single point support. The difference between seven-step preservation and seven-step negation is a transfer variant, not a new classification or existence theorem. This is a coverage decision, not an inference of priority from a catalogue date.

## value

FAIL

An all-length Walsh-zero classification with constructive witnesses would be worthwhile if unknown. It is already established in this form, with a different exact seven-sign transfer supplying all witnesses. The n=1 check is immediate, and a replacement block that makes the signed value equal rather than opposite does not supply an independently motivated invariant, new spectral classification, or useful unresolved consequence in this record. No surviving repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
