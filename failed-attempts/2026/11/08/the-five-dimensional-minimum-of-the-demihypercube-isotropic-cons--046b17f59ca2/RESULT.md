# The five-dimensional minimum of the demihypercube isotropic constant

## Finding

For every integer \(d\geq3\), define the canonical even-parity demihypercube
\[
H_d=\operatorname{conv}\{x\in\{0,1\}^{d}:\sum_{i=1}^{d}x_i\equiv0\pmod2\}.
\]
Let \(X_d\) be uniform with respect to \(d\)-dimensional Lebesgue measure on \(H_d\), let \(A_d=\operatorname{Cov}(X_d)\), and define the affine-invariant isotropic constant by
\[
L(H_d)^{2d}=\frac{\det A_d}{\operatorname{Vol}_d(H_d)^2}.
\]
Put \(a_d=2^{d-1}/d!\) and \(b_d=(d-1)(d-2)/[(d+1)(d+2)]\). Then
\[
\operatorname{Vol}_d(H_d)=1-a_d,\qquad
\mathbb E X_d=\tfrac12\mathbf1,\qquad
A_d=s_d^2 I_d,
\]
where
\[
s_d^2=\frac1{12}-\frac{a_d}{1-a_d}\frac{b_d}{6}.
\]
Consequently the **complete exact isotropic-constant formula** is
\[
\boxed{L(H_d)^2=\frac{1-(1+2b_d)a_d}{12(1-a_d)^{1+2/d}}.}
\]
The sequence has its **unique global minimum in dimension five**:
\[
\boxed{L(H_5)^2=\frac{83}{1092}\left(\frac{15}{13}\right)^{2/5}<L(H_d)^2\quad(d\ge3,\ d\ne5).}
\]
It exceeds the unit cube isotropic constant in dimension three, but is strictly smaller in every dimension \(d\ge4\):
\[
L(H_3)>\frac1{\sqrt{12}},\qquad
L(H_d)<\frac1{\sqrt{12}}\quad(d\ge4).
\]
Finally, the positive gap from the cube tends to zero at a factorial rate:
\[
\boxed{\lim_{d\to\infty}\frac{\frac1{\sqrt{12}}-L(H_d)}{2^{d-1}/d!}=\frac1{\sqrt{12}}.}
\]
The odd-parity demihypercube is a coordinate reflection and obeys exactly the same formulas. All claims refer to the uniform **interior** distribution, not the uniform vertex distribution.

## Assumptions and scope

The dimension is any integer \(d\ge3\). Volume is ordinary coordinate Euclidean Lebesgue volume in \(\mathbb R^d\). Isotropic constant is normalized by volume as above; no covariance-volume normalization is hidden. The polytope is full dimensional for \(d\ge3\). An affine or isometric re-embedding leaves its isotropic constant unchanged. At \(d=2\) the even-parity hull is a segment and the full-dimensional formula does not apply.

## Proof

**1. An exact cubical dissection.** For each odd-weight binary vector \(v\in\{0,1\}^{d}\) set
\[
S_v=\bigl\{x\in[0,1]^d:\sum_{i=1}^d|x_i-v_i|\le1\bigr\}.
\]
The standard forbidden-set H-description of the even-parity polytope (Ermel--Walter, equation (2), also reproduced here) reads
\[
H_d=\{x\in[0,1]^d:\sum_i|x_i-v_i|\ge1\text{ for every odd-weight }v\}.
\]
Thus the complement of \(H_d\) in the cube is the union of the interiors of \(S_v\), modulo lower-dimensional boundaries. Each \(S_v\) is a right \(d\)-simplex of edge length one and volume \(1/d!\). Any two distinct odd-weight cube vertices have Hamming distance at least two, hence \(\ell_1\)-distance at least two; their unit \(\ell_1\) simplex-neighborhood interiors are disjoint by the triangle inequality. There are \(2^{d-1}\) odd vertices. It follows *without overcounting* that
\[
\operatorname{Vol}_d(H_d)=1-\frac{2^{d-1}}{d!}=1-a_d.
\]
For \(d\ge3\), \(0<a_d<1\).

