# Opposite optimal orderings for three-edge weighted gossip

## Finding

Let \(K_{1,3}\) have hub \(0\), leaves \(1,2,3\), and three fixed update parameters \(p_i\in(0,1)\). At one contact on edge \((0,i)\), both endpoints take the convex combinations \(x_0^+=(1-p_i)x_0+p_ix_i\) and \(x_i^+=p_ix_0+(1-p_i)x_i\). Apply each of the three contacts exactly once, in a selectable temporal order \(\pi=(i,j,k)\), and write its resulting four-by-four matrix as \(T_\pi\). Define the mean projection \(J=\mathbf{1}\mathbf{1}^{\mathsf T}/4\), the isotropic centered squared error \(E_\pi=\|T_\pi-J\|_F^2\), and the squared worst-case centered error \(W_\pi=\|T_\pi-J\|_2^2\).

**Complete opposite-ordering theorem.** Every order with a *largest* parameter in the middle position minimizes \(E_\pi\), and these are all the minimizers. Every order with a *smallest* parameter in the middle position minimizes \(W_\pi\), and these are all the minimizers. For three distinct parameters there are exactly two minimizers of each objective, with disjoint optimal sets. For equal parameters, the stated maximum/minimum selection rule includes all ties. All six \(T_\pi\) have the same characteristic polynomial, hence the same asymptotic spectral convergence factor despite their potentially different one-sweep errors.

A stronger exact comparison holds for arbitrary \(a,b,c\in(0,1)\), assigned to the same three distinct leaves:
\[
E_{(a,b,c)}-E_{(a,c,b)}=4abc(1-a)(c-b).
\]
The subscript denotes the three chronological contact weights, not repeated contact on a leaf. In particular, the above comparison is strictly signed whenever \(b\ne c\).

## Assumptions and scope

The graph is exactly the four-vertex star. Every parameter is fixed and belongs to \((0,1)\); the six permutations are the only admissible schedules. The graph update is a doubly stochastic symmetric convex combination; in particular its heat-edge realization \(P_i=\exp[-\tau w_i(e_0-e_i)(e_0-e_i)^{\mathsf T}]\) has \(p_i=(1-e^{-2\tau w_i})/2\in(0,1/2)\). The mean-square metric corresponds to unit covariance on the three-dimensional mean-zero subspace, up to an irrelevant normalization factor. The worst-case metric is a squared Euclidean operator norm on that same subspace, not the spectral radius of the nonnormal product.

## Proof

**1. Matrix and first-error identity.** Write \(v_i=e_0-e_i\) and \(P_i=I-p_iv_iv_i^{\mathsf T}\). Then \(v_i^{\mathsf T}v_i=2\), while \(v_i^{\mathsf T}v_j=1\) for distinct leaves. The chronological \((a,b,c)\) product is \(T=P_cP_bP_a\), and \(E=\operatorname{tr}(T^{\mathsf T}T)-1\) since \(T\) is doubly stochastic. Put \(h(q)=2q(1-q)\). The norm-loss identity \(I-P_i^2=h(p_i)v_iv_i^{\mathsf T}\) gives
\[
\begin{aligned}
E_{(a,b,c)}={}&3-4a(1-a)\\
&-2b(1-b)\{2-2a(1-a)\}\\
&-2c(1-c)\{2-2b(1-b)-2a(1-a)(1-b)^2\}.
\end{aligned}
\]
Indeed \(\|v_a\|^2=2\), \(\|P_av_b\|^2=2-2a(1-a)\), and \(\|P_aP_bv_c\|^2=2-2b(1-b)-2a(1-a)(1-b)^2\). Subtraction after interchanging \(b,c\) yields exactly \(4abc(1-a)(c-b)\). Reversing a sequence transposes its product, so preserves its Frobenius and operator norms. Reversal identifies the six permutations in three pairs, one per middle weight. Hence \(E\) strictly decreases as the chosen middle parameter increases, establishing its complete optimizer set, including ties.

**2. Two order-independent singular-value invariants.** Restrict the positive semidefinite matrix \(S=T^{\mathsf T}T\) to \(H=\mathbf{1}^{\perp}\), and denote its eigenvalues by \(1>\mu_1\ge\mu_2\ge\mu_3\ge0\). Strictly less than one follows from the fact that equality of norms at every positive edge contact forces the input to agree across all three star edges; a vector in \(H\) satisfying this is zero. The determinant is
\[
U:=\mu_1\mu_2\mu_3=\det(T|_H)^2=\prod_{i=1}^3(1-2p_i)^2.
\]
Now let \(T_0=I\), \(T_k=P_{\pi(k)}T_{k-1}\), and \(u_k=T_{k-1}^{\mathsf T}v_{\pi(k)}\). A telescoping loss gives
\[
I-T^{\mathsf T}T=\sum_{k=1}^3h(p_{\pi(k)})u_ku_k^{\mathsf T}.
\]
Each \(u_k\) is its current edge vector plus a linear combination of *earlier* edge vectors; the change-of-basis matrix from the ordered independent star-edge vectors to the ordered \(u_k\) is triangular with diagonal one. The Gram matrix of \(v_1,v_2,v_3\) is \(I_3+\mathbf{1}_3\mathbf{1}_3^{\mathsf T}\) of determinant four. Taking the determinant on \(H\) therefore proves the second order-independent invariant
\[
V:=\prod_{j=1}^3(1-\mu_j)=4\prod_{i=1}^3h(p_i)=32\prod_{i=1}^3p_i(1-p_i)>0.
\]
This calculation holds even if some \(p_i=1/2\), when \(U=0\).

