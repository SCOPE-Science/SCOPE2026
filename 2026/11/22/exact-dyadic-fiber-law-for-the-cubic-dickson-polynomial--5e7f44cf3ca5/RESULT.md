# Exact dyadic fiber law for the cubic Dickson polynomial

## Finding

Let \(f(X)=X^3-3X=D_3(X,1)\), the monic Dickson polynomial of the first kind. For every integer \(k\ge1\) and residue \(0\le y<2^k\), define
\[
N_k(y)=\#\{x\bmod 2^k:f(x)\equiv y\pmod{2^k}\}.
\]
The following formulas determine **every fiber** at every dyadic level. In particular, the image is exactly the even residue classes, so it has \(2^{k-1}\) elements.

For \(1\le k\le6\), odd targets have \(N_k(y)=0\); otherwise \(N_k(y)=1\) except at the listed exceptional targets:

| \(k\) | Exceptional residues \(y\bmod 2^k\) | Their common value \(N_k(y)\) |
|---|---|---|
| 1 | \(0\) | \(2\) |
| 2 | \(2\) | \(3\) |
| 3 | \(2,6\) | \(3\) |
| 4 | \(2,14\) | \(5\) |
| 5 | \(2,14,18,30\) | \(5\) |
| 6 | \(2,18,46,62\) | \(9\) |

For \(m\ge1\), write
\[
S_m(a)=\#\{t\bmod2^m:t^2\equiv a\pmod{2^m}\}.
\]
For every \(k\ge7\), all cases of the complete fiber law are
\[
N_k(y)=\begin{cases}
0,&y\text{ odd},\\
17,&y\equiv18\text{ or }110\pmod{128},\\
1+8S_{k-6}\!\left(3^{-1}\frac{y+2}{64}\right),&y\equiv62\pmod{64},\\
1+8S_{k-6}\!\left(5^{-1}\frac{y-2}{64}\right),&y\equiv2\pmod{64},\\
1,&\text{otherwise}.
\end{cases}
\]
Here the indicated quotients are integers and the inverses and arguments of \(S_{k-6}\) are taken modulo \(2^{k-6}\). The five alternatives are disjoint. The square-root count \(S_m(a)\) is made explicit in the proof below, so this is a closed arithmetical classification rather than a recursive enumeration.

