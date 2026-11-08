# Sharp negative-type threshold for three-capped matrix rank distance in dimension at least four

## Finding

Fix a prime power \(q\ge2\), integers \(4\le m\le n\), and the additive matrix space \(V=M_{m,n}(\mathbb F_q)\). Equip \(V\) with the **three-capped rank metric**
\[
\rho(X,Y)=\min\{\operatorname{rank}(X-Y),3\}.
\]
Put \(M=q^m\), \(N=q^n\), \(U=(M-1)/(q-1)\), and
\[
A=N-U,\qquad
B=\frac{(M-q)\bigl((q^2-1)N-q(M-1)\bigr)}{q(q-1)^2(q+1)}.
\]
Then \(A>0\), \(B>2A+3\), and the function
\[
\Phi(p)=A-B2^p+(B-A-1)3^p
\]
has exactly one positive zero, \(\beta\), which lies in \((0,1)\). For \(p>0\), the metric \(\rho\) has \(p\)-negative type **if and only if** \(p\le\beta\), and strict \(p\)-negative type precisely for \(0<p<\beta\).

The critical zero-sum Fourier eigenspace at \(p=\beta\) consists **exactly** of additive characters indexed by matrices of rank \(m-1\); its dimension is
\[
\mu=\frac{q^m-1}{q-1}\prod_{i=0}^{m-2}(q^n-q^i).
\]
Consequently, the smallest Euclidean dimension for an isometric embedding of \((V,\rho^{p/2})\) is \(q^{mn}-1\) when \(0<p<\beta\), and \(q^{mn}-1-\mu\) at \(p=\beta\). For fixed \(q,m\) and \(n\to\infty\), with \(L=(q^m-q)/(q(q-1))\),
\[
q^n\beta\longrightarrow\frac{1}{L\log(3/2)-\log3}.
\]
In particular, the dangerous Fourier rank is independent of the exponent for **every** \(p>0\), not only near the threshold.

## Assumptions and scope

The field is any finite field of prime-power cardinality, including characteristic two. Rows and columns are ordered so that \(4\le m\le n\). The additive Fourier transform uses any fixed nontrivial character of \((\mathbb F_q,+)\) and the nondegenerate coordinate trace pairing. Negative type means that \(\sum_{X,Y}a_Xa_Y\rho(X,Y)^p\le0\) for all real coefficients with \(\sum_Xa_X=0\). The exponent \(p=0\) has the conventional discrete-metric limiting interpretation and is not needed for the asserted positive threshold. The metric is bounded by three even though the underlying matrix rank can exceed three; therefore this theorem is not a restatement of the uncapped rank metric in matrix spaces of rank diameter three.

## Proof

**1. Rank-one and rank-two Fourier eigenvalues.** Let \(R_j\) be convolution by the indicator of the matrices of rank \(j\). For any nontrivial additive Fourier character of dual matrix rank \(s\in\{1,\dots,m\}\), writing \(k_s\) for its \(R_1\)-eigenvalue, summation over rank-one decompositions \(uv^{\mathsf T}\) (each counted \(q-1\) times) gives
\[
k_s=\frac{q^{m+n-s}-q^n-q^m+1}{q-1}.
\]
The rank-one valency is \(v_1=(q^m-1)(q^n-1)/(q-1)\). For a specified rank-one matrix, there are exactly \(c_1=q^m+q^n-q-2\) ordered decompositions into two nonzero rank-one summands: the summands share either its row or its column line. For a specified rank-two matrix there are exactly \(c_2=q(q+1)\) such decompositions: on its two-dimensional row and column spaces these correspond to rank-one \(uv^{\mathsf T}\) with \(v^{\mathsf T}u=1\). No larger rank can be a sum of two rank-one matrices. Thus the exact convolution identity is
\[
R_1^2=v_1I+c_1R_1+c_2R_2,
\]
and the \(R_2\)-eigenvalue on rank-\(s\) characters is
\[
h_s=\frac{k_s^2-c_1k_s-v_1}{q(q+1)}.
\]
These formulas are valid over arbitrary finite fields, without a characteristic restriction.

**2. Fourier spectrum of the capped powered distance.** For \(p>0\), the kernel \(\rho(Z,0)^p\) equals \(1\) on rank one, \(2^p\) on rank two, and \(3^p\) on every matrix of rank at least three. As the sum of any nontrivial additive character over all matrices vanishes, its Fourier multiplier is exactly
\[
\Lambda_s(p)=(1-3^p)k_s+(2^p-3^p)h_s-3^p.
\]
The powered distance kernel is conditionally negative semidefinite if and only if every \(\Lambda_s(p)\le0\) for \(s\ge1\).

