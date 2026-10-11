# Sparse-weight transfer law for Bohr correlations under iteration
## Finding
Let \(X\) be a compact metric space, let \(f:X\to X\) be continuous, and fix an integer \(q\ge 1\). For a bounded real sequence \(b=(b_m)_{m\ge 0}\), define the \(q\)-sparse lift \(a=(a_n)_{n\ge 0}\) by
\[
a_{qm}=b_m,\qquad a_n=0\quad\text{when }q\nmid n.
\]
Then \(a\) is a non-trivial weight exactly when \(b\) is, and for every \(x\in X\) and every \(\varphi\in C(X)\),
\[
\limsup_{N\to\infty}\frac1N\left|\sum_{n=0}^{N-1}a_n\varphi(f^n x)\right|
=\frac1q\limsup_{M\to\infty}\frac1M\left|\sum_{m=0}^{M-1}b_m\varphi((f^q)^m x)\right|.
\]
Therefore
\[
\mathcal N_a(f,X)=\mathcal N_b(f^q,X).
\]
Two permanence consequences follow. First, if \(f\) is Bohr chaotic, then every positive iterate \(f^q\) is Bohr chaotic. Second, suppose that \(f\) has full-entropy abundance in the sense that for every non-trivial bounded real weight \(\vartheta\),
\[
h_{\mathrm{top}}(f,\mathcal N_\vartheta(f,X))=h_{\mathrm{top}}(f,X).
\]
Then every iterate has the same property: for every non-trivial \(b\),
\[
h_{\mathrm{top}}(f^q,\mathcal N_b(f^q,X))=h_{\mathrm{top}}(f^q,X).
\]

## Assumptions and scope
The phase space is a compact metric space and \(f\) is an arbitrary continuous self-map. We use the real-weight convention of Hou--Lin--Tian: a bounded sequence \(\vartheta=(\vartheta_n)\) is non-trivial when
\[
\limsup_{N\to\infty}\frac1N\sum_{n=0}^{N-1}|\vartheta_n|>0,
\]
and \(\mathcal N_\vartheta(f,X)\) is the set of points for which some real continuous observable has positive limsup absolute correlation. Entropy on an arbitrary subset is Bowen topological entropy. No shadowing, specification, invertibility, surjectivity, or finite-entropy hypothesis is required for the transfer law. The entropy identities are interpreted in \([0,\infty]\).

## Proof
Set \(B=\sup_m|b_m|\). Write \(N=qM+r\) with \(0\le r<q\). The nonzero terms of the sparse sum below \(N\) consist of the first \(M\) sampled terms, plus at most the term with index \(m=M\) when \(r>0\). Hence
\[
\sum_{n=0}^{N-1}a_n\varphi(f^n x)
=
\sum_{m=0}^{M-1}b_m\varphi((f^q)^m x)+E_{M,r},
\]
where \(|E_{M,r}|\le B\|\varphi\|\). Also, replacing the denominator \(N\) by \(qM\) changes the normalized first sum by a quantity tending to zero, because \(|N-qM|<q\) and the first sum has absolute value at most \(MB\|\varphi\|\). Therefore
\[
\frac1N\sum_{n=0}^{N-1}a_n\varphi(f^n x)
-
\frac1q\frac1M\sum_{m=0}^{M-1}b_m\varphi((f^q)^m x)
\longrightarrow 0.
\]
Taking limsup of absolute values gives the displayed correlation identity. Applying the same argument with \(\varphi\equiv 1\) and absolute values on the weights gives
\[
\limsup_{N\to\infty}\frac1N\sum_{n=0}^{N-1}|a_n|
=
\frac1q\limsup_{M\to\infty}\frac1M\sum_{m=0}^{M-1}|b_m|,
\]
so non-triviality is preserved exactly.

Because the correlation identity holds for each fixed \(x\) and \(\varphi\), a point is correlated with \(a\) for \(f\) if and only if it is correlated with \(b\) for \(f^q\). This proves \(\mathcal N_a(f,X)=\mathcal N_b(f^q,X)\). If \(f\) is Bohr chaotic, then the sparse lift of every non-trivial \(b\) is non-trivial, so the identity supplies a correlated point for \(f^q\).

For the entropy assertion, assume full-entropy abundance for \(f\). Hou--Lin--Tian record the standard Bowen subset-entropy power law
\[
h_{\mathrm{top}}(f^q,Y)=q\,h_{\mathrm{top}}(f,Y)
\]
for every subset \(Y\subseteq X\). Using the exact correlated-set identity and the full-entropy hypothesis for the sparse lift \(a\),
\[
\begin{aligned}
h_{\mathrm{top}}(f^q,\mathcal N_b(f^q,X))
&=h_{\mathrm{top}}(f^q,\mathcal N_a(f,X))\\
&=q\,h_{\mathrm{top}}(f,\mathcal N_a(f,X))\\
&=q\,h_{\mathrm{top}}(f,X)\\
&=h_{\mathrm{top}}(f^q,X).
\end{aligned}
\]
This proves the claim.

## Verification
The proof has two independent exact steps. The index decomposition \(N=qM+r\) leaves at most one additional nonzero sparse term, and both its contribution and the denominator mismatch are \(o(1)\) after normalization. Thus the limsup identity is not a density heuristic: it is an exact asymptotic equality for every point and every continuous observable. The entropy step uses the subset power law stated as Lemma 2.11(3) in Hou--Lin--Tian, which applies to arbitrary subsets and therefore applies directly to the correlated set. No finite experiment or exhaustion argument is used.

## Relationship to prior work
Hou, Lin and Tian introduced the notation \(\mathcal N_\vartheta(f,X)\) for the set of points correlated with a weight and proved full-entropy abundance under shadowing or modified almost specification, including cyclic-decomposition formulations. Their Lemma 2.11(3) records the Bowen subset-entropy scaling law under powers. The inspected full text does not state the sparse-weight correlated-set identity above or the resulting general permanence principle for arbitrary systems already known to have full-entropy abundance.

Kawaguchi records several structural inheritance properties of Bohr chaoticity under embeddings and factors and proves new shadowing-based sufficient criteria. The inspected source also recalls the high-order horseshoe criterion. These statements do not identify time decimation with sparse lifting of the external weight and do not imply the exact correlated-set equality above.

Earlier papers introducing Bohr chaoticity and treating algebraic actions give major sufficient classes and closure mechanisms, but the inspected statements did not contain this iterate transfer law. The present result is deliberately limited to the exact implication established by the sparse-index calculation and does not claim a converse.

## Limitations
No converse is proved: Bohr chaoticity or full-entropy abundance of one iterate is not shown to imply the corresponding property for \(f\). The result treats integer iterates only and does not address nonuniform time changes, subsequences of zero or irregular density, or other entropy notions. The originality comparison is based on the cited full-text inspections and targeted searches; an elementary sparse-weight observation of this kind could have appeared elsewhere without being located.

## References
1. X. Hou, W. Lin and X. Tian, *Bohr chaoticity, semi-horseshoes and full-entropy abundance*, arXiv:2604.05713v1, 2026.
2. N. Kawaguchi, *A note on Bohr chaos and hyperbolic sets*, arXiv:2601.06869, 2026.
3. A.-H. Fan, S. Fan, V. Ryzhikov and W. Shen, *Bohr chaoticity of topological dynamical systems*, arXiv:2103.04745, later published in Mathematische Zeitschrift.
4. A.-H. Fan, K. Schmidt and E. Verbitskiy, *Bohr chaoticity of principal algebraic actions and Riesz product measures*, arXiv:2103.04767, later published in Ergodic Theory and Dynamical Systems.
