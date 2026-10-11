# The exceptional divisor generates the Chow ring of the \(V_2^{\oplus n}/C_p\) resolution
## Finding
Let \(k\) be an algebraically closed field of characteristic \(p>0\), let \(n\ge2\), and let
\[
f:W\longrightarrow X=V_2^{\oplus n}/C_p
\]
be the smooth model constructed by Fan and Li. Let \(F\subset W\) be its unique exceptional prime divisor. Their torsor description factors the geometry through \(P=\mathbf P^{n-1}\): with \(L=\mathcal O_P(-1)\) and tautological quotient bundle \(Q\), set \(H=\operatorname{Tot}_P(L\oplus Q)\). The morphism \(W\to H\) is an affine torsor under the additive line bundle \(L^{\otimes p}\). Write \(\rho:W\to P\) for the composite and \(h=\rho^*c_1(\mathcal O_P(1))\).

Then
\[
\operatorname{CH}^*(W)\cong \mathbf Z[h]/(h^n),\qquad
\operatorname{CH}^*(F)\cong \mathbf Z[h_F]/(h_F^n),
\]
where \(h_F=h|_F\). Moreover
\[
[F]=-h,\qquad N_{F/W}\cong \rho_F^*\mathcal O_P(-1).
\]
Thus \(\operatorname{Pic}(W)=\mathbf Z[F]\), restriction sends \(h\) to \(h_F\), and
\[
F^j=(-1)^j h^j\ne0\quad(1\le j\le n-1),\qquad F^n=0.
\]
When \(n=p\), this is the integral exceptional intersection algebra of the unique projective crepant resolution supplied by the Fan--Li classification.

## Assumptions and scope
The statement concerns exactly the \(V_2^{\oplus n}\) family in Fan--Li, with \(n\ge2\). Chow groups are integral. The conclusion does not assert analogous formulas for the other Jordan-block cases in their paper, where their natural model can be singular. The only general input beyond Fan--Li's geometric presentation is homotopy invariance of Chow groups for vector bundles and affine bundles (torsors under vector bundles).

## Proof
Fan--Li construct \(P=\mathbf P^{n-1}\), \(L=\mathcal O_P(-1)\), and the tautological sequence
\[
0\to L\to \mathcal O_P^{\oplus n}\to Q\to0.
\]
They set \(H=\operatorname{Tot}_P(L\oplus Q)\), so \(H\to P\) is a rank-\(n\) vector bundle. Their Proposition 3.6 identifies \(W\to H\) as an affine torsor under the additive line bundle \(L^{\otimes p}\) pulled back to \(H\). Such a torsor is Zariski locally an affine-line bundle. Homotopy invariance therefore makes both pullbacks
\[
\operatorname{CH}^*(P)\longrightarrow\operatorname{CH}^*(H)
\longrightarrow\operatorname{CH}^*(W)
\]
isomorphisms. Since \(\operatorname{CH}^*(P)=\mathbf Z[h]/(h^n)\), this proves the first Chow-ring formula.

Let \(r\) be the universal section of the pullback of \(L\) to \(H\). Fan--Li identify \(H_0=V(r)\) with \(\operatorname{Tot}_P(Q)\) and identify \(F\) scheme-theoretically with \(W\times_H H_0\). Hence \(F\to H_0\) is the base change of the same affine-line torsor, while \(H_0\to P\) is a rank-\(n-1\) vector bundle. The same homotopy-invariance argument gives
\[
\operatorname{CH}^*(F)\cong\operatorname{CH}^*(P)=\mathbf Z[h_F]/(h_F^n),
\]
and the restriction map takes \(h\) to \(h_F\).

Because \(r\) is a section of the pullback of \(L\), its zero divisor satisfies
\[
\mathcal O_H(H_0)\cong \pi_H^*L.
\]
Pulling this Cartier divisor back along the flat torsor \(W\to H\) gives
\[
\mathcal O_W(F)\cong \rho^*L=\rho^*\mathcal O_P(-1).
\]
Therefore \([F]=c_1(\mathcal O_W(F))=-h\), and restriction to \(F\) gives
\[
N_{F/W}\cong\mathcal O_W(F)|_F\cong\rho_F^*\mathcal O_P(-1).
\]
The model \(W\) is smooth, so \(\operatorname{Pic}(W)=\operatorname{CH}^1(W)\cong\mathbf Z h\); since \([F]=-h\), the exceptional divisor itself generates the Picard group. Finally the projective-space relation gives \(h^j\ne0\) for \(j<n\) and \(h^n=0\), which yields the stated powers of \(F\).

## Verification
The proof was checked against the full text of Fan--Li, especially their construction of \(H\), Proposition 3.6, and Corollaries 3.7--3.8. Their paper explicitly states that the affine torsor is Zariski locally trivial and uses that fact to compute Grothendieck classes. Keyword checks of the full PDF found no Chow-ring or Picard-group computation. The sign of \([F]\) is fixed by the fact that \(H_0\) is the zero divisor of the tautological section of the pullback of \(L=\mathcal O_P(-1)\), so \(\mathcal O_H(H_0)\cong\pi_H^*L\), not its dual.

## Relationship to prior work
Fan--Li prove that \(W\) is smooth, identify its unique exceptional prime divisor, exhibit the affine-torsor presentation, and compute \([W]=\mathbb L^{n+1}[\mathbf P^{n-1}]\), \([F]=\mathbb L^n[\mathbf P^{n-1}]\) in the Grothendieck ring and \(\chi(W)=\chi(F)=n\). The present statement uses their stronger torsor geometry to determine the integral Chow rings and, crucially, the distinguished exceptional class and its normal bundle. Yasuda's wild McKay correspondence predicts the Euler characteristic \(p\) in the crepant case \(n=p\), but does not supply this integral exceptional intersection algebra.

## Limitations
This is a consequence of the affine-torsor geometry specific to the \(V_2^{\oplus n}\) case; it is not a new construction of the resolution and it does not extend the Fan--Li classification. The originality check covered the motivating full preprint, targeted web searches, published-finding corpus searches, and the older wild-McKay source identified below. A residual risk remains that an unindexed source records the same Chow-ring refinement.

## References
1. L. Fan and H. Li, *Resolutions of linear \(p\)-cyclic quotient singularities*, arXiv:2609.07182v1 (2026), especially Proposition 3.6 and Corollaries 3.7--3.8.
2. T. Yasuda, *The \(p\)-cyclic McKay correspondence via motivic integration*, Compositio Mathematica 150 (2014), arXiv:1208.0132.
3. W. Fulton, *Intersection Theory*, 2nd ed., Springer, 1998; homotopy invariance for Chow groups and the Chow ring of projective space.
