# A sharp nonattaining codimension-two projection interval in real continuous-function space

## Finding
Let \(I_1=[0,1/3)\), \(I_2=[1/3,2/3)\), and \(I_3=[2/3,1]\). For \(f\in C([0,1];\mathbb R)\), let \(m_j(f)=3\int_{I_j}f(s)\,ds\). For every \(0<t\le1\), define the closed codimension-two subspace
\[
Y_t=\{f\in C([0,1];\mathbb R):m_1(f)=m_2(f),\ m_3(f)=t\,m_1(f)\}.
\]
Its relative projection constant is
\[
\boxed{\lambda(Y_t,C([0,1];\mathbb R))=2+\frac{t}{1+t+t^2}}.
\]
No bounded projection onto \(Y_t\) attains this infimum. As \(t\) runs through \((0,1]\), the right side runs bijectively through \((2,7/3]\). Since the largest absolute projection constant of a real two-dimensional Banach space equals \(4/3\), this is the full range of projection constants strictly above \(2\) allowed for nonattaining codimension-two subspaces of a real Daugavet space. It answers the codimension-two instance of Question 6.2 of Kania–Lewicki (2026).

## Assumptions and scope
All spaces and operators are **real**. For a complemented closed subspace \(E\subset X\), \(\lambda(E,X)\) means the infimum of \(\|P\|\) over bounded linear projections \(P:X\to E\). Let \(M[0,1]=C([0,1];\mathbb R)^*\) be the real signed Borel measures with variation norm. The functionals \(m_j\) are the probability measures \(\nu_j=3\mathbf1_{I_j}\,ds\). They have disjoint supports up to null sets. The parameter interval excludes \(t=0\); there is no nonattainment assertion at that boundary.

## Proof
**1. Exact finite-dimensional optimization.** Write \(a=(1,1,t)\), \(V_t=\{c\in\mathbb R^3:a\cdot c=0\}\subset\ell_1^3\), and \(s=1+t+t^2\). Any projection \(R:\ell_1^3\to V_t\) has the form \(R=I-u a^\top\) with \(a\cdot u=1\). For arbitrary such \(u=(u_1,u_2,u_3)\), the norms of its three columns are at least, respectively,
\[
L_1=1-u_1+u_2+u_3,\quad L_2=1+u_1-u_2+u_3,\quad L_3=1+t(u_1+u_2-u_3).
\]
These lower bounds come from evaluating the columns against the fixed sign vectors \((1,-1,-1)\), \((-1,1,-1)\), and \((-1,-1,1)\). With \(b=t(1+t)/2>0\), an exact dual identity is
\[
b(L_1+L_2)+L_3=(2b+1)\left(1+\frac{t}{s}\right).
\]
Indeed \(2b+1=s\) and the numerator is \(s+t(a\cdot u)=s+t\). Thus every projection has norm at least \(r_t=1+t/s\).

Set \(x=(1+t)/(2s)\), \(y=t/s\), and \(u_*=(x,x,y)\). Then \(a\cdot u_*=1\), and \(R_*=I-u_*a^\top\) has all three \(\ell_1\) column norms equal to \(r_t\), so
\[
\lambda(V_t,\ell_1^3)=r_t.
\]
Moreover, \(R_*\) is the **unique** minimizing projection: if \(\|R\|\le r_t\), positivity of both dual weights forces \(L_1=L_2=L_3=r_t\); the first two equations give \(u_1=u_2\), the first gives \(u_3=t/s\), and \(a\cdot u=1\) determines \(u_1=u_2=x\). Its first two columns are \(q_1=(1-x,-x,-y)\) and \(q_2=(-x,1-x,-y)\), both of norm \(r_t\), with strict sign patterns \((+,-,-)\) and \((-,+,-)\).

**2. The exact dual measure constant.** The map \(J:\ell_1^3\to M[0,1]\), \(J(c)=\sum_{j=1}^3 c_j\nu_j\), is an isometry. Put \(W_t=J(V_t)\). The mass map \(B:M[0,1]\to\ell_1^3\), \(B\mu=(\mu(I_1),\mu(I_2),\mu(I_3))\), is a contraction and \(BJ=I\). Hence \(JR_*B\) projects \(M[0,1]\) onto \(W_t\) with norm \(r_t\). Restricting any projection onto \(W_t\) to \(J(\ell_1^3)\) proves the opposite bound. Therefore
\[
\lambda(W_t,M[0,1])=r_t.
\]
The annihilator \(W_t^\perp\subset C([0,1];\mathbb R)\) is precisely \(Y_t\): its three interval means are orthogonal to \(\ker a\), hence proportional to \(a\). By the finite-codimensional Daugavet duality theorem of Kania–Lewicki (2026, Theorem 3.1),
\[
\lambda(Y_t,C([0,1];\mathbb R))=1+\lambda(W_t,M[0,1])=1+r_t.
\]
For completeness, the mechanism is that the complement of any projection onto \(Y_t\) is finite rank; the Daugavet identity yields \(\|P\|=1+\|I-P\|\). Taking adjoints converts the complementary projection into a weak-star continuous projection onto \(W_t\), and local reflexivity gives equality of the weak-star and unrestricted projection infima, as proved in the cited theorem. Alternatively, weak-star continuous projections of norms approaching \(r_t\) can be obtained by continuously interpolating the three columns of \(R_*\) across arbitrarily short neighborhoods of the interval boundaries and applying small continuous, interior-supported mean corrections. Their coefficient vectors remain in \(V_t\), preserve the three required means, and have uniform \(\ell_1\)-norm at most \(r_t+o(1)\).

