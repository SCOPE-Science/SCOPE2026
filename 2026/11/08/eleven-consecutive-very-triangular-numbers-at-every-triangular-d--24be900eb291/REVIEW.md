# Scientific review

## Correctness — PASS

The theorem has explicit quantifiers: for each triangular \(H=t(t+1)/2\), \(t\ge13\), and each integer \(K\ge L+30\), the indices \(q2^K+36{,}853{,}059+j\), \(0\le j\le10\), are consecutive and give exactly \(H\) set bits. The eleven hexadecimal seed values directly verify the common digit weight \(26\). The repunit identity \(s_2(A(2^L-1))=L\) for \(1\le A<2^L\) follows from complementary \(L\)-bit blocks. The exact decomposition for \(9(2^L-1)^2\) gives the odd-weight branch. Strict block-size inequalities rule out carries in the quadratic expansion, and both parities evaluate to the requested \(H\). The companion integer-arithmetic checker reproduces the seed and boundary examples. Limit: finite testing alone would not prove the infinitely many values of \(K\); the algebraic identity does.

## Originality — PASS within inspected evidence

The closest primary source is Baumheckel–Forgács, arXiv:2105.10354. Its Theorem 2.2 gives each triangular weight for *individual* terms, Proposition 3.9 gives stability within a specified binary-shift range, and Corollary 3.10 obtains *six* consecutive very triangular numbers. Those assertions do not state or logically force eleven consecutive indices for every triangular \(H\ge91\). The new statement couples an exact eleven-term seed with a separate repunit weight-lifting mechanism. Search variants involving consecutive triangular indices, Hamming weight, very triangular numbers, repunit lifting, and eleven-term blocks disclosed no equivalent result in the sources checked. An unindexed equivalent or an implicit reduction in less-visible literature remains possible; searches do not certify uniqueness.

## Mathematical value — PASS

The problem is explicitly motivated by Baumheckel–Forgács's consecutive-run theorem and their longer-arithmetic-progression conjecture. The new theorem advances the known explicit consecutive-run length from six to eleven and, more strongly, supplies infinitely many blocks for **every prescribed sufficiently large triangular digit weight** rather than a single chosen weight. Both features concern a natural invariant (binary Hamming weight of triangular numbers) and have a uniform structural proof; the precise value eleven comes from an exactly checkable seed, not an arbitrary parameter restriction. Limit: the general arbitrary-length conjecture is not settled.

## References and residual risks

Closest primary document: *An exploration of very triangular numbers*, https://arxiv.org/pdf/2105.10354 (Sections 2–3, pp. 1–8 and concluding discussion); first public date 2021-05-19. The journal DOI is https://doi.org/10.46787/pump.v6i0.3853 . The original author-described six-consecutive corollary is clear, but a fully exhaustive historical priority review across all publications has not been performed. Results are not independently audited.

Self-review: passed. Independent audit: not yet performed.
