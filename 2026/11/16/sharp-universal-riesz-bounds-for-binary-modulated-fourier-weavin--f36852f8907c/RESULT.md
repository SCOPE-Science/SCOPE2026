# Sharp universal Riesz bounds for binary-modulated Fourier weavings

## Finding

Let \(e_n(t)=e^{2\pi i n t}\) on \((0,1)\), and, for \(J\subseteq\mathbb Z\) and real \(\theta\), let
\[
\mathcal E_\theta(J)=\{e_n:n\in J\}\cup\{e^{2\pi i\theta t}e_n:n\notin J\}.
\]
For every \(|\theta|<1/2\), all these systems are Riesz bases of \(L^2(0,1)\). **Their optimal uniform squared Riesz bounds, simultaneously over every subset and every finite coefficient vector, are exactly**
\[
 A_\theta=1-\sin(\pi|\theta|),\qquad
 B_\theta=1+\sin(\pi|\theta|).
\]
The same numbers are their uniform frame bounds. Both are sharp already for the one-sided partition \(J=\{0,1,2,\ldots\}\), in the sense of limits of finitely supported vectors. The resulting worst-case squared condition-number ratio diverges as
\[
 \frac{B_\theta}{A_\theta}\sim\frac4{\pi^2(1/2-|\theta|)^2}
 \quad (|\theta|\uparrow 1/2).
\]
At \(|\theta|=1/2\), an explicit one-sided weaving fails the frame lower bound. For \(1/2<|\theta|<1\), an explicit one-sided weaving is incomplete. The qualitative cutoff is compatible with the classical one-quarter theorem; the quantitative novelty asserted here is the **optimal simultaneous constants** and their explicit realization, not the existence threshold alone.

## Assumptions and scope

Use Lebesgue measure \(dt\) on \((0,1)\), with \(\|e_n\|_2=1\). All norms are Hilbert-space norms. A squared Riesz lower (upper) bound means a constant \(A\) (\(B\)) satisfying
\[
 A\sum_{n\in\mathbb Z}|a_n|^2\le
 \left\|\sum_{n\in J}a_ne_n+
 \sum_{n\notin J}a_ne^{2\pi i\theta t}\right\|_2^2
 \le B\sum_{n\in\mathbb Z}|a_n|^2
\]
for every finite coefficient sequence, uniformly in \(J\). An invertible synthesis operator ensures that these are also frame bounds. The phase is real; the positive regime is \(|\theta|<1/2\) and the explicit obstruction regime is \(1/2\le|\theta|<1\). No assertion about phases outside \((-1,1)\) is needed; integral frequency shifts require separate reindexing.

## Proof

**1. Block synthesis and uniform cross-norm bound.** Write \(H=L^2(0,1)\), \(U=\overline{\operatorname{span}}\{e_n:n\in J\}\), \(V=U^\perp\), and let \(P_U,P_V\) be their orthogonal projections. Multiplication by \(e^{2\pi i\theta t}\) is the unitary \(M_\theta\). Relative to the orthogonal decomposition \(U\oplus V\), the weaving synthesis is
\[
 T_J(u+v)=u+M_\theta v,
\]
with Gram operator
\[
 T_J^*T_J=\begin{pmatrix}I_U&C_J\\C_J^*&I_V\end{pmatrix},
 \qquad C_J=P_UM_\theta P_V|_V.
\]
For \(0\le\theta\le1/2\), take \(c_\theta=e^{i\pi\theta}\cos(\pi\theta)\). The arc identity
\[
 \|M_\theta-c_\theta I\|
 =\operatorname*{ess\,sup}_{0<t<1}
 |e^{2\pi i\theta t}-c_\theta|=\sin(\pi\theta)
\]
gives \(\|C_J\|\le\sin(\pi\theta)\), since \(P_UI P_V=0\). Diagonalizing the block Gram form yields the claimed uniform quadratic bounds for \(0\le\theta<1/2\).

