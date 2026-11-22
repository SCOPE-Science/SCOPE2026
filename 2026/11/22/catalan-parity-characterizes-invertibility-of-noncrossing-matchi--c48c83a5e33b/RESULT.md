# Catalan parity characterizes invertibility of noncrossing-matching convolution

## Finding
For every integer \(n\ge1\), let \(\mathcal N_n\) be the noncrossing perfect matchings of the vertices \(0,1,\ldots,2n-1\) of a strictly convex polygon. Define the eligible edge set
\[
E_n=\{\{a,b\}:0\le a<b<2n,\ b-a\equiv1\pmod2\},
\qquad |E_n|=n^2.
\]
Write \(G_n=\mathbb F_2^{E_n}\) and identify each matching with its binary edge-incidence vector. Let \(f_n:G_n\to\{0,1\}\) be the indicator of these vectors and \(T_nh=f_n*h\) their unnormalized counting-convolution operator.

**Theorem.** For every \(n\ge1\),
\[
\boxed{T_n\text{ is invertible over }\mathbb C\iff n=2^k-1\text{ for some }k\ge1.}
\]
At the invertible orders every signed Fourier multiplier is odd. At all other orders the proof explicitly constructs a vanishing multiplier using only reflection and smaller noncrossing matchings. This is a complete invertibility criterion, not a complete eigenvalue-multiplicity classification.

## Assumptions and scope
A perfect matching consists of \(n\) pairwise disjoint chords covering all \(2n\) vertices, and noncrossing means their relative interiors do not intersect. Any chord in such a matching joins an even vertex to an odd vertex: each of its complementary polygonal arcs contains an even number of unmatched vertices. The eligible chords therefore include every possible edge in \(\mathcal N_n\).

For any chord frequency \(S\subseteq E_n\), define the unnormalized Walsh coefficient
\[
W_n(S)=\sum_{M\in\mathcal N_n}(-1)^{|S\cap M|}.
\]
The characters \(\chi_S(x)=(-1)^{\sum_{e\in S}x_e}\) diagonalize counting convolution on \(G_n\), with eigenvalues \(W_n(S)\). Thus the theorem is equivalent to the zero-free classification of this signed enumerator. The total number of matchings is the Catalan number \(C_n=\binom{2n}{n}/(n+1)\).

## Proof
**Step 1: Catalan parity by reflection.** Define the polygon reflection \(\rho(0)=0\), \(\rho(i)=2n-i\) for \(1\le i<2n\), and extend it to chords and matchings. Every partner \(j\) of vertex \(0\) must be odd. If \(n\) is even, no such \(j\) is fixed by reflection: the reflected partner is \(2n-j\), so the matchings pair off. Hence \(C_n\) is even. If \(n=2m+1\) is odd, the noncentral partner classes still pair off, while the central class, comprising matchings containing \(\{0,n\}\), has \(C_m^2\) elements. Consequently
\[
C_{2m+1}\equiv C_m^2\equiv C_m\pmod 2.
\]
Beginning with \(C_1=1\), this recurrence proves that \(C_n\) is odd exactly when \(n\) is obtained by iterating \(m\mapsto2m+1\) from \(1\), i.e., \(n=2^k-1\). For odd \(C_n\), every sum \(W_n(S)\) is the sum of an odd number of signs and therefore is a nonzero odd integer. Thus every such convolution is invertible.

**Step 2: An explicit zero at every even order.** For even \(n\), take
\[
R_n=\{\{0,j\}:1\le j<n,\ j\text{ odd}\}.
\]
For each matching \(M\), vertex \(0\) is paired with exactly one odd \(j\). Its partner in \(\rho M\) is \(2n-j\), so exactly one of these two root chords lies in \(R_n\). The reflection has no fixed matching at even \(n\), and
\[
(-1)^{|R_n\cap\rho M|}=-(-1)^{|R_n\cap M|}.
\]
Thus \(W_n(R_n)=0\).

