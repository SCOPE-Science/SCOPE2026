# Independent audit — cyclic STS(15) resolvability record

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/036`  
**Audited directory tree:** `f119da32060d93653479e28df37a989087741a2f` (unchanged when checked at repository head `c40ff4843745efb8c2c7275f5cacbda243c36a25`)  
**Review type:** separate AI independent audit.

## Claim audited

The record studies two cyclic Steiner triple systems on Z15 generated respectively by
`{0,1,4}, {0,2,8}, {0,5,10}` (B) and
`{0,1,4}, {0,2,9}, {0,5,10}` (A). It claims B has 56 parallel classes and 240 resolutions, A has 11 parallel classes and no resolution, their automorphism-group orders are 20160 and 60, and a 36-system cyclic generator census splits 18/18 between the two affine classes.

## Correctness — PASS

I independently reconstructed both block systems rather than relying on the historical audit. Cyclic development produces 35 blocks in each case, and every one of the 105 unordered point-pairs occurs exactly once. Independent parallel-class backtracking gives 56 classes for B and 11 for A. An independent exact-cover count gives 240 partitions of B into seven parallel classes and 0 for A. Point-stabilizer enumeration using the Steiner third-point relation gives stabilizers 1344 and 4; the verified translation action is transitive, so orbit-stabilizer yields full automorphism orders 20160 and 60. Finally, enumeration of the 91 triples containing 0, paired two at a time with the short orbit {0,5,10}, gives exactly 36 cyclic STS(15)s; canonicalization under `x -> u*x+t`, with u a unit mod 15, splits them 18/18 into the A and B classes. These checks reproduce the record's numerical claims.

## Originality — FAIL

The headline result is covered by prior literature. Svetlana Topalova, **“On the resolutions of cyclic Steiner triple systems with small parameters,”** *J. Algebra Combin. Discrete Appl.* 3(3) (2016), 201–208, DOI `10.13069/jacodesmath.47635`, §3.2 and Table 1, states that there are exactly two cyclic STS(15), with full automorphism groups of orders 60 and 20160; exactly the latter is resolvable; and it has two nonisomorphic resolutions, each with resolution automorphism group 168. The paper expressly treats all resolutions of cyclic STS(15).

That covers the record's central dichotomy and automorphism orders. Moreover, the record's raw count 240 is mechanically recovered from Topalova's two resolution isomorphism classes: each has orbit size `20160/168 = 120` under the design automorphism group, hence 240 labeled resolutions in total. The explicit Z15 presentation identifies the two known cyclic designs, but does not create a new abstract resolvability result.

Sources checked also included the cited cyclic-STS classification background and searches for the specific generator pairs, parallel-class counts, and automorphism orders. No evidence was found that the exact residual numbers 56/11 were themselves tabulated in Topalova, but that does not rescue the claimed headline novelty.

## Scientific value — FAIL

After subtracting known coverage, the surviving content is an explicit coordinate realization plus small finite counts (56/11 parallel classes and the 18/18 generator-pair bookkeeping split) for the two already-classified order-15 cyclic designs. A bounded repair was considered: narrow the record to those residual counts and replayable certificates. That would be correct, but it is a small finite census at the first nontrivial order, with no new structural theorem, new regime, or algorithmic improvement beyond exhaustive enumeration. It does not meet this campaign's scientific-value threshold.

## Disposition

**FAILED.** Correctness passes, but originality and value fail. The record should be retained only in the failed-attempt archive with its original package preserved.

## Search/access notes

Topalova's full text was available lawfully online and the decisive §3.2/Table 1 text was inspected. No Oxford institutional fallback was needed. Searches included variants of “cyclic STS(15) resolutions”, “two cyclic Steiner triple systems order 15 20160 60”, the exact generator families, “parallel classes STS(15) 56 11”, and references cited by the record. No inaccessible source was used to establish the failure.
