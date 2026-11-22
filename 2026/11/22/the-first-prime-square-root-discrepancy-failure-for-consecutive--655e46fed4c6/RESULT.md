# The first prime square-root discrepancy failure for consecutive Stern residues

## Finding
Let \(s(0)=0\), \(s(1)=1\), \(s(2n)=s(n)\) and \(s(2n+1)=s(n)+s(n+1)\). For a prime \(p\), a nonzero pair \((a,b)\in\mathbb F_p^2\), and an integer \(k\ge0\), define
\[
C_{p,k}(a,b)=\#\{0\le n<2^k:(s(n),s(n+1))\equiv(a,b)\pmod p\},
\qquad D_{p,k}=\max_{(a,b)\ne(0,0)}\left|C_{p,k}(a,b)-\frac{2^k}{p^2-1}\right|.
\]
Then
\[
\boxed{\limsup_{k\to\infty}D_{p,k}^{1/k}\le\sqrt2\quad\text{for }p\in\{2,3,5,7\}.}
\]
In contrast, at the next prime \(11\), even the single primitive pair \((1,2)\) satisfies
\[
\boxed{\limsup_{k\to\infty}\left|C_{11,k}(1,2)-\frac{2^k}{120}\right|^{1/k}\ge\rho>\sqrt2,}
\]
where \(\rho\) is the unique positive root of \(\rho^3-\rho-2=0\), namely \(1.5213797068\ldots\). Therefore \(11\) is the *least prime modulus* at which the maximal discrepancy of consecutive Stern-residue pairs has dyadic root growth strictly larger than the square-root scale. This theorem gives a rigorous lower bound at \(11\), not a claimed exact maximal exponent there.

## Assumptions and scope
The index interval is the complete dyadic prefix \(0\le n<2^k\). The states are the \(p^2-1\) nonzero ordered residue pairs modulo a *prime* \(p\). The theorem is about root-growth limsups, so neither an every-depth lower bound nor a sharp asymptotic constant is asserted. All matrix factors and nonvanishing claims below are exact integer identities. The primary subject is modular distribution of integer sequences (MSC2020 11B85).

## Proof
**1. Exact finite transfer.** For \(v=(a,b)\), let \(U_0(v)=(a,a+b)\) and \(U_1(v)=(a+b,b)\), modulo \(p\). Index a square integer matrix \(T_p\) by the nonzero pairs, and put
\[
(T_p)_{v,w}=\mathbf1_{v=U_0(w)}+\mathbf1_{v=U_1(w)}.
\]
Both maps permute the state set, so \(T_p\) has all row and column sums equal to \(2\). Put \(e=e_{(0,1)}\). Recursing on the binary digits of \(n\) proves that the vector \(T_p^ke\) consists precisely of the counts \(C_{p,k}(a,b)\). Direct enumeration is unnecessary for this identity: \(s(2n)=s(n)\), \(s(2n+1)=s(n)+s(n+1)\), and \(s(2n+2)=s(n+1)\) yield the two transitions. For each of the five primes below, the exact characteristic polynomial has a **simple** factor \(X-2\). Thus the eigenvalue \(2\) contributes the constant vector \(2^k/(p^2-1)\), and all other spectral modes give the discrepancy.

**2. The four smaller primes.** An exact determinant calculation for the explicitly defined integer matrices gives
\[
\begin{aligned}
\det(XI-T_2)={}&(X-2)(X-1)(X+1),\\
\det(XI-T_3)={}&X^2(X-2)(X-1)^3(X^2+X+2),\\
\det(XI-T_5)={}&X^4(X-2)(X-1)^7(X+1)^2(X^2+1)^2\\
&\cdot(X^2-X+2)(X^4-X^2+4),\\
\det(XI-T_7)={}&X^{10}(X-2)(X-1)^{11}(X+1)^4(X^2+2)(X^4+3)^2\\
&\cdot(X^4+X^3+2X+4)\\
&\cdot(X^4-2X^3+3X^2-4X+4)^2.
\end{aligned}
\]
The quadratics \(X^2\pm X+2\) and \(X^2+2\) have roots of modulus \(\sqrt2\). Roots of \(X^4+3\) have modulus \(3^{1/4}<\sqrt2\). For the remaining reciprocal quartics set \(Y=X+2/X\). Dividing by \(X^2\) respectively yields the three equations
\[
Y^2-5=0,\qquad Y^2+Y-4=0,\qquad Y^2-2Y-1=0.
\]
Each root \(Y\) is real and satisfies \(|Y|<2\sqrt2\). Consequently the two solutions of \(X+2/X=Y\) are conjugate of product \(2\), hence have modulus \(\sqrt2\). Therefore every nonprincipal eigenvalue of each of \(T_2,T_3,T_5,T_7\) has modulus at most \(\sqrt2\). Matrix Jordan theory gives \(D_{p,k}=O_p(k^{p^2-2}2^{k/2})\), in particular the first asserted limsup bound.

