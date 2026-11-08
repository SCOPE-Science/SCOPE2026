# Eleven dyadic zeros per Narayana period, from modulus \(64\) onward

## Finding

Let \((u_n)_{n\ge0}\) be the shifted Narayana-cows sequence
\[
u_0=u_1=0,\quad u_2=1,\quad u_{n+3}=u_{n+2}+u_n\quad(n\ge0).
\]
For every integer \(k\ge1\), the least period of this scalar sequence modulo \(2^k\) is
\[
T_k=7\cdot2^{k-1}.
\]
Let \(Z_k=\#\{0\le n<T_k:2^k\mid u_n\}\). Then
\[
(Z_1,Z_2,Z_3,Z_4,Z_5)=(3,4,5,5,7),\qquad
\boxed{Z_k=11\quad\text{for all }k\ge6.}
\]
For \(k\ge6\), precisely two zeros have \(n\equiv0\pmod7\), eight have \(n\equiv1\pmod7\), and one has \(n\equiv5\pmod7\). No other residue class modulo seven contains a zero.

## Assumptions and scope

All indices are nonnegative integers, and divisibility includes \(u_0=0\). The count is per *least* period, with endpoints \(0\le n<T_k\). This is the zero-residue distribution for the canonical Narayana-cows sequence shifted by two positions; shifting does not change counts per full period. The theorem concerns divisibility by powers of two, not distribution across all residues or divisibility at odd prime powers.

## Proof

**1. Companion matrix and least periods.** Put
\[
M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},\qquad
v=(0,0,1)^{\mathsf T},\qquad u_n=e_1^{\mathsf T}M^nv.
\]
Direct matrix multiplication gives
\[
M^7=\begin{pmatrix}3&2&4\\4&3&6\\6&4&9\end{pmatrix}=I+2B,
\quad B=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix},
\]
\[
M^{14}=I+4\begin{pmatrix}10&7&15\\15&10&22\\22&15&32\end{pmatrix},
\]
and
\[
M^{28}=I+8C,\qquad
C=\begin{pmatrix}1080&737&1583\\1583&1080&2320\\2320&1583&3400\end{pmatrix}.
\]
The order of \(M\) modulo two is exactly seven (since \(M^7=I\pmod2\), \(M\ne I\pmod2\), and seven is prime). The displayed matrices prove that the orders modulo four and eight are fourteen and twenty-eight respectively. For \(k\ge3\), if \(M^{T_k}=I+2^kC_k\) with \(C_k\equiv C\pmod2\), then squaring gives \(M^{2T_k}=I+2^{k+1}C_{k+1}\), \(C_{k+1}\equiv C_k\pmod2\). Since \(C\not\equiv0\pmod2\), the order doubles at every level. Moreover, \(v,Mv,M^2v\) have determinant \(-1\). Thus any scalar period forces \(M^Tv=v\) and then \(M^T=I\), proving the asserted *least* scalar period.

**2. The two nonsingular zero branches.** Modulo two, the seven values are \((0,0,1,1,1,0,1)\). Thus zeros can occur only for \(n\equiv0,1,5\pmod7\). The twenty-eight values modulo eight have zeros exactly at
\[
n\in\{0,1,15,21,26\}.
\]
In particular the branches \(n\equiv0\) and \(n\equiv5\pmod7\) contain respectively two and one zeros. For \(k\ge3\), the matrix congruence from Step 1 implies
\[
u_{n+T_k}-u_n\equiv2^k e_1^{\mathsf T}C M^nv\pmod{2^{k+1}}.
\]
For \(n\equiv0\) or \(5\pmod7\), the last coefficient is odd (check \(e_1^{\mathsf T}C M^nv\equiv1\pmod2\) for those two classes). Hence exactly one of the lifts \(n\) and \(n+T_k\) is a zero modulo \(2^{k+1}\). Each of these two branch counts is therefore stable for all \(k\ge3\).

**3. The singular branch.** Write \(n=1+7t\). Since \(M^7=I+2B\), direct binomial expansion yields
\[
u_{1+7t}=\sum_{j\ge1}2^jc_j\binom tj,\qquad
(c_1,c_2,c_3)=(3,19,129),
\]
where \(c_j=e_1^{\mathsf T}M B^jv\). This sum is finite for integer \(t\ge0\). Reduction modulo four gives \(u_{1+7t}\equiv2t\pmod4\), so odd \(t\) cannot contribute for \(k\ge2\). When \(t\equiv2\pmod4\), reduction modulo sixteen gives \(u_{1+7t}\equiv8\pmod{16}\): the first two binomial summands are each congruent to \(12+8a\pmod{16}\) for \(t=2+4a\), the third vanishes because \(\binom t3\) is even, and higher summands are multiples of sixteen. Thus \(k\ge4\) requires \(t=4s\).