**2. Symmetry and exact covariance.** Coordinate permutations and any even number of independent coordinate complements preserve \(H_d\). For \(d\ge3\), the group includes a symmetry reversing coordinate \(i\) while leaving a distinct coordinate \(j\) unchanged (complement \(i\) and a third coordinate); it also includes a symmetry reversing coordinate \(i\) itself. Therefore \(\mathbb E X_d=\mathbf1/2\) and each off-diagonal entry of \(\operatorname{Cov}(X_d)\) vanishes. Coordinate permutations make all diagonal entries equal.

On one removed simplex, write \(y_i=|x_i-v_i|\), so \(y_i\ge0\) and \(\sum y_i\le1\). Under normalized uniform measure on this simplex, the standard simplex integration identity
\[
\int_{\sum y_i\le1}\prod_i y_i^{m_i}\,dy
=\frac{\prod_i m_i!}{(d+\sum_i m_i)!}
\]
gives \(\mathbb E y_i=1/(d+1)\) and \(\mathbb E y_i^2=2/[(d+1)(d+2)]\). As \((x_i-1/2)^2=(y_i-1/2)^2\), the average squared centered coordinate on every removed simplex is
\[
\frac14-\frac1{d+1}+\frac2{(d+1)(d+2)}
=\frac14-\frac{d}{(d+1)(d+2)}.
\]
The corresponding unnormalized cube integral is \(1/12\). Subtracting the disjoint removed contributions and dividing by remaining volume produces
\[
s_d^2=\frac{\frac1{12}-a_d\left(\frac14-\frac{d}{(d+1)(d+2)}\right)}{1-a_d}
=\frac1{12}-\frac{a_d}{1-a_d}\frac{(d-1)(d-2)}{6(d+1)(d+2)}.
\]
Since \(A_d=s_d^2I_d\), inserting \(\det A_d=(s_d^2)^d\) into the definition yields the boxed isotropic formula. This is a full interior integral, not a finite vertex average.

**3. A sharp global minimum at \(d=5\).** Set \(t=13/160\). The rational data in dimensions \(3,4,5,6,7\) are
\[
\begin{array}{c|cc}
d&\operatorname{Vol}_d(H_d)&s_d^2\\\hline
3&1/3&1/20\\
4&2/3&1/15\\
5&13/15&83/1092\\
6&43/45&97/1204\\
7&311/315&923/11196
\end{array}
\]
For any fixed \(d\), comparison of \(L(H_d)^2=s_d^2\operatorname{Vol}_d(H_d)^{-2/d}\) with \(t\) is equivalent to comparing the *rational* powers \((s_d^2/t)^d\) and \(\operatorname{Vol}_d(H_d)^2\). Direct rational cross-multiplication gives the four strict comparisons
\[
\left(\frac8{13}\right)^3>\left(\frac13\right)^2,\quad
\left(\frac{32}{39}\right)^4>\left(\frac23\right)^2,\quad
\left(\frac{3320}{3549}\right)^5<\left(\frac{13}{15}\right)^2,\quad
\left(\frac{3880}{3913}\right)^6>\left(\frac{43}{45}\right)^2.
\]
Thus the five-dimensional value is below \(t\), while the values for dimensions three, four, and six are above \(t\).

For every \(d\ge5\), the ratio of consecutive positive covariance deficits \(\frac1{12}-s_d^2=a_db_d/[6(1-a_d)]\) is
\[
\frac{\frac1{12}-s_{d+1}^2}{\frac1{12}-s_d^2}
=\frac{2d}{(d-2)(d+3)}\frac{1-a_d}{1-a_{d+1}}<1.
\]
The first factor is strictly less than one for \(d\ge5\), and the second is below one because \(a_{d+1}<a_d\). Hence \(s_d^2\) is strictly increasing for \(d\ge5\). Finally, \(s_7^2=923/11196>13/160=t\) by rational cross-multiplication. Since \(\operatorname{Vol}_d(H_d)<1\), for every \(d\ge7\) we have \(L(H_d)^2\ge s_d^2\ge s_7^2>t\). This proves the unique all-dimensional minimum, including every possible integer dimension.

