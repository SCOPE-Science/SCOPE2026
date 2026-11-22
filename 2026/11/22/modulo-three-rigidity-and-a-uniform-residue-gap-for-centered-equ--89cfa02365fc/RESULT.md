# Modulo-three rigidity and a uniform residue gap for centered equilateral triangles in hypercubes

## Finding

Let \(d\ge 2\) be an integer and let \(Q_d=[-1,1]^d\). For three points \(p_1,p_2,p_3\in Q_d\) with \(p_1+p_2+p_3=0\) and \(\|p_1-p_2\|=\|p_2-p_3\|=\|p_3-p_1\|=s>0\), set
\[
M_d^2=\max s^2,\qquad \Delta_d=2d-M_d^2.
\]
The following statements hold.

**Saturation, classification and count.** Every such triangle satisfies \(s^2\le 2d\). Equality occurs if and only if \(d=3m\), \(m\ge1\). In that case every maximizing ordered triple is exactly a \(d\times3\) matrix whose rows are signed permutations of \((1,-1,0)\), with each of the three vertex columns having exactly \(m\) zeros. These matrices form one orbit under coordinate permutations, coordinate sign changes and permutation of the three triangle vertices. The number of *unordered, geometrically distinct* maximizing triangles in the fixed cube is exactly
\[
N_{3m}=\frac{2^{3m}(3m)!}{6(m!)^3}\qquad(m\ge1).
\]
In particular, \(N_3=8\) and \(N_6=960\).

**Uniform residue obstruction and constructions.** In the two remaining residue classes,
\[
\begin{aligned}
 d\equiv1\pmod3,\ d\ge4 &: \quad \frac45\le\Delta_d\le12\sqrt2-16,\\
 d\equiv2\pmod3,\ d\ge2 &: \quad \frac47\le\Delta_d\le12\sqrt3-20.
\end{aligned}
\]
Both upper bounds on \(\Delta_d\) are attained by explicitly constructed *feasible triangles*, but the theorem does not assert that these constructions are optimizing. The lower bounds are uniform, not claimed to be sharp.

**Near-equality rigidity.** If \(d=3m\) and a centered equilateral triangle has \(\delta=2d-s^2<6/5\), then a saturating triangle \(v_1,v_2,v_3\) with \(v_1+v_2+v_3=0\) exists in the *same fixed cube*, with corresponding labeled vertices satisfying
\[
\sum_{i=1}^3\|p_i-v_i\|^2\le\delta.
\]
Consequently \(M_d^2=2d-O(1)\), and \(M_d/\sqrt{2d}\to1\) as \(d\to\infty\).

## Assumptions and scope

All norms and distances are Euclidean. The triangle must have its arithmetic vertex centroid at the center of the cube; it need not have all three vertices on the boundary. Cube coordinates have half-side length one. The dimension \(d\) is any integer at least two. The maximum is attained by compactness, since positive-length feasible examples exist. The count distinguishes unordered sets of three triangle points inside the fixed, coordinate-labeled cube; it does not quotient by cube symmetries. The near-equality assertion is for triangles with \(3\mid d\) only.

## Proof

**1. Coordinate cap.** Since \(p_1+p_2+p_3=0\) and all three edges have length \(s\), the identity
\[
\sum_{i<j}\|p_i-p_j\|^2=3\sum_i\|p_i\|^2
\]
gives \(\sum_i\|p_i\|^2=s^2\); moreover all three vertex norms agree and \(\|p_i\|^2=s^2/3\). For each ambient coordinate \(j\), the triple \(q_j=(p_{1j},p_{2j},p_{3j})\) lies in the planar hexagon
\[
H=\{q\in[-1,1]^3:q_1+q_2+q_3=0\},
\]
whose six vertices are the permutations of \((1,-1,0)\). The strictly convex function \(q\mapsto\sum_iq_i^2\) has maximum \(2\) on \(H\), attained only at these six vertices: every nonvertex is a nontrivial convex combination of vertices, and strict convexity makes its squared norm smaller. Hence
\[
s^2=\sum_{j=1}^d\|q_j\|^2\le2d,
\]
with equality if and only if all rows of the coordinate matrix belong to the six-vertex set.

