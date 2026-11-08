# Rigidity of minimum-width plank coverings of rectangular square annuli

## Finding
Let \(Q=[-\tfrac12,\tfrac12]^2\) and let \(H=I_1\times I_2\subset\operatorname{int}Q\) be any closed, axis-parallel rectangle, with side lengths \(0<h_1,h_2<1\). A plank is a closed strip between distinct parallel lines; its width is the distance between the lines. For finite covers of \(Q\setminus\operatorname{int}H\), define \(W_*(H)\) as the infimum of total Euclidean plank width, and put \(S=2-h_1-h_2\).

**Exact cost and complete rigidity in the large-hole phase.**
\[
W_*(H)=\min\{1,S\}.
\]
If \(S<1\), every finite cover attaining this minimum consists exclusively of planks with normals parallel to a coordinate axis. For each \(j\in\{1,2\}\), the planks with normal \(e_j\) have total width exactly \(1-h_j\); their one-dimensional strips, restricted to \([-\tfrac12,\tfrac12]\), partition the two closed exterior intervals \([-\tfrac12,\tfrac12]\setminus\operatorname{int}I_j\), apart from endpoints and zero-length overlaps. Conversely, any finite such subdivision gives a minimizing cover. This describes all minimizers up to subdividing the four canonical exterior strips, for arbitrarily positioned interior rectangles.

The strict condition \(S<1\) is sharp for the **interval-partition classification**: at \(S=1\), both a single width-one coordinate plank covering all of \(Q\) and the four exterior strips attain the minimum, and at \(S>1\) the canonical exterior-strip cover is no longer minimizing. (No classification of all minimizers in these latter regimes is claimed.)

## Assumptions and scope
Dimension is exactly two, the outer body is a Euclidean unit square, the hole is an axis-parallel closed rectangle strictly contained in its interior, and coverings are finite families of positive-width *closed* planks. The removed set is \(\operatorname{int}H\), so its boundary remains to be covered. The formula is independent of the position of \(H\) within the square. No orientation restriction is imposed on competing planks.

## Proof
Set \(\delta_j=1-h_j>0\), so \(S=\delta_1+\delta_2\). For a proposed finite plank family \(P_i=\{x:|\langle n_i,x\rangle-s_i|\le w_i/2\}\), use unit normals \(n_i\), positive widths \(w_i\), and \(W=\sum_iw_i\). Put \(a_i=|n_{i1}|\), \(b_i=|n_{i2}|\), hence \(a_i^2+b_i^2=1\), and define the directional budget
\[
R_1=\sum_i\frac{w_i a_i}{a_i+b_i},\qquad R_2=\sum_i\frac{w_i b_i}{a_i+b_i},\qquad R_1+R_2=W.
\]

**Step 1: Bang-box obstruction.** For a parameter \(\lambda\ge1\), set
\[
X_1(\lambda)=\sum_i\frac{w_i a_i}{a_i^2+\lambda b_i^2},\qquad
X_2(\lambda)=\sum_i\frac{w_i\lambda b_i}{a_i^2+\lambda b_i^2}.
\]
If for either order of coordinates \(j,k\) one has \(X_j<\delta_j\) and \(X_k<1\), the planks cannot cover \(Q\setminus\operatorname{int}H\). Indeed, slightly enlarge the closed planks to open planks while preserving these strict inequalities. Add an open coordinate plank of width arbitrarily close to \(h_j\) containing \(\operatorname{int}H\); its Bang-box contribution is its own width in coordinate \(j\). Bang's sign lemma (maximize the usual quadratic sign functional and flip one sign) then gives a point outside all these open planks among signed sums in the box of side lengths strictly less than one. This point lies in \(Q\setminus\operatorname{int}H\), a contradiction. This is the two-dimensional strict-margin version of the geometric reduction of Bakaev--Polyanskii [1, Lemmas 3--4]; it applies to closed planks because the inequalities have strict slack.

**Step 2: a strict two-coordinate budget lemma.** Fix one coordinate \(j\), writing its absolute normal coordinates as \(a\) and \(b\), with \(k\) the other coordinate; write \(X_j,X_k,R_j\) accordingly. For every \(\lambda>1\) and \(a,b\ge0\) with \(a^2+b^2=1\),
\[
\frac{(\lambda-1)a+\lambda b}{a^2+\lambda b^2}
\le1+(\lambda-1)\frac{a}{a+b}.
\tag{1}
\]
It is strict if \(a,b>0\). For \(a,b>0\), the left side as a function of \(\lambda\) is concave and lies below its tangent at \(1+a/b\), namely \((\lambda a+b)/(1+ab)\). Since \(1+ab-(a+b)=(1-a)(1-b)>0\), the tangent is strictly below \((\lambda a+b)/(a+b)\), proving the assertion. Both axial boundary cases follow by substitution. Multiplication by \(w_i\) and summation gives
\[
(\lambda-1)X_j(\lambda)+X_k(\lambda)
\le W+(\lambda-1)R_j,
\tag{2}
\]
strictly if at least one plank has both normal coordinates nonzero.

