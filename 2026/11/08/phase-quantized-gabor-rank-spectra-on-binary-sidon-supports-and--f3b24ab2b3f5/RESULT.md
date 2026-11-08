# Phase-quantized Gabor rank spectra on binary Sidon supports and anisotropic conics

## Finding

Write \(G=\mathbb F_2^d\), with \(d\ge2\), and let \(N=|G|\). Suppose \(S\subseteq G\) has odd size \(s\ge3\) and has the **binary unordered-pair Sidon property**: all sums \(x+y\) for distinct unordered pairs \(\{x,y\}\subset S\) are different. For an arbitrary unimodular labeling \(z:S\to\mathbb C\), set \(g(x)=z_x\) on \(S\), and \(g(x)=0\) otherwise. Put \(C=\binom{s}{2}\), and declare two phase labels equivalent if their ratio lies in \(\mu_4=\{1,-1,i,-i\}\). If the nonempty equivalence classes have sizes \(\lambda_1,\ldots,\lambda_t\), the **exact complex-linear Gabor projector rank** is
\[
\boxed{\operatorname{rank}\mathcal L_g=N\left(1+C-\frac12\sum_{j=1}^t\binom{\lambda_j}{2}\right).}
\]
Every integer partition \(\lambda\vdash s\) is realizable by a unit-phase labeling. Thus this formula gives the *entire attainable rank spectrum*, not only upper and lower bounds. In particular,
\[
\boxed{N(1+C/2)\le\operatorname{rank}\mathcal L_g\le N(1+C),}
\]
with the lower endpoint attained exactly when every ratio of phase labels belongs to \(\mu_4\), and the upper endpoint exactly when every pair of phases represents distinct cosets of \(\mu_4\) in the unit circle.

For an alphabet of \(\ell\)-th roots of unity (integer \(\ell\ge1\)), put \(r=\ell/\gcd(\ell,4)\). Only partitions of \(s\) with at most \(r\) parts occur, and *every such partition occurs*. If \(s=ar+b\), where \(0\le b<r\), then the sharp maximum rank in that alphabet is
\[
N\left(1+\binom{s}{2}-\frac12\left[b\binom{a+1}{2}+(r-b)\binom a2\right]\right).
\]
The generic upper endpoint \(N(1+C)\) is achievable with the \(\ell\)-phase alphabet if and only if \(r\ge s\).

The singular spectrum is explicit, not merely the rank. Define \(\theta_{xy}\) by \(z_y\overline{z_x}=e^{i\theta_{xy}}\). Its multiset comprises the following \(N^2\) (possibly zero) singular values:
\[
\begin{array}{ll}
\sqrt N\left|\sum_{x\in S}(-1)^{\langle b,x\rangle}\right|, & b\in G;\\
2\sqrt N\,|\cos\theta_{xy}|\quad\text{and}\quad2\sqrt N\,|\sin\theta_{xy}|,
&\text{each with multiplicity }N/2,\ \{x,y\}\in\binom S2;\\
0,&\text{with multiplicity }N(N-1-C).
\end{array}
\]
The first \(N\) singular values are strictly positive because \(s\) is odd. Additional zeros occur precisely at resonant phase pairs.

A canonical geometric instance is the **anisotropic characteristic-two norm-one conic**. Let \(q=2^m\), \(m\ge1\), and choose \(\alpha\in\mathbb F_q\) with absolute trace \(1\). The set
\[
T_q=\{(x,y)\in\mathbb F_q^2:x^2+xy+\alpha y^2=1\}
\]
has \(s=q+1\) points, satisfies the binary unordered-pair property on the additive group of \(\mathbb F_q^2\), and so has sharp unrestricted Gabor lifting rank bounds
\[
\boxed{q^2\left(1+\frac{q(q+1)}4\right)\le \operatorname{rank}\mathcal L_g\le q^2\left(1+\frac{q(q+1)}2\right).}
\]
The lower and upper normalized rank fractions tend to \(1/4\) and \(1/2\), respectively, as \(q\to\infty\). For \(q=2\), the upper extreme is full rank, while for all \(q\ge4\) even a generic phase labeling cannot give full matrix recovery.

## Assumptions and scope

