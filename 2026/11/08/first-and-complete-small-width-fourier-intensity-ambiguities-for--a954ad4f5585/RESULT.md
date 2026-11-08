# First and complete small-width Fourier-intensity ambiguities for binary two-row arrays

## Finding
For every integer \(1\le n\le8\), consider the \(2\times n\) arrays with every entry in \(\{-1,1\}\). The fiber of the *full continuous-torus Fourier intensity* is the set of such arrays with identical intensities, modulo global sign and simultaneous central reversal. All fibers are singletons for widths \(1,2,3,4,5,7\). Width \(6\) is the first admitting an inequivalent pair: exactly four fibers are doubles and 1048 are singletons. Width \(8\) has twelve doubles and 16488 singletons. No fiber has more than two equivalence classes through width eight. Thus nonuniqueness first appears at width six, but uniqueness returns at width seven. Every member of each width-six double fiber is nonseparable (not a tensor product of two sign vectors).

The complete exact census is:

| Width \(n\) | Trivial-equivalence classes | Singleton fibers | Double fibers |
| --- | ---: | ---: | ---: |
| 1 | 2 | 2 | 0 |
| 2 | 6 | 6 | 0 |
| 3 | 20 | 20 | 0 |
| 4 | 72 | 72 | 0 |
| 5 | 272 | 272 | 0 |
| 6 | 1056 | 1048 | 4 |
| 7 | 4160 | 4160 | 0 |
| 8 | 16512 | 16488 | 12 |

An explicit inequivalent width-six pair, with rows displayed from left to right, is

```
A: --++++     B: ----++
   +--+-+        +-+--+
```

Here `+` represents \(+1\) and `-` represents \(-1\). Both arrays have exactly the same full Fourier intensity, although neither is separable and they are not related by the allowed trivialities.

## Assumptions and scope
Let \(F=(f_{r,j})\), with \(r\in\{0,1\}\), \(0\le j<n\), and \(f_{r,j}\in\{-1,1\}\). Define the bivariate Fourier polynomial and its intensity by
\[
P_F(z,w)=\sum_{r=0}^{1}\sum_{j=0}^{n-1}f_{r,j}w^rz^j,\qquad I_F(z,w)=|P_F(z,w)|^2,\quad |z|=|w|=1.
\]
Intensities agree only if they agree at *every* pair of phases on the torus, not merely on a possibly aliased finite Fourier grid. The trivial actions are \(F\mapsto-F\) and \(f_{r,j}\mapsto f_{1-r,n-1-j}\), together with their composition. A translation of a supported array does not change intensity, but requiring its bounding rectangle to start at \((0,0)\) eliminates that redundancy. No additional row-wise or coordinate-wise reflections are assumed trivial. A fiber counts orbits under precisely those actions. The finding is a complete finite-range classification for \(1\le n\le8\); it makes no assertion for larger widths.

## Proof
**Step 1: exact reduction to correlations.** For \(u\in\{-1,0,1\}\) and \(|v|<n\), define the integer aperiodic autocorrelation
\[
C_F(u,v)=\sum_{\substack{0\le r,r+u<2\\0\le j,j+v<n}}f_{r,j}f_{r+u,j+v}.
\]
The finite Laurent expansion
\[
P_F(z,w)P_F(z^{-1},w^{-1})=\sum_{u=-1}^{1}\sum_{v=1-n}^{n-1}C_F(u,v)w^{-u}z^{-v}
\]
holds by multiplication and reindexing; changing the signs of both lag indices merely changes the convention. In particular, intensity equality on the entire torus is equivalent to equality of all the integer coefficients \(C_F(u,v)\). By \(C_F(-u,-v)=C_F(u,v)\), \(C_F(0,-v)=C_F(0,v)\), and \(C_F(0,0)=2n\), a complete signature consists of \(C_F(0,v)\) for \(1\le v<n\) and \(C_F(1,v)\) for \(1-n\le v<n\).

**Step 2: exact orbit representatives.** Encode each row by an integer \(a\) or \(b\) in \(\{0,\ldots,2^n-1\}\), with bit value one meaning sign \(-1\). Write \(R_n(a)\) for reversal of its \(n\) bits and \(M_n=2^n-1\). The triviality orbit of \((a,b)\) is exactly
\[
\{(a,b),(a\oplus M_n,b\oplus M_n),(R_n(b),R_n(a)),(R_n(b)\oplus M_n,R_n(a)\oplus M_n)\}.
\]
The lexicographically smallest ordered pair in this set is a unique representative of each orbit, even if some group operations have fixed points. Hence looping over every \(0\le a,b<2^n\) and retaining only the minimum yields an exhaustive, duplication-free set.

