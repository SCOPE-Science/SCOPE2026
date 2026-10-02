# Serial group algebras of symmetric wreath products

## Statement

Let \(A\) be a finite group, let \(n\ge 2\), let \(F\) be a field of
characteristic \(p>0\), and write
\[
A\wr S_n=A^n\rtimes S_n
\]
for the standard wreath product in which \(S_n\) permutes the \(n\) factors.

**Theorem.**
\[
F[A\wr S_n]\text{ is serial}
\quad\Longleftrightarrow\quad
p\nmid |A|\ \text{ and }\ FS_n\text{ is serial}.
\]
Equivalently,
\[
F[A\wr S_n]\text{ is serial}
\]
if and only if \(p\nmid |A|\) and one of the following holds:
\[
n<p,\qquad
p=2\text{ and }2\le n\le3,\qquad
p=3\text{ and }3\le n\le5.
\]

In characteristic \(0\), every finite group algebra is semisimple and hence serial.

A useful algebraic form of the argument is the following. If \(k\) is algebraically
closed, \(B\) is a finite-dimensional split semisimple \(k\)-algebra, and
\[
B\wr S_n:=B^{\otimes n}\rtimes kS_n,
\]
then
\[
B\wr S_n\text{ is serial}\quad\Longleftrightarrow\quad kS_n\text{ is serial}.
\]

## Proof

Seriality of finite group algebras depends only on the characteristic of the
coefficient field, so it is enough to work over an algebraic closure \(k\) of \(F\).

### 1. Two necessary conditions

If \(p\mid |A|\), let \(P\ne1\) be a Sylow \(p\)-subgroup of \(A\).
Because \(n\ge2\), the base subgroup \(A^n\) contains \(P^n\), which is
noncyclic. Hence a Sylow \(p\)-subgroup of \(A\wr S_n\) is noncyclic.
Higman's finite-representation-type criterion therefore rules out seriality.

There is also a quotient
\[
A\wr S_n\twoheadrightarrow S_n.
\]
Factor rings of serial rings are serial, so seriality of
\(k[A\wr S_n]\) forces seriality of \(kS_n\).

Thus only the case \(p\nmid |A|\) and serial \(kS_n\) remains.

### 2. Semisimple-base wreath products

Let
\[
B\cong \prod_{i=1}^t M_{d_i}(k)
\]
be split semisimple, with central primitive idempotents \(e_1,\ldots,e_t\).
For a word
\(\mathbf i=(i_1,\ldots,i_n)\in\{1,\ldots,t\}^n\), put
\[
e_{\mathbf i}=e_{i_1}\otimes\cdots\otimes e_{i_n}\in B^{\otimes n}.
\]
The symmetric group permutes these idempotents. Its orbits are indexed by
multiplicity vectors
\[
\mathbf n=(n_1,\ldots,n_t),\qquad n_i\ge0,\qquad \sum_i n_i=n.
\]

Fix one such orbit and a representative \(e=e_{\mathbf i}\).
The sum of all conjugates of \(e\) is a central idempotent of
\(B\wr S_n\), and \(e\) is full in the corresponding component.
The stabilizer of \(e\) is the Young subgroup
\[
H_{\mathbf n}=S_{n_1}\times\cdots\times S_{n_t}.
\]
Consequently that component is Morita equivalent to
\[
e(B\wr S_n)e
 \cong (eB^{\otimes n}e)\rtimes kH_{\mathbf n}.
\]

If \(V_i=k^{d_i}\), then
\[
eB^{\otimes n}e
 \cong \operatorname{End}_k\!\left(
 \bigotimes_i V_i^{\otimes n_i}\right).
\]
The action of \(H_{\mathbf n}\) is permutation of equal tensor factors.
It is inner, implemented by the genuine place-permutation representation
on
\[
W_{\mathbf n}=\bigotimes_i V_i^{\otimes n_i}.
\]
Therefore
\[
\operatorname{End}_k(W_{\mathbf n})\rtimes kH_{\mathbf n}
 \cong
\operatorname{End}_k(W_{\mathbf n})\otimes kH_{\mathbf n}.
\]
Hence
\[
B\wr S_n
\ \text{is Morita equivalent to}\
\prod_{\mathbf n:\,\sum n_i=n}
k[S_{n_1}\times\cdots\times S_{n_t}].
\tag{1}
\]

Seriality is Morita invariant and is componentwise for finite direct products.
The multiplicity vector \((n,0,\ldots,0)\) already gives a component Morita
equivalent to \(kS_n\), proving the necessary direction of the semisimple-base
statement. Thus it remains to examine these Young-subgroup algebras for
sufficiency.

### 3. The symmetric-group input

For completeness, the needed classification of \(kS_m\) can be recovered from
standard cyclic-defect facts.

If \(m<p\), Maschke's theorem makes \(kS_m\) semisimple, hence serial.
If \(m\ge2p\), \(S_m\) contains two disjoint \(p\)-cycles, so its Sylow
\(p\)-subgroup is noncyclic and \(kS_m\) is not serial.

Suppose
\[
p\le m<2p.
\]
Then the Sylow \(p\)-subgroups are cyclic of order \(p\).
Every positive-defect block of a symmetric group with cyclic defect has Brauer
tree a line with \(p-1\) edges and no exceptional vertex. A cyclic-defect block is
serial exactly when its Brauer tree is a star with the exceptional vertex, if
present, at the center. A line with \(p-1\) edges is a star precisely for
\(p=2\) or \(p=3\). Hence
\[
kS_m\text{ is serial}
\Longleftrightarrow
m<p,\ \text{or }(p=2,\ 2\le m\le3),\ \text{or }(p=3,\ 3\le m\le5).
\tag{2}
\]

