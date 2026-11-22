# Scientific review: Sharp survivor-deletion spectrum of run-two words

## Correctness — PASS

For linear indexed \(q\)-ary words \(q\ge2\), \(n\ge1\) with no three equal successive letters, outputs are counted only after one deletion and only if the output also obeys that constraint. One output per maximal run is the established unconstrained identity. The critical new filter disallows exactly interior singleton deletions joining identical neighboring run letters into a triple; double-run deletions always remain legal. The four-state transfer weights all symbol choices and all middle-run contributions, and the endpoints are counted separately. The inequality based on incidences of singleton and double runs gives the sharp minimum \(\lceil(n+2)/4\rceil\), achieved by explicit run patterns at each length. Equality at lengths \(n=4h-2\) rigidly forces the alternating double–singleton–singleton run pattern, with exactly \(q(q-1)^{h-1}\) realizations. The maximum \(n\) is attained exactly by proper words, \(q(q-1)^{n-1}\) in total.

The standalone standard-library checker enumerated all admissible source words for \(q=2\), \(n\le16\); \(q=3\), \(n\le10\); and \(q=4\), \(n\le8\). For 115,544 words, direct filtered-deletion enumeration, the run criterion, and the four-state polynomial counts agreed. Constructed extremizers were also checked for seventeen consecutive target degrees. Finite tests do not replace the proof of statements for all lengths.

## Originality — PASS, qualified

Primary material inspected includes Liu, Xing and Zhang, [arXiv:2307.00221](https://arxiv.org/abs/2307.00221), and Kulkarni and Kiyavash, [arXiv:1211.3128](https://arxiv.org/abs/1211.3128). These concern DNA codes and binary \((d,k)\)-run constraints respectively. The complete [public deletion-pattern theorem](https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-pattern-collision-thresholds-and-short-deletion-extrem--2036e6f8e3be) was read and compared: it addresses unrestricted deletion descendants, without a receiver run cap. A published finite codebook optimum for a different run-constrained language, and several deletion/read-spectrum results, were also compared. No identified result implies the exact both-sided run-two filtered-degree distribution and sharp minimizer census. Equivalent terminology or unindexed older results remain a historical-priority risk; failed searches are not proof of priority.

## Value — PASS

The same run-limit restriction on a receiver is natural for constrained-molecule outputs and makes the valid one-deletion neighborhood strictly smaller than the standard deletion sphere. The all-length structural law, four-state count, sharp universal lower bound and equality census measure possible constrained read diversity and identify fragile patterns. The finding is a motivated complete invariant rather than a preselected finite benchmark or a routine reproduction of an unrestricted sphere count.

## Limitations

Only one deletion from linear words with maximum run length two is covered; the results do not establish error-correcting code capacity, nor extend automatically to cyclic words, longer runs or multiple deletions. Related inaccessible or unindexed historical work could affect priority. Computational checks support, rather than prove, the all-length statements.

Self-review: passed. Independent audit: not yet performed.
