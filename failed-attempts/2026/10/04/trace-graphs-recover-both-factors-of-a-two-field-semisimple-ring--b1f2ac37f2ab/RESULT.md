# Trace graphs recover both factors of a two-field semisimple ring

## Finding

Let \(q,r\) be prime powers and \(n\ge2\). Put
\[
N=n^2,\qquad P=qr,
\]
and let
\[
G_{n;q,r}
=
\Gamma_t\!\left(M_n(\mathbf F_q\times\mathbf F_r)\right).
\]
Using
\[
M_n(\mathbf F_q\times\mathbf F_r)
\cong
M_n(\mathbf F_q)\times M_n(\mathbf F_r),
\]
write a vertex as \(X=(A,B)\).

Then
\[
\boxed{|V(G_{n;q,r})|=P^N-1.}
\]
If
\[
B_0=P^{N-1},
\]
then the exact set of distinct vertex degrees is
\[
\boxed{
\{B_0s-2,\ B_0s-1:s\in\{1,q,r\}\},
}
\]
with repetitions removed when \(q=r\). Thus
\[
\boxed{\delta(G_{n;q,r})=B_0-2.}
\]

More explicitly:

- if \(A\ne0\) and \(B\ne0\), the degree is \(B_0-2\) when \(\operatorname{tr}(A^2)=\operatorname{tr}(B^2)=0\), and \(B_0-1\) otherwise;
- if \(A=0\) and \(B\ne0\), the degree is \(qB_0-2\) when \(\operatorname{tr}(B^2)=0\), and \(qB_0-1\) otherwise;
- if \(A\ne0\) and \(B=0\), the degree is \(rB_0-2\) when \(\operatorname{tr}(A^2)=0\), and \(rB_0-1\) otherwise.

Every displayed value actually occurs.

The degree fingerprint reconstructs the two simple factors. If \(G\) is known to belong to this family, let
\[
v=|V(G)|,\qquad
\delta=\delta(G),\qquad
D=\{\deg_G(x):x\in V(G)\}.
\]
Then
\[
B_0=\delta+2,
\qquad
P=\frac{v+1}{B_0},
\]
and
\[
\boxed{
\{1,q,r\}
=
\left\{
\frac{d+2}{B_0}:
d\in D,\ B_0\mid(d+2)
\right\}.
}
\]
The equality here is as sets. If the recovered set has only two elements, then \(q=r\), because \(P=qr\) is already known.

Moreover \(N\) is the unique positive integer satisfying
\[
v+1=P^N,
\]
and hence
\[
n=\sqrt N.
\]

Consequently, for prime powers \(q,r,s,t\) and integers \(n,m\ge2\),
\[
\boxed{
\Gamma_t\!\left(M_n(\mathbf F_q\times\mathbf F_r)\right)
\cong
\Gamma_t\!\left(M_m(\mathbf F_s\times\mathbf F_t)\right)
}
\]
if and only if
\[
\boxed{
n=m
\quad\text{and}\quad
\{q,r\}_{\mathrm{multi}}=\{s,t\}_{\mathrm{multi}}.
}
\]

Thus, within the two-field semisimple class, the trace graph recovers the underlying product ring up to swapping its two field factors.

## Assumptions and scope

For a commutative ring \(R\) and \(n\ge2\), the trace graph
\[
\Gamma_t(M_n(R))
\]
has all nonzero matrices as vertices, with two distinct matrices adjacent exactly when
\[
\operatorname{Tr}(XY)=0.
\]

The theorem concerns a product of exactly two finite fields and equal matrix sizes on the two factors. It does not claim an analogous reconstruction theorem for arbitrary finite commutative rings or for products with different matrix sizes.

Finite fields are determined up to isomorphism by their order, so recovering the unordered pair \(\{q,r\}_{\mathrm{multi}}\) recovers the unordered pair of field factors.

## Proof

