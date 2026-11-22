# Two dyadic isometric branches and singleton residue balls for Narayana numbers

## Finding
Let \(u_0=0\), \(u_1=u_2=1\), and \(u_{n+3}=u_{n+2}+u_n\) for every integer \(n\ge0\). For every pair of distinct nonnegative integers \(s,t\), and each \(r\in\{3,4\}\), the **exact difference valuation** is
\[
\nu_2(u_{r+7s}-u_{r+7t})=1+\nu_2(s-t).
\]
Thus for every integer \(k\ge1\), as \(j\) runs over \(0\le j<2^{k-1}\), the values \(u_{3+7j}\pmod{2^k}\) represent **each odd residue exactly once**, and \(u_{4+7j}\pmod{2^k}\) represent **each even residue exactly once**. In particular, the full Narayana sequence represents **every residue modulo every positive power of two**.

The least period of the full sequence modulo \(2^k\) is \(P_k=7\cdot2^{k-1}\). For \(k\ge3\), every target residue \(y\equiv2\) or \(7\pmod8\) has **exactly one** preimage among the \(P_k\) indices of a least period:
\[
\#\{0\le n<P_k:u_n\equiv y\pmod{2^k}\}=1
\quad (y\bmod8\in\{2,7\}).
\]
Hence the least fiber size is one for all \(k\ge3\), and at least one quarter of the output classes have singleton fibers in a complete period. The theorem does **not** claim that these are the only singleton fibers.

## Assumptions and scope
The recurrence and indexing are fixed as written; all indices are nonnegative. For nonzero integers \(m\), \(\nu_2(m)\) denotes the exponent of two dividing \(m\). The asserted valuation concerns only differences at distinct indices. A fiber is counted with indices in precisely one *least* period, not as a set of all integer occurrences. The two disjoint parity branches are specified by indices congruent to three and four modulo seven, respectively. No assertion is made for odd-prime-power moduli.

## Proof
**1. Exact seven-step matrices.** Let
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},
\quad v=\begin{pmatrix}0\\1\\1\end{pmatrix},\quad e=(1,0,0).
\]
Then \(u_n=eM^nv\) for \(n\ge0\). Direct integral matrix multiplication gives
\[
M^7=I+2B,\quad B=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix},
\]
\[
M^{14}=I+4C,\quad C=B+B^2=\begin{pmatrix}10&7&15\\15&10&22\\22&15&32\end{pmatrix}.
\]
Also \(M^3v=(1,2,3)^T\) and \(M^4v=(2,3,4)^T\), and the four exact scalar products are
\[
eBM^3v=9,\quad eBM^4v=13,\quad eCM^3v=69,\quad eCM^4v=101.
\]
All four numbers are odd.

**2. Uniform increment congruence.** Write \(M^{7\cdot2^h}=I+2^{h+1}D_h\) for \(h\ge0\). The preceding identities give \(D_0=B\) and \(D_1=C\). For \(h\ge1\), squaring yields
\[
D_{h+1}=D_h+2^h D_h^2,\qquad D_h\equiv C\pmod2.
\]
Since \(M^7\equiv I\pmod2\), for any \(j\ge0\) the vector \(M^{r+7j}v\) reduces modulo two to \(M^rv\). Consequently, for both \(r\in\{3,4\}\), every \(j,h\ge0\) satisfies
\[
u_{r+7(j+2^h)}-u_{r+7j}
=2^{h+1}eD_hM^{r+7j}v
\equiv2^{h+1}\pmod{2^{h+2}}.
\]
Here the scalar factor is odd: for \(h=0\) this follows from the two products with \(B\); for \(h\ge1\) it follows from the products with \(C\). If \(s>t\) and \(s-t=2^h w\) with \(w\) odd, sum the preceding congruence over \(w\) successive increments of size \(2^h\). The resulting difference is still \(2^{h+1}\pmod{2^{h+2}}\). This proves the claimed exact valuation for every pair of distinct nonnegative indices.

**3. Two complete parity charts.** The initial values \(u_3=1\) and \(u_4=2\), together with \(M^7\equiv I\pmod2\), show that the first chart is always odd and the second always even. For a fixed \(k\ge1\), the exact valuation implies that two chart indices give the same value modulo \(2^k\) if and only if their parameters are congruent modulo \(2^{k-1}\). Each chart therefore gives \(2^{k-1}\) distinct values of its parity, and so maps bijectively onto the full corresponding parity class. Their union proves surjectivity.

