# Exact XOR representation profile and fourth Walsh moment of Fibonacci cubes

## Finding

For every integer \(n\geq 1\), let \(A_n\subseteq\mathbb F_2^n\) consist of the binary words with no adjacent ones, and define the **ordered XOR representation profile**
\[
R_n(x)=\#\{(u,v)\in A_n^2:u\oplus v=x\},\qquad x\in\mathbb F_2^n.
\]
Let \(b(x)\) be the number of maximal nonempty runs of ones in \(x\). For every maximal zero-run \(I\) of length \(\ell(I)\), write \(a(I)=1\) if a one immediately precedes it, and \(c(I)=1\) if a one immediately follows it; otherwise set the corresponding boundary indicator to zero. Define the nonnegative integer
\[
m(I)=\max\{0,\ell(I)-a(I)-c(I)\}.
\]
With Fibonacci numbers \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\), the **complete pointwise profile** is
\[
\boxed{R_n(x)=2^{b(x)}\prod_{I\,\mathrm{maximal\ zero\ run\ of}\,x}F_{m(I)+2}.}
\]
The empty product equals one; the definition covers zero-runs of length one between two one-runs (their unique forced zero is counted only once). In particular every coefficient is strictly positive, so \(A_n\oplus A_n=\mathbb F_2^n\), and
\[
\min_x R_n(x)=2,\qquad \max_x R_n(x)=F_{n+2}=|A_n|.
\]
The maximum is attained only at \(x=0\) when \(n\ge2\); the all-one word always attains the minimum. For \(n=1\) both values equal two.

A complementary fourth-moment consequence is exact. Write
\[
W_n(\xi)=\sum_{u\in A_n}(-1)^{\langle\xi,u\rangle},\qquad
E_n=\sum_{x\in\mathbb F_2^n}R_n(x)^2
=2^{-n}\sum_{\xi\in\mathbb F_2^n}W_n(\xi)^4.
\]
Then \(E_0=1\), \(E_1=8\), \(E_2=21\), and for all \(n\ge3\),
\[
\boxed{E_n=2E_{n-1}+6E_{n-2}-E_{n-3},\qquad
\sum_{n\ge0}E_n z^n=\frac{1+6z-z^2}{1-2z-6z^2+z^3}.}
\]
The numerical sequence \(8,21,89,296,1105,\ldots\) and its recurrence occur already as OEIS A264238 under a **different counting interpretation**; the scalar recurrence alone is not claimed as new. The pointwise XOR profile, its bounds and its harmonic interpretation are the claim of interest.

Let \(\lambda\) be the largest real root of \(t^3-2t^2-6t+1\), approximately \(3.592614742039924\). An optional asymptotic consequence of the generating function is
\[
E_n\sim \frac{\lambda^2+6\lambda-1}{3\lambda^2-4\lambda-6}\lambda^n
\quad (n\to\infty),
\]
with the coefficient approximately \(1.8235550555611175\). This follows from the simple dominant pole and is not a claim of novelty for the already indexed scalar sequence.

## Assumptions and scope

All additions are coordinatewise modulo two in \(\mathbb F_2^n\), not integer addition. The two entries in an ordered pair are distinguished. Endpoints of the length-\(n\) path are **not adjacent to each other**. The ambient Walsh transform is unnormalized; the fourth-moment average includes \(2^{-n}\). All formulas use the standard Fibonacci indexing and cover every \(n\ge1\). The auxiliary value \(E_0=1\) counts the unique empty quadruple.

## Proof

**Step 1, forced alternation in one-runs.** Fix \(x\), and choose an ordered pair \((u,v)\) with \(u\oplus v=x\). At each coordinate with \(x_i=1\), exactly one of \(u_i,v_i\) equals one. If two consecutive coordinates of \(x\) are one, the choice of which string carries the one must alternate, because neither \(u\) nor \(v\) may contain adjacent ones. Every maximal one-run therefore has exactly two possible orientations, and choices on distinct one-runs are independent once the intervening zeros are dealt with.

**Step 2, free choices in zero-runs.** Where \(x_i=0\), the pair of bits is either \((0,0)\) or \((1,1)\). Any such coordinate adjacent to a one-coordinate of \(x\) is forced to be \((0,0)\), since one of the two strings has a one at the neighboring coordinate. In a zero-run \(I\) of length \(\ell\), these endpoint constraints remove the first coordinate when \(a(I)=1\) and the last when \(c(I)=1\); if both refer to the same coordinate, it is removed only once. Exactly \(m(I)=\max(0,\ell-a(I)-c(I))\) consecutive coordinates remain free, each simultaneously carrying either zero or one in both strings. Their choices must have no adjacent ones, hence number \(F_{m(I)+2}\). Multiplication over independent runs yields the boxed profile.

