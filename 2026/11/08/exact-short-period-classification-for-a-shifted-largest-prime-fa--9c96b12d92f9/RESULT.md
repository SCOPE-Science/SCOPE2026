# Exact short-period classification for a shifted largest-prime-factor map

## Finding
For every positive integer \(k\), define the deterministic map \(\varphi_k\) on integers \(n\ge2\) by
\[
\varphi_k(n)=\begin{cases}n+k,&n\text{ prime},\\P^+(n),&n\text{ composite},\end{cases}
\]
where \(P^+(n)\) is the largest prime divisor of \(n\). A *primitive cycle of length* \(\ell\) is a cyclically ordered orbit of least positive period \(\ell\), counted only once up to rotation. All cycles of lengths at most four are classified as follows.

**Length one:** no fixed points exist.

**Length two:** all and only the cycles
\[
(p,pm),\qquad k=p(m-1),
\]
where \(p\) is prime, \(m\ge2\) is an integer and every prime divisor of \(m\) is at most \(p\).

**Length three:** all and only the cycles
\[
(2,2^a+1,2^{a+1}),\qquad k=2^a-1,
\]
where \(a\ge1\) and \(2^a+1\) is prime. Equivalently \(a=2^s\) for some integer \(s\ge0\), with the associated Fermat number \(2^{2^s}+1\) prime. In particular, for each \(k\), there is at most one length-three cycle.

**Length four:** all and only the following two disjoint types.

*Alternating type.* Choose distinct primes \(p<q\) and an integer \(t\ge1\) such that
\[
k=tpq-p-q>0,\qquad tp-1>1,\quad tq-1>1,
\]
and every prime divisor of \(tp-1\) is at most \(q\), while every prime divisor of \(tq-1\) is at most \(p\). Then the cycle is exactly
\[
\bigl(p,\ q(tp-1),\ q,\ p(tq-1)\bigr).
\]

*Three-prime type.* Choose \(u\ge1\) with both \(3^u+2\) and \(2\cdot3^u+1\) prime, and set \(k=3^u-1\). The cycle is exactly
\[
\bigl(3,\ 3^u+2,\ 2\cdot3^u+1,\ 3^{u+1}\bigr).
\]

The alternating type has two prime entries; the three-prime type has three. All displayed conditions are jointly necessary and sufficient, for every \(k\ge1\).

A useful explicit subfamily occurs at \(t=1\): for distinct odd primes \(p<q\), the parameter \(k=pq-p-q\) has the alternating four-cycle
\[
\bigl(p,\ q(p-1),\ q,\ p(q-1)\bigr)
\]
if and only if all prime divisors of \(q-1\) are at most \(p\). This is a Frobenius-number parameter for a two-prime pair, linked directly to the smoothness of \(q-1\).

## Assumptions and scope
A prime is a positive prime integer. Every iteration starts at an integer at least two. The result concerns actual states of the piecewise map, not the number of prime entries alone; omitting composite states can alter the primitive period. The conditions involving prime divisors of a positive integer greater than one have their usual meaning; no largest-prime-factor value for one is needed.

The family was introduced by Angsuman Das in December 2023. This result is an arithmetic classification of its shortest periodic orbits across **all** positive shift parameters, not a proof that all longer primitive periods occur.

## Proof
**Fixed points.** For prime \(n\), \(\varphi_k(n)=n+k>n\). For composite \(n\), \(P^+(n)<n\). Thus no state is fixed.

**Cycle shape.** Every composite maps immediately to a prime, so two composite entries cannot occur consecutively in a directed cycle, including across the cyclic boundary. Every cycle contains a composite, since consecutive prime steps add \(k>0\) and cannot return to the starting point without a composite. A primitive two-cycle therefore has exactly one prime. A three-cycle has exactly one composite and two consecutive primes. A four-cycle has either one composite and three consecutive primes, or two composites alternating with two primes. The prime entries of a primitive four-cycle are distinct: equal prime entries at different positions would give a shorter period.

**Period two.** Let \(p\) be the prime entry and \(c\) the composite. Then \(c=p+k\) and \(P^+(c)=p\). The latter forces \(p\mid k\), so \(c=p(1+k/p)=pm\) with \(m\ge2\). Since \(p\) divides \(c\), the equality \(P^+(c)=p\) holds exactly when every prime factor of \(m\) is at most \(p\). Conversely these conditions give the two distinct states \(p\to pm\to p\).

**Period three.** Rotate the cycle to \(p,p+k,p+2k\), where the first two states are prime and the last is composite with \(P^+(p+2k)=p\). Consequently \(p\mid2k\). If \(p\) is odd, \(p\mid k\), which would make \(p+k\) a composite multiple of \(p\). Hence \(p=2\). The last state \(2+2k=2(k+1)\) has largest prime divisor two exactly when \(k+1\) is a power of two. Thus \(k=2^a-1\), \(a\ge1\), and the other prime is \(2^a+1\). Conversely, when that number is prime, \(2\to 2^a+1\to2^{a+1}\to2\), and the states are distinct. Finally, if \(2^a+1\) is prime and \(a\) has an odd factor \(d>1\), then \(2^a+1=(2^{a/d})^d+1\) has the proper factor \(2^{a/d}+1\). Thus \(a\) is a power of two; conversely the primality condition on the corresponding Fermat number is exactly the remaining requirement.

