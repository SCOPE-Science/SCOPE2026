# Exact block-size noise amplification for simplex Kaczmarz

## Finding

Let \(d\ge2\), \(n=d+1\), and let \(a_1,\ldots,a_n\in\mathbb R^d\) be the vertices of a unit regular simplex centered at the origin, so that \(\langle a_i,a_j\rangle=-1/d\) for distinct indices. Let \(A\) be the matrix with rows \(a_i^{\mathsf T}\). For any fixed observed response \(b\in\mathbb R^n\), put \(x_\star=A^\dagger b\) and \(\delta=n^{-1}\sum_{i=1}^{n}b_i\). At every iteration choose, independently and uniformly, a subset \(S_t\subseteq\{1,\dots,n\}\) of exactly \(k\) rows, \(1\le k\le d\), and make the **unextended, exact block Kaczmarz** update

\[
x_{t+1}=x_t+A_{S_t}^\dagger(b_{S_t}-A_{S_t}x_t).
\]

For every deterministic initial point and integer \(t\ge0\), set \(\alpha_k=1-k/d\). Then the exact mean and mean-square error satisfy

\[
\mathbb E(x_t-x_\star)=\alpha_k^t(x_0-x_\star),\qquad
\mathbb E\|x_t-x_\star\|_2^2
=\alpha_k^t\|x_0-x_\star\|_2^2
+\frac{\delta^2d^2}{d-k+1}(1-\alpha_k^t).
\]

For \(x_0=x_\star\), the complete covariance matrix is isotropic at every time:

\[
\operatorname{Cov}(x_t)
=\frac{\delta^2d}{d-k+1}(1-\alpha_k^t)I_d.
\]

In particular, if \(\delta\ne0\), increasing the block size strictly improves the homogeneous squared-error contraction \(\alpha_k\) but strictly **increases** the asymptotic squared error \(\delta^2d^2/(d-k+1)\). Its ratio at \(k=d\) to that at \(k=1\) is exactly \(d\). When initialized at \(x_\star\), the mean-square error increases strictly with \(k\) for every \(t\ge1\), despite the faster homogeneous contraction.

## Assumptions and scope

All vector spaces, pseudoinverses, and expectations are over the real numbers and in exact arithmetic. The observations \(A,b\) are fixed throughout; the only iteration randomness is the independently sampled subset \(S_t\). Each subset is sampled *without replacement inside the block* but successive blocks are sampled independently. Every \(k\le d\) selected rows have full row rank. The response can be arbitrary, since all inconsistent residuals for this minimal-redundancy tight frame are constant vectors. The result is about the ordinary block projection, **not** the extended or double-block algorithms that correct inconsistent residuals.

The example belongs to a coefficient-and-response-perturbed setting as well: take the underlying noiseless system \(\gamma A x=0\) with \(\gamma>0\), \(\gamma\ne1\), and observe \(Ax=\delta\mathbf1\), \(\delta\ne0\). Both coefficient matrix and right-hand side change; nevertheless the least-squares solutions of the original and observed systems coincide at the origin.

## Proof

**1. Tight frame and residual decomposition.** The Gram matrix has diagonal entries \(1\), off-diagonal entries \(-1/d\), and eigenvalues \((d+1)/d\) with multiplicity \(d\) and \(0\) with multiplicity one. Consequently

\[
\sum_{i=1}^{n}a_i=0,\quad
A^{\mathsf T}A=\frac nd I_d,\quad
\ker A^{\mathsf T}=\operatorname{span}\{\mathbf1\}.
\]

The normal equations imply \(b-Ax_\star=\delta\mathbf1\), with \(\delta=n^{-1}\mathbf1^{\mathsf T}b\).

**2. Block geometry.** Fix a size-\(k\) subset \(S\). Its row Gram matrix is

\[
A_SA_S^{\mathsf T}=\left(1+\frac1d\right)I_k-\frac1d\mathbf1_k\mathbf1_k^{\mathsf T}.
\]

The eigenvalue in the all-ones direction is \((d-k+1)/d>0\). Put \(P_S=A_S^\dagger A_S\) and \(Q_S=I_d-P_S\). The shift caused by the inconsistent residual is

\[
z_S=\delta A_S^\dagger\mathbf1_k
=\frac{\delta d}{d-k+1}\sum_{i\in S}a_i,
\qquad
\|z_S\|_2^2=\frac{\delta^2kd}{d-k+1}.
\]

Here \(P_S\) is an orthogonal projector of rank \(k\), and \(Q_Sz_S=0\).

**3. Exact random-subset identities.** Uniform sampling of all size-\(k\) subsets is invariant under permutations of the simplex vertices. Every permutation is implemented by an orthogonal operator on \(\mathbb R^d\). An operator commuting with all these permutations is scalar (equivalently, lift it to the coordinate hyperplane \(\mathbf1^\perp\subset\mathbb R^n\): a permutation-invariant matrix has constant diagonal and constant off-diagonal entries). The trace identity \(\operatorname{tr}P_S=k\) therefore gives

