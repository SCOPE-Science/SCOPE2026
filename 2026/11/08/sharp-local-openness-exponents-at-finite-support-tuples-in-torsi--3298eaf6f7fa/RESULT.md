# Sharp local openness exponents at finite-support tuples in torsion group algebras

## Finding

**Theorem.** Let \(G\) be any discrete abelian torsion group (possibly infinite), \(k\ge2\), and let \(a_1,\ldots,a_k\) be finitely supported elements of the complex convolution Banach algebra \(A=\ell^1(G)\). Put \(H=\langle\bigcup_j\operatorname{supp}a_j\rangle\), a finite subgroup, and for each character \(\chi:H\to\mathbb T\) put
\[
\alpha_{\chi,j}=\sum_{h\in H}a_j(h)\chi(h),\quad
z_\chi=\#\{j:\alpha_{\chi,j}=0\},\quad
s=\max\{1,\max_{\chi\in\widehat H}z_\chi\}.
\]
For \(0<\varepsilon<1\), define the local image radius
\[
R(\varepsilon)=\sup\left\{r\ge0:B_A(a_1*\cdots*a_k,r)
 \subseteq\{b_1*\cdots*b_k:\|b_j-a_j\|_1<\varepsilon\ \forall j\}\right\}.
\]
There are constants \(0<c\le C<\infty\), depending only on the tuple, such that
\[
\boxed{c\varepsilon^s\le R(\varepsilon)\le C\varepsilon^s
\qquad(0<\varepsilon<1).}
\]
In particular every finite-support tuple is a point of local openness of the full \(k\)-fold convolution map \(A^k\to A\), **even for target perturbations with infinite support**. For \(k=2\) the exponent is \(2\) exactly when the two inputs share a vanishing Fourier coordinate, and is \(1\) otherwise. Every exponent \(s\in\{1,\ldots,k\}\) occurs for suitable tuples. The exponent is independent of the choice of any finite subgroup containing all supports.

## Assumptions and scope

The group is abelian and every element has finite order. Only the base factors are required to have finite support; the perturbations and their factors range over all of \(\ell^1(G)\). Convolution is \((f*g)(x)=\sum_{y\in G}f(y)g(x-y)\); its identity is \(\delta_0\). All scalars are complex. \(B_A(x,r)\) denotes a norm-open ball. The exponent \(s\) describes the largest polynomial order of vanishing of the coordinatewise product at the base tuple, not the number of zeros of the product alone.

## Proof

**1. Finite Fourier idempotents.** Since \(G\) is abelian torsion, the finitely generated subgroup \(H\) is finite. For each \(\chi\in\widehat H\), set
\[
 e_\chi=\frac1{|H|}\sum_{h\in H}\overline{\chi(h)}\delta_h.
\]
The finite-character orthogonality relations give
\[
 e_\chi*e_\psi=\mathbf1_{\chi=\psi}e_\chi,\quad
\sum_\chi e_\chi=\delta_0,\quad
\|e_\chi\|_1=1,
 \qquad a_j*e_\chi=\alpha_{\chi,j}e_\chi.
\]
These identities remain valid in the full group algebra. Thus every \(w\in A\), including infinite-support \(w\), decomposes into \(w=\sum_\chi w_\chi\) where \(w_\chi=e_\chi*w\), and different components multiply to zero.

**2. Constructive lower image bound.** Write \(N=|H|\) and \(P=a_1*\cdots*a_k\). For each \(\chi\), define a strictly positive scalar
\[
 L_\chi=\begin{cases}
 \prod_{j=2}^k|\alpha_{\chi,j}|,&z_\chi=0,\\
 \prod_{j:\alpha_{\chi,j}\ne0}|\alpha_{\chi,j}|,&z_\chi\ge1,
 \end{cases}
\]
where an empty product equals \(1\). Set \(L=\min_\chi L_\chi>0\), \(t=\varepsilon/(2N)\), and \(\delta=(L/2)t^s\). Fix an arbitrary \(w\in A\) with \(\|w-P\|_1<\delta\). Write \(w_\chi=e_\chi*w\); then \(\|w_\chi-P*e_\chi\|_1<\delta\).

For each \(\chi\), construct factors \(b_{j,\chi}\in e_\chi*A\) whose component product is \(w_\chi\). If \(z_\chi=0\), retain \(b_{j,\chi}=\alpha_{\chi,j}e_\chi\) for \(j\ge2\) and take
\[
 b_{1,\chi}=\alpha_{\chi,1}e_\chi+
 \frac{w_\chi-P*e_\chi}{\prod_{j=2}^k\alpha_{\chi,j}}.
\]
Its deviation is less than \(\delta/L_\chi\le t/2\), because \(s\ge1\) and \(t<1\).

If \(z_\chi=z\ge1\), retain the nonzero components \(\alpha_{\chi,j}e_\chi\); among the \(z\) zero coordinates set the first \(z-1\) to \(t e_\chi\), and set the remaining one to
\[
 \frac{w_\chi}{t^{z-1}\prod_{j:\alpha_{\chi,j}\ne0}\alpha_{\chi,j}}.
\]
Since \(P*e_\chi=0\), the last component has norm less than \(\delta/(L_\chi t^{z-1})\le t/2\), while the other modified components have norm \(t\). In either case the component product is exactly \(w_\chi\). Summing \(b_j=\sum_\chi b_{j,\chi}\) across characters annihilates mixed products and gives \(b_1*\cdots*b_k=w\); moreover
\[
 \|b_j-a_j\|_1\le\sum_\chi\|b_{j,\chi}-\alpha_{\chi,j}e_\chi\|_1\le Nt=\varepsilon/2<\varepsilon.
\]
Hence \(R(\varepsilon)\ge (L/2)(\varepsilon/(2N))^s\).

