# Reznick’s Stern divisibility conjecture for moduli \(22\) and \(27\)

## Finding
Let the Stern sequence be defined by \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\) for \(n\ge1\), and \(s(2n+1)=s(n)+s(n+1)\) for \(n\ge0\). Write
\[
T(N;d,0)=\#\{0\le n<N:s(n)\equiv0\pmod d\}.
\]
For **every integer** \(r\ge0\),
\[
\boxed{T(2^r;22,0)=T(2^r;27,0).}
\]
This proves the particular equality conjectured by Reznick in his 2006 manuscript, where it was verified only through \(r=19\).

## Assumptions and scope
The indices are all nonnegative integers; in particular \(n=0\) contributes one multiple of both moduli. The assertion concerns **dyadic initial segments** only. It does not claim equality on arbitrary initial segments, equality term by term, or a common residue distribution for all moduli.

## Proof
**1. Finite-state reduction.** For an integer \(d\ge2\), set
\[
V_d=\{(a,b)\in(\mathbb Z/d\mathbb Z)^2:\gcd(a,b,d)=1\}.
\]
Define \(L_d(a,b)=(a,a+b)\) and \(R_d(a,b)=(a+b,b)\), with coordinates reduced modulo \(d\). Both preserve \(V_d\). The consecutive Stern pair \((s(n),s(n+1))\) is primitive for every \(n\), since its two entries have gcd one. Moreover, the Stern recurrences give
\[
(s(2n),s(2n+1))=L_d(s(n),s(n+1)),\quad
(s(2n+1),s(2n+2))=R_d(s(n),s(n+1))
\]
modulo \(d\). Every integer in \([0,2^r)\) corresponds to exactly one binary word of length \(r\), including leading zeroes, acting from \((0,1)\) by \(L_d\) and \(R_d\).

Let \(M_d\) be the \(|V_d|\)-dimensional integer transition operator on basis vectors \(e_{(a,b)}\) defined by
\[
M_d e_{(a,b)}=e_{L_d(a,b)}+e_{R_d(a,b)}.
\]
Let \(u_d=e_{(0,1)}\), and let \(h_d\) be the row vector equal to one at exactly those states with first coordinate zero. Then, for all \(r\ge0\),
\[
T(2^r;d,0)=h_dM_d^r u_d.
\]
The cardinalities of the two primitive state sets are
\[
|V_{22}|=22^2(1-2^{-2})(1-11^{-2})=360,
\quad |V_{27}|=27^2(1-3^{-2})=648.
\]

**2. An unconditional finite verification bound.** Form the block-diagonal integer operator \(M=M_{22}\oplus M_{27}\), of dimension \(1008\), and the fixed column \(u=(u_{22},u_{27})\) and row \(h=(h_{22},-h_{27})\). Define \(a_r=hM^r u\). By Cayley–Hamilton, the degree-\(1008\) monic characteristic polynomial of \(M\) annihilates \(M\). Therefore \((a_r)\) obeys a monic, homogeneous, constant-coefficient linear recurrence of order at most \(1008\). In particular,
\[
(a_0=a_1=\cdots=a_{1007}=0)\ \Longrightarrow\ (\forall r\ge0,\ a_r=0).
\]
Thus an **exact integer** check at those \(1008\) indices is an exhaustive finite certificate for the full infinite theorem.

**3. Exact certificate.** The accompanying standalone program `verify_stern_22_27.py` constructs both primitive state sets directly, checks their sizes, generates the distributions by the two explicit transitions, and checks
\[
h_{22}M_{22}^r u_{22}=h_{27}M_{27}^r u_{27}
\qquad(0\le r\le1007)
\]
using unbounded Python integers. It independently repeats the entire \(1008\)-level calculation on the full residue-pair grids, and compares the first \(19\) levels with direct scalar Stern terms. All checks pass. Together with Step 2, this proves the formula for every \(r\ge0\).

## Verification
Execute `python3 verify_stern_22_27.py` using Python 3 and only its standard library. The reported output includes `VERIFY_OK`, `states22=360`, `states27=648`, `exact_levels=0..1007`, `independent_full_grid=PASS`, `direct_Stern_levels=0..18`, and the SHA-256 digest of the newline-delimited exact counts, `e7ca1f54991a09ebd233ffc4a45d8d30cfb2e37be2337307e037ddb3a924bd8d`.

The first ten common counts (for \(r=0,\ldots,9\)) are \(1,1,1,1,1,1,1,1,5,13\). The numerical check is finite, but the proof is not an inference from experiments: the dimension bound and Cayley–Hamilton reduce the universal statement to the checked finite certificate.

## Relationship to prior work
Reznick's *Regularity Properties of the Stern Enumeration of the Rationals* defines exactly this counting function and explicitly conjectures equality for moduli \(22\) and \(27\) (equation after (1.15)). He proves asymptotic frequencies by finite-state transition matrices, observes equal limiting densities \(1/36\), and reports direct confirmation only through \(r=19\). His paper proves distinct equalities for smaller moduli, not the present identity. The transition construction and Cayley–Hamilton principle are classical and are not presented as new; the new content is the **complete and independently checked finite certificate** settling the specified open equality.

Lansing's 2014 thesis, especially Chapter 4, studies distributions by **magnitude** of Stern values, not exact counts of multiples of two different moduli. Her 2013 article's abstract likewise concerns magnitude distributions. None of these inspected statements yields the claimed dyadic congruence identity. The possibility of an unlocated equivalent proof remains a historical-priority limitation.

## Limitations
The argument is computer-assisted with a fully self-contained exact-arithmetic finite certificate; no shorter symbolic characteristic-polynomial identity is asserted. It resolves exactly the equality of these two modular zero-counts on dyadic prefixes; stronger termwise congruences or arbitrary-length equalities are neither proved nor claimed. Independent mathematical auditing and comprehensive priority certification have not been performed.

## References
1. B. Reznick, *Regularity properties of the Stern enumeration of the rationals*, arXiv:math/0610601, first posted 2006-10-19; *Journal of Integer Sequences* 11 (2008), Article 08.4.1. https://arxiv.org/abs/math/0610601
2. J. Lansing, *On the Stern sequence and a related sequence*, PhD dissertation, University of Illinois, 2014, Chapter 4. https://oeis.org/A240388/a240388.pdf
3. J. Lansing, *Distribution of Values of the Binomial Coefficients and the Stern Sequence*, *Journal of Integer Sequences* 16 (2013), Article 13.3.7. https://cs.uwaterloo.ca/journals/JIS/VOL16/Lansing/lansing3.html