The group operation is vector addition over \(\mathbb F_2\); in particular, \(x-y=x+y\). The Sidon condition here concerns **distinct unordered pairs only**. It differs from the usual ordered-difference definition, which has no nontrivial instances in an exponent-two group. Phase masks are unimodular on their fixed support, never zero there. The complex-linear analysis operator on \(M_N(\mathbb C)\) is
\[
\mathcal L_g(X)=(\operatorname{Tr}(X P_{a,b}))_{a,b\in G},\qquad P_{a,b}=(W_{a,b}g)(W_{a,b}g)^*,
\]
where \(W_{a,b}h(t)=(-1)^{\langle b,t\rangle}h(t+a)\), and matrix and output spaces use Hilbert--Schmidt and Euclidean norms. Thus “rank” means identifiable **complex matrix** directions, not the number of real signal degrees of freedom in nonlinear phase retrieval. This definition determines the normalization of all singular values.

## Proof

**1. Gabor diagonalization with explicit normalization.** Set \(W_{u,v}=M_vT_u\). The matrices \(N^{-1/2}W_{u,v}\) form an orthonormal basis of \(M_N(\mathbb C)\). Conjugation by \(W_{a,b}\) multiplies \(W_{u,v}\) by the Walsh character \((-1)^{\langle a,v\rangle+\langle b,u\rangle}\). Writing \(P_{a,b}=W_{a,b}(gg^*)W_{a,b}^*\), orthogonality of these \(N^2\) characters implies that \(\mathcal L_g^*\mathcal L_g\) is diagonal in the Weyl basis with eigenvalue
\[
N|A_g(u,v)|^2,\qquad A_g(u,v)=\langle g,W_{u,v}g\rangle.
\]
Indeed the Weyl coefficient of \(gg^*\) is \(N^{-1/2}A_g(u,v)\) up to conjugation, and there are \(N^2\) measurement rows, giving \(N^2\cdot |A_g(u,v)|^2/N\). The singular values therefore are exactly \(\sqrt N|A_g(u,v)|\). This general diagonalization is classical and is not claimed as new.

**2. Zero shift.** When \(u=0\),
\[
A_g(0,v)=\sum_{x\in S}(-1)^{\langle v,x\rangle}.
\]
It is a sum of an odd number \(s\) of signs, so it is an odd integer and is nonzero at all \(N\) frequency points.

**3. Positive shifts and full singular multiset.** If \(u\ne0\), then \(A_g(u,v)\) is supported on \(S\cap(S+u)\). Under unordered-pair uniqueness this intersection is empty unless \(u=x+y\) for a unique pair \(\{x,y\}\); in that case it contains exactly \(x\) and \(y\). Consequently, with \(z_y\bar z_x=e^{i\theta}\),
\[
A_g(u,v)=(-1)^{\langle v,x\rangle}\left(e^{i\theta}+(-1)^{\langle v,u\rangle}e^{-i\theta}\right).
\]
Since \(u\ne0\), the map \(v\mapsto\langle v,u\rangle\) takes each Boolean value exactly \(N/2\) times. Hence the two modulus levels are \(2|\cos\theta|\) and \(2|\sin\theta|\) with those multiplicities. The shifts outside the \(C\) pair sums contribute exactly \(N(N-1-C)\) zeros.

**4. Rank and phase partitions.** Both modulus levels are nonzero unless the ratio \(z_y/z_x=e^{i\theta}\) belongs to \(\mu_4\); in that resonant case exactly one of the two levels vanishes. Thus each of the \(C\) pair shifts contributes either \(N\) or \(N/2\) to the rank. Resonance is the equivalence relation “same coset of \(\mu_4\)” on the phase labels, and if its class sizes are \(\lambda_j\), the count of resonant pairs is exactly \(\sum_j\binom{\lambda_j}{2}\). Adding the \(N\) zero-shift directions gives the rank formula. Because the unit circle has arbitrarily many distinct cosets modulo \(\mu_4\), each integer partition can be realized. The lower bound occurs only for one class, and the upper bound only for all singleton classes.

