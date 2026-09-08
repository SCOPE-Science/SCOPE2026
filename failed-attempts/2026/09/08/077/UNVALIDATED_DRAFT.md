# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified same-permutation conjugacy separation for positive 4-braids with Dehornoy comparison and closure-genus log

## 1. Statement

Work in the braid group $B_4$ with Artin generators $\sigma_1,\sigma_2,\sigma_3$
(indexed $0,1,2$ in code). Let

- $X = \sigma_1^2\sigma_2$ (word $(0,0,1)$),
- $Y = \sigma_1^2\sigma_2\sigma_1^2$ (word $(0,0,1,0,0)$).

**Theorem (extremal-witness lemma).**
(i) $X$ and $Y$ are positive $4$-braids of Garside canonical length $2 \le 10$
with identical Artin permutation $(0,2,1,3)$.
(ii) Their summit invariants differ: $X$ has $(\inf_s,\ell_s)=(0,1)$ and $Y$
has $(\inf_s,\ell_s)=(0,2)$. Hence $X$ and $Y$ are **not conjugate** in $B_4$.
(iii) $X^{-1}Y = \sigma_1^2$ on the nose after free reduction, so $X < Y$ in the
Dehornoy left order and $X \ne Y$.
(iv) Both closures are $3$-component links with $4$ Seifert circles;
$\chi(\hat X)=1$ (3 crossings) vs $\chi(\hat Y)=-1$ (5 crossings).

## 2. Method and replay

Classical Garside structure is implemented from scratch on permutations
(`artifacts/garside.py`): simple elements as permutations with stacked
composition, left-weightedness via correct descent sets
($S(s)$ = descents of $s$, $F(a)$ = descents of $a^{-1}$), meet via largest
biclosed inversion subset, local sliding normalization. Cycling/decycling with
$\Delta$-absorption and summit-orbit extraction in `artifacts/invariants.py`.
The braid word problem and conjugation certificates use the faithful Artin
action on the free group $F_4$ (`artifacts/dehornoy2.py`), cross-checked by
free reduction.

Replay: `python3 artifacts/verify.py` prints 22 PASS lines and `VERIFY_OK`:
normal-form weightedness, permutation-product identity, same-permutation
check, summit values, per-step cycling-equals-conjugation certificates
($e_{\mathrm{next}} = A_1^{-1} e A_1$ verified through the Artin action),
$X^{-1}Y \to [1,1]$ free reduction with $X\cdot(X^{-1}Y)=Y$, and closure data.
A bounded census corpus (`artifacts/census_raw.json`: 2047 words $n=3$,
$3280$ words $n=4$) with 40/60 same-(length,permutation) multi-summit groups
provides context.

## 3. Proofs of the one-sided bounds used

- *Summit invariants are conjugacy invariants.* Cycling
$c(x)=\tau^{-p}(A_1)^{-1}x\,\tau^{-p}(A_1)$ and decycling are conjugations
preserving the conjugacy class; the summit infimum (maximal infimum over the
class) and the canonical length at summit level are therefore class
invariants. Distinct $(\inf_s,\ell_s)$ implies non-conjugacy. The conjugation
identity for each logged cycling step is machine-checked via the faithful
Artin representation (not assumed).
- *Dehornoy comparison.* A word in which the smallest-index generator occurs
with only one sign is $\sigma$-positive by definition; $[1,1]=\sigma_1^2$ is
such a word, is nontrivial (faithful action), and $X\cdot\sigma_1^2=Y$ as
braids (action-checked). Hence $X^{-1}Y>1$, i.e. $X<Y$.
- *Seifert data.* Lemma: oriented (Seifert) smoothing at every crossing of a
closed-braid diagram runs strands straight through, so the Seifert circles
are exactly the $n$ strands ($s=4$ here); see `artifacts/seifert_note.txt`.
Components $\mu=3$ come from cycles of the common permutation; $\chi=s-c$.

## 4. Scope, originality, limits (honest)

- This is the **fallback claim** of the admitted topic: a certified
extremal-witness lemma, not the full $(n,\mathrm{length})$ class-count table
over canonical length $\le 10$ (the $n=4$ enumeration covered word-length
$\le 7$, hence canonical lengths $\le 7$ only; the complete length-$\le 10$
census is not claimed).
- Novelty relative to cited priors: Chen–Suen gives a closed form only for
$3$-braids; Birman–Ko–Lee/Caruso give general machinery and exponential
worst-case bounds, not this explicit same-permutation pair with replayable
cycling, Dehornoy, and closure logs. No prior art consulted here publishes
this witness.
- Uncertainty: none material to the four assertions; all are machine-replayed
from the committed words. Generalization beyond the pair (e.g. minimality of
the example, full class counts) is conjectural and not claimed.