**Period four, alternating type.** Rotate an alternating cycle as \(p,p+k,q,q+k\), with distinct prime states \(p,q\). The composite-to-prime transitions require \(q\mid p+k\) and \(p\mid q+k\), so
\[
k+p+q\equiv0\pmod p,\qquad k+p+q\equiv0\pmod q.
\]
Since \(p,q\) are distinct primes, \(pq\mid k+p+q\), giving \(k=tpq-p-q\) with integer \(t\ge1\). Substitution shows
\[
p+k=q(tp-1),\qquad q+k=p(tq-1).
\]
Each displayed intermediate state must be composite, hence \(tp-1>1\) and \(tq-1>1\). Its largest prime divisor is the desired next prime precisely when every prime divisor of the respective multiplier is no larger than that desired prime. These are the asserted two smoothness conditions. Conversely these conditions force the four transitions exactly as displayed. The primes are distinct, both other states are composite, and all four states are distinct; thus the cycle has least period four. We may take \(p<q\) uniquely by rotating the cycle.

**Period four, three-prime type.** Rotate the cycle as \(p,p+k,p+2k,p+3k\), where the first three are prime and the last is composite with largest prime divisor \(p\). Thus \(p\mid3k\). For any prime \(p\ne3\), this forces \(p\mid k\), contradicting the primality of \(p+k>p\). Therefore \(p=3\). Since \(3+k>3\) is prime, \(k\) is even. The composite state is \(3(k+1)\), whose largest prime divisor is \(3\); because \(k+1\) is odd, it must be a positive power \(3^u\) with \(u\ge1\). Consequently \(k=3^u-1\), while the other two primes are \(3^u+2\) and \(2\cdot3^u+1\). Conversely, their primality yields the stated four-step orbit, and \(3^{u+1}\) is composite with largest prime divisor \(3\). Distinctness follows from \(k>0\). The two four-cycle types are disjoint by their numbers of prime entries. This exhausts the possibilities.

**The smooth-predecessor corollary.** In the alternating family with \(t=1\), the condition \(tp-1>1\) rules out \(p=2\), while \(p<q\) ensures \(q\) is odd. Every prime factor of \(p-1\) is strictly less than \(p<q\), so the first smoothness condition is automatic. The second is exactly the stated \(p\)-smoothness of \(q-1\).

## Verification
The standalone Python script `verify.py` computes the largest prime factor for a fixed finite interval and follows trajectories from specified prime starts for each \(1\le k\le160\). It compares every observed primitive cycle of length at most four with an **independently generated** set from the classification conditions. The saved output `verification_output.txt` records exact agreement, including \(156\) two-cycles, \(3\) three-cycles, and \(35\) four-cycles across the tested shift parameters, with cycles counted separately for distinct parameters. Observed three-cycle parameters are \(1,3,15\); observed exceptional three-prime four-cycle parameters are \(2,8,80\).

The finite computations test transitions and arithmetic boundaries. They do not assert that all cycles for a given shift have been found, or provide an infinite proof. Unrestricted completeness is the symbolic case split and its necessary-and-sufficient arithmetic conditions above.

## Relationship to prior work
Das [1] defined the map, proved eventual periodicity for each shift, bounded the number of cycles, and posed questions about the number of cycles and attainable periods. Figure 2 includes finite data on the least parameter exhibiting various periods; it does not classify all shifts yielding periods three or four. Dubickas [2] gave independent global boundedness results and studied a prime-compressed version of the iteration; these do not imply the stated uncompressed primitive-period classification. A finite public computation [3] gives many cycles for a specific odd shift, and a general locator bound [4] restricts the primes occurring in cycles for even shifts. Neither supplies the universal prime/smoothness classification above.

The exact three-cycle characterization ties the least odd primitive period to Fermat primality. The four-cycle theorem separates two distinct mechanisms: a two-prime Chinese-remainder alignment with smooth multipliers, and an exceptional three-prime chain of powers of three. This is a classification of short periodic orbits, not a solution to the source paper's open question about every possible longer period.

## Limitations
The primality requirements for arbitrarily large Fermat numbers and the exceptional powers-of-three family are not resolved. The classification is conditional on those explicitly stated primality tests and makes no assertion about infinitely many parameters with a given short period. The finite checker is a regression, not an exhaustive global computation. Equivalent short-cycle classifications in unindexed sources cannot be ruled out, and no independent scientific audit is claimed.

## References
1. Angsuman Das, *A Family of Iterated Maps on Natural Numbers*, arXiv:2312.06629v1, first public 11 December 2023, https://arxiv.org/html/2312.06629; *Experimental Mathematics* 33 (2024), 776–780.
2. Artūras Dubickas, *A Class of Bounded Iterative Sequences of Integers*, *Axioms* 13 (2024), 107, DOI 10.3390/axioms13020107; open text https://www.researchgate.net/publication/377990485_A_Class_of_Bounded_Iterative_Sequences_of_Integers.
3. *Thirty-six distinct loops for Das's map at \(k=20735\)*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-thirty-six-distinct-loops-for-das-s-map-at-k-20735--c588f79a1e3b.
4. *Even-parameter cycle bound from the least missing prime \(\rho(k)\)*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-even-parameter-cycle-bound-from-the-least-missing-prime-rho-k--644ecc618762.
