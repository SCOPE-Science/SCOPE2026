# First period-four failure in Fourier recovery of permutation excedance sets

## Finding
For a permutation \(\pi\in\mathfrak S_n\), define its excedance set by \(E(\pi)=\{i\in\{1,\ldots,n-1\}:\pi(i)>i\}\). Form the multiplicity-weighted function \(f_n(x)=|\{\pi:E(\pi)=x\}|\) on \(H_n=(\mathbb Z/2\mathbb Z)^{n-1}\), and let \(T_nh=f_n*h\), using unnormalized convolution. Its Walsh multiplier is
\[
\Lambda_n(S)=\sum_{\pi\in\mathfrak S_n}(-1)^{|S\cap E(\pi)|},\qquad S\subseteq\{1,\ldots,n-1\}.
\]
**Exact finite-cutoff theorem.** In the residue class \(n\equiv3\pmod4\), the first singular order is \(n=19\): \(T_3,T_7,T_{11},T_{15}\) are invertible, while \(T_{19}\) has exactly \(24\) zero Walsh multipliers and rank \(262120\) on the \(262144\)-dimensional signal space. Its \(24\) blind frequencies occur in \(12\) reversal pairs, listed by exact bitmasks in `ZEROS_N19.txt`. At order \(19\), the spectral inertia is \((131048,131072,24)\) (positive, negative, zero); the smallest nonzero multiplier magnitude is exactly \(3403284480\), and the sharp \(\ell^2\) condition number on the recoverable subspace is \(41247931725/1154\). These claims are finite: no assertion about all subsequent orders is made.

## Assumptions and scope
Here \(n\) ranges over positive integers. All character values and convolution multipliers are unnormalized integers; frequency bit \(i-1\) represents position \(i\). The dimension is \(n-1\), because position \(n\) can never be an excedance. Rank and inertia are those of the real symmetric XOR-convolution matrix indexed by \(H_n\). The exact-cutoff and rank claims concern only \(1\le n\le19\). The sharp condition number uses the nonzero singular values on the range, not an inverse on the full space at singular order.

## Proof
**Rook identity.** Put \(B_S=\{(i,v):i\in S,\ i<v\le n\}\). Let \(R_j(S)\) count placements of \(j\) pairwise nonattacking rooks on \(B_S\), with \(R_0(S)=1\). Expand \(\prod_{i\in S}(1-2\mathbf1_{\{\pi(i)>i\}})\). Any chosen \(j\) constraints \(\pi(i)>i\) assign distinct columns to distinct rows and admit exactly \((n-j)!\) completions. Summing by size gives the exact integer formula
\[
\Lambda_n(S)=\sum_{j=0}^{|S|}(-2)^j(n-j)!R_j(S).
\]
Process selected rows from largest \(i\) to smallest. Initially \(r_0=1\), all higher coefficients zero. On adding selected row \(i\), the \(j-1\) rooks in higher rows all use columns \(>i\); hence the update is
\[
r'_j=r_j+(n-i-j+1)r_{j-1}\quad (j\ge1),\qquad r'_0=1.
\]
This enumerates the rook coefficients for every binary frequency mask using only integer arithmetic, and the signed formula determines every Walsh eigenvalue. The algorithm `verify.cpp` visits **every** mask for all \(1\le n\le19\), checks the resulting exact zero counts, and explicitly compares every eigenvalue with a second method described next. Thus the numerical cutoff is a finite exhaustive proof, not extrapolation from sampled frequencies.

**Independent recurrence.** If \([w]\) denotes the number of permutations with excedance word \(w\in\{a,b\}^{n-1}\), direct permutation deletion yields
\[
[vbaw]=[vabw]+[vbw]+[vaw],\qquad [aw]=[w],\quad [wb]=[w],\quad [\emptyset]=1.
\]
The same recurrence is given in Ehrenborg–Steingrímsson (2000, Proposition 2.1 and Lemma 2.3). Repeatedly swap a `ba` to `ab` or remove a boundary letter; this terminates and exactly counts every word. A Walsh–Hadamard transform of the resulting word-count vector independently yields the full spectrum. `verify.cpp` compares this result with the rook formula *at every frequency*, and additionally checks exact permutation enumeration through \(n=8\), the duality identity, and the resulting spectral parameters.

