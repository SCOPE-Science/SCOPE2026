# Review of the binary four-mer Greedy extremal ratio

## Correctness (C) — PASS

The stated ratio applies to all nonempty subsets of the sixteen binary length-four words, and to the worst legal tie-breaking of ordered global-maximum-overlap Greedy. The shortest-superstring recurrence is the exact maximum-weight overlap Hamiltonian-path DP. The Greedy recurrence is exact by the endpoint-overlap invariance for substring-free equal-length inputs (Chukhin et al., 2026, Lemma 2.2), and minimizes cumulative overlap across every maximizing ordered pair. The C++17 verifier exhausts all \(16959\) reversal/complement orbit representatives, representing all \(65535\) inputs. It finds the sole maximizing orbit, checks four labeled equality cases and reconstructs legal output and optimum witnesses. An independent literal-string Greedy recursion reproduces \(17\) for the extremal example; a length-eleven word and factor-window lower bound certify its optimum. Execution output is bundled.

## Originality (O) — PASS against inspected evidence

Kulikov–Savinov–Sluzhaev (2015) gives the much weaker universal \(2\) ratio for length-four inputs; its accessible 18-slide presentation was inspected. Chukhin–Kulikov–Mihajlin–Smal (2026) proves the unrestricted-alphabet length-three value \(9/5\) and supplies an endpoint lemma, not the exact binary four-mer value. A preceding limited-cardinality binary four-mer result covers input sizes through eight and shows four eight-word inputs cross the \(3/2\) threshold, but does not exclude worse ratios at sizes nine through sixteen. The complete finite census distinguishes the present claim logically from these bounds and from the weaker full-spectrum single-instance benchmark. Searches for equivalent full-binary length-four classifications and matching \(17/11\) ratio statements returned no decisive stronger coverage. Search failure is not a proof of global publication novelty. The full 2015 proceedings chapter was not accessible in this check; the available abstract and complete 18-slide presentation state an upper bound \(2\), not the sharp ratio. A hidden small-case table is residual risk.

## Mathematical value (V) — PASS

The finite-alphabet approximation constant is natural and motivated by maximum-overlap genome/string reconstruction: a binary four-mer input is a subset of a canonical set of exactly sixteen distinguishable reads. Determining all tie outcomes across arbitrary input cardinalities is distinct from a finite eight-read example; the theorem supplies the exact worst-case guarantee and the complete equality orbit, which are not implied by the available large-alphabet or general two-approximation statements. The value is an exact natural finite boundary, not an arbitrary range of hand-picked cases.

## Scope, closest literature and residual risks

The proof is computational but exhaustive, not probabilistic; its state reduction relies on the published endpoint lemma and its own state recurrences. No conclusion is made beyond binary four-mers. The closest non-implying sources are arXiv:2608.20018 and DOI:10.1007/978-3-319-19929-0_26. Residual priority risk: an unindexed equivalent table or unavailable detailed text, though none was identified that states or implies the sharp conclusion.

Self-review: passed. Independent audit: not yet performed.
