# Square-length Fourier rank resonances for contiguous-run signals

## Finding

Let \(I_n\) denote the nonempty binary words of length \(n\) containing exactly one maximal run of ones. Equivalently, these are the nonempty connected vertex subsets of the labelled path \(P_n\). Counting convolution by their indicator undergoes an exact arithmetic rank transition: it is invertible at every \(n\ge1\) except those with \(n+1\) a perfect square. At each exceptional length \(n=s^2-1\), its nullity is precisely
\[
\binom{s^2}{s(s-1)/2}.
\]

More strongly, the complete signed Walsh spectrum, every surviving singular value, the sharp Hilbert-space recovery condition number and the globally optimal endpoint projection norms are explicit below.

## Assumptions and scope

Fix an integer \(n\ge1\), the Boolean group \(G_n=(\mathbb F_2)^n\), and the family
\[
I_n=\{\mathbf1_{[a,b]}:1\le a\le b\le n\}\subset G_n.
\]
The empty word is not included, and the endpoints are not identified periodically. For arbitrary complex- or real-valued \(g:G_n\to\mathbb C\), let
\[
(T_ng)(x)=\sum_{u\in I_n}g(x+u).
\]
This is *unnormalized* counting convolution. Equip \(\ell^p(G_n)\) with ordinary counting measure, and use the unnormalized Walsh multiplier \(W_n(S)=\sum_{u\in I_n}(-1)^{\langle S,u\rangle}\). Fourier characters diagonalize \(T_n\) in \(\ell^2\).

For each frequency \(S\subseteq[n]\), put
\[
p_0=1,\qquad p_i=(-1)^{|S\cap[1,i]|}\quad(1\le i\le n),\qquad j(S)=\#\{i\in[n]:p_i=-1\}.
\]

## Proof

**Complete signed spectrum.** Each interval \([a,b]\) has character value \(p_{a-1}p_b\). Consequently
\[
W_n(S)=\sum_{0\le u<v\le n}p_up_v
=\frac{\bigl(\sum_{u=0}^np_u\bigr)^2-(n+1)}{2}
=\frac{(n+1-2j(S))^2-(n+1)}{2}.
\]
The map \(S\mapsto(p_1,\ldots,p_n)\) is bijective: from any signs recover the bit at position \(i\) by whether \(p_i\) differs from \(p_{i-1}\). Therefore the signed multiplier indexed by \(j\in\{0,\ldots,n\}\) occurs with multiplicity \(\binom nj\). Equal numerical levels are to be merged by summing those indexed multiplicities; no assumption that they are distinct is made.

**Zeros and rank.** The multiplier vanishes exactly when \((n+1-2j)^2=n+1\). This requires \(n+1=s^2\) for an integer \(s\ge2\). Conversely, for \(n=s^2-1\), both integers
\[
j_- =\frac{s(s-1)}2,\qquad j_+=\frac{s(s+1)}2
\]
lie between zero and \(n\), and exactly these indexed levels vanish. Their total multiplicity is
\[
\binom{n}{j_-}+\binom{n}{j_+}
=\binom{s^2-1}{j_-}+\binom{s^2-1}{j_--1}
=\binom{s^2}{j_-}.
\]
Walsh diagonalization gives the claimed invertibility criterion, nullity and rank.

**Sharp Hilbert stability.** The maximum absolute multiplier is \(|I_n|=n(n+1)/2\), reached at the trivial character. At resonance \(n=s^2-1\), nonzero admissible integers \(m=n+1-2j\) have parity equal to that of \(s\), and the two zero levels are \(m=\pm s\). The nearest admissible nonzero level below \(s\) is \(m=s-2\), and it gives
\[
\min_{W_n(S)\ne0}|W_n(S)|
=\frac{s^2-(s-2)^2}{2}=2(s-1).
\]
The Moore–Penrose inverse on the range hence has \(\ell^2\)-norm \(1/[2(s-1)]\), and the positive-spectrum condition number is \(n(n+1)/[4(s-1)]\).

