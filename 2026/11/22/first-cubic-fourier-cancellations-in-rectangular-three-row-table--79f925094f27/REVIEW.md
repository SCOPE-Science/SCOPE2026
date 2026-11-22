# Review of the finite ternary tableau convolution finding

## Correctness — PASS

The prefix-row-word bijection fixes the indicator support; independent hook-length arithmetic confirms 462 words at shape \((4,4,4)\). The complete Fourier transform is computed with exact integral cyclotomic coordinates, not floating-point thresholds. An inductively justified tensor transform covers all \(531441\) frequencies. Independent direct phase counts check all frequencies through degree three, including the eight cubic cancellations, plus additional frequencies; exact Parseval and conjugacy give global consistency checks. Thus the rank and degree cutoff are proved for the four stated widths. No infinite-width assertion is made.

## Originality — PASS under bounded comparison

Eu's 2010 treatment of three-row Yamanouchi words and Kim's 2011 skew-tableau enumerations are direct archival antecedents. Their examined content counts tableaux and gives bijections/generating functions, not the position-resolved root-of-unity spectrum of the full ternary word-group convolution. Fourier sampling on three-by-three tableaux concerns a different sampling matrix, so does not imply the present four-column convolution rank. Exact numerical, equivalent-formulation and dominance searches found no matching rank or low-degree-zero list; this is bounded evidence, not proof of historical priority. A previously unindexed position-weight enumerator remains a concrete risk.

## Value — PASS

The central feature is the recovery-boundary reversal between shapes \((3,3,3)\) and \((4,4,4)\): quadratic cancelling modes occur at width three, but none at width four although the operator remains singular. The complete \(3996\)-dimensional kernel, eight first cubic frequencies and exact convolution rank give a natural, nontrivial quantitative benchmark for three-row ballot words. The result deliberately makes no generalization to wider shapes.

## Closest literature and limits

- S.-P. Eu, *Skew-standard tableaux with three rows*, arXiv:1002.4060 (2010).
- J. H. Kim, *On the enumeration of three-rowed standard Young tableaux of skew shape in terms of Motzkin numbers*, arXiv:1107.3873 (2011).
- Limit: finite rectangle widths one through four; independent validation not performed.

Self-review: passed. Independent audit: not yet performed.