**2. Exact saturation and enumeration.** Let \(k_i\) be the number of nonzero entries in the \(i\)-th vertex column of an equality matrix. Since each coordinate row has exactly two nonzero entries, \(k_1+k_2+k_3=2d\). Equal vertex norms require \(k_1=k_2=k_3=2d/3\), which is integral only when \(3\mid d\). For \(d=3m\), take \(m\) copies of the three coordinate rows
\[
B_3=\begin{pmatrix}1&-1&0\\0&1&-1\\-1&0&1\end{pmatrix}.
\]
Its three vertex columns each have squared norm \(2\), sum to zero, and are pairwise at squared distance \(6\). Stacking \(m\) copies attains \(s^2=6m=2d\). For any equality triangle, exactly \(m\) coordinate rows have their zero in each labeled vertex column. Choose the three zero-position blocks in \(d!/(m!)^3\) ways, and choose the sign of each row independently in \(2^d\) ways. Every unordered triangle has precisely six ordered labelings, yielding \(N_{3m}\). Coordinate permutations and sign changes carry any such equality matrix to any other, proving the orbit statement.

**3. Quantitative hexagon-vertex rounding.** For any \(q\in H\), put \(e(q)=2-\|q\|^2\). Reorder the entries and, if needed, reverse signs, to write \(q=(a,-b,-c)\) with \(a=b+c\), \(0\le c\le b\), \(0\le a\le1\). Choose the hexagon vertex \(v=(1,-1,0)\) in these coordinates. We claim
\[
\|q-v\|^2\le e(q),\qquad
\sum_{i=1}^3|q_i^2-v_i^2|\le2e(q).
\tag{1}
\]
For the first inequality, the difference of right and left sides is \(2[a+b-a^2-b^2-c^2]\). Holding \(a\) fixed and writing \(c=a-b\), the polynomial \(f(b)=a^2+b^2+(a-b)^2-a-b\) is convex on \([a/2,a]\). Its endpoint values are \(f(a)=2a(a-1)\le0\) and \(f(a/2)=3a(a-1)/2\le0\). Thus \(f(b)\le0\) throughout. For the second inequality, the left side is \(e(q)+2c^2\). Since \(b=a-c\le1-c\) and \(a\le1\),
\[
e(q)\ge 2-1-(1-c)^2-c^2=2c(1-c)\ge2c^2
\]
(the last inequality uses \(c\le1/2\)). This proves (1), including at vertices and all boundary cases.

Apply (1) independently to the \(d\) coordinate triples, creating a \(d\times3\) matrix of hexagon vertices with vertex columns \(v_i\). Let \(\delta=2d-s^2\), and let the integers \(k_i=\|v_i\|^2\) count their nonzero coordinates. Then
\[
\sum_i\|p_i-v_i\|^2\le\delta,\qquad
\sum_i\left|k_i-\frac{2d-\delta}{3}\right|\le2\delta,
\qquad \sum_i k_i=2d.
\tag{2}
\]

**4. The modular obstructions.** If \(d=3m+1\) and \(0\le\delta<2\), the real target in (2) is \(r=2m+(2-\delta)/3\in(2m,2m+1]\). Over integer triples summing to \(6m+2\), the minimum of \(\sum_i|k_i-r|\) is \((4+\delta)/3\), achieved by a permutation of \((2m,2m+1,2m+1)\). The inequality (2) then requires \(2\delta\ge(4+\delta)/3\), hence \(\delta\ge4/5\). For \(\delta\ge2\), this bound is automatic.

If \(d=3m+2\) and \(0\le\delta<1\), the target \(r=2m+(4-\delta)/3\) lies strictly between \(2m+1\) and \(2m+2\). The minimum over integer triples with sum \(6m+4\) is \((4-\delta)/3\), attained at a permutation of \((2m+1,2m+1,2m+2)\). Consequently \(\delta\ge4/7\); for \(\delta\ge1\), again automatic. These integer minimizations follow by the exchange rule: if two integers in an integer triple differ by at least two, moving one unit from the larger to the smaller cannot increase the sum of absolute deviations from a common target in the stated target interval. Equivalently, check the two adjacent integers around \(r\) and the fixed sum.

If \(d=3m\) and \(\delta<6/5\), then \(r=2m-\delta/3\). If \((k_1,k_2,k_3)\) is not identically \(2m\), its minimum possible total deviation is \(2+\delta/3\), realized by \((2m-1,2m,2m+1)\). This exceeds \(2\delta\) for \(\delta<6/5\), contradicting (2). Hence the rounded matrix has each vertex column of squared norm \(2m\). By step 2 it is a maximizing triangle, and the first inequality of (2) establishes the claimed quantitative rigidity.

