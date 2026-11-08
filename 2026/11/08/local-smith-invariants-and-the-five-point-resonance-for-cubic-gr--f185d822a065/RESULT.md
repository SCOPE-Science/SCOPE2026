# Local Smith invariants and the five-point resonance for cubic-graph Fourier sampling

## Finding
Let \(p\ge5\) be prime, \(c\in\mathbb F_p^\times\), and \(\zeta=\exp(2\pi i/p)\). On the cubic graphs \(C_1=\{(s,s^3):s\in\mathbb F_p\}\) and \(C_c=\{(t,ct^3):t\in\mathbb F_p\}\), the square Fourier pairing matrix is
\[
M_{p,c}(s,t)=\zeta^{st+cs^3t^3},\qquad s,t\in\mathbb F_p.
\]
Set \(N=p-1\). For integers \(1\le t\le N-1\), define
\[
h(t)=\min\{j\ge1:j\le t\le3j,\ j\equiv t\pmod2\}
=2\lfloor t/6\rfloor+\eta_{t\bmod6},\quad
(\eta_0,\ldots,\eta_5)=(0,1,2,1,2,3),
\]
and define \(e=2\lceil N/6\rceil\). Write \(\pi=\zeta-1\) in the discrete valuation ring \(\mathcal O=\mathbb Z_p[\zeta]\), normalized by \(v_\pi(\pi)=1\).

**Complete classification.** For every prime \(p\ge7\) and every \(c\ne0\), the complete multiset of local Smith exponents of \(M_{p,c}\) over \(\mathcal O\) is
\[
\boxed{\{0,e\}\ \uplus\ \{h(1),h(2),\ldots,h(N-1)\}.}
\]
For \(p=5\) this same list, \(\{0,1,1,2,2\}\), holds exactly when \(c\in\{1,4\}\). For \(p=5\) and \(c\in\{2,3\}\), the complex matrix has rank exactly four, with the single zero multiplier indexed by the quadratic character. These cases exhaust the nonzero cubic curvatures.

In particular, whenever the matrix is nonsingular, the exact local determinant valuation is
\[
\boxed{v_\pi(\det M_{p,c})=e+\sum_{t=1}^{N-1}h(t)
=\frac{N^2}{6}+O(N).}
\]
The full Smith profile (not only the determinant valuation) is independent of nonzero cubic curvature outside the isolated five-point resonance.

## Assumptions and scope
All vector spaces and curve coordinates are over the *prime* field \(\mathbb F_p\), with \(p\ge5\). Both cubic graphs include their point at the origin and are paired by the standard dot product; the Fourier matrix is unnormalized. Smith exponents refer to the totally ramified \(p\)-adic cyclotomic local ring \(\mathbb Z_p[\zeta]\), not to an integer Smith form. The symbol \(\uplus\) denotes multiset union. The coefficient \(c\) must be nonzero; the zero-curvature boundary is not covered. Singular values in the Euclidean sense are not classified.

## Proof
**1. Multiplicative diagonalization.** Put \(G=\mathbb F_p^\times\), of order \(N\), and let \(K_c(z)=\zeta^{z+cz^3}\). Index the matrix by \(\{0\}\cup G\). On the nonzero block, replace the column label \(t\) by its inverse: then the block becomes \(K_c(s/t)\). Its multiplicative-character Fourier transform is diagonal over \(\mathcal O\), because the character table of \(G\) has determinant a unit (\(N\) is prime to \(p\) and all \(N\)-th roots of unity lie in \(\mathbb Z_p\)). For a Teichmüller character \(\omega\), its multipliers, up to permutation of labels, are
\[
L_r=\sum_{z\in G}\omega(z)^r K_c(z),\qquad 0\le r<N.
\]
Only the trivial-character sector couples to the row and column indexed by zero; that block is equivalent by unit row and column operations to
\[
\begin{pmatrix}1&N\\1&L_0\end{pmatrix}.
\]
Its Smith exponents are \(0\) and \(v_\pi(L_0-N)\). Every other exponent equals \(v_\pi(L_r)\) for \(1\le r<N\).

**2. First nonzero cyclotomic coefficient.** For a representative \([u]\in\{0,\ldots,p-1\}\), the identity \(\zeta^{[u]}=(1+\pi)^{[u]}\) gives
\[
L_r=\sum_{j\ge0}\pi^j
\sum_{z\in G}\omega(z)^r\binom{[z+cz^3]}j.
\]
When \(j<p\), the binomial coefficient modulo \(p\) is a polynomial of degree \(j\) in \(z+cz^3\), with leading coefficient \(1/j!\). Character orthogonality modulo \(p\) gives, for every integer \(i<p\),
\[
\sum_{z\in G}\omega(z)^r(z+cz^3)^i
\equiv -\sum_{\substack{0\le b\le i\\i+2b\equiv-r\ (\mathrm{mod}\ N)}}\binom ib c^b\pmod p.
\]
A coefficient vanishing modulo \(p\) contributes only at \(\pi\)-order at least \(N\), since \(v_\pi(p)=N\). Thus if the first nonzero coefficient modulo \(p\) occurs at index less than \(N\), its index is the *exact* valuation.

