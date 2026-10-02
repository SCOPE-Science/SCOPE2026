# Independent audit — 2026-10-01

## Final claim

A binary linear code with no weights from the minimum distance plus one through the minimal-support ceiling has every word as a disjoint sum of minimum words and is minimum-distance divisible; for odd minimum distance greater than one only the stated dimension-one or two-block cases occur.

## Correctness — PASS

Ashikhmin--Barg Lemma 2.1 was inspected in the primary paper: minimal supports have size at most \(n-k+1\), minimal vectors span, and every nonminimal binary codeword splits into two nonzero disjoint-support subwords. The full gap therefore forces every minimal word to have weight \(d\); recursive splitting terminates and partitions any codeword into disjoint minimum words, proving divisibility. The intersection and odd-distance classification then follow exactly as stated. A fresh exhaustive replay through length seven and dimension three checked 17,140 subspaces, including 498 full-gap cases, with no counterexample.

Checked sources: Ashikhmin and Barg, Minimal Vectors in Linear Codes, IEEE Trans. Inf. Theory 44 (1998), Lemma 2.1; Xianmang He, A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes, arXiv:2609.20344; Divisible Minimal Codes, arXiv:2312.00885 / Serdica J. Computing 18 (2025); Published-findings semantic search for full initial gaps, minimal vectors and divisible binary codes; Assigned Git package and fresh exhaustive replay for all binary subspaces with length at most 7 and dimension at most 3

Residual risks: No issue remains for correctness; the principal issue is that the theorem is an immediate recursive consequence of the classical lemma.; The finite census is only a sanity check and is not used as a proof of the infinite statement.

## Originality — FAIL

Originality fails under the implication-based standard. Once the three classical Ashikhmin--Barg properties are put together, the final divisibility theorem is a direct induction: the full gap says every minimal vector has minimum weight, and the binary decomposition recursively expresses every other vector as a disjoint sum of them. The odd-distance rigidity is then an elementary parity consequence. Exact wording need not appear in the 1998 paper for this mechanically implied corollary to be covered.

### Equivalent formulations

Searches: Ashikhmin--Barg Lemma 2.1 parts 2, 4 and 5; Resultary search for full initial gap and divisible binary codes

Evidence: The primary paper states the exact three properties needed for the proof on page 2010.; The recent mirror-band paper itself highlights the same binary disjoint-support property as a classical ingredient.

Reasoning: `All minimal words have common weight d` is an equivalent formulation sufficient for the same induction, and it is immediately forced by the full gap plus the classical minimal-support ceiling.

### Broader coverage

Searches: Ashikhmin--Barg general minimal-vector theorem; divisible minimal code literature

Evidence: The 1998 lemma applies to every binary linear code, strictly broader than the full-gap subclass.; No additional nonstandard theorem is needed after specializing it.

Reasoning: The general classical decomposition theorem mechanically dominates the claimed closure step.

### Exact database or table

Searches: published-findings query for the exact full-gap endpoint and odd-distance classification

Evidence: No separate exact table was located, but this is irrelevant because the theorem is mechanically implied by the classical lemma.

Reasoning: Absence of a printed table cannot restore originality.

### Claim versus prior implication

Searches: line-by-line implication from Lemma 2.1 to the final theorem

Evidence: Minimal support ceiling plus the gap forces weight d; spanning and disjoint binary decomposition give the induction; parity gives disjoint minimum supports for odd d.

Reasoning: The final claim is a short corollary of those prior statements rather than an independent mathematical result.

### Source inspections

- **Minimal Vectors in Linear Codes** — https://user.eng.umd.edu/~abarg/reprints/MinimalVectors98.pdf
  Trigger: Exact nonstandard lemma used in every step of the proof
  Material read: Lemma 2.1 and its surrounding proof on the first two pages
  Method: Primary PDF text and page inspection
  Assessment: Decisive prior implication coverage.
  Evidence: Lemma 2.1 states the minimal-support ceiling, spanning property and binary disjoint-support decomposition explicitly.
- **A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes** — https://arxiv.org/abs/2609.20344
  Trigger: Recent motivating use of the same classical binary decomposition property
  Material read: Abstract
  Method: Primary-source abstract inspection
  Assessment: Motivates the endpoint question but is not needed for the coverage failure.
  Evidence: The abstract explicitly attributes the disjoint-support decomposition of nonminimal binary codewords to Ashikhmin--Barg.

Checked sources: Ashikhmin and Barg, Minimal Vectors in Linear Codes, IEEE Trans. Inf. Theory 44 (1998), Lemma 2.1; Xianmang He, A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes, arXiv:2609.20344; Divisible Minimal Codes, arXiv:2312.00885 / Serdica J. Computing 18 (2025); Published-findings semantic search for full initial gaps, minimal vectors and divisible binary codes; Assigned Git package and fresh exhaustive replay for all binary subspaces with length at most 7 and dimension at most 3

Residual risks: No issue remains for correctness; the principal issue is that the theorem is an immediate recursive consequence of the classical lemma.; The finite census is only a sanity check and is not used as a proof of the infinite statement.

## Scientific value — FAIL

Although the divisibility observation may be a useful bookkeeping corollary, its proof is a routine induction from a classical lemma plus an elementary parity check. It introduces no new structural lemma, difficult boundary, or independently motivated exact invariant beyond that immediate consequence. Under the required value standard this is too close to a textbook deduction.

Checked sources: Ashikhmin and Barg, Minimal Vectors in Linear Codes, IEEE Trans. Inf. Theory 44 (1998), Lemma 2.1; Xianmang He, A Mirror Vanishing Band for Weight Distributions of Binary Linear Codes, arXiv:2609.20344; Divisible Minimal Codes, arXiv:2312.00885 / Serdica J. Computing 18 (2025); Published-findings semantic search for full initial gaps, minimal vectors and divisible binary codes; Assigned Git package and fresh exhaustive replay for all binary subspaces with length at most 7 and dimension at most 3

Residual risks: No issue remains for correctness; the principal issue is that the theorem is an immediate recursive consequence of the classical lemma.; The finite census is only a sanity check and is not used as a proof of the infinite statement.

## Limitations

- Binary linear codes only for the recursive disjoint-support step.
- The finite census is supplementary, not the proof.
- Scientific rejection is on prior implication and routine-deduction value, not correctness.

## Conclusion

Disposition: **failed**. Acceptance requires PASS on all three axes.
