# Independent audit — 2026-09-25

## Record
- Source path: `2026/09/08/033`
- Record ID: `SCOPE-20260908-033`
- Audited source tree: `47fa7519555f889600576c969be5b73fa56560d8`
- Current repository comparison: no files under this source path changed between commit `253a0fe5d0217455660a277f9adb940030e567ad` and audited HEAD `7b29a9c25636a3c7b1d86c2610b7f24fc991e33f`.

## Claim audited
The record claims, conditional on the tabled equality (A(14,6,7)=42), that there are at least two coordinate-permutation-inequivalent optimal binary constant-weight ((14,6,7)) codes of size 42, represented by two explicit witnesses, and reports their distance distributions and stabilizer orders.

## Correctness

**Assessment: mathematical core passes, but the committed replay instructions are broken.**

The two committed witness files were independently parsed and checked from first principles.

- `artifacts/brouwer42.txt`: 42 distinct binary words, length 14, weight 7; minimum Hamming distance 6; unordered-pair distance distribution ({6:580,8:80,10:181,12:20}); coordinate-degree multiset ([20,20,21^{10},22,22]).
- `artifacts/clique42_1_155.txt`: 42 distinct binary words, length 14, weight 7; minimum Hamming distance 6; unordered-pair distance distribution ({6:580,8:80,10:180,12:21}); coordinate-degree multiset ([20,21^{12},22]).

Each distribution sums to (inom{42}{2}=861). Because Hamming distance is invariant under coordinate permutation, the differing distance distributions alone prove that the two codes are inequivalent.

An independent exact coordinate-permutation backtracking count, using coordinate degrees and pair-incidence constraints and verifying the resulting image family, gives stabilizer orders 40 and 720 respectively. This agrees with the record.

The Johnson-scheme Delsarte linear program was also rederived independently in exact rational arithmetic from the stated Eberlein constraints; its optimum is 197, so the record correctly describes it only as the weak upper bound (A(14,6,7)le 197). The current Brouwer constant-weight table records (A(14,6,7)=42), so the record's conditional use of 42 is consistent with that external table.

However, the committed package is not replayable as stated. `RESULT.md`, `METADATA.json`, `artifacts/stab_check.py`, and `artifacts/iso_test.py` refer to files under `output/artifacts/`, while the actual committed files are under `artifacts/`. Thus the printed replay commands and the verifier scripts' hard-coded input paths fail without editing. This is a real reproducibility defect, though it does not overturn the independently rechecked mathematical core.

## Originality

**Assessment: FAIL. The headline partial classification is covered by prior work.**

The decisive source is:

P. R. J. Östergård, “Classification of Binary Constant Weight Codes,” *IEEE Transactions on Information Theory* 56(8) (2010), 3779–3785. DOI: 10.1109/TIT.2010.2050922.

The full text was inspected. Its abstract on p. 3779 states that optimal binary constant-weight codes are classified up to equivalence for minimum distance (d=6) and all lengths (nle 14). Section V on p. 3782 states that the tables give exhaustive classification results and, for each listed parameter set, tabulate both (A(n,d,w)) and the number of optimal codes; Table II is specifically the table for minimum distance 6. The paper says the one still-open classification entry is in Table IV (minimum distance 10), not Table II. Therefore ((n,d,w)=(14,6,7)) lies inside an already completed exhaustive classification.

This directly contradicts the record's prior-art assessment in `AUDIT.json`, which says Östergård 2010 “contains no (14,6,7) orbit census.” The paper's stated classification range necessarily covers this parameter. Because the present audit independently verifies that two inequivalent size-42 optimal witnesses exist, an exhaustive earlier classification of the same parameter already entails that those inequivalent classes were accounted for in the earlier census, whether or not the current record's exact representatives were the ones printed in the article.

Additional checked context:
- A. E. Brouwer's current constant-weight-code table records (A(14,6,7)=42) and provides one construction, but a bounds table is not the right source for deciding whether a separate classification paper exists.
- W. G. Valiant's 1976 report “A(14,6,7) < 52 or the nonexistence of a certain constant weight code” concerns an older upper-bound step and does not rescue the 2026 novelty claim.

The 2010 paper was first sought through arXiv/preprint and lawful open-access routes; those searches did not yield the relevant full text. The same paper was then obtained through authorized institutional access and read directly. Hence this failure is based on inspected full text, not on an abstract-only inference.

## Scientific value

**Assessment: FAIL after subtracting prior coverage.**

Once Östergård's exhaustive classification is credited, the surviving content is a pair of explicit representatives plus routine invariants (distance distributions, coordinate degrees, and stabilizer orders) and a weak LP bound. These are useful reproducibility data, but the record does not identify a new regime, a new classification result, a stronger bound, a new proof method, or a reusable structural theorem. The second witness was found by a removed heuristic search, and the record explicitly does not determine the full orbit count. As a scientific finding, the remaining computations do not clear the value threshold independently of the already-known classification.

## Bounded repair considered

A bounded repair could fix all `output/artifacts/` paths to `artifacts/` and rewrite the note as a reproduction of two representatives from an already-classified parameter set, explicitly crediting Östergård 2010. That repair would correct provenance and replayability, but it would remove the claimed novel classification content. The remaining invariant calculations are routine and do not supply a comparably original and scientifically substantial replacement theorem. Therefore no bounded repair yields a record that passes all three axes.

## Final disposition

**FAILED.** The mathematical witness checks are largely correct, but the record's claimed originality is decisively false relative to Östergård 2010, and the residual computations do not constitute a sufficiently valuable standalone finding after that prior coverage is subtracted. The accepted record should therefore be withdrawn to the assigned failed-attempt path, preserving the complete package and this audit evidence.

## Sources checked
1. P. R. J. Östergård, *Classification of Binary Constant Weight Codes*, IEEE Trans. Inf. Theory 56(8) (2010), 3779–3785, DOI 10.1109/TIT.2010.2050922; full text, especially p. 3779 abstract and Section V, p. 3782.
2. A. E. Brouwer, “Bounds for constant weight codes,” https://aeb.win.tue.nl/codes/Andw.html — current table entry (A(14,6,7)=42).
3. W. G. Valiant, *A(14,6,7) < 52 or the nonexistence of a certain constant weight code* (1976), CWI repository, https://ir.cwi.nl/pub/6874.
