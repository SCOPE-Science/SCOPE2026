# Fan-tree Walsh singularities: a three-periodic dichotomy and sharp spectral gap

## Finding
For every integer \(n\ge1\), form the fan graph \(F_n=K_1\vee P_n\) by joining one hub to each of \(n\) path vertices. Let \(\mathcal T_n\subseteq\mathbb F_2^{2n-1}\) be the edge-incidence vectors of all spanning trees. The unnormalized Walsh coefficients
\[
W_n(b)=\sum_{T\in\mathcal T_n}(-1)^{\langle b,\mathbf1_T\rangle}
\]
vanish at some frequency if and only if \(3\mid n\). Their least positive absolute value and greatest common divisor agree, with sharp common value
\[
\gcd_{b}|W_n(b)|=\min_{b:W_n(b)\ne0}|W_n(b)|=
\begin{cases}2,&3\mid n,\\1,&3\nmid n.\end{cases}
\]
When \(n=3k\) with \(k\ge1\), at least \(2^{k+1}\) distinct frequencies vanish. Convolution by \(\mathbf1_{\mathcal T_n}\) on the full Boolean edge group is therefore invertible exactly for \(3\nmid n\). Its \(\ell^2\) Moore–Penrose pseudoinverse norm is \(1\) when \(3\nmid n\) and \(1/2\) when \(3\mid n\). The sharp positive-subspace spectral condition number is \(F_{2n}\) and \(F_{2n}/2\), respectively, where \(F_j\) is the Fibonacci sequence \(F_0=0,F_1=1\).

## Assumptions and scope
The edge group is the binary vector space of dimension \(2n-1\) with the usual mod-two coordinate pairing. The path has vertices \(1,\ldots,n\), plus hub \(0\). Its hub edges are assigned signs \(s_i\in\{\pm1\}\), and consecutive path edges signs \(t_i\in\{\pm1\}\). A Walsh frequency is uniquely specified by these signs; an edge has negative sign exactly when its frequency coordinate is one. Convolution is unnormalized, \((f*g)(x)=\sum_y f(y)g(x-y)\). For \(n=1\), the graph consists of a single hub edge and all assertions hold directly.

## Proof
**Signed matrix-tree identity.** For \(n\ge2\), delete the hub row from the oriented vertex-edge incidence matrix and call the resulting integer matrix \(B\). The weighted Laplacian cofactor \(L=B\operatorname{diag}(s_1,\ldots,s_n,t_1,\ldots,t_{n-1})B^{\mathsf T}\) has diagonal \(s_i+t_{i-1}+t_i\), where \(t_0=t_n=0\), and adjacent off-diagonal entries \(-t_i\). Cauchy–Binet yields
\[
\det L=\sum_{|S|=n}\det(B_S)^2\prod_{e\in S}\sigma_e=\sum_{T\in\mathcal T_n}\prod_{e\in T}\sigma_e=W_n(b),
\]
because \(\det(B_S)^2\) equals one for a spanning tree and zero otherwise. The identity is a polynomial identity, so it remains valid for negative edge weights. If \(d_j\) denotes the leading principal \(j\)-minor, then \(d_0=1\), \(d_1=s_1+t_1\), and, for \(2\le j\le n\),
\[
d_j=(s_j+t_{j-1}+t_j)d_{j-1}-d_{j-2}.
\]

**Parity and the nonresonant gap.** Replacing any sign by its negative does not change it modulo two. Hence every \(W_n(b)\) has the same parity as the all-positive tree count. The latter equals \(F_{2n}\): the unsigned fan count has initial values \(1,3\) and recurrence \(a_n=3a_{n-1}-a_{n-2}\), also satisfied by \(F_{2n}\). The sequence \(F_{2n}\pmod2\) is \(1,1,0\) periodically, so all Walsh coefficients are odd if \(3\nmid n\), and all are even otherwise.

Choose all path signs \(t_i=1\) and all spoke signs \(s_i=-1\). For \(n\ge2\), the cofactor has endpoint diagonal zero, interior diagonal one, and off-diagonal entries negative one. Its leading minors obey \(d_0=1\), \(d_1=0\), \(d_j=d_{j-1}-d_{j-2}\) for \(2\le j<n\), and \(d_n=-d_{n-2}\). The resulting six-periodic sequence \(1,0,-1,-1,0,1,\ldots\) shows that \(d_n=0\) exactly for multiples of three, and \(|d_n|=1\) otherwise. The same sharp value is immediate for \(n=1\). This proves the full zero classification and the least nonzero modulus one outside resonance.

