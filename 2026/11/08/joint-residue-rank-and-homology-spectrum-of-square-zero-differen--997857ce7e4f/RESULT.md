# Joint residue-rank and homology spectrum of square-zero differentials over split local algebras

## Finding
Let \(q\) be any prime power, \(k=\mathbb F_q\), and \(n,d\ge1\). Put
\[
R=k\oplus V=k[\varepsilon_1,\ldots,\varepsilon_d]/(\varepsilon_i\varepsilon_j:1\le i,j\le d),\quad \dim_k V=d.
\]
For each \(X\in M_n(R)\) with \(X^2=0\), let \(r=\operatorname{rank}_k(X\bmod V)\), and let \(h\) be the ordinary \(k\)-linear rank of the induced map on \(R^n\), a space of dimension \((d+1)n\) over \(k\). Put \(s=n-2r\). For \(0\le r\le\lfloor n/2\rfloor\), \(0\le t\le s\), the exact number with
\[
h=(d+1)r+t
\]
is
\[
\boxed{B_{n,d,q}(r,t)=
\begin{bmatrix}n\\r\end{bmatrix}_q
\begin{bmatrix}n-r\\r\end{bmatrix}_q
|\mathrm{GL}_r(k)|\,q^{2dr(n-r)}
\begin{bmatrix}s\\t\end{bmatrix}_q
\begin{bmatrix}ds\\t\end{bmatrix}_q
|\mathrm{GL}_t(k)|.}
\]
Here Gaussian coefficients are zero outside their natural ranges, and \(|\mathrm{GL}_0(k)|=1\). Every displayed pair occurs; no other pairs occur. In particular, the full rank-generating polynomial is
\[
P_{n,d,q}(z)=\sum_{r=0}^{\lfloor n/2\rfloor}\sum_{t=0}^{n-2r} B_{n,d,q}(r,t)z^{(d+1)r+t}.
\]
For the one-periodic complex with the same differential in each degree, \(\cdots\xrightarrow{X}R^n\xrightarrow{X}R^n\xrightarrow{X}\cdots\), its homology has \(k\)-dimension
\[
\dim_k\ker(X)/\operatorname{im}(X)=(d+1)n-2((d+1)r+t).
\]
Hence its smallest possible homology dimension is \(0\) for even \(n\) and \(d-1\) for odd \(n\) (both sharp), and its largest possible differential rank is \(n+(d-1)\lfloor n/2\rfloor\). If \(d\ge2\), the complex is exact precisely when \(n\) is even and \(r=n/2\). If \(d=1\), exactness instead is equivalent to \(t=n-2r\), and is possible for every \(n\).

For \(n=2\) the polynomial simplifies to
\[
P_{2,d,q}(z)=1+(q+1)(q^{2d}-1)z+(q^{2d}-1)(q^{2d}-q)z^2+(q^2-1)q^{2d}z^{d+1}.
\]
For \(d\ge3\), the ranks \(3,4,\ldots,d\) are absent although both rank \(2\) and rank \(d+1\) occur. For \((q,n,d)=(2,2,3)\), the rank multiplicities at \(0,1,2,4\) are \(1,189,3906,192\), totaling \(4288\); rank \(3\) never occurs.

## Assumptions and scope
The ring is split, commutative, local, and has radical \(V\) with \(V^2=0\); its coefficient field is \(k\). No characteristic restriction is imposed. The word rank always means \(k\)-linear rank on \(R^n\), *not* McCoy rank, free-module rank of an image, or the residue-field rank \(r\). The homology is that of the periodic differential \(X\) on the underlying additive \(k\)-vector spaces, and is also an \(R\)-module, but only its \(k\)-dimension is enumerated.

## Proof
**1. Residue classes.** Write \(X=N+\sum_{j=1}^d\varepsilon_jY_j\), with \(N,Y_j\in M_n(k)\). Because \(V^2=0\), the square-zero equations are exactly
\[
N^2=0,\qquad NY_j+Y_jN=0\quad (1\le j\le d).
\]
They hold in every characteristic. A square-zero \(N\) of rank \(r\) has image of dimension \(r\), kernel of dimension \(n-r\), and image contained in kernel. Choose its image and kernel, then the induced isomorphism \(k^n/\ker N\to\operatorname{im}N\). This gives
\[
\#\{N:N^2=0,\operatorname{rank}N=r\}=
\begin{bmatrix}n\\r\end{bmatrix}_q
\begin{bmatrix}n-r\\r\end{bmatrix}_q|\mathrm{GL}_r(k)|.
\]

**2. Lift equations.** Fix one such \(N\). Choose a \(k\)-basis decomposition \(k^n=U\oplus W\oplus Z\) with \(\dim U=\dim W=r\), \(\dim Z=s\), where \(N:U\to W\) is the identity and \(N\) vanishes on \(W\oplus Z\). In the ordered blocks \((U,W,Z)\), the equations \(NY_j+Y_jN=0\) are equivalent to
\[
Y_j=\begin{pmatrix}A_j&0&0\\D_j&-A_j&F_j\\G_j&0&K_j\end{pmatrix},
\]
with unrestricted blocks \(A_j,D_j\) of size \(r\times r\), \(F_j\) of size \(r\times s\), \(G_j\) of size \(s\times r\), and \(K_j\) of size \(s\times s\). The four non-\(K\) blocks contribute exactly \(2r^2+2rs=2r(n-r)\) independent entries for every \(j\), hence \(q^{2dr(n-r)}\) possibilities. The \(d\) blocks \(K_j\) are completely independent.