Identify
\[
M_n(\mathbf F_q\times\mathbf F_r)
\]
with
\[
M_n(\mathbf F_q)\times M_n(\mathbf F_r).
\]
For
\[
X=(A,B),\qquad
Y=(C,D),
\]
the trace is componentwise:
\[
\operatorname{Tr}(XY)
=
\bigl(\operatorname{tr}(AC),\operatorname{tr}(BD)\bigr).
\]
Hence \(X\) and \(Y\) are adjacent exactly when
\[
\operatorname{tr}(AC)=0
\quad\text{and}\quad
\operatorname{tr}(BD)=0.
\]

For a finite field \(\mathbf F_u\), the bilinear pairing
\[
\langle A,C\rangle=\operatorname{tr}(AC)
\]
on \(M_n(\mathbf F_u)\) is nondegenerate. Indeed, if \(A=(a_{ij})\ne0\), choose \(a_{ij}\ne0\). Then
\[
\operatorname{tr}(AE_{ji})=a_{ij}\ne0.
\]
Therefore, for nonzero \(A\), the kernel of
\[
C\longmapsto\operatorname{tr}(AC)
\]
has exactly
\[
u^{N-1}
\]
elements, whereas for \(A=0\) the kernel has \(u^N\) elements.

Now fix \(X=(A,B)\ne(0,0)\). The number of \(Y=(C,D)\), including \(Y=0\), satisfying the two trace equations is the product of the two kernel sizes.

If \(A\ne0\) and \(B\ne0\), this number is
\[
q^{N-1}r^{N-1}=P^{N-1}=B_0.
\]
After deleting \(Y=0\), and deleting \(Y=X\) exactly when \(X\) is self-orthogonal, the degree is
\[
B_0-1
\]
or
\[
B_0-2.
\]
Self-orthogonality is equivalent to
\[
\operatorname{tr}(A^2)=0
\quad\text{and}\quad
\operatorname{tr}(B^2)=0.
\]

If \(A=0\) and \(B\ne0\), the number of solutions before deleting vertices is
\[
q^Nr^{N-1}=qB_0,
\]
so the degree is
\[
qB_0-1
\]
or
\[
qB_0-2
\]
according as
\[
\operatorname{tr}(B^2)\ne0
\quad\text{or}\quad
\operatorname{tr}(B^2)=0.
\]
Similarly, when \(A\ne0\) and \(B=0\), the two possibilities are
\[
rB_0-1
\quad\text{and}\quad
rB_0-2.
\]

All six formal degree values occur before duplicate collapsing. Because \(n\ge2\), the matrix unit
\[
E_{12}
\]
is nonzero and satisfies
\[
\operatorname{tr}(E_{12}^2)=0,
\]
while
\[
E_{11}
\]
satisfies
\[
\operatorname{tr}(E_{11}^2)=1.
\]
Using these matrices independently in the nonzero components realizes both self-orthogonal and non-self-orthogonal vertices in every support type.

Since \(q,r\ge2\), the minimum of the degree set is
\[
B_0-2,
\]
so the graph recovers
\[
B_0=\delta+2.
\]
The vertex count gives
\[
v+1=P^N.
\]
Dividing by
\[
B_0=P^{N-1}
\]
gives
\[
P=\frac{v+1}{B_0}.
\]

For a degree
\[
d=B_0s-2,
\]
where
\[
s\in\{1,q,r\},
\]
we have
\[
\frac{d+2}{B_0}=s.
\]
For the companion degree
\[
d=B_0s-1,
\]
the quantity
\[
\frac{d+2}{B_0}
=
s+\frac1{B_0}
\]
is not an integer. Hence the divisibility filter
\[
B_0\mid(d+2)
\]
extracts exactly
\[
\{1,q,r\}.
\]
If \(q=r\), the set records one repeated field order only once, but \(P=q^2\) identifies this as the equal-factor case.

Finally, \(P\ge4\), so the equation
\[
v+1=P^N
\]
recovers \(N\) uniquely, and the family hypothesis gives
\[
n=\sqrt N.
\]

