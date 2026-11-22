# Exact gap-run spectrum of an odd-parameter affine-repunit triple

## Finding
For every odd integer \(a\ge3\), let
\[
S_a=\langle a,2a+2,4a+6\rangle
=\{ax+(2a+2)y+(4a+6)z:x,y,z\in\mathbb Z_{\ge0}\}.
\]
A *gap run of length* \(\ell\ge1\) is a maximal interval of \(\ell\) consecutive nonnegative integers outside \(S_a\). Let \(B_\ell(a)\) count such runs, and set \(m=(a-1)/2\).

All run lengths and their exact multiplicities are as follows:
\[
\boxed{B_{2(m-j)}(a)=\begin{cases}
2,&0\le j<m,\ j\not\equiv2\pmod3,\\
0,&0\le j<m,\ j\equiv2\pmod3,
\end{cases}}
\]
while every other length \(\ell\ge2\) has multiplicity zero. The number of one-element runs (the isolated gaps) is
\[
\boxed{B_1(a)=\begin{cases}
12k^2+3k,&m=3k,\\
12k^2+11k+3,&m=3k+1,\\
12k^2+19k+6,&m=3k+2.
\end{cases}}
\]
In particular, the longest gap run has length \(a-1\) and occurs exactly twice. The spectrum omits precisely the positive even lengths \(2(m-j)\) with \(j\equiv2\pmod3\), and all odd lengths exceeding one.

## Assumptions and scope
The parameter \(a\) is any odd integer at least three. The semigroup is numerical because \(\gcd(a,2a+2)=\gcd(a,2)=1\). The third displayed generator is redundant at \(a=3\) but not for \(a\ge5\). A maximal gap run is maximal in \(\mathbb Z_{\ge0}\), not just relative to an individual residue class. The zero integer lies in the semigroup and is not a gap. No assertion is made for even \(a\), for an arbitrary increment in the generator family, or for a fourth generator.

## Proof
**1. Exact Apéry thresholds.** For any representation
\[
n=ax+(2a+2)y+(4a+6)z=a(x+2y+4z)+2(y+3z),
\]
put \(t=y+3z\). For fixed \(t\ge0\), the minimum of \(2y+4z\) over nonnegative \(y,z\) with \(y+3z=t\) equals
\[
c(t)=2\left(t-\left\lfloor\frac t3\right\rfloor\right),
\]
attained at \(z=\lfloor t/3\rfloor\). Its increments \(c(t+1)-c(t)\) are two except when \(t\equiv2\pmod3\), when they are zero. In particular, \(c\) is nondecreasing.

Since \(a\) is odd, multiplication by two permutes residue classes modulo \(a\). For every residue \(r\) there is a unique \(t_r\in\{0,\ldots,a-1\}\) with \(2t_r\equiv r\pmod a\). Every admissible \(t\) for that class has the form \(t_r+ha\) with \(h\ge0\) (negative \(h\) would give \(t<0\)). By monotonicity of \(c\), the smallest element of \(S_a\) in that class is
\[
w(r)=a c(t_r)+2t_r.
\]
Thus, for \(q\ge0\) and \(0\le r<a\),
\[
qa+r\in S_a\quad\Longleftrightarrow\quad
q\ge H_r:=\left\lfloor\frac{w(r)}a\right\rfloor.
\tag{1}
\]
The least-element claim follows not only from the fixed-\(t\) minimization but also because increasing \(t\) by \(a\) raises \(2t\) and never lowers \(c(t)\).

**2. Row geometry.** Write \(a=2m+1\). The residues corresponding to \(t=0,\ldots,m\) are \(r=2t\), whereas those corresponding to \(t=m+1,\ldots,2m\) are \(r=2j+1\) with \(t=m+j+1\). Equation (1) therefore becomes
\[
H_{2j}=c(j)\quad(0\le j\le m),\qquad
H_{2j+1}=c(m+j+1)+1\quad(0\le j<m).
\tag{2}
\]
In any fixed row \([qa,(q+1)a-1]\), the represented even residues are an initial string \(0,2,\ldots,2E_q\), where \(E_q\) is the largest index \(j\le m\) with \(c(j)\le q\). The represented odd residues, when present, are likewise an initial string. Moreover, every represented odd residue has both neighboring even residues represented: its threshold is \(c(m+j+1)+1\), which exceeds both \(c(j)\) and \(c(j+1)\). Consequently no represented odd residue lies beyond the last represented even residue.

It follows that each row contains only singleton missing odd residues between represented even residues, plus (when \(E_q<m\)) a *single final gap interval* from residue \(2E_q+1\) through \(2m\), of even length \(2(m-E_q)\). No gap interval crosses from one row to the next, because each row starts at \(qa\in S_a\). Every non-singleton run is therefore one of these terminal intervals.

**3. Classification of longer runs.** Fix \(0\le j<m\). The equality \(E_q=j\) holds for exactly \(c(j+1)-c(j)\) nonnegative integer row indices \(q\), namely \(c(j)\le q<c(j+1)\). This difference is two when \(j\not\equiv2\pmod3\), and zero otherwise. The associated terminal gap has length \(2(m-j)\). These lengths are distinct as \(j\) varies. This proves the complete formula for \(B_\ell(a)\) with \(\ell\ge2\).

