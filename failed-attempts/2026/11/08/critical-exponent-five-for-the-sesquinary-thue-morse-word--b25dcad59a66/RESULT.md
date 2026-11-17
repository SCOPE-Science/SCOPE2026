# Critical exponent five for the sesquinary Thue–Morse word

## Finding

The binary sequence \(x=(x_n)_{n\geq0}\), with \(x_n\) equal to the parity of the digit sum of the canonical base-\(3/2\) expansion of \(n\), has **critical exponent exactly \(5\)**. More precisely, for every integer period \(p\geq1\), no factor of \(x\) of length \(5p+1\) has period \(p\). Equality is attained: the length-\(15\) factor starting at position \(18\) is \({\tt 101101101101101}=({\tt 101})^5\).

This proves the critical-exponent conjecture attributed to Jeffrey Shallit in Dekking's 2023 paper (Conjecture 9 of the first preprint; Conjecture 10 of the journal version).

## Assumptions and scope

For each \(n\geq0\), let its canonical sesquinary expansion be the finite expression \(n=\sum_{i\geq0}d_i(3/2)^i\), where \(d_i\in\{0,1,2\}\) and leading zeroes are ignored. Define \(x_n=(\sum_i d_i)\bmod2\); set \(x_0=0\). All positions are zero-indexed. For a finite binary word of length \(L\), a positive integer \(p\leq L\) is a period if its symbols at positions \(j\) and \(j+p\) coincide whenever both positions lie in the word. Its exponent with respect to \(p\) is \(L/p\); critical exponent is the supremum of \(L/p\) over factors and their periods. For the empty set of periods the definition is inapplicable; throughout \(p\ge1\).

Dekking's digit recurrence, valid for all \(n\geq0\), is
\[
x_{3n}=x_{2n},\qquad x_{3n+1}=1-x_{2n},\qquad x_{3n+2}=x_{2n}.
\]
This follows directly from the sesquinary digit extraction identity: the least digit of \(3n+r\) is \(r\) and the remaining expansion is that of \(2n\), for \(r=0,1,2\). Define the auxiliary binary word \(y_n=x_{2n}\). Thus
\[
(x_{3n},x_{3n+1},x_{3n+2})=(y_n,1-y_n,y_n),
\]
and, by substituting even indices into the preceding recurrence,
\[
(y_{3n},y_{3n+1},y_{3n+2})=(y_{2n},y_{2n},1-y_{2n+1}).\tag{1}
\]
These identities, and not any finite enumeration, are the premises of the proof.

## Proof

**1. Two forbidden patterns for the auxiliary word.** The word \(y\) has no alternating factor of length \(4\): any four consecutive integers include two consecutive indices \(3n,3n+1\), and (1) gives \(y_{3n}=y_{3n+1}\).

The word \(y\) has no constant factor of length \(6\). Suppose six consecutive letters from index \(s\) all equal \(c\in\{0,1\}\). Write \(s=3n+r\). Applying (1) gives, according as \(r=0,1,2\), an alternating string of parent letters
\[
\begin{array}{c|c|c}
r&\text{parent indices}&\text{forced parent values}\\
0&2n,2n+1,2n+2,2n+3&c,1-c,c,1-c\\
1&2n,2n+1,2n+2,2n+3,2n+4&c,1-c,c,1-c,c\\
2&2n+1,2n+2,2n+3,2n+4&1-c,c,1-c,c.
\end{array}
\]
Each contradicts the preceding four-letter prohibition.

**2. A five-power-plus-one exclusion for \(y\).** Suppose, contrary to the claim, that a factor \(y_s\cdots y_{s+5p}\) has period \(p\ge1\). First suppose \(3\nmid p\). For each \(k\in[s,s+p-1]\), choose \(t\in\{0,1,2\}\) such that \(j=k+tp\equiv0\pmod3\). Both \(j\) and \(j+1\) lie in the assumed factor. Periodicity gives \(y_k=y_j\) and \(y_{k+1}=y_{j+1}\), while (1) gives \(y_j=y_{j+1}\). Thus \(y_k=y_{k+1}\) throughout the first \(p+1\) letters; period \(p\) makes the entire length-\(5p+1\) factor constant. As \(5p+1\ge6\), this is impossible.

Now suppose \(p=3q\) with \(q\ge1\). Define
\[
F(j)=2\lfloor j/3\rfloor+\mathbf1_{j\bmod3=2},\qquad E(j)=\mathbf1_{j\bmod3=2}.
\]
Equation (1) says \(y_j=y_{F(j)}\oplus E(j)\), where \(\oplus\) is addition modulo two. For every \(j\), \(F(j+p)=F(j)+2q\) and \(E(j+p)=E(j)\). The presumed period therefore implies \(y_{F(j)}=y_{F(j)+2q}\) for each \(s\le j\le s+4p\). The map \(F\) is nondecreasing and surjective onto each integer between the images of the endpoints, as its consecutive increments are \(0\) or \(1\). Moreover, \(F(s+4p)=F(s)+8q\). Consequently the factor of \(y\) of length \(10q+1=5(2q)+1\), starting at \(F(s)\), has period \(2q\). This is a strictly smaller positive period than \(p=3q\). Repeating the descent eventually reaches the preceding case \(3\nmid p\), a contradiction. Thus **no factor of \(y\) has length \(5p+1\) and period \(p\)**.

