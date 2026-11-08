# Review of the specific ternary \([24,6,12]\) code support profile

## Correctness

PASS. The statement is finite and exact for the explicitly printed generator. A dependency-free checker performs rank tests modulo three, enumerates every one of the \(729\) coefficient words and every one of the \(56631\) nonzero-dimensional message subspaces exactly once through unique reduced-row-echelon forms, and checks their supports against complete per-dimension histograms. The unique minimum two-subspace has a displayed witness. Rank tests of all \(2024\) column triples and \(10626\) quadruples establish precisely three minimal triple supports and \(102\) minimal four-support circuits, hence the coordinatewise locality partition. Critical logical steps are: row rank six gives a bijection from message subspaces to code subspaces; echelon normal forms are unique; nonzero column-dependence coefficients furnish local recovery checks.

## Originality

PASS on the searched evidence, not a claim of exhaustive priority. The full-text PDF of arXiv:2601.20600 was searched and its relevant sections inspected, including the exact matrix in Proposition 4.1 and the nearby tables and conclusion; it states the generator and LCD distance but no higher-support or locality census. Wei's generalized-weight theory and San-José's algorithm are general frameworks, not the numerical profile of this specific matrix. Indexed findings titled *Higher-support geometry of the displayed ternary code C3,2* and *Projective fingerprint of the optimal ternary [23,4,14] LCD code* concern different generator matrices and do not imply this one. Real risks: earlier unpublished or unindexed exact tables and possible code-equivalence coincidences with unexamined public collections. Novelty is an evidence-based best-knowledge assessment.

## Mathematical value

PASS. This is a complete, natural higher-support invariant for a newly constructed, small distance-optimal LCD code, rather than an arbitrary slice of codewords: it determines higher-dimensional support thresholds important to erasure and wiretap-II interpretations. The unique two-dimensional extremizer and nonuniform local-repair partition are non-obvious structural distinctions inaccessible from parameters \([24,6,12]\) alone. The answer is exact, reproductible, and finite; it does not require a general theorem or optimality of locality among all codes.

## Limitations

The claim applies only to the printed \(C_{3,3}\) generator. It does not give globally optimal recovery, performance bounds for a specific protocol, or a classification of all such parameter codes. Priority remains contingent on human assessment of unindexed literature; computational correctness is established by a transparent exhaustive finite certificate, not by an independent audit.

Self-review: passed. Independent audit: not yet performed.