For \(\ell\)-root phases, the quotient \(\mu_\ell/(\mu_\ell\cap\mu_4)\) has exactly \(r=\ell/\gcd(\ell,4)\) classes. Every partition with at most \(r\) nonempty parts occurs by assigning a different quotient label to each part. To maximize rank, minimize \(\sum_j\binom{\lambda_j}{2}\); moving one label from a class larger than another by at least two strictly decreases this count. Therefore the minimizer has \(b\) classes of size \(a+1\) and \(r-b\) classes of size \(a\) (allowing empty classes when \(r>s\)). This proves the exact alphabet threshold and optimal balanced formula.

**5. Norm-one conic.** The polynomial \(X^2+X+\alpha\) is irreducible over \(\mathbb F_q\) because \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(\alpha)=1\). Hence \(Q(x,y)=x^2+xy+\alpha y^2\) is the norm from \(\mathbb F_{q^2}\), and every nonzero vector has nonzero norm. The norm-one fiber has size \((q^2-1)/(q-1)=q+1\), which is odd.

If \(u=a+b\ne0\), with \(Q(a)=Q(b)=1\), let \(B\) be the polar bilinear form of \(Q\). Then \(Q(u)=B(a,u)\). Every possible first point \(a'\) of another representation with this same sum \(u\) must satisfy \(B(a',u)=Q(u)\), so lies on the affine line \(a'=a+tu\) with \(t\in\mathbb F_q\), since \(B\) is nondegenerate. But
\[
Q(a+tu)=1+Q(u)(t^2+t).
\]
As \(Q(u)\ne0\), this equals one precisely when \(t=0\) or \(t=1\). Therefore \(\{a,b\}\) is the unique unordered pair with sum \(u\). Applying the rank formula with \(s=q+1\), \(N=q^2\) proves the claimed bounds and limiting fractions. The upper bound equals \(N^2\) only if \(1+q(q+1)/2=q^2\), i.e. \(q=2\), establishing the full-rank endpoint claim.

## Verification

Run the standalone standard-library checker `python3 check.py`. It implements fields of orders \(q=2,4,8,16\), builds each norm-one conic, verifies the cardinality and every unordered-pair sum, and directly calculates all \(N^2\) complex Weyl ambiguity coefficients for 4-, 6-, and 101-phase assignments. In every case it compares the observed nonzero count with the phase-partition formula. The script prints `BINARY_SIDON_PHASE_RANK_SPECTRUM_PASS` on success. At \(q=2\), an independent direct numerical singular-value decomposition of the complete 16-row operator also checked the \(\sqrt N\) normalization for distinct resonant and nonresonant masks. These finite tests support rather than replace the proof for all \(m\).

## Relationship to prior work

Cilleruelo [1] studies finite-field Sidon sets, with the classical ordered-difference definition and incidence applications. The present **unordered-pair** condition is essential in exponent two. Bojarovska and Flinth [2] provide the Gabor time-frequency ambiguity and operator-frame diagonalization (including the underlying \(N|A_g|^2\) norm relationship), and study characteristic functions of classical difference sets. We **do not claim** that general identity or standard finite-field conic geometry. The contribution here is the complete phase-label quotient classification of all attainable Gabor ranks, full singular multisets and root-of-unity alphabet threshold for the binary-Sidon setting, together with the sharp family of anisotropic conic consequences.

Related published research describes Gabor tomography for odd-characteristic hyperbolic quadratic shells, and sharp Fourier-extension norms for characteristic-two finite-field conics. Those settings and invariants differ from the phase-resolved complex Gabor lifting classification here. A more general published Gabor or finite-geometry theorem might still imply parts of this consequence; historical priority remains bounded by the inspected sources.

## Limitations

The theorem assumes odd-cardinality unordered binary-Sidon support, constant coefficient moduli and a full set of translations and Walsh modulations. It does not cover even support sizes, arbitrary amplitudes, partial measurement schedules, nonlinear signal recovery, or generic groups of odd exponent. The general Weyl diagonalization and norm-one conic cardinality are established ingredients, not new claims. This is a self-review, not independent mathematical validation. Historical-priority comparison is bounded and does not establish a global uniqueness claim.

## References

1. J. Cilleruelo, *Combinatorial problems in finite fields and Sidon sets*, arXiv:1003.3576v1, first publicly submitted 18 March 2010, https://arxiv.org/abs/1003.3576.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first publicly submitted 19 March 2015, https://arxiv.org/abs/1503.05800.
