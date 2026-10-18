# Factorial census of fundamental preconditionals on finite chains
## Finding

Let
\[
C_n=\{c_0<c_1<\cdots<c_{n-1}\}
\]
be the \(n\)-element bounded chain, with
\[
n\ge2.
\]

Chen's systems distinguish \(\mathsf T\)-algebras from \(\mathsf F\)-algebras by adding double-negation inflation to the latter. On a finite chain, this distinction disappears:

\[
\boxed{
\mathsf T\text{-preconditionals on }C_n
=
\mathsf F\text{-preconditionals on }C_n.
}
\]

Moreover, their exact number is

\[
\boxed{
(n-2)!.
}
\]

Since every bounded-lattice automorphism of a finite chain is the identity, this is also the number of isomorphism classes whose lattice reduct is \(C_n\).

There is an explicit parametrization. For every interior element
\[
c_j,\qquad 1\le j\le n-2,
\]
choose independently a **birth time**
\[
\tau_j\in\{j+1,j+2,\ldots,n-1\}.
\]

For antecedent \(c_i\), define the set of non-top fixed consequents
\[
F_i
=
\{c_0\}
\cup
\{c_j:1\le j<i,\ \tau_j\le i\}
\qquad(1\le i\le n-2),
\]
with
\[
F_0=\varnothing,
\qquad
F_{n-1}=\{c_0,\ldots,c_{n-2}\}.
\]

Then
\[
c_i\to c_k
\]
is the least element of
\[
F_i\cup\{c_{n-1}\}
\]
lying at or above \(c_k\).

Every \(\mathsf T\)- or \(\mathsf F\)-preconditional arises uniquely from one such birth-time vector.

Thus
\[
\#\{\mathsf F\text{-preconditionals on }C_n\}
=
\prod_{j=1}^{n-2}(n-1-j)
=
(n-2)!.
\]

All of these operations induce exactly the same negation:
\[
\neg c_0=c_{n-1},
\qquad
\neg c_i=c_0
\quad(1\le i\le n-1).
\]

Exactly one operation is the Heyting implication. It is the earliest-birth code
\[
\tau_j=j+1
\qquad(1\le j\le n-2),
\]
for which
\[
c_i\to c_k
=
\begin{cases}
c_{n-1},&c_i\le c_k,\\
c_k,&c_k<c_i.
\end{cases}
\]

Consequently the first chain on which fundamental propositional logic with a preconditional has a non-Heyting \(\mathsf F\)-algebra is
\[
C_4.
\]
Indeed the counts begin
\[
1,1,2,6,24,120,\ldots
\]
for chain sizes
\[
2,3,4,5,6,7,\ldots.
\]

## Assumptions and scope

A preconditional is a binary operation satisfying Chen's recalled axioms P1--P5. A \(\mathsf T\)-algebra additionally satisfies conditional identity
\[
a\to a=1
\]
and semicomplementation
\[
a\wedge(a\to0)=0.
\]
An \(\mathsf F\)-algebra additionally satisfies
\[
a\le\neg\neg a,
\qquad
\neg a:=a\to0.
\]

The theorem classifies all such binary operations on a fixed finite chain. It does not classify preconditionals without conditional identity and semicomplementation.

The count is simultaneously labelled and unlabelled for a fixed chain because any bounded-lattice isomorphism
\[
C_n\to C_n
\]
must preserve every position in the total order.

## Proof

Write
\[
1=c_{n-1}.
\]

Fix a \(\mathsf T\)-preconditional.

First, conditional identity and the preconditional law
\[
a\to b=a\to(a\wedge b)
\]
imply
\[
a\le b
\quad\Longrightarrow\quad
a\to b=1.
\]
Also P1 and P2 give
\[
1\to b=b.
\]

For \(a>0\), semicomplementation on a chain forces
\[
a\to0=0,
\]
because
\[
a\wedge(a\to0)=0
\]
and the only element whose meet with a positive chain element is \(0\) is \(0\). Conditional identity gives
\[
0\to0=1.
\]
Hence every \(\mathsf T\)-preconditional induces
\[
\neg0=1,
\qquad
\neg a=0\quad(a>0).
\]
Therefore
\[
a\le\neg\neg a
\]
holds automatically. Thus every \(\mathsf T\)-algebra on a chain is already an \(\mathsf F\)-algebra.

Now fix an antecedent \(a\), and consider the row map
\[
\rho_a(b)=a\to b.
\]

P2 makes \(\rho_a\) extensive below \(a\), and conditional identity makes every input at or above \(a\) map to \(1\). P3 and P4 give consequent monotonicity, so \(\rho_a\) is monotone.

P5 with its inner antecedent equal to \(a\) gives
\[
a\to(a\to b)\le a\to b.
\]
Let
\[
y=a\to b.
\]
If \(y<a\), then P2 gives
\[
y\le a\to y,
\]
hence
\[
a\to y=y.
\]
If \(y\ge a\), conditional identity forces
\[
a\to y=1,
\]
so the displayed P5 inequality implies
\[
y=1.
\]
Thus every row is idempotent:
\[
\rho_a(\rho_a(b))=\rho_a(b).
\]

Consequently each row is a closure map onto its fixed points, except that all inputs at or above the antecedent collapse to the top fixed point. In particular, for
\[
0<a<1,
\]
the non-top fixed points of \(\rho_a\) form a set
\[
F_a\subseteq\{b:b<a\}
\]
containing \(0\), and
\[
a\to b
\]
is the least element of
\[
F_a\cup\{1\}
\]
above \(b\).

