# Sharp one-third spectral-hole threshold for fourth-autocorrelation recovery

## Finding

Let \(G\) be any finite abelian group, let \(K=\widehat G\) be its dual, and let \(H\le K\) have index two. Fix \(a\in K\setminus H\). For a real-valued signal \(f:G\to\mathbb R\), put \(S=\operatorname{supp}\widehat f\). Suppose \(S\subseteq a+H\) and
\[
|S|>\frac23|H|.
\]
If another real-valued signal \(g:G\to\mathbb R\) has the same **single fourth-order autocorrelation** as \(f\), then \(g\) is a translate of \(f\). No lower-order autocorrelation data are assumed.

The strict density threshold is optimal as a uniform guarantee over all such groups: when \(G=\mathbb Z/6\mathbb Z\), its dual has index-two subgroup \(H=\{0,2,4\}\), and two nontranslated real signals with support \(S=\{1,5\}\) have identical fourth-order autocorrelations. Thus equality \(|S|=2|H|/3\) cannot be admitted universally.

## Assumptions and scope

Write the dual group additively. For \(\chi\in K\), use the unnormalized Fourier transform
\[
\widehat f(\chi)=\sum_{x\in G}f(x)\overline{\chi(x)}.
\]
The unnormalized fourth-order autocorrelation is the function on \(G^3\)
\[
\rho_4(f)(t_1,t_2,t_3)=\sum_{x\in G}f(x)f(x+t_1)f(x+t_2)f(x+t_3).
\]
Equality means equality at every triple \((t_1,t_2,t_3)\in G^3\). The value \(f\equiv0\) is excluded by the strict support-density hypothesis. No assumption is made about coefficient magnitudes, signs, exact arithmetic values, or the structure of \(H\).

## Proof

**1. Extract the support and pair-sum phases from the fourth autocorrelation.** Applying the Fourier transform in the three lag variables gives
\[
\widehat{\rho_4(f)}(u,v,w)
=\widehat f(u)\widehat f(v)\widehat f(w)
\widehat f(-u-v-w).
\]
For any \(s\in K\), take the zero-sum quadruple \((s,-s,s,-s)\). Since \(f\) is real, the corresponding Fourier product is \(|\widehat f(s)|^4\). Equality of the two fourth autocorrelations therefore implies
\[
|\widehat f(s)|=|\widehat g(s)|\qquad(s\in K).
\]
In particular, both Fourier supports equal \(S\). On this support set
\[
r(s)=\frac{\widehat g(s)}{\widehat f(s)}\in\mathbb T,
\]
where \(\mathbb T\) denotes the unit circle. Reality gives \(r(-s)=r(s)^{-1}\). Comparing the quadruples \((s_1,s_2,-s_3,-s_4)\) whenever \(s_1+s_2=s_3+s_4\) yields
\[
r(s_1)r(s_2)=r(s_3)r(s_4)
\quad(s_1,s_2,s_3,s_4\in S,\ s_1+s_2=s_3+s_4).
\tag{1}
\]
Thus the phase ratio is a multiplicative Freiman two-homomorphism on \(S\).

**2. The three-translate intersection creates a character on \(H\).** Translate \(S\) by \(-a\), obtaining \(A=S-a\subseteq H\), and set \(D=H\setminus A\). The hypothesis is exactly \(3|D|<|H|\). For every \(t\in H\), some \(s,s+t\in S\) exist, since two translates of \(D\) cannot cover \(H\). Define
\[
\delta(t)=\frac{r(s+t)}{r(s)}.
\]
This is independent of the choice of \(s\): for another \(y,y+t\in S\), the identity \((s+t)+y=s+(y+t)\) and (1) show that the two ratios coincide.

For arbitrary \(t,u\in H\), the three excluded sets \(D\), \(D-t\), \(D-t-u\) cover fewer than \(|H|\) elements. Hence there is an \(s\in S\) such that \(s,s+t,s+t+u\) all belong to \(S\). Consequently
\[
\delta(t+u)=\frac{r(s+t+u)}{r(s)}
=\frac{r(s+t+u)}{r(s+t)}\frac{r(s+t)}{r(s)}
=\delta(u)\delta(t).
\]
Therefore \(\delta:H\to\mathbb T\) is a character.

