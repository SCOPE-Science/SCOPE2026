# A positive-density six-cycle family in an unresolved residue class of ring structure graphs

## Finding
For a finite field \(\mathbb F_p\), write \(\Phi_p(a,b)=(a+b,ab)\) and \(g(x)=x-x^2\). Define
\[
P(X)=X^6-4X^5+8X^4-10X^3+9X^2-6X+3.
\]
The set of rational primes \(p\equiv19\pmod{24}\) for which \(P\) has a root in \(\mathbb F_p\) has **natural density exactly \(5/72\)** among all primes, or conditional density \(5/9\) among primes congruent to \(19\pmod{24}\). Among primes in the specified congruence class, the numbers of **six-cycles canonically arising from roots of \(P\)** are zero, one and two with conditional densities \(4/9\), \(4/9\), and \(1/9\), respectively. Every prime with one or two such cycles has a **primitive directed six-cycle**. Consequently the still-unresolved prime class \(p\equiv7\pmod{12}\) contains a positive-density infinite subfamily whose ring structure graph has more than \(p\) weakly connected components. No assertion is made for every prime in that class.

## Assumptions and scope
A prime is a positive rational prime. The graph has vertex set \(\mathbb F_p^2\) and one outgoing directed edge from each vertex \((a,b)\) to \(\Phi_p(a,b)\). A primitive six-cycle consists of six distinct vertices, with the sixth iterate returning to the first. Natural density means the limit of the proportion of rational primes up to a real bound; the theorem computes the density of the **specified polynomial-root witness set**, not of all primes whose structure graph contains a six-cycle. The proof uses the classical Chebotarev density theorem. The date and classification of the motivating work are recorded in the references.

## Proof
**1. A six-cycle certificate.** Direct polynomial expansion gives
\[
g^3(X)-X=-X^2P(X),\qquad
 g^2(X)-X=-X^2(X^2-2X+2).
\]
The integer resultant \(\operatorname{Res}(P,X^2-2X+2)\) equals \(1\), and \(P(0)=3\). Therefore, for every prime \(p>3\), any \(y\in\mathbb F_p\) satisfying \(P(y)=0\) has exact period three under \(g\). Furthermore,
\[
\Phi_p(-1,z)=(z-1,-z),\qquad
\Phi_p^2(-1,z)=(-1,g(z)).
\]
Hence \(\Phi_p^{2j}(-1,y)=(-1,g^j(y))\), so the sixth iterate returns. An odd iterate could return to \((-1,y)\) only if \(g^j(y)=0\), which is impossible on a nonzero three-cycle; an even return before six would contradict the least \(g\)-period. Thus the six vertices are distinct.

**2. The exact Galois group.** Over \(\mathbb Q\), the six roots of the squarefree polynomial \(P\) form exactly two disjoint primitive three-cycles under \(g\). Every Galois automorphism commutes with \(g\), so the splitting-field Galois group \(G\) embeds in \((C_3\times C_3)\rtimes C_2\), with the last factor interchanging the two cycles. The reduction of \(P\) modulo \(5\) is irreducible of degree six. Its reduction modulo \(11\) has three distinct linear factors at \(2,5,9\), and the irreducible cubic factor \(X^3+X^2+6X+4\). Both primes are unramified because
\[
\operatorname{Disc}(P)=-41472=-2^9 3^4.
\]
The Frobenius permutations therefore supply a six-cycle and a three-cycle fixing the other three roots. The latter rotates only one \(g\)-cycle; conjugating by the former gives a rotation on the other. They generate \(C_3\times C_3\), and the six-cycle interchanges the blocks. It follows that
\[
G\cong(C_3\times C_3)\rtimes C_2,\qquad |G|=18.
\]

