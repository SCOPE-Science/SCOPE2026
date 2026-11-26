# Triangular descent spectrum of Feng–Rao multiplicities for consecutive-generator semigroups

## Finding
For every integer \(n\ge 2\), let \(S_n=\langle n,n+1\rangle\subseteq\mathbb N_0\). For \(s\in S_n\), define
\[
\nu_n(s)=\#\{(u,v)\in S_n^2:u+v=s\},
\]
where the ordered pairs are counted with multiplicity one each. Let \(s^+\) be the immediate successor of \(s\) in the increasing enumeration of \(S_n\). Define a *descent* at \(s\) when \(\nu_n(s)>\nu_n(s^+)\), and its drop size as \(\nu_n(s)-\nu_n(s^+)\).

**Theorem.** The complete set of descents is
\[
\left\{s=nt+r:\ 1\le r\le n-2,\quad r+1\le t\le2r\right\}.
\]
Every such descent has \(s^+=s+1\) and exact drop size \(2r+1-t\). This is the complete list on both sides of the conductor; in particular, for \(n\ge 3\) some descents occur strictly past it. Consequently:
\[
\#\{s:\nu_n(s)>\nu_n(s^+)\}=\binom{n-1}{2},
\]
\[
\#\{s:\nu_n(s)-\nu_n(s^+)=d\}=n-1-d
\quad\text{for }1\le d\le n-2,
\]
with no larger drop, and the total decrease accumulated over all descending transitions is
\[
\sum_{\nu_n(s)>\nu_n(s^+)}(\nu_n(s)-\nu_n(s^+))=\binom n3.
\]
For \(n\ge3\), the final descent occurs at the explicit semigroup element \(2n^2-3n-2\). At \(n=2\) there are no descents.

## Assumptions and scope
This is a theorem of additive numerical semigroups. All variables \(n,t,r,d\) are integers with the ranges explicitly stated. The ordering is the increasing order on the *elements of the semigroup*, not all nonnegative integers; the term \(\nu_n(s)\) counts ordered decompositions, equivalently the divisor set used in the Feng–Rao bound. It does not count distinct factorizations of \(s\) into the generators.

The family is particularly natural for Hermitian one-point coding semigroups when \(n\) is a prime power, but the theorem is purely arithmetical and holds also when it is not. No assertion is made about minimum distances of particular codes.

## Proof
**1. Normal form and all values of \(\nu_n\).** Every \(s\in S_n\) has a unique expression
\[
s=an+r(n+1)=tn+r,
\quad 0\le r<n,\quad a=t-r\ge0.
\]
Existence follows by replacing \(n\) copies of \(n+1\) by \(n+1\) copies of \(n\); uniqueness follows by reduction modulo \(n\). Thus \(s=tn+r\), \(0\le r<n\), belongs to \(S_n\) precisely when \(t\ge r\).

Write both addends of \(s\) in normal form with remainders in \(\{0,\ldots,n-1\}\). If their remainders sum to \(r\), there are \(r+1\) choices of the ordered remainder pair and \(a+1\) choices of the ordered \(n\)-coefficient pair. If the remainders sum to \(n+r\), there are \(n-1-r\) choices of the remainder pair. In that case normalization introduces \(n+1\) extra copies of \(n\), leaving \(a-n-1\) to split, for \(\max(a-n,0)\) choices. No third case exists because the remainder sum is at most \(2n-2\). Therefore the exact identity at every nongap is
\[
\boxed{\nu_n(tn+r)=(t-r+1)(r+1)+(n-1-r)\max(t-r-n,0).}\tag{1}
\]

**2. Adjacent elements and exact differences.** Within a quotient block, when \(0\le r\le n-2\) and \(t\ge r+1\), both \(tn+r\) and \(tn+r+1\) lie in \(S_n\), and the second is the immediate successor. Subtracting (1), with the carry threshold handled on both sides, gives
\[
\nu_n(tn+r+1)-\nu_n(tn+r)=
\begin{cases}
t-2r-1,&t\le n+r,\\
1,&t\ge n+r+1.
\end{cases}\tag{2}
\]
At the end of a block, the successor is \((t+1)n\): the last remainder is \(\min(t,n-1)\). Substituting both points in (1) shows that the difference of their \(\nu_n\)-values is always \(+1\), including the transition into and beyond the conductor \(n(n-1)\). Hence every strict descent must be an interior transition in (2).

