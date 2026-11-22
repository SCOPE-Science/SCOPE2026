# Exact all-vertex sensing resonances and a totient placement law on a one-defect diffusion ring

## Finding

**Theorem (complete single-vertex placement classification).** For each integer \(n\ge5\), form the undirected cycle on vertices \(0,1,\ldots,n-1\). All edges \(\{i,i+1\}\), for \(0\le i<n-1\), have conductance \(1\), whereas the edge \(\{0,n-1\}\) has conductance \(w>0\). Write \(L_n(w)\) for the combinatorial weighted Laplacian. For an actuator or sensor at vertex \(s\), let
\[
 j=\min\{s,n-1-s\},\qquad 0\le j\le\lfloor(n-1)/2\rfloor.
\]
The pair \((-L_n(w),e_s)\) is controllable, equivalently \((-L_n(w),e_s^{\mathsf T})\) is observable, **if and only if** all the following conditions hold:

1. \(w\ne1\).
2. If \(n=2m+1\), then \(j\ne m\). If \(n=2m\), then \(\gcd(2j+1,m)=1\).
3. For every integer \(k\) satisfying
   \[
    1\le k\le\left\lfloor\frac{n-2j-2}{2}\right\rfloor,
    \quad \theta_k=\frac{2\pi k}{n-2j-1},
   \]
   for which \(\sin(j\theta_k)\ne0\), the positive number
   \[
    \omega_{n,j,k}=\frac12\left(1-\frac{\sin((j+1)\theta_k)}{\sin(j\theta_k)}\right)
   \]
   is not equal to \(w\). Values \(\omega_{n,j,k}\le0\) are irrelevant because \(w>0\). When \(j=0\), or the range of \(k\) is empty, this condition is vacuous.

In particular, the two endpoints of the exceptional edge (\(j=0\)) are controllable at every positive nonunit weight; interior positions can have both permanent geometric blind spots and isolated weight-dependent resonances.

**Arithmetic specialization (exact placement census and rank loss).** If \(n=2m+1\ge5\) is odd and \(w=1/2\), then for every \(0\le j<m\), the rank deficiency of the one-vertex Kalman matrix at either vertex of reflected distance \(j\) is exactly
\[
 \delta_j=\gcd(m+1,j+1)-1.
\]
The opposite central vertex \(j=m\) has deficiency \(m\). Hence the number of *labelled* single-vertex locations with complete controllability is precisely
\[
 \boxed{\ 2\varphi(m+1)=2\varphi\!\left(\frac{n+1}{2}\right)\ },
\]
where \(\varphi\) is Euler's totient function. This can be a small minority of the ring; for example, at \(n=11\) exactly the four vertices \(\{0,4,6,10\}\) work. Along \(n=4r-1\), the vertex at reflected distance \(r-1\) loses exactly \(r-1\) modes at \(w=1/2\), so the loss is unbounded with network size.

## Assumptions and scope

All statements use real finite-dimensional continuous-time consensus dynamics and the unnormalized symmetric weighted graph Laplacian. Input or output is the state of exactly one coordinate. Controllability means rank \(n\) of the finite Kalman matrix \([e_s,L_ne_s,\ldots,L_n^{n-1}e_s]\); observability uses its transpose. Reversing the system-matrix sign does not affect rank. The exceptional edge weight must be strictly positive. The special totient count concerns the *fixed* conductance \(w=1/2\), not an average over random weights. The letter \(j\) always denotes distance in the unit-edge path from the nearest endpoint of the exceptional closing edge, not cyclic distance from an arbitrary chosen origin.

## Proof

**1. Reflection spectrum and simplicity away from the uniform cycle.** Let \(R\) reflect vertex \(i\) to \(n-1-i\), and let \(b=e_0-e_{n-1}\). Then
\[
 L_n(w)=L(P_n)+wbb^{\mathsf T},\quad RL_n(w)=L_n(w)R,\quad Rb=-b.
\]
On the reflection-even space, the operator is independent of \(w\) and has the distinct path eigenpairs
\[
 \lambda_{2r}=2-2\cos(2\pi r/n),\qquad
 q_{2r}(i)=\cos\!\left(\frac{2\pi r(i+1/2)}n\right).
\]
The reflection-odd restriction is an irreducible real symmetric tridiagonal Jacobi matrix \(A_w=A_0+2wff^{\mathsf T}\), where \(f\) is its first unit coordinate. All its eigenvalues are simple. At \(w=1\), the Fourier modes of the uniform cycle show that each fixed reflection-even eigenvalue other than \(0\) is also a simple odd-block eigenvalue; \(0\) belongs to the even block alone, and if \(n\) is even, the unmatched odd top mode has eigenvalue \(4\).

