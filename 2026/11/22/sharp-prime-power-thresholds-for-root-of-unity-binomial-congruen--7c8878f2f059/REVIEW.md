# Scientific review

## Correctness — PASS
The claim is a quantified all-integer congruence with a closed endpoint. For all degrees below \(d=p^r\), the normalized product at integer input \(-1\) has at most \(p-1\) valuation-one factors, implying the uniform lower bound \(2t-p+1\). Pascal finite differences propagate the congruence to every integer. For each exponent above the threshold a specified intermediate degree has exactly \(p-1\) valuation-one factors and a nonvanishing degree-\(j\) coefficient over \(\mathbb F_p\); all higher root-of-unity-filtered degrees have strictly larger valuation. Repeated finite differences show that this single failure rules out the original all-input condition. The exact checker confirms 72 finite-field coefficients and six full-product examples; it does not replace the proof.

## Originality — PASS on inspected evidence
Miska's 2022 arXiv full text (Theorem 2.3, Proposition 3.7, Corollaries 3.9 and 3.11, and section 4) concerns the same condition. Its sufficient exponent bound specializes to \(2t-p+1\), whereas its generic failure bound begins strictly above \(2t-1\), leaving \(p-2\) or more potentially ambiguous layers. The special \(t=p^u\) result has disjoint parameters. The new precise failure construction identifies the exact endpoint in all cases of an infinite two-parameter band, not a relabeling of the known sufficient result. Searches of related mathematical records did not expose a covering theorem. A published final version was only accessible in abstract, leaving possible text changes and unindexed equivalents as residual risks; failed searches do not establish uniqueness.

## Value — PASS
The problem is directly motivated by a published general classification with explicitly unresolved exceptional prime-power cases. Closing an entire natural near-prime band supplies a sharp existence threshold and a uniform arithmetic obstruction, without arbitrary slices or routine finite enumeration. The result distinguishes a sufficient bound from its sharp converse by a nontrivial finite-field coefficient identity.

## Literature and limitations
The primary source is P. Miska, *Binomial coefficients, roots of unity and powers of prime numbers*, arXiv:2203.03281v1 (2022-03-07), https://arxiv.org/pdf/2203.03281 ; the journal article is DOI 10.1007/s40840-022-01266-4. The theorem does not resolve remaining exceptional composite moduli or other ratio bands. The journal final full text and unindexed research may affect originality, and the present review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
