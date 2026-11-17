# Lossless backward-chain coherence for finite-ascent operators

## Finding

Let \(X\) be a complex Banach space and \(T\in\mathcal B(X)\) have finite ascent: for some integer \(p\geq0\),
\[
\ker T^p=\ker T^{p+1}.
\]
For \(x\in X\) and \(n\geq0\), let
\[
 a_n(x)=\inf\{\|y\|:T^ny=x\},
\]
with the infimum of the empty set defined to be \(+\infty\). Set
\[
 \gamma_{\mathrm{ind}}(x)=\limsup_{n\to\infty}a_n(x)^{1/n},\quad
 \gamma_{\mathrm{coh}}(x)=\inf_{(z_n)}\limsup_{n\to\infty}\|z_n\|^{1/n},
\]
where the latter infimum runs over all chains \(z_0=x\), \(Tz_{n+1}=z_n\), and is \(+\infty\) if there are none. The root expression concerns positive indices \(n\geq1\).

**Theorem (zero coherence penalty).** For every \(x\in X\), including those with no high-order preimages,
\[
\boxed{\gamma_{\mathrm{coh}}(x)=\gamma_{\mathrm{ind}}(x).}
\]
More precisely, if \(x\ne0\) has preimages under every power of \(T\), there is a unique backward chain \((z_n)_{n\geq0}\) with each \(z_n\in\operatorname{ran}T^p\). It satisfies, simultaneously for every \(n\geq0\),
\[
\boxed{\|z_n\|\leq\|T^p\|\left(1+\frac1{n+p+1}\right)a_{n+p}(x).}
\]
The same chain realizes the optimal exponential growth rate \(\gamma_{\mathrm{ind}}(x)\). For \(x=0\), the zero chain has rate zero.

Consequently, for the strict radial preimage spaces \(\mathcal I_r(T)\) and coherent radial spaces \(\mathcal K_r(T)\) of Aznay–Chabbabi–Zariouh, **all radii** \(r\geq0\) satisfy
\[
\boxed{\mathcal I_r(T)=\mathcal K_r(T).}
\]
For \(r>0\), both conditions mean that the corresponding growth rate is strictly less than \(1/r\); for \(r=0\), they mean finite growth rate. No closed-range, closed-radial-space, invariant-complement, or spectral-separation hypothesis is assumed.

## Assumptions and scope

The ascent hypothesis is algebraic: no topology on \(\operatorname{ran}T^p\) beyond its inherited norm is required. It includes all injective operators (\(p=0\)), but also operators with nonzero nilpotent kernels and nonclosed ranges. An infinite-dimensional Banach space is permitted, and the result does not require reflexivity. We take \(T^0=I\) and \(\|T^0\|=1\) on a nonzero \(X\). The zero space has only the zero vector and is trivial.

A standard equivalent formulation of finite ascent is \(\ker T^{p+n}=\ker T^p\) for every \(n\geq0\), by induction. Therefore \(T\) and every power of \(T\) act injectively on the algebraic subspace \(\operatorname{ran}T^p\).

## Proof

**Step 1: injectivity after stabilization.** If \(u=T^pv\in\operatorname{ran}T^p\) and \(Tu=0\), then \(v\in\ker T^{p+1}=\ker T^p\), hence \(u=0\). Thus \(T\), and therefore \(T^n\) for every \(n\geq1\), is injective on \(\operatorname{ran}T^p\). This conclusion does not require the range to be closed.

**Step 2: a canonical chain from unrelated preimages.** Suppose \(x\in\bigcap_{m\geq1}\operatorname{ran}T^m\). For every \(n\geq0\), independently choose \(y_{n+p}\) satisfying \(T^{n+p}y_{n+p}=x\). Define \(z_n=T^py_{n+p}\). Then \(z_n\in\operatorname{ran}T^p\), \(T^nz_n=x\) and \(z_0=x\). The vectors \(Tz_{n+1}\) and \(z_n\) both belong to \(\operatorname{ran}T^p\), and their \(T^n\)-images are both \(x\). Step 1 forces \(Tz_{n+1}=z_n\). Moreover, for each \(n\), \(z_n\) is the **unique** element of \(\operatorname{ran}T^p\) mapped to \(x\) by \(T^n\); thus the chain is independent of every choice of \(y_{n+p}\).

**Step 3: a simultaneous near-optimal bound.** If \(x\ne0\), then each \(a_m(x)\) is positive: for all \(y\) with \(T^my=x\),
\[
 \|x\|\leq\|T^m\|\,\|y\|,
\]
and \(\|T^m\|>0\) whenever \(x\) has such a preimage. Choose the unrelated preimages in Step 2 with
\[
\|y_{n+p}\|\leq\left(1+\frac1{n+p+1}\right)a_{n+p}(x).
\]
Such choices exist by the definition of the infimum. Applying \(T^p\) gives the stated norm inequality. Since the constructed \(z_n\) is unique in \(\operatorname{ran}T^p\), the bound holds for one and the same coherent chain for all indices.

**Step 4: exact exponential growth.** Any coherent chain is in particular an independent preimage at every order, so \(a_n(x)\leq\|z_n\|\). Consequently \(\gamma_{\mathrm{ind}}(x)\leq\gamma_{\mathrm{coh}}(x)\). If some \(a_m(x)=+\infty\), all subsequent \(a_n(x)=+\infty\), and there is no coherent chain, proving equality at \(+\infty\). Otherwise all preimages exist. For \(x\ne0\), Step 3 yields
\[
\limsup_{n\to\infty}\|z_n\|^{1/n}
\leq \limsup_{n\to\infty}a_{n+p}(x)^{1/n}
=\limsup_{m\to\infty}a_m(x)^{1/m}.
\]
For the last equality, a finite positive limsup is unchanged by a fixed index shift and by changing the positive root from \(1/m\) to \(1/(m-p)\); the same holds for an infinite limsup. The positive lower bound \(a_m(x)\geq\|x\|/\|T\|^m\) excludes the exceptional zero-limsup case. If \(p=0\), the same argument applies with \(\|T^0\|=1\). This proves equality. For \(x=0\), both growth quantities are zero by the zero chain.

