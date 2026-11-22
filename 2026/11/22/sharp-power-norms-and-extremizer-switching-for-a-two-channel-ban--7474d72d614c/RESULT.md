# Sharp power norms and extremizer switching for a two-channel Banach shift

## Finding

Let \(1\le p\le\infty\), let \(X_p=\ell^p(\mathbb N_0;\mathbb C^2)\) with the ordinary coordinatewise \(\ell^p\) norm, and let \(S\) be the unilateral forward shift on the sequence index. Set
\[
P=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad Q=I-P,
\qquad T=P+SQ,\quad R=Q+SP.
\]
Here constant matrices act at each sequence index. Both \(P\) and \(Q\) are norm-one projections on every \(\ell^p_2\), and \(T\) and \(R\) commute and satisfy \(TR=RT=S\), yet the two factors need not be contractions. For every positive integer \(k\),
\[
\boxed{\|T^k\|_{X_p\to X_p}=\|R^k\|_{X_p\to X_p}=2^{|1-2/p|}},
\]
with \(1/p=0\) for \(p=\infty\). Thus these factors are isometries exactly for \(p=2\); the sharp power bound does not grow with \(k\).

There is also a complete norming-vector dichotomy for \(1<p<\infty\), \(p\ne2\). Write \(x_n=(a_n+b_n,a_n-b_n)\) and extend \(b_n=0\) to negative indices. For \(1<p<2\), a nonzero \(x\) is norming for \(T^k\) exactly when there is a nonempty support set \(E\subset\mathbb N_0\) with \(E\cap(E+k)=\varnothing\), complex \(\ell^p\)-amplitudes \((b_n)\) supported on \(E\), and signs \(\epsilon_n\in\{-1,1\}\) such that \(a_n=\epsilon_n b_n\). For \(2<p<\infty\), the corresponding exact description is \(b\) supported on such an \(E\) and \(a_{n+k}=\epsilon_n b_n\), with every other \(a_j=0\). At \(p=2\), every vector is norming because \(T\) is an isometry. Endpoint norm identities also hold for \(p=1,\infty\); no endpoint extremizer classification is asserted.

## Assumptions and scope

All spaces and operators are over \(\mathbb C\); the statement is also true over \(\mathbb R\). For \(p=\infty\), take bounded sequences with the coordinate maximum norm; for finite \(p\), the usual counting-measure \(\ell^p\) norm. The zero vector is excluded when discussing norming vectors. The operator \(S\) has \((Sx)_0=0\), \((Sx)_n=x_{n-1}\) for \(n\ge1\). The notation \(E+k\) means \(\{n+k:n\in E\}\). The designation “norming” means exactly \(\|T^k x\|=\|T^k\|\|x\|\), not approximate attainment. Only the canonical equal-weight Haar projection \(P\) is considered; no analogous sharp formula for arbitrary projections is implied.

## Proof

First \(P^2=P\), \(Q^2=Q\), \(PQ=QP=0\), and \(S\) commutes with \(P,Q\). Therefore \(T^k=P+S^kQ\) and \((P+SQ)(Q+SP)=S\). Conjugation by the coordinate sign isometry \(D=\operatorname{diag}(1,-1)\) interchanges \(P,Q\), so \(R=DTD\) and the two power norms agree. The formulas \(Px=((x_1+x_2)/2,(x_1+x_2)/2)\) and \(Qx=((x_1-x_2)/2,(x_2-x_1)/2)\) show that \(P,Q\) are bicontractive and have norm one.

Set \(F_p(a,b)=|a+b|^p+|a-b|^p\). For \(1\le p\le2\), the sharp complex scalar Clarkson comparisons are
\[
2^{p-1}(|a|^p+|b|^p)\le F_p(a,b)\le2(|a|^p+|b|^p),
\]
and for \(2\le p<\infty\) they are
\[
2(|a|^p+|b|^p)\le F_p(a,b)\le2^{p-1}(|a|^p+|b|^p).
\]
These follow from the sharp \(\ell^p_2\)-norm of the two-point Walsh matrix \(H(a,b)=(a+b,a-b)\), namely \(\|H\|=2^{\max\{1/p,1-1/p\}}\), and \(H^{-1}=H/2\). For \(1<p<2\), equality in the upper scalar comparison holds precisely when \(ab=0\), and equality in the lower comparison holds precisely when \(a=\pm b\); for \(2<p<\infty\) these roles reverse. One way to check the strict equality cases is to write \(|a\pm b|^2=|a|^2+|b|^2\pm2\operatorname{Re}(a\bar b)\), apply strict convexity/concavity of \(u^{p/2}\) and the strict two-point power-mean inequality, and examine the equality conditions. These inequalities and equality cases are classical and not claimed as new.

