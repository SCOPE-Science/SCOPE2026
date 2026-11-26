# Rank-independent Euler characteristic and the maximal-minor degree crossover
## Finding
Let
\[
2\le m\le n,
\]
and let
\[
D_{m,n}^{\le r}\subset\mathbb P^{mn-1}
\]
be the projective determinantal variety of nonzero complex \(m\times n\) matrices of rank at most
\[
1\le r\le m-1.
\]

Then
\[
\boxed{
\chi_{\mathrm{top}}\!\left(D_{m,n}^{\le r}\right)=mn
}
\]
for every \(r\). Thus the ordinary topological Euler characteristic is completely independent of the rank bound.

For the maximal-minor locus
\[
M_{m,n}=D_{m,n}^{\le m-1},
\]
one has
\[
\boxed{
\deg M_{m,n}=\binom{n}{m-1}.
}
\]

Hence
\[
R_{m,n}
=
\frac{\deg M_{m,n}}
{\chi_{\mathrm{top}}(M_{m,n})}
=
\frac{\binom{n}{m-1}}{mn}.
\]

For \(m=2\),
\[
R_{2,n}=\frac12.
\]
For every \(m\ge3\),
\[
\boxed{
\frac{R_{m,n+1}}{R_{m,n}}
=
\frac{n}{n-m+2}>1.
}
\]
Therefore the comparison has only one transition in each fixed row \(m\).

Equality occurs exactly twice:
\[
\boxed{
\deg M_{3,7}
=
\chi_{\mathrm{top}}(M_{3,7})
=
21
}
\]
and
\[
\boxed{
\deg M_{5,7}
=
\chi_{\mathrm{top}}(M_{5,7})
=
35.
}
\]

The strict inequality
\[
\deg M_{m,n}<\chi_{\mathrm{top}}(M_{m,n})
\]
holds exactly in the following cases:
\[
m=2
\quad\text{for every }n\ge2;
\]
\[
m=3,\qquad 3\le n\le6;
\]
\[
m=4,\qquad 4\le n\le6;
\]
\[
m=5,\qquad n=5,6;
\]
and, for every
\[
m\ge6,
\]
exactly at
\[
n=m,\ m+1.
\]

In every remaining case,
\[
\deg M_{m,n}>\chi_{\mathrm{top}}(M_{m,n}).
\]

## Assumptions and scope
The base field is \(\mathbb C\). Projectivization removes the zero matrix.

The Euler statement applies to every nontrivial rank bound
\[
1\le r\le m-1.
\]
The degree comparison is specialized to the maximal-minor locus
\[
r=m-1.
\]

The projective degree is taken in the standard matrix-entry embedding
\[
D_{m,n}^{\le r}\subset\mathbb P^{mn-1}.
\]

## Proof
Choose integers
\[
u_1,\ldots,u_m,\qquad v_1,\ldots,v_n
\]
such that all sums
\[
u_i+v_j
\]
are pairwise distinct. The one-parameter torus
\[
\mathbb C^*
\]
acts on matrix coordinates by
\[
x_{ij}\longmapsto t^{u_i+v_j}x_{ij}.
\]
This action preserves every determinantal rank locus.

The fixed points in the ambient projective space are exactly the coordinate points
\[
[E_{ij}],
\]
because all coordinate weights are distinct. Every \(E_{ij}\) has rank \(1\), so for every
\[
r\ge1
\]
all \(mn\) fixed points lie in \(D_{m,n}^{\le r}\), and there are no others.

For a complex projective variety with a \(\mathbb C^*\)-action, Euler characteristic equals the Euler characteristic of the fixed locus. Therefore
\[
\chi_{\mathrm{top}}\!\left(D_{m,n}^{\le r}\right)=mn.
\]

