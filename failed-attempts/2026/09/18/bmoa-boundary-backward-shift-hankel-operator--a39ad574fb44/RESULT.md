# The sharp BMOA boundary for a backward-shift Hankel operator

## Statement

Let \(S^*\) be the backward shift on \(H^2(\mathbb D)\). For
\[
g(z)=\sum_{m\ge 0}\alpha_m z^m\in H^2(\mathbb D)
\]
and a polynomial \(f(z)=\sum_{k\ge0}\beta_kz^k\), define
\[
L_g f=\sum_{k\ge0}\beta_k(S^*)^k g.
\]
Equivalently, the Taylor coefficients of \(L_g f\) are
\[
(L_g f)_j=\sum_{k\ge0}\alpha_{j+k}\beta_k,\qquad j\ge0,
\]
so \(L_g\) is the Hankel matrix \((\alpha_{j+k})_{j,k\ge0}\).

Then:

1. \(L_g\) extends to an everywhere-defined linear operator \(H^2(\mathbb D)\to H^2(\mathbb D)\) if and only if \(g\in \mathrm{BMOA}\). In that case the operator is automatically bounded.
2. \(L_g\) is compact if and only if \(g\in \mathrm{VMOA}\).
3. The hypothesis \(g\in H^2\) alone is insufficient. In particular,
   \[
   g(z)=\sum_{m=0}^\infty (m+1)^{-3/4}z^m
   \]
   belongs to \(H^2\), but the corresponding \(L_g\) is not an everywhere-defined operator on \(H^2\).

The third assertion gives a direct counterexample to Lemma 2.1 of Ferreira--do Carmo, arXiv:2609.19311v1, which states that the displayed \(L_g\) is well defined for every \(g\in H^2(\mathbb D)\).

## Proof

For a polynomial \(f=\sum_k\beta_kz^k\), the coefficient identity above follows from
\[
(S^*)^kg(z)=\sum_{j\ge0}\alpha_{j+k}z^j.
\]
Thus the matrix of \(L_g\) in the monomial basis is exactly
\[
\Gamma_g=(\alpha_{j+k})_{j,k\ge0}.
\]

Classical Nehari--Fefferman theory for Hankel matrices says that
\((\alpha_{j+k})\) defines a bounded operator on \(\ell^2(\mathbb N_0)\) if and only if the analytic function
\(\sum_{m\ge0}\alpha_m z^m\) belongs to BMO on the circle, equivalently \(g\in\mathrm{BMOA}\).
The corresponding Hartman/VMO criterion says that this Hankel operator is compact if and only if \(g\in\mathrm{VMOA}\).

It remains only to note that “everywhere defined” cannot be weaker here than boundedness. For each fixed \(j\), the row
\[
(\alpha_{j+k})_{k\ge0}
\]
lies in \(\ell^2\), since \(g\in H^2\). Hence the \(j\)-th output coordinate is a continuous linear functional of the input. If the Hankel formula mapped every \(\ell^2\) sequence to an \(\ell^2\) sequence, its graph would therefore be closed coordinatewise. The closed graph theorem would make \(L_g\) bounded. This proves the first assertion.

For the explicit obstruction, put
\[
\alpha_m=(m+1)^{-3/4}.
\]
Then \(\sum_m|\alpha_m|^2=\sum_m(m+1)^{-3/2}<\infty\), so \(g\in H^2\). Take also
\[
f(z)=g(z)=\sum_{k\ge0}(k+1)^{-3/4}z^k.
\]
Every formal output coefficient is finite and equals
\[
c_j=\sum_{k=0}^\infty (j+k+1)^{-3/4}(k+1)^{-3/4}.
\]
For \(j\ge16\), restricting to \(0\le k\le j\) gives
\[
\begin{aligned}
c_j
&\ge (2j+1)^{-3/4}\sum_{k=0}^{j}(k+1)^{-3/4}\\
&\ge (3j)^{-3/4}\int_1^{j+2}x^{-3/4}\,dx\\
&=4(3j)^{-3/4}\big((j+2)^{1/4}-1\big)\\
&\ge 2\,3^{-3/4}j^{-1/2}.
\end{aligned}
\]
Consequently \(\sum_j|c_j|^2=\infty\), so \(L_g f\notin H^2\). Thus the formula is not well defined on all of \(H^2\).

