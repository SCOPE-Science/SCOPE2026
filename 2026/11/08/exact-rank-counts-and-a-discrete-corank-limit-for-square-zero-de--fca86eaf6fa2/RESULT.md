# Exact rank counts and a discrete corank limit for square-zero derivations of finite Heisenberg Lie algebras

## Finding
For every prime power \(q\), integer \(m\ge1\), and \(0\le k\le m\), the number \(N_{m,k}(q)\) of square-zero ordinary derivations of the \((2m+1)\)-dimensional Heisenberg Lie algebra having linear rank \(k\) is explicitly determined. Put \(M_{m,-1}=0\), and for \(0\le r\le m\), define
\[
M_{m,r}(q)=q^{r(2m-r+1)}
\frac{\displaystyle\prod_{t=m-r+1}^{m}(1-q^{-2t})}
{\displaystyle\prod_{i=1}^{\lfloor r/2\rfloor}(1-q^{-2i})}.
\]
The rational product is an integer. The complete distribution is
\[
\boxed{N_{m,0}(q)=1,\qquad
N_{m,k}(q)=q^{k}M_{m,k}(q)+
\big(q^{2m-k+1}-q^{k-1}\big)M_{m,k-1}(q)
\quad(1\le k\le m).}
\]
All other ranks have count zero, and every rank in the stated interval occurs.

For fixed \(q\), choose \(D\) uniformly among all derivations satisfying \(D^2=0\). Then \(J_m=m-\operatorname{rank}D\) converges in total variation as \(m\to\infty\). Writing an empty product as one, define
\[
w_j(q)=\frac{q^{-j(j+2)}+q^{-(j+1)^2}}
{\prod_{i=1}^{j}(1-q^{-2i})},\quad
Z_q=\sum_{j=0}^{\infty}w_j(q).
\]
The sum satisfies \(0<Z_q<\infty\), and the limiting law is
\[
\boxed{\lim_{m\to\infty}\Pr(J_m=j)=\frac{w_j(q)}{Z_q}\quad(j\ge0),}
\]
with convergence in total variation, not merely pointwise. In particular \(\Pr(\operatorname{rank}D=m)\) converges to \((1+q^{-1})/Z_q\), a strictly positive number below one; for \(q=2\), it is approximately \(0.8530484194\).

## Assumptions and scope
Let \(\mathbb F_q\) be the field of order \(q\), including even characteristic. Let \(V\) be a vector space of dimension \(2m\), equipped with a nondegenerate alternating bilinear form \(\omega\). Set \(H=V\oplus \mathbb F_q z\), with Lie bracket
\[
[v+az,w+bz]=\omega(v,w)z.
\]
An **ordinary derivation** is a field-linear map satisfying \(D([x,y])=[D(x),y]+[x,D(y)]\). No compatibility with a restricted Lie-algebra \(p\)-map is assumed. \(D^2=0\) denotes composition-square zero, not the square of its adjoint action. Ranks are dimensions over \(\mathbb F_q\). All formulas hold for each \(m\ge1\) and every prime-power \(q\).

## Proof
**1. Derivation equations.** Since \([H,H]=\mathbb F_q z\), a derivation has the unique form
\[
D(v)=Av+\phi(v)z,\qquad D(z)=\lambda z,
\]
where \(A\in\operatorname{End}(V)\), \(\phi\in V^*\), and \(\lambda\in\mathbb F_q\). Applying the derivation identity to \([v,w]\) is equivalent to
\[
\omega(Av,w)+\omega(v,Aw)=\lambda\omega(v,w)
\quad\text{for all }v,w\in V.
\]
Now \(D^2(z)=\lambda^2z\), so \(D^2=0\) implies \(\lambda=0\) in every field. Its remaining blocks yield exactly
\[
\omega(Av,w)+\omega(v,Aw)=0,\qquad A^2=0,
\qquad\phi\circ A=0.
\]
Conversely these three conditions imply the derivation identity and \(D^2=0\). The central functional \(\phi\) is unconstrained by the derivation identity itself.