**3. An active cubic mode at eleven.** Let \(q(X)=X^3-X+2\). Exact characteristic-polynomial calculation yields
\[
\begin{aligned}
\det(XI-T_{11})={}&X^{20}(X-2)(X-1)^{21}(X+1)^{10}\\
&\cdot(X^2-2X+2)(X^2+X+2)(X^2+2X+2)q(X)^2\\
&\cdot(X^8+3X^4+16)^2\\
&\cdot(X^4-3X^3+5X^2-6X+4)^2\\
&\cdot(X^4-X^3+3X^2-2X+4)^2\\
&\cdot(X^{12}+X^{10}-2X^9+X^8-4X^7+4X^5+13X^4+4X^3-X^2-2X+1)^2.
\end{aligned}
\]
Write this polynomial as \((X-2)q(X)^2R(X)\), and define \(P(X)=(X-2)R(X)\). Expanding \(P\) has degree \(114\). Exact integer multiplication, starting from \(e=e_{(0,1)}\), gives the **nonzero scalar certificate**
\[
\boxed{e_{(1,2)}^{\mathsf T}P(T_{11})e_{(0,1)}=573530441763580574433280\ne0.}
\]
The finite calculation is specified completely by the transitions and reproduced by the attached verifier; no approximate spectral computation enters the certificate.

Let \(c_k=C_{11,k}(1,2)\). By Cayley–Hamilton, its minimal annihilating polynomial over \(\mathbb Q\) divides \(\det(XI-T_{11})\). The certificate means \(P\) does not annihilate \((c_k)\), so that minimal polynomial must contain \(q\): otherwise it would divide \(P\). The polynomial \(q\) is irreducible over \(\mathbb Q\), since none of \(\pm1,\pm2\) is a root. Hence all its conjugate characteristic roots occur in the scalar recurrence. One of these is \(-\rho\), with \(\rho^3-\rho-2=0\). Since \(x^3-x-2\) is strictly increasing for \(x\ge1\) and negative at \(x=\sqrt2\), we have \(\rho>\sqrt2\). Removing the simple \(2\)-eigenmode (exactly \(2^k/120\)) does not remove the \(q\)-component. The root-growth identity for rational generating functions therefore gives
\[
\limsup_{k\to\infty}\left|c_k-2^k/120\right|^{1/k}\ge\rho>\sqrt2.
\]
The maximum discrepancy is at least the discrepancy of that pair, completing the least-prime classification.

## Verification
Run `python3 verify_stern_prime_threshold.py` with Python 3 and SymPy. The script constructs all five integer matrices directly from the two residue transitions; verifies every displayed characteristic polynomial exactly; independently compares dyadic residue-pair counts with the Stern recurrence for levels \(0\) through \(12\); checks the reciprocal-quartic radial bounds symbolically; verifies irreducibility of the cubic; and reproduces the nonzero degree-114 scalar certificate as an exact integer. The completed bundled run printed PASS. The finite determinant and polynomial-action checks certify specified finite identities that are used in the analytic all-depth argument. The initial dyadic comparisons alone are not offered as an infinite proof.

## Relationship to prior work
Reznick (2008) proved equidistribution of feasible consecutive Stern residues and supplied the general finite-state framework, including detailed small moduli two and three. Deshouillers and Schinzel (2019) independently developed the general modular automaton and its exact density \(1/(p^2-1)\). Neither inspected work evaluates the four smaller-prime complete spectra and the active modulus-eleven cubic mode together to identify the **least prime threshold** for square-root dyadic discrepancy. A published modulus-nine result gives faster-than-square-root root growth for a *composite* modulus, with a distinct degree-six spectral factor; it therefore does not settle the minimum *prime* modulus. The theorem concerns a natural evaluated threshold rather than claiming a new general automaton construction.

## Limitations
No exact exponent is claimed for the worst eleven-adic pair (only the rigorous lower bound \(\rho\)), and no uniform lower bound is claimed at each depth. Nothing is asserted for nondyadic index intervals, for composite modulus thresholds, or for primes larger than eleven. An older unindexed spectral computation or a stronger, not-yet-identified theorem may affect publication priority. The exact finite matrix certificates are computational and require their independent mathematical validation for external certification.

## References
- B. Reznick, “Regularity Properties of the Stern Enumeration of the Rationals,” *Journal of Integer Sequences* 11 (2008), Article 08.4.1; preprint first submitted October 19, 2006 (arXiv:math/0610601); journal publication 2008. https://arxiv.org/abs/math/0610601 ; https://cs.uwaterloo.ca/journals/JIS/VOL11/Reznick/reznick4.pdf
- V. De Angelis, “The Stern diatomic sequence via generalized Chebyshev polynomials,” arXiv:1511.02422, submitted November 8, 2015. https://arxiv.org/abs/1511.02422
- J.-M. Deshouillers and A. Schinzel, “The modular distribution of Stern's sequence,” *Banach Center Publications* 118 (2019), 37–44; DOI:10.4064/bc118-3. https://www.impan.pl/shop/en/publication/transaction/download/product/113097
