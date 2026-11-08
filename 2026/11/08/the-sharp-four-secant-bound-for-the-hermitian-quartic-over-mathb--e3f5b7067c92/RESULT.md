# The sharp four-secant bound for the Hermitian quartic over \(\mathbb F_{729}\)

## Finding

Let \(K=\mathbb F_{3^6}\) and let \(H\subset\mathbb P^2_K\) be the geometrically smooth Hermitian plane quartic
\[
H:\quad X^4+Y^4+Z^4=0.
\]
Its rational-point set \(\Omega=H(K)\) has \(892\) points. A *four-secant* is a projective \(K\)-line containing four **distinct** points of \(\Omega\). For a point \(P\in\mathbb P^2(K)\), define \(s(P)\) to be the number of four-secants through \(P\).

**Theorem.** The curve has precisely \(39{,}879\) rational four-secants. Every external point \(P\notin\Omega\) satisfies \(25\leq s(P)\leq222\); both bounds are sharp. The complete distribution on the \(531{,}279\) external points is:

| Four-secants through an external point | Number of external points |
|---:|---:|
| 25 | 1,512 |
| 48 | 36,288 |
| 49 | 60,480 |
| 50 | 36,288 |
| 51 | 12,096 |
| 52 | 36,288 |
| 53 | 18,144 |
| 54 | 67,032 |
| 55 | 12,096 |
| 56 | 72,576 |
| 57 | 36,288 |
| 58 | 48,384 |
| 59 | 54,432 |
| 61 | 12,096 |
| 62 | 9,072 |
| 65 | 18,144 |
| 222 | 63 |


In particular, \(\Omega\) is a **complete \((892,4)\)-arc** in \(\operatorname{PG}(2,729)\), with the stronger uniform assertion that every point outside it belongs to at least \(25\) four-secants. The maximum \(s(P)=222\) occurs if and only if
\[
P\in\mathbb P^2(\mathbb F_9)\setminus H(\mathbb F_9),
\]
which consists of exactly \(63\) points. The minimum \(s(P)=25\) occurs at exactly \(1{,}512\) points.

