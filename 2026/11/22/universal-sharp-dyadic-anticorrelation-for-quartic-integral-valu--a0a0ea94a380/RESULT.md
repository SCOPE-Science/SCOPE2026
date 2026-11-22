# Universal sharp dyadic anticorrelation for quartic-integral valuations

## Finding

For integers \(\ell\ge1\) and \(m\ge\ell\), let
\[
A_{\ell,m}=\frac{\ell!m!}{2^{m-\ell}}
\sum_{k=\ell}^{m}2^k\binom{2m-2k}{m-k}\binom{m+k}{m}\binom{k}{\ell}.
\]
This is the integral coefficient sequence of Amdeberhan, Manna and Moll. Put \(X_\ell(m)=\nu_2(A_{\ell,m})\), where \(\nu_2\) is the exponent of two in a positive integer. For every positive integer \(h\), the limits
\[
\mu_\ell=\lim_{N\to\infty}\frac1N\sum_{m=\ell}^{\ell+N-1}X_\ell(m),\qquad
\Gamma_\ell(h)=\lim_{N\to\infty}\frac1N\sum_{m=\ell}^{\ell+N-1}(X_\ell(m)-3\ell)(X_\ell(m+h)-3\ell)
\]
exist, \(\mu_\ell=3\ell\), and \(V_\ell:=\Gamma_\ell(0)>0\), where the second definition also applies at \(h=0\). Let
\[
P_\ell=2^{1+\lceil\log_2(2\ell)\rceil}.
\]
Then **the complete sharp autocorrelation lower bound and all its equality shifts** are
\[
\boxed{\frac{\Gamma_\ell(h)}{V_\ell}\ge-\frac12,
\quad\text{with equality exactly when}\quad
h\equiv\pm2\ell\pmod{P_\ell}.}
\]
Moreover, for each fixed nonzero \(h\), \(\Gamma_\ell(h)<V_\ell\), and \(\Gamma_\ell(2^j)/V_\ell\to1\) as \(j\to\infty\). Thus the supremum of the positive-shift correlations is one, but it is not attained. Each individual correlation has the following finite formula:
\[
\Gamma_\ell(h)=\sum_{t=1-2\ell}^{2\ell-1}(2\ell-|t|)K(h+t),
\quad K(0)=2,\quad K(d)=2-\frac3{2^{\nu_2(|d|)}}\ (d\ne0).
\]
All quantities in the displayed formula are exact rational numbers.

## Assumptions and scope

All integers \(\ell\ge1\) and shifts \(h\ge1\) are included; there is no primality or unproved distributional hypothesis. Natural density limits use consecutive positive indices, and include finite starting-index exclusions without changing their values. The reported correlations are centered at the actual limiting mean, not the finite-sample mean. The critical modulus \(P_\ell\) is a power of two, not an index period of the nonperiodic valuation sequence.

## Proof

The established exact valuation identity in Amdeberhan–Manna–Moll is
\[
\nu_2(A_{\ell,m})=\ell+\sum_{j=m-\ell+1}^{m+\ell}\nu_2(j).
\]
For any \(w\ge1\), define \(F_w(n)=\sum_{j=0}^{w-1}(\nu_2(n+j)-1)\) for positive \(n\). Hence \(X_\ell(m)-3\ell=F_{2\ell}(m-\ell+1)\). The geometric tails of \(\nu_2(n+j)\) have uniformly bounded second moments in long positive intervals, so residue-class averaging proves convergence of all the displayed means and second moments; the limiting mean of each \(\nu_2(n+j)\) is one.

