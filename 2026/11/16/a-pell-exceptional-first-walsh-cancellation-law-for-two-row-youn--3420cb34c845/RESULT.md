# A Pell-exceptional first Walsh cancellation law for two-row Young diagrams

## Finding
For every integer \(n\ge1\), embed the Young diagrams contained in a \(2\times n\) rectangle as their \(2n\)-bit cell-incidence vectors, and let \(T_n\) denote unnormalized counting convolution by their indicator on \(G_n=(\mathbb F_2)^{2n}\). Then:

1. \(T_n\) is invertible **if and only if** \(n\equiv0,1\pmod4\). Its least nonzero Fourier multiplier magnitude is \(\delta_n=1\) for those two residues and \(\delta_n=2\) for \(n\equiv2,3\pmod4\). Thus \(\|T_n^\dagger\|_{2\to2}=1/\delta_n\).
2. At singular widths, the smallest support size of a frequency with a vanishing Fourier multiplier is \(1\) **exactly** for the widths \(n=2,19,118,695,4058,\ldots\), and is \(2\) at every other singular width. The exceptional widths are given by \(n=(x-3)/2\), where \(x+y\sqrt2=(1+\sqrt2)^{2k+1}\), \(k\ge1\). At each exceptional width there are exactly two vanishing singleton frequencies: one in each row.
3. The complete Fourier nullity at any width is given by a finite, exact, polynomial-complexity transfer recurrence (defined below), rather than an exponential scan. In particular the nullities at widths \(n=2,3,6,7,10,11\) are \(6,18,789,2807,137820,511732\), respectively.

The first-zero classification is about **coordinate support size of a Fourier character**, not the number of Young diagrams or the number of zero frequencies.

## Assumptions and scope
Index both rows by columns \(1,\ldots,n\). Every diagram is uniquely described by a pair \((a,b)\) with \(0\le b\le a\le n\), where the top row occupies its first \(a\) cells and the bottom row its first \(b\) cells. Write \(A_n\subset G_n\) for the incidence-vector set, \(f_n=1_{A_n}\), and
\[
W_n(u)=\sum_{(a,b):0\le b\le a\le n}(-1)^{\langle u,1_{(a,b)}\rangle},\qquad
(T_nh)(z)=\sum_{v\in G_n}f_n(v)h(z-v).
\]
There are \(M_n=\binom{n+2}{2}\) diagrams. The word *zero* always means \(W_n(u)=0\) as an integer. The Fourier transform is unnormalized and the \(\ell^2\) norm uses counting measure; these conventions give convolution eigenvalues exactly \(W_n(u)\).

## Proof
**Signed-prefix parametrization.** Given a character \(u\), let \(X_a\in\{-1,1\}\) be the product of its signs on the first \(a\) cells of the top row and let \(Y_b\) be the corresponding product for the bottom row, with \(X_0=Y_0=1\). Every choice of \(X_1,\ldots,X_n,Y_1,\ldots,Y_n\) corresponds bijectively to a character. Setting \(S_a=\sum_{b=0}^{a}Y_b\), one obtains the exact identity
\[
W_n=\sum_{a=0}^{n}X_a S_a.
\]
In particular all multipliers have parity \(M_n\). The integer \(M_n\) is odd exactly for \(n\equiv0,1\pmod4\). For a constructive sharp bound, take \(Y_b=(-1)^b\). Then \(S_a=1\) for even \(a\), and \(S_a=0\) for odd \(a\), hence \(W_n\) is the sum of \(m=\lfloor n/2\rfloor+1\) independently choosable signs, except that its first sign is fixed at \(+1\). Every admissible sign sum from \(-m+2\) to \(m\) in steps of two is realized. When \(m\) is odd, \(1\) occurs; when \(m\) is even, both \(0\) and \(2\) occur. Combined with the parity lower bound, this proves assertion 1, including the singularity and sharp nonzero gap.

**Singleton cancellations and Pell's equation.** Let \(C_1(j)\), respectively \(C_2(j)\), count diagrams containing the top, respectively bottom, cell of column \(j\). Direct summation gives
\[
C_1(j)=M_n-\frac{j(j+1)}2,\qquad C_2(j)=\frac{(n-j+1)(n-j+2)}2.
\]
A singleton-character multiplier equals \(M_n-2C_r(j)\). It vanishes precisely when some triangular number \(t(t+1)/2\), with \(1\le t\le n\), equals \(M_n/2\). This is equivalent to
\[
(n+1)(n+2)=2t(t+1),\quad\text{equivalently}\quad x^2-2y^2=-1,
\quad x=2n+3,\ y=2t+1.
\]
All positive integral solutions of this negative Pell equation satisfy \(x+y\sqrt2=(1+\sqrt2)^{2k+1}\) for an integer \(k\ge0\). The bound \(n\ge1\) selects \(k\ge1\). Conversely, each such solution has odd \(x,y\) and gives valid \(1\le t\le n\). The first widths are \(2,19,118,695,4058\); alternatively the sequence obeys \(n_{k+2}=6n_{k+1}-n_k+6\), beginning \(n_1=2,n_2=19\). The two and only two cancelling singleton supports are top cell \(t\) and bottom cell \(n-t+1\), because the cell counts are strictly monotone in each row.

