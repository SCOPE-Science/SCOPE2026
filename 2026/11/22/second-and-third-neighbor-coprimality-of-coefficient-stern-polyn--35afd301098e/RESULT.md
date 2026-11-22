# Second- and third-neighbor coprimality of coefficient-Stern polynomials

## Finding
Let \(s(0)=0\), \(s(1)=1\), and let Stern's diatomic sequence satisfy
\[
s(2j)=s(j)\quad(j\ge1),\qquad s(2j+1)=s(j)+s(j+1)\quad(j\ge1).
\]
For every integer \(n\ge0\), define the coefficient-Stern polynomial
\[
P_n(X)=\sum_{j=1}^{n+1}s(j)X^{n+1-j}\in\mathbb Z[X].
\]
Then, for **each** integer \(n\ge0\) and **both** offsets \(d\in\{2,3\}\),
\[
\gcd_{\mathbb Q[X]}(P_n(X),P_{n+d}(X))=1,
\qquad
\operatorname{Res}_X(P_n,P_{n+d})\ne0.
\]
Thus the first two previously unclassified neighbor offsets after the known adjacent resultant have no common complex roots at any index. The statements are over characteristic zero and make no assertion at greater offsets or upon reducing coefficients modulo a prime.

## Assumptions and scope
All indices are nonnegative integers; \(P_0(X)=1\). Polynomial gcds are over \(\mathbb Q[X]\), and resultants are the usual Sylvester determinants over \(\mathbb Z\). Every \(P_n\) is monic of degree \(n\). No conjecture or numerical root approximation is used. The only general external ingredient in the proof is the classical Eneström–Kakeya positive-coefficient root bound; a convenient explicit version is stated and justified below.

## Proof
**1. Elementary Stern facts.** For every \(k\ge1\),
\[
\gcd(s(k),s(k+1))=1.
\]
This follows by induction on \(k\): an even index reduces the gcd to the adjacent pair at \(k/2\), and an odd index reduces it to the pair at \((k-1)/2\). All positive-index values are positive. Further, \(s(k)=1\) exactly at the powers of two: even indices halve repeatedly, whereas an odd index greater than one has value at least two. Iterating the odd recurrence gives
\[
s(2^h+1)=h+1\qquad(h\ge1).
\]
For every \(k\ge1\), an induction on binary length gives
\[
\frac{s(k+1)}{s(k)}\le1+\lfloor\log_2 k\rfloor.
\]
Indeed at \(k=2r\) the left side is \(1+s(r+1)/s(r)\), while at odd \(k=2r+1\ge3\) it is \(s(r+1)/(s(r)+s(r+1))<1\); the base case is \(k=1\).

If \(a_0,\ldots,a_N>0\), every zero of \(a_0X^N+\cdots+a_N\) has modulus at most \(\max_{j<N}a_{j+1}/a_j\). This is the standard Eneström–Kakeya upper bound, valid even if the ratios are not monotone. Consequently, when \(1\le n\le2^h-1\), every zero of \(P_n\) satisfies \(|X|\le h\), because its consecutive coefficient ratios obey the preceding binary-length bound.

**2. Offset two.** The defining coefficient shift yields
\[
P_{n+2}(X)=X^2P_n(X)+s(n+2)X+s(n+3).
\]
Suppose \(P_n\) and \(P_{n+2}\) had a common zero \(\alpha\) with \(n\ge1\). It would have to be the rational number
\[
\alpha=-\frac{s(n+3)}{s(n+2)}.
\]
Adjacent Stern values are coprime, and \(P_n\) is monic with integral coefficients. By the rational-root theorem, \(s(n+2)=1\). Hence \(n+2=2^h\) for some \(h\ge2\), so \(n=2^h-2\) and \(\alpha=-(h+1)\). But \(2^{h-1}\le n<2^h\), so every zero of \(P_n\) has modulus at most \(h\), contradicting \(|\alpha|=h+1\). For \(n=0\) there is no common root since \(P_0=1\).