Put \(d_j=e_1^{\mathsf T}M C^jv\). From the displayed matrix,
\[
d_1=2320,\qquad d_2=12899489.
\]
Since \(M^{28}=I+8C\), for positive integer \(s\) we have
\[
u_{1+28s}=\sum_{j\ge1}8^jd_j\binom sj=32s\,g(s),
\]
where the convergent \(2\)-adic power series
\[
g(s)=580+d_2(s-1)
 +\sum_{j\ge3}\frac{2^{3j-5}d_j}{j!}
 \prod_{h=1}^{j-1}(s-h)
\]
extends to every \(s\in\mathbb Z_2\). The displayed coefficients are multiples of eight in \(\mathbb Z_2\) for every \(j\ge3\): indeed \(3j-5-\nu_2(j!)\ge3\) for \(j\ge3\). Their valuations tend to infinity. Each integral polynomial in the sum is \(1\)-Lipschitz on \(\mathbb Z_2\). Consequently
\[
g(s)=580+d_2(s-1)+8h(s),\quad h:\mathbb Z_2\to\mathbb Z_2\ \text{is }1\text{-Lipschitz}.
\]
Because \(d_2\) is odd, \(\nu_2(g(s)-g(t))=\nu_2(s-t)\) for all \(s,t\in\mathbb Z_2\). The map \(g\) is a bijection modulo every \(2^m\): it is injective by the isometry property and therefore surjective on the finite residue ring. Compatible inverse residues yield exactly one \(2\)-adic root \(s_*\). Reduction modulo two gives \(g(s)\equiv s-1\pmod2\), hence \(s_*\) is odd and
\[
\nu_2(u_{1+28s})=5+\nu_2(s)+\nu_2(s-s_*)
\]
for each positive integer \(s\); \(s=0\) gives a zero separately. For \(k\ge6\), the allowable \(t\) range \(0\le t<2^{k-1}\), with \(t=4s\), means \(0\le s<2^{k-3}\). As \(s_*\) is odd, the divisibility condition is exactly
\[
s\equiv0\pmod{2^{k-5}}\quad\text{or}\quad
s\equiv s_*\pmod{2^{k-5}}.
\]
These two distinct classes each have four representatives modulo \(2^{k-3}\), giving exactly eight zeros in this branch. (At \(s=0\), the first congruence still correctly includes \(u_1=0\).)

**4. Small moduli.** Direct exact recurrence in one period yields \(Z_1=3\), \(Z_2=4\), \(Z_3=5\), \(Z_4=5\), and \(Z_5=7\). Steps 2 and 3 prove \(Z_k=2+8+1=11\) for every \(k\ge6\), as required.

## Verification

Run `python3 checker.py` (Python standard library only). It checks the matrix identities, period base-step obstructions, the coefficients controlling the \(2\)-adic map, and every zero residue in a full period for \(1\le k\le12\). At \(k=6\) the exact zero residues are \(\{0,1,29,57,85,113,141,169,197,217,222\}\). The finite checker does *not* establish the infinite theorem; the matrix lifting and \(2\)-adic isometry arguments above do.

## Relationship to prior work

Guadalupe (2021) gives a complete **3-adic** valuation treatment of the Narayana sequence, motivating analogous local questions at two. Kirthi (2015) studies periods **modulo primes** and autocorrelations, not zero counts modulo unbounded powers of two. OEIS A271953 tabulates small-modulus Narayana periods, but not this stable exact zero count. These prior works supply the recurrence context and some lower-modulus observations; the present classification is a different two-adic counting statement. Absence from inspected sources is not proof that no unindexed equivalent exists.

## Limitations

This result does not determine the valuation of every individual term, the full frequency distribution modulo \(2^k\), or analogues for odd prime powers. The originality comparison is limited to inspected literature and accessible records. No independent mathematical audit has yet been performed.

## References

1. R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187, first posted 2021-12-12, https://arxiv.org/abs/2112.06187.
2. K. Kirthi, *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745, first posted 2015-09-17, https://arxiv.org/abs/1509.05745.
3. OEIS A271953, *Periods of A000930 modulo n*, https://oeis.org/A271953, accessed 2026-11-05 UTC.
4. X. Lin, *On the Recurrence Properties of Narayana's Cows Sequence*, *Symmetry* 13 (2021), article 149, https://doi.org/10.3390/sym13010149.