**3. Nontrivial characters.** For \(r\ne0\) let \(t=N-r\in\{1,\ldots,N-1\}\). The smallest \(j\) with \(j+2b\equiv t\pmod N\), \(0\le b\le j\), is \(j=h(t)\): indeed \(h(t)\le(t+4)/3\). For \(N\ge6\), no representative \(t+N\) is reachable at this index because \(3h(t)\le t+4<t+N\). Hence exactly one binomial term survives, with \(b=(t-h(t))/2\). Its coefficient is a nonzero multiple of \(\binom{h(t)}b c^b\), because \(h(t)<p\) and \(c\ne0\). Therefore \(v_\pi(L_r)=h(t)\) for every \(p\ge7\).

At \(p=5\), the sole simultaneous least-index representation occurs for \(t=2\), \(j=2\), via exponents \(2\) and \(6\). The first coefficient is proportional to \(1+c^2\). For \(c=1,4\) this is a unit and the same Smith list follows. If \(c=2,3\), consider the quadratic-character multiplier directly:
\[
L_2=\zeta^{1+c}+\zeta^{-(1+c)}-
\zeta^{2+3c}-\zeta^{-(2+3c)}=0,
\]
since \(1+c\equiv\pm(2+3c)\pmod5\). The other two nontrivial character multipliers have valuation one and are nonzero.

**4. Trivial-character block.** The constant term of \(L_0-N\) vanishes identically. A positive moment \(\sum_{z\in G}(z+cz^3)^j\) can be nonzero modulo \(p\) only if one of the exponents \(j,j+2,\ldots,3j\) is divisible by the even integer \(N\). The least such positive \(j\) is the smallest *even* integer at least \(N/3\), namely \(e=2\lceil N/6\rceil\). At index \(e\), the only attainable positive multiple of \(N\) is \(N\), with the unique coefficient \(\binom{e}{(N-e)/2}c^{(N-e)/2}\ne0\pmod p\). As \(e<N\), it follows that \(v_\pi(L_0-N)=e\) in all cases. Thus the trivial two-dimensional sector is always invertible and has exponents \(0,e\).

Combining the two sectors proves the nonsingular cases and the rank-four exception. Finally \(h(t)=t/3+O(1)\), uniformly in \(t\); summing the exact exponents gives the displayed determinant asymptotic.

## Verification
The standalone `verify.py` performs elimination over \(\mathbb F_p[\pi]/(\pi^{p-1})\), using entries \((1+\pi)^{[st+cs^3t^3]}\). This quotient is the reduction of \(\mathcal O\) modulo \(p\). Every claimed *finite* exponent is strictly below \(p-1\), so the truncated computation detects it exactly. The script independently checks the full Smith lists for \(p=5,7,11,13,17,19\), every nonzero curvature for \(p=7,11\), and all four nonzero five-point curvatures. Its censored exponent \(p-1\) in the exceptional cases is not treated as proof of singularity: exact cancellation in Step 3 proves that independently. Run `python3 verify.py` using Python 3 standard library. Expected final line: `CUBIC_GRAPH_LOCAL_SMITH_PASS`.

## Relationship to prior work
Mockenhaupt and Tao (2002) establish the finite-field Fourier restriction framework and study analytic estimates for algebraic surfaces, not local Smith invariants of the paired cubic-graph sampling matrix. Katz, Langevin, Lee, and Sapozhnikov (2016) study \(p\)-adic valuations and minima for additive Weil sums of binomials. Their paper does not state the simultaneous complete multiplicative-character spectrum, the matrix Smith profile, or the exceptional five-point singularity. Related results on spectral bases of cubic graphs over prime-square cyclic rings concern orthogonality of frequency sets over a different coefficient ring and do not imply these local Smith exponents. General multiplicative Fourier diagonalization and cyclotomic expansions are classical ingredients, not claimed as new.

## Limitations
The theorem does not treat extension fields, other monomial degrees, mixed curves with unequal polynomial degrees, the global integer Smith normal form, Euclidean singular values, or optimal numerical conditioning. The proof uses elementary cyclotomic arithmetic, and a stronger general theorem for mixed exponential sums or local invariant factors may imply this classification; exhaustive historical priority certification and independent validation have not been performed. The computational checks are finite corroboration, not an infinite proof.

## References
1. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, initial public arXiv version 18 April 2002, arXiv:math/0204234, later *Duke Mathematical Journal* 121 (2004), 35–74. https://arxiv.org/abs/math/0204234
2. D. J. Katz, P. Langevin, S. Lee, and Y. Sapozhnikov, *The \(p\)-adic valuations of Weil sums of binomials*, initial public arXiv version 14 August 2016, arXiv:1608.04047. https://arxiv.org/abs/1608.04047