**3. The isotropic and worst-case objectives order in opposite ways.** Write \(R=\mu_1=W\) and \(E=\mu_1+\mu_2+\mu_3\). The two fixed invariants imply
\[
E=f(R):=1+R+\frac{U}{R}-\frac{V}{1-R},\qquad 0<R<1.
\]
Since each \(\mu_j/(1-\mu_j)\le R/(1-R)\), one has \(R\ge r_0:=U^{1/3}/(U^{1/3}+V^{1/3})\), taking \(r_0=0\) when \(U=0\). Direct differentiation shows
\[
f''(r)=\frac{2U}{r^3}-\frac{2V}{(1-r)^3}\le0\quad(r\ge r_0).
\]
At every feasible largest eigenvalue \(R\), substitution of the remaining two eigenvalues into the derivative gives
\[
f'(R)=-\frac{(R-\mu_2)(R-\mu_3)}{R(1-R)}\le0.
\]
As \(f'\) is nonincreasing beyond each feasible \(R\), and is strictly decreasing immediately unless the two invariants both vanish (impossible because \(V>0\)), \(f\) is *strictly decreasing between any two different feasible largest eigenvalues*. Thus a strictly larger isotropic error \(E\) corresponds to a strictly smaller worst-case error \(W\). By Step 1, the worst-case minimizing middle weight must consequently be the *smallest*, with exactly the stated tie behavior.

**4. Characteristic-polynomial equality and minimality.** A cyclic permutation of three matrix factors leaves their product characteristic polynomial invariant by \(\det(\lambda I-AB)=\det(\lambda I-BA)\); reversing the three factors transposes the product since every factor is symmetric. Cyclic rotation and reversal generate all six orders, proving the claim about asymptotic spectra for arbitrary parameters, including singular factors. For a star with only two leaves, its two contact orders are reversals, and their products are transposes; both one-sweep metrics are consequently equal. Thus the four-vertex star is the smallest star that can exhibit the opposed optimizer phenomena.

## Verification

The accompanying `verify.py` reconstructs the update matrices, checks the symbolic comparison identity, the two determinant invariants and the common characteristic polynomial on a rational example, and tests the two opposite optimizer sets over an additional finite collection of rational parameters. All symbolic identities are checked with exact arithmetic. The finite tests supplement, but do not replace, the proof for arbitrary real parameters.

For \((p_1,p_2,p_3)=(1/8,1/4,3/8)\), the three distinct isotropic-error values for middle-weight choice \(1/8,1/4,3/8\), respectively, are
\[
\frac{19565}{16384},\qquad\frac{19505}{16384},\qquad\frac{19421}{16384}.
\]
The corresponding squared worst-case errors are approximately \(0.707412275846\), \(0.711765397805\), and \(0.717426466762\), in the opposite order of preference. Exact characteristic polynomials and rational checks are built into the verifier.

## Relationship to prior work

Deterministic minimal-complete gossip on trees has a classical order-invariant *spectral-rate* law; the 2011 treatment by Liu, Mou, Morse, Anderson and Yu studies that asymptotic behavior. Mangoubi, Mou, Liu and Morse (2013) optimize a common convex-combination parameter for periodic gossip, including stars, rather than optimizing finite-horizon singular and Frobenius criteria over independently prescribed heterogeneous edge parameters. Lu, Morse, Anderson and Yu (2010) establish the strict Euclidean contraction property of complete gossip sequences and explicitly raise the question of selecting sequences with the smallest singular-value contraction; they do not give this three-edge optimizer classification. Shi, Li, Johansson and Johansson (initially public 2012) study exact *finite-time consensus*, a different objective. These differences distinguish this result from those identified statements, but do not constitute a proof that no equivalent unpublished or unindexed theorem exists.

## Limitations

The theorem concerns exactly one contact per edge on the three-leaf star, and fixed positive contact strengths; it does not classify arbitrarily long schedules, general trees, other initial covariance models, non-Euclidean losses, or freely chosen contact strengths. Equality of the asymptotic eigenvalue spectra is not equality of the one-sweep singular values. The literature comparison is not a formal priority certificate, and no independent mathematical audit is claimed.

## References

1. G. Shi, B. Li, M. Johansson, and K. H. Johansson, *Finite-time Convergent Gossiping*, arXiv:1206.0992, initial public submission 2012-06-05, https://arxiv.org/abs/1206.0992.
2. O. Mangoubi, S. Mou, J. Liu, and A. S. Morse, *Towards Optimal Convex Combination Rules for Gossiping*, American Control Conference (2013), DOI 10.1109/ACC.2013.6580009, https://doi.org/10.1109/ACC.2013.6580009.
3. J. Liu, S. Mou, A. S. Morse, B. D. O. Anderson, and C. Yu, *Deterministic Gossiping*, Proceedings of the IEEE 99 (2011), DOI 10.1109/JPROC.2011.2159689, https://doi.org/10.1109/JPROC.2011.2159689.
4. J. Lu, A. S. Morse, B. D. O. Anderson, and C. Yu, *The Contraction Coefficient of a Complete Gossip Sequence*, 2010, DOI 10.1007/978-3-642-11278-2_19, https://doi.org/10.1007/978-3-642-11278-2_19.
