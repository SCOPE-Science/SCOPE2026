# The complete Fibonacci run-length spectrum of shifted-Fibonacci numerical semigroup gaps

## Finding
Let \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\). For an arbitrary integer \(a\ge5\), consider the numerical semigroup
\[
S_a=\langle F_a+F_j:j\ge0\rangle
=\langle F_a,F_a+F_2,\ldots,F_a+F_{a-1}\rangle.
\]
A *gap block* is a maximal interval of consecutive positive integers omitted by \(S_a\). Let \(H_a(L)\) be the number of such blocks of length \(L\). Then **the entire length-frequency distribution** is
\[
\boxed{H_a(L)=
\begin{cases}
1,&L=F_a-1,\\
F_{a-j-1},&L=F_j-1\text{ for some }3\le j\le a-2,\\
0,&\text{otherwise.}
\end{cases}}
\]
The lengths in this formula are distinct. Consequently there are exactly \(F_{a-2}\) maximal gap blocks. The initial interval \([1,F_a-1]\) is the unique block of maximum length; there is no block of length \(F_{a-1}-1\). For example, at \(a=10\), the complete spectrum (length, frequency) is
\[
(1,8),(2,5),(4,3),(7,2),(12,1),(20,1),(54,1).
\]
This is a full classification of lengths and frequencies, not a formula only for isolated gaps (blocks of length one).

## Assumptions and scope
The parameter \(a\) is an integer at least five. All nonnegative integer combinations of the displayed generators are allowed. Fibonacci indices follow the convention above, and \(F_2=1\). A Zeckendorf decomposition is the unique expression of a nonnegative integer as a sum of distinct nonconsecutive Fibonacci numbers with indices at least two. Its number of summands is denoted by \(\beta(r)\), with \(\beta(0)=0\). A gap block is maximal on *both* sides: its predecessor and successor are semigroup elements (allowing the predecessor zero for the first block).

The published Apéry formula for this semigroup is used as an explicit input, not claimed as new. The proof below establishes the new all-length combinatorial recurrence and evaluates it uniformly for every \(a\ge5\). No assumptions on primality or on asymptotic limits are needed.

## Proof
**1. The membership word.** Write \(m=F_a\). Theorem 4.6 of Robles-Pérez--Rosales gives, for every \(0\le r<m\), the least member of \(S_a\) congruent to \(r\pmod m\) as
\[
w_a(r)=m\beta(r)+r.
\]
It follows, for all integers \(q\ge0\) and \(0\le r<m\), that
\[
qm+r\notin S_a\quad\Longleftrightarrow\quad q<\beta(r).\tag{1}
\]
In particular every multiple of \(m\) belongs to \(S_a\). Therefore no gap block crosses a multiple of \(m\).

Define the finite word of summand counts
\[
B_a=(\beta(0),\beta(1),\ldots,\beta(F_a-1)).
\]
For each integer \(q\ge0\), the gap blocks within the half-open interval \([qm,(q+1)m)\) correspond exactly to the maximal consecutive subwords of \(B_a\) whose entries exceed \(q\). By (1), the entire \(q=0\) row is the single block \([1,m-1]\), of length \(m-1\), because \(\beta(0)=0\) and \(\beta(r)\ge1\) for every \(1\le r<m\).

**2. A Zeckendorf-word concatenation.** For every \(a\ge5\), the Fibonacci identity \(F_a=F_{a-1}+F_{a-2}\) and the nonconsecutive-index rule give the *exact word identity*
\[
\boxed{B_a=B_{a-1}\mathbin{\|}(\mathbf 1+B_{a-2})},\tag{2}
\]
where \(\|\) denotes concatenation and \(\mathbf1\) adds one to each entry. Indeed, the integers \(0\le r<F_{a-1}\) have the same Zeckendorf expansions as before; every integer in the complementary range has the unique form \(r=F_{a-1}+t\) with \(0\le t<F_{a-2}\), and its Zeckendorf decomposition is the term \(F_{a-1}\) together with that of \(t\). The latter uses only indices at most \(a-3\), so no adjacent indices are introduced. Hence \(\beta(F_{a-1}+t)=1+\beta(t)\).

**3. Recurrence for all noninitial gap blocks.** Let \(\mathcal R_a\) be the multiset of lengths of gap blocks found in rows \(q\ge1\) (the unique initial row-zero block excluded). At the concatenation boundary in (2), the first entry of \(\mathbf1+B_{a-2}\) equals one, so it is *not* a gap position in any row \(q\ge1\). Consequently no maximal run at such a level crosses that boundary.

In the first segment \(B_{a-1}\), the runs above levels \(q\ge1\) contribute precisely \(\mathcal R_{a-1}\). In the second segment \(\mathbf1+B_{a-2}\), the runs above \(q\ge2\) correspond to all runs of \(B_{a-2}\) above levels \(q-1\ge1\), contributing \(\mathcal R_{a-2}\). At the remaining level \(q=1\), the second segment exceeds one exactly in its last \(F_{a-2}-1\) positions (since its first entry is one and every other entry is at least two). Thus it contributes one *additional* gap block of length \(F_{a-2}-1\). We have proved the disjoint multiset identity
\[
\boxed{\mathcal R_a=\mathcal R_{a-1}\uplus\mathcal R_{a-2}\uplus\{F_{a-2}-1\}}\qquad(a\ge5),\tag{3}
\]
with \(\mathcal R_3=\mathcal R_4=\varnothing\). These initial cases follow immediately from \(B_3=(0,1)\) and \(B_4=(0,1,1)\), whose entries never exceed one. Equation (3) also proves that no unlisted run length can occur.

