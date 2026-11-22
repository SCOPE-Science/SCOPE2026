# Sharp mixed-norm amplification for row-dominant triangular inverses

## Finding

Fix a real threshold \(0<\tau<1\). Among all unit lower-triangular real or complex matrices \(T=I-G\) of order \(n\), with \(G\) strictly lower triangular and every absolute off-diagonal row sum at most \(\tau\), the **exact** largest squared Frobenius inverse defect is

\[
\max_T\|T^{-1}-I\|_F^2=\sum_{h=1}^{n-1}(n-h)\tau^{2h}.
\]

In contrast, their **sharp dimension-normalized Euclidean inverse gain** is

\[
\lim_{n\to\infty}\frac{1}{\sqrt n}\max_T\|T^{-1}\|_2=\frac{\tau}{\sqrt{1-\tau^2}}.
\]

A weighted chain attains the finite Frobenius maximum; a chain with an increasing number of terminal leaves attains the asymptotic spectral-norm coefficient. Hence a dimension-independent strict row-diagonal-dominance bound does not imply dimension-uniform Euclidean inverse conditioning, even for triangular matrices all of whose eigenvalues equal one.

## Assumptions and scope

Let \(n\ge1\), \(0<\tau<1\), and let \(\mathcal U_n(\tau)\) consist of all matrices \(T=I-G\in\mathbb F^{n\times n}\), \(\mathbb F\in\{\mathbb R,\mathbb C\}\), such that \(G_{ij}=0\) for \(j\ge i\) and \(\sum_{j<i}|G_{ij}|\le\tau\) for every row \(i\). The Euclidean operator norm is \(\|\cdot\|_2\), the Frobenius norm is \(\|\cdot\|_F\), and the identity is \(I\). Matrix indices in the proof begin at one. Write

\[
F_n(\tau):=\sum_{h=1}^{n-1}(n-h)\tau^{2h}.
\]

The two maxima are taken over the entire class, not merely matrices with one nonzero per row. The finite Frobenius identity includes \(n=1\), when its sum is zero. The second assertion is an asymptotic maximum, not a claim of an exact finite-order spectral-norm maximizer.

## Proof

**Row bound.** Because \(G\) is nilpotent, \(B=T^{-1}=I+G+\cdots+G^{n-1}\) exists. Let \(r_i=e_i^{*}B\) denote row \(i\), with conjugation understood when applicable. From \(B=I+GB\),

\[
r_i=e_i^{*}+\sum_{j<i}G_{ij}r_j.
\]

Each \(r_j\) has support confined to columns \(1,\ldots,j\), so \(e_i^{*}\) is orthogonal to every \(r_j\) with \(j<i\). The triangle inequality and the row budget therefore give

\[
\|r_i-e_i^{*}\|_2\le\tau\max_{j<i}\|r_j\|_2,
\qquad
\|r_i\|_2^2=1+\|r_i-e_i^{*}\|_2^2.
\]

Starting at \(\|r_1\|_2=1\), induction proves, simultaneously for all \(i\),

\[
\|r_i\|_2^2\le\sum_{h=0}^{i-1}\tau^{2h},
\qquad
\|r_i-e_i^{*}\|_2^2\le\sum_{h=1}^{i-1}\tau^{2h}.
\]

**Exact Frobenius extremum.** Summing the squared inverse defects of the rows yields

\[
\|B-I\|_F^2\le\sum_{i=1}^{n}\sum_{h=1}^{i-1}\tau^{2h}
=\sum_{h=1}^{n-1}(n-h)\tau^{2h}=F_n(\tau).
\]

For the weighted bidiagonal chain, put \(G_{i,i-1}=\tau\) for \(2\le i\le n\), all other entries zero. Then \(r_i=e_i^{*}+\tau r_{i-1}\), with perpendicular summands. Thus every displayed row inequality is an equality, proving the claimed exact finite maximum. For this chain, \(\|B\|_2\le\sum_{h=0}^{n-1}\tau^h\le(1-\tau)^{-1}\); it is not an asymptotic spectral maximizer.

**Universal spectral upper bound.** The Frobenius estimate implies

\[
\|B\|_2\le1+\|B-I\|_2\le1+\sqrt{F_n(\tau)}.
\]

Since \(F_n(\tau)/n\longrightarrow\sum_{h\ge1}\tau^{2h}=\tau^2/(1-\tau^2)\), the limit superior of the normalized spectral maximum is at most \(\tau/\sqrt{1-\tau^2}\).