**3. Unique maximal nonconstant multiplier.** Set \(E_p=3^p-2^p>0\) and \(R_p=(3^p-1)/E_p\). The elementary function \(2\cdot3^p-3\cdot2^p+1\) vanishes at zero and has positive derivative for every \(p\ge0\), so \(R_p<3\). For two rank-one eigenvalues \(k>k'\), the difference of their capped-distance multipliers is
\[
\Lambda(k)-\Lambda(k')=-E_p(k-k')\left(\frac{k+k'-c_1}{q(q+1)}+R_p\right).
\]
Write \(H=M+2U-q-2\). Since \(m\ge4\), the weaker bound \(m\ge3\) suffices for \(H\ge3q(q+1)\): at \(m=3\), \(H=q(q+1)^2\). Now \(k_{m-1}=N-U\) and \(k_m=-U\), so \(c_1-(k_{m-1}+k_m)=H\). The difference formula and \(R_p<3\) show \(\Lambda_{m-1}(p)>\Lambda_m(p)\).

For any \(s\le m-2\), monotonicity of the \(k_s\) gives
\[
k_s+k_{m-1}-c_1\ge(q+1)N-H\ge qM-2U+q+2>0.
\]
Here \(U\le M-1\) and \(N\ge M\). The same difference formula shows \(\Lambda_{m-1}(p)>\Lambda_s(p)\). Thus **the unique maximal nontrivial Fourier shell is rank \(m-1\) for every \(p>0\)**.

**4. Existence and uniqueness of the threshold.** Substituting \(s=m-1\) in the preceding formulas yields \(k_{m-1}=A\) and \(h_{m-1}=-B\), hence \(\Lambda_{m-1}(p)=\Phi(p)\). Put \(L=(M-q)/(q(q-1))\) and \(T=(M-q)(M-1)/((q-1)^2(q+1))\). Then \(B=LN-T\) and \(L\ge q+1>2\). Consequently \(B-2A-3=(L-2)N-T+2U-3\) increases with \(N\) and is smallest at \(N=M\).

For \(N=M\), writing \(z=M-q^3\ge0\), direct algebra gives
\[
B-2A-3=(q-1)(q^3-q^2+1)+\frac{2q^3-2q^2-q+2}{q^2-1}z+\frac{q^2-q-1}{q(q-1)^2(q+1)}z^2>0.
\]
All displayed coefficients are positive for integer \(q\ge2\), so the inequality holds for all permitted parameters. In particular \(B-A-1>0\). Moreover \(\Phi(0)=-1\), \(\Phi(1)=B-2A-3>0\), and
\[
2^{-p}\Phi(p)=A2^{-p}+(B-A-1)(3/2)^p-B
\]
is strictly convex on the real line. Its nonpositive set on \([0,\infty)\) is therefore precisely \([0,\beta]\), with one crossing \(\beta\in(0,1)\). By step 3 this is the exact negative-type range, with strictness below the endpoint.

**5. Nullspace, embedding dimension and asymptotic.** At \(p=\beta\) all positive-rank Fourier multipliers other than those of rank \(m-1\) are strictly negative. The number of rank-\(m-1\) dual matrices is the stated \(\mu\), using the standard finite-field rank count. The centered Gram matrix associated with \(\rho^p\) is \(-\tfrac12 J D_pJ\), so its rank is \(q^{mn}-1\) in the strict regime and \(q^{mn}-1-\mu\) at the endpoint. Finally, at fixed \(q,m\) the derivative \(\Phi'(0)\) equals \(q^n\bigl(L\log(3/2)-\log3\bigr)+O_{q,m}(1)\), whose leading constant is positive since \(L\ge3\). A Taylor expansion with the proved unique root gives \(\beta\sim 1/[q^n(L\log(3/2)-\log3)]\).

## Verification

The standalone script `verify.py` independently constructs all \(2^{16}\) binary Fourier characters for \(4\)-by-\(4\) matrices, computes the complete rank-one and rank-two convolution spectra by a Walsh transform, and compares both against the two formulas above for each dual rank. It also exhaustively counts rank-one two-step decompositions and checks the predicted critical Fourier rank and root on \(36\) additional prime-power parameter triples (\(q\in\{2,3,4,5\}\), \(m\in\{4,5,6\}\), \(n\in\{m,m+1,m+3\}\)). Reproduction: run `python verify.py` with NumPy installed. This finite check does not establish the all-parameter claim; the proof is the infinite-family argument above.

For \(q=2\), \(m=n=4\), the root is approximately \(0.0634878683033\). Its zero-sum endpoint Fourier nullity is \(15(15)(14)(12)=37800\) and its least Euclidean embedding dimension is \(27735\).

## Relationship to prior work

Delsarte (1978) develops the bilinear-forms association scheme and derives its full generalized Krawtchouk character table; the first two entries are used here as foundations, not claimed as new. Sánchez (2011) supplies general finite-metric negative-type criteria, not this family-wide optimizing Fourier rank. Van Dam–Koolen–Tanaka (2014/2016) identify bilinear forms graphs as the matrix-rank analogue of Hamming graphs. Brouwer–Cioabă–Ihringer–McGinnis (2017/2018) optimize eigenvalues of **single** distance-relation graphs, not the exponent-dependent capped-distance combination. The previously studied uncapped rank distance when one matrix dimension equals three lacks rank-four differences and does not establish the capped-distance theorem for \(m\ge4\).

The asserted result is the universal critical Fourier shell, exact exponent, endpoint multiplicity and high-aspect-ratio law for the genuinely capped higher-rank setting. In particular, the theorem is not a claim of novelty for the Krawtchouk formulas or the general Schoenberg criterion.

## Limitations

The claim concerns the cap equal to three, unweighted matrix ranks, \(m\ge4\), and finite fields. Different truncation radii, non-field matrix rings, and arbitrary rank-dependent weights are unaddressed. No independent validation or comprehensive historical-priority certification is asserted; existing general spectral formulas could implicitly yield some deductions after additional optimization.

## References

1. P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, J. Combin. Theory A **25** (1978), 226–241. DOI: 10.1016/0097-3165(78)90015-8. Original full text, especially §2 and Appendix, inspected.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first posted 2011-08-02. Introduction, Theorem 2.3 and §3 inspected.
3. E. R. van Dam, J. H. Koolen, H. Tanaka, *Distance-regular graphs*, arXiv:1410.6294, first posted 2014-10-23; §3.1 inspected.
4. A. E. Brouwer, S. M. Cioabă, F. Ihringer, M. McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, arXiv:1709.09011, first posted 2017-09-26; introduction and §7 inspected.
