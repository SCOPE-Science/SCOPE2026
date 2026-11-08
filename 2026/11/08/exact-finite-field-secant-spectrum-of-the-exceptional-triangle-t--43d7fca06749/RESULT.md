# Exact finite-field secant spectrum of the exceptional-triangle toric cubic

## Finding

For a prime power \(q\ge3\), set \(k=\mathbb F_q\), \(N=(q-1)^2\), and consider the torus point set
\[
\mathcal T_q=\{[1:x:y:(xy)^{-1}]:(x,y)\in(k^\times)^2\}\subset\mathbb P^3(k).
\]
It is the dense-torus point set of the projective cubic surface
\[
\Sigma:\quad X_1X_2X_3=X_0^3.
\]
For \(0\le j\le3\), let \(n_j(q)\) be the number of \(k\)-rational projective lines whose intersections with \(\mathcal T_q\) contain exactly \(j\) distinct rational points. Define
\[
\rho_q=\#\{t\in k:t^2+t+1=0\}=
\begin{cases}
2,&q\equiv1\pmod3,\\
0,&q\equiv2\pmod3,\\
1,&3\mid q,
\end{cases}
\qquad \tau_q=(q-2)(q-5)+2\rho_q.
\]
The **entire rational line-intersection spectrum** is
\[
\begin{aligned}
n_3(q)&=\frac{(q-1)^2\tau_q}{6},\\
n_2(q)&=\frac{(q-1)^2(5q-10-2\rho_q)}{2},\\
n_1(q)&=\frac{(q-1)^2(q^2-q+12+2\rho_q)}{2},\\
n_0(q)&=(q^2+1)(q^2+q+1)-n_1(q)-n_2(q)-n_3(q).
\end{aligned}
\]
No rational projective line meets \(\mathcal T_q\) in more than three points. In particular \(\mathcal T_3\) and \(\mathcal T_5\) are caps (sets without collinear triples), whereas \(\mathcal T_q\) has collinear triples for \(q=4\) and every prime power \(q\ge7\). The number of collinear triples is exactly \(n_3(q)\).

The four-dimensional **exceptional-triangle toric code**
\[
C_q=\operatorname{ev}_{(k^\times)^2}
\langle 1,x,y,(xy)^{-1}\rangle_k\subset k^N
\]
has second generalized Hamming weight
\[
\boxed{d_2(C_q)=\begin{cases}
N-2,&q\in\{3,5\},\\
N-3,&q=4\text{ or }q\ge7.
\end{cases}}
\]
Hence it is 2-MDS (attains the generalized Singleton bound) precisely for \(q=3,5\); otherwise its second weight has Singleton defect one. The number of two-dimensional subcodes attaining this weight is \(n_2(q)\) for \(q=3,5\) and \(n_3(q)\) otherwise. For all \(q\ge3\), its third and fourth generalized Hamming weights are \(d_3(C_q)=N-1\) and \(d_4(C_q)=N\).

## Assumptions and scope

A rational line means an \(\mathbb F_q\)-defined line in the ambient projective three-space, not necessarily a line contained in \(\Sigma\). In fact none of the lines contained in \(\Sigma\) meets \(\mathcal T_q\). Points and intersections are counted over \(\mathbb F_q\); no claim is made about geometric multiplicities of a tangent intersection. The four lattice exponents \((0,0),(1,0),(0,1),(-1,-1)\) are the complete lattice-point set of a strongly indecomposable exceptional triangle: the three nonzero points are its primitive vertices and the origin is its unique interior point. The code is the full torus evaluation of their four characters, not the full degree-one Reed–Muller code on a projective torus.

For a linear code \(C\), its second generalized Hamming weight is the minimum cardinality of the union of coordinate supports of a two-dimensional subcode. More generally \(d_r(C)\) uses \(r\)-dimensional subcodes. Here \(C_q\) has dimension four for all \(q\ge3\), because its four characters have pairwise distinct exponent residues modulo \(q-1\); the full torus character-evaluation matrix has independent columns (equivalently, a tensor product of finite-field Vandermonde matrices).

## Proof

**1. A uniform cubic upper bound.** The equation \(X_1X_2X_3=X_0^3\) is homogeneous of degree three and vanishes on \(\mathcal T_q\). It has no geometric projective line contained in it that meets its dense torus: after passing to the affine chart \(X_0=1\), such a line would have three affine-linear coordinate functions in one parameter whose product is the constant one. The only polynomial units are constants, which would make the line a point. Consequently, Bezout's degree bound for a line not contained in a cubic gives at most three distinct torus intersection points, over \(k\) or its algebraic closure.