**Step 3: Odd orders inherit a zero from the half-size.** Suppose \(n=2m+1\) and a chord set \(S_m\subseteq E_m\) satisfies \(W_m(S_m)=0\). Embed the \(2m\) vertices of the smaller polygon as \(1,\ldots,2m\) by \(\iota(a)=a+1\). Write \(L=\iota(S_m)\) and take the reflection-invariant non-root set \(B=L\cup\rho(L)\). Then set
\[
S_n=R_n\cup B,
\qquad R_n=\{\{0,j\}:1\le j<n,\ j\text{ odd}\}.
\]
For any matching whose root partner is not \(n\), reflection exchanges two partner classes. Membership parity in \(B\) is reflection-invariant, whereas exactly one member of the reflected root-chord pair lies in \(R_n\). Therefore contributions from all noncentral matchings cancel in pairs. A matching with central chord \(\{0,n\}\) splits uniquely into one noncrossing matching on each of the two consecutive \(2m\)-vertex blocks. The two block signed sums are both \(W_m(S_m)\) (one is read in reflected vertex order), so their combined contribution is
\[
W_m(S_m)^2=0.
\]
Thus \(W_n(S_n)=0\).

**Step 4: Termination.** If \(n\) is not one less than a positive power of two, repeatedly applying \(n\mapsto(n-1)/2\) as long as \(n\) is odd must eventually reach a positive even integer. Otherwise the process reaches \(1\), which would force \(n=2^k-1\). The even-order construction in Step 2 and the odd lifting in Step 3 therefore produce a vanishing Fourier multiplier at every remaining order. A zero diagonal eigenvalue makes \(T_n\) singular, establishing both directions.

## Verification
The accompanying standard-library checker `verify_noncrossing_walsh.py` replays the reflection witness construction and exact signed-Catalan interval recurrence for every \(1\le n\le30\). It confirms that each non-Mersenne order has a zero witness. It also exhaustively enumerates the entire character group at orders \(n=1,2,3,4\), finding respectively \(0,8,0,15104\) vanishing multipliers (the corresponding group sizes are \(2,16,512,65536\)). These checks are finite and do not establish the all-size theorem independently of the proof above.

Reproduce with `python3 verify_noncrossing_walsh.py` using only Python's standard library. No floating-point arithmetic is used. The general conclusion rests on the pairing and factorization arguments, not on extrapolation from tested sizes.

## Relationship to prior work
The classical enumeration \(|\mathcal N_n|=C_n\) is given explicitly in Asinowski's 2015 paper and is not new here. Lin's 2010 archival paper states the Catalan oddness classification; it provides the sufficiency implication through parity, but does not derive the converse Fourier cancellation via an explicit character. DeCorte, de Laat, and Vallentin (2013) develop Fourier methods for finite-group Cayley graphs, without treating this particular convolution family.

A distinct published result, *Integral Fourier identifiability from noncrossing perfect matchings*, proves full rank of the **centered degree-one edge sampling covariance**, namely \((n-1)^2\), and integral spanning by incidence differences. That restricted Gram rank does not determine whether all \(2^{n^2}\) convolution eigenvalues vanish or survive; the present theorem settles that separate global invertibility question. Other published perfect-matching Walsh results concern unrestricted matchings of a complete graph rather than noncrossing matchings. A binary Dyck-word singleton-character result uses step coordinates, not the chord-incidence convolution here.

## Limitations
No exact general nullity, nonzero singular-value spectrum or stability bound is established at singular orders. The result is for the incidence indicator of **all** noncrossing perfect matchings in convex position, using the natural binary chord group; arbitrary planar point configurations, weighted matchings and restricted matching families are not covered. Literature comparisons were bounded: a historical signed Temperley–Lieb or Catalan enumerator could encode the same character cancellation under a different name. The finding has not undergone independent mathematical audit.

## References
1. H.-Y. Lin, *The odd Catalan numbers modulo \(2^k\)*, arXiv:1012.1756v1, first posted 2010-12-08. https://arxiv.org/abs/1012.1756
2. E. DeCorte, D. de Laat, F. Vallentin, *Fourier analysis on finite groups and the Lovász theta-number of Cayley graphs*, arXiv:1307.5703v1, first posted 2013-07-22. https://arxiv.org/abs/1307.5703
3. A. Asinowski, *The number of non-crossing perfect plane matchings is minimized (almost) only by point sets in convex position*, arXiv:1502.05332v1, first posted 2015-02-18. https://arxiv.org/abs/1502.05332
4. *Integral Fourier identifiability from noncrossing perfect matchings*, published mathematical result, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-fourier-identifiability-from-noncrossing-perfect-matchi--e353f7965df9
