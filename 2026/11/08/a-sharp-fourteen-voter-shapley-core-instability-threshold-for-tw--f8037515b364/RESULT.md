# A sharp fourteen-voter Shapley core-instability threshold for two-party PAV games

## Finding

**Theorem (exact first failure in two-party elections).** Let there be exactly two nonempty parties with \(a,b\ge1\) voters, and let \(n=a+b\). Each voter of a party approves all of that party's candidates and no others; the candidate sets are disjoint, and each has at least two candidates. With committee size \(k=2\), use harmonic proportional approval voting (PAV) to define the transferable-utility (TU) coalition game, where a coalition of size \(h\) can select at most \(\lfloor 2h/n\rfloor\) candidates.

The Shapley value belongs to the TU core for **every** such election with \(2\le n\le13\). For \(n=14\), it fails the TU-core constraints **exactly** when the party sizes are \(6\) and \(8\), up to exchanging parties. In the order \((a,b)=(6,8)\), the only violating coalition-composition type is \((s,t)=(6,1)\), with exact individual payoffs

\[
\phi_A=\frac{7127}{9009},\qquad \phi_B=\frac{6947}{6006},\qquad
\chi(6,1)-(6\phi_A+\phi_B)=\frac{83}{858}>0.
\]

This is the first **restricted-domain** failure, not the first arbitrary approval-profile failure: unrestricted Shapley TU-PAV instability was already exhibited by Chen and Hatschka (2026).

## Assumptions and scope

For \(j=0,1,2\), set harmonic weights \(H_0=0\), \(H_1=1\), \(H_2=3/2\). An agent's score for a committee containing \(j\) of their approved candidates is \(H_j\). A coalition \(S\) may use only \(\lfloor 2|S|/n\rfloor\) seats, and its worth \(\chi(S)\) is the maximum sum of its members' PAV scores across admissible committees; transfers inside the coalition are allowed. The TU core consists of payoff vectors whose entries sum to \(\chi(N)\) and whose sum over every coalition \(S\) is at least \(\chi(S)\).

By within-party exchangeability, \(\chi(S)\) depends only on the numbers \(s\) and \(t\) of party-A and party-B members. For every integer \(0\le s\le a\), \(0\le t\le b\), writing \(q=\lfloor 2(s+t)/n\rfloor\), the worth is exactly

\[
\chi_{a,b}(s,t)=\begin{cases}
0,&q=0,\\
\max\{s,t\},&q=1,\\
\max\{3a/2,a+b,3b/2\},&q=2.
\end{cases}
\]

The final case \(q=2\) occurs only for the full grand coalition \((s,t)=(a,b)\). The assumption of at least two candidates per party makes all three two-seat allocations feasible. No cardinal valuation claims beyond harmonic PAV satisfaction are made.

## Proof

**1. Characteristic function.** A one-seat entitled coalition can obtain precisely \(\max\{s,t\}\) by choosing one of the two parties' candidates. A full coalition can choose both seats from party A, one from each, or both from party B, obtaining respectively \(3a/2\), \(a+b\), and \(3b/2\). Coalitions of size less than \(n/2\) are entitled to zero seats. This proves the displayed worth formula for all coalitions.

**2. Exact Shapley reduction.** For each predecessor subset of size \(h\) in a uniformly random voter order, the usual Shapley weight is \(1/[n\binom{n-1}{h}]\). Collapsing predecessor subsets by party composition, the value per party-A member is

\[
\phi_A=\sum_{s=0}^{a-1}\sum_{t=0}^{b}
\frac{\binom{a-1}{s}\binom bt}{n\binom{n-1}{s+t}}
\bigl(\chi_{a,b}(s+1,t)-\chi_{a,b}(s,t)\bigr),
\]

and the value per party-B member is

\[
\phi_B=\sum_{s=0}^{a}\sum_{t=0}^{b-1}
\frac{\binom as\binom{b-1}{t}}{n\binom{n-1}{s+t}}
\bigl(\chi_{a,b}(s,t+1)-\chi_{a,b}(s,t)\bigr).
\]

Both are rational, and Shapley efficiency gives \(a\phi_A+b\phi_B=\chi_{a,b}(a,b)\). The TU-core test therefore consists precisely of the finite family

\[
 s\phi_A+t\phi_B\ge\chi_{a,b}(s,t)
 \quad\text{for all integer }0\le s\le a,\quad0\le t\le b.
\]