**4. Solving the multiset recurrence.** Fix \(j\ge3\). The length \(F_j-1\) is first introduced into (3) at \(a=j+2\), once; it is present once at \(a=j+3\), and at subsequent indices its multiplicity obeys the Fibonacci recurrence. Hence for every \(a\ge j+2\), its multiplicity in \(\mathcal R_a\) is precisely \(F_{a-j-1}\). Since the introduced lengths are strictly increasing with \(j\ge3\), these frequencies do not interfere. Adjoining the single excluded initial run \(F_a-1\) proves the stated formula.

Summing the block frequencies gives
\[
1+\sum_{j=3}^{a-2}F_{a-j-1}
=1+\sum_{t=1}^{a-4}F_t=F_{a-2},
\]
using \(\sum_{t=1}^{n}F_t=F_{n+2}-1\). Moreover, the largest noninitial length is \(F_{a-2}-1\), so the initial block is strictly longer and the intermediate length \(F_{a-1}-1\) does not occur. This completes the infinite-parameter proof.

## Verification
The standalone `verify.py` checks every integer \(5\le a\le24\) in three arithmetically distinct ways: unrestricted coin-change dynamic programming with the finite generating set, direct Zeckendorf digit-count membership thresholds, and the closed run-length-frequency formula. It also checks the concatenation identity (2), the total block count, and the isolated-gap specialization. All comparisons passed: 1,381,700 semigroup membership decisions, 121,385 digit-word positions, and 46,365 maximal gap blocks. To reproduce: `python3 verify.py` with the standard Python 3 interpreter; no third-party packages are required. The finite checks corroborate the calculations but do not substitute for the proof of (3).

A further consistency check is that summing \(L H_a(L)\) recovers the published genus \(\big((a-2)F_a+aF_{a-2}\big)/5\), though the new claim concerns the refined histogram, not the already known genus.

## Relationship to prior work
Robles-Pérez and Rosales [1] establish the exact same semigroup's minimal generators, Zeckendorf Apéry representatives, Frobenius number, genus, and Wilf inequality. The present proof explicitly relies on their Theorem 4.6; [1] does not state the complete gap-block histogram or recurrence (3). An existing isolated-gap classification for this family [2] gives the length-one frequency \(F_{a-4}\) and an explicit description of individual isolated gaps, a *proper one-length component* of the present full spectrum. It does not give the lengths or frequencies of blocks of length two or greater. Another classification [3] treats pseudo-Frobenius gaps and Padovan-type, not maximal consecutive missing-integer blocks. The broader \(r\)-Fibonacci semigroup study [4] determines Frobenius, genus, and type but does not state the all-length spectrum here. The general work on perfect semigroups [5] introduces isolated gaps and algorithms rather than this Fibonacci-family distribution.

The all-length recurrence (3) is the new structural content, not a reinterpretation of the existing isolated-gap count. The formula is derived transparently from an established Apéry theorem; any unindexed prior computation of the same full spectrum would affect priority.

## Limitations
The classification concerns only the shifted-Fibonacci family \(S_a\) for \(a\ge5\). It does not classify the *locations* of all gap blocks, other shifted recurrence families, or arbitrary numerical semigroups. The proof depends on the established Apéry formula in [1] and on Zeckendorf uniqueness. A published Apéry formula and a generic enumeration algorithm logically permit computation of this finite histogram for each fixed parameter; the new contribution is a closed uniform full-spectrum theorem and its exact structural recurrence. The available comparisons do not certify global mathematical priority, and no independent audit of this proof is claimed.

## References
1. A. M. Robles-Pérez and J. C. Rosales, *The extended Frobenius problem for Fibonacci sequences incremented by a Fibonacci number*, arXiv:2210.00816 (first public version 2022-10-03), *Mediterranean Journal of Mathematics* 20 (2023), 222, Theorem 4.6; https://arxiv.org/abs/2210.00816 and https://doi.org/10.1007/s00009-023-02428-9.
2. *Isolated gaps in Fibonacci-shifted numerical semigroups*, public mathematical research record, 2026-11-02; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-isolated-gaps-in-fibonacci-shifted-numerical-semigroups--cb7605e44e01 (readable `RESULT.md`).
3. *Pseudo-Frobenius spectrum and Padovan type of shifted-Fibonacci numerical semigroups*, public mathematical research record, 2026-10-18; https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-pseudo-frobenius-spectrum-and-padovan-type-of-shifted-fibonacci--3a32d9f79cbe (`RESULT.md`).
4. J. M. López-Medel, A. M. Robles-Pérez, and J. C. Rosales, *The extended Frobenius problem for r-Fibonacci sequences shifted by r-Fibonacci numbers*, *Arabian Journal of Mathematics* 14 (2025), 233--252; https://doi.org/10.1007/s40065-025-00513-3.
5. M. A. Moreno-Frías and J. C. Rosales, *The covariety of perfect numerical semigroups with fixed Frobenius number*, arXiv:2305.14967 (first public version 2023-05-24); https://arxiv.org/abs/2305.14967.
