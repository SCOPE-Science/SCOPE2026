# A universal two-cell bottleneck penalty in majority-lethal multicellular fragmentation

## Finding

**Theorem (three adjacent bottlenecks).** For every integer \(m\ge 3\), start with a parent organism consisting of exactly \(m\) infected and \(m\) healthy cells. Independently and uniformly sample which \(a\) of its \(2m\) cells enter the smaller daughter, with \(a\in\{1,2,3\}\); the other daughter receives the remaining \(2m-a\) cells. Immediately remove each daughter whose infected fraction is *strictly greater than* \(1/2\). No intervening growth, infection, background cell mortality, or size-dependent mortality occurs. Let \(I_a\) be the number of infected cells left across the surviving daughters, \(C_a\) the number of infected–healthy unordered cell pairs co-resident within surviving daughters, and \(N_a\) the number of surviving cells. Then

\[
\begin{aligned}
\mathbb E I_1&=\frac{m-1}{2},&
\mathbb E I_2&=\frac{3m^2-3m+2}{2(2m-1)},&
\mathbb E I_3&=\frac{2m^2-4m+3}{2(2m-1)},\\
\mathbb E C_1&=\frac{m(m-1)}2,&
\mathbb E C_2&=\frac{m(3m^2-7m+6)}{2(2m-1)},&
\mathbb E C_3&=\frac{m(2m^2-7m+9)}{2(2m-1)},\\
\mathbb E N_1&=m,&
\mathbb E N_2&=\frac{m(3m-1)}{2m-1},&
\mathbb E N_3&=m.
\end{aligned}
\]

Each of the three observables \(\mathbb E I_a\), \(\mathbb E C_a\), and \(\mathbb E I_a/\mathbb E N_a\) is **strictly largest** for the intermediate two-cell bottleneck \(a=2\). In fact its expected infected count and expected mixed-cell contact count both exceed their \(a=1\) and \(a=3\) counterparts, while \(\mathbb E I_1>\mathbb E I_3\) and \(\mathbb E C_1>\mathbb E C_3\). Among even parent sizes, six cells is the minimum allowing all three compared unordered splits. Thus the middle daughter size can be strictly worst for three immediate infection-persistence metrics, notwithstanding more extreme asymmetry.

For the smallest case \(m=3\), the three split types \(1+5\), \(2+4\), \(3+3\) have respective expected infected survivors \(1,2,9/10\), expected surviving within-daughter infected–healthy pairs \(3,18/5,9/5\), and ratios of expected infected to expected total survivors \(1/3,5/12,3/10\).

## Assumptions and scope

An infected cell is a binary infected unit, not a continuous parasite dose. The parent always contains precisely half infected cells. Uniform random sampling is without replacement. Offspring remain distinguishable by their specified sizes, except at \(a=m\), where either labeling produces the same totals. A daughter with infection fraction exactly \(1/2\) survives, and one above \(1/2\) dies as a whole. In this one-partition experiment, all other death, growth, infection, transmission and competition processes are switched off. \(C_a\) counts *potential* infected–healthy pairs, not actual transmissions. The ratio \(\mathbb E I_a/\mathbb E N_a\) is a ratio of expectations; it is not asserted to equal \(\mathbb E[I_a/N_a]\).

## Proof

Let \(J\) be the number of infected cells in the daughter of size \(a\). Hypergeometric sampling gives

\[
\Pr(J=j)=\frac{\binom mj\binom m{a-j}}{\binom{2m}a},\qquad 0\le j\le a.
\]

The small daughter has \(j\) infected and \(a-j\) healthy cells; the large daughter has \(m-j\) infected and \(m-a+j\) healthy cells. The small daughter survives if and only if \(2j\le a\), and the large one survives if and only if \(2j\ge a\). Hence for odd \(a\) precisely one daughter survives for every assignment. For even \(a\), both survive exactly when \(j=a/2\); otherwise precisely one survives. This parity rule is the structural cause of the two-cell anomaly.

For each sampled \(j\), the three surviving totals are

\[
\begin{aligned}
I_a(j)&=j\mathbf 1_{2j\le a}+(m-j)\mathbf 1_{2j\ge a},\\
C_a(j)&=j(a-j)\mathbf 1_{2j\le a}+(m-j)(m-a+j)\mathbf 1_{2j\ge a},\\
N_a(j)&=a\mathbf 1_{2j\le a}+(2m-a)\mathbf 1_{2j\ge a}.
\end{aligned}
\]

For \(a=1\), the two equiprobable cases \(j=0,1\) leave respectively the healthy singleton or the large mixed daughter. Their average totals give the first column of the theorem.