**3. Extend to the entire dual group.** Fix \(s_0\in S\) and put \(c=r(s_0)\). Because the nontrivial coset has order two in \(K/H\), \(2s_0\in H\). Also \(-s_0\in S\), by reality. Hence
\[
\delta(-2s_0)=\frac{r(-s_0)}{r(s_0)}=c^{-2},
\qquad c^2=\delta(2s_0).
\]
Define \(\chi:K\to\mathbb T\) by
\[
\chi(h)=\delta(h),\qquad
\chi(s_0+h)=c\,\delta(h)\quad(h\in H).
\]
The relation \(c^2=\delta(2s_0)\) verifies multiplicativity when both arguments lie outside \(H\); multiplicativity in the other two cases is immediate. Thus \(\chi\) is a character of \(K\). By the definition of \(\delta\), it agrees with \(r\) throughout \(S\), and both Fourier transforms vanish outside \(S\). Finite Pontryagin duality supplies \(x_0\in G\) with \(\chi(s)=s(x_0)\). Therefore
\[
\widehat g(s)=s(x_0)\widehat f(s)\quad(s\in K),
\]
and Fourier inversion gives \(g(x)=f(x+x_0)\) for all \(x\in G\).

**4. Failure exactly at two-thirds density.** Work on \(G=\mathbb Z/6\mathbb Z\), identified with its dual. Let \(S=\{1,5\}\), and prescribe the Fourier coefficients
\[
\widehat f(1)=\widehat f(5)=1,\qquad
\widehat g(1)=i,\quad \widehat g(5)=-i,
\]
with all other coefficients zero. Fourier inversion makes both signals real. Among four elements chosen from \(S\), a sum vanishes modulo six exactly when two entries are \(1\) and two are \(5\). The corresponding Fourier products equal \(1\) for both signals. Thus \(\rho_4(f)=\rho_4(g)\). If \(g\) were a translate of \(f\), the phase ratio at frequency \(1\) would be a sixth root of unity; it is \(i\), which has order four. Hence the signals are not translates. This proves sharpness in the uniform density sense.

## Verification

The proof is exact for every finite abelian group. As independent finite checks, the accompanying `CHECK.py` exhaustively verifies the required two- and three-translate intersections for every cyclic \(H\) of order at most \(18\), for every erasure pattern obeying \(3|D|<|H|\). It also checks all zero-sum quartic Fourier products in the six-point sharpness example, and confirms that its phase discrepancy cannot be a sixth-root character. These finite calculations test the combinatorial mechanism and the counterexample; they do not replace the general argument.

## Relationship to prior work

Agulnick and Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups* (first posted April 14, 2026), prove that under an index-two structure condition on Fourier support, autocorrelations **through order six** determine the signal, and they study the six-point obstruction. Their Lemma 4.4 identifies the relevant Fourier phase product relations. The present density condition yields recovery from **fourth order alone**, tolerates arbitrary locations of fewer than one-third missing modes in the nontrivial coset, and proves the universal threshold is sharp. The six-point obstruction is used with explicit attribution rather than asserted as a new example.

Casper and Orozco, *Reconstructing Gridded Data from Higher Autocorrelations* (2025), establish reconstruction from a range of autocorrelation orders for rational-valued grid signals. Their hypotheses and conclusion do not supply this single-order, real-valued, density-dependent theorem. Standard Freiman-homomorphism theory supplies useful conceptual language; the specific three-translate threshold and its fourth-autocorrelation consequence are established directly here.

## Limitations

This is an exact/noiseless uniqueness theorem; no numerical stability bound or constructive efficient decoder is asserted. The threshold is sharp as a **uniform guarantee across all finite abelian groups**; it is not claimed to be the minimum threshold for each fixed group or support geometry. Real-valuedness and support containment in a single nontrivial index-two coset are essential stated hypotheses. Possible equivalent results in older dense-Freiman-extension or higher-correlation literature remain a publication-priority risk; independent validation has not been performed.

## References

1. A. Agulnick and T. Busick-Warner, *Higher-Order Autocorrelations on Finite Abelian Groups*, arXiv:2604.13310v1 (April 14, 2026), Sections 1, 2, and 4. https://arxiv.org/html/2604.13310v1
2. W. R. Casper and B. Orozco, *Reconstructing Gridded Data from Higher Autocorrelations*, arXiv:2503.21022v1 (March 26, 2025). https://arxiv.org/abs/2503.21022
3. R. L. Adler and A. G. Konheim, *A note on translation invariants*, Proceedings of the American Mathematical Society 13 (1962), 425–428, as cited in reference 1.
