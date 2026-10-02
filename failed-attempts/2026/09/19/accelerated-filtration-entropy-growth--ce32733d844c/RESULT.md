# Universal acceleration gives divergent filtration entropy on every infinite-dimensional affine algebra

## Result

Let \(A\) be an infinite-dimensional affine \(k\)-algebra. Then \(A\) admits a finite-dimensional exhaustive algebra filtration \(\mathcal F=\{V_n\}_{n\ge0}\) such that
\[
\boxed{h_{\rm alg}(A,\mathcal F)=+\infty.}
\]
Consequently,
\[
\boxed{h_{\rm alg}(A,\mathcal F)=0\text{ for every finite-dimensional filtration }\mathcal F
\iff A\text{ is finite dimensional}.}
\]

This record originally also presented an accelerated filtration on \(k[x]\) with positive entropy and a linear-control repair criterion. Those statements are correct, but they are no longer claimed as a distinct contribution here: the earlier same-day SCOPE record `accelerated-filtration-entropy-growth-obstruction--f6a5a54dee7a` already gives the stronger full entropy spectrum \([0,\infty]\) on \(k[x]\) and the linear-control repair. The contribution retained here is the universal \(+\infty\) acceleration theorem for arbitrary infinite-dimensional affine algebras.

## Proof

Choose a finite-dimensional generating subspace \(W\subset A\) containing \(1\), and put \(S_m=W^m\). Because \(A\) is infinite dimensional, \(d_m=\dim S_m\) is unbounded.

Construct integers \(r_1<r_2<\cdots\) recursively. Having chosen \(r_1,\ldots,r_{n-1}\), choose \(r_n\) so large that
\[
r_n\ge \max_{1\le i<n}(r_i+r_{n-i})
\]
and
\[
d_{r_n}-d_{r_{n-1}}\ge \lceil e^{n^2}\rceil.
\]
There are only finitely many superadditivity constraints at stage \(n\), and unboundedness of \(d_m\) makes the second requirement possible.

Set \(V_0=0\) and \(V_n=S_{r_n}\) for \(n\ge1\). Then every \(V_n\) is finite dimensional, the filtration is increasing and exhaustive, and for \(i,j\ge1\),
\[
V_iV_j\subseteq S_{r_i+r_j}\subseteq S_{r_{i+j}}=V_{i+j}.
\]
Moreover
\[
\dim(V_n/V_{n-1})=d_{r_n}-d_{r_{n-1}}\ge e^{n^2},
\]
so
\[
\limsup_{n\to\infty}\frac{\log\dim(V_n/V_{n-1})}{n}\ge n
\]
along every sufficiently large \(n\), and hence the entropy is \(+\infty\).

If \(A\) is finite dimensional, the definition assigns entropy \(0\) to every finite-dimensional filtration. This proves the equivalence.

## Context and originality boundary

Bock et al. (2024) define this filtered algebraic entropy, prove dependence under linear reindexing, and explicitly note that their results might suggest zero entropy could persist between filtrations. Schwarz–Sebandal (2026) make broad growth claims for arbitrary finite-dimensional filtrations. An earlier SCOPE record on 19 September 2026 already supplies a sharper polynomial-ring obstruction and the one-filtration linear-control repair. The only novelty claimed here is the universal acceleration mechanism above.

The construction is elementary once arbitrary filtrations are allowed, so equivalent older observations in re-filtering language remain a residual originality risk.

## References

1. W. Bock et al., *Algebraic Entropy of Path Algebras and Leavitt Path Algebras of Finite Graphs*, Results Math. 79 (2024), Art. 180, https://doi.org/10.1007/s00025-024-02198-0
2. J. Schwarz and A. Sebandal, *Growth functions of algebras and an application to Leavitt path algebras*, arXiv:2609.18144 (2026).
3. SCOPE, `2026/09/19/accelerated-filtration-entropy-growth-obstruction--f6a5a54dee7a` (earlier same-day record).