This agrees with the dedicated classification of alternating and symmetric
group rings by Kukharev and Puninski.

### 4. Sufficiency for the wreath product

Assume now that \(kS_n\) is serial.

If \(n<p\), every part \(n_i\) of every multiplicity vector satisfies
\(n_i<p\). Hence every \(kS_{n_i}\) is semisimple, so every algebra on the
right-hand side of (1) is semisimple.

If \(p=2\) and \(n\le3\), at most one part \(n_i\) is at least \(2\).
That factor is \(S_2\) or \(S_3\), whose group algebra is serial by (2);
all remaining factors are semisimple. Tensoring with split semisimple
algebras only produces finite products of matrix algebras over the serial
factor, so the Young-subgroup algebra is serial.

If \(p=3\) and \(n\le5\), at most one part \(n_i\) is at least \(3\).
That factor is one of \(S_3,S_4,S_5\), each serial by (2), while all other
factors are semisimple. Again every Young-subgroup algebra in (1) is serial.

Thus \(B\wr S_n\) is serial whenever \(kS_n\) is serial. Taking
\(B=kA\), which is split semisimple because \(p\nmid |A|\), proves the theorem.

## Consequences

For the generalized symmetric groups
\[
G(m,1,n)=C_m\wr S_n,
\]
the modular group algebra in characteristic \(p\) is serial exactly when
\(p\nmid m\) and the displayed symmetric-group condition holds.

For the hyperoctahedral group \(C_2\wr S_n\), the only nonsemisimple serial
cases with \(n\ge2\) occur in characteristic \(3\), for
\[
n=3,4,5.
\]
In particular,
\[
F[C_2\wr S_5]
\]
is serial in characteristic \(3\). More generally, for every finite
\(3'\)-group \(A\),
\[
F[A\wr S_5]
\]
is serial in characteristic \(3\). These groups have quotient \(S_5\), so
they are not \(3\)-solvable. Thus the theorem supplies an infinite family of
non-\(3\)-solvable groups with serial modular group algebras, complementing the
classical sufficient theorem for \(p\)-solvable groups with cyclic Sylow
\(p\)-subgroups.

## Relation to prior work

Kukharev and Puninski proved that a finite \(p\)-solvable group with cyclic
Sylow \(p\)-subgroup has serial group algebra, and their later work develops the
general classification problem for serial finite group algebras. Their 2014
paper specifically treats alternating and symmetric groups. Volkov, Kukharev
and Puninski proved that seriality depends only on the characteristic of the
field.

The cyclic-defect facts used above are standard: a block with cyclic defect is
controlled by its Brauer tree, and a group algebra with cyclic Sylow
\(p\)-subgroups is serial exactly when all its block trees are stars with the
exceptional vertex at the center. For symmetric groups, cyclic-defect Brauer
trees are lines with \(p-1\) edges and no exceptional vertex.

Morita equivalences for wreath products are also a developed subject; equation
(1) is the elementary semisimple-base orbit-and-corner reduction needed here.
The claimed contribution is the resulting complete seriality classification
for finite-base symmetric wreath products and, in particular, the
characteristic-\(3\) non-\(3\)-solvable family above.

## Limitations

Originality is asserted only to the best of our knowledge. Targeted searches
for serial group rings/algebras together with wreath products, generalized
symmetric groups, hyperoctahedral groups, signed symmetric groups and
\(G(m,1,n)\) did not locate this classification. The main residual risk is that
the conclusion is a short consequence of standard wreath-product Morita
methods combined with the known symmetric-group classification, and could
therefore exist implicitly or under different terminology in unindexed
literature.

The theorem is stated for the standard finite wreath product
\(A^n\rtimes S_n\) and \(n\ge2\). It does not classify arbitrary permutation
wreath products or the case \(n=1\), where the question is simply seriality of
\(FA\).

## References

1. A. V. Kukharev and G. E. Puninski, *Serial group rings of finite groups:
   \(p\)-solvability*, Algebra and Discrete Mathematics 16 (2013), 201--216.
   https://admjournal.luguniv.edu.ua/index.php/adm/article/view/1157

2. A. V. Kukharev and G. E. Puninski, *Serial group rings of finite groups:
   \(p\)-nilpotency*, Zap. Nauchn. Sem. POMI 413 (2013), 134--152;
   J. Math. Sci. 202 (2014), 422--433.
   https://www.mathnet.ru/eng/znsl5661

3. A. V. Kukharev and G. E. Puninski, *The seriality of group rings of
   alternating and symmetric groups*, Vestnik BGU, Mathematics and Informatics
   series 2 (2014), 61--64. Bibliographic record reproduced in:
   https://geodesic.mathdoc.fr/item/ADM_2015_20_1_a8/

4. Yu. V. Volkov, A. V. Kukharev and G. E. Puninski, *The seriality of the group
   ring of a finite group depends only on the characteristic of the field*,
   Zap. Nauchn. Sem. POMI 423 (2014), 57--66; J. Math. Sci. 209 (2015), 515--521.
   https://doi.org/10.1007/s10958-015-2509-z

5. A. V. Kukharev and G. E. Puninski, *When the group ring of a finite group
   over a field is serial*, arXiv:1701.03579.
   https://arxiv.org/abs/1701.03579

6. D. A. Craven, *Representation Theory of Finite Groups: a Guidebook*,
   Springer, 2019, Chapter 5 (cyclic-defect Brauer trees).
   https://doi.org/10.1007/978-3-030-21792-1_5

7. V.-A. Minuță, *Group graded Morita equivalences for wreath products*,
   Studia Univ. Babeș-Bolyai Math. 66 (2021), 417--429.
   https://doi.org/10.24193/subbmath.2021.3.01