**3. Classification and enumeration.** The second case of (2) cannot descend. In the first case, a strict descent means \(t\le2r\); membership of both adjacent elements means \(t\ge r+1\). Since \(r\le n-2\), every \(t\le2r\) automatically satisfies \(t\le n+r\). Thus the exact necessary and sufficient conditions are \(1\le r\le n-2\), \(r+1\le t\le2r\), and the drop is \(2r+1-t\).

At each fixed \(r\), precisely \(r\) drops occur, of sizes \(r,r-1,\ldots,1\). Summing \(r\) over \(1,\ldots,n-2\) gives \(\binom{n-1}{2}\) descents. Each size \(d\) occurs once for each \(r=d,\ldots,n-2\), hence \(n-1-d\) times. Summing the triangular numbers \(r(r+1)/2\) gives \(\binom n3\). Finally, the last descent is obtained by taking \(r=n-2\) and \(t=2r\), which yields \(2n^2-3n-2\). These arguments cover all \(s\in S_n\), not merely a finite test range. QED.

## Verification
The accompanying standard-library Python checker `verify_descents.py` uses a reachability construction of each semigroup and independently counts every ordered pair of nongaps summing to each tested value. It checks, for every \(2\le n\le48\), every adjacent nongap up through \(2n(n-1)+n+2\), the complete normal-form count (1), every descent location and magnitude, and the aggregate identities. The checker passed in all 47 parameter cases, comprising 17,296 predicted descent locations. These finite checks corroborate the algebra; the proof establishes the unbounded statement.

To reproduce: `python3 verify_descents.py`.

## Relationship to prior work
Bras-Amorós (published June 2004; arXiv copy posted July 31, 2023) studies acute numerical semigroups and determines the **last** strict decrease of their Feng–Rao multiplicity sequence, using conductor and subconductor. Theorem 6.3 and Proposition 6.6 specialize for the symmetric semigroup \(S_n\), \(n\ge3\), to the last-descent location \(2c-2-n\), with \(c=n(n-1)\), agreeing with the final descent above. The present theorem instead supplies **every** descent and its exact magnitude and histogram. The prior last-descent result alone does not give that spectrum.

Delgado, Farrán, García-Sánchez and Llena study generalized Feng–Rao numbers of two-generator semigroups, obtaining their stable higher-weight behavior. Their results concern different order-bound invariants rather than the complete finite list of adjacent negative changes of \(\nu_n\). Earlier universal divisor-count formulas make individual evaluations possible but do not directly supply the stated triangular descent law without the normal-form analysis above.

## Limitations
The theorem does not assert new minimum-distance bounds, nor does it classify drops for arbitrary coprime generators \(\langle a,b\rangle\) with \(b>a+1\). Priority is assessed against accessible primary text and searches; a differently formulated older Hermitian-code computation or an unindexed table could imply the same finite-difference spectrum. No independent mathematical audit has been performed.

## References
1. M. Bras-Amorós, *Acute Semigroups, the Order Bound on the Minimum Distance and the Feng-Rao Improvements*, IEEE Transactions on Information Theory 50(6), June 2004, especially Theorem 6.3 and Proposition 6.6. ArXiv copy: https://arxiv.org/abs/2307.16448
2. M. Delgado, J. I. Farrán, P. A. García-Sánchez, D. Llena, *On the weight hierarchy of codes coming from semigroups with two generators*, arXiv:1306.2862, first posted June 12, 2013, especially Sections 2–3. https://arxiv.org/abs/1306.2862
3. J. I. Farrán, P. A. García-Sánchez, D. Llena, *On the Feng-Rao numbers*, 2010; available manuscript: https://www.academia.edu/54015844/On_the_Feng_Rao_numbers
4. C. Kirfel and R. Pellikaan, *The minimum distance of codes in an array coming from telescopic semigroups*, IEEE Trans. Inform. Theory 41 (1995), cited for the underlying general divisor-count identity by reference 1.