**3. Sharp upper bound.** Every character \(\chi\) of \(H\) extends to a character \(\widetilde\chi\) of \(G\). One proof is to extend maximally by Zorn's lemma: upon adjoining \(g\), choose an \(n\)-th root of the prescribed value at \(ng\) if some least \(n>0\) has \(ng\) in the current subgroup, or any circle value otherwise; divisibility of \(\mathbb T\) makes the extension possible. The resulting functional
\[
 \Phi_\chi(f)=\sum_{g\in G}f(g)\widetilde\chi(g)
\]
 is multiplicative, has norm \(1\), and satisfies \(\Phi_\chi(e_\chi)=1\), \(\Phi_\chi(a_j)=\alpha_{\chi,j}\).

If \(s\ge2\), choose \(\chi\) with \(z_\chi=s\). For \(\|b_j-a_j\|_1<\varepsilon<1\), multiplicativity gives
\[
 |\Phi_\chi(b_1*\cdots*b_k)|<D\varepsilon^s,
 \qquad D=\prod_{j:\alpha_{\chi,j}\ne0}(|\alpha_{\chi,j}|+1),
\]
while \(\Phi_\chi(P)=0\). Consequently \(P+2D\varepsilon^s e_\chi\), at exact distance \(2D\varepsilon^s\) from \(P\), is not such a product, and \(R(\varepsilon)\le 2D\varepsilon^s\).

If \(s=1\), choose any \(\chi\). A telescoping product difference yields
\[
 |\Phi_\chi(b_1*\cdots*b_k)-\Phi_\chi(P)|< D'\varepsilon,
 \quad D'=\sum_{j=1}^k\prod_{\ell\ne j}(|\alpha_{\chi,\ell}|+1).
\]
The target \(P+2D'\varepsilon e_\chi\) is therefore unattainable in the specified factor balls, proving \(R(\varepsilon)\le2D'\varepsilon\). The two-sided rate is proved.

**4. Extremal orders and subgroup independence.** For any \(1\le m\le k\), take \(m\) inputs equal to \(0\) and the others equal to \(\delta_0\). Every character has exactly \(m\) vanishing factors, so \(s=m\); for \(m=1\) this realizes exponent \(1\). If \(K\supseteq H\) is finite, every character of \(H\) extends to \(K\); the Fourier values of each input at a character of \(K\) depend only on its restriction to \(H\). Hence the maximal zero multiplicity is unchanged.

## Verification

The companion exact-rational checker `checks/check_finite_moduli.py` constructs the primitive Fourier idempotents of \(H=(\mathbb Z/2\mathbb Z)^2\) inside \(G=(\mathbb Z/2\mathbb Z)^3\), and verifies their orthogonality, exact reconstruction and component-by-component factorization for multiple \(k\) and zero-multiplicities. Its targets include a perturbation supported outside \(H\), so the test does not merely factor inside the small subgroup algebra. Run `python3 checks/check_finite_moduli.py` from a directory containing the embedded checker; expected output is `EXACT_FINITE_CONVOLUTION_MODULI_OK 201`. The infinitely many characters/cases and general conclusion are established by the proof, not by enumeration.

## Relationship to prior work

Flores (2026, arXiv:2610.38722v1) proves non-openness for nonabelian groups or groups with an infinite-order element, explicitly leaving infinite abelian torsion groups as possible open cases. The present local theorem does **not** prove global openness for those groups; it proves that any obstruction in the unresolved case must involve at least one infinite-support base factor. Draga–Kania (2017, arXiv:1704.08608v2) show density of invertibles when idempotents span densely (Corollary 2.6), but stable rank one is weaker than open multiplication and their finite/idempotent discussion does not give the full-algebra sharp local exponents. Kania–Maślany (2024, arXiv:2301.02320) prove openness for jointly non-degenerate pairs under further assumptions and establish non-uniform openness for abelian groups of unbounded exponent; their theorems do not imply local openness at simultaneously vanishing factors or the exact \(k\)-fold modulus. The Fourier coordinate construction is elementary; any unrecognized older quantitative finite-idempotent factorization lemma is a residual priority risk.

## Limitations

The result does not settle whether convolution on any infinite abelian torsion group is open at **all** input pairs. The finite-support restriction is essential to this proof. Constants depend on the factors and their finite subgroup; no tuple-uniform or group-uniform openness is claimed. The exponent concerns a fixed tuple and arbitrarily supported targets. Other infinite-support tuples, nonabelian groups, and non-torsion abelian groups are outside the theorem. Publication priority and independent mathematical validation have not been established.

## References

1. F. I. Flores, *The convolution product is generally not an open map*, arXiv:2610.38722v1, first posted 2026-10-28. https://arxiv.org/html/2610.38722v1
2. S. Draga and T. Kania, *When is multiplication in a Banach algebra open?*, arXiv:1704.08608v2 (2017), especially Corollary 2.6 and §5. https://arxiv.org/pdf/1704.08608
3. T. Kania and N. Maślany, *Differential embeddings into algebras of topological stable rank 1*, arXiv:2301.02320; Proc. R. Soc. Edinburgh Sect. A, published online 2024-11-20. https://doi.org/10.1017/prm.2024.108