Writing \(x_n=H(a_n,b_n)\) gives the exact identity
\[
(T^k x)_n=H(a_n,b_{n-k}),\qquad b_j=0\ (j<0).
\]
For \(1\le p<2\), the upper estimate on every output and the lower estimate on every input give
\[
\|T^k x\|_p^p\le 2\sum_n(|a_n|^p+|b_{n-k}|^p)
=2\sum_n(|a_n|^p+|b_n|^p)
\le2^{2-p}\|x\|_p^p.
\]
For \(2<p<\infty\), the inequalities reverse and give
\[
\|T^k x\|_p^p\le2^{p-1}\sum_n(|a_n|^p+|b_{n-k}|^p)
\le2^{p-2}\|x\|_p^p.
\]
At \(p=2\), equality is automatic. At \(p=\infty\), the explicit two-tap matrix has coordinate row-sum norm at most two. This proves all upper bounds.

For \(1\le p<2\), the input supported at time zero with \(x_0=(1,0)\) has output four coordinates of modulus \(1/2\) at times zero and \(k\), yielding ratio \(2^{2/p-1}\). For \(2<p\le\infty\), choose \(x_0=(1,-1)\), \(x_k=(1,1)\), all others zero. The output has a single nonzero coordinate equal to two, while the input has four unit-modulus coordinates, giving ratio \(2^{1-2/p}\). Thus every upper bound is sharp and attained; the formula for \(p=2\) follows from the isometric Parseval identity.

For \(1<p<2\), equality in the norm bound forces equality in every nonnegative scalar gap above. Hence \(a_n=\pm b_n\) whenever nonzero and \(a_n b_{n-k}=0\) at every index, equivalently the claimed \(k\)-disjoint support. Conversely these conditions make every scalar inequality an equality. For \(2<p<\infty\), equality forces \(a_n b_n=0\) and, for every index, either both \(a_n,b_{n-k}\) vanish or \(a_n=\pm b_{n-k}\). These are exactly the shifted support/sign conditions. Again they suffice. The strictness of scalar equality conditions establishes that there are no other norming vectors. The result applies to infinite \(\ell^p\) sequences by summing nonnegative gaps; equality of sums forces zero gaps term by term.

Finally, the invertible two-point Walsh change of coordinates conjugates \(T\) to \(I\oplus S\). Hence its spectrum is the closed unit disk for every \(p\), including the endpoint sequence spaces; this spectrum statement is supplementary, not needed for the norm proof.

## Verification

The included standalone `check.py` implements \(P\), \(Q\), and the lagged two-tap operator directly, checks \(TR=S\) and \(T^k=P+S^kQ\) on test sequences, tests random complex inputs against the proved norm upper bounds across several exponents and lags, and independently constructs each sharp finite-support extremizer. These finite tests are diagnostics, not substitutes for the all-parameter proof. Running `python check.py` reproduces the diagnostic count.

## Relationship to prior work

Jana, Pal and Roy develop block-Toeplitz models for commuting Banach-space Wold isometries and emphasize one-complemented ranges and the subtleties of Banach-space analogues of Hilbert-space shift models. The present test family is a fixed bicontractive two-channel projection pair; it illustrates quantitatively why a Hilbert-space inner matrix symbol need not yield Banach-space isometric factors. It does not assume their hypotheses for \(p\ne2\), and it is not a counterexample to their theorems. Maligranda and Sabourova establish the underlying sharp two-point Clarkson constants; those classical constants and their scalar equality cases are explicitly credited. The assertion here is the exact all-lag Toeplitz power law together with the classification of all norming sequences and their sharp change of support geometry at \(p=2\).

## Limitations

This is a two-channel, equal-weight example, not a universal Banach-space BCL theorem or a classification of all two-tap multipliers. The proof gives no quantitative near-extremizer stability and no full description of norming vectors at the endpoint exponents. The argument uses established two-point Clarkson inequalities, so the novelty of assembling them for this particular Toeplitz model and its extremizers is a bibliographic risk. Independent mathematical validation has not been performed.

## References

1. S. Jana, S. Pal and S. Roy, *On Słociński-type decomposition, BCL model and unitary extension of commuting Banach space Wold isometries*, arXiv:2611.11536v1 (8 November 2026), https://arxiv.org/html/2611.11536v1 .
2. L. Maligranda and N. Sabourova, *On Clarkson's inequality in the real case*, Math. Nachr. 280 (2007), 1363–1375, https://doi.org/10.1002/mana.200610552 .
3. J. A. Clarkson, *Uniformly convex spaces*, Trans. Amer. Math. Soc. 40 (1936), 396–414, https://doi.org/10.2307/1989630 .