**Matching comb lower bound.** For each sufficiently large \(n\), choose \(k=\lfloor\sqrt n\rfloor\), so \(k+1<n\). Construct \(G\) from a length-\(k\) chain and \(n-k-1\) terminal leaves:

\[
G_{i,i-1}=\tau\quad(2\le i\le k+1),\qquad
G_{i,k+1}=\tau\quad(k+2\le i\le n),
\]

with every other entry zero. Each nonzero row has absolute row sum exactly \(\tau\). For a leaf row \(i>k+1\), the first \(k+1\) entries of row \(i\) of \(B\) are precisely \((\tau^{k+1},\tau^k,\ldots,\tau)\), of squared Euclidean norm \(\sum_{h=1}^{k+1}\tau^{2h}\). Choose a Euclidean unit input vector supported on those first \(k+1\) coordinates, proportional to that vector (using conjugate phases in the complex setting). Each of the \(n-k-1\) leaf output coordinates then equals its norm. Hence

\[
\|B\|_2\ge\sqrt{n-k-1}\,\tau
\sqrt{\frac{1-\tau^{2(k+1)}}{1-\tau^2}}.
\]

Because \(k\to\infty\) and \(k/n\to0\), this lower bound divided by \(\sqrt n\) tends to \(\tau/\sqrt{1-\tau^2}\), matching the upper bound. The two norm laws follow.

**Strict-threshold convention.** If the application insists on \(\sum_{j<i}|G_{ij}|<\tau\), the displayed finite maxima become suprema, approached by chains whose weight tends to \(\tau\) from below. For the asymptotic lower bound, replace the comb weight by \(\tau(1-1/n)\); the leading coefficient is unchanged.

## Verification

The included `checker.py` verifies exact-rational row and Frobenius bounds for every deterministic parent-forest pattern up to order six at three rational thresholds, including the attaining chain. It also checks 360 sampled signed, row-budgeted triangular matrices and nine comb test cases, for 15,117 exact-rational row assertions and 369 finite numerical cases. Run `python3 checker.py` with NumPy installed. These finite calculations exercise the formulas but do not replace the general algebraic proof above.

## Relationship to prior work

Dargaville and Pain introduce a coarse/fine splitting that constrains fine-fine row diagonal-dominance ratios, and analyze iterative triangular solves and their nonnormal behavior; they do not state the two extremal inverse-norm formulas. Standard row-diagonal-dominance inverse bounds, notably the infinity-norm theory associated with Varah and the Skeel-condition analyses of Peña, control different quantities. Echeverría, Liesen and Nabben give inverse-decay estimates for block-tridiagonal systems rather than the unrestricted triangular row-budget class here. The present chain and comb constructions distinguish a sharp Frobenius inverse defect from a sharp asymptotic Euclidean inverse gain.

## Limitations

The result is for exact arithmetic, unit diagonal, fixed \(0<\tau<1\), all strictly lower-triangular sparsity patterns, and two specified norms. It does not assert that a particular ILU construction produces the comb, that an entire coarse/fine preconditioner has poor convergence, or that the asymptotic coefficient is a finite-order optimum formula. A row ratio by itself gives no column-sum or spectral contraction hypothesis. Earlier unindexed equivalent extremal-norm bounds remain a possible priority risk.

## References

1. S. Dargaville and C. C. Pain, *A comparison of parallel iterative methods for ILU triangular solves*, arXiv:2611.00552v1, first public 2026-10-31, especially Sections 4–6.2. https://arxiv.org/html/2611.00552v1
2. C. Echeverría, J. Liesen and R. Nabben, *Block diagonal dominance of matrices revisited: bounds for the norms of inverses and eigenvalue inclusion sets*, arXiv:1712.05662, 2017. https://arxiv.org/abs/1712.05662
3. J. M. Peña, *Strict diagonal dominance and optimal bounds for the Skeel condition number*, SIAM J. Numer. Anal. 45 (2007), 1107–1108; see also Shuhuang Xiang's 2010 correction. https://doi.org/10.1137/060677562
4. J. M. Peña, *Scaled pivots and scaled partial pivoting strategies*, SIAM J. Numer. Anal., DOI:10.1137/S0036142901395163, for dimension-independent Skeel conditioning under strict row diagonal dominance. https://doi.org/10.1137/S0036142901395163