Let \(M_k=\max_y N_k(y)\), and let \(E_k=\#\{y\bmod2^k:N_k(y)=M_k\}\). The sharp extremal law is
\[
M_1=2,\quad M_2=M_3=3,\quad M_4=M_5=5,
\qquad M_k=1+2^{\lceil k/2\rceil}\ (k\ge6),
\]
and the exact number of maximizers is
\[
E_1=E_2=1,\quad E_3=E_4=2,\quad E_5=E_6=4,
\qquad E_k=\begin{cases}2,&k\ge7\text{ odd},\\8,&k\ge8\text{ even}.\end{cases}
\]

## Assumptions and scope

All congruences are in the ordinary residue ring \(\mathbb Z/2^k\mathbb Z\). Fibers count distinct input residue classes, not algebraic multiplicities. The parameter of the first-kind Dickson polynomial is fixed at \(1\), and the degree is exactly \(3\). The statements hold for **every** positive integer exponent \(k\), without an upper cutoff. The polynomial is \(D_3(X,1)=2T_3(X/2)\) over rational polynomials; division by \(2\) is not a permitted change of variables in dyadic residue rings. We use \(\mathbb Z_2\) only as a convenient inverse-limit description of compatible congruences.

## Proof

**1. The even branch is bijective.** Every value of \(f\) is even: for even inputs this is immediate, and for odd \(x\) the factor \(x^2-3\) is even. If \(x=2t\), then
\[
f(2t)=2h(t),\qquad h(t)=4t^3-3t.
\]
For any integers \(t,u\),
\[
h(t)-h(u)=(t-u)\bigl(4(t^2+tu+u^2)-3\bigr),
\]
and the second factor is odd. Consequently \(h\) preserves every \(2\)-adic difference valuation, hence permutes each \(\mathbb Z/2^m\mathbb Z\). There is exactly one even preimage modulo \(2^k\) for every even target, and none for an odd target.

**2. A precise square-coordinate lemma.** For any odd integer \(b\) and \(t\in\mathbb Z_2\), the unit \(1+8t/b\) has a unique square root \(u_b(t)\) satisfying \(u_b(t)\equiv1\pmod4\). Indeed the square map from \(1+4\mathbb Z_2\) onto \(1+8\mathbb Z_2\) is a bijection, as follows by lifting successive binary digits. For \(s,t\in\mathbb Z_2\),
\[
\nu_2\bigl(u_b(t)-u_b(s)\bigr)
=\nu_2\!\left(\frac{8(t-s)}{b}\right)-\nu_2\bigl(u_b(t)+u_b(s)\bigr)
=\nu_2(t-s)+2,
\]
when \(s\ne t\), since both roots are \(1\pmod4\), so their sum has valuation \(1\). Thus the maps \(t\mapsto t u_b(t)\) and \(t\mapsto(1+t)u_b(t)\) preserve \(2\)-adic distance and biject \(\mathbb Z_2\) onto itself. The map \(t\mapsto(1+2t)u_b(t)\) multiplies all difference distances by \(1/2\), and bijects \(\mathbb Z_2\) onto \(1+2\mathbb Z_2\): the linear term in its difference has valuation \(\nu_2(t-s)+1\), strictly below the correction term. In each case bijectivity follows because the induced map modulo each \(2^m\) is distance-preserving (after the specified normalization), and the finite domain and codomain have the same size.

**3. Four exact odd branches.** The polynomial identities
\[
f(X)+2=(X-1)^2(X+2),\qquad
f(X)-2=(X+1)^2(X-2)
\]
give, for \(t\in\mathbb Z_2\), the following normal forms:
\[
\begin{aligned}
f(1+8t)&=-2+64\cdot3\,[t u_3(t)]^2,\\
f(7+8t)&= 2+64\cdot5\,[(1+t)u_5(t)]^2,\\
f(5+8t)&=-2+16\cdot7\,[(1+2t)u_7(t)]^2,\\
f(3+8t)&= 2+16\,[(1+2t)u_1(t)]^2.
\end{aligned}
\]
These four input classes are disjoint and exhaust all odd inputs. By Step 2, the bracketed coordinates in the first two branches range bijectively over all of \(\mathbb Z_2\), while those in the last two range bijectively over all odd elements \(1+2\mathbb Z_2\).

For \(k\ge7\), the first two branches can contribute only to target residue classes \(-2\) and \(2\) modulo \(64\), respectively; within those classes the square-root condition determines which targets actually receive an odd preimage. An input \(t\bmod2^{k-3}\) induces a square equation modulo \(2^{k-6}\), with exactly \(8\) input lifts per solution. Thus their contributions are the two \(8S_{k-6}\) terms in the displayed law.

For the last two branches, every odd square is \(1\pmod8\), and every class \(1\pmod8\) has exactly four odd square roots modulo \(2^{k-4}\), because \(k-4\ge3\). Their output classes are respectively \(110\) and \(18\) modulo \(128\); each square root has four input lifts from the coordinate modulo \(2^{k-4}\) to \(t\bmod2^{k-3}\). Hence each last branch gives exactly \(16\) odd preimages at each target of its support. Adding the unique even preimage proves the law for \(k\ge7\). At the levels \(k\le6\), reducing the same exact normal forms modulo \(2^k\), along with direct inspection at \(k=1,2\), yields the six displayed finite rows.

**4. Closed count of square roots and sharp maximum.** To evaluate \(S_m(a)\), take the representative \(0\le a<2^m\). If \(a=0\), then \(S_m(0)=2^{\lfloor m/2\rfloor}\). If \(0<a<2^m\) has odd \(\nu_2(a)\), then \(S_m(a)=0\). Otherwise write \(a=2^{2s}u\) with \(u\) odd and \(2s<m\), and put \(d=m-2s\). Then
\[
S_m(a)=2^s\begin{cases}
1,&d=1,\\
2,&d=2,\ u\equiv1\pmod4,\\
4,&d\ge3,\ u\equiv1\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]
The formula follows by extracting the even valuation \(2s\) from a square, then applying the classical odd-square root count modulo powers of two. In particular, for odd \(m\ge3\), the maximum of \(S_m\) is \(2^{\lceil m/2\rceil}\) and occurs only at \(a=2^{m-3}\). For even \(m\ge4\), the same maximum occurs at exactly the four residues \(0,2^{m-2},2^{m-4},9\cdot2^{m-4}\). At \(m=1\) the maximum is \(1\) at both residues; at \(m=2\) it is \(2\) at \(0\) and \(1\).

For \(k\ge9\), the two square-branch maxima are strictly greater than the constant \(17\) in the other exceptional branches, and the preceding square classification yields \(M_k=1+2^{\lceil k/2\rceil}\) and exactly two maximizing targets for odd \(k\), eight for even \(k\). At \(k=8\), each of the two square branches has two maximizing targets and each of the two constant branches has two maximizing targets, for eight in all; at \(k=7\), precisely the two constant-branch targets maximize. The finite table handles \(k\le6\). This proves all assertions.

## Verification

The accompanying standalone `verify.py` implements the independent root-count formula and exhaustively compares the theorem with direct evaluation of \(f(x)\bmod2^k\) for every \(1\le k\le16\). It checks **all 131,070 target fibers** across those levels, using the same number of direct polynomial evaluations, including all small-exponent exceptions. It separately exhaustively tests the closed square-root formula for all residues modulo \(2^m\) at every \(1\le m\le12\). The script checks sharp maxima, number of maximizing targets, and exact image sizes. Run `python3 verify.py`. These checks corroborate the proof but are not substituted for the arguments establishing every exponent.

## Relationship to prior work

Brazelton–Harrington–Litman–Wong (first public preprint 2021-03-16) determine Dickson-polynomial image sizes and residue sums over **finite fields of odd characteristic**, not the residue-by-residue fibers over dyadic prime-power rings here. Bremser–Gómez-Calderón (1991) discuss value sets and selected fibers over Galois rings, but restrict their main result and fiber count to odd residue characteristic and acknowledge exceptional cases outside their method. Yoshioka–Dainobu (2015) and Iwasaki–Umeno (2016) treat the **ordinary Chebyshev polynomial** \(T_3(X)=4X^3-3X\), a permutation modulo \(2^k\), and its orbital/degree periods. That polynomial controls only the even-input branch of the monic Dickson polynomial \(D_3(X,1)\); their bijection results do not determine the four singular odd-input fibers. Shang (2023) gives extremal upper bounds for general non-permutation polynomial value sets over residue rings, not complete fibers of this cubic. Related public findings concerning the cubic Dickson map modulo \(3^k\) or even-degree Dickson maps modulo \(2^k\) concern distinct maps or prime supports and do not imply the target-by-target formula.

## Limitations

This is a fixed-parameter, fixed-degree classification; it makes no claim for \(D_n(X,a)\) at other degrees, parameters, or odd-prime moduli. The finite checker stops at exponent \(16\), whereas the proof is uniform for all \(k\ge1\). The novelty comparison has not established mathematical uniqueness against every unindexed or inaccessible historic source. In particular, not all earlier research archives were available for duplicate checking, though an accessible current archive and pertinent primary texts were compared. Independent external review remains unperformed.

## References

1. T. Brazelton, J. Harrington, M. Litman, T. W. H. Wong, *Residue sums of Dickson polynomials over finite fields*, arXiv:2103.09119 (first public version 2021-03-16), https://arxiv.org/abs/2103.09119.
2. P. S. Bremser and J. Gómez-Calderón, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory **38** (1991), 240–250, https://doi.org/10.1016/0022-314X(91)90087-R.
3. D. Yoshioka and Y. Dainobu, *On some properties of Chebyshev polynomial sequences modulo \(2^k\)*, Nonlinear Theory and Its Applications, IEICE **6** (2015), 443–452, https://doi.org/10.1587/nolta.6.443.
4. A. Iwasaki and K. Umeno, *Three Theorems on odd degree Chebyshev polynomials and more generalized permutation polynomials over a ring of module \(2^w\)*, arXiv:1602.08238 (2016), https://arxiv.org/abs/1602.08238.
5. S. Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226 (2023), https://arxiv.org/abs/2310.20226.
