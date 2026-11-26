# A fixed-order stiff-limit positivity obstruction for symmetric graph heat filters

## Finding

Let \(L\) be the Laplacian of a finite connected undirected weighted graph and \(L^+\) its Moore–Penrose pseudoinverse. Fix a positive splitting multiple \(c\) and a finite integer filter order \(p\ge1\). For a step \(h\ge0\), define
\[
 J=(I+hcL/2)^{-1},\qquad R=I-(I-J)^p,\qquad T_{p,c}(h)=I-hLR^2.
\]
For every such fixed \(G,p,c\),
\[
 T_{p,c}(h)=I-\frac{4p^2}{c^2h}L^++O(h^{-2})\qquad(h\to\infty)
\]
in matrix norm. Thus any strictly positive off-diagonal entry of \(L^+\) forces a negative entry in the same position of the *completed step* for all sufficiently large \(h\). In particular, increasing the finite filter order or changing the positive splitting strength cannot prevent eventual endpoint-neighbor negativity on the unit path \(P_n\) for any \(n\ge4\):
\[
 (L_{P_n}^+)_{12}=\frac{(n-1)(2n-7)}{6n}>0.
\]
The obstruction persists even for splitting choices that guarantee every amplification factor lies in \([1/2,1]\) for all step sizes. One sufficient bound is \(c\ge4 C_p\), where
\[
C_p=\max_{x\ge0}x\left[1-\left(\frac{x}{1+x}\right)^p\right]^2.
\]

## Assumptions and scope

The graph has positive symmetric conductances on its edges. The physical generator is \(-L\) and the splitting operator is \(cL\). The two operators commute and the statement is for the completed filtered Euler map in exact arithmetic. The graph, order and splitting multiple are all held fixed in the limit. Path conductances are one, with vertices numbered consecutively. This is a sufficient sign obstruction, not a claim that this sign test is necessary or determines a finite-step threshold. In particular the analysis does not address order or splitting strength that grows with step size, or the nonlinearly filtered scheme.

## Proof

Spectral calculus gives eigenvalue \(1\) on constants. On a positive eigenvalue \(\lambda\) of \(L\), put \(x=hc\lambda/2\) and \(r_p(x)=1-(x/(1+x))^p\). Since \(x/(1+x)=1-1/(1+x)\), the binomial expansion with fixed \(p\) gives \(r_p(x)=p/x+O(x^{-2})\). Consequently the subtracted eigenvalue satisfies
\[
h\lambda\,r_p(x)^2=\frac{4p^2}{hc^2\lambda}+O(h^{-2}).
\]
There are finitely many positive eigenvalues, so this gives the stated matrix-norm expansion, with zero subtracted on constants. The identity contributes zero to any off-diagonal entry, and a strictly negative leading coefficient controls the sign for all sufficiently large steps. For arbitrary \(h\) the amplifier is \(1-(2/c)x r_p(x)^2\). The continuous nonnegative function \(x r_p(x)^2\) vanishes at zero and at infinity, so \(C_p\) is finite and \(c\ge4 C_p\) implies the claimed spectral band. Symmetry and preservation of constants also follow from spectral calculus.

To verify the unit-path obstruction, use the effective-resistance identity \(D_{ij}=(L^+)_{ii}+(L^+)_{jj}-2(L^+)_{ij}\). As \(L^+\mathbf1=0\), double centering gives \(L^+=-HDH/2\), with \(H=I-\mathbf1\mathbf1^\mathsf{T}/n\). For a unit path, \(D_{ij}=|i-j|\) by the unique series of edges. The endpoint row sum is \(n(n-1)/2\); the next row sum is \(1+(n-2)(n-1)/2\); the total is \(n(n^2-1)/3\). Hence
\[
 (L^+)_{12}=-\frac12+\frac{n(n-1)/2+1+(n-2)(n-1)/2}{2n}-\frac{n(n^2-1)/3}{2n^2}
 =\frac{(n-1)(2n-7)}{6n}.
\]
This is strictly positive for all \(n\ge4\), completing the proof.

## Relationship to prior work

Wu and Shu introduce the filter and its energy stability analysis; the spectral band is included here to distinguish the obstruction from scalar instability. Fontan and Altafini discuss the general sign structure of graph Laplacian pseudoinverses. Pseudoinverse sign arguments also occur in graph-step positivity analyses of the two-stage Gauss method, with a different multiplier. The conclusion retained here concerns the exact coefficient and persistence through **every fixed finite order** of the Wu–Shu resolvent filter. The sharp first-order four-vertex cutoff is not part of the claim: see the separate Resultary record `4f94a5560a16`, which states that cutoff in the variable \(sh/2\) for the symmetrically filtered Euler step. The date of the two catalogue records alone does not establish priority.

## References

1. Yue Wu and Chi-Wang Shu, *Unconditionally \(L^2\)-stable explicit–implicit–null filtered Runge–Kutta methods for general nonlinear degenerate parabolic equations*, arXiv:2611.02282v1, §3, https://arxiv.org/abs/2611.02282v1.
2. Angela Fontan and Claudio Altafini, *On the properties of Laplacian pseudoinverses*, arXiv:2109.14587v1, https://arxiv.org/abs/2109.14587v1.
3. *Four vertices are the sharp positivity barrier for symmetrically filtered Euler graph heat steps*, Resultary record `4f94a5560a16`.
4. *Unconditional fourth-order Gauss positivity on weighted paths: a four-vertex cutoff*, Resultary record `73910250a06c`.