**2. Completeness and the frame interpretation.** With respect to output \(U\oplus V\), the synthesis is upper triangular:
\[
 T_J=\begin{pmatrix}I_U&C_J\\0&D_J\end{pmatrix},
 \qquad D_J=P_VM_\theta|_V.
\]
For every \(v\in V\),
\[
 \operatorname{Re}\langle e^{-i\pi\theta}D_Jv,v\rangle
 =\int_0^1\cos(2\pi\theta(t-1/2))|v(t)|^2dt
 \ge\cos(\pi\theta)\|v\|_2^2.
\]
For \(0\le\theta<1/2\), this coercivity holds for \(D_J\) and \(D_J^*\), making \(D_J\) boundedly invertible. Consequently \(T_J\) is onto and one-to-one; the weaving is a Riesz basis. The same squared bounds apply to its frame operator because \(T_JT_J^*\) and \(T_J^*T_J\) are unitarily equivalent for invertible \(T_J\).

**3. Sharpness from a shifted Hilbert corner.** Choose \(J=\{0,1,2,\ldots\}\), so the shifted columns are indexed by \(-k-1\) for \(k\ge0\). A direct Fourier integral gives
\[
 \langle e_j,M_\theta e_{-k-1}\rangle
 =-\frac{e^{i\pi\theta}\sin(\pi\theta)}{\pi(j+k+1-\theta)}
 \quad (j,k\ge0).
\]
Thus, up to a scalar phase, \(C_J\) is \((\sin(\pi\theta)/\pi)H_{1-\theta}\), with shifted Hilbert matrix \(H_a=(1/(j+k+a))_{j,k\ge0}\). For \(0\le\theta\le1/2\), Step 1 already implies \(\|H_{1-\theta}\|\le\pi\) whenever \(\theta>0\).

To prove the converse without assuming a Hilbert-matrix norm theorem, use the finite vector \(b^{(N)}_j=(j+1)^{-1/2}\), \(0\le j<N\), with zero coefficients elsewhere. Then \(\|b^{(N)}\|_2^2=\log N+O(1)\), and for each fixed \(a>0\),
\[
 \left\langle b^{(N)},H_a b^{(N)}\right\rangle
 =\pi\log N+O_a(1).
\]
Indeed replacing the sum by \(\int_1^N\!\int_1^N [\sqrt{xy}(x+y)]^{-1}dx\,dy\) incurs only a bounded error: the fixed denominator shift contributes a summable \((x+y)^{-2}/\sqrt{xy}\) discrepancy, and a cellwise derivative comparison bounds the Riemann-sum error. The substitution \(x=e^u,y=e^v\) turns the integral into
\[
 \int_0^{\log N}\!\int_0^{\log N}
 \frac{du\,dv}{2\cosh((u-v)/2)}
 =\pi\log N+O(1),
\]
because \(\int_{\mathbb R}[2\cosh(s/2)]^{-1}ds=\pi\). Therefore \(\|H_{1-\theta}\|\ge\pi\) and \(\|C_J\|=\sin(\pi\theta)\). Since the two Gram eigenvalue edges are exactly \(1\pm\|C_J\|\), neither uniform Riesz bound can be improved. Their ratio has the asserted quadratic asymptotic by \(\sin(\pi(1/2-\delta))=1-\pi^2\delta^2/2+O(\delta^4)\).

**4. At and above the half-phase boundary.** It suffices to consider \(\theta>0\), since multiplication by \(M_\theta\) interchanges the roles of the two bases and changes \(\theta\) to \(-\theta\). Choose \(J=\{\ldots,-2,-1\}\). Write \(z=e^{2\pi i t}\); let \(H_+\) and \(H_-\) be respectively the nonnegative and strictly negative Fourier-mode subspaces. The chosen weaving consists of \(H_-\) and \(M_\theta H_+\).

For \(1/2<\theta<1\), put \(\alpha=1-\theta\), \(0<\alpha<1/2\), and choose \(F(z)=(1-z)^{-\alpha}\in H_+\), with its holomorphic branch on the disk. The boundary identity
\[
 e^{2\pi i\theta t}
 z^{-1}\overline{F(z)}=e^{-i\pi\alpha}F(z),
 \qquad 0<t<1,
\]
shows that \(M_\theta^*F=e^{i\pi\alpha}z^{-1}\overline{F}\in H_-\). Thus nonzero \(F\) is perpendicular to both \(H_-\) and \(M_\theta H_+\), proving incompleteness.

