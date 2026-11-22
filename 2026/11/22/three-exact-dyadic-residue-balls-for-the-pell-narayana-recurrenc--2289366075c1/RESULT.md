# Three exact dyadic residue balls for the Pell–Narayana recurrence

## Finding

Let \(P_0=0\), \(P_1=P_2=1\), and \(P_{n+3}=2P_{n+2}+P_n\) for every integer \(n\ge0\). Its complete set of values in the two-adic integers, after closure, is

\[
\overline{\{P_n:n\ge0\}}^{\,\mathbb Z_2}
=(1+2\mathbb Z_2)\;\sqcup\;8\mathbb Z_2\;\sqcup\;(2+256\mathbb Z_2).
\]

Every allowed residue is actually attained by infinitely many nonnegative indices, modulo every prescribed power of two. For \(I_k=\{P_n\bmod 2^k:n\ge0\}\),

\[
|I_1|=2,\qquad
|I_k|=2^{k-1}+2^{\max\{k-3,0\}}+2^{\max\{k-8,0\}}
\quad(k\ge2).
\]

In particular, \(|I_k|=161\cdot 2^{k-8}\) for every \(k\ge8\), and the Haar measure of the closure is exactly \(161/256\). The only even values allowed in the two-adic closure are multiples of eight or numbers congruent to two modulo 256. The theorem concerns *attained residue sets*, not the multiplicity of each residue within a period.

## Assumptions and scope

All indices are nonnegative integers. The recurrence and initial conditions above fix the normalization unambiguously. Write \(\nu_2\) for the two-adic valuation, with \(\nu_2(0)=+\infty\); \(\mathbb Z_2\) denotes the two-adic integers. Congruences and residue sets use all nonnegative indices, not a sampled finite prefix. No hypotheses on an unproved conjecture are needed.

## Proof

**1. Matrix interpolation.** Put

\[
K=\begin{pmatrix}0&1&0\\0&0&1\\1&0&2\end{pmatrix},
\qquad v=\begin{pmatrix}0\\1\\1\end{pmatrix},\qquad e=(1,0,0).
\]

The defining recurrence gives \(P_n=eK^nv\). Direct multiplication yields

\[
K^3=\begin{pmatrix}1&0&2\\2&1&4\\4&2&9\end{pmatrix},
\qquad K^6-I\in4M_3(\mathbb Z),\qquad K^{24}-I\in16M_3(\mathbb Z).
\]

For each of the integer pairs \((n,h)=(2,3),(0,6),(9,24),(21,24)\), set \(D_h=K^h-I\) and \(c_j(n,h)=eD_h^jK^nv\). Because \(D_h\) is divisible by a positive power of two, the uniformly convergent Mahler series

\[
f_{n,h}(t)=\sum_{j=0}^{\infty}c_j(n,h)\binom tj
\qquad(t\in\mathbb Z_2)
\]

extends \(P_{n+ht}\) from nonnegative integer \(t\) to all of \(\mathbb Z_2\). Its first two coefficient valuations, determined by exact integer matrix arithmetic, are

| \((n,h)\) | \(s\) with \(D_h\in2^sM_3(\mathbb Z)\) | \(\nu_2(c_1)\) | \(\nu_2(c_2)\) |
|---|---:|---:|---:|
| \((2,3)\) | 1 | 1 | 5 |
| \((0,6)\) | 2 | 3 | 5 |
| \((9,24)\) | 4 | 9 | 13 |
| \((21,24)\) | 4 | 9 | 15 |

For any \(t,u\in\mathbb Z_2\) and \(j\ge1\), the binomial identity

\[
\binom tj-\binom uj=\sum_{i=1}^j\binom{t-u}{i}\binom{u}{j-i}
\]

and \(i\binom{t-u}{i}=(t-u)\binom{t-u-1}{i-1}\) imply

\[
\nu_2\!\left(\binom tj-\binom uj\right)
\ge\nu_2(t-u)-\lfloor\log_2j\rfloor.
\]

If \(d=\nu_2(c_1)\), the displayed coefficient table gives \(\nu_2(c_2)\ge d+2\). For \(j\ge3\), the matrix divisibility gives \(\nu_2(c_j)\ge sj\), while in each of the four rows \(sj\ge d+1+\lfloor\log_2j\rfloor\). Thus the term \(c_1(t-u)\) has strictly smaller two-adic valuation than the sum of all terms with \(j\ge2\). Consequently

\[
\boxed{\nu_2(f_{n,h}(t)-f_{n,h}(u))
=d+\nu_2(t-u)}
\quad(t\ne u).
\]

A map of \(\mathbb Z_2\) satisfying this identity induces, for each precision, a bijection between index residues and residues of its target disk. Hence its image is exactly \(f_{n,h}(0)+2^d\mathbb Z_2\). Applying the four rows produces the following *four surjective subbranches*:

