# First four attainable nonzero cycle lengths of a ternary quadratic lag recurrence

## Finding

Let \(k\geq 2\) be an integer, and let \((x_t)_{t\in\mathbb Z}\) be a nonzero, periodic sequence in \(\mathbb F_3\) satisfying
\[
x_t=x_{t-1}+x_{t-k}^{2}\pmod 3\qquad(t\in\mathbb Z).
\]
If its least positive period \(N\) is at most \(22\), then \(N\in\{4,9,19,22\}\). For each \(N\) in this set, there are precisely two residue classes of \(k\pmod N\) admitting a nonzero orbit of least period \(N\). In each admissible class there is **exactly one orbit up to cyclic rotation**, given by the following table; no other choices exist.

| \(N\) | \(k\pmod N\) | One period of the orbit (consecutive ternary digits) |
| ---: | ---: | :--- |
| 4 | 2 | `1120` |
| 4 | 3 | `1220` |
| 9 | 4 | `122201200` |
| 9 | 6 | `120111200` |
| 19 | 5 | `1222201201120012000` |
| 19 | 15 | `1200122012011112000` |
| 22 | 8 | `1222011120122012001200` |
| 22 | 15 | `1201120122201112001200` |

Consequently, every nonzero *eventual* cycle of the recurrence with least period \(N\leq22\), from **any** initial block, has one of the listed shapes. This says nothing about which orbit is entered from a particular initial block.

## Assumptions and scope

All arithmetic is in \(\mathbb F_3\), with the displayed digit words using representatives \(0,1,2\). The delay \(k\) is any integer at least \(2\), and the initial values are unrestricted. The identically zero sequence is a separate solution of least period one and is excluded from the claim. Two periodic words are considered equivalent exactly when one is a cyclic rotation of the other. No classification is asserted for least periods greater than \(22\).

## Proof

First, any nonzero periodic orbit contains a zero. Indeed, if none of its entries vanished, then every square \(x_{t-k}^2\) would equal \(1\), implying \(x_t=x_{t-1}+1\). This progression cycles through all three residues and thus contains zero, a contradiction.

Fix a hypothetical orbit of least period \(N\), where \(1\leq N\leq22\), and rotate its entries so that \(x_{N-1}=0\). Set \(b_j=1\) when \(x_j\neq0\) and \(b_j=0\) otherwise, for \(0\leq j<N\), periodically extended. The recurrence is equivalent to
\[
x_j-x_{j-1}=b_{j-k}\pmod3.
\]
Summing once around the period gives \(\sum_{j=0}^{N-1}b_j\equiv0\pmod3\). Since \(x_{N-1}=0\), every entry of a proposed orbit is *uniquely determined* by its binary mask and the delay residue \(r=k\bmod N\):
\[
x_j\equiv\sum_{i=0}^{j}b_{i-r}\pmod3\qquad(0\leq j<N),
\]
with subscripts of \(b\) taken modulo \(N\). Conversely, such a mask represents an orbit precisely when \(b_j=[x_j\neq0]\) for all \(j\). There is no untested choice of an initial ternary value because the rotation fixes the endpoint to zero.

It remains to perform a finite exhaustive test over each \(N\in\{1,\ldots,22\}\), every \(r\in\{0,\ldots,N-1\}\), and all \(2^N-1\) nonzero masks. Masks whose number of ones is not divisible by three are ruled out by the preceding identity. For each remaining mask, reconstruct the entire ternary word by the displayed sum, check the mask identity at every position, and discard words having a smaller period \(d\mid N\). The provided `verify_short_cycles.cpp` directly implements these necessary-and-sufficient criteria using exact integer arithmetic. It also checks the original quadratic recurrence for each survivor, proves every survivor is a rotation of the listed word, and verifies exact counts of the zero-ended rotations: \(1,1,3,3,7,7,7,7\), respectively. In total it examines \(176{,}160{,}517\) nonzero mask/period/lag triples; none is omitted by sampling or by a search cutoff within the claimed range.

Each listed word has exactly as many zero-ended cyclic rotations as the count recorded for its row, so the comparison establishes **one** orbit per admissible delay class, not merely existence. The direct recurrence checks establish existence. A nonzero periodic word contains a zero, hence some rotation is covered by the exhaustive test. This proves both directions of the classification. \(\square\)

## Verification

Compile and execute `verify_short_cycles.cpp` with a C++17 compiler, for example:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_short_cycles.cpp -o short_cycles
./short_cycles
```

The program raises an error if any period or lag outside the table has an orbit, if an orbit lies outside a listed rotation class, or if a listed orbit has an incorrect multiplicity. Its final successful line begins `VERIFY_OK periods=1..22`. An independent, differently organized brute-force check enumerating ternary words directly for periods through \(11\) is supplied as `verify_small_direct.py` (Python standard library only).

## Relationship to prior work

Steven Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess* (arXiv:2610.34300, first posted 2026-10-25), Section 4, proves that the distinguished seed cannot have a nonzero eventual period below four and classifies its period-four possibilities. Its numerical table includes distinguished-seed periods \(9\), \(19\), and \(22\) at particular delays, but does not give the all-initial-condition short-cycle spectrum, the excluded least periods, or the uniqueness-up-to-rotation result for those lengths. The earlier *Periodicity in Sequences Mod 3* (Finch, 2002) and OEIS A112683 likewise tabulate periods for a **fixed** initial seed rather than all periodic solutions. The period-four rows above are already contained in Finch's classification; the contribution here is the complete all-seed spectrum through the first four attainable lengths and the additional orbit uniqueness claims.

## Limitations

The result is a finite exact classification of primitive cycle words; it is **not** an asymptotic theorem or a statement about all possible cycle lengths. Its finite certificate must be run to validate the exhaustion. It does not determine basins of attraction, eventual periods of the distinguished initial seed at arbitrary delays, or the spectrum beyond length \(22\). The first four observed lengths in the cited seed data were known; the complete all-initial-state exclusion and uniqueness are the proposed new assertions. Priority in unindexed or partially inaccessible older literature has not been independently ruled out.

## References

- S. Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1, posted 2026-10-25, Sections 1 and 4 and addenda. https://arxiv.org/html/2610.34300v1
- S. Finch, *Periodicity in Sequences Mod 3*, 2002, pages 1–4. https://www.mit.edu/~sfinch/seqmod3.pdf
- OEIS A112683, *Period of a ternary quadratic recurrence with a distinguished initial block*. https://oeis.org/A112683
- V. Miller, *Finch's sequence over the finite field of three elements*, MathOverflow (2010), https://mathoverflow.net/questions/50678/finchs-sequence-over-mathbbf-3
- J. Cassaigne and S. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics 4 (1995), 49–60, DOI 10.1080/10586458.1995.10504307 (a different ternary recurrence in Section 3).
