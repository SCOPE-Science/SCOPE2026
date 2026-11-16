# Three rank shells are optimal for exact first-coordinate Fourier sampling of finite matrices

## Finding
Fix a prime power \(q\ge2\), an integer \(n\ge2\), and \(N=q^n\). There exists a probability measure on \(n\times n\) matrices over \(\mathbb F_q\) which is uniform on each matrix-rank stratum, is supported on **exactly three distinct ranks** \(n,n-1,n-2\), and makes the constant and every one-coordinate additive character an orthonormal system. No measure invariant under left and right invertible matrix multiplication, supported on fewer than three ranks, has this property.

Precisely, let \(\psi\) be a fixed nontrivial additive character of \(\mathbb F_q\), and set
\[
\mathcal B=\{1\}\cup\{M\mapsto\psi(aM_{ij}):1\le i,j\le n,\;a\in\mathbb F_q^\times\}.
\]
For \(t=0,1,2\) set \(b_*=q+1-q/N\), \(\mu_*=2-1/N\), and define
\[
\begin{aligned}
w_2&=\frac{(\mu_*-1)(b_*-q)}{(q^2-1)(q^2-q)},\\
w_1&=\frac{(\mu_*-1)(q^2-b_*)}{(q-1)(q^2-q)},\\
w_0&=1-w_1-w_2.
\end{aligned}
\]
These are strictly positive and add to one. To sample, first choose \(t\) with probability \(w_t\), then sample uniformly among matrices of rank \(n-t\). The Gram matrix of \(\mathcal B\) under this sampling law is **exactly the identity**. Moreover, these are the unique weights with this property on the specified three ranks, and any bi-invariant exact-orthonormal sampling law uses at least three distinct ranks.

## Assumptions and scope
A bi-invariant measure means \(\mu(gMh)=\mu(M)\) for all invertible \(g,h\), which is equivalent to constancy on each rank orbit. All scalar weights are positive probabilities, not signed cubature. The norm and inner product are probability-normalized: \(\langle f,g\rangle=\mathbb E_\mu[f(M)\overline{g(M)}]\). Rank and matrix multiplication are over \(\mathbb F_q\). This is a statement about the \(1+n^2(q-1)\) distinct functions in \(\mathcal B\), **not** an orthonormal basis of every function on the matrix space.

## Proof
**1. Fourier criterion.** Associate to each character its frequency matrix: the constant has frequency zero, while \(\psi(aM_{ij})\) has frequency \(aE_{ij}\). Differences of two distinct frequencies have rank one (when they share a row or column) or rank two (when they use distinct rows and columns). Left-right invariance makes the Fourier transform of \(\mu\) depend only on frequency rank. Hence \(\mathcal B\) is orthonormal if and only if the rank-one and rank-two Fourier multipliers both vanish.

**2. Convert to kernel moments.** Write \(T=n-\operatorname{rank}(M)\) and \(Z=q^T\), so that \(Z=|\ker M|\). Under bi-invariance, for a fixed nonzero vector \(v\), and a fixed independent pair \(v,w\), the inclusion probabilities are
\[
 p_1=\mathbb P(Mv=0)=\frac{\mathbb EZ-1}{N-1},\qquad
 p_0=\mathbb P(Mv=Mw=0)=\frac{\mathbb E[(Z-1)(Z-q)]}{(N-1)(N-q)}.
\]
The formulas count, respectively, nonzero vectors and ordered independent vector pairs inside a uniform random kernel of dimension \(T\). The first Fourier multiplier is \((Np_1-1)/(N-1)\), so it vanishes exactly when \(p_1=N^{-1}\).

By simultaneous left-right invariance, the pair \((Mv,Mw)\) is uniform within each of its three rank classes. Their masses are \(p_0\), \((q+1)(p_1-p_0)\), and \(1-p_0-(q+1)(p_1-p_0)\), respectively. Evaluating the rank-two character \(\psi((Mv)_1+(Mw)_2)\) on each class gives the averages \(1\), \(-1/(N-1)\), and \(q/((N-1)(N-q))\). The latter count follows by subtracting the zero and dependent ordered pairs from the full character sum. When \(p_1=N^{-1}\), the resulting Fourier multiplier is
\[
 \frac{N^2p_0-1}{(N-1)(N-q)},
\]
which vanishes exactly when \(p_0=N^{-2}\). Thus the Fourier criterion is equivalent to
\[
 \mathbb EZ=2-N^{-1},\qquad
 \mathbb EZ^2=q+3-2(q+1)N^{-1}+qN^{-2}.
\]
Its variance is \(\operatorname{Var}(Z)=(q-1)(1-N^{-1})^2>0\).