**4. Cube comparison and asymptotic.** The unit cube has covariance \(I_d/12\), unit volume, and isotropic constant \(1/\sqrt{12}\). For \(d=3\), \(12L(H_3)^2=(3/5)3^{2/3}>1\), as its cube is \(243/125>1\). For \(d=4\), \(12L(H_4)^2=(4/5)\sqrt{3/2}<1\), since its square is \(24/25<1\). For \(d\ge5\), let \(p_d=1+2/d\) and \(c_d=1+2b_d\). We have \(b_d>1/d\) because
\[
d(d-1)(d-2)-(d+1)(d+2)=d^3-4d^2-d-2>0\qquad(d\ge5).
\]
Hence \(c_d>p_d>1\). The strict Bernoulli/tangent inequality \((1-a_d)^{p_d}>1-p_da_d>1-c_da_d\) proves \(12L(H_d)^2<1\).

Lastly \(a_d\to0\), \(b_d\to1\), and \(a_d=2^{d-1}/d!\). Uniform first-order expansion of the exact formula gives
\[
L(H_d)=\frac1{\sqrt{12}}\bigl[1-(b_d-1/d)a_d+O(a_d^2)\bigr].
\]
Here \(b_d-1/d\to1\), proving the claimed factorially scaled limit.

## Verification

A standalone exact-rational checker in `check_demicube.py` verifies the displayed rational comparisons, the covariance and volume formulas for finite dimensions, the covariance-deficit recurrence, and the cube comparisons using arbitrary-precision integer arithmetic. When NumPy and SciPy are installed, it also constructs the convex hull directly for dimensions three through six and compares its computed geometric volume against the formula. The latter calculation is a finite independent numerical cross-check, not a substitute for the dissection proof.

Run `python check_demicube.py` from the directory containing the checker. The optional numerical hull tests require `numpy` and `scipy` as listed in `requirements.txt`. If these packages are absent, the checker still performs its exact-rational tests and clearly reports that hull tests were skipped.

## Relationship to prior work

Ermel and Walter (2018) give the known complete forbidden-set inequalities for the parity polytope; those inequalities justify the cubical corner dissection. Borodachov (2023) studies the same demihypercube vertex configurations as spherical codes and classifies certain potential-minimizing points, not the uniform **interior** covariance and affine-invariant isotropic constant. Kipp (2024) studies isotropic constants of convex polytopes and provides the correct normalization and cube/cross-polytope benchmarks; its results on local maximizers and certain zonotopes do not give the present demihypercube formula or its unique five-dimensional minimizer. The known dimensions three and four are regular simplex and cross-polytope cases; the new claim is the all-dimensional exact family, global minimum at five, and factorial cube-gap law. A prior record on type-\(D\) spin-weight polytopes concerns John and Löwner ellipsoids of the same even-parity vertex orbit, not the uniform-volume isotropic constant. These invariants are distinct, and an ellipsoid theorem alone does not imply the present formula.

## Limitations

The proof is restricted to the standard even- or odd-parity demihypercube for \(d\ge3\). It does not classify all parity-restricted subsets, arbitrary orthant truncations, or arbitrary vertex-deletion polytopes. Affine invariance permits rescalings or invertible affine images but not arbitrary changes of the distribution from interior-uniform to vertex-uniform. Historical priority is provisional: although targeted literature and mathematical-record searches did not identify an equivalent full formula and all-dimensional extremizer statement, terminology including halfcubes, type-\(D\) weight polytopes, and parity-code polytopes may conceal related prior work. Some potentially relevant external full texts could not be accessed. Independent audit has not been performed.

## References

1. D. Ermel and M. Walter, *Parity Polytopes and Binarization*, arXiv:1803.10561v2 (2018), especially equation (2) and Section 3. https://arxiv.org/html/1803.10561v2
2. S. Borodachov, *Universal minima of potentials of certain spherical designs contained in the fewest parallel hyperplanes*, arXiv:2301.06623v1 (first public version 2023-01-16), especially Section 3. https://arxiv.org/html/2301.06623v1
3. C. Kipp, *Isotropic constants and platonic solids*, arXiv:2407.01353 (first public version 2024-07-01), especially Section 1 and Section 6. https://arxiv.org/abs/2407.01353