**Step 5: radial equality.** For \(r>0\), independently chosen preimages meet the strict condition \(\limsup\|y_n\|^{1/n}<1/r\) if and only if \(\gamma_{\mathrm{ind}}(x)<1/r\): choose asymptotically near-infimal preimages as in Step 3. The analogous statement for coherent chains follows from their defining infimum: if \(\gamma_{\mathrm{coh}}(x)<1/r\), then at least one chain has a smaller rate. At radius zero, both spaces are the union over positive radii, equivalent to a finite rate. Step 4 proves all equalities.

**An example outside the earlier closedness and splitting hypotheses.** On the complex Hilbert space \(X=\mathbb C\oplus L^2(0,1)\), set
\[
T(a,f)=\left(\int_0^1 f(t)\,dt,\quad tf(t)\right).
\]
The kernel of every positive power is exactly \(\mathbb C\oplus\{0\}\), so the ascent is one. But there is no *closed, invariant complement* to its kernel. Indeed, such a complement would be a graph \(\{(\phi(f),f):f\in L^2\}\) for a bounded functional \(\phi\); its invariance would give \(\phi(tf)=\int_0^1 f\) for all \(f\), forcing its \(L^2\) representing function to be \(1/t\), a contradiction.

For each \(s\in(0,1)\) define
\[
x_s=\left(-\log s,\ \mathbf1_{[s,1]}\right).
\]
The preimages under \(T^n\) have second component \(t^{-n}\mathbf1_{[s,1]}\), while the first component can be arbitrary. Therefore
\[
 a_n(x_s)=\left(\int_s^1 t^{-2n}\,dt\right)^{1/2},\qquad
 \gamma_{\mathrm{ind}}(x_s)=1/s.
\]
For each fixed \(0<r<1\), vectors \(x_s\) with \(s>r\) lie in \(\mathcal I_r(T)\), but \(x_s\to x_r\) as \(s\downarrow r\) and \(x_r\notin\mathcal I_r(T)\). Hence every such \(\mathcal I_r(T)\) is nonclosed. The theorem nevertheless gives \(\mathcal I_r(T)=\mathcal K_r(T)\). The operator has continuum spectrum \([0,1]\), so spectral-countability criteria do not explain the example either.

## Verification

All arguments above are exact. In the example, for \(n\geq1\), the identity \(T^n(a,f)=(\int_0^1t^{n-1}f(t)\,dt,\ t^nf(t))\) directly verifies the asserted preimages. The root limit follows by bounding the integral above by \((1-s)s^{-2n}\) and below on each interval \([s,s+\varepsilon]\) by \(\varepsilon(s+\varepsilon)^{-2n}\), then sending \(\varepsilon\downarrow0\). The graph-complement contradiction is the Riesz representation theorem for \(L^2(0,1)\). No finite computation is invoked as a proof of an infinite-dimensional statement.

## Relationship to prior work

Aznay, Chabbabi and Zariouh introduce \(\mathcal I_r(T)\) and prove its equality with \(\mathcal K_r(T)\) under injectivity, spectral decomposition, and suitable closedness or countable-spectral hypotheses; their Example 3.5 demonstrates a failure of equality in general. In particular, Proposition 3.1 contains the injective case, Lemma 3.2 uses stabilized quotient kernels to transport *independent* preimages into an invariant subspace, Theorem 5.2 treats closed radial spaces, and Proposition 7.4 treats spectrally restricted operators. These statements and proof ingredients are acknowledged. The new conclusion concerns all finite-ascent operators and identifies **exact pointwise growth**, even for the nonsplitting, nonclosed-radial example above, without invoking a decomposition.

Koliha and Poon developed the coherent radial spaces and spectral-set decompositions, and the analytic core has a longer history. Their framework supplies motivation rather than an independently verified prior equality for the new independently chosen-preimage invariant. The same-result priority question has not been conclusively resolved across all historical formulations.

## Limitations

Finite ascent is sufficient, not necessary. The theorem does not characterize all operators for which the two growth quantities agree; in particular, infinite-ascent operators can have either equality or strict failure. The construction guarantees pointwise chains, not a bounded linear right inverse on a closed subspace, and gives no uniform bound in \(x\) when ranges are nonclosed. The original source's infinite-ascent example proves that no completely unconditional assertion is possible. Independent expert validation and a complete historical publication-priority determination have not been performed.

## References

1. Z. Aznay, F. Chabbabi and H. Zariouh, *Independent Backward Preimages and Algebraic Radial Decompositions of Operators*, arXiv:2611.06831v1, first posted 4 November 2026, especially §§2–3, 5, 7 and Proposition 8.1. https://arxiv.org/html/2611.06831v1
2. J. J. Koliha and P. W. Poon, *Spectral sets II*, Rend. Circ. Mat. Palermo (2) **47** (1998), 293–310.
3. M. Mbekhta, *Sur la théorie spectrale locale et limite des nilpotents*, Proc. Amer. Math. Soc. **110** (1990), 621–631.
4. B. P. Duggal, *Upper triangular operator matrices, asymptotic intertwining and Browder, Weyl theorems*, SpringerPlus **2** (2013), Article 268, DOI:10.1186/1029-242X-2013-268 (analytic core and finite-ascent background).
