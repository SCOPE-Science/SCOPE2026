# Sharp finite-layer support of Geil–Matsumoto footprints for interval numerical semigroups

## Finding
For integers \(n\ge2\), \(1\le t<n\), and \(q\ge2\), define the numerical semigroup \(S=\langle n,n+1,\ldots,n+t\rangle\), its positive part \(S^*=S\setminus\{0\}\), and its Geil–Matsumoto footprint \(E_q=S\setminus(qS^*+S)\). Here \(qS^*=\{qu:u\in S^*\}\). Define \(e=\lceil(q-1)/t\rceil\) and \(K=q+e\). Then

\[
 E_q\subseteq[0,Kn-1],
\]
and, with \([a,b]_{\mathbb Z}=\{z\in\mathbb Z:a\le z\le b\}\) (empty when \(a>b\)),
\[
\begin{aligned}
E_q=\Big(\{0\}&\cup\bigcup_{k=1}^{K-1}[kn,\min\{k(n+t),Kn-1\}]_{\mathbb Z}\Big)\\[-2pt]
&\setminus\bigcup_{h=0}^{e-1}\bigcup_{i=0}^{t}
[(q+h)n+qi,\min\{(q+h)n+qi+ht,Kn-1\}]_{\mathbb Z}.
\end{aligned}
\]
The cutoff is uniformly best possible: for each fixed \(q\ge2\), \(t\ge1\), and arbitrarily large integers \(n>t\), the footprint intersects \([(K-1)n,Kn-1]\).

