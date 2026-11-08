# Multiplicity-optimal consecutive outer actuators on every generalized Petersen graph

## Finding

For every integer \(n\ge5\) and \(2\le k<n/2\), let \(G=\operatorname{GP}(n,k)\) be the *unweighted generalized Petersen graph*: its vertices are \(u_i,v_i\) indexed modulo \(n\), with edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+k}\). Write \(L=3I-A_G\) for its combinatorial Laplacian, and for a vertex set \(S\) let \(B_S\) consist of the corresponding coordinate columns. We consider the exact, fixed-matrix, continuous-time system \(\dot x=-Lx+B_S w\), with one independent scalar input at each selected vertex.

Put \(\theta_j=2\pi j/n\) and
\[
\Phi_j(\lambda)=(3-2\cos\theta_j-\lambda)(3-2\cos(k\theta_j)-\lambda)-1,
\quad J_\lambda=\{0\le j<n:\Phi_j(\lambda)=0\}.
\]
The minimum number of coordinate actuators is *exactly* the maximum spectral multiplicity,
\[
\boxed{\kappa(G)=r:=\max_{\lambda\in\mathbb R}|J_\lambda|.}
\]
**A universally optimal construction is the first \(r\) consecutive OUTER vertices**
\[
\boxed{S_r=\{u_0,u_1,\ldots,u_{r-1}\}.}
\]
Moreover \(2\le r\le \min\{n,2k+2\}\). Both the optimal number and the actual placement are thus specified by the graph's explicit two-band spectrum, even when several different Fourier frequencies share an eigenvalue.

For example, \(\kappa(\operatorname{GP}(11,2))=2\): its two adjacent outer vertices suffice, whereas its published *zero-forcing number* is \(6\). This is an exact separation between fixed-Laplacian controllability and the stronger zero-forcing criterion; the two notions must not be conflated.

## Assumptions and scope

The vertex labels are interpreted modulo \(n\), all graph edges have weight one, no other edges or loops are present, and both the outer and inner cycles use the same time-invariant combinatorial Laplacian. Each input channel can be actuated independently. Full-state Kalman controllability is required; there is no parameter uncertainty, nonlinearity, sign restriction on the input, or minimization of control energy. The range \(2k<n\) rules out the double-counting of an inner edge when \(n=2k\).

The spectral maximum ranges only over the finitely many roots of \(\Phi_j\), not over an unspecified continuum. Repeated occurrences across distinct indices are counted, including \(j\) and \(n-j\). Coincidence of the two eigenvalues *within the same frequency block* cannot occur because its off-diagonal entry is \(-1\).

## Proof

**Fourier eigenspaces.** Let \(\omega=\exp(2\pi i/n)\), \(f_j=(\omega^{ij})_{i=0}^{n-1}\). In the layer order \((u_0,\ldots,u_{n-1};v_0,\ldots,v_{n-1})\), the Laplacian has the block form
\[
L=\begin{pmatrix}3I-(C+C^{-1})&-I\\-I&3I-(C^k+C^{-k})\end{pmatrix},
\]
where \(Cf_j=\omega^j f_j\). The invariant two-dimensional frequency space spanned by \((f_j,0)\) and \((0,f_j)\) has restriction
\[
M_j=\begin{pmatrix}3-2\cos\theta_j&-1\\-1&3-2\cos(k\theta_j)\end{pmatrix}.
\]
Its characteristic polynomial is precisely \(\Phi_j(\lambda)\). It is real symmetric and has two **distinct** eigenvalues, since its discriminant is \(4[(\cos\theta_j-\cos(k\theta_j))^2+1]>0\). Also, any eigenvector \((a,b)\) of \(M_j\) has \(a\ne0\): if \(a=0\), the first row forces \(b=0\). Hence for each \(\lambda\) the full complex eigenspace of \(L\) has exactly the basis \((f_j,c_jf_j)\), for \(j\in J_\lambda\), with suitable scalar \(c_j\). Consequently \(\dim E_\lambda=|J_\lambda|\).

**Necessary number of inputs.** For a real symmetric state matrix, the Popov--Belevitch--Hautus (PBH) criterion says \((-L,B_S)\) is controllable if and only if the coordinate restriction \(E_\lambda\to\mathbb C^S\) is injective for every eigenvalue. An eigenspace of dimension \(r\) cannot inject into fewer than \(r\) coordinate channels. Therefore \(|S|\ge r\).

**Consecutive outer vertices attain it.** For fixed \(\lambda\), put \(m=|J_\lambda|\le r\). The restriction of the above eigenspace basis to \(u_0,\ldots,u_{m-1}\) is the square matrix \((\omega^{ij})_{0\le i<m,\,j\in J_\lambda}\). This is a Vandermonde matrix in the **distinct** points \(\omega^j\); its determinant is their nonzero pairwise-difference product. Therefore restriction to the larger set \(S_r\) is injective on every eigenspace, so PBH proves full controllability. Combining with the lower bound proves \(\kappa(G)=r\) and the optimality of the displayed placement for *every* allowed \(n,k\). Complex Fourier vectors cause no issue: complexifying a real controllability matrix preserves its rank.

