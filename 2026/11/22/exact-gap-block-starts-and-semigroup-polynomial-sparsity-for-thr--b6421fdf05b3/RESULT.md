# Exact gap-block starts and semigroup-polynomial sparsity for three geometric generators

## Finding
For every integer \(n\ge2\), consider the numerical semigroup
\[
S_n=\langle a,b,c\rangle=\langle n^2,n(n+1),(n+1)^2\rangle.
\]
A *gap block* is a maximal interval of consecutive positive integers missing from \(S_n\). Its *start* is its least integer. Put \(a=n^2\). Every gap-block start belongs to exactly one of the following arithmetic progressions:
\[
\begin{aligned}
&\big\{(\lceil u/2\rceil+t)a+un+\lfloor u/2\rfloor+1:0\le t<n\big\}
&&\text{for each }0\le u<n;\\
&\big\{(u-j_2+n+2+t)a+un+j_2:0\le t<n\big\},
\quad j_2=\lfloor(n+u)/2\rfloor+1
&&\text{for each }0\le u\le n-3.
\end{aligned}
\]
When \(n=2\), the second collection is empty. The union is disjoint. There are precisely \(2n-2\) progressions, each containing \(n\) terms; therefore the total number of maximal gap blocks is exactly
\[
\boxed{R_n=2n(n-1).}
\]
In particular, the *semigroup polynomial*
\[
P_n(z)=(1-z)\sum_{s\in S_n}z^s
\]
is finite and has precisely \(4n(n-1)+1\) nonzero coefficients; its negative coefficients occur exactly at the displayed gap-block starts. Its degree equals \(2n^3-2n\). The genus and Frobenius number are, respectively, \(n^3-n\) and \(2n^3-2n-1\).

## Assumptions and scope
All generators and coefficients are integers. The numerical semigroup is the additive monoid of nonnegative linear combinations of the three displayed generators. Since \(\gcd(n^2,(n+1)^2)=1\), its complement is finite. Here a gap block is maximal in the full positive integer line, not merely within a fixed residue block. The polynomial is interpreted as a finite formal polynomial after cancellation of the eventual constant tail in the generating series. The theorem classifies every gap-block *start* but does not give a separate closed distribution of block *lengths*.

## Proof
**1. Exact Apéry rectangle.** The relations \(nb=(n+1)a\) and \(nc=(n+1)b\) reduce every representation in \(S_n\) to \(xa+ib+jc\) with \(x\ge0\) and \(0\le i,j<n\). The \(n^2\) numbers \(ib+jc\) represent different residues modulo \(a=n^2\): modulo \(n\) the residue determines \(j\), and after subtracting \(jc\), dividing by \(n\) and reducing again modulo \(n\) determines \(i\), since \(b/n=n+1\) is a unit modulo \(n\). Consequently the whole Apéry set relative to \(a\) is
\[
\operatorname{Ap}(S_n,a)=\{ib+jc:0\le i,j<n\}.
\]
Its elements are minimal in their residue classes, because reducing a representation never creates negative coefficients, and the canonical remainder pair is unique.

**2. Row thresholds.** Write each residue uniquely as \(r=un+j\), with \(0\le u,j<n\), and define
\[
h_u(j)=\left\lceil\frac{2j-u}{n}\right\rceil,
\quad i=u-2j+nh_u(j),
\quad H_u(j)=u-j+(n+1)h_u(j).
\]
Here \(0\le i<n\), and direct expansion gives \(ib+jc=H_u(j)a+un+j\). Thus
\[
qa+un+j\in S_n\quad\Longleftrightarrow\quad q\ge H_u(j)
\qquad(q\ge0).
\]
For fixed \(u\), as \(j\) increases, \(h_u(j)\) makes its first unit jump at \(j_1=\lfloor u/2\rfloor+1\). Its second jump occurs at \(j_2=\lfloor(n+u)/2\rfloor+1\) exactly when \(u\le n-3\). At every other step \(H_u(j+1)-H_u(j)=-1\); at each jump the difference is \(n\). At the two jumps the preceding threshold is, respectively,
\[
H_u(j_1-1)=\lceil u/2\rceil,
\qquad H_u(j_2-1)=u-j_2+n+2.
\]
At the boundary between successive \(u\)-blocks, the threshold decreases: \(H_u(n-1)>H_{u+1}(0)=u+1\) for \(u<n-1\). Residue zero is always represented at each multiple of \(a\). Therefore no new gap block begins at a block boundary, at residue zero, or at a strictly descending adjacent threshold.

**3. Exhaustion of gap starts.** In a row \(q\), an integer of residue \(un+j\), with \(j>0\), starts a maximal gap block if and only if its immediate predecessor is represented and it is missing. By the preceding threshold criterion this holds exactly when
\[
H_u(j-1)\le q<H_u(j).
\]
Only a height-\(n\) jump satisfies this, at the \(n\) consecutive row values \(q=H_u(j-1),\ldots,H_u(j-1)+n-1\). These are precisely the two listed families of progressions. They are mutually disjoint because their residues modulo \(a\) are distinct, and their total number is \(n[n+(n-2)]=2n(n-1)\).