**3. The cyclotomic intersection.** Write \(L\) for the splitting field of \(P\), and \(C=\mathbb Q(\zeta_{24})\). The only index-two subgroup of \(G\) is its odd-order normal subgroup \(C_3\times C_3\). By the discriminant, its unique quadratic subfield is \(\mathbb Q(\sqrt{-2})\). Since \([L:\mathbb Q]=18\), \([C:\mathbb Q]=8\), and \(\mathbb Q(\sqrt{-2})\subseteq C\), the intersection has degree exactly \(2\):
\[
L\cap C=\mathbb Q(\sqrt{-2}),\qquad [LC:\mathbb Q]=72.
\]
For a prime \(p\equiv19\pmod{24}\), Frobenius on \(C\) is the automorphism \(\zeta_{24}\mapsto\zeta_{24}^{19}\). Because \(p\equiv3\pmod8\), the quadratic symbol \(\bigl(\frac{-2}{p}\bigr)=+1\). The compatible Frobenius elements in \(\operatorname{Gal}(LC/\mathbb Q)\) consequently have the nine possible \(L\)-components \((a,b)\in C_3\times C_3\). Such an element fixes a root of \(P\) if and only if \(a\) or \(b\) is the identity; there are \(3+3-1=5\) such elements. More precisely, four elements rotate both blocks nontrivially and fix zero roots, four rotate exactly one block nontrivially and fix three roots, and one fixes all six roots. Each \(g\)-orbit of three roots gives precisely one distinct \(\Phi_p\)-orbit of length six through \((-1,y)\). Thus the same Frobenius calculation gives conditional frequencies \(4/9,4/9,1/9\) for zero, one or two such cycles. This criterion is invariant under conjugacy in the compositum Galois group. Chebotarev therefore gives the exact density
\[
\frac{5}{72}
\]
of primes in the specified residue class with a root of \(P\). Only the ramified primes \(2,3\) are excluded, and neither lies in this residue class.

**4. Graph components.** A functional graph has one directed cycle in every weakly connected component. The graph of \(\Phi_p\) always has \(p\) distinct fixed-point components, represented by \((a,0)\). The additional primitive six-cycle lies in another component. Thus every prime in this explicitly described positive-density family has strictly more than \(p\) components.

## Verification
Run `python3 prime_structure_cycle_checker.py` from the directory containing this document. The standalone Python checker evaluates both iterated-polynomial identities, the discriminant and resultant using exact rational/integer arithmetic, proves the degree-six irreducibility modulo \(5\) by the finite-field polynomial gcd criterion, checks the factorization and cubic irreducibility modulo \(11\), and directly verifies primitive six-cycles at primes \(43,67,139,163\). It prints `PRIME_STRUCTURE_GRAPH_DENSITY_CERTIFICATE_OK`. Computational checks do not substitute for the Galois argument or Chebotarev's theorem.

## Relationship to prior work
Chernev and Chernev (2026), Section 5, Lemma 5.1, prove the two-step reduction \(\Phi^2(-1,z)=(-1,g(z))\) and explicitly leave the infinite prime class \(p\equiv7\pmod{12}\) unresolved, beyond finite experiments through \(2077\). The present statement gives a quantitatively explicit infinite subfamily in that open class, rather than solving their conjecture for the entire class. Lipkovski (2012, 2017) studies the same graphs and small cycles without this congruence-conditioned density. Bridy and Garton (2017) use dynatomic Galois wreath products and Frobenius fixed-point proportions for broader dynamical questions; the present argument specializes these tools to the *specific* ring-structure graph and resolves the quadratic-intersection constraint needed for the residue-class density. These methods, viewed in isolation, are not claimed as new.

## Limitations
The theorem supplies an exact distribution only for six-cycles canonically produced by the stated polynomial-root witness, and a lower bound of \(5/72\) for primes with at least one primitive six-cycle. It does **not** classify all such primes, all period-six orbits, or primes congruent to \(7\pmod{24}\), nor prove the full ring-structure-graph conjecture. Historical priority for the special fixed-parameter density may depend on older arithmetic-dynamics work; published literature checked includes the principal graph papers and a general dynatomic-density treatment. No independently conducted scientific audit or external mathematical certification is asserted.

## References
1. A. M. Chernev and N. A. Chernev, *On the Connected Components of Structure Graphs of Associative Rings*, arXiv:2611.07521v1 (first posted 2026-11-05), Sections 3, 5, 8 and 9, https://arxiv.org/html/2611.07521v1 .
2. A. T. Lipkovski, *Digraphs associated with finite rings*, Publications de l'Institut Mathématique 92 (2012), 35–41, https://doi.org/10.2298/PIM1206035L .
3. A. T. Lipkovski, *Structure Graphs of Rings: Definitions and First Results*, Journal of Mathematical Sciences 225 (2017), 658–665, https://doi.org/10.1007/s10958-017-3484-3 .
4. A. Bridy and D. Garton, *Dynamically distinguishing polynomials*, Research in the Mathematical Sciences 4 (2017), article 13, https://doi.org/10.1186/s40687-017-0103-3 .
