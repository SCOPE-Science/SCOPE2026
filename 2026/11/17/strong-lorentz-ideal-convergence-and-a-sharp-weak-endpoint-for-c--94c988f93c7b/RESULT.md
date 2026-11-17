# Strong Lorentz-ideal convergence and a sharp weak endpoint for compact Aluthge iterates

## Finding

Let \(H\) be a complex separable Hilbert space and let \(T\) be compact. Fix \(0<t<1\). Write \(T=U|T|\), and define \(\Delta_t(T)=|T|^tU|T|^{1-t}\). For \(n\ge0\), put \(X_n=\Delta_t^n(T)\). Denote by \(x^{(n)}=(s_k(X_n))_{k\ge1}\) the decreasing singular-value sequence and by \(a=(|\lambda_k(T)|)_{k\ge1}\) the decreasing moduli of nonzero eigenvalues, counted with algebraic multiplicity and then padded with zeros.

For every \(0<p,q<\infty\), if \(T\) lies in the Schatten--Lorentz ideal \(\mathcal S_{p,q}\), then
\[
\lim_{n\to\infty}\big\|x^{(n)}-a\big\|_{\ell_{p,q}}=0,
\qquad
\lim_{n\to\infty}\|X_n\|_{\mathcal S_{p,q}}=\|a\|_{\ell_{p,q}}.
\]
The first quasi-norm uses decreasing rearrangement of the absolute coordinate differences. Both conclusions also hold with \(\ell_{p,q}\) replaced by the little weak space \(\ell_{p,\infty}^{0}\).

The little weak condition is sharp for a universal claim: for each \(p>0\), the compact quasinilpotent weighted shift \(We_j=(j+1)^{-1/p}e_{j+1}\), \(j\ge0\), belongs to \(\mathcal S_{p,\infty}\setminus\mathcal S_{p,\infty}^{0}\) but satisfies
\[
\|\Delta_t^n(W)\|_{\mathcal S_{p,\infty}}=1
\quad(n\ge0),
\qquad
\|\Delta_t^n(W)\|_{\mathrm{op}}\longrightarrow0.
\]

## Assumptions and scope

For \(0<p,q<\infty\), define, for any complex sequence \(z\) and its decreasing absolute rearrangement \(z^*\),
\[
\|z\|_{\ell_{p,q}}^q=\sum_{k=1}^{\infty}\frac{(k^{1/p}z_k^*)^q}{k}.
\]
At \(q=\infty\), put \(\|z\|_{\ell_{p,\infty}}=\sup_{k\ge1}k^{1/p}z_k^*\). The little weak subspace consists of sequences for which \(k^{1/p}z_k^*\to0\). Operator ideals are defined via singular values. All limits are for the fixed transform parameter \(t\) and fixed \(p,q\). The assertion is about singular-value sequences, not convergence of the operators themselves in a Lorentz ideal. When \(H\) is finite-dimensional, pad all singular/eigenvalue sequences with zeros.

## Proof

**1. Common geometric-mean envelope.** For a nonnegative decreasing null sequence \(y\), set \(G_k(y)=(\prod_{j=1}^k y_j)^{1/k}\), declaring the product zero when a factor vanishes. The log-majorization inequality established in Stanković (Theorem 1.1 and equation (6)) gives
\[
\prod_{j=1}^k x_j^{(n)}\le\prod_{j=1}^k y_j,
\qquad y=s(T),
\]
for all \(n,k\). Because \(x^{(n)}\) is decreasing, \((x_k^{(n)})^k\le\prod_{j\le k}x_j^{(n)}\), so \(0\le x_k^{(n)}\le G_k(y)\). Stanković's same theorem gives \(x_k^{(n)}\to a_k\) at every fixed \(k\), hence also \(0\le a_k\le G_k(y)\).

**2. Lorentz stability of the envelope.** Fix \(p,q>0\), put \(r=p/2\), \(Q=q/r\), and \(A_k=y_k^r\). By arithmetic--geometric mean,
\[
G_k(y)^r\le (HA)_k:=\frac1k\sum_{j=1}^kA_j.
\]
The discrete Hardy operator is bounded on the weighted sequence quasi-space with functional \(\sum_{k\ge1}k^{-1}(k^{1/2}A_k)^Q\) when \(A\) is decreasing. To see this directly, write \(B_m=2^{m/2}A_{2^m}\). For \(2^m\le k<2^{m+1}\), subdividing the sum \(\sum_{j\le k}A_j\) into dyadic blocks yields
\[
k^{1/2}(HA)_k\le \sum_{\ell=0}^m 2^{-(m-\ell)/2}B_\ell.
\]
Summing with weights \(1/k\) over each dyadic block, using the geometric-kernel convolution inequality in \(\ell^Q\) (ordinary triangle inequality when \(Q\ge1\), subadditivity of the \(Q\)-th power when \(0<Q<1\)), and comparing \(B_m\) with the preceding block of the original decreasing sequence, gives a constant \(C_Q<\infty\) such that
\[
\sum_{k\ge1}\frac{(k^{1/2}(HA)_k)^Q}{k}
\le C_Q\sum_{k\ge1}\frac{(k^{1/2}A_k)^Q}{k}.
\]
Consequently \(\|G(y)\|_{\ell_{p,q}}^q\le C_Q\|y\|_{\ell_{p,q}}^q\). The same reasoning also covers sequences with zeros by approximation or the zero-product convention.