\[
\mathbb E_S P_S=\frac{k}{d}I_d,\qquad
\mathbb E_S z_S=0,\qquad
\mathbb E_S z_Sz_S^{\mathsf T}=\frac{\delta^2 k}{d-k+1}I_d.
\]

The last relation follows from permutation invariance and its trace \(\mathbb E\|z_S\|_2^2=\delta^2kd/(d-k+1)\).

**4. Recurrences and solution.** With \(e_t=x_t-x_\star\), every update is \(e_{t+1}=Q_{S_t}e_t+z_{S_t}\). Because \(Q_Sz_S=0\), the two terms are perpendicular for each realized subset, not just on average. Fresh subset independence and the identities above give

\[
\mathbb E[e_{t+1}\mid e_t]=\alpha_k e_t,\quad
\mathbb E[\|e_{t+1}\|_2^2\mid e_t]
=\alpha_k\|e_t\|_2^2+\frac{\delta^2kd}{d-k+1}.
\]

Induction and summation of the finite geometric series yield the displayed mean and mean-square formulas, including \(k=d\), when \(\alpha_k=0\). If \(e_0=0\), all subsequent means vanish. The covariance recursion is scalar by the third identity: if \(\operatorname{Cov}(e_t)=c_tI_d\), then \(c_{t+1}=\alpha_kc_t+\delta^2 k/(d-k+1)\). Its solution proves the covariance formula.

**5. Strict tradeoff.** For fixed \(d\) and nonzero \(\delta\), the floor \(\delta^2d^2/(d-k+1)\) increases strictly with integer \(k\), whereas \(\alpha_k\) decreases strictly. With \(e_0=0\), both the floor and the positive factor \(1-\alpha_k^t\) are strictly increasing with \(k\) for every positive integer \(t\). At the endpoints, the floors are \(\delta^2d\) and \(\delta^2d^2\), respectively. This proves the stated dimension-factor amplification.

## Verification

The independent subset identities were also verified by exact rational matrix arithmetic for all \(2\le d\le7\) and \(1\le k\le d\), enumerating every possible subset. The script `verify_simplex.py` checks each projector, the averaged projector, the averaged shift outer product, and the transient recurrence. Run `python verify_simplex.py` with Python 3 and SymPy installed. These finite checks are diagnostics, not a proof for arbitrary dimension; the proof above supplies the infinite-dimensional-parameter argument for all finite \(d\).

For \(d=3\), the exact asymptotic squared-error floors at \(k=1,2,3\), after dividing by \(\delta^2\), are respectively \(3,9/2,9\). The noiseless squared-error contraction factors are \(2/3,1/3,0\), respectively.

## Relationship to prior work

Gan and Wu (2026) establish general convergence-neighborhood bounds for randomized and block Kaczmarz on perturbed systems, and their Section 5 treats sketch-and-project in a general metric. Their proof (particularly its orthogonal projection identity and bound (34)) is the closest general framework. The present statement makes a different, finite-time equality assertion: the *entire* second-moment and covariance profile, for every subset size and every fixed data vector, as well as the strict and dimension-unbounded reversal of the block-size/error-floor ordering. General upper bounds alone do not give these equalities; special simplex symmetry and the exact affine correction are essential.

Needell and Tropp (2012) study randomized block Kaczmarz from a fixed row paving and derive general convergence horizons. Needell, Zhao and Zouzias (2014) study block projection combined with residual correction for inconsistent least squares. Neither of these methods' general statements specifies the all-subsets regular-simplex covariance identity. The elementary spectral and symmetry identities used here are standard and are not claimed as new individually.

## Limitations

This is an exact result for a regular simplex and uniform *fresh subset* sampling. It does not prove that all large blocks worsen noisy Kaczmarz, nor compare arithmetic costs per iteration. A fixed block partition, nonuniform probabilities, extended residual correction, general frames, time-varying measurement noise, and floating-point errors are outside its scope. The usual generic sketch-and-project error bounds already predict a nonzero horizon; this result identifies their exact saturation and an explicit block-size dependence for one highly symmetric family. Historical priority for an equivalent unindexed equality case remains open to external verification; no independent audit has been performed.

## References

- Y. Gan and G. Wu, *On Convergence Behavior of Randomized Kaczmarz-type Methods for Solving Doubly Noisy Linear Systems*, arXiv:2608.22259 (first public version, August 23, 2026), https://arxiv.org/abs/2608.22259.
- D. Needell and J. A. Tropp, *Paved with Good Intentions: Analysis of a Randomized Block Kaczmarz Method*, arXiv:1208.3805 (2012), https://arxiv.org/abs/1208.3805.
- D. Needell, R. Zhao and A. Zouzias, *Randomized Block Kaczmarz Method with Projection for Solving Least Squares*, arXiv:1403.4192 (2014), https://arxiv.org/abs/1403.4192.