At \(\theta=1/2\), define \(F_r(z)=(1-rz)^{-1/2}\in H_+\) for \(0<r<1\). Its norm diverges as \(\|F_r\|_2^2\asymp\log(1/(1-r))\). Nevertheless,
\[
 \|M_{1/2}^*F_r-i z^{-1}\overline{F_r}\|_2=O(1)
 \quad(r\uparrow1).
\]
To verify this, first note the exact boundary identity \(M_{1/2}^*(1-z)^{-1/2}=i z^{-1}\overline{(1-z)^{-1/2}}\) off \(z=1\). Set \(\delta=1-r\). On the two boundary arcs of total length \(O(\delta)\), each regularized term is \(O(\delta^{-1/2})\); on the remainder, comparison with the limiting identity and the mean-value bound for the power function give \(O(\delta/d^{3/2})\) at circle distance \(d\ge\delta\) from \(z=1\). Squaring and integrating yields \(O(1)\) in both regions. Since \(z^{-1}\overline{F_r}\in H_-\), the expression above implies \(\|P_+M_{1/2}^*F_r\|_2=O(1)\). The analysis energy of the chosen weaving on \(F_r\) is \(\|P_-F_r\|_2^2+\|P_+M_{1/2}^*F_r\|_2^2=O(1)\), divided by \(\|F_r\|_2^2\to\infty\). Hence no lower frame bound exists at the critical phase.

## Verification

The standalone `CHECK.py` performs 250 finite consistency assertions: coefficient-space Gram eigenvalue tests for 200 finite binary patterns, shifted Hilbert-matrix monotonicity and bound tests for five phases, direct numerical verification of the supercritical boundary identity, and critical approximate-annihilator diagnostics. Invoke `python CHECK.py` with NumPy and SciPy installed. These finite tests verify numerical normalizations and illustrative limits; they do not establish the infinite-dimensional theorem, which follows from the four analytical steps above.

## Relationship to prior work

Pai, Rocha and Yu's *Woven weighted exponentials* (first public 2026-08-14, arXiv:2608.14393) studies all-index woven completeness and sufficient frame conditions. Their Example 3.5 explicitly uses the classical Kadets one-quarter theorem to produce a phase-shift weaving. Their Theorems 3.17 and 3.19 give sufficient weaving and perturbation statements but not the above exact simultaneous optimal squared bounds for this two-phase family. Centering the two frequency shifts at \(\pm\theta/2\) and invoking Kadets already proves the **qualitative** weaving property when \(|\theta|<1/2\). The novelty claimed here is instead the exact \(1\pm\sin(\pi|\theta|)\) extremal envelope and its half-line Hilbert-corner saturation, together with the explicit way that envelope degenerates.

Cabrelli, Molter and Negreira's *Weaving Riesz Bases* (arXiv:2404.02229) gives a general characterization via uniformly invertible central compressions and broad translated-basis applications, but not this computed sharp envelope. Classical Hilbert-matrix and Hardy-space arguments provide proof ingredients: the novelty is their parameter-exact synthesis into a uniform answer to a natural weaving problem. Existing general perturbation estimates, including Kadets, should not be confused with a claim that the exact constants themselves are new without qualification; a possible equivalent older quantitative inequality is the main priority risk.

## Limitations

The statement uses unit-modulus scalar exponential generators and arbitrary binary partitions of the full integer Fourier lattice. It does not address general weights, more than two generators, multidimensional lattices, or noninteger phases outside the stated interval. Sharpness is in the infimum/supremum sense across arbitrarily long coefficient vectors; no finite vector need attain either edge. The qualitative half-phase cutoff is classical through the one-quarter theorem, and independent literature-priority assessment of the exact quantitative constants remains open.

## References

1. R. Pai, I. Rocha and P.-T. Yu, *Woven weighted exponentials*, arXiv:2608.14393, first posted 2026-08-14, https://arxiv.org/abs/2608.14393 .
2. C. Cabrelli, U. Molter and F. Negreira, *Weaving Riesz Bases*, arXiv:2404.02229, first posted 2024-04-02, https://arxiv.org/abs/2404.02229 .
3. M. I. Kadets, *The exact value of the Paley-Wiener constant*, Dokl. Akad. Nauk SSSR 155 (1964), 1253–1254. Used only for contextual comparison; the sharp quantitative bounds above have a direct proof.
