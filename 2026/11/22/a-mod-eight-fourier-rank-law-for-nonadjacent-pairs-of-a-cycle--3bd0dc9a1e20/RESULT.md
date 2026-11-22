# A mod-eight Fourier rank law for nonadjacent pairs of a cycle

## Finding

For each integer \(n\ge4\), let \(C_n\) be the simple labelled cycle on \(\mathbb Z/n\mathbb Z\). On the additive group \(G_n=\mathbb F_2^n\), let \(f_n\) be the indicator of the incidence vectors of independent vertex pairs of \(C_n\): vectors with exactly two ones, in nonadjacent coordinates. Counting convolution \(T_nu=f_n*u\) on complex-valued functions on \(G_n\) is invertible **if and only if**

\[
n\not\equiv0\pmod4\quad\text{and}\quad n\not\equiv3\pmod8.
\]

Equivalently, singularity occurs exactly for the residue classes \(n\equiv0,3,4\pmod8\). The complete zero set and its multiplicities have the following exact formulas. For a Fourier frequency \(S\subseteq\mathbb Z/n\mathbb Z\), write \(k=|S|\) and \(t(S)=\#\{i:\mathbf1_S(i)\ne\mathbf1_S(i+1)\}\). Its unnormalized Walsh multiplier is

\[
W_n(S)=\frac{(n-2k)^2-3n+4t(S)}2.
\]

For nonconstant masks \(0<k<n\), put \(j=t(S)/2\). The multiplier vanishes precisely when

\[
8j=3n-(n-2k)^2,
\qquad1\le j\le\min\{k,n-k\}.
\]

Let \(j_k=(3n-(n-2k)^2)/8\). With the convention that an invalid or nonintegral \(j_k\) contributes zero, the convolution nullity is

\[
\operatorname{nullity}(T_n)=
\sum_{\substack{1\le k\le n-1\\ j_k\in\mathbb Z,\ 1\le j_k\le\min(k,n-k)}}
\frac{n}{j_k}\binom{k-1}{j_k-1}\binom{n-k-1}{j_k-1},
\qquad\operatorname{rank}(T_n)=2^n-\operatorname{nullity}(T_n).
\]

This gives exact information loss for every cycle length, not only the singularity dichotomy.

## Assumptions and scope

The cycle is simple and has at least four vertices. Independent vertex pairs are **unordered**; each contributes once. Fourier characters are \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\); transforms and convolution are unnormalized. Ranks and nullities are over \(\mathbb C\), and the operator acts on all \(2^n\) functions on \(G_n\). No other sizes of independent sets are included.

## Proof

Fix \(S\), write \(s_i=(-1)^{\mathbf1_S(i)}\), so \(s_i\in\{-1,+1\}\) and \(\sum_i s_i=n-2k\). Summing \(s_is_l\) over all unordered distinct pairs gives

\[
\sum_{i<l}s_is_l=\tfrac12\bigl((n-2k)^2-n\bigr).
\]

The independent pairs in the cycle are all unordered pairs except the \(n\) adjacent pairs. For an adjacent pair \(\{i,i+1\}\), its product equals \(+1\) if the two signs agree and \(-1\) otherwise. Hence \(\sum_i s_is_{i+1}=n-2t(S)\). Subtracting proves the stated exact multiplier. Walsh characters diagonalize convolution, so its nullspace consists precisely of characters with zero multiplier.

If \(k=0\) or \(k=n\), then \(t=0\) and \(W_n(S)=n(n-3)/2>0\). Otherwise cyclic changes between signs occur in an even number \(t=2j\), with \(1\le j\le\min(k,n-k)\). The stated integer equation is thus an exact equivalence.

To classify its possible solutions, reduce \(8j=3n-(n-2k)^2\) modulo eight. If \(n\) is odd, \(n-2k\) is odd and its square is \(1\pmod8\); therefore \(n\equiv3\pmod8\). If \(n\) is even, its square is \(0\) or \(4\pmod8\), forcing \(n\equiv0\pmod4\). Conversely every allowed length has a legal pair \((k,j)\): for \(n\equiv0\pmod8\), choose \(k=n/2\), \(j=3n/8\); for \(n\equiv4\pmod8\), choose \(k=n/2-1\), \(j=(3n-4)/8\); and for \(n\equiv3\pmod8\) with \(n\ge4\), choose \(k=(n-1)/2\), \(j=(3n-1)/8\). The bounds on \(j\) hold in each case (the last case first occurs at \(n=11\)). A cyclic sign word with \(k\) negative signs and \(j\) negative runs exists for each legal \((k,j)\), proving singularity.

For the exact nullity count, cyclic sign words with \(k\) negative entries and \(j\) negative runs have \(j\) alternating positive runs. Their positive and negative run lengths are ordered positive compositions, counted by \(\binom{k-1}{j-1}\binom{n-k-1}{j-1}\). Choosing a labelled starting transition gives \(n\) placements, while each word was marked in \(j\) ways. Hence their count is \(\frac n j\binom{k-1}{j-1}\binom{n-k-1}{j-1}\). Summing over the exact zero condition counts each vanishing Walsh frequency once, which proves the nullity and rank formulas.

## Verification

The supplied `verify.py` creates the indicator directly from all unordered nonadjacent pairs, performs an integer Walsh–Hadamard transform, and compares each entry to the symbolic multiplier for every \(4\le n\le15\). This checks 65,520 coefficients without floating-point arithmetic. It also compares all zero counts against the composition formula and checks the residue classification through \(n=399\); these are finite tests, **not** the proof of the all-length theorem.

Selected exact ranks and nullities:

| \(n\) | Rank | Nullity |
|---:|---:|---:|
| 4 | 8 | 8 |
| 5 | 32 | 0 |
| 8 | 216 | 40 |
| 11 | 1476 | 572 |
| 12 | 3616 | 480 |
| 15 | 32768 | 0 |

Run `python3 verify.py` with only the Python standard library. The program exits nonzero on disagreement.

## Relationship to prior work

The coefficient of degree two of a cycle's ordinary independence polynomial counts the support size \(n(n-3)/2\). Brown and Hoshino give the full univariate independence polynomial of powers of cycles (Theorem 3.3), but that invariant supplies only the **zero-frequency** value of this signed Fourier transform and does not determine its frequency-dependent cancellations or convolution nullities. Earlier Boolean Fourier frameworks and independent-set results on graph products supply general methods, rather than this cycle-pair spectrum. The new assertion is the residue-class cancellation classification and its exact multiplicity formula, not the basic independent-pair count or Walsh diagonalization.

## Limitations

Only the cardinality-two sector of independent sets of simple cycles is covered; higher sectors and more general circulant exclusion graphs are not classified. The argument proves vanishing locations and ranks, but does not classify all distinct *nonzero* spectral magnitudes. Possible earlier equivalent results framed as signed hard-core partition functions or cyclic Seidel quadratic sums have not been excluded with certainty; historical priority is subject to broader literature verification. Scientific verification is internal and does not constitute an independent audit.

## References

- J. Brown and R. Hoshino, "Independence polynomials of circulants with an application to music," *Discrete Mathematics* **309** (2009), 2292–2304, first available online 2008-09-11, https://www.mscs.dal.ca/~hoshino/music.pdf , Theorem 3.3 and Section 4.
- N. Alon, I. Dinur, E. Friedgut and B. Sudakov, "Graph Products, Fourier Analysis and Spectral Techniques," *Geometric and Functional Analysis* **14** (2004), 913–940, https://doi.org/10.1007/s00039-004-0478-3 .
- R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), Chapter 1, https://doi.org/10.1017/CBO9781139814782 .
