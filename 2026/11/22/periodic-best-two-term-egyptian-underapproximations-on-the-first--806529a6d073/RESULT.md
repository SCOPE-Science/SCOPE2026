# Periodic best two-term Egyptian underapproximations on the first threshold-four numerator ray

## Finding

For every integer \(m\ge1\), put \(u=m+1\), \(q=5m+1=5u-4\), and \(\theta=5/q\). Among all pairs of positive integers \(a\le b\) such that \(1/a+1/b<\theta\), let a *maximizing pair* be one maximizing \(1/a+1/b\). Define for \(s\in\{0,1,2\}\)

\[
B_s(u)=\left\lfloor\frac{(5u-4)(u+s)}{5s+4}\right\rfloor+1,\qquad T_s(u)=(u+s,B_s(u)).
\]

The **complete set of maximizing pairs** is

\[
\begin{cases}
\{T_0(u),T_2(u)\},&m=5,\\
\{T_2(u)\},&m\in\{6,16\},\\
\{T_1(u)\},&m\equiv2\text{ or }3\pmod9,\\
\{T_0(u)\},&\text{otherwise}.
\end{cases}
\]

The cases are disjoint. In the tie case, the two pairs are exactly \((6,40)\) and \((8,15)\), both summing to \(23/120\), strictly less than \(5/26\). Every maximizing pair has distinct denominators, so the classification remains true if \(a<b\) is required.

Consequently the two-step strict greedy underapproximation fails to be best precisely for \(m\equiv2,3\pmod9\) or \(m\in\{6,16\}\); at \(m=5\) the greedy pair is best but is not unique; for all other \(m\) it is uniquely best. The set of integers \(m\ge1\) where greedy is not best has natural density exactly \(2/9\).

This is the first possible numerator threshold: for every reduced fraction \(p/q\) with \(1\le p\le4\), the least positive \(j\) satisfying \(p\mid(q+j)\) is at most \(3\). The fractions \(5/(5m+1)\) are exactly the reduced proper fractions with numerator \(5\) and this threshold equal to \(4\).

## Assumptions and scope

The strict inequality in the definition of underapproximation is essential. All denominators are positive integers, equal denominators are initially allowed, and the best sum is considered among exactly two denominators. The theorem concerns all \(m\ge1\), including the two isolated nonperiodic exceptions and the isolated tie. It makes no assertion for other numerators or for three or more terms.

## Proof

**1. Exhaustive reduction to the first denominator.** Since \(q/5=u-4/5\), every admissible pair has \(a\ge u\). If \(a\ge2u\), then \(1/a+1/b\le2/a\le1/u\), while \(T_0(u)\) has sum greater than \(1/u\); these pairs cannot maximize. It remains to consider \(a=u+s\) for \(0\le s\le u-1\). Put

\[
d_s=5s+4,\qquad X_s=q(u+s),\qquad
b_s=\left\lfloor\frac{X_s}{d_s}\right\rfloor+1,\qquad
t_s=d_s-(X_s\bmod d_s).
\]

Then \(1/(u+s)+1/b_s<5/q\), and \(b_s\) is the smallest integer for which this strict inequality holds, without an ordering requirement. The smallest *legal* second denominator is \(\max\{u+s,b_s\}\). When \(s\le u-2\), one has \(d_s<q\), so \(b_s>u+s\). In all cases the minimum possible approximation error at the first denominator \(u+s\) is at least

\[
E_s=\frac5q-\frac1{u+s}-\frac1{b_s}
=\frac{d_st_s}{X_s(X_s+t_s)},\qquad 1\le t_s\le d_s.
\]

Equality holds for \(s\le u-2\). For \(s=u-1\), using \(E_s\) as a lower bound only strengthens exclusion. Because the right-hand side is strictly increasing in \(t_s\),

\[
E_s\ge\frac{d_s}{X_s(X_s+1)}\ge\frac{d_s}{X_s(X_s+d_s)}.
\]

**2. The greedy error and the first alternative.** Write \(X_0=qu\), \(X_1=q(u+1)\), \(X_2=q(u+2)\). The congruence \(X_0\equiv u^2\pmod4\) yields

\[
E_0=\begin{cases}
16/[X_0(X_0+4)],&u\text{ even},\\
12/[X_0(X_0+3)],&u\text{ odd}.
\end{cases}
\]

For \(s=1\), direct reduction of \(X_1=5u^2+u-4\) modulo \(9\) gives \(t_1=1\) exactly when \(u\equiv3,4\pmod9\); in all other residue classes \(t_1\in\{4,7,9\}\). If \(t_1=1\), then \(E_1=9/[X_1(X_1+1)]<E_0\) for every \(u\ge2\), as follows from the positive identities

\[
12X_1(X_1+1)-9X_0(X_0+3)=3q^2(u^2+8u+3)
\]

in the odd case and

\[
16X_1(X_1+1)-9X_0(X_0+4)=q^2(7u^2+32u+12)
\]

in the even case. If \(t_1\ge4\), then \(E_1\ge36/[X_1(X_1+9)]\) and \(E_0\le16/[X_0(X_0+4)]\). For \(u\ge3\),

\[
36X_0(X_0+4)-16X_1(X_1+9)=4q(25u^3-60u^2+12u-20)>0.
\]

Hence \(E_1>E_0\) in all other classes when \(u\ge3\).

