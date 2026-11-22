# Klein-four subgroup conjugacy and exact enumerators in type-\(B\) Coxeter groups

## Finding

Let \(B_n=C_2\wr S_n\), the signed-permutation Coxeter group, for every integer \(n\ge0\). Write \(c_n\) for the number of its conjugacy classes of subgroups isomorphic to \(C_2\times C_2\), and \(v_n\) for the number of distinct such embedded subgroups. Set

\[
\begin{aligned}
P(z)&=\frac{1}{(1-z)^4(1-z^2)^6(1-z^4)},\\
T(z)&=\frac{1}{(1-z)^2(1-z^2)^3(1-z^4)^3},\\
C(z)&=\frac{1}{(1-z)(1-z^3)(1-z^4)(1-z^6)^2},\\
I(z)&=\frac{1}{(1-z)^2(1-z^2)}.
\end{aligned}
\]

Then the two complete enumerators are

\[
\boxed{\sum_{n\ge0}c_nz^n=\frac{P(z)+3T(z)+2C(z)}6-I(z)}
\]

and

\[
\boxed{\sum_{n\ge0}\frac{v_n}{n!}z^n=\frac{e^{4z+6z^2+2z^4}-3e^{2z+z^2}+2e^z}{6}.}
\]

In particular, \(c_n\) is a quasipolynomial of degree ten with period dividing twelve, and

\[
c_n=\frac{n^{10}}{1536\,10!}+O(n^9)\quad(n\to\infty).
\]

The first values \((c_n)_{n=0}^{10}\) are \((0,0,2,7,23,51,116,223,431,762,1341)\); the first values \((v_n)_{n=0}^{7}\) are \((0,0,2,25,277,2895,32631,382963)\).

## Assumptions and scope

The only group-theoretic assumptions are that \(B_n\) consists of signed permutation matrices on \(n\) labeled coordinate lines and that \(C_2\) is a cyclic group of order two. We count actual subgroups and conjugacy classes under *inner conjugation by \(B_n\)*, not classes under the larger automorphism group of \(B_n\). The case \(n=0\) is the trivial group and contributes zero. A subgroup is counted once irrespective of which ordered generating pair is chosen.

## Proof

Let \(K=C_2\times C_2\). A homomorphism \(\rho:K\to B_n\) is a signed action of \(K\) on \(n\) coordinate lines. Forgetting signs gives an ordinary \(K\)-set, and each transitive orbit is \(K/H\), with stabilizer \(H\le K\). The sign on a line stabilizer is a character \(\chi:H\to C_2\). Conversely, the induced signed permutation representation \(\operatorname{Ind}_H^K\chi\) provides the orbit. Choices of coset representatives alter only the signs of the coordinate basis vectors and are therefore conjugate in \(B_n\). Thus transitive signed \(K\)-sets are classified by \((H,\chi)\), and arbitrary signed actions by multisets of these types. Since \(K\) is abelian, there is no additional identification through conjugation of stabilizers.

There are four characters of \(H=K\), producing four types of size one; three subgroups \(H\) of order two, each with two characters, producing six types of size two; and the trivial subgroup with its one character, producing one type of size four. Consequently the ordinary generating function for \(B_n\)-conjugacy classes of homomorphisms from \(K\) is \(P(z)\).

Two injective homomorphisms from \(K\) have conjugate images if and only if they are in one orbit under conjugation in \(B_n\) and precomposition by \(\operatorname{Aut}(K)\cong S_3\). Apply Burnside's lemma to the multiset description. An identity automorphism fixes all eleven types and contributes \(P(z)\). A transposition permutes the size-one types with cycle pattern \(1^2 2\), and the size-two types with pattern \(1^2 2^2\); it fixes the size-four type, contributing \(T(z)\). A three-cycle has patterns \(1\,3\) and \(3^2\) on the first two groups, also fixing the last type, contributing \(C(z)\). Thus \((P+3T+2C)/6\) counts all homomorphism orbits modulo automorphisms of \(K\), including those with nontrivial kernel.

