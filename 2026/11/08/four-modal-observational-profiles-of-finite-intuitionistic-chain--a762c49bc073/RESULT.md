# Large observational fibers for four intuitionistic modalities on finite chains

## Finding

Let \(C_n=\{0<\cdots<n-1\}\), \(n\ge4\), be a fixed labelled intuitionistic chain. For each arbitrary binary relation \(R\subseteq C_n^2\), interpret the four Přenosil, Fischer–Servi, Wijesekera and dual modal operators on all upsets by the standard clauses of Balbiani–Gencer. Two relations belong to the same observational fiber if all four operators have the same truth-set action on every upset. Set \(M_n\) equal to the largest number of concrete binary relations in one such fiber.

**Improved unbounded-size fiber theorem.** For every \(n\ge4\),
\[
\boxed{ M_n\ \ge\ 9^{n-2}2^{n^2-4n+2}. }
\]
The displayed size is attained by one explicit fiber, not merely by a union of fibers or a collection of isomorphic relations. This lower bound is strictly sharper, for every \(n\ge4\), than the earlier general bound \(2^{n(n-2)}\) from *Four-modal observational fibers on finite intuitionistic chains* (November 2, 2026); their ratio is \(9^{n-2}/4^{n-1}\), increasing exponentially with \(n\).

