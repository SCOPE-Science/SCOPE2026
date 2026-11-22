# Logarithmic vertex-dispersion deficit of Catalan matroid polytopes

## Finding
For each integer \(n\ge2\), let \(P_n\subset\mathbb R^{2n}\) be the convex hull of the incidence vectors of the up-step positions of all Dyck paths of semilength \(n\), with the standard orthonormal-coordinate Euclidean metric. Let \(X,Y\) be independent uniformly selected **vertices** (not uniform interior points) of \(P_n\). Define
\[
 a_j=\binom{2j}{j},\quad
 q_{n,j}=\frac{n-2j}{n}\frac{a_ja_{n-j}}{a_n}\qquad(1\le j<n).
\]
Then the exact mean squared distance and the centered vertex inertia are
\[
 \mathbb E\|X-Y\|_2^2=n-1-\sum_{j=1}^{n-1}q_{n,j}^2,
 \qquad
 I_n:=\mathbb E\|X-\mathbb EX\|_2^2
 =\frac{n-1}{2}-\frac12\sum_{j=1}^{n-1}q_{n,j}^2.
\]
Writing \(\gamma\) for Euler's constant, their large-size asymptotics are
\[
 I_n=\frac n2-\frac{\log n}{\pi}
 +\frac12-\frac{\gamma+\log16-2}{\pi}
 +O\!\left(\frac{\log n}{n}\right),
\]
\[
 \mathbb E\|X-Y\|_2^2
 =n-\frac{2\log n}{\pi}+1-
 \frac{2(\gamma+\log16-2)}{\pi}
 +O\!\left(\frac{\log n}{n}\right).
\]
In contrast, two independent uniformly chosen vertices of the hypersimplex \(\Delta(2n,n)\) have mean squared Euclidean distance exactly \(n\). Thus the nonnegativity constraint defining the Catalan vertices decreases this metric dispersion by a growing, but only logarithmic, amount with sharp coefficient \(2/\pi\).

## Assumptions and scope
A Dyck path consists of \(2n\) unit steps \(+1,-1\) with \(n\) of each sign, starting and ending at height zero and staying nonnegative. Each Dyck path defines its binary incidence vector \(X\in\{0,1\}^{2n}\), where a coordinate is one at an up-step. These are distinct vertices of the standard matroid base polytope. The expectation assigns equal mass to each of the \(C_n=a_n/(n+1)\) vertices. All distances and centered moments use the ambient standard Euclidean metric, which agrees with the induced intrinsic metric on the affine hull. The first and last coordinates are fixed and contribute zero variance. No interior-volume or random-direction statement is claimed.

## Proof
**Step 1: exact mean step bias.** Write \(\xi_i=2X_i-1\in\{-1,1\}\) and \(\mu_i=\mathbb E\xi_i\). Time reversal and sign reversal give \(\mu_{2n+1-i}=-\mu_i\). A local swap of the two steps around an even time gives \(\mu_{2j}=\mu_{2j+1}\) for \(1\le j<n\); if the steps are opposite, both orders are nonnegative because the preceding height is odd and at least one, so the two choices are equinumerous.

For a self-contained algebraic evaluation, let \(B_k(h)\) be the number of nonnegative up/down prefixes of length \(k\) ending at height \(h\), with zero for negative or parity-incompatible \(h\). Reflection gives
\[
 B_k(h)=\binom{k}{(k-h)/2}-\binom{k}{(k-h)/2-1}
\]
with out-of-range binomial coefficients interpreted as zero. Let \(C(z)=(1-\sqrt{1-4z})/(2z)\), satisfying \(C=1+zC^2\). The standard first-return decomposition gives, for every \(m\ge0\),
\[
 \sum_{j\ge0}B_{2j}(2m)x^j=x^mC(x)^{2m+1},\quad
 \sum_{L\ge1}B_{2L-1}(2m+1)y^L=y^{m+1}C(y)^{2m+2},
\]
and, for \(m\ge1\),
\[
 \sum_{L\ge1}B_{2L-1}(2m-1)y^L=y^mC(y)^{2m}.
\]
Counting the two possible signs of the step following time \(2j\) therefore gives the bivariate generating series
\[
 G(x,y):=\sum_{j\ge0,L\ge1}C_{j+L}\mu_{2j+1}^{(j+L)}x^j y^L
 =\frac{C(x)(C(y)-1)(2-C(x))}{1-(C(x)-1)(C(y)-1)}.
\]
Here \(\mu_i^{(n)}\) denotes the bias at step \(i\) in semilength \(n\). Set \(F=G-(C(x)-1)\), \(s=\sqrt{1-4x}\), \(t=\sqrt{1-4y}\). Since \(C(z)-1=(1-\sqrt{1-4z})/(1+\sqrt{1-4z})\), direct simplification yields
\[
 F(x,y)=\frac{s-t}{s+t}.
\]
Let \(D=x\partial_x+y\partial_y\) and \(S(z)=(1-4z)^{-1/2}=\sum_{k\ge0}a_kz^k\). Direct differentiation establishes the formal-power-series identity
\[
 D(D+1)F=S(x)yS'(y)-xS'(x)S(y).
\]
Since \(F\) has zero constant term, comparing the coefficients of \(x^jy^L\) with \(j+L=n\ge1\) gives
\[
 [x^jy^L]F=\frac{L-j}{n(n+1)}a_ja_L.
\]
For \(L\ge1\), these coefficients are \(C_n\mu_{2j+1}^{(n)}\). Using \(C_n=a_n/(n+1)\), one obtains
\[
 \mu_1=1,\quad \mu_{2n}=-1,\quad
 \mu_{2j}=\mu_{2j+1}=q_{n,j}\quad(1\le j<n).
\]
The formula for \(\mu_{2j}\) follows also by the two-step swap noted above.

