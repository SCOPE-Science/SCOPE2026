# Degree-sequence rigidity for short finite Gorenstein local algebras

## Finding
For a prime power \(q\), let \(k=\mathbb F_q\), let \(V\) have dimension \(n\ge 2\) over \(k\), and let \(B:V\times V\to k\) be a nondegenerate symmetric bilinear form. Form the commutative unital algebra \(R_B=k\oplus V\oplus kz\), with multiplication as specified below. Write \(\Gamma(R_B)\) for its *simple* zero-divisor graph, whose vertices are the nonzero zero divisors and whose edges join distinct vertices having zero product.

**Theorem.** The degree multiset of \(\Gamma(R_B)\) determines the unital ring-isomorphism type of \(R_B\), even when the field size and vector-space dimension are not supplied. Consequently, for any two algebras in this family, the following are equivalent: their zero-divisor graphs are isomorphic; their graphs have the same degree multiset; and the algebras are isomorphic as unital rings.

More precisely, set \(I_B=|\{v\in V:B(v,v)=0\}|\), including the zero vector. The complete degree distribution is
\[
\begin{array}{c|c}
\text{degree}&\text{multiplicity}\\\hline
q^{n+1}-2&q-1\\
q^n-2&q(I_B-1)\\
q^n-1&q(q^n-I_B).
\end{array}
\]
A zero multiplicity means that degree is absent. These three potential degrees are distinct for \(n\ge2\).

The isotropic-vector count is explicit:
\[
I_B=\begin{cases}
q^{n-1}, &q\text{ odd and }n\text{ odd},\\
q^{n-1}+\varepsilon(q-1)q^{n/2-1}, &q\text{ odd and }n\text{ even},\\
q^n, &q\text{ even and }B\text{ alternating},\\
q^{n-1}, &q\text{ even and }B\text{ not alternating}.
\end{cases}
\]
In the second case \(\varepsilon=\chi((-1)^{n/2}\det B)\in\{-1,1\}\), with \(\chi\) the quadratic character of \(k^\times\). Alternating means \(B(v,v)=0\) for every \(v\); this can occur for nondegenerate symmetric \(B\) only when \(q\) is even and \(n\) is even.

## Assumptions and scope
All finite fields, including characteristic two and extension fields, are covered. The algebra is defined by
\[
(a,u,c)(b,v,d)=(ab,av+bu,ad+bc+B(u,v)),
\]
where the last component is its coefficient of \(z\). Thus \((u,0)(v,0)=B(u,v)z\), \(zV=0\), and \(z^2=0\). The maximal ideal is \(\mathfrak m=V\oplus kz\), with \(\mathfrak m^2=kz\), \(\mathfrak m^3=0\), and socle \(kz\); these are local Gorenstein algebras of Hilbert function \((1,n,1)\).

The theorem also applies to every finite commutative *equicharacteristic* local Gorenstein ring of the same Hilbert function: its residue field \(k\) has a coefficient-field lift because the polynomial \(X^q-X\) has simple roots modulo its nilpotent maximal ideal. Choosing a \(k\)-linear complement of \(\mathfrak m^2\) in \(\mathfrak m\) produces the form \(B\). The socle condition makes \(B\) nondegenerate. The claim does not assert the same rigidity for mixed-characteristic rings or other Hilbert functions.

## Proof
**1. Degrees from annihilators.** A finite local ring has precisely the maximal-ideal elements as nonunits, hence here the nonzero zero divisors are the \(q^{n+1}-1\) nonzero vectors of \(\mathfrak m\). For \(x=u+cz\) and \(y=v+dz\) in \(\mathfrak m\),
\[
xy=B(u,v)z.
\]
If \(u=0\) and \(c\ne0\), then \(x\) annihilates all of \(\mathfrak m\) and has degree \(q^{n+1}-2\); there are \(q-1\) such vertices. If \(u\ne0\), nondegeneracy makes \(v\mapsto B(u,v)\) a nonzero linear functional. Thus exactly \(q^{n-1}\) choices for \(v\), each with \(q\) choices for \(d\), satisfy \(xy=0\). Of these \(q^n\) elements one is zero, and \(x\) itself must additionally be excluded precisely when \(B(u,u)=0\). Therefore
\[
\deg(x)=q^n-1-\mathbf1_{\{B(u,u)=0\}}.
\]
Each nonzero \(u\) gives \(q\) vertices, which yields the complete displayed table.

**2. Isotropic-vector count.** If \(q\) is odd, diagonalize \(B\) and let \(Q(u)=B(u,u)\). For a nontrivial additive character \(\psi\) of \(k\), character orthogonality gives
\[
I_B=q^{-1}\sum_{t\in k}\sum_{u\in k^n}\psi(tQ(u)).
\]
The \(t=0\) term contributes \(q^{n-1}\). For \(t\ne0\), multiplicativity of the quadratic Gauss sums gives \(\chi(t)^n\chi(\det B)G^n\), with \(G^2=\chi(-1)q\). The nonzero-\(t\) contributions cancel when \(n\) is odd and sum to \(\chi((-1)^{n/2}\det B)(q-1)q^{n/2-1}\) when \(n\) is even. For \(q\) even, the expression \(Q(u)=B(u,u)\) is additive because \(B\) is symmetric, and \(Q(au)=a^2Q(u)\). The Frobenius square map is a bijection on \(k\), so \(Q\) is either identically zero, giving \(I_B=q^n\), or a surjective Frobenius-semilinear map with kernel of size \(q^{n-1}\).