**3. Why two ranks never suffice.** The required mean \(\mu_*=2-N^{-1}\) lies strictly between \(1\) and \(q\), and the support values of \(Z\) are among \(1,q,q^2,\ldots,q^n\). Therefore any distribution on at most two such values satisfying the mean must use \(1\) and one \(b=q^t\), \(t\ge1\). The variance of a two-point law with support \(\{1,b\}\) and mean \(\mu_*\) is \((\mu_*-1)(b-\mu_*)\). Matching the required variance forces
\[
 b=\mu_*+\frac{\operatorname{Var}(Z)}{\mu_*-1}=q+1-q/N.
\]
But \(q<b<q^2\) for every \(n,q\ge2\), and this is not any power of \(q\). Contradiction. A single rank is already excluded by positive variance.

**4. Attainment by exactly three ranks.** On the values \(Z\in\{1,q,q^2\}\), the unique solution to the probability, mean and second-moment equations is precisely \((w_0,w_1,w_2)\) given above. Since \(q<b_*<q^2\), both \(w_1,w_2\) are strictly positive. Because \(\mathbb EZ<q\), the other weights satisfy \(w_0>0\): indeed \(\mathbb EZ\ge w_0+(1-w_0)q\) implies \(w_0\ge(q-\mu_*)/(q-1)>0\). Direct substitution verifies both moments, completing orthonormality. Uniqueness on the three stated rank shells is Vandermonde uniqueness.

## Verification
The standalone Python script `check_rank_shell.py` checks the symbolic weight and moment identities in exact algebra and exhaustively counts all matrices over the **prime** fields of orders \(2,3,5\) in the six configurations \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\). For each case, two frequency-rank representatives have uniform additive-character residues under the three-shell mixture. The analytical proof, rather than these finite calculations, establishes all prime-power cases and all \(n\ge2\).

## Relationship to prior work
Kawamura's 2020 rank-orbit Fourier transform gives the general invariant-transform framework and affine \(q\)-Krawtchouk coefficients. The present proof needs only its lowest two Fourier-rank sectors and supplies the separate positive three-shell construction and matching rank-shell impossibility. Yang and Honold's 2010 framework of \(k\)-good matrices supplies the broader interpretation in terms of uniformly distributed linear images, and studies minimum *point-support size*, not minimum number of rank orbits. The matrix- and Hamming-sampling results cited below study single-orbit conditioning or different Hamming-shell designs, rather than exact, minimal **rank-orbit** orthonormality. These differences are claim comparisons, not guarantees of publication priority.

## Limitations
The minimum three ranks is proved only under left-right invariance. Non-invariant constructions can have smaller numbers of occupied rank levels or much fewer individual matrices; this theorem does not claim point-support optimality. For a fixed triple of ranks other than \(n,n-1,n-2\), existence and positivity of matching weights are not classified. Independent verification and an exhaustive historical-priority audit have not been performed; an equivalent construction hidden in earlier rank-design literature remains possible.

## References
1. Koei Kawamura, *\(q\)-Hypergeometric polynomials and group-invariant Fourier transformations over a finite field*, arXiv:2008.13408, first version 2020-08-31; Section 4.2, Proposition 4.2.1 and surrounding orbit-Fourier discussion.
2. Shengtian Yang and Thomas Honold, *Good Random Matrices over Finite Fields*, arXiv:1008.3408, first version 2010-08-19; Section 3 (\(k\)-good matrices), Section 4 (homogeneous-weight distributions).
3. Eimear Byrne, Michela Ceria, Sorina Ionica and Relinde Jurrius, *Weighted Subspace Designs from \(q\)-Polymatroids*, Journal of Combinatorial Theory, Series A, 201 (2024), article 105799, DOI:10.1016/j.jcta.2023.105799; Section 6 (weighted subspace designs).