**Step 3, sharp extremes.** Every factor is positive. When \(x\ne0\), there is at least one one-run and thus \(R_n(x)\ge2\). When \(x=0\), there is one zero-run of length \(n\) and \(R_n(0)=F_{n+2}\ge2\). For the all-one word there is one one-run and no zero-run, so \(R_n(x)=2\). For the upper bound, \(R_n(x)=|A_n\cap(A_n\oplus x)|\le |A_n|\); equality means translation by \(x\) preserves \(A_n\). For \(n\ge2\), if \(x\notin A_n\), then \(0\in A_n\) but \(0\oplus x\notin A_n\), ruling out equality. If \(x\in A_n\setminus\{0\}\), select an occupied coordinate \(i\) and an adjacent path coordinate \(j\); the single-one word at \(j\) lies in \(A_n\) but its XOR with \(x\) does not. Thus the maximum is unique at zero. The \(n=1\) equality is direct.

**Step 4, fourth moment.** The indicator \(f=\mathbf1_{A_n}\) has convolution \((f*f)(x)=R_n(x)\), where convolution is **unnormalized**. With \(\widehat f=W_n\), the transform of \(f*f\) is \(W_n^2\); finite-group Plancherel gives \(\sum_x R_n(x)^2=2^{-n}\sum_\xi W_n(\xi)^4\).

**Step 5, exact transfer recurrence.** Equivalently, \(E_n\) counts ordered quadruples of Fibonacci words whose bitwise XOR is zero. Each coordinate's occupied subset of the four words has even size, hence belongs to one of three classes: empty (one possibility), two-element (six possibilities), or full (one possibility). Consecutive occupied subsets must be disjoint. A type-0 column can precede any type; a fixed type-2 column can precede only the empty column or the **unique complementary** type-2 column; a type-4 column can precede only the empty column. The matrix of numbers of next-column choices is therefore
\[
B=\begin{pmatrix}1&6&1\\1&1&0\\1&0&0\end{pmatrix}.
\]
Consequently, with \(\mathbf v=(1,6,1)\) and \(\mathbf1=(1,1,1)^T\),
\[
E_n=\mathbf v B^{n-1}\mathbf1\quad(n\ge1).
\]
Direct multiplication gives \(B^3-2B^2-6B+I=0\). Thus the recurrence holds, including \(n=3\) using \(E_0=1\), with \(E_1=8\), \(E_2=21\). Summing it supplies the displayed rational generating function. Its denominator has three distinct real roots; the reciprocal of the largest positive root has smallest modulus, yielding the asymptotic by partial fractions.

## Verification

The standalone standard-library checker `CHECK.py` enumerates **all** ordered pairs \((u,v)\in A_n^2\) and checks the product formula at **every** one of the \(2^n\) possible differences for each \(1\le n\le13\). It independently computes the Walsh–Hadamard transform through \(n=12\), checks Parseval and the fourth-moment identity, tests the extrema including the unique maximum, and verifies the transfer recurrence through \(n=18\) and the exact matrix polynomial relation. Run `python3 CHECK.py`. Successful output ends with `FIBONACCI_XOR_PROFILE_AND_FOURTH_MOMENT_PASS`. These are finite corroborations; the all-\(n\) result is proved by the run decomposition and transfer argument above.

## Relationship to prior work

Fibonacci cubes as the induced Boolean-cube graphs on words without adjacent ones and their basic cardinalities are classical (Cabello–Eppstein–Klavžar; Klavžar survey). Codara–D’Antona derive a **scalar sequence convolution** for counts of graph edges in the poset of independent sets; their displayed convolution \(\sum_i F_iF_{n-i+1}\) is **not** the pointwise XOR group convolution \(R_n(x)\). The numeric fourth-moment sequence and its recurrence match OEIS A264238, so neither is asserted to be arithmetically new. The full \(2^n\)-coordinate difference-multiplicity profile is more informative than a scalar edge count, a scalar fourth moment, or a Hamming-distance aggregate. A 1997 paper on unitary transforms of generalized Fibonacci cubes was located by abstract but its full text could not be inspected; it remains an originality risk. No proof of exhaustive historical priority is claimed.

## Limitations

The profile applies to the ordinary Fibonacci cube (path-independent words), not arbitrary forbidden-substring cubes, cyclic Lucas cubes, or complex-phase Fourier extensions. The recurrence for \(E_n\) is already present numerically in a database under a separate interpretation. No independence from every prior unpublished or unindexed result is claimed. The checker tests finite dimensions and is not an independent audit.

## References

- S. Cabello, D. Eppstein, S. Klavžar, *The Fibonacci dimension of a graph*, arXiv:0903.2507, submitted 2009-03-13. https://arxiv.org/abs/0903.2507
- P. Codara, O. D’Antona, *On the independent subsets of powers of paths and cycles*, arXiv:1210.5561, 2012. https://arxiv.org/abs/1210.5561
- S. Klavžar, *Structure of Fibonacci cubes: a survey*, 2011. https://users.fmf.uni-lj.si/klavzar/preprints/FibonacciCubesRevised.pdf
- OEIS, *A264238*, author R. H. Hardin, entry dated 2015-11-09. https://oeis.org/A264238
- K. Egiazarian and J. Astola, *On Generalized Fibonacci Cubes and Unitary Transforms*, 1997. DOI: 10.1007/s002000050074 (abstract-level comparison only).