**Optimal endpoint projection.** For a resonant length set \(N=2^n\), \(Z=\binom{s^2}{j_-}\), and define the binary Krawtchouk number
\[
K_j(t;n)=\sum_{r=0}^j(-1)^r\binom tr\binom{n-t}{j-r},
\]
using zero for out-of-range binomial coefficients. Under the invertible prefix-parity change of frequency coordinates, the zero set is the union of Hamming layers \(j_-\) and \(j_+\). Thus the unique translation-invariant projection \(P_n\) onto \(\mathrm{ran}(T_n)\) has convolution kernel whose values, up to a bijective reindexing of input coordinates, are
\[
k_n(0)=1-Z/N,\qquad
k_n(x)=-\frac{K_{j_-}(t;n)+K_{j_+}(t;n)}N\quad(t=|x|\ge1).
\]
Its endpoint norms are the same absolute row/column sum,
\[
\boxed{\|P_n\|_{1\to1}=\|P_n\|_{\infty\to\infty}
=\frac{N-Z+\sum_{t=1}^n\binom nt|K_{j_-}(t;n)+K_{j_+}(t;n)|}{N}.}
\]
To see global optimality, average any linear projection \(Q\) onto the translation-invariant range of \(T_n\) over all group translations. The average remains a projection onto that range and cannot increase either endpoint norm. In the Walsh basis a translation-invariant projection onto this range must be \(P_n\), because its multiplier is one on surviving frequencies and zero on all other frequencies. Therefore the displayed norm is minimal among arbitrary projections, not only translation-invariant ones.

**Asymptotic lost fraction.** For \(n=s^2-1\), the ratio \(Z/2^n=2\binom{s^2}{(s^2-s)/2}/2^{s^2}\) has, by Stirling's formula, the sharp asymptotic
\[
\frac{Z}{2^n}\sim \frac{2}{s}\sqrt{\frac{2}{\pi e}}\qquad(s\to\infty).
\]
No limit claim is made at non-resonant lengths, where the nullity is identically zero.

## Verification

Independent exact-integer implementations accompany the theorem. Compile and run `verify_direct.cpp` with `g++ -O2 -std=c++17 verify_direct.cpp -o direct && ./direct 16`; it constructs the interval indicator on the full Boolean cube and independently applies an integer Walsh–Hadamard transform for each length one through sixteen, checking *all* coefficients against the formula. Run `python3 verify_independent.py` for an independently organized direct interval-by-interval parity sum through length ten and an exact Krawtchouk norm calculation. Compile and run `verify_projection.cpp` analogously for a second direct inverse-transform check of the projection norms at \(n=3,8,15\).

The tested resonance examples are:

| \(n\) | Nullity | Rank | Smallest nonzero absolute multiplier | Optimal endpoint projection norm |
|---:|---:|---:|---:|---:|
| 3 | 4 | 4 | 2 | \(1\) |
| 8 | 84 | 172 | 4 | \(25/4\) |
| 15 | 8008 | 24760 | 6 | \(131177/2048\) |

Finite checks are not used as the proof of the all-length theorem; the displayed algebra establishes that separately.

## Relationship to prior work

General Walsh diagonalization and the convolution theorem are classical (O'Donnell, *Analysis of Boolean Functions*, 2014, Chapter 1, especially §1.5). Bilotta, Pergola and Pinzani (2011) treat enumeration of forbidden-pattern binary words by succession rules, a distinct counting problem. These sources give the mathematical setting, but the inspected portions do not state the exact one-run Fourier spectrum, perfect-square nullity, or optimal endpoint projection norm. The full claim is for one-run words, not for all pattern-avoiding words, all binary words, or the uniform Hamming slice.

## Limitations

This is a complete result for the *nonempty, single-contiguous-run* model on a noncyclic path. It does not extend by the same argument to cyclic runs, multiple separated runs, arbitrary trees, or weighted interval families. The projection formula is an exact finite binomial sum; no elementary simplification or asymptotic of that endpoint norm is asserted. Prior-art searches cannot rule out unindexed equivalent calculations; the full textbook is a general reference and not an exhaustive novelty certificate. Independent audit has not been performed.

## References

1. S. Bilotta, E. Pergola and R. Pinzani, *Pattern \(1^j0^i\) avoiding binary words*, preprint arXiv:1108.3621, first posted 2011-08-18. https://arxiv.org/abs/1108.3621
2. R. O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press, first edition 2014; DOI:10.1017/CBO9781139814782, §1.5. Open author copy: https://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf
