# Zero avoidance of Tribonacci recurrences is decided modulo sixteen

## Finding

For every integer \(r\ge1\), start with an arbitrary triple \((a_0,a_1,a_2)\in(\mathbb Z/2^r\mathbb Z)^3\) and extend it by
\[
a_{n+3}=a_{n+2}+a_{n+1}+a_n\qquad(n\ge0).
\]
Call the triple *zero-avoiding* when \(a_n\not\equiv0\pmod{2^r}\) for every \(n\ge0\). Let \(N_r\) be the exact number of such initial triples. Then
\[
N_1=1,\qquad N_2=9,\qquad
N_r=\frac{5\cdot8^r-642}{14}\quad(r\ge3).
\]
In particular, \(\lim_{r\to\infty}N_r/8^r=5/14\).

More sharply, for every \(r\ge4\), an initial triple with at least one odd coordinate is zero-avoiding modulo \(2^r\) **if and only if** its reduction modulo \(16\) is zero-avoiding. Exactly \(1280\) of the \(3584\) primitive initial triples modulo \(16\) are zero-avoiding.

## Assumptions and scope

All residue classes and all triples are counted separately, not up to cyclic rotation. The recurrence is homogeneous with coefficients \((1,1,1)\), and initial triples are unrestricted: they need not equal the distinguished Tribonacci sequence. A triple is *primitive* modulo \(2^r\) if at least one of its coordinates is odd. Zero-avoidance refers to all nonnegative indices, not only to the initial three terms or to one particular period length.

Put
\[
T=\begin{pmatrix}0&1&0\\0&0&1\\1&1&1\end{pmatrix},
\qquad v=(a_0,a_1,a_2)^\mathsf T.
\]
The state after \(n\) steps is \(T^nv\). Because \(\det T=1\), reduction modulo \(2^r\) is a permutation of the finite state space. Every state therefore lies on a purely periodic orbit, and zero-avoidance can be checked over one whole cycle.

## Proof

**1. Finite orbit-incidence lemma modulo sixteen.** Exact enumeration of the entire residue space \((\mathbb Z/16\mathbb Z)^3\), using only modular integer operations, gives the following complete primitive-cycle table:

| Cycle length | Cycles avoiding a zero first coordinate | Cycles containing a zero first coordinate |
| ---: | ---: | ---: |
| \(16\) | \(32\) | \(0\) |
| \(32\) | \(24\) | \(72\) |

Every one of the \(72\) zero-containing cycles has an orbit state \((x,y,z)\) satisfying \(x\equiv0\pmod{16}\) and \(y\not\equiv0\pmod4\). The four integers \(16,32,24,72\), the total \(1280=32\cdot16+24\cdot32\), the complementary total \(2304=72\cdot32\), and the asserted condition on *every* zero-containing cycle are checked exhaustively by the independent, standalone `check.py` attached to this result. The checker iterates all \(4096\) triples, marks every orbit state, and requires its return to its starting state. This exhaustive finite step is part of the proof, not evidence by sampling.

**2. Matrix lifting lemma.** Exact multiplication gives
\[
T^{16}=\begin{pmatrix}
1705&2632&3136\\3136&4841&5768\\5768&8904&10609
\end{pmatrix}.
\]
Thus, writing \(B_4=(T^{16}-I)/8\), one has
\[
B_4\equiv
\begin{pmatrix}1&1&0\\0&1&1\\1&1&2\end{pmatrix}\pmod4.
\]
Repeated squaring proves by induction that for every integer \(k\ge4\),
\[
T^{2^k}=I+2^{k-1}B_k,\qquad
B_{k+1}=B_k+2^{k-2}B_k^2,\qquad B_k\equiv B_4\pmod4,
\]
where every \(B_k\) is integral. The matrix congruence is consistent with Klaška's earlier period calculation; the use of its first row to lift zero-*incidence* is the new step here.

Suppose some state \(w=(x,y,z)^\mathsf T\) on a primitive orbit satisfies \(x\equiv0\pmod{2^k}\) for \(k\ge4\), with \(y\not\equiv0\pmod4\). If \(y\) is odd, use the orbit shift \(T^{2^{k+1}}\). Its first coordinate changes by
\[
2^k(B_{k+1}w)_1\equiv 2^k\pmod{2^{k+1}},
\]
because \((B_{k+1}w)_1\equiv x+y\equiv1\pmod2\). If \(y\equiv2\pmod4\), use instead \(T^{2^k}\). Its first coordinate changes by
\[
2^{k-1}(B_kw)_1\equiv2^k\pmod{2^{k+1}},
\]
because \((B_kw)_1\equiv x+y\equiv2\pmod4\). Either shift changes the \(k\)-th binary digit of the first coordinate without disturbing any lower digit. Both shifts preserve the second coordinate modulo \(4\), since \(T^{2^k}\equiv I\pmod8\) for all \(k\ge4\). Taking the shifted state or the original state according to whether its first coordinate has the next bit set, we obtain a state with first coordinate zero modulo \(2^{k+1}\) and second coordinate still nonzero modulo \(4\). Induction lifts such a state to a zero modulo \(2^r\) for every \(r\ge k\).