For the 2-adic Haar average write \(K(d)=\mathbb E[(\nu_2(n)-1)(\nu_2(n+d)-1)]\). The divisibility-indicator expansion \(\nu_2(n)=\sum_{k\ge1}\mathbf1_{2^k\mid n}\), with monotone convergence of the products, gives
\[
K(d)=-1+3\sum_{k\ge1}2^{-k}\mathbf1_{2^k\mid d}.
\]
This equals the piecewise formula in the finding (also at \(d=0\), taking every indicator as one). Summing the \(w^2\) pair covariances gives
\[
C_w(h):=\mathbb E[F_w(n)F_w(n+h)]
=-w^2+3\sum_{k\ge1}2^{-k}N_k(h),
\]
where \(N_k(h)=\#\{0\le i,j<w:i-j\equiv h\pmod{2^k}\}\). The series converges because \(0\le N_k(h)\le w^2\). Consequently \(\Gamma_\ell(h)=C_{2\ell}(h)\) and the finite kernel formula follows.

For any \(q=2^k\) write \(w=aq+r\), \(0\le r<q\). The residue counts of \([0,w-1]\) are \(a+1\) on one cyclic arc of length \(r\), and \(a\) elsewhere. Therefore
\[
N_k(h)=qa^2+2ar+|[0,r-1]\cap([h,h+r-1]\bmod q)|.
\]
Two cyclic arcs of length \(r\) overlap in at least \(\max(0,2r-q)\) points. The shift \(h=w\) has residue \(r\) modulo \(q\) and attains this minimum. Thus \(N_k(h)\ge N_k(w)\) at *every* dyadic scale, proving \(C_w(h)\ge C_w(w)\).

Since \(F_{2w}(n)=F_w(n)+F_w(n+w)\), while \(F_{2w}(2n)=F_w(n)\) and \(F_{2w}(2n+1)=F_w(n+1)\), the variance of \(F_{2w}\) equals that of \(F_w\). Expanding the former variance gives \(2C_w(0)+2C_w(w)=C_w(0)\), hence \(C_w(w)=-C_w(0)/2\). The variance is positive: its centered valuation sum is unbounded on positive-measure dyadic cylinders, so it cannot be almost surely constant.

It remains to locate equality. Set \(P=2^{1+\lceil\log_2w\rceil}\) and \(q=P/2\). Since each dyadic-scale difference is nonnegative, equality requires minimal overlap at moduli \(P\) and \(q\). At modulus \(P\), \(w\le P/2\), so the two \(w\)-arcs are disjoint exactly when \(h\bmod P\in[w,P-w]\). If \(w=q\), this interval is the singleton \(\{w\}\). Otherwise \(q/2<w<q\); at modulus \(q\), the minimum overlap is attained precisely for \(h\bmod q\in[q-w,w]\). Intersecting these two conditions leaves exactly \(h\bmod P=w\) and \(h\bmod P=P-w\). Conversely, either congruence gives the minimizing shift \(\pm w\) at every scale at most \(P\), and for higher scales there are no colliding index pairs because \(P\ge2w\). Both therefore attain equality. Apply this with \(w=2\ell\).

For any fixed \(h>0\), at sufficiently high dyadic scales the zero shift has \(N_k(0)=w\), while \(N_k(h)=0\) if \(h\ge w\), and \(N_k(h)=w-h<w\) if \(h<w\), so \(C_w(h)<C_w(0)\). Conversely, at \(h=2^j\), the first \(j\) dyadic overlap terms equal those at zero; the remaining weighted tail is at most \(3w^2/2^j\), giving \(C_w(2^j)\to C_w(0)\). This completes the proof.

## Verification

`CHECK.py` independently evaluates the correlation kernel and its cyclic-arc formula, verifies the universal lower bound and the two equality residue classes for \(1\le w\le80\) over at least two full critical residue periods, and checks the defining coefficient sum against the cited valuation identity for a finite grid. It uses exact rational arithmetic only. Example outputs: \(\ell=3\) has variance \(3\), minimum covariance \(-3/2\), equality shifts \(h\equiv6,10\pmod{16}\); \(\ell=11\) has variance \(17/4\), minimum \(-17/8\), equality shifts \(h\equiv22,42\pmod{64}\). These are tests of the proof, not a substitute for its infinite argument.

## Relationship to prior work

Boros–Moll–Shallit introduced the integral-coefficient valuation problem. Amdeberhan–Manna–Moll proved the exact individual valuation formula and its block structure; that formula is the crucial input, not claimed here as new. The present claim instead determines **every shifted second moment**, its universally sharp correlation floor, and **all** equality lags through a dyadic-arc extremality argument. Known general carry-count and binomial-valuation machinery is relevant, but does not by itself identify the scale-by-scale overlapping-arc extremizers without further argument. An earlier equivalent autocorrelation theorem may exist outside the inspected literature.

## Limitations

This is a theorem about second moments and extremizing displacements, not a classification of the full two-point joint distribution. Priority is qualified pending a more exhaustive literature review, especially around p-adic digit-sum increments and factorial quotients. The proof and exact checker do not constitute an independent audit.

## References

- G. Boros, V. H. Moll and J. Shallit, *The 2-adic valuation of the coefficients of a polynomial*, first arXiv posting 2003-08-07, https://arxiv.org/abs/math/0308072 .
- T. Amdeberhan, D. Manna and V. H. Moll, *The 2-adic valuation of a sequence arising from a rational integral*, first arXiv posting 2007-07-14, https://arxiv.org/abs/0707.2119 .