The decisive restriction from P5 is nesting of these fixed-point sets. Suppose
\[
x\le a
\]
and
\[
x\to y=y<1.
\]
Using P5 with inner antecedent \(x\),
\[
a\to(x\to y)\le x\to y.
\]
Thus
\[
a\to y\le y.
\]
Since \(y<x\le a\), P2 gives the reverse inequality, so
\[
a\to y=y.
\]
Therefore
\[
F_x\subseteq F_a
\qquad(x\le a).
\]

At the top antecedent,
\[
1\to b=b,
\]
so every non-top element is eventually fixed.

Now enumerate the chain by indices. For each
\[
1\le j\le n-2,
\]
the element \(c_j\) is not fixed in row \(j\), because
\[
c_j\to c_j=1.
\]
It is fixed in the top row \(n-1\), and once it becomes fixed it remains fixed by nesting. Hence it has a unique first fixed row
\[
\tau_j\in\{j+1,\ldots,n-1\}.
\]

Conversely, choose such a number \(\tau_j\) independently for every interior \(j\). Let
\[
F_i
=
\{c_0\}
\cup
\{c_j:\tau_j\le i\}
\]
for \(1\le i\le n-2\), with the endpoint conventions stated above, and define each row by taking the least fixed point above the consequent.

Each row is monotone, extensive below its antecedent, and idempotent. The fixed sets are nested. P1 holds because the top row is the identity. P2 is extensivity. P3 follows because every consequent at or above the antecedent maps to \(1\). P4 is row monotonicity.

For P5, let
\[
x=a\wedge b.
\]
Put
\[
y=x\to c.
\]
If
\[
y=1,
\]
then
\[
a\to y=1=y.
\]
If
\[
y<1,
\]
then \(y\) is a fixed point of the \(x\)-row. Since
\[
x\le a
\]
and the fixed-point sets are nested, \(y\) is also fixed in the \(a\)-row. Hence
\[
a\to(x\to c)=a\to y=y=x\to c,
\]
which is stronger than P5.

Conditional identity and semicomplementation are built into the construction, so every birth-time code yields a \(\mathsf T\)-algebra and therefore an \(\mathsf F\)-algebra.

For each \(j\), the number of possible birth times is
\[
n-1-j.
\]
The choices are independent, so
\[
\prod_{j=1}^{n-2}(n-1-j)
=
(n-2)!.
\]

Finally, the Heyting implication on a chain fixes every consequent strictly below the antecedent. Therefore every \(c_j\) must become fixed at its earliest possible row:
\[
\tau_j=j+1.
\]
This code is unique.

## Verification

The bundled checker performs two independent finite replays.

First, it generates every birth-time code through chain size \(9\), constructs the corresponding operation, and checks P1--P5, conditional identity, semicomplementation, and double-negation inflation directly. It confirms the count
\[
(n-2)!
\]
and confirms that exactly one operation at each size is the Heyting implication.

Second, for chain sizes through \(6\), it ignores the birth-time theorem and brute-forces every operation compatible only with the immediately forced endpoint values and P2 bounds. It then filters by all five preconditional axioms plus the \(\mathsf T\)-conditions. The surviving operations agree exactly with the birth-time construction.

The brute-force counts are
\[
1,1,2,6,24
\]
for
\[
n=2,3,4,5,6.
\]

The computation is corroborative. The factorial formula for arbitrary \(n\) follows from the fixed-point birth-time proof.

## Relationship to prior work

Chen's 2026 paper defines \(\mathsf T\)- and \(\mathsf F\)-algebras, proves their algebraic and relational completeness, and establishes the finite model property. It notes that \(\mathsf F\)-algebras include all Heyting algebras and all ortholattices with the Sasaki hook.

The paper does not classify the \(\mathsf F\)-algebra structures carried by finite chains, count them, or isolate the smallest non-Heyting chain example.

Holliday's earlier axiomatic study introduces preconditionals, proves the derived negation is a precomplementation, and characterizes Heyting implication by adding modus ponens and weak monotonicity. The checked full text does not give a finite-chain census or the nested-row closure description above.

The classification shows that even when the lattice reduct and the induced negation are fixed to the ordinary finite-chain intuitionistic ones, the conditional retains factorially many possibilities. Thus the conditional enrichment has substantial finite algebraic structure that is invisible in the \(\{\wedge,\vee,\neg\}\)-reduct.

## Limitations

The theorem assumes conditional identity and semicomplementation. The larger class of bare \(\mathsf K\)-preconditionals on chains has more degrees of freedom and is not classified here.

The factorial count is specific to chain lattice reducts. General finite distributive lattices need not admit such an independent birth-time parametrization.

No claim is made about the sizes of free \(\mathsf F\)-algebras, the complexity of deciding equations on arbitrary finite \(\mathsf F\)-algebras, or the number of relational frames representing a given chain algebra.

## References

[1] Zhicheng Chen, “Fundamental Propositional Logic with Preconditional: Strong Completeness, Finite Model Property, and Modal Translations,” arXiv:2607.20221, first posted 22 July 2026.

[2] Wesley H. Holliday, “Preconditionals,” arXiv:2402.02296, first posted 3 February 2024; published in *The Logica Yearbook 2023*.

[3] Wesley H. Holliday, “A Fundamental Non-Classical Logic,” *Logics* 1(1) (2023), 36–79. DOI:10.3390/logics1010004.
