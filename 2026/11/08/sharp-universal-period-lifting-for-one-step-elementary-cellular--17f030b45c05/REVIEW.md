# Scientific review: sharp universal period lifting for elementary cellular automata

## Correctness — PASS

The output block \(w\) corresponds to a four-vertex Boolean de Bruijn relation \(R_w\). Its periodic repetition is attainable exactly if \(R_w\) contains a directed cycle, and a predecessor of period dividing \(m|w|\) exists exactly if \(R_w^m\) has a diagonal entry. Every nonempty four-vertex cycle has a simple cycle of length one through four, and all four lengths divide twelve. Explicit relations for Rules 90 and 30 force divisibility by four and six, respectively. All 256 minimal per-rule multipliers were obtained by exhaustive closure of the finite Boolean relation semigroups, checking each possible matrix rather than a finite list of short output periods. Two independently implemented scripts return identical classifications; independent small-ring enumeration checks their semantic interpretation. The computational certificate is reproducible using Python standard library from files attached to this result.

## Originality — PASS, qualified

Prior primary work of Mariot and Leporati (2015) studies periods for bipermutive rules, and its 2017 extension with Dennunzio and Formenti provides a labeled de Bruijn closure method and multiplicity results for specified periodic outputs under surjective rules. Those constructions support our method but do not give the minimum **uniform** period multiplier per rule over all periodic outputs, the exhaustive 256-rule stratification, or the sharp common bound of twelve for all elementary rules. Salo's 2018 study concerns existence and consistency of equal-period predecessors for weak inverses rather than the full minimal multiplier stratification. Searches of scholarly sources and available published research descriptions did not reveal a dominating classification. Exhaustive historical priority is not established: an older specialized computation or unindexed table may contain equivalent numerical results.

## Value — PASS

The period-multiplier question measures the finite-ring enlargement needed to represent every attainable spatially periodic output of a rule by a periodic input. A sharp global bound guarantees a uniform finite construction, and the full classification identifies exactly which rules permit no inflation and which require factors two, four or six. Unlike a finite-period sampling, the output is a complete all-period statement for the natural finite family of elementary rules. The nondividing exceptional multipliers four and six make the optimal common bound twelve nontrivial in this context. The result uses no arbitrary fixed output length and is applicable when translating infinite-shift reachability into cyclic finite-volume computations.

## Closest literature and limitations

Mariot and Leporati, *AUTOMATA 2015*, pp. 181–195 (author postprint: https://lucamariot.org/files/papers/ml_automata_2015_postprint.pdf); Mariot et al., *Natural Computing* (2017) (author postprint: https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf); Salo, arXiv:1804.03913 (2018). The result concerns one step, binary radius-one rules and admissible periodic outputs. The finite classification is computer-assisted but exhaustively reproducible; no independent mathematical audit or definitive priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