**Dimension bound.** Let \(T_k\) be the Chebyshev polynomial satisfying \(T_k(\cos\theta)=\cos(k\theta)\). For fixed \(\lambda\), the equation for frequencies can be rewritten as
\[
F_\lambda(t)=(3-2t-\lambda)(3-2T_k(t)-\lambda)-1=0,
\qquad t=\cos(2\pi j/n).
\]
The coefficient of \(t^{k+1}\) in \(F_\lambda\) is \(2^{k+1}\ne0\). Consequently there are at most \(k+1\) distinct real values \(t\) solving it, each attained by at most two frequency indices modulo \(n\). Hence \(|J_\lambda|\le2k+2\) for every eigenvalue. The \(n\) frequency spaces give the trivial cap \(|J_\lambda|\le n\); the pairing of frequency \(1\) with \(n-1\) yields \(r\ge2\).

**An exact two-versus-six example.** At \((n,k)=(11,2)\), write \(t=2\cos(2\pi j/11)\). For \(1\le j\le5\), these five distinct values are precisely the roots of
\[
H(t)=t^5+t^4-4t^3-3t^2+3t+1.
\]
The two eigenvalues in each frequency block satisfy \(Q(t,\lambda)=(3-t-\lambda)(5-t^2-\lambda)-1=0\). Eliminating \(t\) gives the following monic polynomial, computed as the exact resultant \(\operatorname{Res}_t(H,Q)\):
\[
\begin{aligned}
R(\lambda)={}&\lambda^{10}-32\lambda^9+447\lambda^8-3578\lambda^7+18109\lambda^6\\
 &-60301\lambda^5+133122\lambda^4-191202\lambda^3\\
 &+169675\lambda^2-83215\lambda+16951.
\end{aligned}
\]
Modulo two, \(R'(\lambda)=(\lambda+1)^4\) and \(R(1)=1\), so \(\gcd(R,R')=1\) modulo two, and thus over the rationals: all ten roots are distinct. The remaining \(j=0\) block has eigenvalues \(0,2\), neither of which is a root, since \(R(0)=16951\) and \(R(2)=-11\). Accordingly, each of the ten nontrivial block eigenvalues occurs at exactly the two mirror frequencies \(j\) and \(11-j\), and the other two eigenvalues occur once. Thus \(r=2\), proving the claimed two-actuator optimum. Rashidi--Poursalavati--Tavakkoli (2020), Theorem 2.5, prove \(Z(\operatorname{GP}(n,2))=6\) for \(n\ge10\), establishing the comparison.

## Verification

The accompanying standard-library `verify_gp.py` constructs the exact integral graph Laplacian, forms the finite Kalman controllability matrix, and computes its rank modulo \(1000003\). Full row rank modulo this prime rigorously implies full row rank over the rationals and reals. It checks 19 graph parameter pairs, including \((11,2)\) where the two-column control placement attains full rank \(22\), and \((15,2)\) with six actuators. The program reconstructs the displayed degree-ten resultant by a five-dimensional quotient-ring multiplication determinant **using integer arithmetic alone**, then checks its reduction modulo two, its derivative and endpoint values. A numerical eigenvalue clustering diagnostic is also run for each finite case; those clusters are *not* treated as exact multiplicity certificates, nor are deficient modular ranks treated as proofs of noncontrollability.

To replay from this extracted package, run `python3 verify_gp.py`. The infinite theorem is independently established by the preceding Fourier, Vandermonde and PBH proof. The finite program tests implementation and the exact eleven-gon arithmetic rather than establishing the theorem by enumeration.

## Relationship to prior work

Gera and Stănică (2011) supply the already-known two-band adjacency spectrum of generalized Petersen graphs; the Fourier blocks and their eigenvalues are **not claimed new** here. Parlangeli and Notarstefano (arXiv first public September 16, 2011) give path- and cycle-graph reachability conditions, including the effectiveness of adjacent cycle vertices; they do not establish multiplicity-optimal coordinate placement on generalized Petersen graphs. Rashidi, Poursalavati and Tavakkoli (2020), Theorem 2.2, show that \(2k+2\) consecutive outer vertices form a zero-forcing set, so that **fixed upper-bound design is also prior work**. Their Theorem 2.5 gives the six-vertex zero-forcing number when \(k=2,n\ge10\). The present precise contribution instead adapts the outer block length to the *actual* maximum eigenspace dimension, proves it is globally minimum for the fixed Laplacian, and distinguishes the two actuator models; the \(\operatorname{GP}(11,2)\) calculation shows a strict four-input reduction compared with the known zero-forcing size. General minimal-leader methods such as Dai (2022, first online publication) concern other example graph classes and do not establish this explicit all-parameter formula.

## Limitations

The result does **not** classify every minimum placement. It makes no claim that two actuators suffice for all circumferences or that the zero-forcing number equals the spectral actuator minimum. The unweighted regular Laplacian, independent coordinate channels and fixed system matrix are essential; generic edge perturbations or strong structural controllability are outside the proved statement. The finite spectral formula may require exact algebraic comparison to resolve eigenvalue collisions for large \(n,k\); numerical rounding alone is inadequate. Publication priority beyond the specifically inspected works is not fully settled. No external independent mathematical review is asserted.

## References

1. R. Gera and P. Stănică, *The spectrum of generalized Petersen graphs*, Australasian Journal of Combinatorics 49 (2011), 39–45. https://ajc.maths.uq.edu.au/pdf/49/ajc_v49_p039.pdf
2. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, first public 2011-09-16. https://arxiv.org/abs/1109.3556
3. S. Rashidi, N. Shajareh Poursalavati and M. Tavakkoli, *Computing the zero forcing number for generalized Petersen graphs*, J. Algebra Comb. Discrete Appl. 7 (2020), 183–193. https://doi.org/10.13069/jacodesmath.729465
4. L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework*, first published 2022-10-29, IET Control Theory Appl. 17 (2023), 505–515. https://doi.org/10.1049/cth2.12385
