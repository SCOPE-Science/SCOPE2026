# Independent three-axis audit — 2026-09-22 campaign

## Record and source identity

- Source path: `2026/09/08/026`
- Audited repository: `SCOPE-Science/SCOPE2026`
- Audited source tree: `de2d628121dbe129ecce0f429c0f77f2a2dbf84f`
- `RESULT.md` blob: `5bc24881c717dabb01fdeb7e1398789345a145d0`
- `VERIFICATION.md` blob: `83b03a7f246da30fad50fa39962dbb6d7f0519f0`
- Review date (UTC): 2026-09-23
- Review type: separate AI independent audit; not human/expert attestation and not Lean/formal verification.

## Claim audited

The record gives a census of the simple rank-3 matroids on eight elements, states that there are 68 isomorphism types and 433,038 labeled rank-3 line families, and claims that over this window `T_M(2,0)` is uniquely maximized by `U(3,8)` at 58, with runner-up 56 and gap 2. It also exhibits an eight-element type whose deletion is the Fano matroid.

## Correctness — PASS

I independently checked the enumerative and Tutte claims by methods different from the record's deletion-contraction computation.

### Labeled line-family count

A simple rank-3 matroid on `[8]` can be encoded by its nontrivial rank-2 lines, each of size at least three, with distinct lines sharing at most one point. I wrote an independent dynamic program on the 28 unordered point-pairs. At each state it chooses the first undecided pair and either leaves it uncovered or selects one candidate line containing it whose pair set is still undecided. Memoization over the decided-pair mask gives exactly 433,039 valid line families, including the single rank-2 family `{[8]}`. Removing that family gives **433,038**, exactly the record's labeled count.

The isomorphism-type count is independently corroborated by Mayhew and Royle's complete catalogue. Their Table 2 (“Simple matroids on up to 9 elements”) gives **68** simple rank-3 matroids on eight elements and explicitly states that their computation agrees with the earlier Blackburn–Crapo–Higgs catalogue. See D. Mayhew and G. F. Royle, *Matroids with nine elements*, JCTB 98 (2008), 415–431, arXiv:math/0702316, Table 2.

### `T(2,0)` maximality and gap

The maximization does not require a census. From the defining subset expansion, `T_M(2,0)=sum_{A subseteq E} (-1)^{|A|-r(A)}`. For a simple rank-3 matroid, every dependent subset of size at least three lies in a unique nontrivial line. Relative to `U(3,8)`, a subset of size `k>=3` contained in a line has rank 2 rather than 3, so its contribution changes by `(-1)^(k-2)-(-1)^(k-3)=2(-1)^(k-2)`.

Therefore every simple rank-3 matroid on eight elements satisfies the closed formula `T_M(2,0) = 58 - sum_L (|L|-1)(|L|-2)`, where the sum is over its nontrivial lines. I independently checked the binomial identity `2 sum_{k=3}^s C(s,k)(-1)^(k-2)=-(s-1)(s-2)`.

Consequently the uniform matroid, which has no nontrivial lines, has value 58 and is the unique maximizer. Every nonuniform simple rank-3 matroid has at least one line of size at least three and therefore loses at least 2; a single 3-point line attains 56. Thus the claimed gap 2 is correct, by a direct proof stronger and simpler than the record's exhaustive verification.

### Fano certificate

For the seven lines listed in the record after deleting point 4, I independently checked that their 21 unordered pairs are all distinct and exhaust the 21 pairs on the remaining seven points. Hence they form the Fano plane. The stated GF(2) vectors give the standard seven nonzero vectors of `GF(2)^3`, so the characteristic-2 representation and the usual characteristic-not-2 obstruction are consistent with the classical Fano facts.

No correctness defect was found in the headline claims.

## Originality — FAIL

The census is not new. Mayhew–Royle's 2008 complete catalogue, confirming the earlier Blackburn–Crapo–Higgs work, already tabulates the 68 simple rank-3 eight-element matroids. Their catalogue is a stronger reusable object than a new enumeration of this one window.

The `T(2,0)` extremal statement also does not survive as a substantial new theorem. The direct subset-expansion identity above proves, for every simple rank-3 matroid on eight elements, `T_M(2,0)=58-sum_L (|L|-1)(|L|-2)`. Thus the unique maximum at the uniform matroid and the exact gap 2 are immediate consequences of the defining Tutte expansion and the line description of simple rank-3 matroids; no 68-type enumeration is needed. This is a routine derivation rather than a new structural extremal phenomenon.

The Fano-window certificate is likewise a restatement of classical small-matroid structure: adjoining an eighth point to a Fano restriction/deletion gives an eight-element matroid with an `F_7` minor, and the characteristic obstruction for `F_7` is standard.

Searches included the exact small-matroid census, Mayhew–Royle/Blackburn–Crapo–Higgs catalogues, and Tutte-polynomial extremal terminology. The decisive catalogue source was available as lawful open full text, so no institutional-download fallback was required.

## Scientific value — FAIL

After known catalogue coverage and the elementary closed formula are subtracted, the remaining contribution is a finite `T(2,0)` table plus a classical Fano example. The table is reproducible, but the headline maximum and gap follow immediately without it, and the record does not extract a new invariant relationship, a general rank-3 theorem beyond the displayed elementary identity, a new representability classification, or an algorithmic improvement over the established catalogue.

A finite recomputation of a known 68-object window, when the claimed extremal consequence has a one-line structural formula and the representability example is classical, does not meet the campaign's scientific-value threshold.

## Bounded repair considered

A bounded repair could:
- cite Mayhew–Royle/Blackburn–Crapo–Higgs as the established census;
- replace the exhaustive maximality narrative by the direct formula `T_M(2,0)=58-sum_L(|L|-1)(|L|-2)`;
- present the computed table as a derived catalogue annotation rather than a novel theorem.

That would make the exposition more accurate and useful, but it would not restore sufficient originality/value. A legitimate retry would need a genuinely new general theorem or structural consequence beyond a finite annotation of the established catalogue.

## Final disposition

- Correctness: **PASS**
- Originality: **FAIL**
- Scientific value: **FAIL**
- Disposition: **failed / withdraw from validated findings**

The record's calculations are preserved as reproducible data, but its central census is already known and its claimed `T(2,0)` extremal theorem reduces to an elementary closed formula.