**3. Complete exact first-boundary certificate.** Party relabeling permits \(1\le a\le b\). For every \(n\) from \(2\) through \(14\) and every such integer split, evaluate the two displayed finite Shapley sums using reduced rational arithmetic, then test every integer coalition composition in the rectangle \([0,a]\times[0,b]\). The independent subset-based implementation evaluates both Shapley values directly from all \(2^n\) labelled predecessor masks; the two implementations agree for every tested profile. The program `verify_shapley.py`, supplied in full, makes this a finite exhaustive calculation rather than sampling or a floating-point estimate. It checks **49** distinct party-size profiles and **1512** coalition-type constraints. For each \(n\le13\), every core inequality holds. For \(n=14\), exactly one party-size split fails, \((6,8)\), and exactly one coalition-composition type fails, \((6,1)\). The smallest slack over proper entitled coalition types, by electorate size \(n=2,3,\ldots,14\), is

| \(n\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Minimum slack | \(0\) | \(1/3\) | \(0\) | \(2/5\) | \(0\) | \(18/35\) | \(0\) |

| \(n\) | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---:|---:|---:|---:|---:|---:|
| Minimum slack | \(167/315\) | \(0\) | \(611/1386\) | \(0\) | \(370/1001\) | \(-83/858\) |

**4. Exact witness.** At \((a,b)=(6,8)\), the rational sums give

\[
(\phi_A,\phi_B)=\left(\frac{7127}{9009},\frac{6947}{6006}\right),\qquad
6\phi_A+8\phi_B=14=\chi_{6,8}(6,8).
\]

A coalition containing six A voters and one B voter has seven members, therefore one seat, which it assigns to an A candidate for worth \(6\). Its Shapley receipts are \(6\phi_A+\phi_B=5065/858\), strictly less than its worth by \(83/858\). Since transfers are permitted, the coalition can divide its net advantage to strictly improve all its members. The complete exact check proves there are no smaller counterexamples within the stated domain and no additional fourteen-voter types.

## Verification

Run `python3 verify_shapley.py` with Python 3.8 or later (arbitrary-precision `fractions.Fraction` and built-in `math` only). The verifier constructs every two-party size up to fourteen voters, compares the party-composition Shapley formula against a separate labelled-subset Shapley formula, verifies grand-coalition efficiency, exhaustively evaluates each coalition-type inequality, and asserts the unique threshold witness and rational gap. Expected output begins `PASS: 49 party-size profiles, 1512 coalition-type constraints` and identifies the deficit \(83/858\).

The verification is an **exact finite certificate** for the explicitly finite threshold theorem. It is not a proof about any larger electorate, other voting rule, more than two parties or other committee size.

## Relationship to prior work

Chen and Hatschka (2026) introduce the TU multi-winner voting-game framework, show PAV TU cores can be empty on overlapping approval profiles, and already exhibit a four-voter *overlapping-profile* counterexample in which the Shapley value is not TU-PAV core-stable (their Shapley proposition, proof). This theorem neither claims priority for general Shapley instability nor implies unrestricted core existence. Its added statement isolates the complete **two disjoint homogeneous parties / two seats** boundary. Their general existence theorem for totally separable scoring rules does not establish Shapley TU-PAV core membership, and PAV is not a totally separable rule in general.

Brill, Laslier and Skowron (2016/2021) show that party-list PAV winners coincide with D'Hondt allocations. That allocation identity does not determine the Shapley value of the induced TU characteristic function, since the latter includes proportional seat caps for all coalitions. Pierczyński and Skowron (2021) study the committee core for restricted preference domains under a different (nontransferable) stability notion. Neither of those statements supplies the exact fourteen-voter TU-Shapley threshold. No claim of priority over unindexed results is made.

## Limitations

The theorem assumes exactly two nonempty homogeneous disjoint-approval blocs, at least two candidates per bloc, harmonic PAV utilities, a two-seat committee, proportional floor seat entitlement, and transferable coalition utilities. The finite calculation establishes the full result only through fourteen voters; it does not classify or predict larger electorate sizes. Coalition types are fully enumerated, but different labelled coalitions with the same type are equivalent by symmetry. There is no independent external audit, and novelty is subject to the usual limitations of searchable literature.

## References

1. Jiehua Chen and Christian Hatschka, *Multi-Winner Voting Games in TU and NTU: When is the Core Always Non-Empty?*, arXiv:2605.22528, first version May 21, 2026. https://arxiv.org/html/2605.22528v1
2. Markus Brill, Jean-François Laslier and Piotr Skowron, *Multiwinner Approval Rules as Apportionment Methods*, arXiv:1611.08691, first version November 26, 2016; version inspected April 20, 2021. https://arxiv.org/html/1611.08691v2
3. Grzegorz Pierczyński and Piotr Skowron, *Core-Stable Committees under Restricted Domains*, arXiv:2108.01987, first version August 4, 2021. https://arxiv.org/abs/2108.01987