**4. Genus, conductor, and coefficient count.** The maximum Apéry representative is \((n-1)(b+c)\), so the Frobenius number is \((n-1)(b+c)-a=2n^3-2n-1\). For any Apéry set with \(a\) residues, the genus is its sum divided by \(a\), minus \((a-1)/2\). In this case the sum is \(n^2(n-1)(b+c)/2\), giving genus \(n^3-n\). For any \(m\ge0\), the coefficient of \(z^m\) in \(P_n(z)\) equals \(\mathbf1_{S_n}(m)-\mathbf1_{S_n}(m-1)\), with \(\mathbf1_{S_n}(-1)=0\). A missing-integer block contributes a \(-1\) at its start and a \(+1\) at the first represented integer after it; the constant coefficient is \(+1\). All remaining coefficients vanish. Hence there are exactly \(2R_n+1=4n(n-1)+1\) nonzero coefficients, and the highest is at Frobenius number plus one.

## Verification
Run `python3 verify_gap_starts.py` using Python 3. The standalone program independently constructs represented integers by unbounded-coin reachability, without using the Apéry proof, for every \(2\le n\le80\). For each instance it compares the complete gap-start set, the number of gaps, Frobenius number, negative coefficient locations, and total nonzero polynomial coefficients against the formulas. It checked 20,988,799 integer positions in 79 complete finite cases and reported:

```text
VERIFY_OK cases=79 checked_positions=20988799 n_range=2..80
```

Finite testing corroborates but does not replace the uniform argument above.

## Relationship to prior work
Shor and Sim (2025), arXiv:2503.10826, study exactly the broader family of three-generator geometric semigroups. Their full primary text gives the general rectangular Apéry set (Proposition 2.6, attributed to earlier work) and genus (Proposition 2.5), and resolves **modular equidistribution of the complete gap set**, rather than individual maximal-gap starts or the coefficient-support sparsity formula. The Apéry rectangle is therefore a previously known input, rederived above for self-contained correctness; the jump-location enumeration is the new assertion. Ong and Ponomarenko (2008) address Frobenius numbers for geometric-sequence generators, including the present type of three-term progression. Their Frobenius calculation does not classify maximal missing-integer block starts or the nonzero-coefficient support of the associated semigroup polynomial. Liu, Xin, Ye and Yin (2023), arXiv:2306.03459, develop Apéry methods for families including generalized Mersenne and Thabit semigroups, different from this geometric triple. These serve as motivation for examining finer gap geometry beyond genus and Frobenius number.

Two accessible related published results were compared at the level of their statements: the complete block-length frequencies for two-generator semigroups \(\langle dt+1,d(t+1)+1\rangle\) and the isolated-gap lists for three consecutive triangular numbers. Neither covers the present three-generator geometric triple nor implies this complete progression classification. Pascadi (2017), arXiv:1712.02522, describes graphical methods for Hilbert series of numerical semigroups, potentially broad enough to recover special-case coefficient support after additional computation, but its full primary text could not be inspected. A prior implicit equivalent remains a bibliographic risk.

## Limitations
This is an exact statement only for the natural family \(\langle n^2,n(n+1),(n+1)^2\rangle\), not for arbitrary geometric or telescopic semigroups. It determines all block starts and polynomial coefficient signs, but does not enumerate each gap-block length separately. Literature coverage is incomplete, particularly the full text of Pascadi (2017); general Hilbert-series methods may yield equivalent consequences even if not tabulated. No independent mathematical or historical-priority audit has occurred.

## References
1. Feihu Liu, Guoce Xin, Suting Ye, Jingjing Yin, *A Combinatorial Model of Numerical Semigroup* (2023), arXiv:2306.03459, first posted 2023-06-06. https://arxiv.org/abs/2306.03459
2. Caleb M. Shor and Jae Hyung Sim, *Equidistribution Conditions for Gaps of Geometric Numerical Semigroups* (2025), arXiv:2503.10826, first posted 2025-03-13. https://arxiv.org/abs/2503.10826
3. Tom Ong and Vadim Ponomarenko, *The Frobenius Number of Geometric Sequences* (2008). https://www.academia.edu/66791211/The_Frobenius_Number_of_Geometric_Sequences
4. Alexandru Pascadi, *A Graphical Approach to Finding the Frobenius Number, Genus and Hilbert Series of a Numerical Semigroup* (2017), arXiv:1712.02522. https://arxiv.org/abs/1712.02522
5. *Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-length-frequencies-for-binary-semigroups-with-a-dt-1-a--584c998005ae
6. *Isolated gaps in semigroups of three consecutive triangular numbers* (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-isolated-gaps-in-semigroups-of-three-consecutive-triangular-numb--42c2c6edcb7c
