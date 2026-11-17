# Exact cost-driven edge deletion and Fiedler multiplicity on a four-cycle

## Finding

For the four-cycle with vertices \(0,1,2,3\) and nonnegative conductances \(a=w_{01}\), \(b_1=w_{12}\), \(c=w_{23}\), and \(b_2=w_{30}\), assign the edge \(01\) price \(d^2\), and each other edge price \(1\). For every \(d>0\) and budget \(B>0\), maximize the second-smallest eigenvalue \(\lambda_2(L_w)\) of the weighted combinatorial Laplacian under \(d^2a+b_1+c+b_2\le B\). Put \(D=d^2+2d+5\). The **exact optimum** is

\[
\max\lambda_2(L_w)=
\begin{cases}
4B/D,&0<d\le3,\\
B/5,&d\ge3.
\end{cases}
\]

The two expressions agree at \(d=3\). All maximizing allocations, with no symmetry assumption imposed, are as follows.

* For \(0<d<3\), the optimizer is unique:
  \[
  (a,b_1,c,b_2)=\frac{B}{D}\left(\frac{d+1}{d},\,2,\,d+1,\,2\right).
  \]
  The optimal Fiedler eigenvalue has multiplicity exactly two.
* For \(d=3\), the complete set of optimizers is the closed segment
  \[
  (a,b_1,c,b_2)=\left(t,\,\frac{3B}{10}-3t,\,\frac{2B}{5}-3t,\,\frac{3B}{10}-3t\right),
  \quad 0\le t\le\frac{B}{15}.
  \]
  The Fiedler multiplicity is one for \(0\le t<B/15\), and two at \(t=B/15\).
* For \(d>3\), the optimizer is unique:
  \[
  (a,b_1,c,b_2)=\left(0,\frac{3B}{10},\frac{2B}{5},\frac{3B}{10}\right),
  \]
  and the Fiedler eigenvalue is simple.

Consequently an edge whose price exceeds nine times its companions' prices is **deleted at every optimum**. Exactly at the ninefold threshold, a nontrivial continuum of optimal designs emerges, from a path to a positive-edge cycle. Below the threshold, all four edges are used and the Fiedler eigenvalue is double.

## Assumptions and scope

The topology is the simple undirected cycle \(C_4\), with symmetric nonnegative edge conductances and the ordinary (unnormalized) Laplacian. The sole asymmetric *price* is \(d^2\) on edge \(01\); the other three prices are \(1\). The optimization is over all four conductances independently and permits zero conductance, so disconnection is feasible but never optimal. No stationarity constraint beyond Laplacian symmetry and no upper bound on individual conductances is imposed. The budget \(B\) and length parameter \(d\) are strictly positive. The theorem does not optimize discrete-time second-largest-eigenvalue modulus or rates on cycles of other orders.

## Proof

For any \(z\in\mathbb R^4\) with \(\sum_i z_i=0\), the Rayleigh principle gives
\[
\lambda_2(L_w)\le \frac{z^\mathsf{T}L_wz}{z^\mathsf{T}z}
=\frac{a(z_0-z_1)^2+b_1(z_1-z_2)^2+c(z_2-z_3)^2+b_2(z_3-z_0)^2}{\sum_i z_i^2}.
\]
An optimizer exhausts the budget because \(\lambda_2\) is positively homogeneous in the conductances and a positive objective is attainable.

**The regime \(0<d\le3\).** Take the mean-zero, orthogonal vectors
\[
v=(1,1,-1,-1)^\mathsf{T},\qquad
u=(d,-d,-1,1)^\mathsf{T},\qquad
\tau=\frac{2(d^2+1)}{D}.
\]
They have squared norms \(4\) and \(2(d^2+1)\), respectively. Since \(0<\tau\le1\) exactly when \(0<d\le3\), the convex combination of their Rayleigh quotients is a valid universal upper bound on \(\lambda_2\). For **every** allocation, including nonsymmetric ones, direct edge-difference substitution gives the exact identity
\[
(1-\tau)\frac{v^\mathsf{T}L_wv}{4}+
\tau\frac{u^\mathsf{T}L_wu}{2(d^2+1)}
=\frac{4}{D}(d^2a+b_1+c+b_2)\le\frac{4B}{D}.
\]
For \(0<d<3\), assign
\[
a=\frac{B(d+1)}{dD},\quad b_1=b_2=b=\frac{2B}{D},\quad c=\frac{B(d+1)}{D}.
\]
The cost is exactly \(B\). Reflection \((0,1,2,3)\mapsto(1,0,3,2)\) splits the Laplacian into a constant/symmetric mode, with nonzero eigenvalue \(2b\), and the antisymmetric matrix
\[
M=\begin{pmatrix}2a+b&b\\ b&2c+b\end{pmatrix}.
\]
Because \(2ac=b(a+c)\), one eigenvalue of \(M\) is \(2b\); the other is \(2(a+c)\), which is strictly larger. Thus the full spectrum is
\[
\left\{0,\frac{4B}{D},\frac{4B}{D},\frac{2B(d+1)^2}{dD}\right\},
\]
attaining the bound with Fiedler multiplicity two.

