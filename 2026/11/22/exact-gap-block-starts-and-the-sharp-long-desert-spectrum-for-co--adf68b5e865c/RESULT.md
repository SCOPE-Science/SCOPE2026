# Exact gap-block starts and the sharp long-desert spectrum for consecutive triangular generators

## Finding
For every integer \(n\ge3\), put \(T_k=k(k+1)/2\), \(a=T_n\), \(b=T_{n+1}\), \(c=T_{n+2}\), and \(S_n=\langle a,b,c\rangle\). A *gap block* or *desert* is a maximal nonempty interval of consecutive positive integers disjoint from \(S_n\). Let \(R_n\) count these intervals. Then
\[
R_n=\begin{cases}n^2,&n\text{ even},\\n^2-1,&n\text{ odd}.\end{cases}
\]
More precisely, *every* block of length strictly greater than \(n+1=b-a\) is one of
\[
I_q=[qc+1,(q+1)a-1]\cap\mathbb Z,
\quad q=0,1,\ldots,\left\lfloor\frac{n+1}{4}\right\rfloor-1.
\]
The displayed intervals are nonempty and distinct, and their lengths are exactly
\[
|I_q|=a-1-q(2n+3).
\]
Thus the entire long-block length spectrum is a strictly decreasing arithmetic progression, with common difference \(2n+3\), and the cutoff \(n+1\) separates it from every other gap block.

For a complete *starting-position* formula, define \((d,A,B,C,H)\) according to parity:
\[
(d,A,B,C,H)=
\begin{cases}
(n+1,n/2,n/2+1,n/2+2,n/2),&n\text{ even},\\
((n+1)/2,n,n+2,n+4,n+1),&n\text{ odd}.
\end{cases}
\]
One has \(a=dA\), \(b=dB\), \(c=dC+1\) and \(\gcd(A,B)=1\). For each \(r=dt+\ell\), with \(0\le t<A\) and \(0\le\ell<d\), let \(j_r\in\{0,\ldots,A-1\}\) be the unique solution of
\[
Bj_r+C\ell\equiv t\pmod A,
\]
and set \(w_r=j_rb+\ell c\), \(\kappa_r=(w_r-r)/a\). The complete set of **first integers in all maximal gap blocks** is the disjoint union
\[
\bigcup_{\substack{0\le r<a-1\\\ell=r\bmod d<d-1\\j_r\in\{0,1\}}}
\{r+1+a(\kappa_r+h):0\le h<H\}.
\]
In particular this formula specifies every block start even when its length is at most \(n+1\).

## Assumptions and scope
The parameter \(n\) is any integer at least three. All semigroups are additive submonoids of nonnegative integers. Gap blocks are maximal with respect to *consecutive integers*, not Apéry residue steps or factorization lengths. The long-block inequality is strict: blocks of length exactly \(n+1\) belong to the shorter class and are not listed as long. No assertion is made about the full length histogram of the remaining blocks; only their starts and their aggregate count are classified.

## Proof
**1. Normal form and Apéry thresholds.** The parity-dependent integers displayed in the finding satisfy
\[
a=dA,\qquad b=dB,\qquad c=dC+1,
\qquad A b=B a,\qquad d c=e b,
\]
where \(e=(n+3)/2\) for odd \(n\) and \(e=n+3\) for even \(n\). Any nonnegative combination of \(a,b,c\) can be reduced first modulo the relation \(dc=eb\), and then modulo \(Ab=Ba\), to \(xa+yb+zc\) with \(x\ge0\), \(0\le y<A\), and \(0\le z<d\). These \(Ad=a\) values \(yb+zc\) have pairwise distinct residues modulo \(a\): reduction modulo \(d\), using \(c\equiv1\pmod d\), determines \(z\); coprimality of \(A,B\) then determines \(y\). Consequently they constitute the full Apéry set relative to \(a\), and the least element of \(S_n\) congruent to \(r\pmod a\) equals \(w_r\). Equivalently,
\[
r+ka\in S_n\quad\Longleftrightarrow\quad k\ge\kappa_r
\qquad(k\ge0,\ 0\le r<a).
\]

**2. Exact starts and count.** A gap block begins immediately after some \(s=r+ka\in S_n\) if \(s+1\notin S_n\). When \(r=a-1\), \(s+1\) is a multiple of \(a\), so cannot begin a gap. For \(0\le r<a-1\), such a start occurs for each integer \(\kappa_r\le k<\kappa_{r+1}\); its first gap is \(r+ka+1\). Thus the number of starts at this residue transition is \(\max(0,\kappa_{r+1}-\kappa_r)\).

Suppose first that \(\ell=r\bmod d<d-1\). Since \(CB^{-1}\equiv2\pmod A\) for both parities, increasing \(r\) by one changes the Apéry coordinate to \(j_{r+1}\equiv j_r-2\pmod A\), while the other coordinate increases to \(\ell+1\). The triangular identity \(2b-c=a-1\) gives
\[
\kappa_{r+1}-\kappa_r=
\begin{cases}
B-1=H,&j_r=0\text{ or }1,\\
-1,&j_r\ge2.
\end{cases}
\]
For \(\ell=d-1\) and \(r<a-1\), the threshold difference is *negative*. Indeed, when \(n\) is even, \(j_r=t\) and \(j_{r+1}=t+1\), hence \(w_{r+1}-w_r=b-(d-1)c<0\). When \(n\) is odd, the change in \(j\) is at most \((A-1)/2=d-1\), so \(w_{r+1}-w_r\le(d-1)(b-c)<0\). Thus only interior digit transitions with \(j_r\in\{0,1\}\) produce starts, each producing *exactly* \(H\) starts; this establishes the displayed formula.

