# A two-law quantum Kac return spectrum for every rank-one qubit-bond projection

## Finding

Let \(\alpha\) be the bilateral shift on the tracial qubit spin chain and let \(p_\psi\) be a rank-one projection associated with a unit two-qubit vector \(\psi\). The spectral distribution of the projection-lattice first-return observable is determined by precisely two cases. For every integer \(m\geq0\), its normalized spectral survival probability is

\[
\tau_{p_\psi}\bigl(\mathbf 1_{[m+1,\infty)}(T_{p_\psi})\bigr)
=\begin{cases}
F_{m+1}/2^m,&\psi=u\otimes u\text{ for some unit }u,\\
(m+1)/2^m,&\text{otherwise},
\end{cases}
\]

where \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). In the second case, the point masses are \(\tau_{p_\psi}(\mathbf 1_{\{k\}}(T_{p_\psi}))=(k-1)/2^k\) for every \(k\geq1\). In the exceptional case, they are \(1/2\) at \(k=1\), zero at \(k=2\), and \(F_{k-2}/2^k\) at every \(k\geq3\). Both distributions have mean \(4\); their variances are respectively \(20\) (exceptional) and \(4\) (otherwise). Thus the full spectral law is constant on the complement of the projective diagonal-product locus, and discontinuous at every point of that locus as a function of the local projection in operator norm.

Equivalently, the probability-generating functions in the generic and exceptional cases are, respectively,

\[
G_{\mathrm{gen}}(z)=\frac{z^2}{(2-z)^2},\qquad
G_{\mathrm{exc}}(z)=\frac{z(z-2)}{z^2+2z-4},\qquad |z|\leq1.
\]

## Assumptions and scope

Let \(\mathcal M=\overline{\bigotimes}_{j\in\mathbb Z}(M_2(\mathbb C),\operatorname{tr}_2)\) be the weak von Neumann completion, equipped with the product normalized trace \(\tau\); it is the tracial hyperfinite factor. Fix the shift convention \(\alpha(p_{j,j+1})=p_{j+1,j+2}\). For a unit vector \(\psi\in\mathbb C^2\otimes\mathbb C^2\), the projection \(p=p_\psi=|\psi\rangle\langle\psi|\) acts on sites \(0,1\), and \(\tau(p)=1/4\). Set \(s_0=0\), \(s_m=\bigvee_{j=1}^m\alpha^j(p)\), \(t_m=p-(p\wedge s_{m-1})\) for \(m\geq1\), \(f_m=t_m-t_{m+1}\), and \(T_p=\sum_{m\geq1}m f_m\). These are exactly the projection-lattice first-return objects of Amrutam--Saha--Wang, not the first-detection statistics of repeated projective measurements. The normalized trace on the corner is \(\tau_p(x)=4\tau(x)\).

The shift is strongly mixing on local observables and hence ergodic; its first-return projections sum to \(p\), so the above spectral law is a probability measure. All formulas quantify over every normalized two-qubit vector and every positive integer spectral value; no commutativity of shifted local projections is required.

## Proof

**1. Return tails are consecutive-bond constraint ranks.** For \(L\geq1\), define \(G_L(\psi)\subseteq(\mathbb C^2)^{\otimes L}\) as the simultaneous kernel of the rank-one projections \(p_{j,j+1}\) for \(0\leq j\leq L-2\), and put \(g_L=\dim G_L\). Also \(g_1=2\). On the finite tensor block \(0,\ldots,m+1\), the complement \(Q_m=1-s_m\) has image \(\mathbb C^2\otimes G_{m+1}\), of dimension \(2g_{m+1}\). The kernel of the restricted local projection \(p|_{\operatorname{ran}Q_m}\) is exactly \(G_{m+2}\). Therefore

\[
\operatorname{rank}(pQ_m)=2g_{m+1}-g_{m+2}.
\]

For two orthogonal projections \(P,Q\) on a finite-dimensional Hilbert space, \(\operatorname{rank}(PQ)=\operatorname{rank}(P)-\dim(\operatorname{ran}P\cap\ker Q)\). Since \(t_{m+1}=p-(p\wedge s_m)\) and \(\ker Q_m=\operatorname{ran}s_m\), this identity gives \(\operatorname{rank}(t_{m+1})=\operatorname{rank}(pQ_m)\), even when \(p\) and \(s_m\) do not commute. After normalization by the trace of \(p\),

\[
\tau_p(t_{m+1})=\frac{2g_{m+1}-g_{m+2}}{2^m}.
\]

**2. Classify the chain-kernel dimensions.** Write the two-qubit covector as the bilinear matrix \(C=(\overline{\psi}_{ab})_{a,b\in\{0,1\}}\). If \(\psi\) is entangled, \(C\) is invertible. With \(\varepsilon=\begin{psmallmatrix}0&1\\-1&0\end{psmallmatrix}\), choose \(U_0=I_2\) and recursively choose invertible \(U_{j+1}=C^{-1}U_j^{-\mathsf T}\varepsilon\). Then \(U_j^{\mathsf T}CU_{j+1}=\varepsilon\) on every bond, so the invertible tensor product \(\bigotimes_j U_j\) carries the common kernel of the adjacent antisymmetric covectors to \(G_L(\psi)\). The former common kernel is the symmetric tensor power \(\operatorname{Sym}^L(\mathbb C^2)\): annihilation by each adjacent antisymmetric covector is equivalent to invariance under each adjacent transposition. Consequently \(g_L=L+1\).

