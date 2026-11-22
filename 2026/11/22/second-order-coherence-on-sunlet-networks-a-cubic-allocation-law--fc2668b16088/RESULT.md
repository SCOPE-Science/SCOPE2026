# Second-order coherence on sunlet networks: a cubic allocation law and a strict first-order mismatch

## Finding

For every integer \(n\ge3\), let the *sunlet* \(S_n=C_n\circ K_1\) consist of a cycle with one distinct pendant leaf attached to each cycle vertex. Allocate a total unit conductance budget among the \(2n\) edges; all conductances are independently adjustable and nonnegative, and their positive-weight support must remain connected. If \(L\) denotes the ordinary, unnormalized, symmetric weighted Laplacian, define the two spectral design criteria
\[
 F_1(L)=\operatorname{tr}(L^+),\qquad F_2(L)=\operatorname{tr}((L^+)^2),
\]
where \(L^+\) is the Moore--Penrose pseudoinverse. These are, up to fixed positive normalization factors, first- and second-order noisy-consensus coherence measures.

**Theorem.** The unique global minimizer of \(F_2\), even over fully nonuniform edge allocations, assigns a common conductance \(a_{2,n}>0\) to every cycle edge and \(b_{2,n}>0\) to every pendant edge. Set
\[
 A_n=n-\frac34,\quad B_n=\frac{n^2-1}{6},\quad C_n=\frac{n^4+10n^2-11}{180}.
\]
There is exactly one positive root \(t_{2,n}\) of
\[
 2A_nt^3+B_nt^2-B_nt-2C_n=0.
\]
The exact optimum is
\[
 \boxed{a_{2,n}=\frac{t_{2,n}}{n(1+t_{2,n})},\quad b_{2,n}=\frac{1}{n(1+t_{2,n})}},
 \qquad
 \boxed{F_2^*=n^2(1+t_{2,n})^2\left(A_n+\frac{B_n}{t_{2,n}}+\frac{C_n}{t_{2,n}^2}\right)}.
\]
The first-order optimum is also unique globally and has the same edge-orbit symmetry, with ratio
\[
 t_{1,n}:=\frac{a_{1,n}}{b_{1,n}}=\sqrt{\frac{n^2-1}{6(n-1/2)}}.
\]
For **every** integer \(n\ge3\), the two objectives have different optimizers, with the strict ordering
\[
 \boxed{t_{2,n}>t_{1,n}},\qquad \boxed{b_{2,n}<b_{1,n}}.
\]
Writing \(c\) for the unique positive root of \(180c^3+15c^2-1=0\), numerically \(c=0.153242321348\ldots\), the sharp large-cycle laws are
\[
 \boxed{\frac{t_{2,n}}n\longrightarrow c,\quad n^2b_{2,n}\longrightarrow c^{-1}},\qquad
 \boxed{\frac{t_{1,n}}{\sqrt n}\longrightarrow\frac1{\sqrt6},\quad n^{3/2}b_{1,n}\longrightarrow\sqrt6}.
\]
The difference between selecting conductances for first-order coherence and then evaluating second-order coherence is asymptotically
\[
 \boxed{F_2(L_{1,n}^*)-F_2(L_{2,n}^*)\sim\frac{\sqrt6}{90}\,n^{11/2}},
\]
while \(F_2(L_{2,n}^*)\sim n^6/180\). Thus the absolute cross-objective regret diverges, although its ratio to the optimum tends to zero.

## Assumptions and scope

The cycle vertices are \(u_i\) and leaves are \(v_i\), with \(i\in\mathbb Z/n\mathbb Z\). Edges are \(\{u_i,u_{i+1}\}\) and \(\{u_i,v_i\}\). Every edge has unit cost per unit conductance; the budget is \(\sum_e w_e=1\). The positive-weight subgraph must be connected, so the zero eigenvalue of \(L\) is simple. A disconnected boundary allocation is assigned infinite objective in this design problem, rather than taking the finite pseudoinverse-square trace of a disconnected matrix with multiple zeros. Normalization of the stochastic disturbance and common control gain only multiplies either objective by a positive constant and does not change its optimizer. The claim concerns the ordinary weighted Laplacian, not the normalized Laplacian, a discrete-time stochastic matrix, or the fastest spectral-gap criterion.

## Proof

