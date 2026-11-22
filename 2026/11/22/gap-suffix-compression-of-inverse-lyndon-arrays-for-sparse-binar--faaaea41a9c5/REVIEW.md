# Review of gap-suffix compression of inverse Lyndon arrays

## Correctness (C): PASS

The exact domain comprises every nonempty binary word specified by nonnegative gaps around any number of ones, including zero ones, consecutive ones, and empty boundary gaps. The proof identifies the inverse Lyndon entry at every zero position; proves an order isomorphism between one-started suffixes and a terminal-aware, reverse-ordered integer gap code; derives expanded LCE from matching completed blocks; and applies the published nearest-greater-suffix/border identity to obtain the entry at every one position. Integer suffix sorting, LCP range minima, prefix sums and a monotone next-greater scan establish the advertised compressed time/space bounds. The actual packaged independent oracle passed the finite tests reported in `check_output.txt`. Finite experiments are sanity checks and not a proof of the all-parameter theorem.

## Originality (O): PASS, with stated historical-priority risk

The original and extended 2026 papers on the inverse Lyndon array provide the NGS/LCE formula and an expanded-text linear-time array construction. Their inspected Sections 3--4 do not give a terminal-aware sparse-binary gap-code suffix sorting, compressed expanded-LCE retrieval, or a complete arithmetic-progression encoding computed without expansion. Ghuman, Giaquinta and Tarhio's 2019 Section 5 is an RLE algorithm for ordinary Lyndon **factorization**, a different, single-factorization output, not for all inverse Lyndon array entries. The 2025 compressed Lyndon-array article's accessible abstract deals with standard arrays during grammar decompression; the full paper was not inspected, so it remains a residual comparison risk. Search comparisons for inverse arrays, sparse words, gap suffixes, RLE and aliases in the available indexed results did not reveal an equivalent theorem, but search absence is not proof of priority. An unindexed or unstated reduction could cover this result; that remains a live risk requiring human confirmation.

## Value (V): PASS

This concerns the full new inverse Lyndon data structure, not an arbitrary counting slice. The general 2026 algorithm takes time proportional to the expanded length, whereas sparse words may have enormous zero runs. The proved transformation replaces the text by only one suffix-code symbol per marked one, faithfully handles the terminal short-suffix asymmetry and the otherwise problematic border correction, and returns every array entry in a compact queryable form. The \(O((r+1)\log(r+2))\) preprocessing cost is independent of the zero-run sizes on a word RAM; this is an asymptotic algorithmic improvement whenever \(r\ll n\). No claim is made for unrestricted alphabets, explicitly outputting the full array, or optimal time.

## Closest sources and limits

* Negri et al., arXiv:2603.17537v1, §§3.1--3.2: defines the inverse Lyndon array and proves the NGS/border correction.
* De Felice et al., arXiv:2609.23401v1, §§3--4: develops expanded-input linear-time construction and relation to canonical inverse factorization.
* Ghuman, Giaquinta and Tarhio, Algorithms 12(6):124 (2019), §5: RLE ordinary Lyndon factorization, not the inverse array.
* *Space-Efficient Lyndon Array Construction from Compressed Texts* (2025): only public abstract inspected; full-document implications remain a stated priority risk.

The proof is mathematical and the verification is same-model only. It has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