**3. A forbidden pattern for \(x\).** The word \(x\) has no alternating factor of length \(10\). Indeed, inside each triple \((y_n,1-y_n,y_n)\), adjacent letters alternate. At the boundary between triples, alternation would require \(y_n\ne y_{n+1}\). Any ten consecutive positions of \(x\) span at least three consecutive such boundaries, which would force four consecutive alternating letters of \(y\), impossible by step 1.

**4. A five-power-plus-one exclusion for \(x\).** Suppose a factor \(x_s\cdots x_{s+5p}\) has period \(p\ge1\). If \(p=3q\), use \(x_j=y_{\lfloor j/3\rfloor}\oplus \mathbf1_{j\bmod3=1}\). The floor map increases by \(q\) under \(j\mapsto j+p\) and is surjective onto the integer interval between the images of the endpoints. Comparing each index \(j\in[s,s+4p]\) with \(j+p\) shows that \(y\) has a factor of length \(5q+1\) with period \(q\), contradicting step 2.

If \(3\nmid p\), then for each \(k\in[s,s+p-1]\), choose \(t\in\{0,1\}\) so \(j=k+tp\equiv0\) or \(1\pmod3\). (For residue \(2\), adding \(p\) reaches either residue \(0\) or \(1\).) Hence \(x_j\ne x_{j+1}\) inside a triple, and periodicity gives \(x_k\ne x_{k+1}\). The first \(p+1\) letters therefore alternate, as does the entire assumed periodic factor. For \(p=1\) a periodic factor is constant, an immediate contradiction; for \(p\ge2\), the factor has length \(5p+1\ge11\) and violates step 3. Both cases are impossible.

**5. Sharpness.** Iterating (1) from \(y_0=0\) gives \(y_6=y_7=y_8=y_9=y_{10}=1\). Therefore the triple relation for \(x\) yields \(x_{18}\cdots x_{32}=({\tt101})^5\). We have excluded length \(5p+1\) with period \(p\) for every \(p\), hence excluded all exponents strictly greater than \(5\); the exhibited factor attains exponent \(5\). \(\square\)

## Verification

The standalone `checker.py` computes the digit-sum parity directly by repeated least-digit removal and independently by the recurrence; it compares the first \(100000\) positions, verifies both triple identities, checks the two auxiliary forbidden patterns and ten-letter alternating prohibition, and searches periods \(1\) through \(80\) in the available prefixes for the forbidden length-\(5p+1\) configuration. It confirms the explicit witness at indices \(18\) to \(32\). Its output is recorded in `checker-output.txt`. These finite tests corroborate the identities and witness; the proof of the universal exponent bound is the descent and residue argument above.

## Relationship to prior work

Dekking's *The Thue–Morse Sequence in Base 3/2*, first posted January 31, 2023 (arXiv:2301.13563v1; journal article 23.2.3), defines the sequence, proves the digit recurrence, and states the critical-exponent-\(5\) assertion as an unsolved conjecture attributed to Shallit. The sequence is OEIS A357448. Cassaigne, Espinoza, Rigo, and Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures* (arXiv:2602.21895v1, February 25, 2026), study a related normalized word and Dekking's word via a uniform morphism, proving uniform recurrence, factor symmetries, and symbol frequencies, but not the critical exponent. This result instead proves the original claimed critical exponent by a two-level descent on periods.

## Limitations

The theorem concerns the unique sesquinary expansions in Dekking's convention, not the distinct \(\frac12\cdot\frac32\) numeration convention. It determines the maximum repetition exponent but does not classify all maximal fifth powers, factor frequencies, or the full power spectrum. The historical comparison is not a guarantee against unindexed equivalent results. Independent external mathematical review has not been performed.

## References

1. F. M. Dekking, *The Thue–Morse Sequence in Base 3/2*, arXiv:2301.13563v1, posted 2023-01-31; *Journal of Integer Sequences* **26** (2023), Article 23.2.3. https://arxiv.org/abs/2301.13563 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Dekking/dek25.html
2. J. Cassaigne, B. Espinoza, M. Rigo, M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures*, arXiv:2602.21895v1, posted 2026-02-25. https://arxiv.org/abs/2602.21895
3. OEIS Foundation, A357448, the fixed point of the two-block substitution \({\tt00,01}\mapsto{\tt010}\), \({\tt10,11}\mapsto{\tt101}\). https://oeis.org/A357448
