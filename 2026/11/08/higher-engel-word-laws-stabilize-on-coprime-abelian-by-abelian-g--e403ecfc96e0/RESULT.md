# Higher Engel word laws stabilize on coprime abelian-by-abelian groups

## Finding

Let \(A\) and \(H\) be finite abelian groups, written additively and multiplicatively respectively, with \(\gcd(|A|,|H|)=1\). Let \(H\) act on \(A\) by automorphisms, and set \(G=A\rtimes H\). For independently uniform \(X,Y\in G\), use the commutator convention \([x,y]=x^{-1}y^{-1}xy\) and the right Engel word \(W_k=[X,{}_{k}Y]\), with \(k\ge 2\). For \(v\in H\), put \(B_v=(v-1)A=\{v a-a:a\in A\}\) and \(C_v=C_A(v)\).

**Complete stabilized law.** For every integer \(k\ge2\) and every \(a\in A\),
\[
\boxed{\Pr(W_k=a)=\frac1{|H|}\sum_{\substack{v\in H\\a\in B_v}}\frac1{|B_v|}.}
\]
All output values lie in \(A\). The entire distribution, not just its identity probability, is independent of \(k\) once \(k\ge2\). More strongly, conditional on the whole element \(Y=(b,v)\) and on the \(H\)-coordinate of \(X\), the variable \(W_k\) is exactly uniform on \(B_v\).

**Fourier and orbit formulas.** Let \(\widehat A\) be the complex character group of \(A\). For every \(\chi\in\widehat A\),
\[
\boxed{\mathbb E[\chi(W_k)]=\frac{|\{v\in H:\chi\circ v=\chi\}|}{|H|}.}
\]
In particular, with \(H\backslash A\) denoting the orbit set for the given action,
\[
\boxed{\Pr(W_k=1_G)=\frac{|H\backslash A|}{|A|}.}
\]
This probability obeys the sharp bound
\[
\boxed{\Pr(W_k=1_G)\ge\frac{|A|+|H|-1}{|A||H|},}
\]
with equality precisely when \(C_v=\{0\}\) for every nonidentity \(v\in H\). If \(A\ne\{0\}\) and \(|H|>1\), this equality condition is the fixed-point-free, Frobenius-action condition.

**Engelizer description.** For any \(y=(b,v)\in G\), the set
\[
E_k(y)=\{x\in G:[x,{}_{k}y]=1_G\}
\]
is the same for all \(k\ge2\) and has exactly \(|H||C_v|\) elements. Explicitly, under the canonical direct sum \(A=C_v\oplus B_v\), write \(b=b_C+b_B\) and choose the unique \(t\in B_v\) with \((v-1)t=b_B\). Then
\[
\boxed{E_k(y)=(-t,1_H)\,(C_v\rtimes H)\,(t,1_H).}
\]
This formula specifies the location of each Engelizer, not merely whether it is a subgroup. Subgroup closure for metabelian Engelizers is known and is not asserted to be new.

## Assumptions and scope

The groups \(A\) and \(H\) may be trivial, need not be cyclic, and need not act faithfully. A group element is written \((a,u)\), with multiplication \((a,u)(b,v)=(a+u b,uv)\). The equality \(W_k=a\) means \(W_k=(a,1_H)\). The index \(k\) counts occurrences of the repeated right argument; thus \(W_2=[[X,Y],Y]\). The hypothesis \(\gcd(|A|,|H|)=1\) is essential to the universal stabilization statement, and is not relaxed silently. All finite sums and probabilities are exact.

## Proof

**1. The commutator and the iterated word.** Direct multiplication using the displayed group law, and the fact that \(u\) and \(v\) commute, gives
\[
[(a,u),(b,v)]=\bigl(u^{-1}v^{-1}((1-v)a+(u-1)b),1_H\bigr).
\]
For \(z\in A\), \([(z,1_H),(b,v)]=((v^{-1}-1)z,1_H)\). Consequently for every \(k\ge1\),
\[
[(a,u),{}_{k}(b,v)]
=\left((v^{-1}-1)^{k-1}u^{-1}v^{-1}\bigl((1-v)a+(u-1)b\bigr),1_H\right).
\]
For \(k=1\) the exponent-zero factor is the identity map.