The continuous function \(X_k(\lambda)\) is nondecreasing in \(\lambda\ge1\) and \(X_k(1)\le W\). If \(X_k(\lambda)=W\) for some \(\lambda>1\), (2) yields \(X_j\le R_j\), strictly in the presence of an oblique normal. If it never reaches \(W\), then \(X_k(\lambda)<W\) for all \(\lambda\), and
\[
\lim_{\lambda\to\infty}X_j(\lambda)
=\sum_{i:b_i=0}w_i\le R_j,
\]
strictly if an oblique plank has \(a_i>0\). If \(X_k(1)=W\), all normals are parallel to \(e_k\), and \(X_j(1)=0=R_j\). Therefore, whenever \(W<1\) and \(R_j<\delta_j\), some finite \(\lambda\ge1\) satisfies the Bang-box obstruction. Whenever \(W<1\), \(R_j=\delta_j\), and an oblique plank exists, the same conclusion holds with strict inequality \(X_j<\delta_j\): choose \(\lambda>1\) in the crossing case or sufficiently large in the noncrossing case.

**Step 3: minimum cost.** Suppose a cover had \(W<\min\{1,S\}\). Since \(R_1+R_2=W<\delta_1+\delta_2\), some \(R_j<\delta_j\). Step 2 produces the strict Bang-box obstruction, contradicting Step 1. Hence \(W\ge\min\{1,S\}\). One coordinate plank of width one covers \(Q\), while four coordinate planks covering the four outer strips have total width \(S\). This proves the exact infimum and its attainment.

**Step 4: equality orientation rigidity.** Suppose \(S<1\) and a cover has \(W=S\). Step 2 rules out \(R_j<\delta_j\); because the two sums coincide, \(R_1=\delta_1\) and \(R_2=\delta_2\). If any plank were oblique, select either coordinate \(j\); Step 2 gives \(X_j<\delta_j\), \(X_k<1\), contradicting Step 1. Hence every plank is coordinate-parallel.

**Step 5: complete equality configurations.** Let \(W_j\) be total width of all \(e_j\)-normal planks. Their coordinate budgets are \(R_j=W_j=\delta_j<1\). Fix any coordinate \(j\) and any scalar \(x_j\in[-\tfrac12,\tfrac12]\setminus\operatorname{int}I_j\). If no \(e_j\)-normal plank contained \(x_j\), choose an \(x_k\in[-\tfrac12,\tfrac12]\) outside every \(e_k\)-normal plank; this is possible because their total width \(W_k<1\). Then \((x_j,x_k)\) is an uncovered point of the annulus. Therefore the projected \(j\)-planks cover both exterior intervals, whose total length is \(\delta_j=W_j\). Equality of total lengths forbids positive-length overlap, waste outside the square, or penetration into \(\operatorname{int}I_j\). The strips must partition precisely those exterior intervals, up to boundary endpoints. Conversely these partitions cover the annulus and have total width \(S\). This completes the characterization.

## Verification
The accompanying standalone `verify.py` checks (1) using exact rational unit normals from Pythagorean triples, including axial cases, and tests its strict mixed-normal gap and the directional-budget balance for families of rational-width planks. It also verifies the exact cost and canonical interval partitions in representative rational boxes. No finite test certifies the universal statement; the proof above supplies the all-parameter argument. Run `python verify.py` with Python 3.10+; there are no third-party dependencies.

## Relationship to prior work
Bakaev--Polyanskii [1] proves the sharp lower threshold when \(h_1+h_2=1\) (and its higher-dimensional analogue), and supplies the Bang-box framework and two-variable estimate used here. Its lower-bound method already yields the numerical cost formula after scaling the total width. Neither its stated theorem nor the inspected full text classifies **every minimizing plank configuration** for the strict supercritical range \(h_1+h_2>1\). The new result is the rigidity and exhaustive equality classification, not a claim of novelty for Bang's lemma or the cost threshold. Ambrus--Corbo--Goto--Leitz--Mawhinney [2] studies lower bounds for homothetic cubical holes; Bakaev--Yehudayoff [3] studies volume stability of plank coverings. The checked available descriptions do not state the present optimizer classification.

## Limitations
The rigidity theorem concerns only finite optimal covers in dimension two with a strictly interior axis-parallel rectangular hole and \(S<1\). It does not classify minimizing covers at \(S=1\) or \(S>1\), arbitrary rotated holes, countably infinite plank families, or quantitative stability of near-minimizers. Historical priority has not received independent external review; full text of [2] and [3] could not be inspected in the available access path.

## References
[1] E. Bakaev and A. Polyanskii, *A sharp plank theorem for cube annuli*, arXiv:2611.00379v1, submitted 2026-10-30, https://arxiv.org/html/2611.00379v1 .

[2] G. Ambrus, M. Corbo, D. N. Goto, D. Leitz, and K. Mawhinney, *On plank coverings of cube annuli*, arXiv:2610.18770v1, submitted 2026-10-13, https://arxiv.org/abs/2610.18770 .

[3] E. Bakaev and A. Yehudayoff, *Volume stability of plank covers*, arXiv:2609.30409v2, revised 2026-10-08, https://arxiv.org/abs/2609.30409 .
