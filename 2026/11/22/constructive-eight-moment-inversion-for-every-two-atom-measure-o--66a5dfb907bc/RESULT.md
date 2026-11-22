# Constructive eight-moment inversion for every two-atom measure on the two-torus

## Finding

Let \(\mathbb T=\mathbb R/\mathbb Z\), and let \(\mathcal M_2\) be the complex measures on \(\mathbb T^2\) supported on at most two **distinct** points, with each displayed atom having a nonzero complex coefficient. The zero measure is included. Set
\[
\Omega=\{(0,0),(1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1)\}.
\]
There is an explicit, finite, exact-arithmetic reconstruction and feasibility algorithm recovering the unique member of \(\mathcal M_2\) from its eight Fourier coefficients \(\widehat\mu(k,\ell)\), \((k,\ell)\in\Omega\). It uses at most two quadratic equations, linear equations of dimension at most two, at most two pairings, and eight exact residual comparisons. It is valid without a generic-position assumption and handles both coincident coordinate projections and complete cancellation of an axial marginal.

The single mixed sample \(\widehat\mu(1,1)\) is structurally necessary relative to the seven specified axial samples: in fact, **no number** of purely axial Fourier samples distinguishes all two-atom measures, whereas adding this one mixed sample does. This is a necessity statement for axis-only designs, **not** a claim that eight is globally the fewest arbitrary Fourier coefficients.

## Assumptions and scope

Use the convention \(\widehat\mu(k,\ell)=\int_{\mathbb T^2}\exp[-2\pi i(kx+\ell y)]\,d\mu(x,y)\). Write \(z_j=e^{-2\pi i x_j}\), \(w_j=e^{-2\pi i y_j}\), so \(|z_j|=|w_j|=1\) and the prescribed moments are \(\sum_{j=1}^r c_jz_j^kw_j^\ell\) for \(0\le r\le2\). For \(r=2\), \((z_1,w_1)\ne(z_2,w_2)\), and \(c_1c_2\ne0\). All statements concern exact complex arithmetic; no numerical stability, noisy data guarantee, or general higher-sparsity inverse algorithm is claimed.

## Proof

**One-coordinate algebra.** Given four moments \(s_k=\sum_{j=1}^r c_j u_j^k\) for \(0\le k\le3\), combine atoms with the same \(u_j\). If two distinct projected nodes remain, then
\[
\Delta=s_0s_2-s_1^2=c_1c_2(u_1-u_2)^2\ne0.
\]
Thus the two elementary symmetric functions are determined by
\[
T=\frac{s_0s_3-s_1s_2}{\Delta},\qquad P=\frac{s_1s_3-s_2^2}{\Delta}.
\]
The two distinct roots of \(U^2-TU+P=0\) are exactly the projected nodes. Their coefficients follow uniquely from \(c_1+c_2=s_0\), \(c_1u_1+c_2u_2=s_1\). If \(\Delta=0\) for a marginal of a measure in \(\mathcal M_2\), the marginal has only one effective node or is zero: the former has \(s_0\ne0\) and node \(s_1/s_0\); the latter has all four moments zero. In particular, two distinct projected nodes cannot mimic one node even if the total mass is zero. All three types are therefore recognized exactly.

**Case table.** Apply this procedure to \(X_k=\widehat\mu(k,0)\), \(Y_k=\widehat\mu(0,k)\), \(0\le k\le3\), and put \(H=\widehat\mu(1,1)\). The two lists of recovered projected nodes and weights have lengths in \(\{0,1,2\}\):

1. For lengths \((2,2)\), the weights on both axes are the same unordered pair. Try the at most two coordinate pairings respecting these weights. If the weights are unequal, this forces a unique matching. If they coincide with common nonzero value \(c\), the two candidate values of \(H\) differ by \(c(z_1-z_2)(w_1-w_2)\ne0\); hence \(H\) chooses exactly one matching.
2. For lengths \((2,1)\), the only possible second coordinate is the unique recovered \(w\). Attach it to both recovered first-coordinate nodes; similarly for \((1,2)\).
3. For lengths \((2,0)\), the two weights are opposite and both second coordinates coincide, say at \(w\), since cancellation of two nonzero atoms at distinct projected nodes is impossible. As \(X_1=c_1(z_1-z_2)\ne0\), necessarily \(H=wX_1\), so \(w=H/X_1\). The \((0,2)\) case is symmetric, giving \(z=H/Y_1\).
4. For lengths \((1,1)\), the measure has one atom. For \((0,0)\), it is zero. Every other type is incompatible with the model.

