# Arithmetic Bernoulli threshold and persistent word correlations in an additive toral skew product

## Finding

Fix integers \(b,q\ge2\). Let \(\mathbb T=\mathbb R/\mathbb Z\), give \(\mathbb T^2\) normalized Haar measure, and define
\[
 F_b(\omega,x)=(b\omega,\ x+\omega)\pmod1.
\]
Write \((\omega_t,X_t)=F_b^t(\omega_0,X_0)\), and let \(J_t=j\) if \(X_t\) belongs to the half-open cell \(I_j=[j/q,(j+1)/q)\), \(0\le j<q\). Then:

1. For every two distinct nonnegative times \(s,t\), the real-valued coordinates \(X_s,X_t\) are independent Haar-uniform circle variables. In particular \(J_s,J_t\) are independent and each is uniform on \(\{0,\ldots,q-1\}\).
2. The entire label sequence \((J_t)_{t\ge0}\) is independent and identically distributed **if and only if** \(q\mid b\). When this divisibility holds, the same independent uniform law holds conditionally on every conserved-fiber parameter \(Z\) defined in the proof.
3. For any fixed \(0\le j,k<q\), put \(A_t^{j,k}=\mathbf1_{\{J_t=j,J_{t+1}=k\}}\). Its long-lag covariance satisfies
\[
 \lim_{n\to\infty}\operatorname{Cov}(A_0^{j,k},A_n^{j,k})=V_{b,q}
 =\frac1{\pi^4b^2}\sum_{m\in\mathbb Z\setminus\{0\}}
 \frac{\sin^2(\pi m/q)\sin^2(\pi b m/q)}{m^4}.
\]
The limit is independent of \(j,k\). It is zero exactly when \(q\mid b\) and is strictly positive otherwise. The convergent series has the exact rational closed form
\[
 V_{b,q}=-\frac1{6b^2}\left[B_4(0)-B_4\!\left(\frac1q\right)
 -B_4\!\left(\left\{\frac bq\right\}\right)
 +\frac12B_4\!\left(\left\{\frac{b+1}q\right\}\right)
 +\frac12B_4\!\left(\left\{\frac{b-1}q\right\}\right)\right],
\]
where \(B_4(u)=u^4-2u^3+u^2-1/30\) on \([0,1]\) and \(\{\cdot\}\) means fractional part. For each \(n\ge1\),
\[
 \left|\operatorname{Cov}(A_0^{j,k},A_n^{j,k})-V_{b,q}\right|
 \le \frac{2(b+2)}{b^n}.
\]
For binary observations \(q=2\), this yields \(V_{b,2}=0\) for even \(b\), while \(V_{b,2}=1/(48b^2)\) for odd \(b\).

Thus a stationary process can have every distinct pair of *single-time labels* independent while its adjacent two-label cylinders retain a strictly positive correlation at arbitrarily long separations. Divisibility of the observation resolution by the base expansion separates an i.i.d. process from this persistent-memory regime.

## Assumptions and scope

The map acts on the compact two-torus, not on a single interval. The initial measure is **product Haar**, not an arbitrary initial distribution. All variables are understood modulo one, with endpoints of the half-open cells irrelevant under Haar measure. The integer \(b\) is fixed through time, and all assertions quantify over **all** integers \(b,q\ge2\) and all cell indices \(j,k\). The covariance involves a length-two word at time zero and an identical word at time \(n\); it is not the covariance of two single-time labels. No independence is claimed for continuous-valued triples or for arbitrary initial measures.

## Proof

