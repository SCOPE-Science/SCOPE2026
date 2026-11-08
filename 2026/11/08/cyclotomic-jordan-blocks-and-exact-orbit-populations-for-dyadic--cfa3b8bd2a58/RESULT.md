# Cyclotomic Jordan blocks and exact orbit populations for dyadic ladder waves

## Finding
For each integer \(r\ge 2\), let \(n=2^r-1\), let \(L_n=P_n\square K_2\) be the labelled open ladder with two rails of \(n\) vertices, and let \(A\) be its loopless adjacency matrix. Fix any finite field \(\mathbb F_q\) of order \(q=2^f\), \(f\ge1\), and evolve two-time-level configurations by
\[
T(u,v)=(Au+v,u),\qquad u,v\in\mathbb F_q^{2n}.
\]
Here every sum is in \(\mathbb F_q\); the vertices and both temporal rows remain labelled. Put \(\Phi(X)=X^2+X+1\). Over the prime field \(\mathbb F_2\), the rational canonical decomposition of \(T\) is exactly
\[
\mathbb F_2[X]/\bigl(\Phi^{n+1}\bigr)\ \oplus\ \mathbb F_2[X]/\bigl(\Phi^{n-1}\bigr).
\]
In particular, its exact permutation order on the entire two-row state space, over every specified \(\mathbb F_q\), is \(3\cdot 2^r\).

For every positive integer \(t\), the number of configurations fixed after \(t\) time steps is
\[
\#\operatorname{Fix}(T^t)=
\begin{cases}
1,&3\nmid t,\\[2mm]
q^{\,2\min(n+1,2^{\nu_2(t)})+2\min(n-1,2^{\nu_2(t)})},&3\mid t.
\end{cases}
\]
The only possible least periods are \(1\) and \(3\cdot2^j\) for \(0\le j\le r\), and every listed period is attained. Define
\[
F_j=q^{\,2\min(n+1,2^j)+2\min(n-1,2^j)}\quad (0\le j\le r),\qquad F_{-1}=1.
\]
There is exactly one fixed state, the zero pair. The number of configurations with primitive period \(3\cdot2^j\) is \(F_j-F_{j-1}\); the number of *distinct temporal orbits* of that period is
\[
\boxed{\frac{F_j-F_{j-1}}{3\cdot2^j}},\qquad 0\le j\le r.
\]
These formulas count no quotient by spatial graph symmetries. Every state is periodic immediately because \(T\) is invertible.

## Assumptions and scope
\(P_n\) is the simple path on \(n\) vertices; \(K_2\) contributes one rung edge at every path position. The graph has \(2n\) vertices. No wraparound edge is added. The characteristic is exactly two, but arbitrary finite extensions \(\mathbb F_{2^f}\) are allowed. The rational-canonical statement is made over \(\mathbb F_2\); fixed-space dimensions remain valid over each extension. The dyadic condition \(n+1=2^r\) is essential to the stated two-block structure; no claim is made for general ladder lengths.

## Proof
**1. Dyadic path nilpotence.** Let \(P\) denote the path adjacency matrix of order \(n\), and let \(p_m(X)=\det(XI-P_m)\) over \(\mathbb F_2\), with \(p_0=1\), \(p_1=X\). The tridiagonal continuant gives \(p_{m+1}=Xp_m+p_{m-1}\). Splitting a path of order \(2m+1\) at its central vertex gives the standard continuant identity \(p_{2m+1}=p_m(p_{m+1}+p_{m-1})=Xp_m^2\). Induction on \(r\) therefore yields
\[
p_{2^r-1}(X)=X^{2^r-1}.
\]
The Krylov list \(e_1,Pe_1,\ldots,P^{n-1}e_1\) is linearly independent: the term \(P^je_1\) has coefficient one at vertex \(j+1\) and zero at every vertex farther from vertex one. Hence the minimum polynomial is \(X^n\), and \(P\) consists of a single nilpotent Jordan block of size \(n\).

**2. The rung shifts the nilpotent structure.** The adjacency of \(K_2\) in characteristic two equals \(I_2+N\), where \(N\ne0\), \(N^2=0\), and \(\operatorname{rank}N=1\). Consequently
\[
A=I_{2n}+K,\qquad K=P\otimes I_2+I_n\otimes N.
\]
Since \(P\) is a single nilpotent block, identify \(K\) with multiplication by \(x+y\) on the \(2n\)-dimensional vector space \(\mathbb F_2[x,y]/(x^n,y^2)\). As \(n=2^r-1\), the Frobenius identity implies \((x+y)^{n+1}=0\), whereas \((x+y)^n=x^{n-1}y\ne0\) (the exponent \(n\) is odd). Thus the largest Jordan block has size exactly \(n+1\). Write a vector as \(a(x)+b(x)y\) modulo \(x^n\). The equation \((x+y)(a+by)=0\) says \(xa=0\) and \(a+xb=0\). Its solutions are \(a=cx^{n-1}\), \(b=cx^{n-2}+dx^{n-1}\), with arbitrary \(c,d\). The kernel of \(K\) therefore has dimension two. There are exactly two nilpotent Jordan blocks, of lengths \(n+1\) and \(2n-(n+1)=n-1\):
\[
K\sim J_{n+1}(0)\oplus J_{n-1}(0).
\]

