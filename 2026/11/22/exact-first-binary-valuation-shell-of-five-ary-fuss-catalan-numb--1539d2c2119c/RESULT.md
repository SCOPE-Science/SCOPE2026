# Exact first binary valuation shell of five-ary Fuss–Catalan numbers

## Finding
For each integer \(n\ge0\), let
\[
C_5(n)=\frac{1}{4n+1}\binom{5n}{n}
\]
be the five-ary Fuss–Catalan number. For each integer \(L\ge0\), define the *first positive binary valuation shell*
\[
B_1(L)=\#\{0\le n<2^L:\nu_2(C_5(n))=1\}
=\#\{0\le n<2^L:C_5(n)\equiv2\pmod4\}.
\]
Then its exact generating function is
\[
\boxed{\sum_{L\ge0}B_1(L)t^L
=\frac{t^3(1+t)}{(1-t-t^3-t^4)^2}
=\frac{t^3(1+t)}{(1+t^2)^2(1-t-t^2)^2}.}
\]
The initial counts for \(L=0,1,\ldots,11\) are
\[
0,0,0,1,3,5,9,19,37,66,118,214.
\]
Writing \(\varphi=(1+\sqrt5)/2\), the coefficient asymptotic is
\[
\boxed{B_1(L)=\frac{3+\sqrt5}{50}\,L\varphi^L+O(\varphi^L).}
\]
Consequently, relative to the already-known odd shell
\(B_0(L)=\#\{0\le n<2^L:C_5(n)\text{ odd}\}\),
\[
\boxed{\frac{B_1(L)}{B_0(L)}\sim
\frac{3-\sqrt5}{10}\,L.}
\]
The novel assertion is the **valuation-one** enumerator and its consequences, not the previously known parity criterion or parity count. The smallest index with valuation one is \(n=5\).

## Assumptions and scope
All indices \(n,L\) are nonnegative integers. The valuation \(\nu_2\) is normalized by \(\nu_2(2)=1\), and \(\nu_2(1)=0\). Since \(4n+1\) is always odd, the valuation of \(C_5(n)\) equals that of \(\binom{5n}{n}\). Generating functions are identities of formal power series over \(\mathbb Q\), not asymptotic approximations. No claim is made for other primes, other Fuss–Catalan arities, or higher valuation shells.

## Proof
**1. Binary carry model.** By Kummer's theorem, \(\nu_2\binom{5n}{n}\) is exactly the number of binary carry-outs in the addition \(n+4n=5n\). Read the \(L\) bits of \(n\) from least to most significant, padded by zeros afterwards. Before reading bit \(a\), let \(u\) be the bit two positions before it, let \(v\) be the previous bit, and let \(c\) be the incoming carry. The outgoing carry is
\[
d=\left\lfloor\frac{a+u+c}{2}\right\rfloor\in\{0,1\},
\]
and the next state is \((v,a,d)\). Give this transition weight \(z^d\). Order the eight states as
\[
(0,0,0),(0,0,1),(0,1,0),(0,1,1),
(1,0,0),(1,0,1),(1,1,0),(1,1,1).
\]
Let \(M(z)\) be the \(8\times8\) matrix with rows indexing source states and columns indexing target states, obtained by adding the two transitions for \(a=0,1\). After the \(L\) real input bits, the subsequent zero bits deterministically flush all pending carry-outs. Their total weight, for the eight states in the stated order, is
\[
h(z)=(1,1,1,1,1,z,1,z^2)^{\mathsf T}.
\]
The initial row is \(e_0^{\mathsf T}=(1,0,\ldots,0)\). Therefore the entire valuation distribution satisfies the exact identity
\[
\sum_{L\ge0}t^L\sum_{0\le n<2^L}z^{\nu_2(C_5(n))}
=e_0^{\mathsf T}(I-tM(z))^{-1}h(z).
\]
In particular \(M(z)=M_0+zM_1\), and \(h(z)=h_0+zh_1+z^2h_2\), where all coefficients are nonnegative integer matrices or vectors. Thus, with \(R=I-tM_0\), the first two valuation-shell series are
\[
G_0=e_0^{\mathsf T}R^{-1}h_0,\qquad
G_1=e_0^{\mathsf T}R^{-1}(h_1+tM_1R^{-1}h_0).
\]

**2. Exact algebraic reduction.** Put \(D(t)=1-t-t^3-t^4\). In the stated state order, define the following polynomial columns:
\[
U=\begin{pmatrix}
1+t+2t^2+t^3\\1+t^2+t^3\\1+t\\1\\1+t^2+t^3\\0\\1\\0
\end{pmatrix},
\qquad
V=\begin{pmatrix}
t^3+t^4\\t-t^2\\t^2-t^4\\t^2-t^3\\t-t^2\\1-t^2-t^3-2t^4-t^5\\t^2-t^3\\0
\end{pmatrix}.
\]
Direct substitution into the eight binary transition rules gives the two **polynomial identities**
\[
(I-tM_0)U=D h_0,\qquad
(I-tM_0)V=D^2h_1+tDM_1U.
\]
These identities, including every coefficient, are verified with exact integer polynomial arithmetic by the standalone verifier, which constructs both matrices afresh from the bit rule. Because \(R\) has constant term \(I\), it is invertible formally. It follows that \(R^{-1}h_0=U/D\) and \(R^{-1}(h_1+tM_1R^{-1}h_0)=V/D^2\). Taking the first components gives
\[
G_0(t)=\frac{1+t+2t^2+t^3}{D(t)},\qquad
G_1(t)=\frac{t^3+t^4}{D(t)^2},
\]
proving the claimed exact valuation-one generating function **for every** \(L\ge0\). Since the coefficients through \(L=2\) vanish and the coefficient at \(L=3\) equals one, the least valuation-one index belongs to \([0,8)\); directly checking those eight indices gives \(n=5\).

**3. Asymptotics and comparison to the known parity layer.** Factor
\(D(t)=(1+t^2)(1-t-t^2)\). The unique dominant singularity is the positive simple zero \(\rho=\varphi^{-1}\) of \(1-t-t^2\); thus \(G_1\) has a double pole at \(\rho\). Its coefficient of \((1-t/\rho)^{-2}\) is
\[
\frac{\rho(1+\rho)}{(1+\rho^2)^2(1+2\rho)^2}
=\frac{3+\sqrt5}{50}.
\]
All other poles have strictly larger modulus, and the lower-order term at \(\rho\) contributes \(O(\varphi^L)\). This proves the stated asymptotic for \(B_1(L)\). The already established parity count \(B_0(L)=F_{\lceil L/2\rceil+2}F_{\lfloor L/2\rfloor+2}\) satisfies
\[
B_0(L)=\frac{7+3\sqrt5}{10}\varphi^L+O(1).
\]
Dividing the leading coefficients gives the exact relative asymptotic \((3-\sqrt5)L/10\).

## Verification
The self-contained Python 3 program `verify.py` reconstructs all eight state transitions directly from the binary carry formula. It checks all eight coordinates of each polynomial-vector identity in the proof using exact integer polynomial arithmetic, so those checks certify the generating-function simplification at arbitrary formal degree. Independently, for every \(L\le16\), it uses Legendre's digit-sum identity
\[
\nu_2\binom{5n}{n}=s_2(n)+s_2(4n)-s_2(5n)
\]
to compare every index with the generating-function coefficient counts. There are 131,071 index instances across these intervals. Command: `python3 verify.py`; expected ending: `VERIFY_OK`. The finite comparisons corroborate, but are not substitutes for, the all-degree polynomial identities and analytic argument.

## Relationship to prior work
The five-ary Fuss–Catalan coefficients and their binary *parity* structure are known. A published 2026 research dossier (published-finding corpus, November 8, 2026) establishes the exact zero-run spectrum and counts of odd indices, identifying the restriction that two set bits may not occur two positions apart. Its published `RESULT.md` gives the \(B_0(L)\) formula used above, but does **not** determine whether a coefficient has valuation one rather than two or more. No novelty is claimed for its parity criterion or parity enumerator.

Eu, Huang and Kao's September 22, 2026 preprint concerns a different Raney sequence \(R_{3,2}\) and mod-prime zero runs, motivating finer arithmetic statistics of Raney coefficients but not giving this modulo-four classification. Bobrowski, He and Shiue (2019) prove divisibilities on specified generalized-Catalan progressions, not the exact dyadic valuation-one population for \(C_5(n)\). A published exact valuation distribution for \(\binom{5n}{2n}\) (published-finding corpus, October 18, 2026) concerns the different addition \(2n+3n\); even the identity
\[
\binom{5n}{2n}\binom{2n}{n}
=\binom{5n}{n}\binom{4n}{n}
\]
does not yield this claim from that **marginal** distribution without the missing joint carry information. Another published result (published-finding corpus, November 2, 2026) shows that \(\binom{3n}{n}\) has no valuation-one indices at all; the positive and asymptotically \(L\varphi^L\) present shell marks a genuine change of binary carry regime.

## Limitations
This is an exact first-positive-valuation count for one canonical binomial/Raney sequence. The carry method is classical; no general theory of arbitrary slopes is claimed. A source with an unindexed or implicit equivalent formula could supersede novelty; the cited primary sources and mathematical-record searches constrain but cannot prove global priority. No complete count is established for valuation two or higher, and no independent audit has been conducted.

## References
1. S.-P. Eu, Z.-T. Huang, L. Kao, *Zero-Run Spectra of the \((3,2)\) Raney Numbers Modulo Primes*, arXiv:2609.25742v1, first public 2026-09-22. https://arxiv.org/html/2609.25742v1
2. *Exact binary zero-run spectrum of the five-ary Fuss–Catalan numbers*, published November 8, 2026, primary MSC 11B50. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-binary-zero-run-spectrum-of-the-five-ary-fuss-catalan-numb--74e266357ef1
3. J. Bobrowski, T.-X. He, P. J.-S. Shiue, *Divisibility of Generalized Catalan Numbers and Raney Numbers*, J. Comput. Anal. Appl. 26 (2019), 1047–1058. https://scholars.iwu.edu/ws/files/39724414/144%20divisibility%20of%20generalized%202019.pdf
4. *Exact binary valuation fibres on the binomial ray \(\binom{5n}{2n}\)*, published October 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-binary-valuation-fibres-on-the-binomial-ray-binom-5n-2n--0127e93f9dac
5. *Exact dyadic valuation law for \(\binom{3n}{n}\)*, published November 2, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-dyadic-valuation-law-for-binom-3n-n--499526ba814d
6. E. E. Kummer, *Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*, J. Reine Angew. Math. 44 (1852), 93–146.
7. OEIS A002294, the fifth-order Fuss–Catalan sequence. https://oeis.org/A002294
