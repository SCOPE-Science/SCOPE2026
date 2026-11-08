# Universal boundary-energy trace law for radial Bergman Hankel operators

## Finding

Let \(d\ge2\) and let \(\nu\) be any unitary-invariant probability measure on the closed unit ball \(\overline{\mathbb B_d}\) whose radial essential supremum equals \(1\). This includes all normalized radial Bergman weights, surface measure on the sphere, and mixtures or singular radial measures. Put \(m_q=\int |z|^{2q}\,d\nu(z)\) and \(B_L=\binom{L+d-1}{d-1}\). Let \(A^2(\nu)\) be the closure of holomorphic polynomials in \(L^2(\nu)\), \(P\) its orthogonal projection, and \(P_{\le M}\) the projection onto polynomials of total degree at most \(M\).

For any bounded holomorphic \(f\) on \(\mathbb B_d\), write \(f=\sum_{k\ge0}f_k\) as its homogeneous Taylor decomposition, and let \(a_k=\int_{\partial\mathbb B_d}|f_k(\zeta)|^2\,d\sigma(\zeta)\), where \(\sigma\) is normalized sphere measure. Set \(H_{\overline f}=(I-P)M_{\overline f}\) on \(A^2(\nu)\). Then, **for every integer \(M\ge0\)**, the compressed Hilbert–Schmidt energy obeys the exact identity

\[
T_M(f):=\operatorname{Tr}(P_{\le M}H_{\overline f}^*H_{\overline f}P_{\le M})
=\sum_{k=1}^{\infty}a_k\sum_{L=\max\{0,M-k+1\}}^M B_L\frac{m_{L+k}}{m_L}.
\]

The following **universal, weight-independent** limit holds in the extended nonnegative reals:

\[
\boxed{\lim_{M\to\infty}\frac{T_M(f)}{\binom{M+d-1}{d-1}}=\mathcal E_{\partial}(f):=\sum_{k=1}^{\infty} k\,a_k\in[0,\infty].}
\]

If \(0<\mathcal E_{\partial}(f)<\infty\), then \(T_M(f)\sim \mathcal E_{\partial}(f)M^{d-1}/(d-1)!\). If the energy is infinite, this normalization diverges to infinity. In particular every nonconstant bounded holomorphic symbol has non-Hilbert–Schmidt \(H_{\overline f}\) in complex dimension \(d\ge2\). For \(d=1\) the same proof yields \(\|H_{\overline f}\|_{\mathcal S_2}^2=\mathcal E_{\partial}(f)\), with infinite values allowed; this one-dimensional identity is a known classical consistency case, not a claim of novelty.

For the standard probability-weighted ball measure \(d\nu_t\propto(1-|z|^2)^t\,dV\), \(t>-1\), and the coordinate symbol \(f(z)=z_1\), the exact finite-scale benchmark is

\[
\boxed{T_M(z_1)=\frac{\binom{M+d}{d}}{M+d+t+1}},\qquad
\mathcal E_{\partial}(z_1)=\frac1d.
\]

## Assumptions and scope

All measures are positive, finite, probability-normalized, invariant under the full unitary group, and supported in the closed unit ball with radial essential supremum \(1\). No density, regularity, or absolute-continuity requirement is imposed. All moments \(m_q\) are strictly positive. On any sphere component the bounded holomorphic symbol is interpreted through its almost-everywhere radial boundary value, which is bounded; interior values use the ordinary holomorphic function. The finite-dimensional trace is computed on the analytic polynomial subspace \(A^2(\nu)\). If the radial support lies strictly inside the ball, the displayed universal boundary limit is not asserted. The purpose of the dimension restriction \(d\ge2\) is the several-variable growth law; the exact identity also holds in dimension one.

## Proof

**Orthogonal homogeneous structure.** Unitary invariance gives, for every multiindex \(\alpha\in\mathbb N^d\),
\[
\|z^\alpha\|_{L^2(\nu)}^2=\frac{\alpha!}{(d)_{|\alpha|}}m_{|\alpha|},
\]
where \((d)_L=d(d+1)\cdots(d+L-1)\). Distinct monomials are orthogonal. Consequently the normalized degree-\(L\) monomial basis satisfies the exactly radial kernel identity
\[
\sum_{|\alpha|=L}|e_\alpha(z)|^2=B_L\frac{|z|^{2L}}{m_L}.
\]
The multinomial theorem proves this equality, and \(\dim\mathcal H_L=B_L\).

**Commutator identity.** Since multiplication by \(f\) preserves the analytic space, \(H_{\overline f}^*H_{\overline f}=M_f^*M_f-M_fM_f^*\). Fix a degree \(L\). The operators of homogeneous pieces \(f_j\) and \(f_k\) with \(j\ne k\) make no contribution to the trace of the compression to \(\mathcal H_L\), since they change total degree differently. By the radial kernel identity,
\[
\operatorname{Tr}_{\mathcal H_L}(M_{f_k}^*M_{f_k})
=\sum_{|\alpha|=L}\|f_ke_\alpha\|^2
=B_L\frac{m_{L+k}}{m_L}a_k.
\]
The trace of \(M_{f_k}M_{f_k}^*\) on \(\mathcal H_L\) is the same expression with degree \(L-k\) when \(L\ge k\), and vanishes otherwise, because \(M_{f_k}\) maps \(\mathcal H_{L-k}\) to \(\mathcal H_L\). Summing over \(0\le L\le M\) telescopes to the finite-cutoff identity. For bounded \(f\), the relevant series are absolutely convergent after aggregation (each trace is finite and both positive component traces are bounded), justifying passage from polynomial symbols to general bounded holomorphic symbols.