Writing \(GM_q(S)=1+\#E_q\), two closed consequences are
\[
GM_2(S)=3+t+\min\{t,\lfloor n/2\rfloor\},
\]
for every \(1\le t<n\), and
\[
GM_3(S)=4+3t+\min\{3t,n-1\}-\max\{0,2t-n+1\}-\min\{t,\lfloor(n-1)/3\rfloor\}
\]
for every \(2\le t<n\). These are consequences of the footprint theorem, not independent novelty claims.

## Assumptions and scope
Only integer parameters \(n\ge2\), \(1\le t<n\), \(q\ge2\) are required. The bound is a semigroup invariant for any integer \(q\), and when \(q\) is a prime power it is the usual finite-field Geil–Matsumoto bound. All intervals are of integers, with repetitions in semigroup sums allowed. The sharpness quantifier is uniform over arbitrarily large multiplicities \(n\), not the assertion that every individual \(n\) has the least cutoff \(K\).

## Proof
Let \(B=[n,n+t]_{\mathbb Z}\). For every integer \(k\ge1\), the set of sums of exactly \(k\) elements of \(B\) equals \(kB=[kn,k(n+t)]_{\mathbb Z}\), by distributing any offset \(0\le r\le kt\) among \(k\) summands. Therefore \(S=\{0\}\cup\bigcup_{k\ge1}kB\).

**High-layer saturation.** If \(k\ge K=q+\lceil(q-1)/t\rceil\), then \((k-q)t\ge q-1\). Every integer offset \(0\le r\le kt\) belongs to at least one interval
\[
[qi,qi+(k-q)t]_{\mathbb Z},\qquad0\le i\le t,
\]
because consecutive intervals are separated by \(q\) and their lengths are at least \(q\) lattice points, and their union spans from zero to \(qt+(k-q)t=kt\). Thus each element of \(kB\) is \(q(n+i)+v\) with \(n+i\in S^*\), \(v\in(k-q)B\subseteq S\). Hence \(kB\subseteq qS^*+S\).

Suppose \(s\in S\) and \(s\ge Kn\). Choose any representation \(s\in kB\). If \(k\ge K\), the previous argument applies. If \(1\le k<K\), then \(Kn\le s\le k(n+t)<K(n+t)\), so \(s\in KB\) and is again covered. This proves \(E_q\subseteq[0,Kn-1]\).

**Exact support below the cutoff.** Since \(e\le q-1\), we have \(K\le2q-1\). An element \(s<Kn\) lies in \(S\) precisely when it is zero or occurs in one of the first \(K-1\) intervals \(kB\), truncated at \(Kn-1\). If also \(s=qu+v\) with \(u\in S^*\), \(v\in S\), then \(u<2n\), since otherwise \(qu\ge2qn>Kn\). Thus \(u=n+i\) for some \(0\le i\le t\). Write \(v\in hB\) for some integer \(h\ge0\) (where \(0B=\{0\}\)). The inequality \(s<Kn\) implies \(q+h<K\), equivalently \(0\le h<e\). Conversely every element in the indicated \(q(n+i)+hB\) intervals belongs to \(qS^*+S\). This gives the exact set formula.

**Sharp uniform cutoff.** Fix \(q,t\), let \(h=e-1\), \(k=q+h=K-1\), and choose arbitrarily large \(n>kt+q\). The number \(s=kn+ht+1\) belongs to \(kB\) because \(ht+1\le kt\), and satisfies \(kn\le s<(k+1)n=Kn\). Suppose \(s=q(n+i)+v\) as above. As \(s<Kn<2qn\), the positive part must be one generator. The gap between adjacent layers is positive through layer \(k\) because \(n>kt\), so the representation \(v\in jB\) must have \(j=h\). It would require \(ht+1=qi+r\) with \(0\le i\le t\), \(0\le r\le ht\). But \(ht\le q-2\); if \(i=0\) the right side is too small, while if \(i\ge1\) it is at least \(q>ht+1\). Contradiction. Thus \(s\in E_q\), proving no smaller uniform cutoff coefficient than \(K\) is possible.

**Small field corollaries.** For \(q=2\), we have \(e=1\), \(K=3\). The truncated layers \(B\) and \(2B\) are disjoint; removing precisely those dilated generators \(2(n+i)<3n\) gives the stated binary formula. For \(q=3\), \(t\ge2\) also gives \(e=1\), \(K=4\). The first two layers are disjoint and the second and third overlap in exactly \(\max\{0,2t-n+1\}\) positions. The third truncated layer has \(1+\min\{3t,n-1\}\) elements. Removing the \(1+\min\{t,\lfloor(n-1)/3\rfloor\}\) dilated generators below \(4n\) yields the ternary formula.

## Verification
Run `python3 verify.py`. It uses an independent dynamic-programming construction of all semigroup elements up to a finite limit, subtracts the translated generator ideals, and compares the exact sets with the interval description. The implemented checks cover \(4650\) cases for \(2\le n\le31\), \(1\le t<n\), and \(2\le q\le11\), as well as \(900\) closed-form cases and \(250\) constructive sharpness witnesses. All pass. These finite tests are corroboration; the proof above establishes the unbounded statements.

## Relationship to prior work
Marques, Mendoza, Quoos and Tizziotti (arXiv:2508.17022, first posted 2025-08-23) give a general Apéry-set sum for \(GM_q\) in their Theorem 4.1, so the numerical **values** of the bound are in principle computable already for all interval semigroups. Their Theorem 4.4 gives simpler cardinality formulas for sufficiently wide intervals, and they explicitly note the additional difficulty of narrow intervals. The claim here is **not** priority for computing a special numerical value from their general formula. It is an exact geometric description of the entire surviving ideal complement, its sharp uniform layer cutoff for every interval width, and the accompanying direct interval construction. The binary and ternary formulas are included to illustrate the new description. Earlier general treatments of semigroup ideals and the Geil–Matsumoto invariant explain the motivation but do not supply this sharp interval-layer cutoff in the material inspected.

## Limitations
This is an elementary structural result about a numerical-semigroup bound, not a construction of curves attaining it. The uniform sharpness is over variable \(n\): particular small multiplicities may have a smaller actual last occupied layer. Earlier general formulas compute the same counts indirectly; no assertion of priority is made for their numerical specializations. Search-based originality review cannot exclude equivalent unindexed statements. No independent mathematical validation has been performed.

## References
1. A. Marques, E. Mendoza, L. Quoos, G. Tizziotti, *A closed formula for the Geil–Matsumoto bound on numerical semigroups via Apéry sets*, arXiv:2508.17022, first version 2025-08-23, relevant Theorems 4.1, 4.4 and Section 4. https://arxiv.org/abs/2508.17022
2. A. Bras-Amorós and M. Vico-Oton, *On the Geil–Matsumoto bound and the length of AG codes*, arXiv:1706.10214 (2017), for two-generator context. https://arxiv.org/abs/1706.10214
3. *Ideals of Numerical Semigroups and Error-Correcting Codes*, Symmetry 11 (2019), 1406, relevant Section 5.2. https://doi.org/10.3390/sym11111406