**5. Feasible residue-class blocks.** Regard the rows of the following matrices as ambient-coordinate triples, and the columns as the three triangle vertices:
\[
B_2=\begin{pmatrix}-1&\sqrt3-1&2-\sqrt3\\2-\sqrt3&\sqrt3-1&-1\end{pmatrix},
\qquad
B_4=\begin{pmatrix}
1&-1&0\\
-1&0&1\\
1-\sqrt2&1&\sqrt2-2\\
1-\sqrt2&\sqrt2-2&1
\end{pmatrix}.
\]
Every entry belongs to \([-1,1]\), every coordinate row sums to zero, and within each matrix the three column norms are equal. Their squared column norms are respectively \(8-4\sqrt3\) and \(8-4\sqrt2\); therefore \(B_2\) and \(B_4\) produce centered equilateral triangles of squared side lengths \(24-12\sqrt3\) and \(24-12\sqrt2\). Concatenating \(B_2\) with \(m\) copies of \(B_3\) yields dimension \(3m+2\); concatenating \(B_4\) with \(m-1\) copies of \(B_3\) yields dimension \(3m+1\). Their squared sides give exactly the stated construction bounds on \(\Delta_d\). The obstruction bounds and these constructions imply \(0\le\Delta_d\le12\sqrt2-16\) for every \(d\ge2\), proving the asymptotic assertion.

## Verification

The accompanying `verify.py` uses SymPy for exact checks of the coordinate-block centroid identities, equality of column norms, every squared edge length, and the three threshold equations. It repeats the constructions in each congruence class for the first several admissible dimensions. It also checks the rounding inequalities on 30,000 independently generated rational coordinate triples. Running `python verify.py` reproduced a PASS. The all-dimensional coordinate inequalities, the integer-minimization arguments, classification, and stability are proved analytically above; a finite test is not their proof.

## Relationship to prior work

The first publicly posted version of Ambrus and Gárgyán, *Non-diagonal critical central sections of the cube* (2023-07-07), concerns the volume and critical normal directions of centered hyperplane slices of a cube. It motivates testing a different central-section geometry, namely the maximal regular two-simplex whose centroid is fixed at the cube center. Its theorems concern hyperplane-section volume, not extremal contained triangles or a modulus-three classification.

Ionin's 2015 solution to Problem 11693 in the *American Mathematical Monthly* determines the largest **unconstrained-centroid** equilateral triangle inside a cube in every dimension; this is essential background. That result does not impose center coincidence and its optimal squared side length on \([-1,1]^d\) is \(8d/3\) when \(3\mid d\), strictly above our \(2d\). Neither the centered equality matrices nor their count, uniform residue gaps, and near-equality distance bound follow as statements of the unrestricted optimum. Wenzel's 2002 work studies full-dimensional regular simplices formed by cube vertices and their binary-code structure, not this three-point centered containment problem. The difference between these precise hypotheses is substantial; matching the residue class alone is not a novelty certificate.

## Limitations

The theorem does **not** determine the exact optimal side length for \(d\equiv1,2\pmod3\). In those classes, the lower bounds on the deficits are not claimed sharp and the explicit constructed upper bounds are not certified optimal. It does not classify nonmaximizing contained triangles, triangles with an arbitrary prescribed centroid, or higher-dimensional regular simplices. The historical-priority comparison is limited by indexed/accessible literature and cannot rule out unindexed equivalent centered-containment results. Independent external mathematical validation has not been performed.

## References

1. G. Ambrus and B. Gárgyán, *Non-diagonal critical central sections of the cube*, arXiv:2307.03792 (first public version 2023-07-07), subsequently *Advances in Mathematics* 441 (2024), article 109524. https://arxiv.org/abs/2307.03792 ; lawful full-text copy https://real.mtak.hu/191901/1/2307.03792v4.pdf
2. Y. J. Ionin, solution to Problem 11693, *Inscribe an Equilateral Triangle in a Hypercube*, *American Mathematical Monthly* 122(2) (2015), 178–181. https://lupucezar.wordpress.com/wp-content/uploads/2011/02/amer-math-monthly-122-02-175.pdf
3. W. Wenzel, *Regular Simplices Inscribed into the Cube and Exhibiting a Group Structure*, TU Chemnitz Preprint 2002-11 (2002). https://www.tu-chemnitz.de/mathematik/preprint/2002/PREPRINT_11.pdf
4. J. Cantarella, E. Denne and J. McCleary, *Families of similar simplices inscribed in most smoothly embedded spheres*, arXiv:2106.12063 (first posted 2021-06-22), *Forum of Mathematics, Sigma* 10 (2022). https://arxiv.org/abs/2106.12063
