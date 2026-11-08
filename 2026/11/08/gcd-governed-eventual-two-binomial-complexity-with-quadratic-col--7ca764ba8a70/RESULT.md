# Gcd-governed eventual two-binomial complexity with quadratic collision delays

## Finding

For every pair of positive integers \(a,b\), put \(p=a+b\), \(g=\gcd(a,b)\), and let \(X=(0^a1^b)^\omega\). Define \(B_{a,b}(n)\) to be the number of equivalence classes of its distinct length-\(n\) contiguous factors under **two-binomial equivalence**, meaning equality of the numbers of scattered occurrences of every binary pattern of length at most two. Then, for every integer \(m\ge 1+\binom{p-1}{2}\) and every \(0\le r<p\),

\[
B_{a,b}(mp+r)=\begin{cases}
p-g+1,&r=0,\\
p,&1\le r<p.
\end{cases}
\]

The period \(p\) is the least period of \(X\), so \(p\) is its ordinary factor complexity for each \(n\ge p\). Thus two-binomial equivalence eventually separates *every* pair of distinct factor phases except at multiples of \(p\), where exactly \(g-1\) identifications persist.

The quadratic dependence on \(p\) in a uniform stabilization bound cannot be replaced by a subquadratic bound measured in complete periods: for every \(h\ge1\), let
\[
a=2h+1,\quad b=2h+3,\quad m=h(h+2),\quad r=2h+2.
\]
There are two distinct length-\(mp+r\) factors of \(X\) that remain two-binomially equivalent. Here \(p=4h+4\), so \(m=p^2/16-1\). Because \(r\ne0\), the eventual value at that residue is \(p\), while at this length the value is at most \(p-1\).

## Assumptions and scope

The alphabet is ordered as \(0<1\), the exponents \(a,b\) are arbitrary **positive** integers, and length \(n=mp+r\) uses \(m\) complete periods and the proper-residue tail \(r\). A scattered occurrence is determined by increasing source indices. For a word \(w\), let \(c(w)=|w|_1\) and \(q(w)=\binom{w}{01}\) denote its number of ones and its number of scattered `01` pairs. For equal-length binary words, two-binomial equivalence is precisely equality of \((c(w),q(w))\): the other pattern counts are \(\binom{|w|-c(w)}2\), \(\binom{c(w)}2\), and \(c(w)(|w|-c(w))-q(w)\).

The theorem concerns sufficiently long factors, not all short lengths; the displayed quadratic cutoff is sufficient but is not claimed to be the least possible for each \(a,b\). The explicit family is a lower bound on *universal* stabilization, not a formula for the exact stabilization threshold.

## Proof

**1. Phase decomposition.** Set \(P=0^a1^b\). For each starting phase \(s\in\{0,\dots,p-1\}\), let \(U_s\) be the length-\(p\) cyclic shift of \(P\) starting at phase \(s\), and let \(T_{s,r}\) be its prefix of length \(r\). The length-\(mp+r\) factor at phase \(s\) is \(U_s^m T_{s,r}\). Each \(U_s\) has \(a\) zeros and \(b\) ones. Counting scattered `01` pairs within and between the concatenated blocks gives exactly
\[
 c(U_s^mT_{s,r})=mb+c(T_{s,r}),
\]
\[
 q(U_s^mT_{s,r})=m q(U_s)+\binom m2 ab+ma\,c(T_{s,r})+q(T_{s,r}).\tag{1}
\]
Hence two phases can collide only when their tail one-counts agree. Conditional on that agreement, their `01` counts differ by
\[
 m\bigl(q(U_s)-q(U_t)\bigr)+q(T_{s,r})-q(T_{t,r}).\tag{2}
\]
Since \(0\le q(T_{s,r})\le\binom r2\), the absolute tail difference is at most \(\binom r2\le\binom{p-1}2\). For the indicated \(m\), equation (2) cannot vanish if \(q(U_s)\ne q(U_t)\).

**2. Full-period phases and arithmetic coincidences.** For \(0\le s<a\),
\(U_s=0^{a-s}1^b0^s\), so \(q(U_s)=b(a-s)\), taking values \(b,2b,\ldots,ab\). For \(0\le j<b\), \(U_{a+j}=1^{b-j}0^a1^j\), so \(q(U_{a+j})=aj\), taking values \(0,a,\ldots,a(b-1)\). Their common values are precisely \(kab/g\) for \(1\le k<g\). It follows that exactly \(p-g+1\) distinct period-level `01` counts occur. When \(r=0\), every tail is empty; (1) then proves the claimed count for *every* \(m\ge1\).

