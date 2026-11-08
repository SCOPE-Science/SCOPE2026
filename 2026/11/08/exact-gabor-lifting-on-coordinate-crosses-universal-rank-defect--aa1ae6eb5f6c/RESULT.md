# Exact Gabor lifting on coordinate crosses: universal rank defect and phase recovery

## Finding
Let \(A\) and \(B\) be finite abelian groups of odd orders \(m,n\ge3\), and let \(G=A\times B\), with \(N=mn\). Define the unnormalized binary window \(g=\mathbf 1_E\) on the **coordinate cross**
\[
E=(A\times\{0\})\cup(\{0\}\times B).
\]
For \(a\in G\) and \(\chi\in\widehat G\), put \((\pi_{a,\chi}f)(x)=\chi(x)f(x-a)\). Consider the complete complex-linear intensity-lifting map
\[
\mathcal L_g: \operatorname{End}_{\mathbb C}(\mathbb C^G)\longrightarrow \mathbb C^{G\times\widehat G},\qquad
\mathcal L_g(H)_{a,\chi}=\operatorname{tr}\bigl(H\,\pi_{a,\chi}gg^*\pi_{a,\chi}^*\bigr),
\]
where both matrix and output spaces have their ordinary Hilbert--Schmidt/Euclidean norms. Its exact complex nullity and rank are
\[
\boxed{\operatorname{nullity}\mathcal L_g=n(m-1)^2+m(n-1)^2,\qquad
\operatorname{rank}\mathcal L_g=N^2-n(m-1)^2-m(n-1)^2.}
\]
The kernel has an entrywise description: \(H\) belongs to it exactly when its diagonal and every off-diagonal entry joining points with **both** coordinates different vanish, while for each nonzero \(u\in A\) and \(v\in B\),
\[
\sum_{x\in A}H_{(x,y),(x-u,y)}=0\quad(\forall y\in B),\qquad
\sum_{y\in B}H_{(x,y),(x,y-v)}=0\quad(\forall x\in A).
\]
Despite this nonzero complex-linear kernel, the intensity data \(\mathcal L_g(ff^*)\) determine **every coordinatewise nonvanishing** \(f\in\mathbb C^G\) uniquely up to global unimodular scalar.

For \(A=B=\mathbb F_p\) under addition, \(p\ge3\) an odd prime, the **entire** singular-value multiset is \(p\) times the following listed ambiguity magnitudes, with their multiplicities. Entries with coincident numerical magnitudes are combined by adding multiplicities.

| Ambiguity magnitude | Multiplicity |
|---|---:|
| \(2p-1\) | \(1\) |
| \(p-1\) | \(2(p-1)\) |
| \(1\) | \((p-1)^2\) |
| \(p\) | \(2p(p-1)\) |
| \(2\) | \(p(p-1)^2\) |
| \(2\cos(\pi j/p)\), for each \(1\le j\le(p-1)/2\) | \(2p(p-1)^2\) |
| \(0\) | \(2p(p-1)^2\) |

In particular,
\[
\operatorname{rank}\mathcal L_g=p^4-2p(p-1)^2,
\quad \kappa^+(\mathcal L_g)=\frac{2p-1}{2\sin(\pi/(2p))}
\sim \frac{2}{\pi}p^2,
\]
where \(\kappa^+\) is the ratio of largest to smallest **positive** singular value. The identifiable fraction is \(1-2(p-1)^2/p^3\to1\), even though no finite member is injective on all matrices.

## Assumptions and scope
The group orders are odd and at least three; no cyclicity is assumed for the universal kernel/rank statement. The complete numerical singular-value table additionally assumes two one-dimensional additive groups over the same odd prime field. There is no normalization of \(g\): its nonzero entries are exactly \(1\). The output has \(N^2\) labeled coordinates and the domain is the full complex matrix space, not only the Hermitian subspace. Phase recovery is asserted only for signals nonzero at **every** point of \(G\).

## Proof
**1. Four exact overlap classes.** Set
\[
\mathcal A_g(a,\chi)=\langle g,\pi_{a,\chi}g\rangle,
\qquad T_a=E\cap(E+a).
\]
Up to complex conjugation, \(\mathcal A_g(a,\chi)=\sum_{x\in T_a}\chi(x)\); this phase convention does not affect its zeros or modulus. Writing \(a=(u,v)\), and \(\chi=(\alpha,\beta)\in\widehat A\times\widehat B\), direct intersection of the two coordinate axes gives
\[
\begin{array}{ll}
(u,v)=(0,0):&\mathcal A_g=m\mathbf1_{\{\alpha=1\}}+n\mathbf1_{\{\beta=1\}}-1,\\
 u\ne0,\ v=0:&\mathcal A_g=m\mathbf1_{\{\alpha=1\}},\\
 u=0,\ v\ne0:&\mathcal A_g=n\mathbf1_{\{\beta=1\}},\\
 u\ne0,\ v\ne0:&\mathcal A_g=\overline{\alpha(u)+\beta(v)}.
\end{array}
\]
In the first line the indicator of the trivial character is \(1\) or \(0\), not the group identity. Its four values are \(m+n-1\), \(m-1\), \(n-1\), and \(-1\), all nonzero for \(m,n\ge3\). In the final line the two character values cannot sum to zero: their ratio has odd order, so cannot equal \(-1\). Hence the only ambiguity zeros occur at shifts along one coordinate axis and modulations nontrivial on that same axis.