**Two-cell cancellation outside the Pell widths.** Consider two top-row cells in columns \(i<j\). Exactly \(\sum_{a=i}^{j-1}(a+1)=(j-i)(i+j+1)/2\) of the diagrams contain exactly one of them. The corresponding two-cell multiplier is zero when this number is \(M_n/2\). If \(n=4k+2\) with \(k\ge1\), take \((i,j)=(k,3k+2)\). If \(n=4k+3\), with \(k\ge0\), take \((i,j)=(k+1,3k+3)\). In both cases \((j-i)(i+j+1)=M_n\), so the two-cell multiplier vanishes. The only singular width not included by these two constructions is \(n=2\), already a singleton exceptional width. The singleton classification gives the matching lower bound at all other singular widths. This proves assertion 2.

**Exact nullity transfer.** Let \(F_j(s,w)\) count sign-prefix choices through column \(j\) for which \(S_j=s\) and \(\sum_{a=0}^{j}X_aS_a=w\). Initialize \(F_0(1,1)=1\) and every other entry at zero. For \(j\ge0\), use
\[
F_{j+1}(s,w)=\sum_{\varepsilon\in\{-1,1\}}\sum_{\eta\in\{-1,1\}}
F_j(s-\varepsilon,w-\eta s).
\]
The two independently chosen signs are \(Y_{j+1}\) and \(X_{j+1}\). Therefore \(Z_n=\sum_s F_n(s,0)\) counts exactly the zero multipliers, \(\mathrm{rank}(T_n)=4^n-Z_n\), and \(\dim\ker T_n=Z_n\). Every reachable \(s\) has magnitude at most \(n+1\) and every reachable \(w\) has magnitude at most \((n+1)(n+2)/2\); hence each layer has \(O(n^3)\) states, allowing \(O(n^4)\) integer additions and \(O(n^3)\) stored states. This proves assertion 3.

## Verification
Two independently implemented exhaustive methods were executed. A C++17 direct Walsh–Hadamard transform of all \(4^n\) characters for each \(1\le n\le10\) agrees with the exact transfer recurrence, including every zero count, smallest nonzero magnitude and first zero support degree, and satisfies the exact Parseval identity \(\sum_u W_n(u)^2=4^n\binom{n+2}{2}\). A separate Python state transfer and analytic one-/two-cell count checker matches all complete spectra through \(n=9\), checks the recurrence and Pell boundaries through \(n=150\), and checks total transfer mass \(4^n\). See `check_direct.cpp` and `check_young.py`.

## Relationship to prior work
The classical Young lattice \(L(m,n)\) and its Gaussian rank enumerator are studied in V. Dhand, *Rank-unimodality of Young's lattice via explicit chain decomposition*, arXiv:1303.2536 (public 11 March 2013). That work concerns rank-unimodal chain decompositions and does not state the binary cell-incidence Walsh singularity, first-zero support, or Pell exception. The standard finite Boolean Fourier conventions and convolution diagonalization appear in R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Graduate Surveys 1 (published 25 September 2008). Those general tools alone do not give the explicit two-row signed-prefix calculation. A related published closed corner-weighted rectangle generating function (published-finding corpus record `2026/9/15/SCOPE031`) tracks area and corner counts, not independent signs for every cell or the exact zeros of the full character transform; its result does not imply the present characterwise claim.

## Limitations
This is an exact theorem only for two-row rectangular Young diagrams. It does not give a simple closed form for all nullities \(Z_n\), or the full multiplicity of each nonzero Walsh eigenvalue. The transfer recurrence is a finite algorithm rather than an asymptotic theorem. The historical comparison is bounded and cannot exclude unindexed or differently formulated results; no independent mathematical audit is claimed.

## References
1. V. Dhand, *Rank-unimodality of Young's lattice via explicit chain decomposition*, arXiv:1303.2536v1 (11 March 2013), https://arxiv.org/html/1303.2536v1.
2. R. de Wolf, *A Brief Introduction to Fourier Analysis on the Boolean Cube*, Theory of Computing Graduate Surveys 1 (25 September 2008), https://theoryofcomputing.org/articles/gs001/.
3. *Closed q-binomial expansion for the corner-weighted rectangle generating function*, public mathematical record dated 15 September 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/15/SCOPE031 (prior-work comparison, not the motivating archived source).