**3. No persistent nonzero-residue collision.** Suppose two different phases have equal \(q(U_s)\). By the strictly monotone values on each of the two phase branches, they must come from opposite branches, so their rotations have the form
\[
 U=0^u1^b0^{a-u},\qquad V=1^{b-v}0^a1^v,
\]
where \(0<u<a\), \(0<v<b\), and \(ub=av\). Their prefix-one-count functions for \(0\le r\le p\) are
\[
 f_U(r)=\min\bigl(b,\max(0,r-u)\bigr),
\]
\[
 f_V(r)=\min(r,b-v)+\max\bigl(0,r-(p-v)\bigr).
\]
On \(1\le r<p\), equality of these functions is possible only at
\(r_0=u+b-v\). To see this, \(V\) has its first \(b-v\) ones at the very beginning, while \(U\) has its \(b\) ones in one interval beginning at \(u\): the difference starts negative, crosses zero at \(r_0\) while \(f_V\) is on its middle plateau and \(f_U\) is increasing, remains positive thereafter, and returns to zero only at \(p\). Explicitly, at that only interior matching length,
\[
 T_{U,r_0}=0^u1^{b-v},\qquad T_{V,r_0}=1^{b-v}0^u.
\]
They have the same one-count but their `01` counts are respectively \(u(b-v)>0\) and \(0\). Thus even when full-period `01` counts coincide, the tails cannot produce equal two-binomial profiles for \(1\le r<p\).

Combining Steps 1--3, all \(p\) distinct phases have distinct two-binomial profiles for nonzero residues and the stated large \(m\). These phases are distinct factors because \(P\) is primitive: its circular word has exactly two symbol changes, whereas a nontrivial power of a nonconstant binary word has at least four. This establishes the formula.

**4. Quadratic-delay witnesses.** Put \(a=2h+1\), \(b=2h+3\), and select phases \(s=h+1\) and \(t=3h+2\). Their full-period words are
\[
 U=0^h1^{2h+3}0^{h+1},\qquad V=1^{h+2}0^{2h+1}1^{h+1}.
\]
For \(r=2h+2\), both tails have exactly \(h+2\) ones and are \(0^h1^{h+2}\) and \(1^{h+2}0^h\). Their full-period `01` counts are \(h(2h+3)\) and \((2h+1)(h+1)=h(2h+3)+1\); the tail `01` counts are \(h(h+2)\) and zero. Equation (2) vanishes at \(m=h(h+2)\), yielding distinct but two-binomially equivalent factors. Their common term \(ma\,c(T)\) cancels because the tail one-counts agree. Since \(p=4(h+1)\), this collision occurs at \(m=p^2/16-1\), proving the stated quadratic-order obstruction.

## Verification

The accompanying standalone Python checker `check_2binomial.py` computes all binary subsequence multiplicities of length at most two by direct position-pair enumeration and independently evaluates the phase expression (1). It reports:

- 1,176 direct complete-binomial-signature comparisons for small parameters and lengths;
- 7,488 direct-window versus phase-expression checks;
- 576 exact multiple-of-period count checks;
- 83,700 large-length residue checks for all \(1\le a,b\le30\) at three post-cutoff multipliers;
- 40 distinct quadratic-delay collisions in the explicit family.

All assertions passed. The infinite theorem rests on Steps 1--4, not on finite sampling. Running `python3 check_2binomial.py` from the extracted package repeats the comparisons.

## Relationship to prior work

Rigo, Stipulanti and Whiteland (2022) provide the guiding framework and emphasize reconstruction via binomial complexity, while Lejeune, Leroy and Rigo (2018) and Lü, Chen, Wen and Wu (2021) compute binomial complexities for aperiodic Thue--Morse families. Atanasiu, Poovanandran and Teh (2018) derive Parikh matrices for powers, an applicable general identity corresponding to part of (1). Vivion (2025) proves that the two-binomial and ordinary factor complexities agree for binary 1-balanced words and several other classes; this directly covers the subfamily with \(\min(a,b)=1\). If \(a,b\ge2\), the length-two factors `00` and `11` show that \(X\) is not 1-balanced; the inspected general sufficient criteria do not imply either the gcd deficit or the exhibited quadratic collision delays. None of these relevant inspected theorems directly gives the full two-run periodic classification. The present result is a special structural classification, not a claimed generalization of their broader morphic theorems. A general power-matrix formula alone does not classify collisions between all cyclic phase prefixes.

## Limitations

The stabilization bound need not be sharp for fixed parameters. The result does not classify every short-length value, nor does it treat alphabets larger than two, arbitrary periodic periods with more than two runs, or binomial order three and above. Bibliographic comparison is limited to inspected accessible sources and recorded search results; possible unindexed equivalent results remain a novelty risk. No independent audit is claimed.

## References

1. M. Rigo, M. Stipulanti, M. A. Whiteland, *Characterizations of families of morphisms and words via binomial complexities*, first public 2022-01-12, arXiv:2201.04603, https://arxiv.org/abs/2201.04603 (primary MSC 68R15).
2. X.-T. Lü, J. Chen, Z.-X. Wen, W. Wu, *On the 2-binomial complexity of the generalized Thue-Morse words*, first public 2021-12-10, arXiv:2112.05347, https://arxiv.org/abs/2112.05347.
3. M. Lejeune, J. Leroy, M. Rigo, *Computing the k-binomial complexity of the Thue--Morse word*, first public 2018-12-18, arXiv:1812.07330, https://arxiv.org/abs/1812.07330.
4. A. Atanasiu, G. Poovanandran, W. C. Teh, *Parikh matrices for powers of words*, first public 2018-08-13, arXiv:1808.04102, https://arxiv.org/abs/1808.04102.
5. L. Vivion, *New examples of words for which binomial complexities and subword complexity coincide*, arXiv preprint 2025, arXiv:2509.11172, https://arxiv.org/abs/2509.11172 (Theorem 1, overlapping balanced subfamily).