Now take any primitive triple modulo \(2^r\), with \(r\ge4\). If its reduction modulo \(16\) avoids zero, then so does the full orbit modulo \(2^r\). Conversely, if its reduction modulo \(16\) hits zero, part 1 supplies some orbit state with first coordinate zero modulo \(16\) and second coordinate nonzero modulo \(4\). The same iterate of the original triple gives a state to which part 2 applies. Therefore its orbit hits zero modulo \(2^r\). This proves the equivalence and yields exactly
\[
P_r=1280\cdot8^{r-4}\quad(r\ge4)
\]
primitive zero-avoiding triples modulo \(2^r\), since every primitive triple modulo \(16\) has precisely \(8^{r-4}\) lifts.

**3. Imprimitive initial conditions and total count.** Let \(P_r\) count primitive zero-avoiding triples. Complete exact enumeration modulo \(2\), \(4\), and \(8\) gives
\[
P_1=1,\qquad P_2=8,\qquad P_3=128.
\]
Every nonzero triple modulo \(2^r\) is uniquely \(2^t\) times a primitive triple modulo \(2^{r-t}\), for \(0\le t<r\); this normalization preserves zero-avoidance of the corresponding recurrence. The zero triple does not avoid zero. Hence
\[
N_r=\sum_{s=1}^rP_s.
\]
For \(r=1,2\) this gives \(1,9\). For \(r\ge3\), inserting the primitive counts and evaluating the geometric sum gives
\[
N_r=137+1280\sum_{j=0}^{r-4}8^j
=\frac{5\cdot8^r-642}{14},
\]
with the sum empty when \(r=3\). The limiting proportion follows immediately.

## Verification

The attached standard-library-only `check.py` verifies the full exhaustive \(16^3\) orbit partition and the lifting seed condition on all \(72\) zero-containing primitive cycles, multiplies the displayed integer matrices, and directly enumerates *every* state modulo \(2^r\) for \(1\le r\le6\). It reports \(N_r=1,9,137,1417,11657,93577\). Run `python3 check.py`; its exact expected output is `check_output.txt`. Verification modulo the larger powers is a cross-check; the infinite assertion is the consequence of the proved matrix lifting lemma and the exhaustive finite base case.

## Relationship to prior work

Klaška, *Tribonacci modulo \(2^t\) and \(11^t\)* (2008), treats primitive periods for sequences with arbitrary initial triples and establishes the key powers-of-two matrix congruences (notably Lemma 2.2). Those congruences do not themselves specify which state cycles meet the zero-coordinate hyperplane; the present theorem adds an exhaustive orbit-incidence classification modulo \(16\) and a lifting argument for that incidence. Bilu, Luca, Nieuwveld, Ouaknine, and Worrell, *On the \(p\)-adic zeros of the Tribonacci sequence* (2022), examine the distinguished Tribonacci sequence and its \(p\)-adic zeros, not all arbitrary initial triples. OEIS A106285 tabulates counts of recurrence orbits, a different invariant from the zero-incidence classification and counts here.

## Limitations

This theorem concerns powers of \(2\), the three-term recurrence with all coefficients \(+1\), and the zero residue, not odd prime-power moduli, other coefficients, or prescribed nonzero target residues. The finite orbit-incidence lemma is computer-enumerated but exhausts all \(4096\) states and uses simple reproducible integer arithmetic. Full equivalence across unindexed mathematical literature cannot be asserted; the named primary sources were reviewed for possible stronger coverage. No independent audit has been performed.

## References

1. Jiří Klaška, *Tribonacci modulo \(2^t\) and \(11^t\)*, Mathematica Bohemica **133** (2008), 377–387. https://dml.cz/bitstream/handle/10338.dmlcz/140627/MathBohem_133-2008-4_5.pdf
2. Yuri Bilu, Florian Luca, Joris Nieuwveld, Joël Ouaknine, and James Worrell, *On the \(p\)-adic zeros of the Tribonacci sequence*, arXiv:2210.16959 (first posted 2022-10-30). https://arxiv.org/abs/2210.16959
3. OEIS A106285, counts of cycles in modular generalized Tribonacci recurrences. https://oeis.org/A106285
