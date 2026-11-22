# Exact first-two-level covering deficit for four odd prime factors

## Finding
For distinct odd primes \(p<q<r<s\), let \(M=pqrs\). Choose exactly one congruence class modulo each of the ten moduli \(p,q,r,s,pq,pr,ps,qr,qs,rs\). The minimum number \(H(p,q,r,s)\) of residue classes modulo \(M\) not covered by their union is
\[
H(p,q,r,s)=\prod_{\ell\in\{p,q,r,s\}}(\ell-1)-\sum_{\{i,j\}\subset\{p,q,r,s\}}\prod_{\ell\notin\{i,j\}}(\ell-1)+\begin{cases}q+2,&p=3,\\3,&p\ge5.\end{cases}
\]
This is an exact minimum, not merely a lower bound. For \((p,q,r,s)=(3,5,7,11)\) it is \(323\), and for \((5,7,11,13)\) it is \(2519\).

## Assumptions and scope
Each modulus occurs once, congruence residues may be chosen arbitrarily, and the ten moduli are only the prime and two-prime divisors of \(M\). There is no assumption that the ten classes form a covering; the theorem quantifies their optimal *partial* coverage. Write \(m_0=p-1,m_1=q-1,m_2=r-1,m_3=s-1\), \(E=\{01,02,03,12,13,23\}\) and
\[
B=\sum_{ij\in E}\prod_{v\notin\{i,j\}}m_v.
\]
The formula is \(H=\prod_vm_v-B+\delta\), where \(\delta=3\) if \(p\ge5\) and \(\delta=m_1+3\) if \(p=3\).

## Proof
By the Chinese remainder theorem, residues modulo \(M\) form a product of four prime fields. Each of the four prime-modulus classes fixes one coordinate. Relabel these four fixed values as zero. The remaining core \(C\) has exactly \(\prod_vm_v\) points; a two-prime class either meets \(C\) in the empty set or is a cylinder fixing its two selected coordinates to nonzero values. Choosing an empty cylinder cannot enlarge the union, so it suffices to optimize six nonempty pair cylinders \(A_{ij}\), one for every \(ij\in E\). Their individual cardinalities sum to \(B\).

At vertex \(v\), the three incident edges select three labels from a set of size \(m_v\). Only equality relations between the three labels affect any intersection. There are exactly five possible equivalence partitions, represented by label triples \((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2)\). Thus there are \(5^4=625\) complete patterns, independent of the sizes. When \(p=3\), the all-distinct pattern is unavailable at the first vertex, so precisely \(4\cdot5^3=500\) patterns are feasible. All other listed patterns can be realized, because each remaining alphabet has at least four labels.

For any fixed equality pattern \(\sigma\) and nonempty subset \(T\subseteq E\), the intersection \(\bigcap_{e\in T}A_e\) is empty if one vertex receives two different selected labels from edges of \(T\). Otherwise its cardinality is exactly \(\prod_{v: T\text{ has no edge at }v}m_v\). Inclusion–exclusion over the \(63\) nonempty subsets yields an explicit integer polynomial \(U_\sigma(m_0,m_1,m_2,m_3)\) for the union size. This gives a complete finite symbolic classification without bounding the prime values.

The exact symbolic certificate `crt_four_prime_certificate.py`, supplied alongside this proof, reconstructs every one of those polynomials from that intersection rule and checks the following two *coefficientwise nonnegative polynomial identities*:

1. For all \(625\) patterns, substitute \(m_v=4+x_v\) and expand \(B-U_\sigma-3\) in \(x_0,x_1,x_2,x_3\). Every coefficient is nonnegative. This applies whenever \(p\ge5\).
2. For all \(500\) feasible patterns, substitute \((m_0,m_1,m_2,m_3)=(2,4+x,6+x+y,8+x+y+z)\) and expand \(B-U_\sigma-(7+x)\). Every coefficient is nonnegative. This applies when \(p=3\): the gaps between successive distinct odd primes are at least two, so \(x=q-5\), \(y=r-q-2\), \(z=s-r-2\) are nonnegative.

These are exact finite integer-coefficient checks on fully specified polynomials: each positivity statement follows directly for **all** nonnegative parameter values, not from sampling the prime parameters. The included checker uses no symbolic algebra library or floating point arithmetic. A complete proof of each identity is given algorithmically by its exhaustive, deterministic expansion of \(625\) and \(500\) patterns; the elementary polynomial-multiplication operations and all ranges are explicit in the code.

Sharpness is immediate from two incidence assignments. If \(p\ge5\), choose all three labels different at each vertex, so that the only overlaps are the three complementary-edge intersections, each a single point: \(U=B-3\). If \(p=3\), make the first-vertex labels of the \(pr\) and \(ps\) cylinders equal and its \(pq\) label different; choose all labels distinct at the other vertices. The intersection \(A_{pr}\cap A_{ps}\) has \(m_1=q-1\) points and the complementary-edge intersections contribute three additional points, with no other overlaps: \(U=B-m_1-3=B-q-2\). All assigned labels are nonzero and available. The stated minimum of \(\prod_vm_v-U\) follows.

## Verification
Run `python3 crt_four_prime_certificate.py` from the directory containing that file. It reports the exhaustive \(625\)-pattern and \(500\)-pattern nonnegative coefficient checks and asserts both exact sharpness patterns. As a separate finite sanity check, full-point enumeration on the two smallest relevant prime tuples gives core-cylinder union maxima \(157\) (core size \(480\)) and \(361\) (core size \(2880\)), respectively. The infinite conclusion is derived from symbolic positivity and the completeness of the five equality patterns, not from these numerical examples.

## Relationship to prior work
Dai–Li–Li–Yi [1] study all distinct covering systems and derive stronger global restrictions, using distortion and convex comparison; they do not supply this exact ten-modulus partial-coverage formula in the inspected portions. Balister–Bollobás–Morris–Sahasrabudhe–Tiba [2] prove that distinct odd squarefree moduli never cover all integers, using a much broader hyperplane sieve. That qualitative noncovering theorem does not determine the sharp number of uncovered classes for this specified four-prime, first-two-level subsystem. Cummings–Filaseta–Trifonov [3] give a global minimum-modulus bound; only its accessible abstract was inspected. An existing exact three-prime CRT result concerns *all* seven nontrivial divisors of a three-prime product, so it does not imply the present four-prime six-pair collision law.

## Limitations
No statement is made about arbitrary subsets of moduli involving triple or four-prime products, repeated moduli, more than four prime factors, or non-squarefree prime-power moduli. The computationally checked symbolic identities are finite, but their implications are uniform over unbounded prime parameters. Earlier equivalent inequalities could be implicit in unindexed literature; a separate independent audit remains unperformed.

## References
[1] X. Dai, H. Li, J. Li, S. Yi, *On the moduli of distinct covering systems*, arXiv:2611.15110v1 (public 2026-11-11), https://arxiv.org/abs/2611.15110.

[2] P. Balister, B. Bollobás, R. Morris, J. Sahasrabudhe, M. Tiba, *The Erdős–Selfridge problem with square-free moduli*, arXiv:1901.11465v1 (2019), https://arxiv.org/abs/1901.11465.

[3] M. Cummings, M. Filaseta, O. Trifonov, *An upper bound for the minimum modulus in a covering system with squarefree moduli*, arXiv:2211.08548v1 (2022), https://arxiv.org/abs/2211.08548.