Thus a graph isomorphism between two members of the family forces equality of \(n\) and equality of the unordered field-order multisets. Conversely, if those data agree, the corresponding finite fields are isomorphic, and after possibly swapping factors the induced ring isomorphism preserves trace and therefore induces a trace-graph isomorphism.

## Verification

The included replay independently constructs the trace pairing on \(2\times2\) matrices over
\[
\mathbf F_2,\ \mathbf F_3,\ \mathbf F_4,\ \mathbf F_5.
\]
The field \(\mathbf F_4\) is implemented as
\[
\mathbf F_2[t]/(t^2+t+1).
\]

For each field, the replay enumerates every matrix and directly counts the kernel of every trace functional
\[
C\longmapsto\operatorname{tr}(AC).
\]
It checks that the kernel has size \(u^4\) for \(A=0\) and \(u^3\) for every nonzero \(A\).

It then checks the full degree multiset obtained from these independently enumerated kernels for the factor pairs
\[
(2,2),\ (2,3),\ (2,4),\ (3,4),\ (3,5).
\]
For each pair it verifies:

- the exact degree set;
- the minimum-degree formula;
- recovery of \(qr\) from graph order and minimum degree;
- recovery of the unordered two-factor field orders from the divisibility fingerprint;
- recovery of \(n=2\).

The checker also verifies directly that both square-trace types occur in every tested field via the expected matrix-unit witnesses.

The replay returns `VERIFY_OK`.

Finite enumeration is not used to prove the theorem.

## Relationship to prior work

The 2024 survey *Graphs from matrices - a survey* explicitly poses as Problem 1 the study of the trace graph of
\[
M_n(R)\times M_n(S)
\]
for two commutative rings. The present theorem gives an exact reconstruction result for the first semisimple case
\[
R=\mathbf F_q,\qquad S=\mathbf F_r.
\]

The same survey quotes the general degree formula of Almahdi, Louartiti, and Tamekkante: for a finite commutative ring \(R\), the degree of a vertex is determined by the size of the ideal generated by its entries and by whether it is self-orthogonal. That general formula supplies a prior framework for degree computations. The novelty claimed here is not the existence of such a degree formula; it is the exact three-support degree fingerprint for a two-field product and the resulting recovery of both field orders.

The survey also quotes a 2021 isomorphism theorem: if two finite-ring trace graphs are isomorphic, then their underlying rings have the same cardinality and their matrix sizes agree. For
\[
\mathbf F_q\times\mathbf F_r,
\]
that theorem recovers only the product
\[
qr.
\]
The degree fingerprint above separates the two factors and proves the stronger if-and-only-if classification within this semisimple family.

Targeted searches using “trace graph”, “direct product”, “product of fields”, “matrix rings”, “degree set”, and “isomorphism” terminology did not locate this factor-recovery theorem.

## Limitations

The theorem assumes exactly two field factors and a common matrix size \(n\). Products of three or more fields can have many support strata; reconstructing all factor orders requires a separate argument.

The prior general degree formula makes the local degree calculation compatible with established trace-graph theory. The new content is the global use of the complete degree set to reconstruct the two semisimple factors.

The full texts of the 2018 and 2021 Springer articles were not available through the public full-text routes checked here. Their relevant statements were independently inspected as reproduced in full in the 2024 survey. This leaves a residual bibliographic risk that one of those articles contains an equivalent consequence not highlighted by the survey.

Failed literature searches do not prove novelty.

## References

1. T. Tamizh Chelvam, “Graphs from matrices - a survey,” published online 2 April 2024, DOI 10.1080/09728600.2024.2332780. Primary MSC 16S50.
2. F. A. A. Almahdi, K. Louartiti, and M. Tamekkante, “The trace graph of the matrix ring over a finite commutative ring,” *Acta Mathematica Hungarica* 156 (2018), 132–144, DOI 10.1007/s10474-018-0815-x.
3. T. Tamizh Chelvam and M. Sivagami, “On trace graph of matrices over fields,” *Beiträge zur Algebra und Geometrie* 63 (2022), 217–231, DOI 10.1007/s13366-021-00561-8.
