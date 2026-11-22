# Exact seven-adic fibers of the derangement numbers

## Finding

Let \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for \(n\ge1\). For every integer \(k\ge1\), the least period of the sequence \(D_n\bmod7^k\) is \(2\cdot7^k\). The exact number of indices \(0\le n<2\cdot7^k\) satisfying \(D_n\equiv y\pmod{7^k}\) is

\[
\boxed{\begin{cases}2,&y\equiv0\pmod7,\\3,&y\equiv1,2,5,6\pmod7,\\0,&y\equiv3,4\pmod7.\end{cases}}
\]

Consequently, the attained residues form exactly five full residue balls \(7\mathbb Z_7\), \(1+7\mathbb Z_7\), \(2+7\mathbb Z_7\), \(5+7\mathbb Z_7\), and \(6+7\mathbb Z_7\). Their Haar measure is \(5/7\).

## Assumptions and scope

Indices are nonnegative integers, \(k\) is any positive integer, and a complete period means indices \(0\le n<2\cdot7^k\). \((x)_0=1\) and \((x)_j=x(x-1)\cdots(x-j+1)\) for \(j\ge1\). All derivatives below are ordinary formal polynomial derivatives, then interpreted in \(\mathbb Z_7\). The assertion concerns the ordinary derangement numbers, not generalized derangements or other primes.

## Proof

Define a seven-adic interpolation by
\[
F(x)=\sum_{j=0}^{\infty}(-1)^j(x)_j,\qquad x\in\mathbb Z_7.
\]
Every run of \(j\) consecutive integer factors includes at least \(\lfloor j/7\rfloor\) factors divisible by seven uniformly for \(x\in\mathbb Z_7\); therefore the series converges uniformly. Its formal derivative series also converges uniformly, since after omitting any one factor, at least \(\lfloor j/7\rfloor-1\) factors remain divisible by seven. For nonnegative integer \(n\), terms with \(j>n\) vanish and inclusion-exclusion gives
\[
D_n=(-1)^nF(n).
\]
Each \((x)_j\) is an integral polynomial. Consequently \(F\) is congruence-preserving, and the first-order Taylor remainder satisfies
\[
F(x+h)-F(x)-hF'(x)\in h^2\mathbb Z_7\quad(x,h\in\mathbb Z_7).
\]

To compute the essential finite tables, set \(L_0=1\), \(L'_0=0\), and recursively \(L_{j+1}(x)=(x-j)L_j(x)\), \(L'_{j+1}(x)=L_j(x)+(x-j)L'_j(x)\). For \(j\ge7\), \(L_j(a)\equiv0\pmod7\) for every \(a\in\{0,\ldots,6\}\); for \(j\ge14\), at least two factors vanish modulo seven and \(L'_j(a)\equiv0\pmod7\). These recurrences give the exact finite tables
\[
\begin{array}{c|rrrrrrr}
a&0&1&2&3&4&5&6\\\hline
F(a)\bmod7&1&0&1&5&2&5&6\\
F'(a)\bmod7&1&5&4&1&5&1&3
\end{array}
\]
(the derivative uses only \(0\le j<14\), while the value uses only \(0\le j<7\)). In particular, all seven slopes are units modulo seven.

For \(x,y\in a+7\mathbb Z_7\) with \(x\ne y\), put \(h=y-x\). The Taylor formula and unit slope imply \(\nu_7(F(y)-F(x))=\nu_7(y-x)\). Thus each restriction \(F:a+7\mathbb Z_7\to F(a)+7\mathbb Z_7\) is an isometry. It is onto: at every digit-lifting step, replacing an input by \(x+7^j t\), \(t\in\{0,\ldots,6\}\), changes the output by \(7^j t F'(a)\) modulo \(7^{j+1}\); all seven next output digits occur exactly once.

In a full index interval \(0\le n<2\cdot7^k\), each residue \(a\pmod{7^k}\) has exactly one even and one odd representative because seven is odd. On the even representative, \(D_n=F(n)\); on the odd representative, \(D_n=-F(n)\). For each choice of sign, every base residue \(a\in\{0,\ldots,6\}\) contributes exactly one input to every output congruent to \(\pm F(a)\pmod7\). Counting the signs in the first table gives multiplicities \((2,3,3,0,0,3,3)\) for output residues \(0,1,2,3,4,5,6\), respectively. This proves all fiber and image assertions at every level.

Congruence preservation gives period \(2\cdot7^k\). To see it is minimal, any least positive period divides this period. A putative period dividing \(7^k\) fails because \(D_{7^k}\equiv-1\pmod7\) while \(D_0=1\). For \(k\ge2\), a putative period dividing \(2\cdot7^{k-1}\) fails since the isometry on \(7\mathbb Z_7\) gives \(D_{2\cdot7^{k-1}}-D_0\) valuation exactly \(k-1\). At \(k=1\), the first fourteen recurrence values directly exclude the remaining proper divisors \(1,2,7\) of fourteen: \(D_0\not\equiv D_1\), \(D_1\not\equiv D_3\), and \(D_0\not\equiv D_7\pmod7\). Hence the least period is exactly \(2\cdot7^k\).

## Verification

Run `python3 verify.py` with Python 3 standard library. The independent checker evaluates the truncated falling-factorial value and derivative tables, verifies their seven entries, and enumerates all residues and complete fiber multiplicities for each \(1\le k\le4\). Observed output: `VERIFY_OK derivative_table=7 residue_classes=7 complete_levels=4`. The infinite result is justified by the analytic isometry proof, not by finite enumeration.

## Relationship to prior work

Miska (2015) develops periodicity and valuation theory of derangement sequences; his 2020 work extends recurrence-based arithmetic techniques. O'Desky and Richman (original preprint 2020) construct seven-adically continuous derangement-related interpolations, providing a broader conceptual context for this interpolation. The present claim identifies the specific nontrivial seven-adic value set and exact fibers at all levels, which are not asserted in the available inspected primary material. Separate published results describe two-, three-, and five-adic derangement image or fiber behavior; they do not logically supply this prime-seven count. An inaccessible full text by Miska is a relevant priority risk.

## Limitations

The theorem concerns only the prime seven, not a general prime-uniform classification. It is not claimed that all p-adic interpolation principles used here are new; the precise prime-seven image, multiplicities and least periods are the proposed new contribution. The available full text of related 2015/2020 Miska work was incomplete, so implicit prior coverage cannot be excluded. No independent scientific audit has been performed.

## References

1. P. Miska, *On a generalization of the recurrence defining the number of derangements*, *Colloquium Mathematicum* 161 (2020), 89–109, first verified online 2020-03-05, https://doi.org/10.4064/cm7510-4-2019.
2. A. O'Desky and D. H. Richman, *Derangements and the p-adic incomplete gamma function*, arXiv:2012.04615, first posted 2020-12-08, https://arxiv.org/abs/2012.04615.
3. P. Miska, *Arithmetic properties of the sequence of derangements*, arXiv:1508.01987, first posted 2015-08-09, https://arxiv.org/abs/1508.01987.