**Moment concentration and limit.** Let \(R=|z|\), with essential supremum \(1\). The probability law tilted by \(R^{2L}\) concentrates at \(R=1\) as \(L\to\infty\): for each \(0<r<s<1\) having positive original mass at \(R\ge s\), the tilted mass at \(R\le r\) is at most \(\nu(R\le r)(r/s)^{2L}/\nu(R\ge s)\). Therefore, for every fixed integer \(k\ge1\), \(m_{L+k}/m_L\to1\). Also \(0\le m_{L+k}/m_L\le1\), since \(R\le1\).

For fixed \(k\), the \(k\) surviving terms have \(L=M,M-1,\ldots,M-k+1\) when \(M\ge k-1\), and \(B_{M-j}/B_M\to1\) for each fixed \(j\). Hence the normalized inner sum tends to \(k\). For all \(k,M\) the same sum is bounded by \(\min\{k,M+1\}\le k\). Dominated convergence proves the claimed limit when \(\sum k a_k\) is finite; Fatou's lemma proves the extended-real version when it is infinite. Since \(B_M\to\infty\) for \(d\ge2\), every \(f\) with \(\mathcal E_{\partial}(f)>0\) yields a non-Hilbert–Schmidt Hankel operator. The energy is zero exactly for constants, by orthogonality of the homogeneous decomposition.

**Coordinate example.** For \(\nu_t\), \(m_q=(d)_q/(d+t+1)_q\) and \(a_1=1/d\); all other positive-degree \(a_k\) vanish. Substitution leaves only the \(L=M\) shell and gives \(T_M=B_M(M+d)/(d(M+d+t+1))=\binom{M+d}{d}/(M+d+t+1)\), as stated.

## Verification

The accompanying standalone Python checker constructs monomial norms directly and compares a direct basiswise commutator trace with the independent boundary-shell expression. It passed 930 exact rational/numerical assertions across dimensions \(1,2,3\); ball power-weights, sphere measure, and a singular mixture of spheres; and symbols with multiple homogeneous components. Further exact checks test the closed coordinate formula through dimension \(5\), as well as large-cutoff asymptotics. These checks concern finitely many inputs and are not a substitute for the proof above. Run \(`python CHECK.py`\) with Python 3 and the standard library only.

## Relationship to prior work

Clos's 2026 theorem establishes Hilbert–Schmidt rigidity for smooth harmonic symbols on smooth bounded strongly pseudoconvex domains in dimension at least two. The preceding Arazy–Fisher–Janson–Peetre results treat Schatten-ideal membership for standard weighted Bergman spaces; Engliš–Guo–Zhang and Engliš treat Dixmier traces of **different, critical-power** Hankel/Toeplitz commutator products. Tang–Wang–Zheng investigate trace formulas under trace-class hypotheses. The present claim is instead the **exact first-power, total-degree compressed trace** for arbitrary unitary-radial measures, together with the weight-independent boundary-energy limit. The classical dimension-one Hilbert–Schmidt identity is acknowledged rather than rebranded as new. No claim of exhaustive priority or independent mathematical certification is made.

## Limitations

The universal asymptotic needs radial essential supremum exactly \(1\) and unitary invariance; it does not apply as stated to nonradial domains, non-unitarily-invariant weights, general unbounded analytic symbols, or arbitrary nonhomogeneous cutoff sequences. The trace is a **basis/spectral-cutoff** trace, not the unordered sum of the first \(N\) singular values and not a Dixmier trace. The literature comparison is incomplete for inaccessible full texts of Arazy et al. (1991) and older weighted-Hankel sources. This is a self-review, with no independent audit.

## References

1. Timothy G. Clos, *Hilbert-Schmidt Hankel operators with harmonic symbols on the Bergman space of strongly pseudoconvex domains in \(\mathbb C^n\)*, arXiv:2603.25483 (first posted 2026-03-26), Proc. Amer. Math. Soc. 154 (2026), 4811–4822.
2. J. Arazy, S. D. Fisher, S. Janson and J. Peetre, *Membership of Hankel operators on the ball in unitary ideals*, J. London Math. Soc. 43 (1991), 485–508, DOI: 10.1112/jlms/s2-43.3.485.
3. M. Engliš, K. Guo and G. Zhang, *Toeplitz and Hankel operators and Dixmier traces on the unit ball*, arXiv:0707.2025 (2007), Proc. Amer. Math. Soc. 137 (2009), 3669–3678.
4. M. Engliš, *Hankel operators and the Dixmier trace on strictly pseudoconvex domains*, Doc. Math. 15 (2010), 601–622, DOI: 10.4171/DM/308.
5. X. Tang, Y. Wang and D. Zheng, *Trace Formula of Semicommutators*, arXiv:2210.04148 (2022).
