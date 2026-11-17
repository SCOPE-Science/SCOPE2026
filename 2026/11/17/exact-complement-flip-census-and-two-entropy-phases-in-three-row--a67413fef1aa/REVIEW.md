# Scientific review

## Correctness — PASS

The exact quantifier is every integer \(n\ge3\) on a labelled, three-row torus with eight distinct Moore neighbors. A direct neighbor-sum argument equates full inversion after one update to the local constraint \(w_{j-1}+w_j+w_{j+1}\in\{3,6\}\). A sixteen-state weighted closed-walk matrix counts every permitted cyclic column-weight sequence with all \(\binom3w\) row choices. Its characteristic polynomial was independently reconstructed by exact Newton identities from its full integer matrix and its factorization checked coefficient by coefficient. The resulting trace identity gives the claimed all-length formula. The complement-equivariant update guarantees that all counted states have least temporal period two. An independent, cell-by-cell C++ simulator reproduced the complete state census at every circumference from three through seven. No inference about infinitely many circumferences comes from finite experiments alone.

## Originality — PASS, qualified

Bell's 1997 primary account establishes the Day & Night rule, complement equivariance, and many specific localized oscillators but does not present a finite-strip complete-inversion census in the inspected text. Eppstein's 2009 full HTML preprint explicitly discusses the same symmetry and the strobing dual, but is a qualitative classification of growth, death, and patterns. The natural equivalence \(F(x)=\overline x\iff (\overline F)(x)=x\) was considered: the theorem is also a complete fixed-state count for the strobing dual B01245/S0125, not a claim that such a dual is new. Searches for this formulation and exact three-row formulas found no identical statement. A third-party pattern archive or an uninspected later part of Bell's five-part catalogue might contain an equivalent finite census; absolute priority is not established. The preceding generalized three-row fixed-point results for other rules are neither a proof nor a direct corollary of this theorem.

## Mathematical value — PASS

Full-state inversion is a canonical dynamical event in a self-complementary automaton and necessarily yields a primitive temporal two-cycle. The exact census is motivated by this specific symmetry, not by arbitrary parameter selection. It shows a nontrivial arithmetic resonance at circumferences divisible by three, a complete natural invariant for every width-three circumference, and two incompatible column-density-one and column-density-two ensembles of equal leading entropy. The all-length theorem distinguishes the two exponentially dominant oscillating phases from genuinely smaller correction sectors. No downstream general theorem is required to make this exact classification informative.

## Principal evidence and limitations

See `RESULT.md` for the complete local equivalence, exact matrix, polynomial factorization, trace argument and scope. `transfer_verify.py` constructs the matrix and checks all polynomial coefficients using standard-library integer arithmetic; `direct_verify.cpp` independently enumerates and evolves every binary state through circumference seven. Both sources were recompiled or executed and their actual outputs captured in `transfer_output.txt` and `direct_output.txt`. The checks do not constitute independent external review. The scope excludes all non-complementary period-two oscillators and higher periods. Closest literature includes Bell's 1997 Day & Night description and Eppstein's 2009 semitotalistic automaton classification.

Self-review: passed. Independent audit: not yet performed.