**2. Classification of the symplectic square-zero block.** Fix a linear \(A\) satisfying the displayed symplectic and square-zero equations, and set \(W=\operatorname{im}A\), \(r=\dim W\). Because
\(\omega(Ax,Ay)=-\omega(x,A^2y)=0\), \(W\) is totally isotropic, hence \(0\le r\le m\). The skew-adjointness equation gives
\(\ker A=W^\perp\). On the \(r\)-dimensional quotient \(Q=V/W^\perp\), the rule
\[
b(\bar v,\bar w)=\omega(Av,w)
\]
is well-defined, symmetric, and nondegenerate. Symmetry follows from \(\omega(Av,w)=-\omega(v,Aw)=\omega(Aw,v)\); nondegeneracy follows from \(\ker A=W^\perp\). Conversely, every totally isotropic \(r\)-plane \(W\) and every nonsingular symmetric bilinear form on \(Q\) uniquely reconstruct \(A\) by \(\omega(Av,w)=b(\bar v,\bar w)\). Indeed the form identifies \(Q\) with \(Q^*\), while \(W=(W^\perp)^\perp\), so the image is precisely \(W\), the symplectic relation holds, and \(A^2=0\). This works in characteristic two because the condition is **symmetric**, not alternating: diagonal values are allowed.

The number of totally isotropic \(r\)-planes in a symplectic \(2m\)-space is
\[
I_{m,r}(q)={m\brack r}_q\prod_{i=0}^{r-1}(q^{m-i}+1)
=\frac{\prod_{t=m-r+1}^{m}(q^{2t}-1)}{\prod_{i=1}^{r}(q^i-1)}.
\]
The number of nonsingular symmetric \(r\times r\) matrices over \(\mathbb F_q\), with **unrestricted diagonal**, is the established MacWilliams count
\[
S_r(q)=q^{r(r+1)/2}\prod_{i=1}^{\lceil r/2\rceil}
(1-q^{-(2i-1)}).
\]
It is valid for all prime powers. Thus the number of admissible \(A\) of rank \(r\) is \(I_{m,r}(q)S_r(q)\). Canceling odd-index factors in \(\prod_{i=1}^{r}(1-q^{-i})\) gives exactly \(M_{m,r}(q)\) above. This also proves integrality.

**3. Rank split for the central functional.** Fix such \(A\) of rank \(r\). The equation \(\phi\circ A=0\) says \(\phi\) annihilates \(W\), so there are \(q^{2m-r}\) possible functionals. For the map \(D\) on \(V\oplus\mathbb F_qz\), one has \(\operatorname{rank}D=r\) exactly when \(\phi\) vanishes on \(\ker A\); otherwise \(\operatorname{rank}D=r+1\). Exactly \(q^r\) functionals vanish on \(\ker A\), because \(\dim(V/\ker A)=r\). Hence the counts at ranks \(r\) and \(r+1\) are respectively \(q^rM_{m,r}\) and \((q^{2m-r}-q^r)M_{m,r}\). For \(r=m\), \(W=W^\perp\), so the latter quantity vanishes. Combining the two contributions for each rank gives the formula in the Finding. Positivity is immediate for every \(0\le k\le m\).

**4. Limit law.** Let
\[
P_q=\prod_{i=1}^{\infty}(1-q^{-2i})>0.
\]
The product form gives the uniform estimate
\[
0\le M_{m,r}\le P_q^{-1}q^{r(2m-r+1)}
\quad(0\le r\le m).
\]
For fixed \(j\ge0\), substitute \(r=m-j\) into the exact count. Since
\[
\frac{M_{m,m-j}}{q^{(m-j)(m+j+1)}}
\longrightarrow\frac1{\prod_{i=1}^{j}(1-q^{-2i})},
\]
one gets
\[
\frac{N_{m,m-j}(q)}{q^{m(m+2)}}
\longrightarrow w_j(q).
\]
Here the two summands of \(w_j\) arise respectively from \(A\) of ranks \(m-j\) and \(m-j-1\). For all \(0\le j\le m\), the same product estimate gives the summable domination
\[
0\le q^{-m(m+2)}N_{m,m-j}(q)
\le P_q^{-1}\big(q^{-j(j+2)}+q^{-(j+1)^2}\big).
\]
For \(j=m\), the left side is \(q^{-m(m+2)}\) and the bound still holds. Extending the finite sequences by zero to all \(j>m\), dominated convergence on nonnegative integer indices shows
\[
q^{-m(m+2)}\sum_{k=0}^{m}N_{m,k}(q)\longrightarrow Z_q.
\]
Normalization and domination yield convergence of the entire mass function in \(\ell^1\), which is total-variation convergence. Each \(w_j\) is positive, so the limit is nondegenerate.

