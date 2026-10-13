# Simple relative genus is 1-Lipschitz under topological concordance distance
## Finding
Fix a compact, oriented, simply-connected \(4\)-manifold \(N\) with boundary \(S^3\), and fix a nonzero class \(x\in H_2(N,\partial N)\) of divisibility \(d\). Let
\[
\mathcal D_d=\{K\subset S^3:H_1(\Sigma_d(K))=0\},
\]
where \(\Sigma_d(K)\) is the \(d\)-fold cyclic branched cover of \(S^3\) over \(K\). For \(K\in\mathcal D_d\), write
\[
G_{x,N}(K)=g^{\mathrm{simple}}_{x,N}(K)
\]
for the minimum genus of a locally flat properly embedded oriented surface in \(N\) with boundary \(K\), representing \(x\), whose complement has fundamental group \(\mathbb Z_d\).

Then for all \(K,J\in\mathcal D_d\),
\[
\left|G_{x,N}(K)-G_{x,N}(J)\right|
\le
g_4^{\mathrm{top}}(K\#-J).
\]
Thus \(G_{x,N}\) is \(1\)-Lipschitz for the topological concordance metric on \(\mathcal D_d\). Consequently, if \(K\) and \(J\) differ by one crossing change and both lie in \(\mathcal D_d\), then
\[
\left|G_{x,N}(K)-G_{x,N}(J)\right|\le1.
\]

## Assumptions and scope
Pencovitch's theorem is used exactly on the domain \(H_1(\Sigma_d(K))=0\). The same condition for both \(K\) and \(J\) implies that the relevant \(d\)-th roots of unity are not roots of either Alexander polynomial, so the Levine--Tristram signatures appearing below have no nullity contribution.

The topological concordance distance is
\[
d_{\mathrm{top}}(K,J)=g_4^{\mathrm{top}}(K\#-J),
\]
where \(g_4^{\mathrm{top}}\) is the locally flat topological \(4\)-genus.

No claim is made outside \(\mathcal D_d\), because the exact simple-genus formula used in the proof is not available there.

## Proof
Put
\[
\zeta=e^{2\pi i/d}
\]
and define, for \(0\le j<d\),
\[
A_j=
\sigma(N)-\frac{2j(d-j)}{d^2}\,x\cdot x.
\]
For \(K\in\mathcal D_d\), set
\[
M(K)=\max_{0\le j<d}
\left|A_j+\sigma_K(\zeta^j)\right|.
\]

Pencovitch's Theorem 1.1 and the discussion following Definition 1.3 give the positive-genus threshold
\[
G_{x,N}(K)
=
\max\left\{1,\left\lceil\frac{M(K)-b_2(N)}2\right\rceil\right\}
\]
unless genus zero is allowed. Genus zero occurs exactly when \(M(K)\le b_2(N)\) and the disc condition from the earlier simple-disc theorem is satisfied. If \(x\) is ordinary, that disc condition is automatic. If \(x\) is characteristic, it is
\[
\operatorname{Arf}(K)+\operatorname{ks}(N)
\equiv
\frac{\sigma(N)-x\cdot x}{8}
\pmod2.
\]

Let
\[
h=g_4^{\mathrm{top}}(K\#-J).
\]
Levine--Tristram signatures are additive under connected sum and change sign under mirror reversal, hence
\[
\sigma_K(\zeta^j)-\sigma_J(\zeta^j)
=
\sigma_{K\#-J}(\zeta^j).
\]
Powell's topological Levine--Tristram genus bound gives
\[
\left|\sigma_{K\#-J}(\zeta^j)\right|\le2h.
\]
Therefore
\[
|M(K)-M(J)|\le2h.
\]

Suppose first that both simple genera are positive. The map
\[
s\longmapsto
\max\left\{1,\left\lceil\frac{s-b_2(N)}2\right\rceil\right\}
\]
changes by at most \(h\) whenever \(s\) changes by at most \(2h\). Hence
\[
|G_{x,N}(K)-G_{x,N}(J)|\le h.
\]

It remains to handle genus zero. Suppose, without loss of generality, that \(G_{x,N}(J)=0\). Then \(M(J)\le b_2(N)\). If \(h=0\), the knots are topologically concordant. Their Levine--Tristram signatures agree, and their Arf invariants agree. Hence \(M(K)=M(J)\), and the genus-zero disc condition has the same truth value for \(K\) and \(J\); therefore \(G_{x,N}(K)=0\) as well.

If instead \(h\ge1\), then
\[
M(K)\le M(J)+2h\le b_2(N)+2h.
\]
Thus, even if the genus-zero disc condition fails for \(K\),
\[
G_{x,N}(K)
\le
\max\left\{1,
\left\lceil\frac{2h}{2}\right\rceil
\right\}
=h.
\]
This proves the stated inequality in every case.

A single crossing change gives a genus-one cobordism, equivalently
\[
g_4^{\mathrm{top}}(K\#-J)\le1,
\]
which yields the crossing-change corollary.

## Verification
The proof uses three independent ingredients.

First, Pencovitch's Theorem 1.1 gives the exact inequality
\[
b_2(N)+2g
\ge
\max_{0\le j<d}
\left|
\sigma(N)-\frac{2j(d-j)}{d^2}\,x\cdot x
+\sigma_K(\zeta^j)
\right|
\]
for positive genus, under \(H_1(\Sigma_d(K))=0\). The same paper separately records the genus-zero Arf condition.

Second, Powell's Theorem 1.4 gives the Levine--Tristram lower bound for locally flat topological \(4\)-genus, which for knots yields
\[
|\sigma_L(\omega)|\le2g_4^{\mathrm{top}}(L).
\]

Third, the only remaining arithmetic issue is the ceiling and the exceptional genus-zero branch. The bundled verifier exhaustively checks the abstract numerical lemma over a broad finite range. It returns:

`VERIFY_OK cases=1696768 b2=0..15 scores=0..63 h=0..15`

The finite computation is not the proof of the theorem; the universal proof is the inequality argument above.

## Relationship to prior work
Pencovitch proves an exact simple-relative-genus formula and derives connected-sum and satellite upper bounds. The inspected full text does not state a concordance-distance estimate, a Lipschitz property, or the crossing-change corollary.

Powell proves the topological Levine--Tristram genus inequality used to control the change of Pencovitch's signature maximum. That paper does not study simple surfaces in an ambient \(4\)-manifold or Pencovitch's relative genus.

The new point is that the recent exact formula, including its separate genus-zero Arf branch, is stable with constant one under topological concordance distance. This remains meaningful for the simple genus because a general cobordism need not preserve the cyclic-complement condition geometrically.

## Limitations
The theorem is restricted to knots for which \(H_1(\Sigma_d(K))=0\), exactly the domain of the source formula.

The bound is one-sided information about variation; it does not claim that concordance distance is detected sharply by the simple relative genus.

The crossing-change corollary requires both endpoint knots to remain in \(\mathcal D_d\).

## References
1. M. Pencovitch, *Simple Slice Surfaces*, arXiv:2609.22924v1, first posted 2026-09-19.
2. M. Powell, *The four genus of a link, Levine--Tristram signatures and satellites*, arXiv:1605.06833v3.
