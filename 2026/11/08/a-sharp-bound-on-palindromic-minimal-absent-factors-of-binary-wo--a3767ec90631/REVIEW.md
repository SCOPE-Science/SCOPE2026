# Scientific review

## Correctness: PASS
The exact statement includes length-one absent letters, the single-symbol case, and the \(n=2\) boundary. The proof shows distinct palindromic minimal absent factors of a binary word using both letters cannot share the first-occurrence endpoint of their truncated prefixes. Its difficult case uses the binary impossibility of excluding two different completion letters at the same nonterminal position, followed by a suffix-occurrence argument at the terminal position. The complete family \(01^{n-2}0\) supplies exactly \(n\) explicit missing palindromes. The included independent programs corroborate small lengths without replacing the universal argument.

## Originality: PASS (best-knowledge, with risk)
The closest full-text sources are Pinho et al. (2009), Barton et al. (2014), and Almirantis et al. (2017). The first two prove structural/general algorithmic facts about all minimal absent factors, not the binary-palindromic exact extremum. The third already supplies the same two-run witness for an asymptotic lower bound, so the witness is acknowledged as known; its proof counts \(n-2\) missing factors and does not state the exact maximum or this injection. Searches of accessible research records and literature for “palindromic minimal absent”, “minimal forbidden palindrome”, endpoint charging, and stronger binary cardinality bounds did not yield an equivalent result. A stronger exact bound on all binary minimal absent factors, if published elsewhere, could dominate the stated cardinality conclusion; this remains a genuine priority risk, not disproved by missing search hits.

## Value: PASS
The extremal count of palindromic *negative* motifs is a natural, precisely defined counterpart to counting palindromic factors. The result replaces generic asymptotic \(O(n)\) control with an exact sharp coefficient for every binary length, and supplies an explicit, nontrivial reason that two letters enable charging to word positions. This determines the worst-case inventory size of a reversal-symmetric subset of a factor antidictionary. It makes no claim of a general algorithm improvement or a demonstrated biological application.

## Limits
The alphabet must be binary, the text must be linear, and the absentness relation is contiguous. Neither a characterization of all equality cases nor an independent historical-priority audit is supplied.

Self-review: passed. Independent audit: not yet performed.
