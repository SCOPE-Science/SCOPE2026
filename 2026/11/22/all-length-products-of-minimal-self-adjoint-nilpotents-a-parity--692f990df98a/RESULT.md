# All-length products of minimal self-adjoint nilpotents: a parity-switching polar-space fiber law

## Finding
Let \(q\) be any odd prime power, \(r\ge2\), and \(V\) a \((2r+1)\)-dimensional vector space over \(\mathbb F_q\) with a nondegenerate symmetric bilinear form \(B\). Put
\[
\mathcal N_B=\{T\in\operatorname{End}(V):T\ne0,\ \operatorname{rank}T=1,\ T^2=0,\ B(Tx,y)=B(x,Ty)\}.
\]
Let \(\mathcal P\) be the set of isotropic projective lines \(L\subseteq V\), and choose a nonzero representative \(u_L\) on each such line. Write
\[
N=\frac{q^{2r}-1}{q-1},\qquad K=q^{2r-1},\qquad D=q^{2r-2}.
\]
Then \(|\mathcal P|=N\) and \(|\mathcal N_B|=(q-1)N\). For every \(k\ge2\), the exact number of ordered factorizations of every prescribed \(Z\in\operatorname{End}(V)\) as a product of \(k\) elements of \(\mathcal N_B\) is as follows:

* If \(Z=0\), the fiber has size
\[
F_k(0)=(q-1)^k\bigl(N^k-NK^{k-1}\bigr).
\]
* If \(Z\ne0\) is not a rank-one operator with both its image line and its \(B\)-identified coimage line isotropic, then \(F_k(Z)=0\).
* Otherwise write uniquely \(Z=c\,u_L B(u_M,\cdot)\) for some \(L,M\in\mathcal P\) and \(c\in\mathbb F_q^\times\). Put \(\ell=k-1\) and \(t=\lfloor\ell/2\rfloor\). Then
\[
\boxed{F_k(Z)=(q-1)^{k-1}H_\ell(L,M)},
\]
where
\[
\boxed{H_{2t}(L,M)=D^t\mathbf1_{L=M}+\frac{K^{2t}-D^t}{N}}\quad(t\ge1)
\]
and
\[
\boxed{H_{2t+1}(L,M)=D^t\mathbf1_{B(u_L,u_M)\ne0}+\frac{K^{2t+1}-D^tK}{N}}\quad(t\ge0).
\]
The fractions here are integers. Thus the prescribed nonzero fiber alternates between two different natural partitions: **odd factor lengths distinguish equal versus distinct endpoint lines**, whereas **even factor lengths distinguish nonorthogonal versus orthogonal endpoints**.

Every nonzero target in the stated rank-one isotropic-endpoint class is a product of **three** factors. Two factors suffice exactly when the target has nonzero trace; no other nonzero target can be a product of any length. In particular, three is the sharp universal nonzero product width within this natural image class.

If the factors are independent and uniform in \(\mathcal N_B\), then
\[
\Pr(T_1\cdots T_k\ne0)=(K/N)^{k-1}.
\]
Conditioned on being nonzero, their product converges to the uniform law on the \((q-1)N^2\) nonzero isotropic-endpoint rank-one operators. Its total variation distance is **exactly**
\[
\boxed{\operatorname{TV}_k=\begin{cases}
(1-N^{-1})q^{-r(k-1)},&k\text{ odd},\\
(1-K/N)q^{-r(k-2)},&k\text{ even}.
\end{cases}}
\]

## Assumptions and scope
The form is symmetric and nonsingular, the characteristic is odd, and the dimension \(2r+1\ge5\). The formula is independent of the discriminant of \(B\); every odd-dimensional nonsingular form is isometric, up to a nonzero scalar, to the orthogonal sum of \(r\) hyperbolic planes and a one-dimensional form. Here “coimage line” means the line corresponding under \(B\colon V\simeq V^*\) to the row space of a rank-one operator. The fiber counts are for labeled, ordered factors. The conditional distribution is conditioned on the final matrix being nonzero, not on any one intermediate factor (all factors are already nonzero).