**3. Offset three: even indices.** Another coefficient shift gives
\[
P_{n+3}(X)=X^3P_n(X)+Q_n(X),\quad
Q_n(X)=s(n+2)X^2+s(n+3)X+s(n+4).
\]
For \(n=2r\), the Stern recurrence factors the remainder as
\[
Q_{2r}(X)=(X+1)\bigl(s(r+1)X+s(r+2)\bigr).
\]
Both its zeros are real. But \(P_{2r}\) has no real zero. To see this without assuming a separate theorem, for \(r\ge1\) the Stern recurrence gives the identity
\[
P_{2r}(X)=(1+X+X^2)P_{r-1}(X^2)+s(r+1).
\]
The right side is strictly positive for every real \(X\), because \(1+X+X^2>0\), \(P_{r-1}(X^2)>0\), and \(s(r+1)>0\). For \(r=0\) the claim follows from \(P_0=1\). Thus \(P_{2r}\) and \(P_{2r+3}\) share no complex root.

**4. Offset three: odd indices.** Write \(n=2r+1\) and \(u=s(r+1)\), \(v=s(r+2)\), \(w=s(r+3)\). All three are positive. Then
\[
Q_{2r+1}(X)=(u+v)X^2+vX+(v+w).
\]
Its discriminant is \(v^2-4(u+v)(v+w)<0\), so it is irreducible over \(\mathbb Q\). It is also primitive in \(\mathbb Z[X]\), since
\[
\gcd(u+v,v,v+w)=\gcd(u,v)=1.
\]
Its leading coefficient \(u+v\) exceeds one. If it shared a root with \(P_{2r+1}\), irreducibility would force \(Q_{2r+1}\) to divide \(P_{2r+1}\) over \(\mathbb Q[X]\). By Gauss's lemma, the primitive polynomial \(Q_{2r+1}\) would then divide it over \(\mathbb Z[X]\). This is impossible: its leading coefficient \(u+v>1\) cannot divide the leading coefficient one of \(P_{2r+1}\). This completes the proof for both offsets and every index. \(\square\)

## Verification
The included standalone \(\texttt{verify.py}\) uses only Python's standard library. It constructs the first 132 coefficient-Stern polynomials exactly, verifies coefficient shifts and the displayed even-degree identity, checks the Stern coprimality and odd-quadratic arithmetic, and establishes gcd one by Euclidean division over explicitly specified finite fields for each offset at every \(0\le n<128\). A separate exact rational-polynomial calculation also checked both offsets at \(0\le n\le81\). These finite checks detect transcription or indexing mistakes; the unrestricted theorem rests on the preceding proof, not on extrapolation from the sample.

## Relationship to prior work
Dilcher and Ericksen introduced and investigated **this coefficient-defined polynomial family** in their 2021 paper. Their Proposition 20 establishes the exact adjacent resultant
\[
\operatorname{Res}_X(P_n,P_{n+1})=s(n+2)^n,
\]
and their Propositions 10 and 14 supply root location and even-degree positivity. The current proof rederives the special bounds needed, so those results are credited rather than presented as discoveries. The cited article does not state the universal offset-two or offset-three coprimality assertion and expressly leaves more general pairwise resultant identities unidentified.

The different Stern polynomials defined recursively by \(B_{2j}(t)=tB_j(t)\), \(B_{2j+1}(t)=B_j(t)+B_{j+1}(t)\), and the Dilcher–Stolarsky \((0,1)\)-polynomials, have **different objects** and do not imply this coefficient-family coprimality result. A targeted comparison with indexed results using the same word “Stern” found no stronger statement covering both offsets in the present family; such searches alone do not establish priority.

## Limitations
No exact closed formula or sign law for these nonadjacent resultants is claimed, only their nonvanishing. The argument does not prove pairwise coprimality for all separations, does not extend to arbitrary coefficient sequences, and does not prohibit common roots after reduction modulo a prime. The originality assessment may miss unpublished or unindexed results; no independent audit has been performed.

## References
1. K. Dilcher and L. Ericksen, *Polynomials Whose Coefficients Are Stern Numbers*, *Journal of Integer Sequences* **24** (2021), Article 21.10.3, first published November 25, 2021. https://cs.uwaterloo.ca/journals/JIS/VOL24/Dilcher/dilcher51.html ; full text: https://cs.uwaterloo.ca/journals/JIS/VOL24/Dilcher/dilcher51.pdf
2. K. Dilcher and L. Ericksen, *Reducibility and irreducibility of Stern (0,1)-polynomials*, *Communications in Mathematics* **22** (2014), 77–102. https://dml.cz/handle/10338.dmlcz/143908
3. OEIS A002487, Stern's diatomic sequence. https://oeis.org/A002487