For \(a=2\), \(j=0,1,2\) has respective probabilities \((m-1)/(2(2m-1))\), \(m/(2m-1)\), \((m-1)/(2(2m-1))\). The surviving infected counts are \(0,m,m-2\); the surviving mixed-pair counts are \(0,(m-1)^2+1,m(m-2)\); and surviving cell counts are \(2,2m,2m-2\). Taking expectations gives the second column.

For \(a=3\), the probabilities of \(j=0,1,2,3\) are

\[
\frac{\binom m3}{\binom{2m}3},\quad
\frac{m\binom m2}{\binom{2m}3},\quad
\frac{m\binom m2}{\binom{2m}3},\quad
\frac{\binom m3}{\binom{2m}3}.
\]

The corresponding surviving infected counts are \(0,1,m-2,m-3\), mixed-pair counts are \(0,2,(m-2)(m-1),m(m-3)\), and surviving cell counts are \(3,3,2m-3,2m-3\). Their expectations simplify to the third column.

The strict infection-survivor inequalities follow from

\[
\mathbb E I_2-\mathbb E I_1=\frac{m^2+1}{2(2m-1)}>0,
\qquad \mathbb E I_1-\mathbb E I_3=\frac{m-2}{2(2m-1)}>0.
\]

The mixed-pair inequalities follow from

\[
\mathbb E C_2-\mathbb E C_1=\frac{m((m-2)^2+1)}{2(2m-1)}>0,
\quad \mathbb E C_1-\mathbb E C_3=\frac{2m(m-2)}{2m-1}>0.
\]

Finally, writing \(q_a=\mathbb E I_a/\mathbb E N_a\), direct division yields

\[
q_2-q_1=\frac{m+1}{2m(3m-1)}>0,
\qquad q_1-q_3=\frac{m-2}{2m(2m-1)}>0.
\]

All denominators are positive for \(m\ge3\). A parent of size less than six admits fewer than three distinct positive unordered daughter sizes, proving the claimed minimality. \(\square\)

## Verification

The accompanying standalone, standard-library-only `CHECK.py` computes exact hypergeometric expectations with rational arithmetic independently from the closed forms for every integer \(m\) from \(3\) through \(149\). It verifies the three formulas, strict inequalities and expected-survivor-normalized infection ratios at each case, as well as an independent explicit assignment enumeration at the six-cell minimum. The infinite-family conclusion follows from the displayed algebraic identities, not from finite enumeration.

Run `python CHECK.py` in a folder containing this result. Expected final output: `PASS: exact hypergeometric and assignment checks`.

## Relationship to prior work

Garcia-Casillas and Wagner (2026) provide the motivating random-partition multicellular infection model, including pathogen-load-dependent removal, direct-contact metrics, and simulation observations that extreme reproductive asymmetry can assist infection purging and isolation. Their results are population-level and multi-generation, and do not state the present all-even-size, one-event, three-adjacent-bottleneck formulas or strict comparison. The present theorem is a tightly scoped analytic result within their partitioning and lethal-load mechanisms, not a theorem about which strategy wins over generations.

Marguet and Smadi (2024; arXiv preprint 2023) analyze parasite loads divided between daughter *cells* using continuous-state branching and partition kernels, with long-run survival comparisons. Their population units, parasite state spaces and mortality event differ: they do not impose fixed-size, binary infected/healthy cell group splitting with majority-lethal daughter-organism removal. Classical hypergeometric sampling and parity arithmetic are used rather than claimed as newly discovered methods.

## Limitations

The result is conditional on a parent with exactly half infected cells and on the strict half-lethality rule; moving the threshold away from \(1/2\) or changing parental prevalence can remove the parity effect. Potential pairs \(C_a\) are not measured transmissions, and neither organism fitness nor competition at population scale is inferred. Other death processes and growth can reverse the one-step comparison. An exhaustive historical-priority claim is not made; related work using alternate terminology might have obtained an equivalent combinatorial identity.

## References

1. A. Garcia-Casillas and A. Wagner, “Single-cell bottlenecks in multicellular reproduction can hinder the spreading of infectious disease,” *Frontiers in Ecology and Evolution* 14, 1816826 (2026). https://doi.org/10.3389/fevo.2026.1816826 . Publisher's directly accessible full-text pages display 18 May 2026 on one DOI landing rendering and 19 May 2026 on the journal page; the earlier publicly displayed date is used for time-window categorization.
2. A. Marguet and C. Smadi, “Parasite infection in a cell population: role of the partitioning kernel,” *Journal of Mathematical Biology* 89, 14 (2024), first preprint 11 May 2023. https://arxiv.org/abs/2305.06962 ; https://doi.org/10.1007/s00285-024-02110-y .