Here each type refers to the number of *nonzero effective nodes* in the recovered marginal. Candidate weights and nodes are finally checked for nonzero coefficients, distinct support, unit-modulus coordinates and agreement with **all eight** input moments. Thus the algorithm not only reconstructs every model measure but gives an exact membership test for arbitrary eight-tuples. Every step is a finite arithmetic operation, a quadratic root extraction, or an equality test. The construction in each case is forced; this proves uniqueness, without relying on the already published abstract sufficiency theorem.

**Indispensability of mixing.** For \(z_1\ne z_2\), \(w_1\ne w_2\) on the unit circle and \(c\ne0\), the two measures \(c\delta_{(z_1,w_1)}+c\delta_{(z_2,w_2)}\) and \(c\delta_{(z_1,w_2)}+c\delta_{(z_2,w_1)}\), interpreted via their torus coordinates, have identical axial Fourier coefficients at every integer frequency. Their mixed coefficient at \((1,1)\) differs by \(c(z_1-z_2)(w_1-w_2)\ne0\). This proves exactly the stated axis-only impossibility and one-mixed-sample sufficiency.

## Verification

The accompanying `check_eight_moments.py` numerically reconstructs and compares all eight moments and recovered support/weights for 700 deterministic random examples in seven regimes, including merged and fully cancelled marginals; it also checks 5,355 combinations of two distinct nodes on a \(7\times5\) root-of-unity grid with three complex coefficient choices and checks the empty measure. These are numerical stress checks, **not** a proof of algebraic equalities or universal uniqueness. The proof above is self-contained; the checker uses only the Python standard library.

Reproduce: `python3 check_eight_moments.py` from the same directory as this file. A successful run prints a `PASS` count for 700 random and 5,355 root-grid instances.

## Relationship to prior work

Diederichs, Kolountzakis and Papageorgiou (arXiv:2107.10348, first public 21 July 2021) prove in Theorem 9 and Corollary 10 that the hyperbolic cross \(\Gamma_{2N}^d\) identifies all at-most-\(N\)-atomic complex measures; our eight indices are precisely \(\Gamma_4^2\), so **identifiability at these indices is already known**. They explicitly state after Corollary 10 that their proof is not a reconstruction algorithm and give a finite algorithm in Theorem 11 for the larger \(\widetilde\Gamma_N^d\) (12 indices when \(N=d=2\)). The contribution here is a complete, direct, branchwise inverse **on the smaller eight-index set**, not a new general uniqueness theorem.

Sauer (arXiv:1603.03944, Algorithm 1) presents a general symbolic multivariate Prony algorithm using Hankel samples \(f(\alpha+\beta)\) over interpolation-index sets; its stated input is a function on all nonnegative indices, not this specific fixed eight-sample inverse. Cuyt and Lee (arXiv:1610.06329; Adv. Comput. Math. 44, 987–1002) develop efficient multivariate exponential analysis based on identification shifts and treat collided projections, possibly requiring additional probes; the fixed axis-plus-single-mixed sample and full cancellation branches here are not their stated theorem. Kunis et al. (arXiv:1506.00450) give multidimensional Toeplitz/Prony methods and stability under separation conditions, a distinct sampling framework. These comparisons concern mathematical statements and input requirements, not merely paper titles. An exhaustive historical-priority guarantee is not asserted.

## Limitations

The restriction to at most two atoms is essential to this short case analysis. There is no claim of optimality among *all* arbitrary frequency sets or of a numerically stable inverse near colliding nodes or cancelling amplitudes. When discriminants approach zero, floating-point versions can be extremely ill-conditioned. Unchecked older literature could contain an equivalent explicit eight-index formula; independent scholarly priority review remains necessary.

## References

1. B. Diederichs, M. N. Kolountzakis and E. Papageorgiou, *How many Fourier coefficients are needed?*, arXiv:2107.10348 (2021); Monatshefte für Mathematik 200, 23–42 (2023), doi:10.1007/s00605-022-01792-0.
2. T. Sauer, *Prony's method in several variables: symbolic solutions by universal interpolation*, arXiv:1603.03944 (2016/2017).
3. A. Cuyt and W.-s. Lee, *Multivariate exponential analysis from the minimal number of samples*, arXiv:1610.06329; Adv. Comput. Math. 44, 987–1002 (2018).
4. S. Kunis, T. Peter, T. Römer and U. von der Ohe, *A multivariate generalization of Prony's method*, arXiv:1506.00450; Linear Algebra Appl. 490, 31–47 (2016).