## Verification
A standalone `verify.py` independently enumerates all symmetric matrices representing \(A\), retains those with \(A^2=0\), enumerates compatible central functionals, and performs finite-field row reduction to obtain ranks. Cases include \((m,q)=(1,2),(1,3),(1,5),(2,2),(2,3)\), plus an independent \(\mathbb F_4\) extension-field implementation for \(m=1\). It separately checks **every** linear \(3\times3\) matrix over \(\mathbb F_2\) and \(\mathbb F_3\) against the original Lie derivation identity and \(D^2=0\), not just the symplectic parametrization. It also verifies product-factor cancellation as an exact rational identity and compares finite-dimensional maximal-rank probabilities with the limiting weights. Running `python3 verify.py` ends in `VERIFY_OK` when all assertions pass.

Representative exact rank vectors \((N_{m,0},\ldots,N_{m,m})\) are \((1,9)\) for \((m,q)=(1,2)\), \((1,32)\) for \((1,3)\), \((1,75)\) for \((1,4)\), \((1,45,330)\) for \((2,2)\), and \((1,320,8400)\) for \((2,3)\). These checks support, but do not replace, the proof for arbitrary dimension and field size.

## Relationship to prior work
La Rosa and Mancini study derivation algebras of two-step nilpotent algebras, including Heisenberg examples, with substantial emphasis on the complex and real cases. Their published structural treatment (including a characteristic-not-two assumption in the general preliminaries) is an antecedent for the derivation-block representation; the present argument independently verifies the block equations in every characteristic. The full accessible text does not state finite-field rank multiplicities for square-zero derivations or the total-variation limit.

MacWilliams already counted symmetric matrices by rank over arbitrary finite fields. Lewis, Liu, Morales, Panova, Sam, and Zhang explicitly reproduce that formula in Section 4, equation (4.5). The nonsingular symmetric-form factor is **prior mathematics**, and the count above does not claim novelty for that factor or for standard symplectic isotropic-subspace counts. The contribution assessed here is the combined exact rank distribution for square-zero Heisenberg derivations (including their central-functional rank transitions) and its discrete-Gaussian-type limiting corank law.

The literature comparison includes general nilpotent-orbit enumeration for classical Lie algebras, but such formulas for symplectic blocks alone do not account for the \(\phi\)-dependent rank split in derivations. Nonetheless, a broader unlocated theorem on square-zero derivations or their rank distribution could imply this result; publication priority has not been independently established.

## Limitations
The theorem concerns ordinary field-linear derivations of split finite Heisenberg Lie algebras, not general two-step nilpotent Lie algebras, higher nilpotence indices, restricted derivations, or group automorphisms. The limiting distribution holds for fixed \(q\) as \(m\to\infty\); it is not a joint field-size/dimension limit. Proofs give exact counts without requiring numerical extrapolation. Independent mathematical review and comprehensive publication-priority verification remain outstanding.

## References
1. G. La Rosa and M. Mancini, *Derivations of two-step nilpotent algebras*, arXiv:2301.11058v1, first publicly posted January 26, 2023; https://arxiv.org/abs/2301.11058.
2. J. MacWilliams, *Orthogonal Matrices Over Finite Fields* (1969), Theorem 2, DOI:10.1080/00029890.1969.12000160.
3. J. B. Lewis, R. I. Liu, A. H. Morales, G. Panova, S. V. Sam, and Y. X. Zhang, *Matrices with restricted entries and q-analogues of permutations*, Journal of Combinatorics 2 (2011), 355–396, arXiv:1011.4539, equation (4.5); https://arxiv.org/abs/1011.4539.
4. J. Feldvoss, S. Siciliano, and T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629 (existence results for a distinct derivation category).