Now consider the maximal-minor locus. On
\[
\mathbb P^{mn-1}
=
\mathbb P(\operatorname{Hom}(\mathbb C^m,\mathbb C^n))
\]
there is a universal bundle map
\[
\mathcal O(-1)^{\oplus m}
\longrightarrow
\mathcal O^{\oplus n}.
\]
Its rank-\((m-1)\) degeneracy locus is \(M_{m,n}\), of expected codimension
\[
n-m+1.
\]
The Thom--Porteous formula gives its class as
\[
c_{n-m+1}
\left(
\mathcal O^{\oplus n}
-
\mathcal O(-1)^{\oplus m}
\right).
\]
Writing \(H=c_1(\mathcal O(1))\),
\[
c\left(
\mathcal O^{\oplus n}
-
\mathcal O(-1)^{\oplus m}
\right)
=
(1-H)^{-m}.
\]
The coefficient of
\[
H^{n-m+1}
\]
is
\[
\binom{m+n-m+1-1}{n-m+1}
=
\binom{n}{m-1}.
\]
Hence
\[
\deg M_{m,n}=\binom{n}{m-1}.
\]

For fixed \(m\),
\[
R_{m,n}
=
\frac{\binom{n}{m-1}}{mn}.
\]
When \(m=2\), this is \(1/2\).

For \(m\ge3\),
\[
\frac{R_{m,n+1}}{R_{m,n}}
=
\frac{\binom{n+1}{m-1}}{\binom{n}{m-1}}
\frac{n}{n+1}
=
\frac{n}{n-m+2}>1.
\]
So one only needs a few base values:
\[
R_{m,m}=\frac1m,
\qquad
R_{m,m+1}=\frac12,
\qquad
R_{m,m+2}=\frac{m+1}{6}.
\]

For \(m\ge6\), the third quantity is already greater than \(1\), proving the stated transition after \(n=m+1\). For \(m=5\), it equals \(1\), giving \((5,7)\). For \(m=4\), it is \(5/6\), while
\[
R_{4,7}=\frac54,
\]
so there is no equality. For \(m=3\),
\[
R_{3,n}=\frac{n-1}{6},
\]
giving equality exactly at \(n=7\). This proves the complete classification.

## Verification
The bundled checker evaluates the classical generic determinantal degree product
\[
\deg D_{m,n}^{\le r}
=
\prod_{i=0}^{m-r-1}
\frac{(n+i)!\,i!}{(r+i)!(n-r+i)!}
\]
and verifies that its maximal-minor specialization equals
\[
\binom{n}{m-1}.
\]

It checks the degree--Euler classification for all
\[
2\le m\le40,\qquad m\le n\le100,
\]
and verifies the exact adjacent-\(n\) ratio.

It also checks combinatorially that a generic diagonal one-parameter action on the ambient matrix projective space has exactly \(mn\) coordinate fixed points and that all have rank \(1\).

These finite checks are regression evidence only. The infinite theorem follows from the torus fixed-point argument, Thom--Porteous, and the symbolic ratio calculation.

## Relationship to prior work
Zhang explicitly observes that all square projective determinantal rank loci have the same Euler characteristic \(n^2\), using the torus fixed points consisting of matrices with one nonzero entry. The same fixed-point argument works without change for rectangular matrices and gives the rank-independent value \(mn\).

Classical determinantal geometry gives the degree of generic rank loci, and Thom--Porteous gives the maximal-minor degree \(\binom{n}{m-1}\) directly.

The new comparison combines these two invariants over the full rectangular maximal-minor family. Targeted searches in rectangular determinantal, maximal-minor, Euler-characteristic, degree, binomial, and equality language did not locate the complete crossover or the two equality formats \((3,7)\) and \((5,7)\).

## Limitations
The degree--Euler crossover is proved only for maximal-minor loci. Interior rank loci have more complicated degree behavior and are not classified here.

The rank-independent Euler statement itself is a direct rectangular extension of a square observation already explicit in the literature.

The comparison is elementary once the fixed-point Euler value and the Thom--Porteous degree are juxtaposed, so an older or unindexed source may contain the same phase classification.

## References
Xiping Zhang, *Chern classes and Characteristic Cycles of Determinantal Varieties*, arXiv:1605.05380, first submitted 17 May 2016.

Marcello Bernardara, Michele Bolognesi, and Daniele Faenzi, *Homological Projective Duality for Determinantal Varieties*, arXiv:1410.7803, first submitted 28 October 2014.

William Fulton, *Intersection Theory*, second edition, Springer, 1998, especially the Thom--Porteous formula for degeneracy loci.