**4. The least period.** The matrix identity in step 2 gives \(M^{7\cdot2^{k-1}}\equiv I\pmod{2^k}\), an upper bound for every sequence period. Modulo two, the sequence has nonconstant least period seven: its first seven values are \(0,1,1,1,0,1,0\), and seven is prime. Thus any period \(T\) modulo \(2^k\) must be divisible by seven. For \(T=7m\), the equality \(u_{3+T}\equiv u_3\pmod{2^k}\) and the exact valuation theorem force \(2^{k-1}\mid m\). This proves the least period is exactly \(P_k\).

**5. Singleton output balls.** Direct recurrence evaluation in one complete period modulo eight (length \(28\)) gives, for \(r=0,\ldots,6\), the ordered values \(u_{r+7j}\pmod8\) with \(j=0,1,2,3\):
\[
\begin{array}{c|c}
r&\text{four values modulo }8\\\hline
0&(0,6,0,6)\\
1&(1,1,1,1)\\
2&(1,5,5,1)\\
3&(1,3,5,7)\\
4&(2,4,6,0)\\
5&(3,1,3,1)\\
6&(4,4,0,0)
\end{array}
\]
Hence every index attaining a target \(y\equiv7\pmod8\) lies in the third residue branch \(n\equiv3\pmod7\), and every index attaining \(y\equiv2\pmod8\) lies in the fourth branch \(n\equiv4\pmod7\). For \(k\ge3\), the least period is a multiple of 28, so these exclusions persist; by step 3, the one eligible branch attains each target of its parity **exactly once**. This proves the singleton claim. There are precisely \(2\cdot2^{k-3}=2^{k-2}\) target classes in these two congruence balls, one quarter of all \(2^k\) targets.

## Verification
Run `python3 verify.py` alongside this document. The checker reconstructs the two exact matrix identities, tests both parity-chart permutations and surjectivity for every \(1\le k\le14\), checks the sharp periods and both singleton congruence balls through \(2^{14}\), and tests 1,920 additional high-precision modular increment identities up to \(2^{81}\). All tests are exact-integer calculations. Exhaustive checks are confined to the named finite moduli; the unrestricted theorem follows from the matrix proof, not from finite enumeration.

## Relationship to prior work
Kuloğlu, Özkan and Shannon (2022), Theorems 2.1 and 2.5, give periodicity and prime-power **period lifting** for this same recurrence; they do not determine which scalar residues occur or the multiplicity of each target. Franzone and Harrington (2024), Section 3, enumerate selected index sets for prescribed prime moduli in constructing Narayana-cow Sierpiński and Riesel numbers; they do not establish the two all-power parity bijections or the singleton target balls. Lin (2021) studies recurrence identities, not these two-adic fibers. Guadalupe (2021) gives three-adic valuation information rather than binary target fibers.

Related modular recurrence work classifies cycles of **three-coordinate state maps** for generalized Narayana recurrences modulo \(2^k\); its cycle formulas imply the period bound but do not, by themselves, classify **first-coordinate fibers** or these two exact isometric index charts. A separate study gives exact two-adic *valuations* of Narayana numbers, which controls divisibility and zero targets but does not imply that every unit and every even residue has a chart preimage, nor uniqueness for the two specified nonzero output classes. The distinction is in the mathematical implications, not merely terminology.

## Limitations
Only two index branches and two singleton output classes modulo eight are classified; other index branches can also contribute singleton targets, and their complete spectrum is not claimed. No general expression for all target multiplicities is asserted. Standard matrix lifting underlies the proof and may have appeared in a form that entails the chart theorem; bibliographic priority is not certified. The published 2015 cryptographic Narayana study and any unindexed earlier congruence tables leave residual search risk. The executable checks are finite and do not constitute an independent audit.

## References
1. X. Lin, *On the Recurrence Properties of Narayana's Cows Sequence*, Symmetry 13 (2021), 149; published 2021-01-17, https://www.mdpi.com/2073-8994/13/1/149 .
2. B. Kuloğlu, E. Özkan and A. G. Shannon, *The Narayana Sequence in Finite Groups*, Fibonacci Quarterly 60(5) (2022), 212–221, https://www.fq.math.ca/Papers1/60-5/kologlu.pdf .
3. K. Franzone and J. Harrington, *Sierpiński and Riesel Numbers in Narayana's Cow Sequence*, Integers 24 (2024), A10; published 2024-01-29, https://math.colgate.edu/~integers/y10/y10.pdf .
4. R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187 (2021), https://arxiv.org/abs/2112.06187 .
5. K. Kirthi, *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745 (2015), https://arxiv.org/abs/1509.05745 .
6. *Complete periodic-cycle spectra of the generalized Narayana recurrence modulo powers of two*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-periodic-cycle-spectra-of-the-generalized-narayana-recu--849f5443ff2b .
7. *A complete binary valuation law and bounded-discrepancy density for Narayana numbers*, publicly available 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-complete-binary-valuation-law-and-bounded-discrepancy-density--145313dde067 .