**3. Nonattainment without duplication rigidity.** Suppose a projection \(P:C([0,1];\mathbb R)\to Y_t\) had norm \(1+r_t\). Its complementary adjoint \(Q=(I-P)^*:M[0,1]\to W_t\) would be a weak-star continuous projection of norm \(r_t\). The restriction of \(Q\) to \(J(\ell_1^3)\) must be \(JR_*J^{-1}\), by the uniqueness above. Since \(Q\) is weak-star continuous and finite rank, its coefficients are continuous: there is a continuous vector function \(g:[0,1]\to V_t\) with
\[
Q\mu=\sum_{j=1}^3\left(\int g_j(s)\,d\mu(s)\right)\nu_j,
\qquad \|g(s)\|_1\le r_t\ \ (s\in[0,1]).
\]
For each \(j\), the average of \(g\) over \(I_j\) equals the column \(q_j=R_*e_j\). In particular, the first two columns have norm \(r_t\). Evaluating their averages against \(\sigma_1=(1,-1,-1)\) and \(\sigma_2=(-1,1,-1)\), respectively, shows that the continuous functions \(\sigma_1\cdot g\) and \(\sigma_2\cdot g\), each everywhere at most \(r_t\), have average \(r_t\) on \(I_1\) and \(I_2\), respectively. Therefore
\[
\sigma_1\cdot g(s)=r_t\ (s\in\overline{I_1}),\qquad
\sigma_2\cdot g(s)=r_t\ (s\in\overline{I_2}).
\]
At their common boundary \(s=1/3\), both equalities hold. Since \(\|g(s)\|_1\le r_t\), equality against both signs requires \(g_1(s)=g_2(s)=0\) and \(g_3(s)=-r_t\). This contradicts \(g(s)\in V_t\), because \(g_1+g_2+t g_3=-t r_t\ne0\). Thus no minimum-norm projection onto \(Y_t\) exists.

**4. Full sharp interval.** The map \(t\mapsto t/(1+t+t^2)\) is continuous and strictly increasing on \((0,1)\), with derivative \((1-t^2)/(1+t+t^2)^2\), lower limit \(0\), and value \(1/3\) at \(t=1\). The classical real two-dimensional Grünbaum bound \(\lambda_2=4/3\) makes \(7/3\) the greatest possible codimension-two projection constant in a Daugavet space. This establishes the claimed sharp interval.

## Verification
Run `python check_exact.py` using Python 3 standard library. It checks exact rational versions of the rank-two projection identity, all column norms, both facet sign patterns, the dual lower-bound identity for a wide grid of auxiliary vectors satisfying \(a\cdot u=1\), and the monotonicity sign. The check is finite and does not establish the continuous-function nonattainment or the universal quantifiers; those follow from the preceding proof. At \(t=1\), the finite-dimensional minimizing matrix is \(I-\frac13\mathbf1\mathbf1^\top\), with norm \(4/3\).

## Relationship to prior work
Kania and Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections* (arXiv:2604.10771v1, first posted April 12, 2026), prove the duality theorem used here and construct codimension-two nonattaining constants throughout \((2,(3+\sqrt2)/2]\) (Theorem 5.2). Their Question 6.2 asks for the entire interval \((2,1+\lambda_n]\), in particular at codimension two. The present elementary three-block family reaches the complete codimension-two interval, including the extremal endpoint \(7/3\). It uses sharp, incompatible column norming faces rather than the unique-minimizer-on-all-duplicates hypothesis of their Theorem 4.4.

The absolute planar constant \(\lambda_2=4/3\) is classical (Grünbaum conjecture, proved by Chalmers–Lewicki, 2010; see also Deręgowska–Lewandowska, arXiv:2206.09454). The finite-dimensional extremal hexagonal plane and ordinary finite-dimensional projection calculations are **not** new claims. The asserted contribution is their realization as sharp **unattained** projection constants at each fixed codimension-two value, including the full endpoint.

## Limitations
The construction and nonattainment proof use real scalars, three contiguous equal-length intervals, and the Daugavet property of \(C[0,1]\). The case \(t=0\) is excluded. No assertion is made for higher fixed codimension or for complex scalars. The mathematical argument is self-contained apart from explicitly cited classical projection-constant/Daugavet facts. An equivalent older formulation in the approximation-theory literature remains a publication-priority risk; no independent mathematical or bibliographic audit has been performed.

## References
1. T. Kania and G. Lewicki, *Finite-codimensional subspaces of Daugavet spaces: projection constants and minimal projections*, arXiv:2604.10771v1 (2026), especially Theorems 3.1, 4.4, 5.2 and Question 6.2. https://arxiv.org/html/2604.10771v1
2. B. L. Chalmers and G. Lewicki, *A proof of the Grünbaum conjecture*, Studia Math. 200 (2010), 103–129. DOI: 10.4064/sm200-2-1.
3. B. Deręgowska and B. Lewandowska, *A simple proof of the Grünbaum conjecture*, arXiv:2206.09454 (2022), J. Funct. Anal. 285 (2023), 109950. https://arxiv.org/abs/2206.09454
4. B. L. Chalmers and G. Lewicki, *Two-dimensional real symmetric spaces with maximal projection constant*, Ann. Polon. Math. 73 (2000), 119–134. DOI: 10.4064/ap-73-2-119-134.