**Haar invariance and a conserved coordinate.** The integer matrix of \(F_b\) is \(\begin{pmatrix}b&0\\1&1\end{pmatrix}\), of nonzero determinant \(b\). A surjective compact-group endomorphism takes Haar measure to Haar measure, so product Haar is stationary. Set
\[
 Z=\omega-(b-1)x\pmod1.
\]
Direct substitution gives \(Z\circ F_b=Z\). The change \((\omega,x)\mapsto(Z,x)\) has integer determinant one, so \(Z\) and \(X_0\) are independent Haar variables. On each level \(Z=z\), the fiber iterates the map
\[
 T_z(x)=bx+z\pmod1,
 \qquad X_t=b^tX_0+\frac{b^t-1}{b-1}z\pmod1.
\]
Translation by \(z/(b-1)\) conjugates \(T_z\) to the expanding circle endomorphism \(x\mapsto bx\pmod1\). In particular, every fiber map preserves Haar measure and is mixing (e.g. by its action on trigonometric characters).

**Pairwise independence.** For \(0\le s<t\), set \(H_t=(b^t-1)/(b-1)\). The map \((X_0,Z)\mapsto(X_s,X_t)\) is induced by the integer matrix \(\begin{pmatrix}b^s&H_s\\b^t&H_t\end{pmatrix}\), whose determinant is \((b^t-b^s)/(b-1)\ne0\). It is a surjective torus endomorphism, hence carries product Haar onto product Haar. This proves the first assertion, including the uniform probability \(\Pr(J_s=j,J_t=k)=q^{-2}\).

**If \(q\mid b\), all words are independent.** Fix any \(z\). Each cell \(I_j\) has length \(1/q\); under the slope-\(b\) map \(T_z\) its image traverses the entire circle exactly \(b/q\) times, counting multiplicity. Consequently the push-forward of normalized Lebesgue measure on \(I_j\) under \(T_z\) is Haar measure, independently of \(j,z\). Initially \(X_0\) is Haar, conditionally on \(z\). Inductively, after conditioning on the observed word \((J_0,\ldots,J_t)\), the conditional distribution of \(X_{t+1}\) is Haar, so the next label is conditionally uniform and independent of the word. Every finite word thus has probability \(q^{-r}\), for each \(z\), proving the claimed conditional and unconditional i.i.d. laws.

**Word correlations and conditional mixing.** For any \(z\) let
\[
 h_z(x)=\mathbf1_{I_j}(x)\,\mathbf1_{I_k}(T_zx),\qquad
 p_z=\int_{\mathbb T}h_z(x)\,dx.
\]
Conditionally on \(Z=z\), \(A_t^{j,k}=h_z\circ T_z^t(X_0)\). The expanding integer map \(T_z\) is mixing for Haar, giving
\[
 \lim_{n\to\infty}\mathbb E[A_0^{j,k}A_n^{j,k}\mid Z=z]=p_z^2.
\]
Since the unconditional two-time law is product Haar, \(\int p_z\,dz=q^{-2}\). Dominated convergence yields
\[
 \lim_{n\to\infty}\operatorname{Cov}(A_0^{j,k},A_n^{j,k})
 =\int_0^1(p_z-q^{-2})^2\,dz.
\]
The convergence has a uniform explicit rate: \(h_z\) is an indicator of a union of at most \(b+2\) intervals on the circle, hence its total variation is at most \(2(b+2)\). The \(n\)-step transfer operator of \(T_z\) averages over a grid of \(b^n\) equally spaced inverse branches. For any bounded-variation \(h\), comparison of that grid average to its integral gives \(\|P_z^nh-\int h\|_\infty\le\operatorname{Var}(h)/b^n\). Applying it to \(h_z\), integrating against \(h_z\), and then averaging over \(z\) proves the displayed uniform error bound.

**Fourier and exact rational evaluation.** Adopt \(\widehat f(m)=\int_0^1f(u)e^{-2\pi imu}\,du\). Fourier integration in \(z\) shows that for each nonzero integer \(m\),
\[
 \widehat {p}(m)=\widehat{\mathbf1_{I_k}}(m)
 \int_{I_j}e^{2\pi i m b x}\,dx.
\]
The absolute values of these two factors are \(|\sin(\pi m/q)|/(\pi|m|)\) and \(|\sin(\pi b m/q)|/(\pi b|m|)\), independent of the cell indices. Parseval gives the claimed nonnegative, absolutely convergent series. Its \(m=1\) summand is strictly positive whenever \(q\nmid b\), since \(q\ge2\); if \(q\mid b\) every summand vanishes. This establishes both positivity and the converse to the i.i.d. assertion, because i.i.d. labels would force the limiting covariance of separated words to be zero.

