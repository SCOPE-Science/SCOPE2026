# Nonexistence of nearly free nine-degree conic–seven-line arrangements with simple intersections

## Finding

There is no nearly free reduced plane curve over \(\mathbb C\) which is the union of **one smooth conic and seven distinct lines** and whose singularities are exclusively ordinary nodes \(A_1\), tacnodes \(A_3\), and ordinary triple points \(D_4\).

This settles the one-conic/seven-line case of the previously open degree-nine existence problem for such nearly free conic–line arrangements. It does not assert nonexistence for degree-nine arrangements with two or more conics or for arrangements allowing other singularity types.

## Assumptions and scope

Write \(D=Q\cup L_1\cup\cdots\cup L_7\subset\mathbb P^2_{\mathbb C}\), with \(Q\) a smooth irreducible conic and the \(L_i\) pairwise distinct lines. Suppose every singular point of this *reduced union* is a transverse ordinary node, an ordinary tangency of exactly two smooth branches (a tacnode), or a transverse ordinary triple of three smooth branches. The assertion concerns nearly freeness in the standard sense: for a degree-nine equation \(f\) defining \(D\), the saturation quotient of its Jacobian ideal is nonzero and has graded components of dimension at most one. Write \(r=\operatorname{mdr}(f)\) for the minimal degree of a nonzero homogeneous Jacobian relation.

A triple point is either a meeting of three lines *off* the conic, or a meeting of the conic and exactly two lines, all transverse. A tacnode necessarily occurs between \(Q\) and one of the lines (distinct lines cannot be tangent). No higher multiple intersections are allowed.

## Proof

**1. Near-freeness fixes the Tjurina number.** The established minimal-Jacobian-relation bound for conic–line arrangements with exactly these singularity types is
\[
\operatorname{mdr}(f)\geq \frac23\deg(D)-2=4.
\]
For a nearly free degree-nine curve, the exponents \((d_1,d_2)\) satisfy \(d_1+d_2=9\), \(d_1\le d_2\), and \(d_1=\operatorname{mdr}(f)\). Therefore \(r=d_1=4\). The nearly-free Tjurina formula yields
\[
\tau(D)=(9-1)^2-r(9-r-1)-1=64-16-1=47.
\]
The bound, exponent formula and Tjurina characterization appear in Gałecka [1, Sections 3–4]; they apply because the allowed singularities are quasi-homogeneous.

**2. Bézout and local singularities.** Let \(n,t,s\) denote the numbers of nodes, tacnodes and ordinary triple points. There are \(\binom72=21\) pairwise line intersection contributions and \(2\cdot7=14\) conic–line contributions. Local intersection multiplicities are respectively \(1,2,3\); local Tjurina numbers are \(1,3,4\). Thus
\[
 n+2t+3s=35,\qquad n+3t+4s=47.
\]
Subtracting and eliminating gives
\[
 t+s=12,\qquad n=t-1.
\]
In particular, \(t\ge1\).

**3. A conic–line Hirzebruch bound limits tangencies.** For arrangements with \(k\) smooth conics and \(d\) lines and these singularities, Gałecka [1, Proposition 4.4] quotes the geometric inequality
\[
8k+n+\tfrac34s\ge d+\tfrac52t.
\]
Taking \(k=1\), \(d=7\), \(n=t-1\), \(s=12-t\) gives \(16+t/4\ge7+5t/2\), hence
\[
 t\le4.
\]

**4. The ordinary line triples are numerous.** Split \(s=u+v\), where \(u\) counts triples of lines off \(Q\), and \(v\) counts transverse triples comprising \(Q\) and two lines. Each of the \(t\) tacnodes involves a different tangent line to \(Q\); a smooth conic has a unique tangent at a point, and a line has at most one tangency to a conic. Hence exactly \(h=7-t\) lines are nontangent. At a transverse triple on \(Q\), both incident lines must be nontangent. Every nontangent line has only two intersections with \(Q\), counted with multiplicity; therefore \(2v\le2h\), or \(v\le7-t\). It follows that
\[
 u=(12-t)-v\ge (12-t)-(7-t)=5.
\]

