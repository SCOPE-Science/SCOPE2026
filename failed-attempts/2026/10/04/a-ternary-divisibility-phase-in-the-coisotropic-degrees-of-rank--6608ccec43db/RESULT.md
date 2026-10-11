# A ternary divisibility phase in the coisotropic degrees of rank-one \(3\)-by-\((n+1)\) matrices
## Finding
Let
\[
X_n=\mathbb P^2_{\mathbb C}\times\mathbb P^n_{\mathbb C},\qquad n\ge2,
\]
in its Segre embedding, and let \(\delta_i\) be its polar degrees in the convention
\[
\delta_0=\deg X_n.
\]
For the nonzero coisotropic hypersurfaces, these are exactly their projective degrees.

The complete nonzero polar vector is
\[
\left(
\binom{n+2}{2},
2n(n+1),
3n^2,
2(n^2-1),
\binom{n+1}{2}
\right).
\]
All higher polar degrees vanish. Its common divisor is
\[
\gcd(\delta_0,\delta_1,\delta_2,\delta_3,\delta_4)=\gcd(3,n+1).
\]
Therefore all five nonzero coisotropic degrees are divisible by \(3\) exactly when
\[
n\equiv2\pmod3.
\]
Otherwise their gcd is \(1\).

For \(n=5\) the vector is
\[
(21,60,75,48,15),
\]
with gcd \(3\); for \(n=4\) it is
\[
(15,40,48,30,10),
\]
with gcd \(1\).

## Assumptions and scope
The ground field is \(\mathbb C\), and the embedding is the standard Segre embedding of
\[
\mathbb P^2\times\mathbb P^n
\]
as the projective variety of rank-one \(3\times(n+1)\) matrices.

The polar indexing is fixed by \(\delta_0=\deg X_n\). The claim concerns the gcd of the complete nonzero polar vector, not proper subcollections.

## Proof
Let
\[
x=c_1(\mathcal O_{\mathbb P^2}(1)),\qquad y=c_1(\mathcal O_{\mathbb P^n}(1)).
\]
Then the Segre hyperplane class is
\[
H=x+y,
\]
and
\[
c(TX_n)=(1+x)^3(1+y)^{n+1}.
\]
Put \(d=n+2\) and
\[
I_j=\int_{X_n}c_j(TX_n)H^{d-j}.
\]
For a smooth projective variety the polar degrees satisfy
\[
\delta_i=\sum_{j=0}^{i}(-1)^j\binom{d-j+1}{i-j}I_j.
\]
Using
\[
\int_{X_n}x^2y^n=1
\]
and extracting the coefficient of \(x^2y^n\) from
\[
(1+x)^3(1+y)^{n+1}(x+y)^{d-j}
\]
gives
\[
\delta_0=\frac{(n+1)(n+2)}2,\qquad
\delta_1=2n(n+1),
\]
\[
\delta_2=3n^2,\qquad
\delta_3=2(n-1)(n+1),\qquad
\delta_4=\frac{n(n+1)}2.
\]

The projective dual of \(X_n\) is the determinantal variety of \(3\times(n+1)\) matrices of rank at most \(2\), whose codimension is
\[
n-1.
\]
The standard polar range is therefore
\[
0\le i\le (n+2)-(n-1)+1=4,
\]
so no further polar degree is nonzero.

Let \(G\) be the gcd of the five displayed integers. Since
\[
\delta_0-\delta_4=n+1,
\]
we have \(G\mid n+1\). Also \(G\mid3n^2\), and
\[
\gcd(n,n+1)=1,
\]
so
\[
G\mid\gcd(3,n+1).
\]
Conversely, if \(3\mid n+1\), then each of the five degrees is divisible by \(3\); if \(3\nmid n+1\), the right-hand gcd is \(1\). Hence
\[
G=\gcd(3,n+1).
\]

## Verification
The bundled checker reconstructs the first five polar degrees from the Chern-class formula for every
\[
2\le n\le500
\]
and checks the gcd identity. It also reconstructs the entire polar vector for
\[
2\le n\le40
\]
and verifies that every entry after index \(4\) vanishes.

These finite checks are regression evidence only. The infinite result is the symbolic coefficient extraction and gcd argument above.

## Relationship to prior work
Kohn proves that degrees of coisotropic hypersurfaces equal polar degrees and explains that Segre coisotropic hypersurfaces are hyperdeterminantal in origin. Later work gives explicit formulas for polar degrees of general Segre--Veronese varieties.

The present statement instead extracts the exact common prime content of the whole five-term coisotropic degree vector. Searches using Segre, rank-one matrix, polar degree, coisotropic degree, gcd, common divisor, and divisibility formulations did not locate
\[
\gcd(\delta_0,\ldots,\delta_4)=\gcd(3,n+1)
\]
or the equivalent residue-class criterion.

A nearby result for \(\mathbb P^a\times\mathbb P^b\) determines the projective-dual degree only, which is a single endpoint of the polar vector and does not imply the whole-vector gcd.

## Limitations
The result treats the natural \(3\times(n+1)\) rank-one matrix family. It does not claim the analogous formula for arbitrary
\[
\mathbb P^m\times\mathbb P^n.
\]
Proper subsets of the five nonzero degrees may have larger gcd.

Because the gcd proof is short after the explicit polar vector is known, an unindexed source could contain the same arithmetic corollary.

## References
Kathlén Kohn, *Coisotropic Hypersurfaces in Grassmannians*, arXiv:1607.05932, first submitted 20 July 2016.

Türkü Özlüm Çelik, Asgar Jamneshan, Guido Montúfar, Bernd Sturmfels, and Lorenzo Venturello, *Wasserstein distance to independence models*, Journal of Symbolic Computation 104 (2021), 855--873.

Ragni Piene, *Polar classes of singular varieties*, Annales scientifiques de l'École Normale Supérieure 11 (1978), 247--276.
