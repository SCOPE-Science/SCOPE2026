# Exact eleven-adic fibers of three-column lonesum matrices

## Finding

Let \(B_n\) be the number of binary lonesum matrices of size \(n\times3\), equivalently the negative-index poly-Bernoulli number \(B_n^{(-3)}\). For every integer \(n\ge0\),
\[
B_n=6\cdot4^n-6\cdot3^n+2^n.
\]
For every integer \(k\ge1\), the least index period of \(B_n\) modulo \(11^k\) is precisely \(P_k=10\cdot11^{k-1}\), and its image is exactly
\[
\{y\bmod11^k:y\bmod11\in\{0,1,2,4,5,8,10\}\}.
\]
Thus there are exactly \(7\cdot11^{k-1}\) image residues, and the closure of the values in \(\mathbb Z_{11}\) is the union of these seven residue balls, of Haar measure \(7/11\).

The fiber law is more refined. Define \(\alpha_0=\alpha_1=\alpha_2=\alpha_4=\alpha_8=1\), \(\alpha_5=\alpha_{10}=2\), and \(\alpha_j=0\) for other residues modulo \(11\). There exist canonical \(A,U\in\mathbb Z_{11}\) with \(A\equiv120\pmod{121}\) and \(U\equiv7\pmod{11}\), defined below. For \(k=1\), the number \(N_1(y)\) of \(0\le n<P_1\) with \(B_n\equiv y\pmod{11}\) is
\[
N_1(y)=\alpha_{y\bmod11}+\mathbf1_{y\equiv10\pmod{11}}.
\]
For \(k\ge2\), put \(m=k-2\) and define \(R_m(z)\) to be the number of square roots of \(z\) modulo \(11^m\), with \(R_0(0)=1\). Then the exact number of indices in one least period representing \(y\bmod11^k\) is
\[
N_k(y)=\alpha_{y\bmod11}+
\begin{cases}
11R_m\!\left(U^{-1}(y-A)/121\right),&y\equiv A\pmod{121},\\
0,&y\not\equiv A\pmod{121}.
\end{cases}
\]
In the first case the argument of \(R_m\) is taken modulo \(11^m\). Explicitly, if \(m\ge1\), then \(R_m(0)=11^{\lfloor m/2\rfloor}\). For nonzero \(z\) modulo \(11^m\) with valuation \(v<m\), \(R_m(z)=2\cdot11^{v/2}\) when \(v\) is even and the leading unit is a square modulo \(11\), and \(R_m(z)=0\) otherwise. This describes every fiber, including arbitrarily large exceptional multiplicities.

## Assumptions and scope

The index \(n\) is a nonnegative integer, \(k\ge1\), and all modular residue classes are taken in \(\mathbb Z/11^k\mathbb Z\). A lonesum matrix is a binary matrix uniquely determined by its row and column sum vectors. No restriction on the number of rows is imposed. For \(a\in\{2,3,4\}\), the map \(t\mapsto(a^{10})^t\) for \(t\in\mathbb Z_{11}\) is its convergent binomial-series extension. Define
\[
G_r(t)=6\cdot4^r(4^{10})^t-6\cdot3^r(3^{10})^t+2^r(2^{10})^t,\qquad 0\le r\le9.
\]
For the exceptional branch, \(H(t)=(G_5(t)-G_5(0))/121\) is restricted analytic over \(\mathbb Z_{11}\). Its derivative has precisely one zero \(\tau\in\mathbb Z_{11}\). Set \(A=G_5(\tau)\) and \(U=H''(\tau)/2\). These definitions fix the normalization of the fiber law and require no choices of square-root branches.

## Proof

**1. Exact enumeration formula.** The defining exponential generating series of the negative-index poly-Bernoulli numbers is \(\operatorname{Li}_{-3}(1-e^{-t})/(1-e^{-t})\). Using
\[
\operatorname{Li}_{-3}(z)=\frac{z(1+4z+z^2)}{(1-z)^4}
\]
gives \(6e^{4t}-6e^{3t}+e^{2t}\). Coefficient extraction proves the displayed formula for every \(n\ge0\); it also agrees with the binary-lonesum enumeration in the cited literature.

