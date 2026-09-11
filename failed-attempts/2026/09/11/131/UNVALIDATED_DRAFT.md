# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Self-orthogonal-member exclusion for 3-MOLS(10): the constant-diagonal subtype is empty by counting

## Claim (TARGET, positive/exclusion resolution)

No Latin square of any order $n \ge 2$ — in particular no member of any triple
of mutually orthogonal Latin squares of order 10, equivalently no distinguished
row-class of any OA(5,10) — can be simultaneously orthogonal to its own
transpose and have constant diagonal symbols. Hence no 3-MOLS(10) contains a
constant-diagonal self-orthogonal member. The subtype is empty already at the
single-square level, with no Latin property, no triple orthogonality, and no
solver search required.

## Definitions

- A **Latin square** $L$ of order $n$ is an $n \times n$ array over an
  $n$-symbol alphabet with each symbol once per row and column.
- $L$ is **orthogonal to its transpose** $L^T$ (self-orthogonal) if the $n^2$
  ordered pairs $(L[i][j], L[j][i])$ are pairwise distinct.
- $L$ has **constant diagonal** if $L[i][i] = c$ for all $i$ and some symbol $c$.
- 3-MOLS(10) $\equiv$ OA(5,10) is standard; only the single distinguished member
  matters here.

## Theorem and proof

**Theorem.** For every $n \ge 2$, no $n \times n$ array (Latin or otherwise) with
constant diagonal is orthogonal to its transpose.

**Proof.** Suppose $L[i][i] = c$ for all $i$. In the superposition of $L$ with
$L^T$, each diagonal cell $(i,i)$ carries the pair $(L[i][i], L[i][i]) = (c,c)$.
Thus the pair $(c,c)$ occurs at least $n \ge 2$ times among the $n^2$
superposition pairs, which are therefore not pairwise distinct. So $L$ is not
orthogonal to $L^T$. ∎

**Corollary (target).** No 3-MOLS(10) contains a member that is orthogonal to
its own transpose when normalized to constant diagonal symbols — there is no
such square at all. The exclusion resolution of the target holds.

## Remarks on normalization readings

The target phrase "when normalized to constant diagonal symbols" admits two
readings; the exclusion holds under both:

1. **Literal conjunction** (proved above): a square that *is* self-orthogonal
   *and has* constant diagonal. Empty for all $n \ge 2$ by the Theorem.
2. **Attainability reading**: "every self-orthogonal member can be put in
   constant-diagonal form by the declared isotopism." This normalization is
   unattainable, so the subtype is still empty. Indeed, a self-orthogonal
   square's diagonal is necessarily a **transversal** (all $n$ symbols exactly
   once): its diagonal superposition pairs $(d_i, d_i)$ must be pairwise
   distinct, forcing the $d_i$ pairwise distinct. The isotopisms preserving
   self-orthogonality — simultaneous row/column permutations plus symbol
   permutations — preserve diagonal distinctness, so no self-orthogonal square
   can be moved to constant diagonal without destroying self-orthogonality.
   (General isotopisms can force a constant diagonal onto a Latin square, but
   they do not preserve the transpose-orthogonality property.)

**Correction to the admission preflight.** The preflight's nonvacuity premise —
"self-orthogonal Latin squares with constant diagonal are a consistent
single-square class at order 10" — is false: no such square exists at *any*
order $n \ge 2$, by the Theorem above. Single-square self-orthogonality itself
is of course real (e.g. the SOLS(5) below; existence for all $n \ne 2,3,6$ is
the Brayton–Coppersmith–Hoffman theorem, cited here as background, not
re-verified), but it always forces a transversal, never constant, diagonal.
The error points in the direction that strengthens the exclusion into a
one-line theorem rather than weakening it.

## Computational cross-check (stdlib only, replayable)

`output/artifacts/verify.py` (`python3 output/artifacts/verify.py` →
`VERIFY_OK`) independently corroborates every layer that can be checked
mechanically:

- **General lemma instances** ($n = 2,3,4,5,10$): a constant-diagonal array
  repeats one transpose-superposition pair $n$ times — confirmed.
- **Exhaustive $n = 2$**: both Latin squares checked; none is simultaneously
  self-orthogonal and constant-diagonal.
- **Exhaustive $n = 3$**: all 12 Latin squares checked; 0 are self-orthogonal
  (consistent with the classical nonexistence of SOLS(3)) and none meets the
  conjunction.
- **Exhaustive $n = 4$**: all 576 Latin squares checked; 48 are
  self-orthogonal, every one of them has a transversal (all-distinct) diagonal,
  and none has constant diagonal.
- **Witness SOLS(5)** with transversal diagonal, $L[i][j] = i + 2j \pmod 5$:

  | 0 2 4 1 3 |
  | 1 3 0 2 4 |
  | 2 4 1 3 0 |
  | 3 0 2 4 1 |
  | 4 1 3 0 2 |

  verified Latin, self-orthogonal, diagonal $(0,3,1,4,2)$ all-distinct —
  showing the single-square class is nonempty but always transversal-diagonal.
- **Isotopism-invariance sanity**: a random simultaneous row/column permutation
  plus symbol relabelling of the SOLS(5) preserves both self-orthogonality and
  diagonal distinctness, confirming reading (2) above.

## What is and is not decided

- **Decided**: the exact posed subtype — constant-diagonal self-orthogonal
  member of a 3-MOLS(10) — is excluded, rigorously and in closed form.
- **Not decided**: the scientifically interesting neighbours — a 3-MOLS(10)
  containing a self-orthogonal member with (necessary) transversal diagonal,
  and general 3-MOLS(10) existence — are untouched; the proof uses only the
  diagonal cells and says nothing about them. Isotopic variants of
  transpose-orthogonality (e.g. orthogonality to a symbol-permuted transpose)
  are likewise outside the literal statement and not addressed.

## Reproduction

```
python3 output/artifacts/verify.py   # expect VERIFY_OK (stdlib only, seconds)
```

No SAT solver, no external package, and no literature lookup is needed for the
proof; the script is corroborating evidence, and the Theorem stands on its own.