**2. Coprime decomposition.** Fix \(v\in H\) of order \(m\). Multiplication by \(m\) is an automorphism of \(A\), because \(m\mid |H|\) and \(\gcd(|A|,|H|)=1\). Thus the averaging operator
\[
P=\frac1m(1+v+\cdots+v^{m-1})
\]
is a well-defined endomorphism of the finite abelian group \(A\). Here \(1/m\) denotes the inverse of the multiplication-by-\(m\) automorphism. One has \(P^2=P\), \(\operatorname{im}P=C_v\), and \(\ker P=(v-1)A=B_v\). For the final identity, \(P(v-1)=0\) and, on \(\ker P\), the polynomial relation \(1-P\in(v-1)\mathbb Z[1/m][v]\) supplies a preimage; alternatively the usual cyclic averaging telescoping identity proves it. Hence
\[
A=C_v\oplus B_v,
\]
and \(v-1\) and \(v^{-1}-1\) restrict to automorphisms of \(B_v\): their kernels on \(B_v\) intersect \(C_v\) trivially, and \(B_v\) is finite.

**3. Conditional uniformity and stabilization.** Fix \(Y=(b,v)\) and \(u\in H\). As \(a\) varies uniformly over \(A\), the term \((1-v)a\) varies uniformly over \(B_v\), with every value appearing \(|C_v|\) times. For \(k\ge2\), application of the factor \((v^{-1}-1)^{k-1}\) annihilates the \(C_v\)-component of the constant term \((u-1)b\) and maps \(B_v\) bijectively to itself; the other factors \(u^{-1}v^{-1}\) preserve \(B_v\) since the action of \(H\) is abelian. The conditional distribution of \(W_k\) is therefore uniform on \(B_v\), independently of \(b,u,k\). Averaging over uniform \(v\in H\) gives the complete displayed law.

**4. Fourier transform and identity probability.** For any character \(\chi\), character orthogonality on the subgroup \(B_v\) yields \(|B_v|^{-1}\sum_{z\in B_v}\chi(z)=1\) if \(\chi\) vanishes on \(B_v\), and \(0\) otherwise. Vanishing is equivalent to \(\chi\circ v=\chi\); this proves the Fourier formula. At the identity,
\[
\Pr(W_k=1_G)=\frac1{|H|}\sum_{v\in H}\frac1{|B_v|}
=\frac1{|A||H|}\sum_{v\in H}|C_v|.
\]
Burnside's orbit-counting lemma identifies the last sum divided by \(|H|\) with \(|H\backslash A|\). Since \(C_1=A\) and every other \(C_v\) contains zero, the claimed lower bound follows. Equality is equivalent to \(|C_v|=1\) for all \(v\ne1\), proving sharpness and the equality characterization.

**5. Exact Engelizer.** The last nonidentity factor in the explicit word expression is invertible on \(B_v\) and annihilates \(C_v\). Thus for all \(k\ge2\),
\[
[(a,u),{}_{k}(b,v)]=1_G\iff (v-1)a_B=(u-1)b_B,
\]
where \(a_B,b_B\) are the \(B_v\)-components. As \(v-1\) and \(u-1\) commute, putting \(b_B=(v-1)t\) gives \(a_B=(u-1)t\). The \(C_v\)-coordinate \(a_C\) is arbitrary. Therefore the solutions are \((a_C+(u-1)t,u)\) for \(a_C\in C_v\) and \(u\in H\), exactly the indicated conjugate of \(C_v\rtimes H\). The cardinality and independence of \(k\) follow.

**6. Necessity of a genuine hypothesis.** Coprimality cannot simply be dropped. In the dihedral group \(C_8\rtimes C_2\) with inversion action, exhaustive exact counting gives \(\Pr(W_2=1_G)=3/4\) but \(\Pr(W_3=1_G)=1\). Indeed \(v-1\) is multiplication by \(-2\) on \(C_8\), which is not invertible on its image and becomes nilpotent after further iterations. Thus higher Engel distributions need not stabilize at depth two without coprimality.

## Verification