**5. Hirzebruch's *strong* inequality for the seven-line subarrangement.** On forgetting \(Q\), the seven distinct lines have only double and triple intersections, with \(u\) triple points and
\[
 t_2^{\mathrm{lines}}=21-3u-v
\]
double points. The \(v\) points on \(Q\) are ordinary double intersections of the two corresponding lines. Hirzebruch's inequality [2, Section 6, equation (9)] for a complex arrangement of \(\ell\) lines with \(t_\ell=t_{\ell-1}=t_{\ell-2}=0\) gives, in the absence of points with multiplicity at least four,
\[
 t_2^{\mathrm{lines}}+\tfrac34t_3^{\mathrm{lines}}\ge\ell.
\]
For \(\ell=7\), this reads \(21-3u-v+\tfrac34u\ge7\), or
\[
 9u+4v\le56.
\]
But \(u+v=12-t\), \(u\ge5\), and \(t\le4\), so
\[
9u+4v=4(u+v)+5u=4(12-t)+5u\ge4\cdot8+25=57,
\]
a contradiction. Therefore the proposed nearly free arrangement does not exist. \(\square\)

## Verification

The argument is uniform over \(\mathbb C\) and is not an inference from finite-field sampling. The standalone standard-library program `verify_constraints.py` enumerates the bounded integer incidence possibilities using exact rational arithmetic, checking both quoted geometric inequalities, Bézout, the local Tjurina relation, and the conic incidence constraint. Run `python3 verify_constraints.py`; the expected line starts with `DEGREE9_ONE_CONIC_SEVEN_LINES_NO_NEARLY_FREE_PASS` and finishes with zero surviving integer cases. Its function is a reproducible arithmetic cross-check, not a proof of either external geometric inequality.

The two external inequalities have been checked against their primary textual statements: Gałecka's Proposition 4.4 [1] and Hirzebruch's **strong** line-arrangement inequality [2, equation (9)], whose nonconcurrency hypotheses are met because the seven-line arrangement has no intersection of multiplicity four or higher. The weaker inequality with coefficient \(1\) instead of \(3/4\) is insufficient for this contradiction.

## Relationship to prior work

Gałecka [1] initiated the near-freeness classification for these three local singularity types, established the syzygy and conic–line inequalities used here, and explicitly left total degrees eight and nine open. The nonexistence result above concerns the natural first nonlinear-component case within degree nine and uses a second, independent Hirzebruch inequality applied to the **line-only subarrangement**. It is not an existing theorem of [1] restated with different parameters.

Măcinic and Pokora [3] investigate plus-one generated arrangements with defect two, rather than the nearly-free (defect-one) condition. The constructions of Bannai, Kawana, Masuya and Tokunaga [4] show that one-conic/seven-line incidence arrangements can exist with different singularity counts, without contradicting the near-freeness obstruction. Pokora's 2026 degree-nine nearly-free example [5] admits ordinary quadruple singularities and therefore lies outside the exact \(A_1/A_3/D_4\) scope here.

## Limitations

The conclusion applies only to one smooth conic plus exactly seven distinct lines over \(\mathbb C\), with no other singularity types. It leaves the two-conic/five-line and three-conic/three-line degree-nine cases undecided, and does not address free curves or plus-one generated curves of greater defect. Priority could be affected by an earlier incidence inequality or unindexed classification equivalent to the combination used here. No claim of independent mathematical validation is made.

## References

[1] A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969 (first posted 2022-04-29), *Boletín de la Sociedad Matemática Mexicana* 28, article 67 (2022), DOI: 10.1007/s40590-022-00461-4. Primary text: https://link.springer.com/article/10.1007/s40590-022-00461-4 .

[2] F. Hirzebruch, *Singularities of Algebraic Surfaces and Characteristic Numbers*, MPI preprint 85-39 (1985), Section 6, inequality (9). Primary full text: https://archive.mpim-bonn.mpg.de/id/eprint/2262/1/preprint_1985_39.pdf .

[3] A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228 (2023); *Atti Accad. Naz. Lincei Rend. Lincei Mat. Appl.* 35 (2024), DOI: 10.4171/RLM/1044. https://arxiv.org/abs/2309.15228 .

[4] S. Bannai, R. Kawana, K. Masuya, and H. Tokunaga, *Zariski pairs of conic-line arrangements with a unique conic*, arXiv:2410.04969 (2024). https://arxiv.org/abs/2410.04969 .

[5] P. Pokora, *On the Numerical Terao Conjecture*, arXiv:2608.05662 (2026), Section 4. https://arxiv.org/abs/2608.05662 .
