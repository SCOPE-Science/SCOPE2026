# Exact minimum uncovered residues for three-prime divisor coverings

## Finding
For distinct odd primes \(p<q<r\), put \(M=pqr\). Let \(u(M)\) denote the minimum number of residues modulo \(M\) left uncovered when **exactly one** congruence class is selected for every divisor \(d\mid M\) with \(d>1\). Then

\[
\boxed{u(pqr)=pqr-pq-pr-qr+1.}
\]

Equivalently, seven residue classes, with the distinct moduli \(p,q,r,pq,pr,qr,pqr\), cover at most \(pq+pr+qr-1\) residues modulo \(M\), and that maximum is achieved. This proves the explicit three-prime conjecture in the cited 2026 preprint.

## Assumptions and scope
All three primes are odd, positive, and distinct, ordered as \(p<q<r\). A class \(a\pmod d\), for \(d\mid M\), is interpreted as the corresponding subset of \(\mathbb Z/M\mathbb Z\). Every proper divisor greater than one occurs once. The result is exact for every such triple and does not assert a result for repeated prime factors or more than three distinct primes.

## Proof
**Upper bound on coverage.** Fix arbitrary classes \(P,Q,R\) modulo \(p,q,r\) respectively, and let \(U_1=P\cup Q\cup R\). By the Chinese remainder theorem their sizes are \(qr,pr,pq\), their pairwise intersection sizes are \(r,q,p\), and their triple intersection has size one. Therefore

\[
|U_1|=qr+pr+pq-r-q-p+1.
\]

Let \(T_{pq}\) be any chosen class modulo \(pq\). It has exactly \(r\) elements modulo \(M\), and since \(pq\) and \(r\) are coprime, its intersection with the already chosen class \(R\) is **exactly one element**, regardless of the residues selected. Thus \(|T_{pq}\setminus U_1|\le r-1\). Similarly, the classes \(T_{pr}\) and \(T_{qr}\) introduce at most \(q-1\) and \(p-1\) new points. Their mutual overlaps can only decrease the number of newly covered points. The single class modulo \(pqr\) contributes at most one further point. Hence any seven-class union has size at most

\[
\begin{aligned}
|U_1|+(r-1)+(q-1)+(p-1)+1
&=pq+pr+qr-1.
\end{aligned}
\]

This proves \(u(M)\ge M-pq-pr-qr+1\).

**A sharp construction.** Identify each residue modulo \(M\) with its CRT coordinate triple \((x_p,x_q,x_r)\). Select the seven classes by fixing the indicated coordinates:

\[
\begin{array}{c|c}
\text{Modulus}&\text{Coordinate constraint}\\\hline
p&x_p=0\\
q&x_q=0\\
r&x_r=0\\
pq&(x_p,x_q)=(1,1)\\
pr&(x_p,x_r)=(2,1)\\
qr&(x_q,x_r)=(2,2)\\
pqr&(x_p,x_q,x_r)=(1,2,1)
\end{array}
\]

Because all primes are at least three, the coordinate values \(0,1,2\) are available and distinct. The three two-coordinate classes avoid the first three (zero-coordinate) classes along their constrained coordinates. Among them, the \(pq\)- and \(pr\)-classes are disjoint because their \(p\)-coordinates disagree; the \(pq\)- and \(qr\)-classes are disjoint because their \(q\)-coordinates disagree; and the \(pr\)- and \(qr\)-classes are disjoint because their \(r\)-coordinates disagree. Each contributes exactly its full cardinality minus the one intersection with its omitted-prime zero-coordinate class, respectively \(r-1,q-1,p-1\). Finally the specified \(pqr\)-class avoids every prior class: it has no zero coordinate, violates the \(pq\) constraint at \(q\), the \(pr\) constraint at \(p\), and the \(qr\) constraint at \(r\). It adds one point. Thus equality holds in every preceding upper bound, giving \(|U|=pq+pr+qr-1\) and the asserted formula.

## Verification
The proof is a symbolic CRT count and requires no finite search. Run the accompanying standalone `verify.py` with Python 3 to reproduce the exact witness coverage for six prime triples and to check the upper bound for a deterministic collection of additional arbitrary choices. These finite calculations only supplement the uniform proof.

For example, the formula gives \(u(105)=35\) at \((p,q,r)=(3,5,7)\) and \(u(385)=219\) at \((5,7,11)\), agreeing with the published exact examples. The construction itself works uniformly in the parameters.

## Relationship to prior work
Öztürk's August 2026 preprint proves \(u(qr)=qr-q-r\) for two distinct odd primes and then explicitly proposes the displayed three-prime identity as **Conjecture 1**, noting numerical verification but no proof (Section 6). The argument here supplies the missing global bound and an attaining construction, rather than another finite verification. Dai, Li, Li and Yi (November 2026) develop general necessary conditions for distinct covering systems and squarefree moduli; their work concerns global covering obstructions, not this precise seven-class extremum. The general odd covering-system question remains open.

## Limitations
The theorem treats the specific seven divisor moduli of a squarefree integer with exactly three odd prime factors. It does not prove the existence or nonexistence of odd distinct covering systems for arbitrary moduli, improve known minimum-modulus bounds, or assert a general formula for four-prime products. The originality comparison includes the explicit conjecture and relevant recent covering-system results, but cannot exclude unpublished or unindexed independent solutions.

## References
1. E. Öztürk, *Closed-form nonexistence certificates for odd covering systems* (August 2026), Section 6, Theorem 6 and Conjecture 1. DOI: https://doi.org/10.13140/RG.2.2.13216.55049 ; full text: https://www.researchgate.net/publication/412442828_Closed-form_nonexistence_certificates_for_odd_covering_systems .
2. X. Dai, H. Li, J. Li, and S. Yi, *On the moduli of distinct covering systems* (first submitted 2026-11-11), arXiv:2611.15110v1, https://arxiv.org/html/2611.15110v1 .
3. P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, and M. Tiba, *The Erdős–Selfridge problem with square-free moduli*, Algebra and Number Theory 15 (2021), 609–626 (for wider context).