**2. Ten branches and nine isometries.** Write \(n=r+10t\). By Fermat's theorem, all three bases to the tenth power are in \(1+11\mathbb Z_{11}\). The series \(G_r\) is therefore restricted analytic. Put \(c_r=G_r(0)\). Its first scaled derivative modulo \(11\) is
\[
d_r\equiv\frac{G_r'(t)}{11}\equiv(10,8,1,8,7,0,10,5,5,1)_r\pmod{11},
\]
independent of \(t\) modulo \(11\), because all higher coefficients are divisible by \(121\). More precisely for \(r\ne5\), \((G_r(t)-c_r)/11=d_rt+11Q_r(t)\) with \(Q_r\) restricted analytic and \(1\)-Lipschitz. Thus for all distinct \(s,t\in\mathbb Z_{11}\),
\[
\nu_{11}(G_r(t)-G_r(s))=1+\nu_{11}(t-s),\qquad r\ne5.
\]
Every such branch maps \(\mathbb Z_{11}\) bijectively onto \(c_r+11\mathbb Z_{11}\), with exactly one preimage modulo \(11^{k-1}\) for each target in its residue class. Their residues \((c_r\bmod11)_{r=0}^9\) are
\[
(1,8,2,10,10,10,4,5,5,0).
\]
Deleting exceptional branch \(r=5\) leaves the multiplicities \(\alpha_j\) in the statement.

**3. Quadratic normal form on the exceptional branch.** Expand in the binomial basis:
\[
G_5(t)=G_5(0)+\sum_{j\ge1}C_j\binom tj,
\qquad C_j=6\cdot4^5(4^{10}-1)^j-6\cdot3^5(3^{10}-1)^j+2^5(2^{10}-1)^j.
\]
Direct exact integer division gives \(C_1/121\equiv6\pmod{11}\) and \(C_2/121\equiv3\pmod{11}\). For \(j\ge3\), \(\nu_{11}(C_j/j!)\ge j-\nu_{11}(j! )\ge3\). Hence the quotient \(H=(G_5-G_5(0))/121\) is a restricted power series and
\[
H(t)\equiv 6t+3\binom t2\equiv7t^2+10t\pmod{11}.
\]
Therefore \(H'(t)\equiv3t+10\pmod{11}\), with unique simple zero \(t\equiv4\pmod{11}\). As \(H'(t)=3t+10+11Q(t)\) with \(Q\) restricted analytic, the contraction/Hensel argument yields exactly one zero \(\tau\in\mathbb Z_{11}\). Factoring at that zero gives
\[
H(t)-H(\tau)=(t-\tau)^2\bigl(U+11W(t)\bigr),\qquad U=H''(\tau)/2\equiv7\pmod{11},
\]
with \(W\) restricted analytic. Because \((U+11W(t))/U\in1+11\mathbb Z_{11}\), its unique square root congruent to \(1\) modulo \(11\) is restricted analytic. Therefore
\[
\Psi(t)=(t-\tau)\sqrt{(U+11W(t))/U}
\]
is a bijective isometry of \(\mathbb Z_{11}\): it equals \(t-\tau\) plus \(11\) times a restricted analytic, hence \(1\)-Lipschitz, correction. We obtain the exact global identity
\[
G_5(t)=A+121U\Psi(t)^2.
\]
Here \(G_5(0)=4718\equiv120\pmod{121}\), and \(G_5(t)-G_5(0)\in121\mathbb Z_{11}\), so \(A\equiv120\pmod{121}\).

**4. Image and fibers.** The exceptional image is \(A+121U\mathbb Z_{11}^2\), entirely inside the ball \(10+11\mathbb Z_{11}\), already covered by branches \(r=3,4\). The other normal branches cover the six remaining balls. Hence the image is exactly the seven listed residue balls. At level \(k\ge2\), the exceptional congruence is equivalent to \(\Psi(t)^2\equiv U^{-1}(y-A)/121\pmod{11^{k-2}}\) if \(y\equiv A\pmod{121}\); otherwise it has no solutions. Since \(\Psi\) is an isometry, each square root modulo \(11^{k-2}\) has eleven lifts among \(t\bmod11^{k-1}\). Adding the nine isometric-branch counts proves the exact fiber formula. Standard odd-prime Hensel lifting proves the explicit root counts. The case \(k=1\) is the displayed ten-entry residue list.

**5. Least period.** The ten-entry pattern modulo \(11\) has least period \(10\), since it has no period equal to a proper divisor \(1,2,5\) of \(10\). Thus every period modulo \(11^k\) is divisible by \(10\). Along branch \(r=0\), the exact scaled distance formula in step 2 forces a period \(10s\) to have \(11^{k-1}\mid s\). Conversely, all branches are \(1\)-Lipschitz with the required powers of \(11\), so \(10\cdot11^{k-1}\) is a period. This proves minimality and completes the theorem.

## Verification

The companion file `check_lonesum_11.py` uses integer modular exponentiation, independent finite-level histogram enumeration, explicit branch derivative checks, and p-adic-log Hensel lifting to compute \(A\) and \(U\) at the precisions needed for the prediction. It checks every output residue and its exact multiplicity for \(k=1,2,3,4,5\); the respective image sizes are \(7,77,847,9317,102487\), with period sizes \(10,110,1210,13310,146410\). For the first four levels it independently excludes all proper divisors of the asserted period. The finite checks support but do not replace the all-depth argument above.

## Relationship to prior work

The poly-Bernoulli enumeration and the lonesum interpretation were established in the literature; specifically, Kim–Krotov–Lee (2011), Section 1 and Section 2, gives both defining equations and the binary-matrix combinatorial interpretation. Bényi–Hajnal (2015) develops combinatorial models for these numbers. OEIS A027650 lists the exact exponential formula and initial values but not a complete prime-power image or fiber law. Ohno–Sakata (2024), Sections 2–3, proves general negative-index poly-Bernoulli periodicity and congruences, but not this output-residue and exceptional-fiber classification at \(11\). The new content is the complete image, the sharp least period, and the exceptional quadratic-fiber normal form for the fixed three-column count.

## Limitations

The classification concerns the single fixed width of three columns and the prime \(11\). It does not claim the same residue pattern for other widths or primes, nor does it give Archimedean distribution estimates. A general theorem on images of exponential polynomials could conceivably contain the present result implicitly; the literature search provides best-knowledge novelty rather than a uniqueness guarantee.

## References

1. H. K. Kim, D. S. Krotov and J. Y. Lee, *Poly-Bernoulli numbers and lonesum matrices*, arXiv:1103.4884v1, submitted March 25, 2011. https://arxiv.org/html/1103.4884v1
2. B. Bényi and P. Hajnal, *Combinatorics of poly-Bernoulli numbers*, arXiv:1510.05765v1, October 20, 2015. https://arxiv.org/abs/1510.05765
3. Y. Ohno and M. Sakata, *On congruence properties of poly-Bernoulli numbers with negative upper-indices*, arXiv:2409.18404, September 27, 2024. https://arxiv.org/abs/2409.18404
4. OEIS Foundation, *A027650: poly-Bernoulli numbers with index negative three*, including the power-sum identity and initial values. https://oeis.org/A027650