**3. Rank on the full module.** Identify \(R^n\cong(k^n)^{d+1}\), with components \((v_0,v_1,\ldots,v_d)\). Multiplication by \(X\) sends
\[
(v_0,v_1,\ldots,v_d)\mapsto
(Nv_0,Nv_1+Y_1v_0,\ldots,Nv_d+Y_dv_0).
\]
For a kernel vector one needs \(Nv_0=0\), so write \(v_0=w+z\in W\oplus Z\). Each equation \(Nv_j=-Y_jv_0\) is solvable exactly when \(K_jz=0\); the component of \(Y_jv_0\) in \(W\) is always cancelable. When solvable, each \(v_j\) has \(q^{n-r}\) choices, since \(\ker N\) has dimension \(n-r\). Let
\[
K=\begin{pmatrix}K_1\\\vdots\\K_d\end{pmatrix}:Z\longrightarrow Z^d,
\qquad t=\operatorname{rank}_kK.
\]
Then \(\dim_k\ker X=(d+1)(n-r)-t\), giving \(h=(d+1)r+t\). The unrestricted matrix \(K\) has size \(ds\times s\), so the exact number of possible \(K\) of rank \(t\) is
\[
\begin{bmatrix}s\\t\end{bmatrix}_q\begin{bmatrix}ds\\t\end{bmatrix}_q|\mathrm{GL}_t(k)|.
\]
Multiplication by the preceding two factors proves the joint count. Each factor is positive on the stated range, proving all claimed rank-pair realizations.

**4. Homology and the sharp extremum.** Since \(\operatorname{im}X\subseteq\ker X\), rank-nullity gives \(\dim_kH=(d+1)n-2h\). As \(t\le n-2r\), we have \(h\le n+(d-1)r\), with equality attainable by choosing \(K\) of full column rank \(s\). Maximizing over \(r\le\lfloor n/2\rfloor\) proves the stated maximum and minimum homology. If \(d\ge2\), equality with \(\dim_kH=0\) forces \(n\) even and \(r=n/2\), and conversely these values give zero homology. When \(d=1\), the condition reduces to \(t=n-2r\), attainable for any \(r\), including \(r=0\) by \(X=\varepsilon_1I_n\).

**5. Two-dimensional rank gap.** For \(n=2\) either \(r=0\), with \(K\) a \(2d\times2\) matrix and ranks \(0,1,2\), or \(r=1\), when \(s=0\) and the full rank is \(d+1\). The rank-one, rank-two, and residue-rank-one matrix counts yield the displayed polynomial and the missing-rank interval.

## Verification
The standalone standard-library program `verify.py` performs direct exhaustive enumeration from the defining equation \(X^2=0\), computes the actual \(k\)-linear rank of the expanded \((d+1)n\times(d+1)n\) matrix by elimination, and compares its joint \((r,h)\)-histogram with an independently computed Gaussian-coefficient formula. Exhaustive cases include \((n,d,q)=(1,3,2),(2,1,2),(2,1,3),(2,2,2),(2,3,2),(3,1,2)\). It separately checks symbolic support extrema across small parameter ranges. Run `python3 verify.py` (Python 3 standard library only); success prints `VERIFY_OK`. These computations cover the specified small prime fields, not every finite field or dimension. The proof, not the computations, establishes universal validity.

## Relationship to prior work
Cheong, Liang and Strand (first made public September 8, 2022, arXiv:2209.03626v1) study matrix polynomial equations and fixed-residue cokernel distributions over prime-power integer rings subject to square-free/irreducible hypotheses on the polynomial modulo the residue characteristic. Their theorems do not cover the repeated-root relation \(X^2=0\) over the split multivariable square-zero local algebra used here. D'Alesio's account of representation schemes identifies the square-zero matrix variety over a field as a representation scheme, without providing this rank-and-homology counting formula over a nonreduced coefficient algebra. Standard finite-field square-zero Jordan-type counts and the *coarser* residue-rank marginal are not claimed as new: summing our formula over \(t\) recovers the familiar count of square-zero lifts for each residue rank,
\[
\begin{bmatrix}n\\r\end{bmatrix}_q
\begin{bmatrix}n-r\\r\end{bmatrix}_q|\mathrm{GL}_r(k)|\,q^{d((n-r)^2+r^2)}.
\]
The added statement is the entire **joint** distribution of residue rank and underlying-field rank, equivalently the homology-dimension spectrum of periodic free differentials, plus its sharp rank gaps and acyclicity boundary. An unlocated broader result on matrix lifting or periodic-complex rank distributions could still subsume the formula.

## Limitations
Only split square-zero local \(k\)-algebras are addressed. Mixed-characteristic local rings, higher radical powers, noncommutative coefficient algebras, the full \(R\)-module isomorphism type of homology, and conjugacy-orbit classification are outside the theorem. The finite experiments cannot certify uniqueness in the literature. No independent external review has been performed.

## References
- G. Cheong, Y. Liang, and M. Strand, *Polynomial equations for matrices over integers modulo a prime power and the cokernel of a random matrix*, arXiv:2209.03626v1, first posted 2022-09-08, https://arxiv.org/abs/2209.03626.
- S. D'Alesio, *Derived representation schemes and Nakajima quiver varieties*, Selecta Mathematica 28 (2022), article 10, https://doi.org/10.1007/s00029-021-00724-4 (Examples 1, especially item 3).