For any fixed even eigenvalue \(\lambda_{2r}\), the polynomial \(\det(\lambda_{2r}I-A_w)\) is affine in \(w\). Its coefficient of \(w\) cannot vanish for an eigenvalue shared at \(w=1\): the corresponding irreducible Jacobi eigenvector has nonzero first coordinate, so the one-coordinate rank-one perturbation moves that eigenvalue strictly. Consequently each shared eigenvalue coincides across parity **only at \(w=1\)**. The even zero eigenvalue never occurs in the odd block for positive \(w\), since the connected positive-weight ring has a one-dimensional constant nullspace. Thus the full spectrum is simple for every \(w>0\) with \(w\ne1\). At \(w=1\), repeated cycle eigenvalues prevent controllability by a single coordinate. Hence for \(w\ne1\), by the symmetric PBH criterion, the system fails precisely when an eigenvector has zero component at vertex \(s\).

**2. Weight-independent reflection-even zeros.** A nonconstant even mode vanishes at reflected distance \(j\) precisely when
\[
 \cos\!\left(\frac{(2j+1)r\pi}{n}\right)=0
 \quad\Longleftrightarrow\quad
 (2j+1)r=\frac n2(2h+1)
\]
for some integer \(r\) with \(1\le r\le\lfloor(n-1)/2\rfloor\). For odd \(n\) the equality is impossible by parity. For even \(n=2m\) it has a solution with \(1\le r<m\) if and only if \(\gcd(2j+1,m)>1\): if the gcd is \(g>1\), use \(r=m/g\), and conversely coprimality would force \(m\mid r\). This proves exactly the permanent even-mode obstruction in condition 2. For odd \(n\), the central vertex \(j=(n-1)/2\) is fixed by reflection and every odd eigenvector vanishes there, so it is permanently blind.

**3. Weight-dependent odd zeros.** It remains to characterize an odd-parity eigenvector \(v\) with \(v_j=0\) away from the odd center. Write \(h=\lfloor n/2\rfloor\) and use the first \(h\) entries \(v_0,\ldots,v_{h-1}\) as independent coordinates. Their tridiagonal eigen-equations have endpoint row
\[
 (1+2w)v_0-v_1=\lambda v_0
\]
and interior recurrence \(-v_{i-1}+2v_i-v_{i+1}=\lambda v_i\). At the other end, reflection gives \(v_h=0\) for odd \(n\), and \(v_h=-v_{h-1}\) for even \(n\). Every eigenvector of this Jacobi system has \(v_0\ne0\), and if \(v_j=0\) for \(j\ge1\), its right tail is nonzero. The right-tail principal matrix (Dirichlet on the left) has spectrum strictly inside \((0,4)\), including the even-\(n\) terminal diagonal \(3\). Thus write \(\lambda=2-2\cos\theta\), \(0<\theta<\pi\).

The right-tail recurrence and \(v_j=0\) imply \(v_i=C\sin((i-j)\theta)\) for \(i\ge j\), with \(C\ne0\). The right boundary condition becomes \(\sin((h-j)\theta)=0\) for odd \(n\), or \(\sin((h-j)\theta)=-\sin((h-j-1)\theta)\) for even \(n\). In both cases the allowed angles are exactly
\[
 \theta_k=\frac{2\pi k}{n-2j-1},\qquad
 1\le k\le\left\lfloor\frac{n-2j-2}{2}\right\rfloor.
\]
The left recurrence at the zero \(v_j\) forces \(v_i=-C\sin((j-i)\theta_k)\) for \(0\le i\le j\). In particular \(v_0=-C\sin(j\theta_k)\ne0\), so \(\sin(j\theta_k)\ne0\). The endpoint equation gives
\[
 1+2w-\lambda
 =\frac{v_1}{v_0}
 =\frac{\sin((j-1)\theta_k)}{\sin(j\theta_k)},
\]
which reduces, by the sine addition identity, to
\[
 2w=1-\frac{\sin((j+1)\theta_k)}{\sin(j\theta_k)}.
\]
This proves necessity. Conversely, for every angle and positive weight in condition 3, the displayed left and right sine sequences meet with \(v_j=0\), satisfy the endpoint equation, and extend by antisymmetric reflection to a nonzero eigenvector of the full Laplacian. That proves sufficiency of the resonant list and hence the complete classification. At \(j=0\), the irreducible odd block has no first-coordinate zero, and the even path eigenvectors also have nonzero endpoint component, so the resonant condition is vacuous.