**1. Unrestricted uniqueness and symmetry.** Restrict \(L\) to the mean-zero space \(\mathbf1^\perp\), obtaining \(X\succ0\). The scalar function \(f(x)=x^{-2}\) is strictly convex for \(x>0\). The Hessian of the associated spectral trace \(\operatorname{tr}f(X)\), in any orthonormal eigenbasis with eigenvalues \(\lambda_i>0\), is
\[
 D^2\operatorname{tr}f(X)[H,H]
 =\sum_{i,j}\frac{f'(\lambda_i)-f'(\lambda_j)}{\lambda_i-\lambda_j}|H_{ij}|^2,
\]
with diagonal quotients interpreted as \(f''(\lambda_i)=6\lambda_i^{-4}\). All coefficients are strictly positive because \(f'(x)=-2x^{-3}\) is strictly increasing. Hence \(\operatorname{tr}(X^{-2})\) is strictly convex in \(X\). Distinct edge-weight vectors give distinct Laplacians (the off-diagonal entries encode every edge weight), so \(F_2\) is strictly convex in the independent edge weights on the connected feasible domain. If positive-weight support approaches disconnection, a positive eigenvalue approaches zero, and \(F_2\) diverges; a minimizer therefore exists. The dihedral automorphisms of the sunlet act transitively on cycle edges and separately on pendant edges. Averaging any optimal allocation under these automorphisms cannot increase \(F_2\), and strict convexity forces the unique optimum to have the two common edge weights \(a,b\). Both must be positive to preserve connectivity.

Exactly the same reasoning applies to \(F_1\), using the strictly convex scalar function \(x^{-1}\).

**2. Exact spectral decomposition.** In the core/leaf order,
\[
 L(a,b)=\begin{pmatrix}aL(C_n)+bI&-bI\\-bI&bI\end{pmatrix}.
\]
The Fourier eigenvalues of \(L(C_n)\) are \(\lambda_k=4\sin^2(\pi k/n)\), for \(0\le k\le n-1\). Each mode reduces \(L\) to
\[
 M_k=\begin{pmatrix}a\lambda_k+b&-b\\-b&b\end{pmatrix},
\]
whose trace is \(a\lambda_k+2b\) and determinant is \(ab\lambda_k\). For \(k=0\), the eigenvalues are \(0\) and \(2b\). For every \(k>0\), both are positive. Taking their reciprocal sums and squared-reciprocal sums gives
\[
 \begin{aligned}
 F_1(a,b)&=\frac{n-1/2}{b}+\frac2a\sum_{k=1}^{n-1}\lambda_k^{-1},\\
 F_2(a,b)&=\frac{n-3/4}{b^2}+\frac2{ab}\sum_{k=1}^{n-1}\lambda_k^{-1}+\frac4{a^2}\sum_{k=1}^{n-1}\lambda_k^{-2}.
 \end{aligned}
\]

The cycle identities are
\[
 \sum_{k=1}^{n-1}\lambda_k^{-1}=\frac{n^2-1}{12},\qquad
 \sum_{k=1}^{n-1}\lambda_k^{-2}=\frac{n^4+10n^2-11}{720}.
\]
For completeness, they follow by expanding at \(x=0\) the identity
\[
 \sum_{k=0}^{n-1}\csc^2(x+k\pi/n)=n^2\csc^2(nx).
\]
The constant terms give \(\sum_{k=1}^{n-1}\csc^2(k\pi/n)=(n^2-1)/3\). The quadratic terms, together with \((\csc^2 x)''=6\csc^4x-4\csc^2x\), give \(\sum_{k=1}^{n-1}\csc^4(k\pi/n)=(n^4+10n^2-11)/45\). Division by \(4\) and \(16\) yields the displayed identities.

**3. Exact allocation.** Since there are \(n\) edges in each class, \(n(a+b)=1\). Set \(t=a/b>0\), so \(a=t/[n(1+t)]\), \(b=1/[n(1+t)]\). Substitution yields
\[
 F_2(t)=n^2(1+t)^2\left(A_n+\frac{B_n}t+\frac{C_n}{t^2}\right).
\]
The derivative has the sign of \(P_n(t)=2A_nt^3+B_nt^2-B_nt-2C_n\), since
\[
 F_2'(t)=\frac{n^2(1+t)}{t^3}\,P_n(t).
\]
The polynomial has exactly one positive zero by Descartes' rule of signs (its coefficient signs have exactly one change), and it is negative at zero and positive at infinity. Therefore this zero is the unique global optimum. Also \(F_1(a,b)=(n-1/2)/b+B_n/a\), whose derivative gives the stated \(t_{1,n}\).

**4. Strict priority for cycle edges in the second-order design.** Put \(E_n=n-1/2\), \(Q_n=2C_nE_n-B_n^2\). At \(t_{1,n}=\sqrt{B_n/E_n}\), direct substitution yields
\[
 E_nP_n(t_{1,n})=B_n(n-1)\sqrt{B_n/E_n}-Q_n.
\]
Moreover,
\[
 Q_n=\frac{(n^2-1)(n^3-3n^2+11n-3)}{90}>0
\]
for \(n\ge3\), and
\[
 E_nQ_n^2-B_n^3(n-1)^2=\frac{(n^2-1)^2}{16200}\,T(n),
\]
where, writing \(h=n-3\ge0\),
\[
 T(n)=2h^7+29h^6+212h^5+905h^4+2270h^3+3500h^2+3600h+2100>0.
\]
Thus \(Q_n>B_n(n-1)\sqrt{B_n/E_n}\) and \(P_n(t_{1,n})<0\). Because \(P_n\) has one positive root, \(t_{2,n}>t_{1,n}\), proving both strict optimizer mismatch and \(b_{2,n}<b_{1,n}\).

**5. Asymptotic laws and regret.** From the optimizing cubic, the positive root satisfies \(t_{2,n}=\Theta(n)\): substitution \(t=\eta n\) gives, after division by \(n^4\), a limiting polynomial \(2\eta^3+\eta^2/6-1/90\), strictly increasing on \((0,\infty)\) and having the unique zero \(c\). A bracketing argument at any two fixed positive \(\eta\) on opposite sides of \(c\) proves \(t_{2,n}/n\to c\). The explicit first-order formula gives \(t_{1,n}\sim\sqrt{n/6}\), which implies the two pendant-conductance laws. Expanding the exact \(F_2\) formula gives
\[
 F_2(L_{2,n}^*)=\frac{n^6}{180}
 +\left(c^2+\frac c6+\frac1{90c}\right)n^5+o(n^5),
\]
whereas substitution of \(t_{1,n}=\sqrt{n/6}(1+o(1))\) yields
\[
 F_2(L_{1,n}^*)=\frac{n^6}{180}
 +\frac{\sqrt6}{90}n^{11/2}+O(n^5).
\]
Subtracting proves the claimed sharp regret. Every asymptotic statement follows from exact identities, not from finite numerical extrapolation.

## Verification

Run `python3 check_sunlet.py` with NumPy and SciPy installed. The script evaluates the exact coefficient formulas, the sign of the optimizing cubic, independent full-Laplacian eigenspectra on multiple sunlets, scalar numerical minimizers, heterogeneous competing edge allocations, the strict first-versus-second allocation ordering over a finite diagnostic range, and asymptotic constants. Its successful output is:

`PASS: 1009 finite analytical/numerical assertions`

`c=0.153242321348; m=3: (t2,t1)=0.7653298918,0.7302967433; m=4: 0.8992407105,0.8451542547`

These finite tests support, but cannot replace, the all-size proof. No formal proof assistant or independent validation is claimed.

## Relationship to prior work

Patterson and Bamieh (2013) define first- and second-order stochastic consensus coherence and use the squared-reciprocal Laplacian spectral sum to analyze fractal networks; their investigated examples and derivations do not treat cost-optimized sunlets. Ghosh, Boyd, and Saberi (2008) provide the convex total-effective-resistance design framework, including tree, wheel, and barbell examples, for the **first** inverse moment. Du, Zhu, Gao, and Li (2022) derive weighted-corona characteristic polynomials and the **first-order** coherence of such networks, without optimizing second-order coherence. Closely related explicit sunlet and transitive-corona results on the published mathematical record maximize algebraic connectivity (the smallest positive Laplacian eigenvalue); that max-min problem is not the sum of squared reciprocal eigenvalues, and its explicit edge rates do not determine the cubic optimizer here. Standard fixed-weight corona spectral identities alone do not supply the budget-constrained optimum, its strict mismatch, or the sharp cross-objective regret.

## Limitations

Only one private pendant leaf per cycle vertex, a common linear cost for every edge, symmetric undirected weighted Laplacians, a total unit budget, and connected support are covered. Different edge prices, general corona bases, nonuniform vertex masses, separate position/velocity feedback gains, and network-topology selection are not asserted. The second-order coherence normalization is suppressed because it is a positive constant for the fixed system size; statements about absolute regret refer to the unnormalized spectral trace \(F_2\). The relative regret tends to zero, so the theorem is not a constant-factor separation. Unindexed equivalent specializations and unexamined literature are residual priority risks; this is not independent peer review.

## References

1. S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1, publicly posted 2013-10-09, especially Section II-B and Appendix A. https://arxiv.org/pdf/1310.2592
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37--66, DOI 10.1137/050645452, especially Sections 1, 4, and 5. https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. W. Du, J. Zhu, H. Gao, and X. Li, *Consensus analysis of the weighted corona networks*, Frontiers in Physics 10 (2022), article 948247, especially Sections 3--4. https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2022.948247/full
4. *Unique price-optimal fastest mixing on sunlet networks*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-unique-price-optimal-fastest-mixing-on-sunlet-networks--638ad6225b9e
5. *Exact price-optimal continuous-time mixing on transitive one-leaf coronas and rigid cyclic sunlets*, published mathematical result, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-price-optimal-continuous-time-mixing-on-transitive-one-lea--eed5b428788a
