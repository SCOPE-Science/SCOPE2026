# Self-review

## Correctness

**PASS.** The nonzero orbit must contain a zero: otherwise the recurrence increments by one everywhere and necessarily reaches zero. Rotating a zero to the terminal index removes any unknown initial value. A binary indicator mask has weight divisible by three and uniquely reconstructs the orbit by prefix sums. Checking mask compatibility and exact minimal period is both necessary and sufficient. The C++17 certificate exhausts every mask, period and delay class through the stated boundary, confirms precisely eight possible period/delay pairs, checks every survivor against the listed rotation class, and verifies the nonlinear equation directly. An independent direct ternary enumeration checks the smaller range through period eleven. The finite certificate provides no information beyond the claimed boundary.

## Originality

**PASS, qualified.** Finch's October 2026 source reports period-four structure and numerical periods of the specially seeded sequence; the complete all-seed primitive-orbit spectrum and unique phase class for each delay residue are not asserted there. The 2002 tables and OEIS cover the same distinguished seed, not all initial states. Relevant mathematical research-record searches identified unrelated low-period recurrence and coding-theoretic records, not an equivalent classification. The earlier Cassaigne–Finch 1995 paper concerns a different ternary recurrence; its full comparison is limited by imperfectly accessible historical text. Unindexed prior computations remain a priority risk. Numbers \(4,9,19,22\) individually were previously observed for special seeds and are not claimed as new.

## Mathematical value

**PASS.** The motivating recent work presents a still-mysterious nonlinear recurrence and a handful of particular seed periods. This result gives the first complete global period spectrum over *all* delays and seeds through the fourth realized primitive length: nine consecutive lengths from \(10\) to \(18\) are excluded (as are \(5\) to \(8\), \(20\), and \(21\)), and every occurring short orbit has a unique phase class. The exact boundary \(22\) is the fourth distinct observed attainable period in the source data; it is not an arbitrary cutoff selected to showcase an isolated answer. The theorem can serve as a tested boundary condition for studying basins and longer cycles. It does not purport to settle general-period conjectures.

## Closest literature and limitations

- Finch (2026), arXiv:2610.34300, Section 4: prior exact period-four result and individual seed data; does not cover the asserted global small-period spectrum.
- Finch (2002), *Periodicity in Sequences Mod 3*: prior distinguished-seed tables; not a global cycle classification.
- OEIS A112683: distinguished-seed periods only.
- Cassaigne–Finch (1995): different multi-lag recurrence; historical full-text access imperfect.

Unindexed-priority risk remains; the computation is certified only through period \(22\). Independent review has not taken place.

Self-review: passed. Independent audit: not yet performed.
