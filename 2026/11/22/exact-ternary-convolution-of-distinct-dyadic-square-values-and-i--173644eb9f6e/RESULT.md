# Exact ternary convolution of distinct dyadic square values and its sixth Fourier moment

## Finding

For every integer \(k\ge1\), let \(Q_k=\{x^2\bmod 2^k:x\in\mathbb Z/2^k\mathbb Z\}\), with **each distinct square value counted once**, including zero. Define the ordered three-sum multiplicity
\[
R_k(t)=\#\{(a,b,c)\in Q_k^3:a+b+c\equiv t\pmod{2^k}\}.
\]
Put \(s_0=1\), \(s_1=s_2=2\), and \(s_j=2^{j-3}+s_{j-2}\) for \(j\ge3\). For every \(k\ge5\) set \(u=2^{k-3}\), \(A=s_{k-4}\), \(B=2^{k-5}\). The **complete target-by-target formula** is
\[
R_k(t)=\begin{cases}
R_{k-2}(t/4),&t\equiv0\pmod4,\\
3(A^2+B^2),&t\equiv1\pmod8,\\
3uA,&t\equiv2\pmod8,\\
u^2,&t\equiv3\pmod8,\\
6AB,&t\equiv5\pmod8,\\
3uB,&t\equiv6\pmod8,\\
0,&t\equiv7\pmod8.
\end{cases}
\]
For \(k\ge6\), the largest fiber is exactly \(2^{2k-6}\), attained **precisely** for \(t\equiv3\pmod8\). Define the ordered triple-collision energy, equivalently the normalized sixth Fourier moment, by
\[
E_k=\sum_{t\bmod 2^k}R_k(t)^2
=2^{-k}\sum_{h\bmod2^k}\left|\sum_{a\in Q_k}e^{2\pi i ha/2^k}\right|^6.
\]
It obeys the exact recurrence for \(k\ge5\):
\[
E_k=E_{k-2}+2^{k-3}\left(9(A^2+B^2)^2+9u^2 A^2+u^4+36A^2B^2+9u^2B^2\right).
\]
The leading sixth-moment constant is the explicit rational number
\[
\boxed{\lim_{k\to\infty}2^{-5k}E_k=\frac{485}{9427968}.}
\]

## Assumptions and scope

All additions occur in the ring \(\mathbb Z/2^k\mathbb Z\). Input variables \(a,b,c\) are **square residues as values**, not original square roots. They are ordered, may repeat, and zero is included. The assertion applies to all target residues and all depths, with the base arrays below. For \(k=1,2,3,4\), the arrays \((R_k(t))_{t=0}^{2^k-1}\) are respectively
\[
(4,4),\quad (1,3,3,1),\quad(4,6,3,1,4,6,3,0),
\]
\[
(1,6,6,4,3,6,6,0,3,6,6,4,1,6,6,0).
\]

## Proof

**1. Square-value decomposition.** For \(j\ge3\), the odd square values are exactly \(1+8\mathbb Z/2^j\mathbb Z\), comprising \(2^{j-3}\) classes; all even square values are \(4Q_{j-2}\), under an injective map from \(\mathbb Z/2^{j-2}\mathbb Z\) to \(\mathbb Z/2^j\mathbb Z\). The two sets are disjoint. This proves both \(Q_j=(1+8\mathbb Z/2^j\mathbb Z)\sqcup4Q_{j-2}\) and the cardinality recurrence for \(s_j\). Odd units congruent to one modulo eight are squares by the standard elementary square-root lifting: an odd square root modulo \(2^r\) can be adjusted by \(2^{r-1}\) to change its square by \(2^r\) at the next precision.

**2. Even square residues.** At \(k\ge5\), the even-square set \(4Q_{k-2}\) splits into those congruent to zero and four modulo eight. The zero-class consists of \(16Q_{k-4}\) and has size \(A\); the four-class consists of the odd-square part of \(4Q_{k-2}\), and has size \(B\). The odd-square class has size \(u\).

**3. Exhaustive triple decomposition.** If all three summands are even-square values, division by four bijects the triples at target \(t\equiv0\pmod4\) with triples counted by \(R_{k-2}(t/4)\); no others occur. With exactly one odd square, choose the odd position in three ways and the two even-square values freely. Their parities modulo eight force the target class to be one when the even classes agree (\(A^2+B^2\) pairs), or five when they differ (\(2AB\) pairs). Because the odd-square values form the complete class one modulo eight, **for each fixed pair** there is exactly one required odd square at each target of its permitted class. This gives \(3(A^2+B^2)\) and \(6AB\). With exactly two odd squares, the even summand is in the zero or four class; there are three choices for its position and \(u\) ordered odd pairs summing to a fixed target minus this even summand. This gives \(3uA\) for targets two modulo eight and \(3uB\) for targets six modulo eight. With three odd squares, any choice of the first two of the \(u\) elements determines the third; this gives \(u^2\) on targets three modulo eight. The residue class seven is absent. These cases partition every triple, proving the complete recurrence and, using direct base enumeration, all depths.