**3. Recovering the parameters.** The unique maximum degree in the table is \(q^{n+1}-2\), occurring exactly \(q-1\) times. Thus its multiplicity determines \(q\), and the vertex count \(q^{n+1}-1\) then determines \(n\). The multiplicity of degree \(q^n-2\) determines \(I_B\). In odd characteristic and even dimension, the two possible signs \(\varepsilon\) give distinct counts. In even characteristic and even dimension, the alternating and nonalternating possibilities also have distinct counts. For odd dimension there is only one similarity class in either characteristic.

**4. Recovering the algebra.** Over finite fields of odd characteristic, nondegenerate symmetric forms are classified up to isometry by dimension and determinant square class. Scaling a form by \(\lambda\in k^\times\) changes the determinant square class by \(\chi(\lambda)^n\); thus there is one *similarity* class in odd dimension, and two in even dimension, distinguished by \(\varepsilon\). Over finite fields of characteristic two, all nonalternating nondegenerate symmetric forms of given dimension are isometric, while in even dimension the nondegenerate alternating forms comprise one separate class. Hence \(q,n,I_B\) determine the similarity class of \(B\). When \(B\) and \(C\) are similar, choose an invertible \(P\) and \(\lambda\ne0\) satisfying \(C(Pu,Pv)=\lambda B(u,v)\). Then \((a,u,c)\mapsto(a,Pu,\lambda c)\) is a unital algebra isomorphism from \(R_B\) to \(R_C\). Conversely, every ring isomorphism induces a graph isomorphism and therefore equality of degree multisets. This finishes the proof.

## Verification
The standalone standard-library program `verify.py` constructs the entire simple zero-divisor graph from multiplication, independently counts its vertex degrees, and compares them with the annihilator formula. It also directly counts isotropic vectors and checks the applicable all-field formula in tested cases. It exhausts all nondegenerate symmetric matrices of dimensions two and three over \(\mathbb F_2\), all such matrices in dimension two over \(\mathbb F_3\) and \(\mathbb F_4\), and tests additional examples over \(\mathbb F_5\) and \(\mathbb F_8\). Its successful output ends with `VERIFY_OK 109`. These finite checks corroborate the proof; they do not prove the statement for all \(q\) and \(n\).

## Relationship to prior work
Arunkumar, Cameron, Kavaskar, and Tamizh Chelvam (arXiv:2207.11741; first posted 2022-07-24) studied induced-subgraph universality and related restrictions on zero-divisor graphs of finite rings. Kadu (arXiv:2010.06924, Proposition 3.6) already establishes the crucial correspondence between orthogonality of a symmetric bilinear form and products of elements in local rings with principal square-zero socle, as well as nondegeneracy in the Gorenstein case. The latter reduction and the finite-field classification of bilinear forms are prior mathematics, not claimed new here. The additional statement is that the ordinary simple graph's *degree multiset alone* reconstructs the full ring-isomorphism class throughout the stated family, with explicit all-characteristic multiplicities. See also Lebedev (arXiv:math/0601536) on characteristic-two forms, and Kadu–Tanpure (arXiv:2609.36021), whose different graph-comparison results concern associate-class and compressed graphs.

## Limitations
The rigidity is asserted only within the specified equicharacteristic Hilbert-function family, not among all finite rings. The full pairwise graph spectrum, automorphism group of the graph, and mixed-characteristic analogues are not determined. Publication priority is provisional: an unidentified general reconstruction theorem may imply this specialization. The 2024 study of three-radical-zero rings examines a different class with \(\dim_k(\mathfrak m^2)=n(n+1)/2\), rather than the one-dimensional socle here; its graph-matrix results have been compared but do not settle the stated full degree-rigidity property.

## References
1. G. Arunkumar, P. J. Cameron, T. Kavaskar, T. Tamizh Chelvam, *Induced subgraphs of zero-divisor graphs*, arXiv:2207.11741, first posted 2022-07-24.
2. G. S. Kadu, *On the problem of the finiteness of the compressed zero divisor graphs of Artinian rings*, arXiv:2010.06924, Proposition 3.6.
3. A. Lebedev, *Non-degenerate bilinear forms in characteristic 2, related contact forms, simple Lie algebras and superalgebras*, arXiv:math/0601536.
4. G. S. Kadu and V. Tanpure, *Zero divisors of Gorenstein Rings*, arXiv:2609.36021.
5. F. O. Ndago, M. O. Oduor, M. O. Ojiema, *Matrices of the Zero Divisor Graphs of Classes of 3-Radical Zero Completely Primary Finite Rings*, Science Mundi 4 (2024), 149–179, https://doi.org/10.51867/scimundi.4.maths.1.1 (full open-access PDF inspected).