**4. Exact totient law and the unbounded loss.** Now assume \(n=2m+1\) and \(w=1/2\). The odd-parity Jacobi block is exactly the \(m\times m\) Dirichlet tridiagonal matrix with diagonal \(2\) and neighboring entries \(-1\), because its first diagonal becomes \(1+2w=2\). Its \(m\) eigenvectors can be taken as
\[
 v_j^{(k)}=\sin\!\left(\frac{(j+1)k\pi}{m+1}\right),
 \qquad k=1,\ldots,m,\quad j=0,\ldots,m-1.
\]
For any \(j<m\), precisely \(\gcd(m+1,j+1)-1\) of these \(m\) entries vanish: write \(m+1=ga\), \(j+1=gb\) with \(\gcd(a,b)=1\), and the vanishing indices are the \(g-1\) multiples of \(a\) below \(ga\). All reflection-even modes are nonzero at every vertex for odd \(n\), and the two parity spectra are disjoint because \(w\ne1\), so this zero count equals the exact Kalman rank deficiency. At the central vertex, all \(m\) odd eigenvectors vanish. Every noncentral reflected distance \(j\) corresponds to two distinct labelled vertices. Thus the working sites have \(\gcd(m+1,j+1)=1\), yielding \(2\varphi(m+1)\) sites. Taking \(m+1=2r\), \(j+1=r\) gives deficiency \(r-1\), completing the proof.

## Verification

The accompanying standalone standard-library `verify.py` independently constructs rational weighted Laplacians and exact fraction-arithmetic Kalman matrices, comparing full ranks with the finite resonance predicate. It checks every vertex for \(5\le n\le15\) at five rational edge weights \(1/2,1/3,3/4,2,1\), for **550 exact full-rank comparisons**. For odd sizes it additionally verifies the predicted gcd rank deficiencies at \(w=1/2\) and checks the totient census at 13 odd sizes through \(n=29\). Run `python3 verify.py`. A separate exploratory numerical PBH comparison covered 3,210 length, site, and resonant-weight instances through size \(27\), with no mismatches under the stated numerical tolerance. These finite checks are reproducibility aids; the preceding proof establishes the all-size and continuous-weight assertions.

## Relationship to prior work

The uniform-cycle result of Parlangeli and Notarstefano (2011) establishes why a single vertex never observes the undisturbed cycle. Previously established one-defect results determine the exact Kalman determinant at **an endpoint** of the exceptional edge, and the precise nonunit resonance list at **one vertex inward**; those two cases are incorporated here only as comparisons and are not claimed as new. In contrast, the classification here covers every vertex and every positive weight, including permanent even-path gcd obstructions and arbitrary-distance odd-mode resonances. The totient number of working sites and unbounded rank-deficiency family at \(w=1/2\) are the new arithmetic consequences.

Grudsky, Maximenko, and Soto-González (2022) analyze the spectrum of the same one-defect weighted cycle, with explicit eigenvector expressions in their Proposition 8. Those formulas provide a strong spectral starting point and could be used to derive conditions of the present kind. Their inspected paper does **not** state the complete site-versus-weight PBH classification, the totient placement count, or the unbounded arithmetic rank-loss law. The present proof derives those exact control-design statements from reflection and a local recurrence. This is a limited originality comparison, not a claim that eigenvector formulas themselves are new or that worldwide priority has been exhaustively established.

## Limitations

The theorem assumes just one exceptional edge in an otherwise unit-weight undirected cycle, an exact single-coordinate input or measurement, and real linear continuous-time dynamics. It gives exact algebraic controllability, not the conditioning of a finite-horizon Gramian or robustness to noise and model uncertainty. For weights in the resonant set, it identifies failure but generally does not specify the complete number of invisible odd modes except in the \(w=1/2\) specialization. The 2022 spectral paper's general eigenvector expressions and any unindexed equivalent control-theoretic consequence remain possible priority risks. Independent mathematical auditing has not been performed.

## References

1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1 (first public 2011-09-16), https://arxiv.org/abs/1109.3556 .
2. S. M. Grudsky, E. A. Maximenko and A. Soto-González, *Eigenvalues of the Laplacian Matrices of the Cycles with One Weighted Edge*, arXiv:2205.12457v1 (first public 2022-05-25), https://arxiv.org/abs/2205.12457 .
3. *Exact reachability-volume factorization for a cycle with one weighted edge*, public result record (2026-10-12), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-reachability-volume-factorization-for-a-cycle-with-one-wei--1ddd581661b4 .
4. *Exact single-sensor observability resonances of a singly weighted cycle*, public result record (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-single-sensor-observability-resonances-of-a-singly-weighte--4620d7539f8a .
