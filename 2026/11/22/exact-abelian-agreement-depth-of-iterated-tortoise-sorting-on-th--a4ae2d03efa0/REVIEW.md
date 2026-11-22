# Scientific review

## Correctness — PASS

The proof is all-integer and self-contained once the standard Thue–Morse complementary-pair identity and the cited definition of tortoise are fixed. Complete sorting holds through length \(2k\), including the potentially exceptional weight-\(k+1\) factors of length \(2k\), which must end in one. At length \(2k+1\) there are exactly two high-weight outputs, separated by the position of the final one; explicit digit-sum witnesses establish that both occur. A third image comes from a lower-weight factor. The direct-operator and morphic factor computations are independently reproducible but are supplementary, not a proof for unbounded \(k\).

## Originality — PASS against checked coverage

Campbell and Rampersad, arXiv:2604.25811 (first public April 28, 2026), define iterated tortoise complexity and invite evaluation of Abelian-agreement depth for Thue–Morse, but give the one-pass complexity instead. The two closely related full published results, *Exact two-tortoise complexity of the Thue–Morse word from length eighteen* and *Exact maximal two-tortoise fiber spectrum of Thue–Morse factors*, concern only exactly two passes and different invariants; neither states this all-iteration sharp first-divergence formula. Equivalent descriptions, stronger coverage and existing tables were compared via indexed claims and relevant primary full text. An implicit or unindexed derivation from elementary substitution identities is still a priority risk.

## Mathematical value — PASS

The theorem resolves a specifically proposed natural numerical invariant in a recent study: it supplies the exact all-iteration agreement-depth function \(\operatorname{abel}_{\mathbf t}(k)=2k\), plus the complete three-image threshold profile. This sharp boundary measures precisely when repeated partial sorting ceases to erase all positional information beyond Abelian counts. It is not merely a finite experimental improvement or an arbitrary parameter slice.

## Scope and limitations

The formula concerns the binary Thue–Morse word and the first failure of agreement. It does not determine general \(k\)-tortoise complexity at all later lengths, nor the behavior of other automatic words. The literature comparison does not establish global priority, and no independent scientific audit has yet occurred.

Self-review: passed. Independent audit: not yet performed.