A noninjective homomorphism has image either trivial or cyclic of order two. Precomposition by \(\operatorname{Aut}(K)\) is transitive on the possible nontrivial linear functionals \(K\to C_2\). Therefore its orbit is determined by the conjugacy class of an element of order dividing two in \(B_n\). Such an element has positive and negative signed fixed-coordinate cycles, and positive signed two-cycles only: a negative signed two-cycle would have order four. Its conjugacy-class generating function is \(I(z)=((1-z)^2(1-z^2))^{-1}\). Subtracting \(I(z)\) proves the first formula.

For the second formula count homomorphisms on *labeled* coordinate lines. The signed orbit species has exponential generating function \(\exp(4z+6z^2+2z^4)\). Explicitly a two-point orbit has two sign gauges for each of the six types, giving \(12z^2/2!=6z^2\), while a four-point regular orbit has \(4!/4\) permutations of the cosets and \(2^3\) relative sign gauges, giving \(48z^4/4!=2z^4\). Homomorphisms with image of order at most two are, by the subgroup-lattice Möbius formula for \(K\), subtracted as three copies of \(\operatorname{Hom}(C_2,B_n)\) and restored as two copies of the trivial homomorphism. The EGF of all involutive elements, including the identity, is \(\exp(2z+z^2)\), since signed fixed cycles have two types and signed order-two paired cycles one type. There is exactly one trivial homomorphism per \(n\), giving EGF \(e^z\). Hence the number of injective homomorphisms has EGF \(e^{4z+6z^2+2z^4}-3e^{2z+z^2}+2e^z\). Every subgroup \(K\) supports exactly six injective homomorphisms, proving the second formula.

For the asymptotic, only \(P(z)\) has an order-eleven pole at \(z=1\), with principal coefficient \(1/256\); the other three terms have poles of order at most eight at \(z=1\). At other roots of unity the poles are of lower order. Thus \([z^n]P(z)=n^{10}/(256\,10!)+O(n^9)\), and division by six yields the displayed leading term. All poles are twelfth roots of unity, so the exact coefficient sequence is a quasipolynomial of period dividing twelve.

## Verification

Run `python verify.py` with Python 3 and SymPy. It expands the two formulas through degree ten, verifies the quoted coefficients, constructs every signed permutation directly through degree four, enumerates all subgroups generated by commuting nonidentity involutions, and computes their actual conjugacy orbits by conjugating every subgroup with every group element. The direct counts are \((v_2,c_2)=(2,2)\), \((v_3,c_3)=(25,7)\), and \((v_4,c_4)=(277,23)\), with zero classes in degree one. This independently checks the finite coefficients; it is not a substitute for the general proof above.

## Relationship to prior work

Burns and Pfeiffer classify maximal-*order* abelian subgroups of finite Coxeter groups, including type \(B\), and motivate the rank-two subgroup enumeration; their problem does not give a generating series for *all* embedded Klein-four subgroups and their conjugacy orbits. Tout studies generalized characters and conjugacy types of *individual elements* in wreath products; that elementwise multipartition theory does not itself identify signed \(K\)-set stabilizer/character configurations for simultaneous generators. Klawuhn and Schmidt classify transitivity properties and character-theoretic statistics of wreath products, not the counts asserted here. The signed \(K\)-set mechanism is a natural extension of standard permutation-module induction and Burnside counting; none of these elementary ingredients is claimed as new.

## Limitations

This counts rank-two elementary abelian two-subgroups only; no formula for higher rank, normalizers, or intersections is claimed. The asymptotic concerns numbers of conjugacy classes, not typical subgroup sizes. The cited work and targeted searches do not exclude an earlier equivalent formula expressed using character-labeled transitive \(K\)-sets or Coxeter subgroup classification. Formal independent auditing has not occurred.

## References

- John M. Burns and Goetz Pfeiffer, *Maximal order Abelian subgroups of Coxeter groups*, Glasgow Mathematical Journal 65 (2023), 114–120; first published online August 2, 2022. DOI: https://doi.org/10.1017/S0017089522000143
- Omar Tout, *Generalized characters of the generalized symmetric group*, arXiv:2212.13241v1 (December 26, 2022). https://arxiv.org/abs/2212.13241
- Lukas Klawuhn and Kai-Uwe Schmidt, *Transitivity in wreath products with symmetric groups*, arXiv:2409.20495v1 (September 30, 2024). https://arxiv.org/abs/2409.20495