**Sharp five-world maximum.** The largest observational fiber on the five-world labelled chain has exactly \(93,312\) relations, and it is unique among observable profiles:
\[
\boxed{M_5=93,312,\qquad \#\{\text{observable profiles with fiber }93,312\}=1.}
\]
The preceding four-world maximum is \(M_4=324\), already proved in the October 25 and November 2 results cited below. The known five-world *number of distinct observational profiles*, \(235,152\), was published on October 18 and is not claimed new here.

This theorem does **not** claim as original the four running-extrema signature, equivalence criterion, two-edge-per-row sparsification, sharp two-world identifiability threshold, general fiber product formula, or previously published class counts. These are explicitly credited prerequisites, not new findings.

## Assumptions, definitions and previously established profile machinery

No frame confluence, seriality, reflexivity or transitivity is assumed. Upward-closed truth sets are \(U_k=\{k,\ldots,n-1\}\), including \(U_n=\varnothing\), and comparisons are pointwise on the same ordered carrier under the same valuation. For row \(R[i]\) put \(a_i=\min R[i]\), \(b_i=\max R[i]\), using \(a_i=n,b_i=-1\) for an empty row. The already-published complete invariant consists of
\[
F_s=\max_{i\le s}b_i,\quad H_s=\min_{i\ge s}b_i,\quad I_s=\max_{i\le s}a_i,\quad G_s=\min_{i\ge s}a_i.
\]
These profiles exactly determine the action of the four operators on all upsets; equivalence of profiles is equivalent to observational equivalence. In particular, the number of relations with a specified profile can be evaluated by independently summing the endpoint multiplicities in each row. The weight of an empty row or a singleton interval is one, and a nonempty endpoint pair \((a,b)\) with \(a<b\) has multiplicity \(2^{b-a-1}\). See the three earlier published mathematical records in the references; this prior theorem is used, not reproved as new.

## Proof of the improved bound

For fixed \(n\ge4\), prescribe row endpoints \(a_0=1,b_0=n-1\) and \(a_{n-1}=0,b_{n-1}=n-2\). For each intermediate row \(1\le i\le n-2\), choose freely
\[
 a_i\in\{0,1\},\qquad b_i\in\{n-2,n-1\},
\]
and choose any actual subset of targets having the prescribed endpoints. All these rows are nonempty. Every such relation has identical profiles \(F_s=n-1\), \(H_s=n-2\), \(I_s=1\), and \(G_s=0\), for every world \(s\): the first row fixes both prefix extrema and the last fixes both suffix extrema. By the prior four-profile criterion, all the relations constructed are observationally equivalent.

Each boundary row, with endpoints differing by \(n-2\), can be filled in \(2^{n-3}\) ways. In one intermediate row the four endpoint choices have respective multiplicities
\[
2^{n-3},\qquad 2^{n-2},\qquad2^{n-4},\qquad2^{n-3},
\]
which sum to \(9\cdot 2^{n-4}\). The row choices are independent and yield distinct raw relations. Thus a **single** observable fiber contains exactly
\[
 2^{2n-6}\,(9\cdot2^{n-4})^{n-2}
 =9^{n-2}2^{n^2-4n+2}
\]
relations, proving the lower bound. This argument is valid for every \(n\ge4\) without finite-size extrapolation. Comparing with the earlier bound gives the exact factor \(9^{n-2}/4^{n-1}>1\) for \(n\ge4\).

## Proof of the sharp five-world maximum

The exact all-size *fiber-product formula* is already known. For \(n=5\), there are precisely \(1+5(6)/2=16\) distinct row endpoint types: one empty sentinel and fifteen pairs \(0\le a\le b<5\). Enumerating all \(16^5=1,048,576\) ordered endpoint-type vectors is exhaustive. For each vector, form the four running-extrema profiles, multiply the five weights \(w(a,b)=2^{\max(b-a-1,0)}\) (or one for the empty sentinel), and accumulate weights sharing the same profile. Every one of the \(2^{25}=33,554,432\) binary relations has exactly one endpoint vector and contributes weight exactly once. Consequently the resulting table computes every observational fiber without omission or double counting. The file `checks/profile_census.cpp` implements this finite integer algorithm with a lossless 60-bit key; its output for \(n=5\) is

```
5 235152 33554432 93312 1
```

in the order (chain size, number of profiles, total relations represented, maximum fiber weight, number of maximizing profiles). The last two entries prove both upper bound and uniqueness. The analytic construction in the preceding section independently supplies a fiber of size \(9^3 2^7=93,312\), confirming attainment. A separate complete integer implementation which reconstructs profiles and counts directly over endpoint vectors reproduced the same five entries, independently of the source checker. The first three entries for \(n=5\) include a previously known quotient count and a consistency total; they are not new discoveries.

## Value, novelty boundary and limitations

The maximum size of an observational equivalence class measures the worst-case ambiguity in reconstructing a concrete relation from all four modal truth transformers. This is a natural exact invariant of a labelled finite chain. The new five-world maximum and unique maximizing fiber close the first open computational case beyond the earlier maximal-fiber tables ending at four worlds. The new uniform bound improves the previously published all-length guaranteed ambiguity by a factor that grows exponentially with chain length. These are independently useful even though the exact global formula for \(M_n\) at all \(n\ge6\) remains open.

The proof uses an exhaustive *finite* calculation for \(n=5\), not an extrapolation. The general lower bound is proved combinatorially. No optimality for \(n\ge6\), unlabelled/isomorphism census, or formulas on non-chain preorders are claimed. Historical priority is best-of-knowledge: a larger maximum table or general improved fiber formula under different names could exist.

## Prior mathematical results and references

1. *Four-modal semantic quotients and optimal relation sparsification on finite intuitionistic chains* (October 18, 2026). Establishes the four-extrema observational invariant, optimal rowwise sparsity and quotient counts through five worlds: https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-four-modal-semantic-quotients-and-optimal-relation-sparsificatio--b99647029094/RESULT.md
2. *Sharp sparse normal form and exact observational fibers for four intuitionistic modalities* (October 25, 2026). Establishes the explicit all-size fiber product, the sparse bound and maximal fibers through four worlds: https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-sharp-sparse-normal-form-and-exact-observational-fibers-for-four--0c002f416cb4/RESULT.md
3. *Four-modal observational fibers on finite intuitionistic chains* (November 2, 2026). Establishes the same all-size observable invariant, injectivity for \(n\le2\), maximal fibers through four worlds, and the general earlier lower bound \(2^{n(n-2)}\): https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-four-modal-observational-fibers-on-finite-intuitionistic-chains--7e6e6da0bef7/RESULT.md
4. P. Balbiani and Ç. Gencer, *Four intuitionistic modal connectives*, arXiv:2606.07348 (June 5, 2026), Section 3.4 for the semantic clauses: https://arxiv.org/abs/2606.07348.
5. A. Přenosil, *Compatibility between modal operators in distributive modal logic*, arXiv:2311.10017 (2023): https://arxiv.org/abs/2311.10017.