**Step 3: independently computed exact signatures.** For each representative, the `CHECK.py` implementation evaluates the defining sum for every nonredundant lag by direct integer summation. It also evaluates the same signature from XOR Hamming distances. For example, if \(v>0\),
\[
C_F(0,v)=2(n-v)-2\Big(\operatorname{popcount}((a\oplus(a\mathbin{\gg}v))\mathbin{\&}M_{n-v})+\operatorname{popcount}((b\oplus(b\mathbin{\gg}v))\mathbin{\&}M_{n-v})\Big).
\]
For \(v\ge0\),
\[
C_F(1,v)=n-v-2\operatorname{popcount}((a\oplus(b\mathbin{\gg}v))\mathbin{\&}M_{n-v});
\]
for negative \(v\), interchange the shifted row as specified in `CHECK.py`. Both algorithms agree *for every enumerated representative*. Grouping their exact complete signatures and counting the resulting groups gives precisely the table in the Finding section. This establishes the exhaustive finite theorem; there is no floating-point comparison, random sampling, or inference beyond width eight.

**Step 4: the explicit nontrivial pair.** Put \(F(z)=z^4+z^2-1\), its reciprocal \(F^*(z)=z^4F(z^{-1})=1+z^2-z^4\), and \(H(z,w)=(1+z)+w(z-1)\). The displayed arrays satisfy \(P_A=F H\) and \(P_B=-F^* H\). Because \(|F(z)|=|F^*(z)|\) when \(|z|=1\), their intensities agree. They are inequivalent under global sign and central reversal (their distinct canonical bit representatives are \((3,22)\) and \((15,26)\)); neither pair of rows is equal or opposite, so neither array separates as a rank-one sign tensor. The other three width-six double fibers, and the absence of further ones, follow from the exhaustive classification in Step 3. This factor-reciprocal ambiguity mechanism itself is classical; the new assertion is the exact binary two-row small-width classification.

## Verification
Run `python3 CHECK.py` using the Python standard library. It enumerates all \(2^{2n}\) full-support binary arrays at every width \(1\le n\le8\), retaining canonical orbit representatives. It independently computes their signatures by direct integer correlations and bit-popcounts, checks agreement for each representative, groups complete signatures, asserts every census entry, verifies every width-six double fiber is nonseparable, and rechecks the four width-six ambiguous fibers via direct coefficient multiplication of the two-dimensional Laurent autocorrelation polynomial. It independently verifies the displayed pair. Expected terminal line: `ALL_EXACT_TWO_ROW_CHECKS_PASSED`. The exhaustive finite code, including the exact loop bounds and comparisons, is part of the proof certificate.

## Relationship to prior work
Multidimensional phase retrieval ambiguities, including constructions by finite differences and oblique tensorization, are developed by Novikov and Xu (2024, 2026). Their general constructions do not state the complete finite \(\{-1,1\}\)-valued two-row census or the sharp first ambiguous width. Grohs, Koppensteiner, and Rathmair give a general polynomial-factorization description of discrete Fourier ambiguities; it explains the reciprocal factor flip in Step 4, not the reported constrained-alphabet fiber counts. Katz, Rahman, and Ward classify and search *one-dimensional* binary sequences and report no nontrivial pairs at lengths one through eight; their one-dimensional result is not an implication about two-row arrays. A published enumeration of \(4\times4\) binary Fourier fourth-moment optimizers studies a scalar norm, not equality of the full intensity functions or the present rectangular family.

## Limitations
No claim is made for width \(n\ge9\), nonbinary coefficients, discrete-grid-only measurements, or equivalence under extra symmetries such as independent coordinate reflections. The proof for the finite table is an exhaustive exact-integer computation with fully specified source; it is not a short symbolic classification of all factor patterns. Classical polynomial factor flipping can generate the exhibited pair; priority of the **numerical two-row census** remains subject to checking any earlier specialized tables under homometric-array terminology. The result has not undergone an independent mathematical audit.

## References
1. R. G. Novikov and T. Xu, *On phase retrieval for continuous and discrete Fourier transforms*, arXiv:2604.25662 (first public 2026-04-28), https://arxiv.org/abs/2604.25662.
2. R. G. Novikov and T. Xu, *On non-uniqueness of phase retrieval in multidimensions*, arXiv:2407.05030 (2024), https://arxiv.org/abs/2407.05030.
3. P. Grohs, S. Koppensteiner, and M. Rathmair, *Phase retrieval: uniqueness and stability*, arXiv:1901.07911 (2019), https://arxiv.org/abs/1901.07911.
4. D. J. Katz, A. Rahman, and M. J. Ward, *Sequences with identical autocorrelation functions*, arXiv:2308.07467 (2023), https://arxiv.org/abs/2308.07467.