For uniqueness when \(0<d<3\), both coefficients in the universal Rayleigh combination are strictly positive. If an allocation attains its upper bound, *each* of \(v\) and \(u\) must individually attain the minimum Rayleigh quotient; hence both are eigenvectors with eigenvalue \(\lambda=4B/D\). The equation \(L_wv=\lambda v\) forces \(b_1=b_2=\lambda/2\). The equations at vertices \(0\) and \(2\) in \(L_wu=\lambda u\) then force \(a=\lambda(d+1)/(4d)\) and \(c=\lambda(d+1)/4\). These are exactly the displayed unique weights, with no possibility of a nonsymmetric maximizer.

**The regime \(d\ge3\).** The mean-zero vector \(x=(-3,3,1,-1)^\mathsf{T}\), with squared norm \(20\), yields
\[
\lambda_2(L_w)\le\frac{x^\mathsf{T}L_wx}{20}
=\frac{9a+b_1+c+b_2}{5}\le\frac{B}{5},
\]
since \(d^2\ge9\). The path allocation \(a=0\), \(b_1=b_2=3B/10\), \(c=2B/5\) has Laplacian spectrum
\[
\left\{0,\frac{B}{5},\frac{3B}{5},\frac{6B}{5}\right\},
\]
so the bound is attained. When \(d>3\), equality forces \(a=0\); it also forces \(x\) to be a Fiedler eigenvector. Solving \(L_wx=(B/5)x\) gives \(b_1=b_2=3B/10\) and \(c=2B/5\), proving uniqueness and simplicity.

At the boundary \(d=3\), every optimizer must satisfy \(L_wx=(B/5)x\). Its four vertex equations yield
\[
b_1=b_2=\frac{3B}{10}-3a,\qquad c=\frac{2B}{5}-3a.
\]
Nonnegativity and budget equality hold over a preliminary interval of \(a\). For any such weights, the reflection-symmetric mode has eigenvalue \(2b_1=3B/5-6a\), while the two antisymmetric modes have eigenvalues \(B/5\) and \(6B/5-10a\). Thus \(B/5\) is the second-smallest eigenvalue **if and only if** \(0\le a\le B/15\). The symmetric eigenvalue meets it only at \(a=B/15\), proving the entire claimed critical segment and the multiplicity statement.

## Verification

The self-contained program `verify.py` uses exact rational arithmetic and symbolic eigenvalue calculations. Its replay passed 12 symbolic identities, 27 rational parameter/budget spectra, four critical-segment configurations, and 1,440 exact Rayleigh-certificate checks on independently sampled feasible four-edge weights. The code directly builds the full four-by-four Laplacian rather than relying solely on the reflected two-by-two formulas. These finite checks are supplemental; the preceding parameter-uniform proof establishes the infinite quantifiers and all boundaries.

To replay with Python 3 and SymPy installed, execute `python3 verify.py` in the directory containing this document and the program. The output is a `PASS` line containing the four check counts. No external data files or third-party papers are needed.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis (2006) formulate the continuous-time fastest-mixing Markov-process problem as weighted Laplacian spectral-gap maximization with arbitrary positive edge prices. Their section 5.2 solves the priced path, while section 5.3 presents uniform-cost cycles and proves a two-dimensional embedding bound for general priced cycles. The present result is an explicit full phase classification for the smallest nontriangular cycle with one exceptional edge price, including all optimizer allocations and the singular critical segment. It does not claim novelty of semidefinite duality, the path solution, or the uniform-cost cycle.

Boyd, Diaconis, Parrilo and Xiao (2009) analyze *discrete-time* fastest-mixing chains with graph symmetries, including homogeneous cycles, under a different eigenvalue objective. Gerencsér, Hendrickx and Van Dooren (2015) study the discrete-time cycle spectral-gap objective and homogeneous reversible optimality under perturbations. These results do not state the continuous-time price-dependent four-cycle allocation law above.

## Limitations

This is an exact result for four vertices and a single exceptional edge price, not a general formula for cycles of arbitrary length or arbitrary edge prices. The critical optimizer family is established for nonnegative conductances; requiring every edge conductance to be strictly positive changes the meaning of edge deletion but not the supremum. No claim is made about nonreversible chains or finite-step spectral-radius mixing. Searches and primary-text comparisons do not prove absolute novelty; other specialist treatments or equivalent consequences may exist. No independent external audit has been performed.

## References

1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699, DOI: 10.1137/S0036144504443821. Full lawful author-hosted text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published online 2006-11-02).
2. S. Boyd, P. Diaconis, P. Parrilo and L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM Journal on Optimization 20 (2009), 792–819, DOI: 10.1137/070689413. Full author-hosted text: https://stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. B. Gerencsér, J. Hendrickx and P. Van Dooren, *Spectral Gap of Markov Chains on a Cycle*, European Control Conference (2015), 765–769, DOI: 10.1109/ECC.2015.7330635. Deposited full text: https://real.mtak.hu/173919/1/cycle_spectral_gap.pdf.
