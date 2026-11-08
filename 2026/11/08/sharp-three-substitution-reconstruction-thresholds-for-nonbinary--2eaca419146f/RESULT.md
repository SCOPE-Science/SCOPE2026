# Sharp three-substitution reconstruction thresholds for nonbinary alphabets

## Finding

For every integer alphabet size \(q\geq 3\) and word length \(n\geq 6\), let \(S_3(x)=\{z\in\Sigma_q^n:d_H(z,x)=3\}\). Define
\[
T_3(n,q)=\max_{x\neq y}|S_3(x)\cap S_3(y)|.
\]
Then
\[
\boxed{T_3(n,q)=\begin{cases}
2(n-2)(2n-5),&q=3,\\
\frac{(n-2)(n-1)(q-2)(q-1)^2}{2},&q\geq4.
\end{cases}}
\]
The maximizing center distance is **uniquely** \(d_H(x,y)=2\) when \(q=3\), and **uniquely** \(d_H(x,y)=1\) when \(q\geq4\). Here uniqueness refers to the distance, not to the centers: every pair at that distance attains the maximum.

Consequently, in the uncoded channel in which the observed reads are arbitrarily selected *distinct* outputs from exactly three symbol substitutions, the smallest number of distinct reads guaranteeing a unique original word is \(T_3(n,q)+1\). This is a worst-case, zero-error identification threshold; repeated copies of an identical read do not count as additional distinct reads.

## Assumptions and scope

The alphabet \(\Sigma_q\) is any set with \(q\) elements; no field structure or probability model is assumed. The Hamming distance is the number of positions containing unequal symbols. A legal read differs from its source in **exactly** three coordinates, with each changed symbol unequal to the original. We impose \(n\geq6\) and \(q\geq3\). The unknown source can be any element of \(\Sigma_q^n\), with no coding constraint.

Two possible source words are observationally indistinguishable from a set of reads if every read belongs to the exact-three substitution spheres of both. Thus the maximum intersection cardinality is the precise worst-case ambiguity threshold: an intersection of size \(T_3\) supplies an ambiguous set of that many distinct reads, while no pair of sources accommodates \(T_3+1\) such reads.

## Proof

**Step 1: exact intersection by center separation.** Fix distinct \(x,y\) with \(d=d_H(x,y)\). In each of the \(d\) positions where the centers differ, a candidate output \(z\) can equal \(x\), equal \(y\), or equal neither (with \(q-2\) choices). Their contributions to the two distance counters are respectively \(v\), \(u\), and \(uv\). In any of the \(n-d\) positions where the centers agree, \(z\) either agrees with both (one choice) or differs from both (\(q-1\) choices). Therefore
\[
F_d(n,q):=|S_3(x)\cap S_3(y)|
=[u^3v^3](u+v+(q-2)uv)^d(1+(q-1)uv)^{n-d}.
\]
This depends only on \(n,q,d\). Necessarily \(F_d=0\) for \(d>6\), by the triangle inequality. For \(1\leq d\leq6\), coefficient extraction gives the following complete list:
\[
\begin{aligned}
F_1&=\tfrac12(n-2)(n-1)(q-2)(q-1)^2,\\
F_2&=(n-2)(q-1)\bigl(n(q-1)+q^2-7q+7\bigr),\\
F_3&=(q-2)\bigl(6n(q-1)+q^2-22q+22\bigr),\\
F_4&=6\bigl(n(q-1)+2q^2-12q+12\bigr),\\
F_5&=30(q-2),\\
F_6&=20.
\end{aligned}
\]
These expressions can also be checked directly by classifying the choices at center-differing coordinates and choosing the same number of changes on the remaining shared coordinates. In particular, write \(a\) for the number of positions at which \(z=x\neq y\) and also, necessarily, for the number with \(z=y\neq x\); write \(b=d-2a\) for the number where \(z\) is a third symbol; and write \(c=3-a-b\) for changed common coordinates. Then the exact count is
\[
F_d=\sum_{\substack{a,b,c\geq0\\2a+b=d\\a+b+c=3}}
\frac{d!}{a!^2b!}\,(q-2)^b\binom{n-d}{c}(q-1)^c.
\]
The sum is understood as zero if \(c>n-d\).

**Step 2: no distance three through six maximizes.** Set \(s=n-6\geq0\) and \(r=q-3\geq0\), and put \(A(r)=4+4r+r^2\). For each \(d\in\{3,4,5,6\}\), direct subtraction from the six formulas yields
\[
F_2-F_d=A(r)s^2+L_d(r)s+K_d(r),
\]
where the coefficient tuples of \(L_d\) and \(K_d\) (in ascending powers of \(r\)) are as follows:

| \(d\) | Coefficients of \(L_d\) | Coefficients of \(K_d\) |
|---:|:---|:---|
| 3 | \((18,15,5,1)\) | \((19,11,7,3)\) |
| 4 | \((18,27,11,1)\) | \((20,32,16,4)\) |
| 5 | \((30,33,11,1)\) | \((26,38,28,4)\) |
| 6 | \((30,33,11,1)\) | \((36,68,28,4)\) |

Every coefficient of these polynomials is positive, so \(F_2>F_d\) for all \(d=3,4,5,6\) and all permitted parameters.

**Step 3: the alphabet-size transition.** At \(q=3\), direct subtraction gives
\[
F_2-F_1=2(n-2)(n-4)>0.
\]
For every integer \(q\geq4\), instead,
\[
2(F_1-F_2)=(n-2)(q-1)\bigl((n-6)(q-1)(q-4)+3q^2-13q+8\bigr)>0.
\]
The last factor is positive: its first term is nonnegative, while \(3q^2-13q+8\) is strictly increasing for \(q\geq4\) and equals \(4\) at \(q=4\). Thus \(F_1>F_2\) for \(q\geq4\), whereas \(F_2>F_1\) for \(q=3\). Combining with Step 2 and \(F_d=0\) for \(d>6\) yields the asserted sharp maximum and its unique maximizing center distance.

**Step 4: reconstruction threshold.** For each permitted \(n,q\), a pair of centers at the maximizing distance exists and admits exactly \(T_3(n,q)\) common, distinct legal outputs; this many observed outputs therefore cannot ensure unique reconstruction. Conversely, \(T_3(n,q)+1\) distinct legal outputs cannot all belong to the spheres of two different source words, by the proved maximum. Hence the number is both sufficient and necessary.

## Verification

The standalone standard-library Python checker `verify.py` computes the six intersection sizes by a second multinomial-coefficient sum; checks each closed expression and positivity identity for \(6\leq n\leq30\) and \(3\leq q\leq14\); and independently counts actual length-\(n\) received words for \((n,q)=(6,3),(7,3),(6,4),(6,5)\). Execute `python verify.py` alongside this file. The computed intersection vectors by center distance \(1,\ldots,6\) for these four cases are respectively \((40,56,37,36,30,20)\), \((60,90,49,48,30,20)\), \((180,156,116,84,60,20)\), and \((480,336,243,156,90,20)\). The infinite result is proved by the symbolic identities and sign argument above; numerical checks alone would not prove it.

## Relationship to prior work

Papadopoulou, Yehezkeally, Rameshwar and Wachter-Zeh (arXiv:2610.30001, first public 2026-10-21) analyze reconstruction under exact-weight substitutions for **binary** words and demonstrate limitations of majority decoding. Their binary theorem does not imply the nonbinary extremal-distance switch established here. Junnila, Laihonen, Lehtilä and Devaraj (arXiv:2606.09158, first public 2026-06-08) study intersections of **Hamming balls** (distance at most a radius), including several centers. Classical Hamming association-scheme intersection numbers, and the elementary two-sphere coefficient formula itself, are known; this finding does not claim their discovery. The asserted contribution is the complete sharp optimization of exact-three **sphere** intersections over every distinct center pair for all \(q\geq3,n\geq6\), including the ternary/other-alphabets transition and its exact reconstruction threshold. Danoyan (2013) studies two-sphere intersections over the binary cube; that work does not itself provide this nonbinary optimized threshold.

## Limitations

No assertion is made for \(q=2\), \(n<6\), substitution radii other than exactly three, non-Hamming channels, a coded source alphabet subset, or reconstruction from repeated identical reads. The result does not assert novelty of general Hamming intersection numbers or an optimal polynomial-time reconstruction algorithm. The older intersection-number literature is extensive and may contain equivalent extremal specializations not identified in the accessible material; independent priority and correctness validation have not been performed.

## References

1. V. Papadopoulou, Y. Yehezkeally, V. A. Rameshwar and A. Wachter-Zeh, *When Majority-Vote Fails: Sequence Reconstruction under Fixed-Weight Substitutions*, arXiv:2610.30001 (2026), https://arxiv.org/abs/2610.30001 (first publicly submitted 2026-10-21).
2. V. Junnila, T. Laihonen, T. Lehtilä and P. P. Devaraj, *The Size of the Intersection of \(q\)-ary Hamming Balls*, arXiv:2606.09158 (2026), https://arxiv.org/abs/2606.09158 (first publicly submitted 2026-06-08).
3. H. E. Danoyan, *On Some Properties of Intersection and Union of Spheres in Hamming Metric*, Mathematical Problems of Computer Science **39** (2013), pp. 119–124, https://mpcs.sci.am/index.php/mpcs/article/view/429.
