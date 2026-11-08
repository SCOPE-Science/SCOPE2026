# A sharp five-moment barrier for modular triples

## Finding
For an integer \(N\ge 2\), write \(R_N=\mathbb Z/N\mathbb Z\), and for a triple \(A=(a_1,a_2,a_3)\in R_N^3\) define \(P_j(A)=a_1^j+a_2^j+a_3^j\) for \(j\ge1\). Let \(m(N)\) be the least positive integer such that, for **all** triples \(A,B\in R_N^3\), the equations \(P_j(A)=P_j(B)\) for \(1\le j\le m(N)\) force \(P_j(A)=P_j(B)\) for every \(j\ge1\). Then

\[
m(N)=\begin{cases}
1,&N=2,\\
2,&N=3\text{ or }N=6,\\
5,&9\mid N,\\
3,&\text{all other integers }N\ge2.
\end{cases}
\]

The value five in the third case is sharp: four matching moments need not imply a matching fifth moment. The statement concerns equality of all power sums, not equality of the underlying triples up to permutation.

## Assumptions and scope
All congruences and triple coordinates are taken in the commutative ring \(R_N\); repeated coordinates and zero coordinates are permitted. Every bound holds for every positive prime-power exponent and every finite product of prime powers. No restriction to units, pairwise-distinct coordinates, or squarefree moduli is imposed.

## Proof
Write \(E_1(A)=a_1+a_2+a_3\), \(E_2(A)=a_1a_2+a_1a_3+a_2a_3\), and \(E_3(A)=a_1a_2a_3\), with analogous quantities for \(B\). Newton's identities, valid in every commutative ring, give
\[
P_1=E_1,\quad P_2=E_1P_1-2E_2,\quad P_3=E_1P_2-E_2P_1+3E_3,
\]
and the recurrence
\[
P_j=E_1P_{j-1}-E_2P_{j-2}+E_3P_{j-3}\qquad(j\ge4).
\]
We first establish the claimed upper bound over each prime-power ring.

**Primes at least five.** If the first three moments match modulo \(p^k\), the successive Newton identities determine \(E_1,E_2,E_3\), since \(2\) and \(3\) are units. The recurrence then forces all higher moments to match.

**The prime two.** Over \(R_2\), every residue satisfies \(x^j=x\) for all positive \(j\), so the first moment suffices. Now let \(N=2^k\) with \(k\ge2\), and suppose the first three moments of \(A\) and \(B\) agree. Put \(t=E_2(A)-E_2(B)\). The first two Newton identities give \(E_1(A)=E_1(B)=e\) and \(2t=0\); the third gives \(3(E_3(A)-E_3(B))=et\). Since \(3\) acts as the identity on any element annihilated by \(2\), and \(3\) is invertible modulo \(2^k\), we obtain \(E_3(A)-E_3(B)=et\). Let \(D_j=P_j(A)-P_j(B)\). Subtracting the recurrences gives, for \(j\ge4\),
\[
D_j=eD_{j-1}-E_2(A)D_{j-2}+E_3(A)D_{j-3}+t\bigl(eP_{j-3}(B)-P_{j-2}(B)\bigr).
\]
For every positive exponent \(r\), \(P_r(B)\equiv P_1(B)=e\pmod2\), because \(x^r\equiv x\pmod2\). Thus the parenthesis is congruent to \(e^2-e=0\pmod2\). Since \(2t=0\), the final term vanishes modulo \(2^k\). Starting from \(D_1=D_2=D_3=0\), induction gives \(D_j=0\) for all \(j\ge4\).

**The prime three.** Over \(R_3\), odd positive powers agree with the first powers of their bases and even positive powers agree with their squares. Hence the first two moments suffice. Now let \(N=3^k\) with \(k\ge2\), and assume the first five moments agree. Since \(2\) is a unit, the first two Newton identities fix \(E_1(A)=E_1(B)=e\) and \(E_2(A)=E_2(B)=f\). Set \(t=E_3(A)-E_3(B)\). Equality of the third, fourth, and fifth moments gives, in turn,
\[
3t=0,\qquad et=0,\qquad tP_2(B)=0.
\]
If \(t=0\), the recurrence settles the claim. Otherwise, \(3t=0\) implies \(t=3^{k-1}u\) with \(u\not\equiv0\pmod3\). The other two equations imply \(P_1(B)=e\equiv0\pmod3\) and \(P_2(B)\equiv0\pmod3\). For every \(r\ge1\), reduction modulo three gives \(P_r(B)\equiv P_1(B)\) for odd \(r\) and \(P_r(B)\equiv P_2(B)\) for even \(r\). Consequently \(tP_r(B)=0\) modulo \(3^k\) for every \(r\ge1\). Subtracting the common-coefficient recurrences for all \(j\ge4\) yields
\[
D_j=eD_{j-1}-fD_{j-2}+E_3(A)D_{j-3}+tP_{j-3}(B).
\]
The final term vanishes, and the first five differences vanish by hypothesis, so induction establishes equality of every later moment.