The complete line-character distribution, where a character is \(\#(L(K)\cap\Omega)\), is
\[
\begin{array}{c|rrrr}
\text{character}&0&1&2&4\\\hline
\text{number of lines}&158760&175420&158112&39879
\end{array}.
\]
For reference, rational curve points on \(H(\mathbb F_9)\) lie on \(297\) four-secants each (\(28\) points), and the other \(864\) curve points lie on \(175\) each. These on-curve values are recorded only as consistency checks; the latter count is already implied by earlier work.

## Assumptions and scope

All fields, projective points, lines, tangent/intersection statements and incidence counts are over \(K=\mathbb F_{729}\), except for the explicitly specified subplane \(\mathbb P^2(\mathbb F_9)\). The quartic is a standard diagonal Hermitian form for \(q=3\), projectively equivalent over \(\mathbb F_9\) to the standard affine equation \(X^{q+1}=Y^q+Y\). The geometric smoothness of the diagonal quartic follows because in characteristic three its three partial derivatives are \(X^3,Y^3,Z^3\); these cannot vanish simultaneously at a projective point. The curve therefore has no line component, and every line meets it in at most four distinct geometric points.

The theorem is specific to this \(q=3,r=3\) Hermitian instance. It does not assert a uniform lower bound for other parameters or any completeness statement for arbitrary quartics.

## Proof

The proof reduces a finite, exactly specified projective incidence problem to two independently implemented exhaustive counts. Each standalone program includes complete field operations, point/line enumerators, the central incidence calculation, independent cross-checks, and assertions of the displayed integers. The following steps explain why each enumeration is exhaustive and why its output implies every part of the theorem.

**1. Finite-field models.** The first program uses
\[
K_1=\mathbb F_3[t]/(t^6+t+2),
\]
and the second uses
\[
K_2=\mathbb F_3[u]/(u^6+u^5+2).
\]
Both build all \(729\times729\) addition/multiplication tables from coefficient arithmetic modulo three and polynomial reduction. Each checks an inverse for every nonzero residue and the identity \(a^{729}=a\), thereby checking that its quotient is a field of order \(729\). The two implementations use different irreducible defining polynomials and different projective-coordinate normalizations; finite fields of order \(729\) are isomorphic, so they represent the same intrinsic incidence problem.

**2. Projective normal forms.** Every point of \(\mathbb P^2(K)\) has exactly one representative of the form \((1:a:b)\), \((0:1:b)\), or \((0:0:1)\) for \(a,b\in K\). Thus there are exactly
\[
729^2+729+1=532171
\]
rational points and equally many rational lines, by duality. In the second implementation the normal forms are \((a:b:1)\), \((a:1:0)\), and \((1:0:0)\). Direct evaluation of \(X^4+Y^4+Z^4\) on all projective representatives yields exactly \(892\) rational points of \(H\) in both field models, agreeing with the standard Hermitian point count \(q^6+1+q^5-q^4\) at \(q=3\).

**3. Direct line-first check.** For each of all \(532171\) normalized dual triples \((A:B:C)\), the independent verifier evaluates \(AX+BY+CZ\) at every one of the \(892\) rational curve points. The line counts for intersection cardinalities \(0,1,2,4\) are exactly \(158760,175420,158112,39879\); no other cardinality occurs. Hence there are \(39879\) four-secants.

**4. Independently reconstructed four-secants.** The other verifier takes all \(\binom{892}{2}\) unordered pairs of distinct curve points, constructs each joining line by the homogeneous cross product, and normalizes its dual coordinates. A line through \(j\) curve points is produced exactly \(\binom{j}{2}\) times. The resulting pair-frequency census is \(334180\) lines of frequency \(0\), \(158112\) of frequency \(1\), and \(39879\) of frequency \(6\); no other positive frequency occurs. Thus a line with frequency six has exactly four points of the curve. The verifier additionally evaluates every such line on all curve points to check it contains exactly four distinct points, independently of the combinatorial frequency interpretation.

**5. Incidence at every point.** In each implementation, all \(730\) rational points on each of the \(39879\) distinct four-secants are generated by explicit linear parametrization and independently normalized. Each such point increments its \(s(P)\). By the uniqueness of the rational projective normal forms, this computes \(s(P)\) for **every** point in \(\mathbb P^2(K)\), with no sampling. The two programs obtain the identical full external histogram stated above. In particular, its smallest and largest positive labels are \(25\) and \(222\), with multiplicities \(1512\) and \(63\). All \(531279=532171-892\) external points are represented in this table. Therefore no external point has \(s(P)=0\), proving completeness, and the bounds are attained.

**6. Extremal subplane.** The independent verifier identifies the \(\mathbb F_9\)-subplane by requiring the normalized homogeneous coordinates to be fixed by the ninth-power Frobenius. It finds its expected \(91\) points, of which \(28\) lie on \(H\). It verifies that each of the other \(63\) has multiplicity \(222\) and that every external point of multiplicity \(222\) is fixed by the same Frobenius. This proves the asserted if-and-only-if characterization.

The total line–point incidence count supplies another independent checksum:
\[
\sum_{P\in\mathbb P^2(K)}s(P)=39879\cdot730=29111670.
\]
The \(892\) on-curve points contribute \(28\cdot297+864\cdot175=159516=4\cdot39879\). The external histogram contributes the remaining \(28952154\), exactly as required. Since the two programs enumerate all finite objects and check the claimed tables, the computational steps constitute a finite exhaustive proof, not a statistical experiment.

## Verification

The two independent public verifiers are `verify_hermitian_q3r3.cpp` (point-pair-first, quotient \(t^6+t+2\)) and `verify_hermitian_q3r3_independent.cpp` (line-first, quotient \(u^6+u^5+2\)). Both require only a C++17 compiler and standard library. From their containing directory, run:

```sh
g++ -O3 -std=c++17 -Wall -Wextra verify_hermitian_q3r3.cpp -o check_pairs
./check_pairs
g++ -O3 -std=c++17 -Wall -Wextra verify_hermitian_q3r3_independent.cpp -o check_lines
./check_lines
```

Expected terminal lines are `HERMITIAN_Q3_R3_EXHAUSTIVE_PASS` and `HERMITIAN_Q3_R3_INDEPENDENT_PASS`. Both were observed in complete local executions. In addition to the two exact histograms, the programs assert finite-field inversion/Frobenius properties, exact rational curve count, exact four-secant count, incidence sums, and the maximum-multiplicity subplane identity. The line-first program verifies all \(532171\) lines directly, not just those containing a chosen pair of curve points.

## Relationship to prior work

Korchmáros, Nagy, and Szőnyi [1] formulated and studied this Hermitian-arc completeness problem. Their Theorem 7.2 gives completeness for \(r>3\), while their introduction explicitly leaves \(r=3\) open. Their Section 8.1 also derives the four-secant count through a **curve** point outside the base-field subplane; this antecedent is not claimed as new here. In particular, their results do not give the present exact distribution on **external** points at \(q=3,r=3\).

Bartoli and Timpanella [2] subsequently establish completeness for \(r=3\) when the base parameter \(q\) is sufficiently large, by using algebraic-variety estimates. Their published Theorem 3.8 does guarantee at least one full secant for a distinguished class \(A=0\) even at small \(q\), but the published main theorem does not establish coverage of all points at \(q=3\), nor the \(25\)-to-\(222\) distribution proved here. The present finite computation resolves the specific small odd-base case and quantifies redundancy of four-secant coverage. No general large-\(q\) theorem is claimed.

## Limitations

This is an exact finite-field computation for one specified Hermitian quartic and extension field, not a symbolic theorem covering all prime powers. Its mathematical force rests on the exhaustiveness of projective normalization, correct finite-field arithmetic, and reproducible enumeration. Two algorithmically distinct programs with distinct field models were executed and agreed, but this is **not** independent human or formal-machine verification. Historical priority is subject to possible older unindexed finite-geometry incidence tables or alternative expressions that imply the same distribution. Only the external-point incidence classification, sharp threshold, and maximum locus are treated as the new contribution; established curve-point results are cited as context.

## References

[1] G. Korchmáros, G. P. Nagy, and T. Szőnyi, *Algebraic approach to the completeness problem for \((k,n)\)-arcs in planes over finite fields*, Journal of Combinatorial Theory, Series A **204** (2024), 105851; publicly available preprint arXiv:2302.10162v1 (20 February 2023), https://arxiv.org/abs/2302.10162.

[2] D. Bartoli and M. Timpanella, *Complete \((k,q+1)\)-arcs in \(\operatorname{PG}(2,\mathbb F_{q^6})\) from the Hermitian curve*, Journal of Algebraic Combinatorics **62** (2025), article 21, published 2 September 2025; DOI 10.1007/s10801-025-01456-w, https://doi.org/10.1007/s10801-025-01456-w.