**2. Fix a torus point and count its three-secants.** The diagonal group
\[
[1:u:v:w]\longmapsto[1:au:bv:(ab)^{-1}w],\qquad a,b\in k^\times,
\]
preserves \(\Sigma\), acts transitively on \(\mathcal T_q\), and acts by projective collineations. Thus it is enough to count the other points \(B=[1:a:b:c]\) on genuine three-secants through \(A=[1:1:1:1]\), with \(abc=1\).

Write \(\alpha=a-1\), \(\beta=b-1\), \(\gamma=c-1\), \(s_1=\alpha+\beta+\gamma\), and \(s_3=\alpha\beta\gamma\). On the affine line through \(A\) and \(B\), parametrized as \([1:1+t\alpha:1+t\beta:1+t\gamma]\), the cubic equation restricts to
\[
(1+t\alpha)(1+t\beta)(1+t\gamma)-1
=t(t-1)(s_3t-s_1).
\]
Here the second symmetric sum is \(-s_1-s_3\), because the restriction vanishes at \(t=1\). This line has a third distinct torus point if and only if \(s_3\ne0\), \(s_1\ne0\), and \(s_1\ne s_3\). In that case the third parameter \(t=s_1/s_3\) belongs to \(k\), is not zero or one, and its three affine coordinates are nonzero because their product is one.

There are exactly \(3(q-2)\) choices \(B\ne A\) with \(s_3=0\): these are the union of the three subtori \(a=1\), \(b=1\), \(c=1\), whose pairwise intersections are the singleton \(A\). Hence \((q-2)(q-3)\) points \(B\ne A\) have \(s_3\ne0\).

**3. Count the tangent exclusions by rational parametrization.** The equation \(s_1=0\) is the tangent-plane condition \(a+b+c=3\). Put \(a=1+u\), \(b=1+ku\). Since \(s_3\ne0\), we have \(u\ne0\), \(k\ne0\), and \(k\ne-1\). The tangency equation \(abc=1\) with \(c=1-(1+k)u\) becomes
\[
u^2\bigl(1+k+k^2+uk(1+k)\bigr)=0.
\]
For every \(k\in k\setminus\{0,-1\}\) with \(1+k+k^2\ne0\), there is exactly one nonzero solution
\[
u=-\frac{1+k+k^2}{k(1+k)},\qquad
(a,b,c)=\left(-\frac1{k(1+k)},-\frac{k^2}{1+k},\frac{(1+k)^2}{k}\right).
\]
All three coordinates are nonzero and different from one, and every \(B\) with \(s_3\ne0\) and \(s_1=0\) arises uniquely. Thus there are \(q-2-\rho_q\) tangent-at-\(A\) exclusions.

The inversion involution \((a,b,c)\mapsto(a^{-1},b^{-1},c^{-1})\) interchanges the conditions \(s_1=0\) and \(s_1=s_3\) when \(abc=1\): indeed
\[
s_1-s_3=(a^{-1}+b^{-1}+c^{-1})-3.
\]
It preserves \(s_3\ne0\), so it gives exactly \(q-2-\rho_q\) tangent-at-\(B\) exclusions as well. The two excluded sets are disjoint when \(s_3\ne0\). Therefore the number of other torus points \(B\) that lie with \(A\) on a genuine three-secant is
\[
\tau_q=(q-2)(q-3)-2(q-2-\rho_q)=(q-2)(q-5)+2\rho_q.
\]
The polynomial \(t^2+t+1\) has two roots when \(q\equiv1\pmod3\), none when \(q\equiv2\pmod3\), and one repeated root when \(3\mid q\); this proves the formula for \(\rho_q\) in every characteristic, including two and three.

**4. Count every projective line.** With \(N=|\mathcal T_q|\), there are \(N\tau_q\) ordered pairs \((A,B)\) lying on a three-secant, and each three-secant accounts for exactly six ordered pairs. Therefore \(n_3(q)=N\tau_q/6\). Every unordered pair of distinct torus points defines one rational projective line. A two-secant contributes one pair and a three-secant contributes three, so
\[
n_2(q)+3n_3(q)=\binom N2.
\]
Every rational point of \(\mathbb P^3(k)\) lies on \(q^2+q+1\) rational projective lines, so
\[
n_1(q)+2n_2(q)+3n_3(q)=N(q^2+q+1).
\]
Finally the total number of rational lines in \(\mathbb P^3(k)\) is
\[
\begin{bmatrix}4\\2\end{bmatrix}_q=(q^2+1)(q^2+q+1),
\]
whence the displayed formulas for \(n_0,n_1,n_2,n_3\). For \(q\ge7\), \(\tau_q>0\); at \(q=4\), \(\rho_q=2\) gives \(\tau_q=2\); at \(q=3\) and \(q=5\), direct substitution gives \(\tau_q=0\). All \(n_2\) values are positive for \(q\ge3\). This proves the cap dichotomy and secant counts.