**Sharpness.** Modulo \(3\), the triples \((0,0,0)\) and \((0,1,2)\) have the same first moment but different second moments. For any \(k\ge2\), write \(u=2^{k-1}\); the triples \((0,0,1+u)\) and \((0,1,u)\) modulo \(2^k\) share their first two moments but not their third. For every \(p\ge5\) and \(k\ge1\), choose \(v=3^{-1}\) in \(R_{p^k}\). The triples \((0,0,1)\) and \((2v,2v,-v)\) have matching first two moments, but their third moments differ by \(4/9\), a unit in \(R_{p^k}\).

For the remaining, crucial case, let \(k\ge2\), \(N=3^k\), and \(u=3^{k-1}\). The polynomial \(F(X)=X^3-X+u\) has three distinct simple roots modulo \(3\), namely \(0,1,-1\), because \(F'(X)=3X^2-1\equiv-1\pmod3\). Hensel lifting gives three roots \(b_1,b_2,b_3\) modulo \(3^k\) reducing to those distinct residues. The factorization of \(F\) modulo \(3^k\) follows from monicity, the three roots, and successive division by the monic factors; hence the triple \(B=(b_1,b_2,b_3)\) has \(E_1(B)=0\), \(E_2(B)=-1\), \(E_3(B)=-u\). Compare with \(A=(0,1,-1)\), which has the same first two elementary symmetric values but \(E_3(A)=0\). Newton's identities give equal moments for \(j=1,2,3,4\): the third-moment difference is \(3u=0\), and the fourth-moment difference is zero because \(E_1=0\). The fifth moments differ by \(2u\not\equiv0\pmod{3^k}\). Thus five moments really are necessary whenever a factor \(3^k\) with \(k\ge2\) is present.

**Chinese remainder theorem.** Writing \(N=\prod p_i^{k_i}\), equality of the first \(m\) moments modulo \(N\) holds exactly when it holds modulo each prime-power factor. The established local upper bounds therefore imply \(m(N)\le\max_i m(p_i^{k_i})\). Conversely, lift a local sharpness witness at a factor with maximal threshold via the Chinese remainder theorem, assigning both triples all-zero coordinates at every other factor. Its moment of the first distinguishing degree differs modulo \(N\), so the opposite inequality holds. This proves the formula for all \(N\ge2\).

## Verification
Run `python3 verify.py` using only the Python standard library. The checker enumerates all unordered triples for each modulus from \(2\) through \(60\), compares moments through degree \(11\), and recovers the exact minimum separating prefix for each enumerated modulus. It also tests explicit sharpness witnesses at powers of \(2\), primes at least \(5\), and Hensel-lifted cubic roots at powers of \(3\). The recorded execution completed successfully after checking \(595664\) unordered triples across the stated moduli. These finite checks are independent illustrations, not a substitute for the unrestricted inductive proof.

## Relationship to prior work
Wooley's work on the cubic Vinogradov mean-value system considers integer solutions of equal power-sum equations and observes diagonal rigidity of triples over the integers [1]. That conclusion does not by itself describe moment equivalence over residue rings with zero divisors. De Vries studies power polynomials and Newton identities over general commutative rings, including rational-function recovery and failure of finite polynomial generation in positive characteristic [2]. Polynomial generation is different from equality of **evaluated** power sums on triples over finite residue rings; in particular neither inspected result supplies the four-case exact minimum above. The present statement concerns the degree at which higher moment data become redundant, not the recovery of all elementary symmetric functions or tuple identity.

## Limitations
This theorem is specific to triples and to the full residue ring \(\mathbb Z/N\mathbb Z\). It does not calculate the number of distinct moment signatures, classify all pairs sharing those signatures, solve general modular Vinogradov systems with more summands, or claim that equal power sums necessarily imply equality of the triples as multisets. The historical-priority search is not exhaustive; an earlier equivalent evaluation-level statement may exist in unindexed symmetric-function literature. Independent verification has not been performed.

## References
[1] T. D. Wooley, *The cubic case of the main conjecture in Vinogradov's mean value theorem*, arXiv:1401.3150v1, publicly posted 14 January 2014, https://arxiv.org/html/1401.3150v1.

[2] S. de Vries, *On Newton's identities in positive characteristic*, arXiv:2305.19850v4, https://arxiv.org/html/2305.19850v4. This is supporting later literature, not the archival source-date anchor.
