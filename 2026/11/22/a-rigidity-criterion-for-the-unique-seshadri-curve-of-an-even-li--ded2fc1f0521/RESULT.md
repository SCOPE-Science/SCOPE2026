# A rigidity criterion for the unique Seshadri curve of an even line arrangement

## Finding

**Theorem (ordinary-double transversal rigidity).** Let \(k\) be an algebraically closed field of arbitrary characteristic, \(m\ge2\), and \(\mathcal A=\{L_1,\ldots,L_{2m}\}\) an arrangement of \(2m\) pairwise distinct lines in \(\mathbb P^2_k\). Let \(Z\) be its reduced set of points incident to at least two arrangement lines and let \(\ell=\max_i\#(L_i\cap Z)\). Suppose:

1. \(\ell<m\).
2. There is a line \(M\notin\mathcal A\) containing \(m\) **distinct ordinary double points** of \(\mathcal A\), i.e. each lies on exactly two lines of \(\mathcal A\).
3. There are two distinct arrangement lines \(L_a,L_b\) each containing exactly one ordinary double point of \(\mathcal A\), and their respective double points \(P_a,P_b\) are distinct.

Then \(P_a,P_b\in M\), the multipoint Seshadri constant satisfies

\[
\varepsilon(\mathbb P^2_k,\mathcal O(1);Z)=\frac1m,
\]

and **\(M\) is the unique integral plane curve, of any degree, attaining this infimum**. If \(\pi:Y=\operatorname{Bl}_Z\mathbb P^2_k\to\mathbb P^2_k\), \(H=\pi^*\mathcal O(1)\), and \(E_P\) are its exceptional curves, then the integral divisor

\[
D=mH-\sum_{P\in Z}E_P
\]

is nef and its **entire null locus** (the union of integral curves \(C\) such that \(D\cdot C=0\)) is precisely the strict transform \(\widetilde M\). In particular \(\widetilde M^2=1-m\).

**Explicit application.** For the sixteen lines over \(\overline{\mathbb F}_7\) of Dumnicki–Farnik–Hanumanthu–Harbourne–Pokora–Roé–Tutaj-Gasińska, arXiv:2611.03797v1, §6.1, the line \(M:x+6y+6z=0\) is the unique Seshadri curve for the full set of \(38\) singular points. On their blow-up the divisor

\[
D=8H-\sum_{P\in Z}E_P
\]

is big and nef, with \(D^2=26\) and sole null curve \(\widetilde M\), which has self-intersection \(-7\). This identifies **every** zero-intersection curve on this high-Picard-rank blow-up, not only the value of the local positivity threshold.

## Assumptions and scope

All curves are reduced and irreducible when computing the Seshadri constant; geometric points and all assertions are over an algebraically closed base field. An ordinary double point here means exactly two distinct arrangement lines meet, regardless of the characteristic. No generic-position assumptions are imposed beyond the three explicit conditions. The theorem is conditional: it does not assert the existence of such arrangements for every \(m\).

For the explicit example work over \(k=\overline{\mathbb F}_7\) and use the following labelled linear forms, coefficients read modulo \(7\):

\[
\begin{array}{rrrr}
L_1:y+2z,&L_2:y+3z,&L_3:y+5z,&L_4:x,\\
L_5:x+z,&L_6:x+3z,&L_7:x+y+z,&L_8:x+y+6z,\\
L_9:x+2y+3z,&L_{10}:x+3y+4z,&L_{11}:x+4y+z,&L_{12}:x+4y+5z,\\
L_{13}:x+5y+z,&L_{14}:x+5y+6z,&L_{15}:x+6y+z,&L_{16}:x+6y+2z.
\end{array}
\]

There are \(38\) intersections, with point-multiplicity distribution \((t_2,t_3,t_4,t_5)=(16,12,8,2)\). Fourteen lines have seven singular points and two have six. The line \(M\) passes through eight ordinary double points. The four lines with just one ordinary double point are

\[
\begin{array}{c|c|c}
\text{line}&\text{sole ordinary double point}&\text{other line there}\\\hline
L_1&(1:2:6)&L_5\\
L_3&(1:3:5)&L_{13}\\
L_{10}&(1:5:3)&L_2\\
L_{15}&(1:1:0)&L_{16}
\end{array}
\]

and these four distinct points all lie on \(M\). Hence \(m=8\), \(\ell=7\), and any two of these four lines verify the criterion.

## Proof

**1. Saturation of the transversal.** Each of the \(m\) distinct ordinary double points of \(\mathcal A\) on \(M\) accounts for two intersections of \(M\) with distinct arrangement lines. An arrangement line different from \(M\) meets it in only one point. Thus the \(m\) double points use all \(2m\) arrangement lines, exactly once. No further point of \(Z\) lies on \(M\), and each arrangement line has its unique intersection with \(M\) at one of these double points. In particular \(P_a,P_b\in M\).

**2. Lower bound.** If \(C\) is an integral plane curve of degree \(e\ge1\) different from every \(L_i\), then Bézout and the local intersection inequality with a smooth line give

\[
2me=\sum_{i=1}^{2m}(L_i\cdot C)
\ \ge\ \sum_{P\in Z}r_P\operatorname{mult}_P C
\ \ge\ 2\sum_{P\in Z}\operatorname{mult}_P C,
\]

where \(r_P\ge2\) is the number of arrangement lines through \(P\). Hence \(e/\sum_{P\in Z}\operatorname{mult}_P C\ge1/m\) whenever the denominator is nonzero. For an arrangement component \(C=L_i\), its ratio is \(1/\#(L_i\cap Z)\ge1/\ell>1/m\). On the other hand \(M\) meets exactly \(m\) points of \(Z\), each simply; its ratio is \(1/m\). Thus the constant is exactly \(1/m\).

**3. Uniqueness in all degrees.** Suppose an integral curve \(C\ne M\) attains \(1/m\). It cannot be an arrangement component because \(\ell<m\). Equality holds at both stages of the displayed Bézout chain. It forces \(\operatorname{mult}_P C=0\) at all points \(P\in Z\) with \(r_P>2\), and it forces **every intersection** of each \(L_i\) with \(C\) to occur at ordinary double points, with local intersection multiplicity exactly \(\operatorname{mult}_P C\). Since \(L_a\) has only the one ordinary double point \(P_a\),

\[
e=L_a\cdot C=\operatorname{mult}_{P_a} C.
\]

Likewise \(e=\operatorname{mult}_{P_b}C\). The two points are distinct and lie on \(M\), which is a different line from \(C\), so another application of Bézout gives

\[
e=M\cdot C\ge\operatorname{mult}_{P_a}C+
\operatorname{mult}_{P_b}C=2e,
\]

an impossibility. Consequently \(M\) is the only integral curve attaining the Seshadri constant. This argument covers arbitrary degrees, singular competitors, and arbitrary field characteristic.

**4. Nef boundary.** On \(Y\), every exceptional curve \(E_P\) has \(D\cdot E_P=1\). Every other integral curve is a strict transform \(\widetilde C\) of an integral plane curve \(C\), and

\[
D\cdot\widetilde C=m\deg C-\sum_{P\in Z}\operatorname{mult}_P C\ge0.
\]

Equality occurs exactly for \(C=M\) by step 3. Thus \(D\) is nef and its null locus has precisely the one integral component \(\widetilde M\). Since \(M\) passes simply through exactly \(m\) blown-up points, \(\widetilde M^2=1-m\).

**5. Explicit instance.** The exact intersection enumeration in `checker.py` gives the assertions under “Assumptions and scope.” The full set \(Z\) consists of intersections of two lines defined over \(\mathbb F_7\), hence every geometric intersection is \(\mathbb F_7\)-rational. The criterion applies with \(m=8\). Finally, \(D^2=8^2-38=26>0\); a nef surface divisor of positive square is big. The strict transform of \(M\) has square \(1-8=-7\).

## Verification

Run `python3 checker.py` using Python 3 standard-library arithmetic only. The script constructs all \(\binom{16}{2}\) line-pair intersections projectively over \(\mathbb F_7\), deduplicates them, recomputes point multiplicities, all sixteen per-line counts, the eight points of \(M\), and the single-double-point condition for \(L_1,L_3,L_{10},L_{15}\). It also enumerates the \(57\) rational lines and verifies that \(M\) alone contains eight singular points (two rational points determine any line containing two of the rational marked points). This last finite enumeration is supplemental, not the proof of uniqueness among curves of arbitrary degree. The general rigidity criterion is proved in steps 1–4, with no finite-experiment premise.

## Relationship to prior work

Dumnicki et al. (2026), arXiv:2611.03797v1, §§1–2 and 6, establish the line-arrangement problem, the covering inequality, and the explicit sixteen-line characteristic-seven counterexample; §6.1 exhibits the eight-point transversal \(M\) as a witness for a strict improvement on the arrangement-line ratio. Their result does not state a general **unique-curve criterion** or identify all null curves of the corresponding blow-up nef divisor. The present theorem changes the object of determination from the numerical upper bound (or even the sharp numerical constant) to all equality-attaining integral curves in arbitrary degrees, and proves the conditional criterion for arbitrary even line arrangements.

Janasz–Pokora (2020) study configuration Seshadri constants over \(\mathbb C\) and distinguish numerical configuration bounds from actual computing curves. Their examples and invariants do not yield this positive-characteristic sixteen-line rigidity or the general two-leaf transversal criterion. Jacob (2026) gives a general relation between uniqueness and differentiability of one-point Seshadri functions on complex surfaces, but does not treat this positive-characteristic multipoint configuration, its null locus, or the incidence criterion.

This is a short structural deduction using elementary intersection theory; it does **not** claim that the underlying sixteen-line arrangement or its eight-point transversal was discovered here. The point is the universal equality-classification principle and its concrete extremal nef face.

## Limitations

The conditional criterion supplies sufficient, not necessary, hypotheses for uniqueness. It does not classify all even line arrangements admitting such a transversal, nor all nef classes on the blow-up. The single-null-curve assertion is about the specified divisor \(D\); it does not assert semi-ampleness, contractibility by a morphism, or complete knowledge of the nef cone. The characteristic-seven data are specific to the displayed sixteen-line arrangement. All originality comparisons are best-knowledge comparisons with the cited accessible sources; they are not a uniqueness guarantee against unindexed literature. Independent mathematical validation has not been performed.

## References

1. M. Dumnicki, Ł. Farnik, K. Hanumanthu, B. Harbourne, P. Pokora, J. Roé, H. Tutaj-Gasińska, *Seshadri constants of singular loci of line arrangements with at most twelve lines*, arXiv:2611.03797v1, submitted 2 November 2026, particularly §§2 and 6. https://arxiv.org/html/2611.03797v1
2. M. Janasz and P. Pokora, *On Seshadri constants and point-curve configurations*, Electronic Research Archive 28 (2020), 795–805, doi:10.3934/era.2020040. https://www.aimspress.com/article/doi/10.3934/era.2020040
3. C. J. Jacob, *Seshadri functions on surfaces*, arXiv:2611.01138v1, submitted 31 October 2026, particularly §§1–2. https://arxiv.org/html/2611.01138v1