**5. Convert the line spectrum into higher weights.** A pair of linearly independent codewords is a pair of independent linear forms on \(\mathbb P^3\); their common coordinate zero set is exactly the intersection of \(\mathcal T_q\) with the projective line cut out by those forms. Conversely every rational projective line arises in this way, with a unique two-dimensional annihilator in the four-dimensional space of linear forms. Thus \(d_2(C_q)=N-\max\{j:n_j(q)>0\}\), and the number of optimal two-dimensional subcodes is precisely \(n_2(q)\) or \(n_3(q)\) as stated. Three independent linear forms cut out one projective point, so the maximum number of common torus zeros is one; four independent forms have no projective common zero. Consequently \(d_3=N-1\) and \(d_4=N\). The second generalized Singleton bound for a length-\(N\), dimension-four code is \(d_2\le N-2\), yielding the exact 2-MDS classification.

## Verification

The self-contained standard-library program `verify_toric_trisecants.py` constructs finite fields via polynomial arithmetic, checks the tangent exclusions and the third-point calculation for all torus points in fields of sizes \(3,4,5,7,8,9,11,13,16,25,27\), and verifies all four line-spectrum formulas. Its recorded output is `verification_output.txt`. The independent `direct_line_census.py` enumerates every rational projective line in \(\mathbb P^3\) for fields of sizes \(3,4,5,7,8,9\) using reduced-row-echelon bases and checks each actual intersection count without using the tangent enumeration. Its recorded output is `direct_line_output.txt`. Both programs passed. These finite checks corroborate the proof but do not substitute for the uniform symbolic argument.

## Relationship to prior work

Soprunov (arXiv:1411.0028, first public 2014-10-31), Section 2, specifically identifies the exceptional triangle as the four-point strongly indecomposable lattice polygon and treats toric-code minimum-distance bounds. It motivates the present natural four-dimensional evaluation code, but does not give its higher Hamming weights or the rational line-intersection spectrum of its projective monomial image.

González Sarabia, Camps, Sarmiento and Villarreal (arXiv:1611.06405, 2016/2018) study second generalized weights of full projective-torus Reed–Muller-type codes and general monotonicity for monomial-parameterized codes. Their degree-one full projective torus has \((q-1)^3\) points in \(\mathbb P^3\), rather than the \((q-1)^2\) points of this proper monomial toric surface; their Theorems 12 and 18 do not determine the stated exact line spectrum. Patanker and Singh (arXiv:2002.10920, 2020) treat hypersimplex and squarefree code families. The exceptional triangle has an interior lattice point and cannot be lattice-equivalent to those hypersimplex supports; their general squarefree formulas do not apply to the four Laurent characters here. The new claim is the all-\(q\) secant spectrum, small-field cap threshold, and precise second-weight/optimizer census, not the definitions or established general bounds.

## Limitations

Historical novelty is qualified by the possibility of an unlocated equivalent finite-geometry computation of trisecants to this toric cubic; the targeted literature comparisons are not a global priority certificate. The result concerns rational lines in ambient projective three-space and the full exceptional-triangle torus code, not the geometric Fano scheme of lines lying on the cubic surface, other lattice polygons, or the first generalized Hamming weight of the code. No independent scientific audit has been performed.

## References

1. I. Soprunov, *Lattice polytopes in coding theory*, first posted 2014-10-31, arXiv:1411.0028, especially Section 2, Definition 2.3 and the classification of strongly indecomposable polygons. https://arxiv.org/abs/1411.0028.
2. M. González Sarabia, E. Camps, E. Sarmiento and R. H. Villarreal, *The second generalized Hamming weight of some evaluation codes arising from a projective torus*, arXiv:1611.06405 (first posted 2016-11-19); Sections 4–5 and Theorems 12, 18. https://arxiv.org/abs/1611.06405.
3. N. Patanker and S. K. Singh, *Generalized Hamming weights of toric codes over hypersimplices and square-free affine evaluation codes*, arXiv:2002.10920 (first posted 2020-02-25); Sections 2–4. https://arxiv.org/abs/2002.10920.
4. V. K. Wei, *Generalized Hamming weights for linear codes*, IEEE Transactions on Information Theory **37** (1991), 1412–1418. https://doi.org/10.1109/18.133259.
