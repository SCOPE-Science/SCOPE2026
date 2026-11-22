# Sharp logarithmic transition discrepancy in the base-\(3/2\) digit-parity word

## Finding
Let \(w=w_0w_1\cdots\) be the unique infinite binary word starting in \(0\) and fixed by the two-to-three block rule
\[
00,01\longmapsto010,\qquad10,11\longmapsto101.
\]
For \(ab\in\{01,10\}\), put
\[
Q_{ab}(M)=\#\{0\le j<M:(w_j,w_{j+1})=(a,b)\}.
\]
There is an absolute constant \(C\) such that, for both \(ab=01\) and \(ab=10\) and all integers \(M\ge1\),
\[
\left|Q_{ab}(M)-\frac{2M}{5}\right|\le C\log(M+2).
\]
**The logarithmic order is optimal:** for each of these two ordered patterns there are constants \(c>0\) and \(X_0\) such that for every real \(X\ge X_0\),
\[
 c\log X\le\max_{1\le M\le X}\left|Q_{ab}(M)-\frac{2M}{5}\right|\le C\log(X+2).
\]
In particular, each transition \(01\) and \(10\) has natural frequency \(2/5\). The new assertion is the *sharp quantitative order of prefix discrepancy*, not solely these limiting frequencies.

An exact auxiliary relation is given below: with the binary word \(t_n=w_{2n}\), its signed adjacency sum \(P(N)\), and \(D(N)=5P(N)-N\),
\[
Q_{01}(3N)-\frac{6N}{5}=-\frac{D(N)}{20}+\frac{t_N-t_0}{2},\qquad
Q_{10}(3N)-\frac{6N}{5}=-\frac{D(N)}{20}-\frac{t_N-t_0}{2}.
\]
The integer \(D(N)\) has logarithmic-sized maximal fluctuations and satisfies an explicit shrinking-index recurrence.

## Assumptions and scope
The word \(w\) is the sequence OEIS A357448: equivalently, \(w_n\) is the parity of the sum of digits in the unique rational-base representation
\[
n=\sum_{j\ge0}d_j(3/2)^j,\qquad d_j\in\{0,1,2\}.
\]
The block map acts on successive nonoverlapping input pairs; its images depend only on the first letter. Equivalently,
\[
w_{3m}=w_{3m+2}=w_{2m},\qquad w_{3m+1}=1-w_{2m}\quad(m\ge0),\qquad w_0=0.
\]
These identities determine the infinite word by induction. Indices, pattern starts and prefix lengths are zero-based. A pattern beginning at position \(M-1\) uses the symbol at position \(M\); there is no circular wraparound. The logarithm is natural. The theorem concerns the two *oriented transitions* \(01\) and \(10\), not every factor length or the one-letter discrepancy.

## Proof
**1. Auxiliary word and exact signed recurrence.** Define \(t_n=w_{2n}\). By the displayed rule for \(w\), each triple in \(w\) is \(t_n(1-t_n)t_n\); hence
\[
w=\phi(t),\qquad\phi(0)=010,\quad\phi(1)=101.
\]
Applying the same rule at the indices \(6m\), \(6m+2\), and \(6m+4\) gives
\[
t_{3m}=t_{3m+1}=t_{2m},\qquad t_{3m+2}=1-t_{2m+1}.
\]
Let \(\epsilon_j=1\) if \(t_j=t_{j+1}\) and \(\epsilon_j=-1\) otherwise, and \(P(N)=\sum_{0\le j<N}\epsilon_j\), with \(P(0)=0\). The three identities for \(t\) imply
\[
(\epsilon_{3m},\epsilon_{3m+1},\epsilon_{3m+2})
=(1,-\epsilon_{2m},-\epsilon_{2m+1}).
\]
Summing complete triples and then one or two further entries yields, for all \(m\ge0\),
\[
\begin{aligned}
P(3m)&=m-P(2m),\\
P(3m+1)&=m-P(2m)+1,\\
P(3m+2)&=m-P(2m)+1-\epsilon_{2m}.
\end{aligned}
\]
With \(D(N)=5P(N)-N\), these are equivalent to
\[
\begin{aligned}
D(3m)&=-D(2m),\\
D(3m+1)&=-D(2m)+4,\\
D(3m+2)&=-D(2m)+3-5\epsilon_{2m}.
\end{aligned}\tag{1}
\]
The last additive term is either \(-2\) or \(8\). Every recursive argument \(2\lfloor N/3\rfloor\) is strictly smaller than \(N\) when \(N>0\), and is at most \(2N/3\). Using \(D(0)=0\), \(D(1)=4\), \(D(2)=-2\), iteration of (1) proves, for instance,
\[
|D(N)|\le 8\bigl(1+\lceil\log_{3/2}(N+2)\rceil\bigr).\tag{2}
\]
Thus the signed adjacency discrepancy is \(O(\log(N+2))\), without assuming the existence of any limiting frequency.

**2. Transfer to the oriented transitions of \(w\).** Each \(\phi(t_j)\) contributes exactly one \(01\) and exactly one \(10\) at its two internal starts. At the boundary between \(\phi(t_j)\) and \(\phi(t_{j+1})\), the oriented pair is exactly \(t_jt_{j+1}\). Set \(A_{ab}(N)=\#\{0\le j<N:t_jt_{j+1}=ab\}\). Then
\[
Q_{01}(3N)=N+A_{01}(N),\qquad Q_{10}(3N)=N+A_{10}(N).
\]
Since \(A_{01}+A_{10}=(N-P(N))/2\) and \(A_{01}-A_{10}=t_N-t_0\), the two formulas stated in the Finding follow exactly. The endpoint term has absolute value at most \(1/2\). A prefix length not divisible by three differs from the preceding multiple by at most two pattern starts, giving \(Q_{ab}(M)=2M/5+O(\log(M+2))\) for \(ab=01,10\). This establishes the upper bound and existence of both frequencies.

**3. A constructed logarithmic lower bound.** It remains to prove that the upper bound cannot be replaced by \(o(\log X)\) uniformly over all prefixes up to \(X\). For each \(k\ge1\), choose \(m_0\) by the Chinese remainder theorem so that
\[
5m_0+6\equiv0\pmod{4^k},\qquad m_0\equiv0\pmod3,\qquad 1\le m_0\le3\cdot4^k.
\]
Such a unique positive representative exists because \(5\) is invertible modulo \(4^k\) and \(3\) is coprime to \(4^k\). Define, for \(0\le j<k\),
\[
m_{j+1}=\frac{9m_j+6}{4}.
\]
The identity \(5m_{j+1}+6=9(5m_j+6)/4\) shows inductively that \(5m_j+6\) remains divisible by \(4^{k-j}\). Thus \(m_j\equiv2\pmod4\) for \(j<k\); in particular all the displayed steps are integers. Moreover each \(m_j\) is divisible by three, since \(4m_{j+1}=9m_j+6\).

Set \(v_j=(3m_j+2)/2\). Because \(m_j\equiv2\pmod4\), \(v_j\) is an even integer and \(2m_{j+1}=3v_j\). Since \(3\mid m_j\), the index \(2m_j\) is a multiple of three. The recurrence for \(t\) then gives \(t_{2m_j}=t_{2m_j+1}\), hence \(\epsilon_{2m_j}=1\). Apply (1) first with index \(3m_j+2=2v_j\), then with index \(3v_j=2m_{j+1}\):
\[
D(2v_j)=-D(2m_j)-2,\qquad
D(2m_{j+1})=-D(2v_j)=D(2m_j)+2.
\]
After \(k\) steps,
\[
D(2m_k)-D(2m_0)=2k.\tag{3}
\]
At least one of the two absolute values on the left is at least \(k\). Further,
\[
m_k=\left(\frac94\right)^k\left(m_0+\frac65\right)-\frac65
\le 5\cdot9^k,
\]
so \(6\max(m_0,m_k)\le30\cdot9^k\). Apply the exact transfer identities in Step 2 at \(N=2m_0\) and \(N=2m_k\). For each of the patterns \(01\) and \(10\), at least one of these two prefix lengths \(M=6m_0,6m_k\) satisfies
\[
\left|Q_{ab}(M)-\frac{2M}{5}\right|\ge\frac{k}{20}-\frac12,
\qquad M\le30\cdot9^k.\tag{4}
\]
Given any sufficiently large \(X\), choose \(k=\lfloor\log_9(X/30)\rfloor\). Inequality (4) gives
\[
\max_{1\le M\le X}\left|Q_{ab}(M)-\frac{2M}{5}\right|
\ge\frac{\log X}{20\log9}-O(1).
\]
Combined with the upper bound this proves the claimed sharp \(\Theta(\log X)\) order for both oriented transitions. The proof is infinite and does not depend on finite computational sampling.

## Verification
The included `verify.py` constructs the rational-base parity digits directly by the digit-extraction recursion \(n=3q+r\mapsto(2q,r)\), independently compares them with the block-derived auxiliary word on 120,000 indices, checks 30,000 exact signed sums, 10,000 pair-count transfer identities for each pattern, and runs 18 full CRT witness chains with exact integer arithmetic. Run `python3 verify.py` in the directory containing this file and the script. All checks passed during preparation; the proof above establishes the universally quantified claims.

## Relationship to prior work
Dekking's 2022 OEIS entry A357448 and its 2023 article establish the digit-parity word and conjecture two-letter frequencies, including \(\mu[01]=2/5\). Cassaigne, Espinoza, Rigo and Stipulanti (2026) prove the one-letter balance and show that two-letter frequencies of the related half-scaled word remained a natural quantitative question; they discuss the expected two-letter values but do not state a sharp prefix discrepancy order. A published all-order run-statistics result for that half-scaled word proves rational limiting run-pattern frequencies, which can imply the limiting transition density, but contains no logarithmic prefix-error bound or matching lower construction. Thus the novelty claim here is confined to the **optimal discrepancy rate** for the specifically defined 2022 word; simple recovery of its limiting frequencies alone would be covered. The classical base-two Thue–Morse frequency and discrepancy statements concern a different sequence.

## Limitations
Only the two ordered patterns \(01\) and \(10\) are treated. The sharp statement is an order-of-growth result for the *maximal absolute prefix error*, not an exact leading constant, an asymptotic value for individual prefixes, or a bound for all factor frequencies. The cited literature comparison is limited to accessible indexed and primary material; an unindexed quantitative argument could affect scholarly priority. No independent external audit or certification is claimed.

## References
1. M. Dekking, OEIS A357448, *Fixed point starting with 0 of the two-block substitution*, approved 2022-09-30; https://oeis.org/A357448 and https://oeis.org/history?seq=A357448&start=10.
2. F. M. Dekking, *The Thue–Morse sequence in base 3/2*, arXiv:2301.13563, first posted 2023-01-31; https://arxiv.org/html/2301.13563v1.
3. J. Cassaigne, B. Espinoza, M. Rigo, M. Stipulanti, *Symbols frequencies in the Thue–Morse word in base 3/2 and related conjectures*, arXiv:2602.21895, first posted 2026-02-25; https://arxiv.org/abs/2602.21895.
4. *All-order rational run statistics and the exact five-state run-transition law for the base-\(3/2\) Thue–Morse word*, public result dated 2026-11-08; https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-all-order-rational-run-statistics-and-the-exact-five-state-run-t--03f7bfb4e7e7.