\[
\begin{aligned}
\{P_{2+3t}:t\ge0\}^{\mathrm{cl}}&=1+2\mathbb Z_2,\\
\{P_{6t}:t\ge0\}^{\mathrm{cl}}&=8\mathbb Z_2,\\
\{P_{9+24t}:t\ge0\}^{\mathrm{cl}}&=258+512\mathbb Z_2,\\
\{P_{21+24t}:t\ge0\}^{\mathrm{cl}}&=2+512\mathbb Z_2.
\end{aligned}
\]

The last two disks partition \(2+256\mathbb Z_2\). This proves that the right side of the claimed image equality is entirely attained in the closure.

**2. No other values.** Modulo two, the recurrence reduces to \(P_{n+3}=P_n\), so the branches \(n\equiv1,2\pmod3\) are always odd. The branch \(n=6t\) lies in \(8\mathbb Z_2\) by the second exact isometry. For the remaining branch \(n=6t+3\), apply the same Mahler expansion with \((n,h)=(3,6)\). Its first four exact coefficients are

\[
(c_0,c_1,c_2,c_3)=(2,256,29184,3330304).
\]

Since \(K^6-I\) is divisible by four, all \(c_j(3,6)\) with \(j\ge4\) are divisible by \(4^4=256\). The three nonconstant coefficients displayed above are also divisible by 256. Therefore

\[
P_{6t+3}\equiv2\pmod{256}
\quad\text{for all }t\ge0.
\]

The four index classes just considered exhaust all nonnegative indices, establishing the reverse inclusion and the exact image identity.

**3. Every precision, and infinitely many hits.** The nonnegative integers are dense in \(\mathbb Z_2\), and all four interpolated maps are continuous. Each of the four image disks is therefore attained modulo every \(2^k\) by nonnegative parameters. Once a parameter gives a residue at precision \(k\), all parameters in some sufficiently small congruence class modulo a power of two give the same residue, hence infinitely many indices do. Projecting the three mutually disjoint two-adic disks modulo \(2^k\), and counting their classes, yields \(|I_1|=2\) and the formula for every \(k\ge2\). Their normalized sizes stabilize to \(1/2+1/8+1/256=161/256\).

## Verification

The accompanying `VERIFY.py` uses exact integers and no external dependencies. It reconstructs the matrix, tests the four coefficient-valuation certificates, the four matrix divisibilities and the nonconstant coefficients for the exceptional branch. It also enumerates the recurrence through the published prime-power period bound \(3\cdot2^{k-1}\) for \(1\le k\le13\), comparing the actual residue set with the exact three-disk formula (98,292 finite recurrence/containment check instances). This is independent finite corroboration of the explicit algebra; the infinite proof is the matrix interpolation and isometry argument above. The period formula itself is established in the cited prior literature and is not presented as a new result.

## Relationship to prior work

Kuloğlu, Özkan and Marin (2023) study the Pell–Narayana recurrence, matrix and modular periods, including the doubling of its period at successive powers of two. The 2025 article *Period of Pell-Narayana sequence in groups* also concerns group orbits and modular periods. Both are distinguished from the present exact value-image theorem: a period length does not determine which residues occur, much less a stable three-ball image and its Haar measure. Related published two-adic image classifications for Pell–Lucas and other *second-order* Lucas recurrences employ similar local methods but do not imply this third-order recurrence's precise disks or its exceptional level \(2^8\). The precise recurrence given above, not a potentially ambiguous sequence label, is used throughout.

## Limitations

The result classifies existence of individual residues, not the distribution of how often they appear in a period. The proof is specialized to the stated third-order recurrence and to the prime two; neither odd-prime distributions nor general third-order recurrences are claimed. Historical priority cannot be guaranteed from indexed literature searches, and comparable unpublished or unindexed local analyses could exist. Independent mathematical validation has not been undertaken.

## References

1. B. Kuloğlu, E. Özkan, M. Marin, *On the period of Pell-Narayana sequence in some groups*, arXiv:2305.04786v1, publicly submitted 27 April 2023, https://arxiv.org/abs/2305.04786 . The source states primary MSC2020 11B39.
2. *Period of Pell-Narayana sequence in groups*, Journal of Combinatorial Mathematics and Combinatorial Computing 128 (2025), 221–238, published online 8 November 2025, https://doi.org/10.61091/jcmcc128-14 .
3. Related published work for comparison: *Three exact 2-adic residue balls for the Pell–Lucas sequence*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-three-exact-2-adic-residue-balls-for-the-pell-lucas-sequence--5a09b024255a . This concerns a distinct second-order sequence.