The standalone checker `verify.py` constructs ten finite abelian-by-abelian semidirect products including noncyclic complements, cyclic/noncyclic kernels, nonfaithful and non-Frobenius actions, and a non-diagonal irreducible action. It computes every ordered pair of group elements at depths \(k=2,3,4\), checking the complete value distributions against the theorem, conditional support and fiber sizes for every fixed complement coordinate and right element, Engelizer sizes and subgroup closure, the Fourier coefficients against independent word counts, and the Burnside and sharp-bound formulas. It also exhaustively checks the noncoprime dihedral boundary example. The fixed case set produces exactly `464790` direct word evaluations and `3884` conditional-fiber checks and terminates in `VERIFY_OK`; its recorded output is in `verification_output.txt`. The Fourier comparison uses complex roots of unity with absolute tolerance \(10^{-10}\); the full value-law and subgroup tests are integer or exact-rational checks. This finite verification supplements, but does not replace, the universal argument above.

As a sample outside the Frobenius family, \(A=C_7\times C_7\) and \(H=C_2\times C_3\) acting independently and faithfully on the two coordinates has \(\Pr(W_k=1_G)=12/49\) for all \(k\ge2\). A second non-Frobenius case, \(A=C_3\times C_3\) and \(H=C_2\times C_2\), has probability \(4/9\).

## Relationship to prior work

Putignano and Vannacci, *Comparing word probabilities in finite groups* (arXiv:2610.23100, first public 16 October 2026), motivate quantitative Engel word probabilities and compare them to cube-word probabilities by analytic and extremal methods. Their results do not supply this explicit conditional word-value law for coprime abelian-by-abelian extensions.

Erfanian and Farrokhi (2013) develop general upper and lower bounds for the \(2\)-Engel degree and establish that the relevant Engelizers are subgroups for metabelian groups. Their subgroup assertion is strictly included in the present case and is expressly credited, not claimed as new. Their bounds and examples do not specify all value fibers, the exact Fourier law, or the Burnside orbit formula for all split coprime abelian-by-abelian groups.

Jafarian Amiri and Rostami (2019) study the probability of *some* Engel depth and classify Engelizers for selected almost simple groups, especially Suzuki and special linear groups. This differs from the fixed-depth law and the split metabelian class here.

An accessible earlier theorem on directed Engel graphs of abelian-kernel **cyclic Frobenius groups** classifies which pairs eventually annihilate and observes depth-two stabilization of the adjacency relation in that narrower class. It does not classify the distribution of the nonidentity word values and does not handle arbitrary abelian, potentially non-Frobenius semidirect actions. In particular, it does not imply the exact Fourier or orbit law across the class in this theorem. Earlier exact \(2\)-Engel laws on unitriangular groups concern different, nilpotent groups with nonabelian kernels and do not yield this theorem.

## Limitations

The claim requires a finite abelian normal subgroup, an abelian complement, and coprime orders. It does not assert a corresponding law for arbitrary metabelian groups, arbitrary extensions, or noncoprime semidirect products. Equal distributions for \(k\ge2\) do not mean the words themselves are equal as functions on pairs. No independence from an individual complement coordinate is asserted: the distribution conditional on that coordinate is on \(B_v\), and different coordinates may give different supports. Uniqueness of the theorem in all historical literature is not formally established; alternative presentations in older character-theoretic or Engel-probability papers remain a priority risk. The numerical verification is finite and is not offered as an infinite certificate.

## References

1. L. Putignano and M. Vannacci, “Comparing word probabilities in finite groups,” arXiv:2610.23100v1, first public 2026-10-16, https://arxiv.org/abs/2610.23100.
2. A. Erfanian and M. Farrokhi D. G., “On the probability of being a 2-Engel group,” *International Journal of Group Theory* 2(4) (2013), 31–38; author-uploaded full text https://www.researchgate.net/publication/288650599_On_the_probability_of_being_a_2-Engel_group.
3. S. M. Jafarian Amiri and H. Rostami, “The Probability That an Ordered Pair of Elements is an Engel Pair,” *Journal of the Indonesian Mathematical Society* 25(2) (2019), 121–127, https://media.neliti.com/media/publications/440132-the-probability-that-an-ordered-pair-of-f8d88df8.pdf.
4. “Engel digraphs of abelian-kernel cyclic Frobenius groups,” accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-engel-digraphs-of-abelian-kernel-cyclic-frobenius-groups--1e7e2c91abea.