**3. Exclusion of the second alternative for large parameters.** The parity of \(u\) implies \(t_2\ge2\) when \(u\) is even and \(t_2\ge1\) when \(u\) is odd. Thus

\[
E_2\ge\begin{cases}
28/[X_2(X_2+2)],&u\text{ even},\\
14/[X_2(X_2+1)],&u\text{ odd}.
\end{cases}
\]

The two exact comparison identities are

\[
28X_0(X_0+4)-16X_2(X_2+2)=4q^2(u-6)(3u+2),
\]

\[
14X_0(X_0+3)-12X_2(X_2+1)=2q^2(u^2-24u-21).
\]

Therefore \(E_2>E_0\) when \(u\) is even and \(u>6\), or when \(u\) is odd and \(u\ge25\). In particular the second alternative never maximizes for \(u\ge34\).

**4. Uniform exclusion of all later alternatives.** For every \(s\ge3\), comparison of the lower bound for \(E_s\) with the upper bound for \(E_0\) reduces to positivity of

\[
D_u(s)=(5s+4)u(qu+4)-16(u+s)[q(u+s)+5s+4].
\]

As a polynomial in \(s\), its quadratic coefficient is \(-80u-16\), so it is strictly concave. For \(u\ge34\) its values at the endpoints of \([3,u-1]\) are positive:

\[
D_u(3)=3(5u^3-164u^2-188u-112)>0,
\]

\[
D_u(u-1)=25u^4-345u^3+440u^2-228u+48>0.
\]

For the first inequality, write the cubic factor as \(u^2(5u-164)-188u-112\), which is positive and increasing from \(u=34\). For the second, write it as \(u^3(25u-345)+u(440u-228)+48\). Strict concavity means every interior value is at least the smaller endpoint value. Consequently \(E_s>E_0\) for \(3\le s\le u-1\) whenever \(u\ge34\). Parts 2–4 prove the asserted unique optimizer for all \(u\ge34\).

**5. The complete finite boundary.** For \(2\le u\le33\), exact integer-floor evaluation of every \(u\le a\le2u-1\), taking \(b=\max\{a,\lfloor qa/(5a-q)\rfloor+1\}\), is a finite exhaustive check. Aside from the greedy maximizer \(T_0(u)\), the nondefault outcomes for \(m=u-1\) are:

| \(m\) | All maximizing pairs |
|---|---|
| \(2\) | \((4,5)\) |
| \(3\) | \((5,9)\) |
| \(5\) | \((6,40),(8,15)\) |
| \(6\) | \((9,20)\) |
| \(11\) | \((13,81)\) |
| \(12\) | \((14,95)\) |
| \(16\) | \((19,110)\) |
| \(20\) | \((22,247)\) |
| \(21\) | \((23,271)\) |
| \(29\) | \((31,503)\) |
| \(30\) | \((32,537)\) |

Every other \(1\le m\le32\) has the unique greedy maximizing pair. `check.py` carries out the exhaustive rational comparisons, including equality detection. Combining the boundary with the infinite inequalities proves every case and the density statement. \(\square\)

## Verification

Run `python3 check.py` in a standard Python 3 environment; no nonstandard packages or external data are needed. The program enumerates all candidate first denominators for \(2\le u\le500\), using exact rational arithmetic, and checks the global optimizer formula, its unique tie, all finite-boundary cases, and algebraic comparison identities. It executed successfully with 125,249 candidate evaluations. The infinite result comes from the inequalities in the proof rather than from the finite checks.

## Relationship to prior work

Nathanson's 2022 preprint (published in 2023) gives a general finite algorithm for best two-term underapproximations and a full classification in the first-denominator-two and -three intervals; these supply the general finite-search context but not a single uniform formula for this unbounded rational ray. Chu's 2023 preprint (2024 journal article) proves greedy uniqueness when the divisibility threshold is at most three, and constructs failures at every larger threshold. Here the threshold is constantly four and the numerator is the least possible, but we classify **every denominator**, all maximizing pairs, the exact periodic failure classes, and the exceptional tie. The 2026 paper of Kovač and Tang concerns eventual greediness as the *number of terms* grows for a fixed rational target, not the present two-term classification along an infinite family of targets.

A published research record on the first-denominator-four harmonic interval concerns \(\theta\in(1/4,1/3]\), intersecting this family in only \(m=3\). Its available summary does not address the uniform ray; the full text was not accessible in this check. No search result proves absolute novelty, and no claim of independent audit is made.

## Limitations

The result is restricted to two terms and reduced fractions with numerator five and denominator congruent to one modulo five. It does not determine the optimum at larger term counts, and a wider harmonic-interval or an unindexed equivalent theorem remains a bibliographic possibility. The proof and verification do not rely on numerical asymptotic heuristics or external certification.

## References

1. H. V. Chu, *A Threshold for the Best Two-term Underapproximation by Egyptian Fractions*, arXiv:2306.12564, first submitted 19 June 2023, https://arxiv.org/abs/2306.12564.
2. M. B. Nathanson, *Underapproximation by Egyptian fractions*, arXiv:2202.00191, first submitted 1 February 2022, https://arxiv.org/abs/2202.00191.
3. V. Kovač and Q. Tang, *Eventually greedy best Egyptian underapproximations of rational numbers via optimal control*, arXiv:2607.28387, 30 July 2026, https://arxiv.org/abs/2607.28387.