**Step 2: exact Euclidean inertia.** Since \(X_i=(1+\xi_i)/2\),
\[
 \operatorname{Var}(X_i)=\frac14(1-\mu_i^2).
\]
Summing over the \(2n\) coordinates and using the endpoint and paired bias values proves the formula for \(I_n\). For independent \(X,Y\), \(\mathbb E\|X-Y\|_2^2=2I_n\), proving the exact distance identity. In the hypersimplex every coordinate has expectation \(1/2\), giving \(2n\cdot2(1/4)=n\).

**Step 3: sharp asymptotics.** Put \(c_j=a_j/4^j\) and \(A(z)=\sum_{j\ge0}c_j^2z^j={}_2F_1(1/2,1/2;1;z)=(2/\pi)K(\sqrt z)\), with \(K\) the complete elliptic integral of the first kind (modulus convention). Define
\[
 T_n=[z^n]A(z)^2,\qquad U_n=[z^n](zA'(z))^2.
\]
Expanding the coefficient products and using \((n-2j)^2=n^2-4j(n-j)\) gives the **exact** identity
\[
 \frac n2-I_n=\frac12\left(\frac{T_n-4U_n/n^2}{c_n^2}-1\right).
\]
The classical elliptic-integral expansion near \(z=1\), valid in a slit complex neighborhood, is
\[
 A(z)=\frac1\pi\log\frac{16}{1-z}+O((1-z)\log(1-z)).
\]
Coefficient extraction (or standard singularity analysis) consequently gives
\[
 T_n=\frac{2}{\pi^2 n}(\log n+\gamma+\log16)+O\!\left(\frac{\log n}{n^2}\right),
\]
\[
 U_n=\frac{n}{\pi^2}+O(\log n),\qquad
 c_n^2=\frac1{\pi n}\left(1+O\!\left(\frac1n\right)\right).
\]
Substitution yields
\[
 \frac n2-I_n=\frac{\log n+\gamma+\log16-2}{\pi}-\frac12+O\!\left(\frac{\log n}{n}\right),
\]
which proves both asymptotic assertions. The \(16\) in the constant comes from the elliptic-integral singularity; omitting it changes the constant term.

## Verification
The standalone `check.py` enumerates every Dyck path for \(1\le n\le7\). For each size it compares the direct step-bias vector, exact rational vertex inertia, and independently computed all-ordered-pairs Hamming distance with the theorem. Its final successful message is `CATALAN_VERTEX_INERTIA_EXACT_PASS n=1..7`. It also reports floating-point asymptotic discrepancies for \(n=10,100,1000\). These finite and numerical tests support, but do not replace, the generating-function proof and elliptic singularity analysis.

## Relationship to prior work
The identification of Dyck words with bases of the Catalan matroid and the canonical incidence-vector polytope are classical. Bidkhori (2012) establishes lattice-path matroid polytope geometry; Knauer, Martínez-Sandoval and Ramírez Alfonsín (2017) study lattice-point enumeration, distributive models and Ehrhart theory; An, Jung and Kim (2017) study faces. Cohen, Tetali and Yeliussizov (2015) establish negative correlation and mixing bounds for Dyck-basis exchange; that result constrains pairwise coordinate correlations but does not imply the exact coordinate **means**, elliptic convolution, or dispersion constant without further calculation. The new statement is a uniform-vertex Euclidean second-moment law and its logarithmic asymptotic correction, not a claim of a new matroid or a new Catalan enumeration.

## Limitations
This is a self-review, not an independent audit. Literature priority is provisional, including possible alternate derivations formulated as average Hamming overlap of independent Dyck paths or mean profile of Catalan excursions. The claim concerns precisely the canonical binary embedding and uniform vertices. No statement is made about uniformly sampled interior points, other embeddings, or the full distance distribution. The use of a classical elliptic singularity expansion is cited; its constant depends on the modulus convention specified above.

## References
- H. Bidkhori, *Lattice Path Matroid Polytopes*, first posted 2012-12-22, https://arxiv.org/abs/1212.5705.
- K. Knauer, L. Martínez-Sandoval, J. L. Ramírez Alfonsín, *On lattice path matroid polytopes: integer points and Ehrhart polynomial*, first posted 2017-01-19, https://arxiv.org/abs/1701.05529.
- S. An, J. Jung, S. Kim, *Facial structures of lattice path matroid polytopes*, first posted 2017-01-02, https://arxiv.org/abs/1701.00362.
- E. Cohen, P. Tetali, D. Yeliussizov, *Lattice Path Matroids: Negative Correlation and Fast Mixing*, first posted 2015-05-25, https://arxiv.org/abs/1505.06710.
- NIST Digital Library of Mathematical Functions, §19.12, elliptic-integral asymptotic expansion, https://dlmf.nist.gov/19.12.