**2. Diagonalization and rank.** The normalized Weyl matrices \(\pi_{a,\chi}/\sqrt N\) form an orthonormal basis of the complex matrix space. Conjugation by the full time-frequency group acts on each Weyl matrix by a character; Fourier orthogonality makes the images under \(\mathcal L_g\) of distinct Weyl basis vectors orthogonal. Their singular values are exactly
\[
\sqrt N\,|\mathcal A_g(a,\chi)|.
\]
The four overlap classes therefore have \(N\), \((m-1)n\), \(m(n-1)\), and \((m-1)(n-1)N\) nonzero coefficients, respectively. Subtraction from \(N^2\) gives the stated nullity. Fourier inversion on the separate displacement diagonals \(H_{x,x-a}\) shows that \(a=0\) and mixed shifts must vanish entrywise in the kernel. For axial shifts only characters trivial on that axis survive, giving exactly the displayed row/column sum conditions. Counting their independent degrees of freedom yields \(n(m-1)^2+m(n-1)^2\), independently corroborating the Weyl count.

**3. Recovery on the nonvanishing stratum.** Suppose \(\mathcal L_g(ff^*)=\mathcal L_g(hh^*)\) and both signals are everywhere nonzero. The kernel description forces \(|f(x)|^2=|h(x)|^2\) at each point and \(f(x)\overline{f(y)}=h(x)\overline{h(y)}\) whenever both coordinates of \(x,y\) differ. The graph joining exactly those pairs is connected, indeed has diameter at most two: whenever a pair is not adjacent, choose an intermediate point whose first coordinate avoids both first coordinates and whose second coordinate avoids both second coordinates. Such choices exist because \(m,n\ge3\). The ratios \(h(x)/f(x)\) are therefore one and the same unit complex number on every vertex.

**4. Prime-field spectral multiplicities and conditioning.** Take \(m=n=p\). The zero-shift magnitudes are \(2p-1,p-1,1\) with multiplicities \(1,2(p-1),(p-1)^2\). The nonzero axial shifts have magnitude \(p\) on \(2p(p-1)\) frequencies. Every mixed shift has magnitude
\[
|\zeta^{r u}+\zeta^{s v}|=2\bigl|\cos(\pi(ru-sv)/p)\bigr|,
\quad \zeta=e^{2\pi i/p}.
\]
Because \(u,v\ne0\) and \(p\) is prime, every residue of \(ru-sv\) occurs for exactly \(p\) modulation pairs. Summing over the \((p-1)^2\) mixed shifts gives the asserted table, including no zeros. The minimum positive ambiguity magnitude is \(2\sin(\pi/(2p))\), and the maximum is \(2p-1\). Multiplication by \(p=\sqrt N\) cancels in their ratio, giving the condition number. The rank fraction and asymptotic statement follow algebraically and from \(\sin t\sim t\).

## Verification
The attached `check_cross.py` directly enumerates all \(N^2\) ambiguity coefficients for \(p=3,5,7\), compares every nonzero magnitude against the proved table, and independently assembles the full complex lifting matrix for \(p=3\) to check every singular value numerically. It reports respectively ranks \(57,465,1897\) and nullities \(24,160,504\). The separate `check_odd_groups.py` performs direct character-sum enumeration for \(A\times B\) equal to \(\mathbb Z_3\times\mathbb Z_5\), \((\mathbb Z_3)^2\times\mathbb Z_3\), and \(\mathbb Z_9\times\mathbb Z_3\), recovering the universal nullities \(68,228,228\). Run the scripts using `python check_cross.py` and `python check_odd_groups.py`; the first requires `numpy`, specified in `requirements.txt`. These finite checks corroborate, but do not replace, the analytic argument for all odd abelian groups and all primes.

## Relationship to prior work
Feichtinger, Kozek and Luef (2007, revised 2008) established the finite-abelian Gabor algebra and spreading representation. Bojarovska and Flinth (2015), especially their Theorem 2.3, give the general connection between self-ambiguity magnitudes and complex-linear Gabor intensity-lifting singular values; their Proposition 2.2 treats nonvanishing ambiguity for cyclic difference-set windows. Iosevich, Kolountzakis, Lyubarskii, Mayeli and Pakianathan (2017) classify aspects of Gabor **orthonormal** windows over prime fields. The theorem here specializes the general machinery to a different, non-orthonormal two-axis indicator window and supplies the exact rank, a concrete entrywise kernel, a full prime-field singular-value census, and recovery on the everywhere-nonzero signal class. A published finite-abelian-cross fourth-moment study concerns an \(L^4\) Fourier extension invariant, not Gabor intensity lifting. The present results should not be interpreted as a general uniqueness theorem for signals with zeros.

## Limitations
This is a linear-lifting spectral theorem and a restricted nonlinear phase-retrieval theorem. It does **not** assert complete phase retrieval of arbitrary sparse or vanishing signals, optimal conditioning among windows, or robustness to erasures. The rank and phase-recovery result assumes odd-order factors; even-order factors can have additional cancellation for mixed shifts. The displayed prime-field singular-value census is not asserted unchanged for composite cyclic factors. Historical novelty comparisons are necessarily bounded and do not establish absolute priority.

## References
1. H. G. Feichtinger, W. Kozek, F. Luef, *Gabor analysis over finite Abelian groups*, arXiv:math/0703228, first public version 2007-03-08; https://arxiv.org/html/math/0703228v2 .
2. I. Bojarovska, A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, first public version 2015-03-19; https://arxiv.org/html/1503.05800v2 .
3. A. Iosevich, M. Kolountzakis, Yu. Lyubarskii, A. Mayeli, J. Pakianathan, *On Gabor orthonormal bases over finite prime fields*, arXiv:1712.09120, first public version 2017-12-25; https://arxiv.org/html/1712.09120v1 .