**Sharp two-unit gap at resonance.** Let \(n=3k\), and start from the zero-producing signs just described. Flip the sign of the first hub edge, changing only the first diagonal entry from zero to two. Since the original determinant is zero, the new one equals twice the determinant of the trailing principal \((n-1)\)-minor. That minor has diagonal \(1,\ldots,1,0\) and off-diagonal entries \(-1\). Writing \(p_0=p_1=1\), \(p_j=p_{j-1}-p_{j-2}\), its determinant equals \(-p_{n-3}=(-1)^k\). Thus the modified Walsh coefficient is exactly \(2(-1)^k\). All coefficients are even, so the least positive magnitude is exactly two.

**Multiple independent zero frequencies.** For the same resonance signs, define a nonzero real vector by \(v_1=1,v_2=0\) and \(v_{i+1}=v_i-v_{i-1}\), for successive interior indices. Its entries repeat \(1,0,-1,-1,0,1\), and the endpoint equations hold whenever \(n=3k\). In particular, \(v_i=0\) at the \(k\) positions \(i\equiv2\pmod3\). Any independent sign changes of the hub edges at these positions change only diagonal entries multiplying zero coordinates, so the same vector remains in the kernel: there are \(2^k\) distinct zero frequencies with all path signs positive. Simultaneously reversing *every* edge sign negates the Laplacian and hence preserves its singularity, yielding \(2^k\) additional distinct zero frequencies with all path signs negative. Thus the number of Fourier zeros is at least \(2^{k+1}\).

**Operator conclusions.** The Walsh characters diagonalize unnormalized convolution on the full binary edge group, with eigenvalues \(W_n(b)\). The largest absolute multiplier is \(F_{2n}\), by the triangle inequality and equality at the zero frequency. The preceding sharp minimum gives exactly the claimed inverse or pseudoinverse norm and positive-subspace condition number; it also gives the greatest common divisor because a multiplier of the smallest possible magnitude has been explicitly constructed.

## Verification
The standalone `check_fan_walsh.py` enumerates spanning trees directly, evaluates full exact-integer Walsh transforms, and independently compares every transform entry with the signed tridiagonal determinant for \(1\le n\le9\). It verifies Fibonacci tree totals, zero existence, sharp gaps, greatest common divisors, and explicit zero-frequency constructions. It separately checks the constructive determinant witnesses for \(1\le n\le150\). On successful execution the program prints `FAN_WALSH_EXACT_PASS n=1..9 full spectra; n=1..150 witnesses`. These finite checks corroborate the general proof; they are not a substitute for its induction or for independent peer validation.

## Relationship to prior work
The all-positive fan spanning-tree formula \(F_{2n}\) is classical and explicitly proved by Chebotarev and by Bogdanowicz. The weighted matrix-tree identity is classical. Cameron, Grubb, and Sawada analyze efficient enumeration of fan spanning trees, rather than the full signed transform. The present statement concerns exact cancellation for **arbitrary independently signed edge weights**, the complete Fourier invertibility dichotomy, its sharp surviving spectral gap, and an explicit exponentially sized family of null frequencies. The unsiged count and weighted matrix-tree theorem are used as premises, not claimed as contributions.

## Limitations
No formula for the *exact number* of zero frequencies at resonant lengths is established, nor a sharp \(\ell^1\) projection or inverse norm. The proof concerns the binary edge group of the fan \(K_1\vee P_n\); it does not classify other joins or general weighted graphs. The literature comparison is bounded, and an older equivalent signed-continuant result cannot be ruled out. There has been no independent mathematical audit.

## References
1. P. Chebotarev, “Spanning Forests and the Golden Ratio,” arXiv:math/0612792, publicly submitted 2006-12-27; especially Theorem 1 and the fan-graph interpretation in Section 2. https://arxiv.org/html/math/0612792v4
2. Z. R. Bogdanowicz, “Formulas for the Number of Spanning Trees in a Fan,” *Applied Mathematical Sciences* 2 (2008), 781–786; Theorems 2.2–2.3. https://www.m-hikari.com/ams/ams-password-2008/ams-password13-16-2008/bogdanowiczAMS13-16-2008.pdf
3. A. Dall and J. Pfeifle, “A Polyhedral Proof of the Matrix Tree Theorem,” arXiv:1404.3876, publicly submitted 2014-04-15; weighted matroid formulation in Section 3. https://arxiv.org/html/1404.3876v2
4. B. Cameron, A. Grubb, and J. Sawada, “A Pivot Gray Code Listing for the Spanning Trees of the Fan Graph,” arXiv:2108.09363, 2021-08-20. https://arxiv.org/abs/2108.09363