## Proof
**1. Rank-one normal form.** Any rank-one endomorphism has the form \(u\varphi\). It is self-adjoint for \(B\) precisely when \(\varphi\) is a scalar multiple of \(B(u,\cdot)\); this follows by comparing the two nonzero rank-one tensors in \(B(Tx,y)=B(x,Ty)\). Thus each \(T\in\mathcal N_B\) has the form \(a u_L B(u_L,\cdot)\), for a unique line \(L\in\mathcal P\) and unique \(a\in\mathbb F_q^\times\), since \(T^2=aB(u_L,u_L)T\). The number of singular nonzero vectors in any nondegenerate odd-dimensional quadratic space of dimension \(2r+1\) is \(q^{2r}-1\), proving \(|\mathcal P|=N\). For completeness, this standard zero count follows by adjoining one hyperbolic plane at a time: if \(Q\) has dimension \(2s+1\) and exactly \(q^{2s}\) zeros, the form \(Q+xy\) has \((2q-1)q^{2s}+(q-1)(q^{2s+1}-q^{2s})=q^{2s+2}\) zeros. Start with the one-variable nonsingular form.

**2. The nonorthogonality graph.** Define an \(N\)-by-\(N\) symmetric zero-diagonal adjacency matrix \(A\) by
\[
A_{LM}=\mathbf1_{B(u_L,u_M)\ne0}.
\]
For fixed isotropic \(u_L\), every nonorthogonal projective line has a unique representative \(w\) satisfying \(B(u_L,w)=1\). Completing \(u_L\) to a hyperbolic pair writes \(w=a u_L+u'_L+t\); its isotropy condition determines \(a\) uniquely from \(t\) in a \((2r-1)\)-space. Hence every row sum is \(K=q^{2r-1}\).

For distinct isotropic lines \(L,M\), count the isotropic projective points nonorthogonal to both. If \(B(u_L,u_M)=0\), extend their totally isotropic plane to two hyperbolic pairs. Fixing the two required nonzero dual coordinates leaves \(q\) choices for the two original coordinates, and \(q^{2r-3}\) choices for the perpendicular residual vector. Dividing the \((q-1)^2q^{2r-2}\) eligible nonzero vectors by \(q-1\) gives \((q-1)q^{2r-2}\) lines.

If \(B(u_L,u_M)\ne0\), their span is a hyperbolic plane. The eligible vectors are \(a u_L+b u_M+t\), with \(a,b\ne0\) and \(t\) in its nonsingular odd-dimensional complement, satisfying a quadratic equation \(Q(t)=-c ab\) for \(c\ne0\). For every fixed nonzero argument \(z\), the number of values \(t\) in this \((2r-1)\)-space with \(Q(t)=z\) equals \(q^{2r-2}+\epsilon\chi(z)q^{r-1}\), for a sign \(\epsilon\in\{\pm1\}\) depending only on the form. One proves this by induction, adding a hyperbolic plane and counting \(xy=z-Q(t)\), starting from \(1+\chi(c^{-1}z)\) solutions in dimension one. The character contribution vanishes after summing over \(a,b\in\mathbb F_q^\times\). Again the common-neighbor count is \((q-1)q^{2r-2}\).

With \(J\) the all-ones matrix, and \(D=q^{2r-2}\), this proves the **exact identity**
\[
\boxed{A^2=D I+(q-1)D J}.\tag{1}
\]
The diagonal entries are \(K=D+(q-1)D\) and every off-diagonal entry is \((q-1)D\). Also \(AJ=JA=KJ\) and \(K^2=D+(q-1)DN\).

**3. All graph-walk counts.** Equation (1), together with \(AJ=KJ\), gives
\[
A^{2t}=D^tI+\frac{K^{2t}-D^t}{N}J,
\qquad
A^{2t+1}=D^tA+\frac{K^{2t+1}-D^tK}{N}J.
\]
These identities follow by multiplying (1) repeatedly and projecting onto the constant vector and its orthogonal complement. They are integer matrix identities for every positive integer exponent, even when the displayed quotients are not obviously integral.

**4. Actual matrix products, including all target classes.** For any sequence of projective lines \(L_1,\ldots,L_k\) and nonzero scalars \(a_1,\ldots,a_k\),
\[
\prod_{i=1}^k\bigl(a_i u_{L_i}B(u_{L_i},\cdot)\bigr)
=\left(\prod_{i=1}^ka_i\right)
\left(\prod_{i=1}^{k-1}B(u_{L_i},u_{L_{i+1}})\right)
 u_{L_1}B(u_{L_k},\cdot).
\]
It is zero exactly when some consecutive orthogonal line pair occurs. Otherwise each length-\((k-1)\) walk from \(L\) to \(M\) admits exactly \((q-1)^{k-1}\) scalar assignments producing a prescribed nonzero coefficient \(c\); this yields the full fiber formula. There are \(NK^{k-1}\) allowable walks and \((q-1)^k\) choices of scalar labels on each, giving the zero formula by complement. Since \(A^2\) is strictly positive, all isotropic-endpoint nonzero targets occur at three factors; at two factors only nonorthogonal endpoints occur. The trace of \(c u_LB(u_M,\cdot)\) is \(cB(u_M,u_L)\), identifying the two-factor obstruction.

**5. Exact conditional mixing.** Conditioned on a nonzero product, the endpoint pair has mass \((A^{k-1})_{LM}/(NK^{k-1})\), and conditional on endpoints the output scalar is uniform in \(\mathbb F_q^\times\). The reference uniform law assigns mass \(1/N^2\) to each endpoint pair. For even \(\ell=k-1\), subtracting the uniform matrix from the normalized \(A^\ell\) leaves \(D^{\ell/2}(I-J/N)/(NK^\ell)\), whose total absolute mass is \(2(N-1)D^{\ell/2}/(NK^\ell)\). For odd \(\ell\), it leaves \(D^{(\ell-1)/2}(A-KJ/N)/(NK^\ell)\), whose total absolute mass is \(2(1-K/N)D^{(\ell-1)/2}/K^{\ell-1}\). Taking one half yields precisely the displayed total-variation formula. No asymptotic approximation is used.

## Verification
The bundled `check.py` independently enumerates all isotropic projective lines, constructs the polar adjacency by finite-field dot products, and verifies both its exact degree and its square identity. It tests graph-walk counts for lengths one through five in four prime-field configurations: \((q,r)=(3,2),(5,2),(7,2),(3,3)\). Separately it constructs all 80 literal rank-one self-adjoint square-zero \(5\times5\) matrices over \(\mathbb F_3\), performs **all 6,400 ordered two-factor dense matrix multiplications** and **all 512,000 ordered three-factor dense matrix multiplications**, and checks every prescribed-output frequency against the formula. There are 2,080 zero products at length two and 278,720 at length three; the 3,200 nonzero length-three target fibers have multiplicities 108 (80 targets) and 72 (3,120 targets). All assertions passed; raw output is in `verification_output.txt`. The finite checks supplement rather than establish the proof for arbitrary fields and lengths.

Reproduce with `python3 check.py` from the extracted artifact directory; the only external package dependency is NumPy.

## Relationship to prior work
Brouwer, Gow and Sheekey (2014) enumerate self-adjoint nilpotent endomorphisms and their Jordan shapes. Their full paper treats one-map counts, not prescribed products of rank-one self-adjoint nilpotents. Ihringer (2016), building on classical finite polar-space theory, records the strong regularity of the point-collinearity graph. In the odd-dimensional orthogonal specialization its complementary graph yields the matrix identity (1), which is **known geometric input** rather than claimed new. The contribution here is the connection to labeled matrix factorizations, complete all-length prescribed fibers, parity-alternating target invariants, sharp length-three reachability, and the exact conditioned multiplication-mixing law. Existing unrestricted minimal-nilpotent multiplication formulas concern factors of the full general-linear similarity orbit, not this self-adjoint subset; unrestricted counts do not determine restricted fibers. Other published zero-product results for arbitrary self-adjoint operators do not determine the nonzero higher-product strata.

## Limitations
The theorem is restricted to odd characteristic and odd orthogonal dimension at least five. It does not assert the corresponding formulas for even-dimensional forms, characteristic two, or higher-rank self-adjoint nilpotents. The adjacency geometry itself is classical and is explicitly credited; only the stated multiplication-fiber interpretation and consequences are presented as the assessed contribution. Published-literature coverage cannot certify global historical priority, and an unlocated equivalent specialized word-map theorem is a residual risk. The checker handles only prime-field examples, while the proof is uniform over every odd prime power.

## References
1. A. E. Brouwer, R. Gow and J. Sheekey, “Counting Symmetric Nilpotent Matrices,” *Electronic Journal of Combinatorics* 21(2) (2014), P2.4, published 2014-04-01, https://doi.org/10.37236/3810 ; full text https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p4/pdf/ .
2. F. Ihringer, “A Switching for all Strongly Regular Collinearity Graphs From Polar Spaces,” arXiv:1606.05898 (first public 2016-06-19), https://arxiv.org/abs/1606.05898 .
3. Published related comparison records: “Complete multiplication fibers of the minimal nonzero nilpotent orbit over finite fields”; “Rank fibers and component intersections of self-adjoint zero-product pairs”; “Complete Fourier spectrum of the isotropic Veronese Cayley graph over odd finite fields.” These address unrestricted, zero-only, and additive invariants respectively, rather than the stated all-length restricted products.
