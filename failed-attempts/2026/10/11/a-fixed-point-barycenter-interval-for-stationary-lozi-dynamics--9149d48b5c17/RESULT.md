# A fixed-point barycenter interval for stationary Lozi dynamics
## Finding
Consider the classical Lozi map
\[
\mathcal L_{a,b}(x,y)=(1+y-a|x|,\,bx)
\]
with \(a>0\), \(0<b<1\), and \(1-a<b<a+1\). Let \(\mu\) be any compactly supported invariant Borel probability measure, let \(X(x,y)=x\), and write
\[
X_+=\max(X,0),\qquad X_-=\max(-X,0),\qquad m=\int X\,d\mu.
\]
Define
\[
A=a+1-b,\qquad B=a+b-1,
\]
so \(A,B>0\). Then the positive and negative first moments satisfy the exact stationary budget
\[
A\int X_+\,d\mu+B\int X_-\,d\mu=1.
\]
The two Lozi fixed points have first coordinates
\[
x_+=\frac1A,\qquad x_-=-\frac1B.
\]
Their distances from the invariant barycenter are exactly
\[
x_+-m=\frac{2a}{A}\int X_-\,d\mu,
\qquad
m-x_-=\frac{2a}{B}\int X_+\,d\mu.
\]
Consequently
\[
x_-\le m\le x_+.
\]
Equality at either endpoint holds if and only if \(\mu\) is the Dirac mass at the corresponding fixed point. Hence every non-Dirac compact invariant probability measure has
\[
x_-<m<x_+
\]
and assigns positive mass to both half-planes \(x<0\) and \(x>0\).

## Assumptions and scope
The map convention is the original two-coordinate form \(\mathcal L_{a,b}(x,y)=(1+y-a|x|,\,bx)\). The parameter restrictions \(a>0\), \(0<b<1\), and \(1-a<b<a+1\) are the standard dissipative regime in which the two fixed points lie in the first and third quadrants. The result applies to every compactly supported invariant Borel probability measure, including periodic-orbit measures and invariant measures supported on chaotic attractors. It does not assume ergodicity or existence of a physical measure.

## Proof
Invariance of \(\mu\) under the second coordinate gives
\[
\int Y\,d\mu=b\int X\,d\mu=bm.
\]
Invariance under the first coordinate therefore gives
\[
m=1-a\int |X|\,d\mu+bm,
\]
so
\[
1=a\int |X|\,d\mu+(1-b)m.
\]
Using \(m=\int X_+\,d\mu-\int X_-\,d\mu\) and \(\int |X|\,d\mu=\int X_+\,d\mu+\int X_-\,d\mu\), this becomes
\[
1=A\int X_+\,d\mu+B\int X_-\,d\mu.
\]
Since \(A+B=2a\), straightforward elimination yields
\[
\frac1A-m=\frac{2a}{A}\int X_-\,d\mu,
\qquad
m+\frac1B=\frac{2a}{B}\int X_+\,d\mu.
\]
Both right-hand sides are nonnegative, proving the interval bound.

Suppose \(m=x_+\). Then \(\int X_-\,d\mu=0\), so \(X\ge0\) almost surely. Invariance of the second coordinate and \(b>0\) gives \(Y\ge0\) almost surely. Thus the support of \(\mu\) lies in the closed first quadrant, where the map is affine. After translating the positive fixed point to the origin, the dynamics on that branch is the invertible linear map with matrix
\[
M_+=\begin{pmatrix}-a&1\\ b&0\end{pmatrix}.
\]
Its eigenvalues are real with opposite signs, and neither has modulus one because \(A>0\) excludes eigenvalue \(-1\) and \(B>0\) excludes eigenvalue \(1\). A compact set invariant under an invertible hyperbolic linear map can contain only the origin: every nonzero vector has either a forward or backward iterate of unbounded norm. Therefore the support is the positive fixed point alone. The argument for \(m=x_-\) is identical on the negative branch, with matrix
\[
M_-=\begin{pmatrix}a&1\\ b&0\end{pmatrix}.
\]
The converse equality statements are immediate for the two fixed-point Dirac measures.

## Verification
The algebraic identities were replayed from the packaged script `verify_lozi.py`; its output is stored in `verification_output.txt` and is `LOZI_IDENTITY_OK`. The proof of endpoint rigidity is independent of symbolic computation and uses only compact support, invariance, branch affinity, and hyperbolicity of the two branch matrices under the stated inequalities.

## Relationship to prior work
Lozi's 1978 paper introduced the piecewise-linear Hénon-type map. A 2023 survey by Lozi restates the map, the dissipative condition, and the two fixed points, and summarizes extensive work on attractors, bifurcations, symbolic dynamics, entropy, synchronization, and applications. A 2001 Hénon-Lozi comparison studies fixed points and global bifurcation, while a 1999 geometric study of Lozi strange attractors is classified under MSC \(37D45\). Searches for invariant-measure barycenters, time averages, first moments, and absolute-value moment identities found no source stating or implying the exact sign-weighted budget or the sharp barycenter interval with endpoint rigidity.

## Limitations
The result constrains first moments only; it does not identify a physical measure, compute an SRB density, determine entropy, or classify the full attractor. The foundational 1978 article was bibliographically verified and its abstract was available, but its full text could not be inspected in the available sources. The map equation and fixed-point formulas were independently checked in later same-map sources. Literature search cannot establish absolute novelty, so an unindexed or inaccessible prior statement remains a residual risk.

## References
1. R. Lozi, “Un attracteur étrange (?) du type attracteur de Hénon,” *J. Phys. Colloques* 39 (C5), C5-9–C5-10 (August 1978), DOI: 10.1051/jphyscol:1978505.
2. R. Lozi, “Survey of Recent Applications of the Chaotic Lozi Map,” *Algorithms* 16 (2023), 491, DOI: 10.3390/a16100491.
3. M. A. Aziz-Alaoui, C. Robert, and C. Grebogi, “Dynamics of a Hénon–Lozi-type map,” *Chaos, Solitons & Fractals* 12 (2001), 2323–2341, DOI: 10.1016/S0960-0779(00)00192-2.
4. Y. Cao and Z. Liu, “The geometric structure of strange attractors in the Lozi map,” *Communications in Nonlinear Science and Numerical Simulation* 4 (1999), 102–108, DOI: 10.1016/S1007-5704(98)90076-4.