For the little weak space, if \(k^{1/p}y_k\to0\), then \(A_k=o(k^{-1/2})\). Splitting the Hardy average into finitely many initial terms and the tail, and using \(\sum_{j\le k}j^{-1/2}\le2\sqrt{k}\), shows \(k^{1/2}(HA)_k\to0\). Therefore \(k^{1/p}G_k(y)\to0\).

**3. Convergence of the differences.** Set \(d_{n,k}=|x_k^{(n)}-a_k|\). The envelope implies \(0\le d_{n,k}\le2G_k(y)\). As \(G(y)\) is decreasing, the decreasing rearrangement satisfies \(d_{n,k}^*\le2G_k(y)\) for each \(k\). Also \(d_{n,k}\to0\) for every fixed \(k\). Since \(G_k(y)\to0\), a finite-prefix/tail argument gives \(\sup_k d_{n,k}\to0\), hence each \(d_{n,k}^*\to0\). Dominated convergence applied to \(\sum k^{-1}(k^{1/p}d_{n,k}^*)^q\) proves the finite-\(q\) claim. For little weak \(q=\infty\), split \(\sup_k k^{1/p}d_{n,k}^*\) at a fixed large index, using the little weak envelope for the tail and pointwise convergence for the finite prefix. The convergence of the corresponding quasi-norm values follows from the quasi-triangle inequality and continuity of the Lorentz quasi-norm.

**4. Sharp failure in the full weak ideal.** Let \(We_j=w_je_{j+1}\) on \(\ell^2(\mathbb N_0)\), where \(w_j=(j+1)^{-1/p}\). The weights are positive and decreasing to zero, so \(W\) is compact. Moreover \(\|W^m\|=(m!)^{-1/p}\), and hence \(W\) is quasinilpotent. The generalized Aluthge transform of a positive weighted shift replaces its weights by \(w_j^{1-t}w_{j+1}^{t}\). Iteration gives
\[
w_j^{(n)}=\exp\!\left[-\frac1p\sum_{h=0}^n\binom nh(1-t)^{n-h}t^h\log(j+h+1)\right].
\]
For each fixed \(n\), this is decreasing in \(j\), satisfies \(w_j^{(n)}\le(j+1)^{-1/p}\), and obeys \((j+1)^{1/p}w_j^{(n)}\to1\) as \(j\to\infty\). Since the singular values of the weighted shift are precisely its weights, \(\|\Delta_t^n(W)\|_{\mathcal S_{p,\infty}}=1\). On the other hand, \(\|\Delta_t^n(W)\|_{\mathrm{op}}=w_0^{(n)}\to0\), because a \(\operatorname{Bin}(n,t)\) random variable tends to infinity in probability and the logarithmic mean of its successor diverges (for any fixed \(M\), it is at least \(\log(M+1)\,\Pr\{\operatorname{Bin}(n,t)\ge M\}\)). This concludes the proof.

## Verification

The file `CHECK.py` supplies independent finite checks of the geometric-mean envelope, dyadic Hardy domination and exact binomial weighted-shift recurrence for representative parameters. These finite checks are not an infinite-dimensional proof; all infinite assertions follow from the arguments above. The singular-value limit and log-majorization are taken from the stated primary reference.

## Relationship to prior work

Stanković (2026), Theorem 1.1, supplies pointwise singular-value convergence and weak log-majorization for compact Aluthge iterates. Its Theorem 5.5 proves an \(\mathcal S_p\)-norm limit under the stronger input assumption \(T\in\mathcal S_q\) for \(q<p\). The finite-\(q\) Lorentz convergence and the little-weak versus full-weak distinction here are not stated there; the new step is stability of the geometric-product envelope in the Lorentz scale, including the critical weak boundary. A separate earlier sharp same-index \(\mathcal S_p\) consequence is acknowledged and is not claimed again. Bala (2026) studies operator-norm convergence in the classical transform, which is weaker than the new ideal-sequence conclusion. Classical geometric-means/Lorentz inequalities are acknowledged as background to the Hardy estimate and not claimed as new.

## Limitations

The theorem does not imply convergence of \(\Delta_t^n(T)\) itself in operator or Lorentz quasi-norm to any fixed operator. It does not assert uniformity in \(t,p,q\). Weak-ideal failure is exhibited for a particular quasinilpotent operator, not every operator outside the little weak ideal. The historical geometric-means literature may contain an equivalent analytic envelope lemma; that would not by itself supply the stated compact-operator dynamical classification. Independent mathematical audit has not been performed.

## References

1. H. Stanković, *Singular values of iterated Aluthge transforms of compact operators*, arXiv:2611.07728v1 (first posted 5 November 2026), https://arxiv.org/html/2611.07728.
2. N. Bala, *The iterated Aluthge Transforms of compact operators*, arXiv:2602.07916v1 (first posted 8 February 2026), https://arxiv.org/abs/2602.07916.
3. *Arithmetic and Geometric Means, an Application to Lorentz Sequence Spaces*, Mathematische Nachrichten (1988), DOI:10.1002/mana.19881390125 (bibliographic comparison; full text not established here).