There is also a quantitative finite-section witness. With
\[
f_N(z)=N^{-1/2}\sum_{k=0}^{N-1}z^k,
\qquad \|f_N\|_{H^2}=1,
\]
for every \(0\le j<N\),
\[
(L_gf_N)_j
\ge N^{-1/2}N(2N)^{-3/4}
=2^{-3/4}N^{-1/4}.
\]
Therefore
\[
\|L_gf_N\|_{H^2}\ge 2^{-3/4}N^{1/4}\to\infty.
\]
This isolates the precise failure of the claimed bounded orbit-synthesis map.

## Consequence for arXiv:2609.19311v1

The preprint introduces \(L_g\) immediately before Proposition 2.2 and argues that
\[
(\beta_k)\longmapsto \sum_{k\ge0}\beta_k(S^*)^kg
\]
is bounded for every \(g\in H^2\). The calculation in that proof is precisely the Hankel matrix above, so the boundedness assertion requires \(g\in\mathrm{BMOA}\), not merely \(H^2\).

The same arbitrary-\(\ell^2\) orbit synthesis is then used to state \(L_g(H^2)\subset P_n(M)\) and inside the proof of Proposition 2.2. Hence the proof route through Lemma 2.1 is not valid as written for general \(H^2\) slice vectors. This record does **not** prove that Proposition 2.2, Corollary 2.3, or the later rigidity theorem are false: they may admit a different proof or hidden regularity may hold in the relevant setting. What is established is the failure of Lemma 2.1 as stated and the exact classical regularity threshold for that operator.

## Context and originality

The BMOA/VMOA characterization itself is classical Hankel-operator theory and is not claimed as new. The contribution here is the identification of the operator in arXiv:2609.19311v1 with that classical Hankel matrix, an explicit \(H^2\) counterexample to the universal well-definedness claim, a quantitative finite-section blow-up, and the resulting sharp repair boundary.

At the time of publication, arXiv lists only version v1 of arXiv:2609.19311, submitted 16 September 2026. Searches for the arXiv identifier, title, Lemma 2.1, the authors' names together with Hankel/BMOA terminology, and equivalent backward-shift orbit formulations did not locate a public correction of this lemma. Originality of the correction is therefore asserted only to the best of our knowledge.

## Limitations

This record concerns the operator \(L_g\) and the logical dependence on its claimed universal well-definedness. It does not decide the truth of the downstream minimal-invariant-subspace statements by other methods. It also does not claim novelty for Nehari's bounded-Hankel theorem, the Fefferman BMO formulation, or Hartman's compactness theorem.

No inaccessible paper was identified as a likely source of prior coverage of this specific correction. Classical primary papers of Nehari and Hartman were not needed to establish novelty of the correction; their standard boundedness/compactness criteria were checked through current reference sources.

## References

1. M. dos Santos Ferreira and J. M. Ribeiro do Carmo, *Projections and minimal invariant subspaces in the Hardy space over the bidisk*, arXiv:2609.19311v1 (2026), especially Lemma 2.1 and Proposition 2.2. https://arxiv.org/abs/2609.19311
2. *Hankel operator*, Encyclopedia of Mathematics, including the Nehari--Fefferman BMO boundedness criterion and the VMO compactness criterion. https://encyclopediaofmath.org/wiki/Hankel_operator
3. F. F. Bonsall and S. C. Power, *A proof of Hartman's theorem on compact Hankel operators*, Math. Proc. Cambridge Philos. Soc. 78 (1975), 447--450. https://doi.org/10.1017/S0305004100051914