**4. Sharp maximum.** For \(k\ge6\), the cardinality recurrence gives \(A\le B=u/4\). Consequently, the five nonrecursive positive fiber values are at most \(3u^2/8,3u^2/4,u^2,3u^2/8,3u^2/4\), respectively; only the class three attains \(u^2\). Every recursive target has at most \(s_{k-2}^2\) representations, since the first two values determine the third, and \(s_{k-2}<u\) for all \(k\ge6\). Hence no recursive target is maximal, establishing both the exact maximum and all maximizers.

**5. Energy and asymptotics.** The recursive targets are in bijection with all targets modulo \(2^{k-2}\), so their squared fiber contributions total \(E_{k-2}\). Each of the five other nonzero residue classes contains \(2^{k-3}\) targets with the displayed constant value, proving the recurrence. For \(k\to\infty\), \(A/2^k\to1/96\), \(B/2^k=1/32\), and \(u/2^k=1/8\); thus the five fiber values divided by \(2^{2k}\) approach \(5/1536,1/256,1/64,1/512,3/256\). Since \(E_{k-2}/2^{5k}\) has scale factor \(1/1024\), convergence to the geometric fixed point follows directly by iterating the exact energy recurrence and bounding its exponentially decaying coefficient errors. Its value is
\[
\frac{\bigl((5/1536)^2+(1/256)^2+(1/64)^2+(1/512)^2+(3/256)^2\bigr)/8}{1-1/1024}
=\frac{485}{9427968}.
\]
The Fourier identity for \(E_k\) is finite-group Parseval applied to threefold convolution. This completes the proof.

## Verification

Run the self-contained Python 3 file `verify.py` with `python3 verify.py`. It independently enumerates \(Q_k\), performs two circular convolutions, and checks **every target** for \(1\le k\le12\), a total of 8190 target comparisons, together with the sharp maximal fibers, total mass \(s_k^3\), energy recurrence, and the exact rational leading constant. It prints `TRIPLE_SQUARE_IMAGE_CHECK_OK`. The all-depth result follows from the above algebra, not from finite enumeration.

## Relationship to prior work

Harrington–Jones–Lamarche (2014), arXiv:1404.0187, addresses the representability of integers as sums of **two input squares** in a finite residue ring, not the triple-sum multiplicities of distinct output values. Arias–Borja–Rubio (2018/2019), arXiv:1812.11599, studies the **support cardinality** of sums of three squares modulo powers of two; this is an implication of the support of the present recurrence but does not give its unequal fiber counts or sixth Fourier moment. A published study of the **same** dyadic square-value set and its exact Fourier transform, *Sharp Fourier-algebra norms of all dyadic square residues* (2026), computes the sharp absolute-first Fourier norm and square-value cardinality. Its character recurrence allows computation of higher convolutions in principle, but it neither states nor evaluates the five-class target law, the sharp maximizer set, or the sixth-moment constant; the exact all-target evaluation is the distinction claimed here. The triple convolution of the dyadic **parabola graph** is a different group-valued object and does not recover these scalar image-value counts.

## Limitations

This is a modular, ordered triple count on **distinct square values**, not a count of triples of integer square roots and not a classification of integer sums of three squares. The asymptotic constant is a sixth Fourier moment of the image indicator, not the fourth moment or Fourier-algebra projection norm. The published square-set Fourier recurrence is a substantial overlapping tool, and an unstated or implicit equivalent in prior harmonic-analysis literature remains a bibliographic priority risk. Finite checks are corroborating, not an independent audit.

## References

1. J. Harrington, L. Jones, A. Lamarche, *Representing Integers as the Sum of Two Squares in the Ring* \(\mathbb Z_n\), arXiv:1404.0187v1 (2014-04-01), https://arxiv.org/abs/1404.0187.
2. F. Arias, J. Borja, L. Rubio, *Counting Integers Representable as Images of Polynomials Modulo n*, arXiv:1812.11599v2 (2018), https://arxiv.org/abs/1812.11599.
3. *Sharp Fourier-algebra norms of all dyadic square residues: a radical recurrence and two-phase asymptotics* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourier-algebra-norms-of-all-dyadic-square-residues-a-radi--0719daa22b4d.
4. *Dyadic parabola triple convolution: a three-mass law and exact sixth Fourier moment* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dyadic-parabola-triple-convolution-a-three-mass-law-and-exact-si--ebf77605a61b.