If \(\psi=u\otimes v\) is a product with linearly independent factors, there is a single invertible matrix \(W\) whose covector evaluations satisfy \(\langle u|W=\langle0|\) and \(\langle v|W=\langle1|\). The tensor product \(W^{\otimes L}\) maps the kernel of each forbidden \(|01\rangle\) bond to the corresponding kernel for \(\psi\). The binary words avoiding \(01\) are precisely \(1^a0^{L-a}\), for \(0\leq a\leq L\), so again \(g_L=L+1\).

Finally, when \(\psi=u\otimes u\), the same local unitary on each site takes the forbidden bond to \(|00\rangle\). The binary words avoiding \(00\) obey the Fibonacci recurrence with initial dimensions \(g_1=2\) and \(g_2=3\), giving \(g_L=F_{L+2}\). These three mutually exclusive cases exhaust every nonzero two-qubit vector, including degenerate product vectors and entangled vectors of arbitrary Schmidt coefficients.

**3. Obtain the entire law and moments.** Inserting \(g_L=L+1\) into the rank formula yields \(\tau_p(t_{m+1})=(m+1)/2^m\). Inserting \(g_L=F_{L+2}\) gives \(\tau_p(t_{m+1})=F_{m+1}/2^m\). Since \(f_k=t_k-t_{k+1}\) and the tails vanish, consecutive differences give the stated masses. Summing the absolutely convergent geometric and Fibonacci series yields the two displayed generating functions. Differentiation at \(z=1\) gives mean \(4\) and variances \(4\) and \(20\), respectively; this also matches the noncommutative Kac mean identity \(\tau_p(T_p)=1/\tau(p)=4\).

**4. Discontinuity and exact boundary.** The entangled vectors \(\psi_\eta=(|00\rangle+\eta|11\rangle)/\sqrt{1+\eta^2}\), for \(\eta>0\), tend to \(|00\rangle\) as \(\eta\downarrow0\), and their rank-one projections converge in operator norm. Nevertheless \(\tau_{p_{\psi_\eta}}(f_1)=0\) for every positive \(\eta\), while \(\tau_{p_{|00\rangle}}(f_1)=1/2\). Therefore even the mass at a single isolated spectral point jumps; no continuous extension of the law to that locus is possible.

## Verification

The standalone `VERIFY.py` builds the finite adjacent-bond annihilation matrices from tensor products and checks \(g_L\) and the rank-tail identities for five representative states, including the singlet, a Bell state, independent product factors, an exceptional parallel product, and an entangled perturbation of it, for lengths up to seven. It also independently checks normalization and the first two moments by convergent finite truncation. It returned `QUANTUM_KAC_FINITARY_CHECK_OK 71`. All infinite-dimensional claims follow from the proof above; these finite checks are supplementary rather than exhaustive certificates.

## Relationship to prior work

Amrutam, Saha, and Wang (arXiv:2611.16972v1, 12 November 2026) introduce the projection-lattice return observable and prove its mean identity for ergodic finite von Neumann dynamical systems. Their Section 3, including equations (3.1)--(3.3), Proposition 3.1, Theorem 3.3, and Remarks 3.5, was compared directly: it does not give the spectral measures for two-site rank-one Bernoulli projections or the sharp exceptional locus. Laumann, Moessner, Scardicchio, and Sondhi (arXiv:0903.1904, Section III.1) already establish the generic \(L+1\) ground-space dimension for rank-one quantum satisfiability constraints on trees. That ground-space result is used here as context; it does not classify the projection-lattice return spectrum or its variance and discontinuity. The proof above also covers singular product constraints without asserting that the generic kernel count itself is new. Sinkovicz, Kiss, and Asbóth (2016) examine a different repeated-measurement quantum recurrence model, not the lattice spectral law computed here.

## Limitations

The complete dichotomy is for spin dimension two, a single repeated rank-one two-site projector, the tracial product state, and the projection-lattice (not measurement) return operator. It does not classify arbitrary local projection ranks, longer words, correlated states, or nontracial shifts. No uniqueness or bibliographic exhaustiveness is inferred merely from searches; an older equivalent presentation in quantum-constraint or operator-algebra language remains possible. The finite checker is not an infinite-dimensional proof. The result is not independently audited.

## References

1. T. Amrutam, D. Saha, X. Wang, *Kac lemma on noncommutative probability spaces*, arXiv:2611.16972v1 (first publicly posted 12 November 2026), https://arxiv.org/html/2611.16972v1. Specifically Section 3, equations (3.1)--(3.3), Proposition 3.1, Theorem 3.3 and Remark 3.5.
2. C. R. Laumann, R. Moessner, A. Scardicchio, S. L. Sondhi, *Phase Transitions and Random Quantum Satisfiability*, arXiv:0903.1904 (2009), https://arxiv.org/abs/0903.1904, Section III.1.
3. P. Sinkovicz, T. Kiss, J. K. Asbóth, *Generalized Kac lemma for recurrence time in iterated open quantum systems*, Phys. Rev. A 93, 050101(R) (2016), https://doi.org/10.1103/PhysRevA.93.050101.