To count, let \(n\) be even. Then \(d-1=2A\), and for each of the \(A\) values of \(t\), among the \(2A\) values \(0\le\ell<2A\), the congruence \(j_r\equiv t-2\ell\pmod A\) has exactly four solutions with \(j_r\in\{0,1\}\) (for odd \(A\), each target has two solutions; for even \(A\), the uniquely parity-compatible target has four). There are \(4A\) eligible transitions and \(H=A\), giving \(R_n=4A^2=n^2\). For odd \(n\), one has \(A=n\) and \(d-1=(A-1)/2\); at each fixed \(\ell<d-1\), the map \(t\mapsto j_r\) permutes \(0,\ldots,A-1\), so exactly two \(t\)-values qualify. There are \(A-1\) eligible transitions and \(H=A+1\), yielding \(R_n=(A-1)(A+1)=n^2-1\).

**3. Separation of every long block by coin count.** Put \(u=b-a=n+1\) and \(v=c-a=2n+3=2u+1\). The semigroup elements expressed using exactly \(q\) generators form the finite set
\[
E_q=\{qa+iu+jv:i,j\ge0,\ i+j\le q\}
\subset[qa,qc],
\]
with both endpoints present. For each \(j=0,\ldots,q\), the part with fixed \(j\) is the progression
\[
qa+jv,\ qa+jv+u,\ldots,qa+jv+(q-j)u.
\]
Its successive gaps have length at most \(u-1\). The next progression begins at most \(u+1\) after the previous progression's maximum because
\[
[qa+(j+1)v]-[qa+jv+(q-j)u]
=v-(q-j)u\le u+1
\]
for \(j<q\). Its maximum is also greater than the previous maximum by \(v-u=u+1\). By induction over \(j\), *every two consecutive elements of \(E_q\) differ by at most \(u+1\)*; hence each gap internal to \([qa,qc]\) has length at most \(u\).

Across consecutive coin counts, the only possible new gap is between \(qc\) and \((q+1)a\), namely
\[
I_q=[qc+1,(q+1)a-1]\cap\mathbb Z,
\quad |I_q|=a-1-qv,
\]
when this length is positive. There can be no representation with fewer than \(q+1\) coins in this interval (such a sum is at most \(qc\)), or with more (such a sum is at least \((q+1)a\)). If two successive spans overlap or touch, their union preserves the bound \(u\) for internal gap lengths. Since \(qc-(q+1)a\) increases with \(q\), once spans overlap or touch they continue to do so. Therefore **all** gap blocks longer than \(u\) are precisely the \(I_q\) satisfying \(a-1-qv>u\).

For \(n\ge3\) and \(K=\lfloor(n+1)/4\rfloor\), elementary substitution of \(n+1=4K+r\), \(0\le r\le3\), shows
\[
a-1-(K-1)v>n+1\ \ge a-1-Kv.
\]
Since \(|I_q|\) decreases strictly with \(q\), the qualifying indices are exactly \(0\le q<K\). This proves the sharp long-block spectrum and completes the proof.

## Verification
`verify.py` is standalone Python 3 code. It independently uses Dijkstra's algorithm over residues modulo \(T_n\) to determine all Apéry minima, compares them with the explicit formula and every predicted start for \(3\le n\le120\), then independently enumerates every gap block through the Frobenius number for \(3\le n\le60\). For \(3\le n\le28\), it additionally checks every membership position using a separate coin-change dynamic program. The actual run printed `VERIFY_OK`, covering 583156 predicted starts and 73776 exhaustive gap blocks in the respective ranges. These finite tests detect implementation errors but do not replace the algebraic proof above. Run `python3 verify.py` to reproduce them.

## Relationship to prior work
Robles-Pérez and Rosales (2017) proved that the three-triangular-generator semigroup is free and computed its Apéry rectangle and Frobenius number (in particular, Corollary 28 supplies the rectangle used as an input above). Komatsu (2022) obtained higher-representation Frobenius thresholds and associated invariants for this same triple, not its adjacency-block geometry. The published *Isolated gaps in semigroups of three consecutive triangular numbers* classifies singleton gaps, meaning blocks of length one, but neither its statement nor its proof enumerates **all** gap starts and the exact long-block cutoff. Its rectangle and neighbor method are closely related to the start-count portion, so that portion alone is not presented as a wholly independent new framework. The long-block spectrum uses the distinct coin-count layer structure. Results on gap-block frequencies for binary numerical semigroups do not imply a corresponding three-generator triangular classification.

## Limitations
The theorem gives every start and the complete spectrum only of blocks strictly longer than \(n+1\); it does not give the lengths of all shorter blocks, nor classify nonconsecutive triangular triples. The structural ingredients are elementary and inherit the known Apéry rectangle; novelty is claimed only for the explicit combined block geometry after inspecting the named sources, not as an unrestricted priority certificate. A general desert-enumeration theorem or less-indexed semigroup table could still imply the stated formulas.

## References
A. M. Robles-Pérez and J. C. Rosales, *The Frobenius number for sequences of triangular and tetrahedral numbers* (first public 2017-06-14), https://arxiv.org/abs/1706.04378.

T. Komatsu, *The Frobenius number for sequences of triangular numbers associated with number of solutions* (first public 2022-06-27), https://arxiv.org/abs/2206.13054.

*Isolated gaps in semigroups of three consecutive triangular numbers*, published research result (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-isolated-gaps-in-semigroups-of-three-consecutive-triangular-numb--42c2c6edcb7c/RESULT.md.