Finally apply \(\sin^2u=(1-\cos2u)/2\) and the standard fourth-Bernoulli Fourier identity
\[
 \sum_{m\in\mathbb Z\setminus\{0\}}\frac{\cos(2\pi mt)}{m^4}
 =-\frac{2\pi^4}{3}B_4(\{t\}).
\]
Termwise substitution gives the displayed five-term Bernoulli formula. In the binary case, the surviving summands for odd \(b\) are precisely the odd \(m\), and \(\sum_{m\ne0,\ m\ \mathrm{odd}}m^{-4}=\pi^4/48\), giving \(1/(48b^2)\).

## Verification

The accompanying standalone `checker.py` uses exact rational arithmetic. It evaluates the Bernoulli closed form and independently computes \(\int_0^1(p_z-q^{-2})^2dz\) by splitting the shift parameter at every overlap break point, integrating the square of the resulting affine functions. For \(2\le b\le12\), \(2\le q\le10\) and three distinct choices of \((j,k)\) per pair it confirms exact agreement and checks the divisibility-zero dichotomy. It separately checks the binary closed form. The checker is a finite consistency test: the universal theorem follows from the analytical steps above, not from these tests.

## Relationship to prior work

Giulietti, Marmi and Tanzi study deterministic chaotic forcing and approximate decay of single-fiber-observable correlations in general skew products. Their explicit additive-forcing example includes \(f(\omega,x)=T(x)+h(\omega)\); the family above is the concrete case \(T(x)=x\), \(h(\omega)=\omega\), \(g(\omega)=b\omega\). Their assumptions and results concern approximate one-observable memory loss and do not provide the divisibility criterion for equal-cell symbolic observations or the exact nonzero two-word covariance plateau. The conservation law in this special subfamily makes such a sharp distinction possible. Classical mixing of integer circle maps, character orthogonality, and Bernoulli-polynomial Fourier series are used as known methods, not claimed as new general principles. Parry's 1995 work and Siboni's 1994 study of translated-fiber skew systems supply contextual background on group-extension mixing; neither accessible abstract establishes this exact equal-cell two-word classification. These abstracts alone cannot exclude additional implicit results in their full texts.

## Limitations

The result is a complete exact classification for this **specific** linear additive forcing family and its equal-interval quantizers, not for generic nonlinear forcing or other partitions. Its nonmixing regime depends on using stationary product Haar and observing a fixed environmental parameter through two-label blocks; the single-time labels alone remain pairwise independent. We do not infer independence of real-valued triples. A general equivalence of this classification to an unindexed theorem in symbolic dynamics is not excluded; the publication-priority comparison is based on the identified sources and searches.

## References

1. P. Giulietti, S. Marmi and M. Tanzi, *Random-like properties of chaotic forcing*, arXiv:2104.06434v1, first posted 13 April 2021; Journal of the London Mathematical Society 106 (2022), 2804–2845. https://arxiv.org/abs/2104.06434
2. W. Parry, *Ergodic properties of a one-parameter family of skew-products*, Nonlinearity 8 (1995), 821–825. https://doi.org/10.1088/0951-7715/8/5/009
3. S. Siboni, *Ergodic properties of a class of skew-systems obtained by coupling the translation of the 1-torus with the endomorphism 2x mod [0,1[*, Nonlinearity 7 (1994), 1133–1141, DOI 10.1088/0951-7715/7/4/002 (abstract inspected; full text not inspected).
4. The standard Fourier expansion of the periodic fourth Bernoulli polynomial and Haar invariance under surjective torus endomorphisms are used in the proofs.