**3. The two cyclotomic primary blocks.** In block-matrix form, the wave is
\[
T=\begin{pmatrix}A&I_{2n}\\ I_{2n}&0\end{pmatrix}.
\]
The matrix identity \(T^2+\operatorname{diag}(A,A)T+I_{4n}=0\) holds by direct multiplication. Because \(A=I+K\), it follows that
\[
\Phi(T)=T^2+T+I_{4n}=\operatorname{diag}(K,K)T.
\]
The diagonal matrix \(\operatorname{diag}(K,K)\) commutes with \(T\), which is invertible with inverse \((u,v)\mapsto(v,u+Av)\). Therefore for every positive integer \(j\),
\[
\dim_{\mathbb F_2}\ker\Phi(T)^j
=2\dim_{\mathbb F_2}\ker K^j
=2\min(n+1,j)+2\min(n-1,j).
\]
Also \(\Phi(T)^{n+1}=0\). Since \(\Phi\) is irreducible of degree two over \(\mathbb F_2\), these nullities characterize precisely two \(\Phi\)-primary rational cyclic blocks, with exponents \(n+1\) and \(n-1\). This establishes the asserted decomposition without assuming that \(\Phi\) remains irreducible after extending the field.

**4. Fixed spaces and primitive periods.** On the cyclic module \(\mathbb F_2[X]/(\Phi^e)\), the kernel dimension of multiplication by \(X^t-1\) is \(\deg\gcd(X^t-1,\Phi^e)\). The roots of \(\Phi\) are exactly the primitive cube roots of unity. If \(3\nmid t\), this gcd is one. If \(3\mid t\), write \(t=3\cdot2^h m\) with \(m\) odd; the multiplicity of \(\Phi\) in \(X^t-1\) is precisely \(2^h\). The two cyclic blocks therefore contribute dimensions \(2\min(n+1,2^h)\) and \(2\min(n-1,2^h)\). Passing to \(\mathbb F_q\) does not change the rank of the binary matrix, so a fixed space of dimension \(d\) contains exactly \(q^d\) elements. This proves the fixed-count formula.

Since \(n+1=2^r\), the smallest positive \(t\) fixing every state is \(3\cdot2^r\). A nonzero vector can have no period without a factor three; the fixed-space filtration increases strictly at each \(3\cdot2^j\), \(0\le j\le r\), because the longer block has length \(2^r\). The sets fixed by successive powers are nested. Their differences yield all primitive populations, and dividing by the corresponding period yields temporal-orbit counts.

## Verification
Two standalone programs require only Python 3's standard library. Run `python3 artifacts/check_matrix.py` and `python3 artifacts/check_states.py` in the extracted package. Their captured outputs are `artifacts/check_matrix.out` and `artifacts/check_states.out`.

The first program constructs binary adjacency and two-row matrices independently from the graph, compares every positive power through the claimed global order to the fixed-space dimension formula, checks the Jordan-nullity sequence, and confirms the exact order for \(n=3,7,15,31\). The second program evolves configurations by explicit neighbor XOR rather than matrix multiplication: it exhausts all \(2^{12}=4096\) binary two-row states on the three-rung ladder, obtaining primitive-state populations \(1,15,240,3840\) for periods \(1,3,6,12\), and checks deterministic samples on the seven- and fifteen-rung ladders. All tests passed. Finite computation is only corroboration; the proof covers every \(r\ge2\) and every \(q=2^f\).

## Relationship to prior work
Macfarlane (2004) treats reversible second-order linear cellular automata and their matrix representations, focusing on the weights of specific one-dimensional rules. Vlasov (first public 2013, especially Section 3) gives the general reversible second-order construction \((u,v)\mapsto(f(u)+v,u)\) in characteristic two. The present result does not claim those constructions, elementary path continuants, or general finite-field Jordan theory. It determines the *specific two-dimensional open-ladder primary blocks*, sharp dyadic global order, and exact configuration/orbit populations, which do not follow from generic reversibility alone. Adjacent first-order finite rule-90/150 period analyses concern different update maps. A published complete classification of these exact ladder-wave fixed spaces has not been established by the available literature search; this is a qualified priority assessment, not a proof of uniqueness.

## Limitations
Only dyadic open-ladder lengths and characteristic-two fields are classified. Other lengths, other characteristics, stochastic perturbations, and spatial-symmetry orbit quotients are not covered. Some older relevant publisher full text was unavailable during literature inspection, including Macfarlane (2004); undiscovered broader published formulas could imply portions of the result. No independent external mathematical audit has been performed.

## References
1. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A 37 (2004), 10791–10814, DOI:10.1088/0305-4470/37/45/006. Official publication date: 2004-10-28.
2. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297 (first posted 2013-11-18), https://arxiv.org/abs/1311.4297, especially Sections 2–3 and 6.
3. S.-i. Tadaki, *Orbits in one-dimensional finite linear cellular automata*, Physical Review E 49 (1994), 1168–1170, DOI:10.1103/PhysRevE.49.1168. Publisher-public date: 1994-02-01.
