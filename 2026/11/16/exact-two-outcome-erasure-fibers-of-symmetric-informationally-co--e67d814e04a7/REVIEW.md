# Scientific assessment: exact two-outcome erasure fibers of SIC measurements

## Correctness — PASS

The SIC Gram matrix is invertible, with trace-dual projectors \(D_j=((d+1)P_j-I)/d\). Deleting two intensity coordinates makes the Hermitian kernel exactly the two-plane spanned by their duals. Differences of **normalized** pure-state projectors have trace zero, forcing the kernel difference to be a multiple of \(P_r-P_s\). Its range is precisely the linearly two-dimensional span of the removed SIC vectors. In its Hermitian eigenbasis, the off-diagonal equality problem has exactly the original projective point and one reflected partner. This proves both completeness and absence of other fibers, including the equator and outside-support boundaries. The probability/chordal formula follows from the exact SIC overlap. The extension to unknown norm in dimensions at least four follows from the rank-at-most-two restriction on the same kernel plane, and the three-dimensional exception is exhibited by the spectrum \(\{4/3,0,-2/3\}\). The algebraic argument is independent of numerical tests.

## Originality — PASS on inspected sources, provisional publication priority

The 2003/2004 SIC paper by Renes et al. supplies the projector geometry and complete-tomography starting point; this result adds a complete classification of the fibers after deleting exactly two original (unrenormalized) probabilities. Edidin--Gonzalez--Tamo (November 12, 2025) investigate pure-state informational completeness and minimal POVMs and formulate deletion/completion questions, but the inspected material does not determine this SIC-specific reflected projective line. Their conditional or rescaled postselection convention is distinguishable from fixed retained original outcome probabilities. Li (September 9, 2026) obtains phase-retrievable finite Gabor windows and limited robust-erasure results, not the claimed two-deletion SIC fiber geometry. Searches of the mathematical results database and prior mathematical claims did not show an equivalent or stronger result. This is not a proof of novelty; equivalent older SIC tomography formulations remain a residual risk.

## Mathematical value — PASS

The theorem resolves an exact and natural erasure-identifiability question for a maximally symmetric, minimal informationally complete frame. Its one-versus-two loss threshold is sharp, and more significantly the **entire noninjective locus**, the precise two-point fibers, the exact geometric-to-probability ambiguity conversion, and the normalization-sensitive dimensional boundary are determined. This offers more than an isolated negative example or a re-expression of frame duality: it describes which pure states are genuinely indistinguishable and by exactly how much.

## Limits of verification

SIC existence is an assumption. The proof is exact, conditional on it. The Hesse SIC numerical test validates one concrete low-dimensional example only. Prior-art and terminology differences, notably conditional probabilities, leave some historical equivalence risk. No independent mathematical assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