**4. Exact singleton count.** Equation (1) shows that the total number of gaps (the genus) is \(g(a)=\sum_{r=0}^{a-1}H_r\). Summing (2) yields
\[
g(a)=\sum_{t=1}^{2m}c(t)+m.
\]
The sum of the lengths of all terminal runs is
\[
\sum_{j=0}^{m-1}2(m-j)[c(j+1)-c(j)]
=2\sum_{j=1}^{m}c(j),
\]
by summation by parts and \(c(0)=0\). Every remaining gap is a singleton, so
\[
B_1(a)=\sum_{t=m+1}^{2m}c(t)-\sum_{t=1}^{m}c(t)+m
=2m^2+m-2\left(F(2m)-2F(m)\right),
\tag{3}
\]
where \(F(n)=\sum_{t=1}^n\lfloor t/3\rfloor\). For \(n=3u+v\), \(0\le v\le2\), direct grouping into blocks of three gives
\[
F(3u+v)=\frac{3u^2-u}{2}+uv.
\]
Substitute \(m=3k\), \(3k+1\), or \(3k+2\) into (3). The three displayed quadratic values follow. This exhausts all gaps and proves the result. \(\square\)

## Verification
The standalone `verify.py` checks the statement for every odd \(a\) from \(3\) through \(251\). For each value, it computes the Apéry set independently with shortest-path Dijkstra search on residue classes, then constructs the entire semigroup membership table through the conductor by additive dynamic programming, independently compares the two membership descriptions, enumerates every maximal missing-integer interval, and compares the full run histogram with the stated formulas. It also compares the sum of all run lengths with the genus. Running the included program produced:

```text
PASS: 125 complete odd-parameter tests; 1785903 gaps; 896931 maximal gap runs; last a=251
3 [(1, 3), (2, 2)]
5 [(1, 6), (2, 2), (4, 2)]
7 [(1, 15), (4, 2), (6, 2)]
11 [(1, 37), (2, 2), (4, 2), (8, 2), (10, 2)]
17 [(1, 92), (2, 2), (4, 2), (8, 2), (10, 2), (14, 2), (16, 2)]
```
These finite checks corroborate the result but are not the proof of the infinite-parameter theorem.

## Relationship to prior work
Liu, Xin, Ye and Yin (2023, arXiv:2306.03459 and 2306.10738) treat the entire generalized affine-repunit family containing \(\langle a,2a+2,4a+6\rangle\) and give Apéry, Frobenius and genus methods. Their full mathematical descriptions determine individual membership thresholds and thus imply that a run census is algorithmically computable; these known contributions are credited and not claimed new. What is asserted here is the explicit, complete maximal-gap-run histogram with its zero-versus-two period-three longer-run law and period-three quadratic isolated-gap count. The proof extracts these from a sharp residue-row geometry not stated as a run classification in those papers.

The published result *Complete minimal presentations for three-term affine repunit numerical semigroups* (2026) treats the same generator form but its theorem concerns toric-ideal relations and Betti degrees, not missing-integer runs; it does not imply these multiplicities by its stated classification. The published result *Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)* (2026) evaluates a different two-generator family, not the present triple. The published *Exact isolated-gap box and digit distribution for unit-shift generalized repunit semigroups* (2026) treats a distinct unit-shift family, whereas the increment here is two. General literature on isolated gaps of two-generator semigroups does not directly supply the triple's complete run spectrum.

## Limitations
The formulas apply only for odd \(a\) and the specified triple. They do not determine representation multiplicities, gaps of larger generator families, or the corresponding distribution when \(a\) is even. Previous Apéry-set theorems encode membership for this family, so an independently published equivalent evaluation of the resulting gap-run census is a residual priority risk, particularly if embedded in an unindexed work. The theorem is a complete evaluation of a natural finite invariant, not a claim that this semigroup family or its Apéry thresholds were previously unknown. The finite checker supplements rather than substitutes for the proof. No independent external audit has been performed.

## References
1. F. Liu, G. Xin, S. Ye and J. Yin, *A Combinatorial Model of Numerical Semigroup*, arXiv:2306.03459, first public version 2023-06-06. https://arxiv.org/abs/2306.03459
2. F. Liu, G. Xin, S. Ye and J. Yin, *A Note on Generalized Repunit Numerical Semigroups*, arXiv:2306.10738, first public version 2023-06-19. https://arxiv.org/abs/2306.10738
3. M. B. Branco, I. Colaço and I. Ojeda, *The Frobenius problem for generalized repunit numerical semigroups*, arXiv:2112.01106. https://arxiv.org/abs/2112.01106
4. S. N. Singh and R. K. Ram, *On Isolated Gaps of Numerical Semigroups of embedding dimension two*, arXiv:2406.09848. https://arxiv.org/abs/2406.09848
5. *Complete minimal presentations for three-term affine repunit numerical semigroups*, online mathematical result, 2026-10-18.
6. *Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)*, online mathematical result, 2026-11-02.
7. *Exact isolated-gap box and digit distribution for unit-shift generalized repunit semigroups*, online mathematical result, 2026-11-02.