**A compact zero certificate.** At \(n=19\), the frequency \(S=\{2,5,7,9,10\}\) has bitmask \(850\) and rook coefficients \((R_0,\ldots,R_5)=(1,62,1413,14685,68970,115830)\). Substituting into the displayed rook formula gives the six terms
\[
\begin{split}
&121645100408832000-793894339510272000\\
&+2010345343598592000-2458009356042240000\\
&+1443044818575360000-323131567030272000=0.
\end{split}
\]
The complete certificate lists all \(24\) zeros; all other \(262120\) frequencies are checked nonzero by two exact implementations.

**Reversal structure.** The excedance-word duality \([w]=[\overline{w}^{\rm rev}]\) implies \(\Lambda_n(S)=(-1)^{|S|}\Lambda_n(S^{\rm rev})\). At order \(19\), its \(24\) zeros form precisely \(12\) reversal pairs. The largest multiplier magnitude is \(\Lambda_n(\varnothing)=n!\), by the triangle inequality. Comparing that value with the exact minimum positive magnitude establishes the stated sharp condition number.

## Verification
The standalone self-contained `verify.cpp` needs a C++17 compiler. Run `g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify && ./verify` in a directory containing the extracted files. Both independently constructed spectra agree at all \(\sum_{n=1}^{19}2^{n-1}=524287\) character positions; the program also asserts the exact nullities, dimension, ranks, inertia, witness minima and reversal structure. Direct enumeration of all permutations confirms the word counts for orders up to eight. The complete nullity table is:

| \(n\) | signal dimension | nullity | rank |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 1 |
| 3 | 4 | 0 | 4 |
| 4 | 8 | 2 | 6 |
| 5 | 16 | 2 | 14 |
| 6 | 32 | 4 | 28 |
| 7 | 64 | 0 | 64 |
| 8 | 128 | 8 | 120 |
| 9 | 256 | 4 | 252 |
| 10 | 512 | 18 | 494 |
| 11 | 1024 | 0 | 1024 |
| 12 | 2048 | 32 | 2016 |
| 13 | 4096 | 14 | 4082 |
| 14 | 8192 | 76 | 8116 |
| 15 | 16384 | 0 | 16384 |
| 16 | 32768 | 130 | 32638 |
| 17 | 65536 | 24 | 65512 |
| 18 | 131072 | 288 | 130784 |
| 19 | 262144 | 24 | 262120 |

All computations are exact signed integers, with 128-bit intermediates in the rook sum. The proof of completeness is the finite range of the loops together with the independently proved recurrence identities; it does not depend on floating-point thresholds or partial enumeration.

## Relationship to prior work
Ehrenborg and Steingrímsson (2000) give exact excedance-word recurrences, duality and inclusion–exclusion, but their results concern word counts and inequalities rather than the rank of an XOR convolution formed from those counts. Andrade, Lundberg and Nagle (arXiv:1403.0691, first posted 2014-03-04) study the asymptotics of the most common excedance words; this does not determine the joint signed Walsh spectrum. Clark and Ehrenborg (2010) study prescribed extremal word counts using rook placements and should not be conflated with a complete signed-frequency classification. The present finite-cutoff statement explicitly builds on the classical word enumeration but asks a different rank/recovery question.

## Limitations
The result determines the complete spectrum's *zeros*, spectral inertia and least nonzero absolute multiplier only at the specified cutoff. It neither characterizes future singular residue-class orders nor supplies a closed formula for their nullities. The fully readable 2000 and 2014 primary works did not contain the claimed cutoff, but some related later or unindexed signed-enumerator specializations could exist. The 2010 extremal-excedance paper was compared at abstract level only, not certified absent of all relevant results. No claim of independent expert audit is made.

## References
1. R. Ehrenborg and E. Steingrímsson, *The Excedance Set of a Permutation*, Advances in Applied Mathematics **24** (2000), 284–299, DOI: 10.1006/aama.1999.0671, author-hosted full text: https://www.ms.uky.edu/~jrge/papers/Excedance.pdf.
2. R. Ferraz de Andrade, E. Lundberg and B. Nagle, *Asymptotics of the Extremal Excedance Set Statistic*, arXiv:1403.0691 (first posted 2014-03-04), https://arxiv.org/abs/1403.0691.
3. E. Clark and R. Ehrenborg, *Explicit Expressions for the Extremal Excedance Set Statistics*, European Journal of Combinatorics **31** (2010), 270–279, DOI: 10.1016/j.ejc.2008.11.014.
