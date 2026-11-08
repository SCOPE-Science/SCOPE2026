# Averaging-projection rigidity and a two-parity rank law for scalar-affine Lie algebras

## Finding

Let \(q\) be any prime power, \(m\ge1\), and \(L_m=\mathbb F_q e\ltimes V\), where \(V=\mathbb F_q^m\) is abelian and \([e,v]=v\) for all \(v\in V\). Call a linear operator \(P:L_m\to L_m\) an **idempotent averaging operator** if \(P^2=P\) and
\[
[P(x),P(y)]=P([P(x),y])=P([x,P(y)])\quad(x,y\in L_m).
\]
Every such \(P\) is a **Lie-algebra endomorphism**. More precisely, either \(P=0\), or there is a unique idempotent linear map \(Q:V\to V\) and a unique vector \(v\in\ker Q\) such that
\[
P(e)=e+v,\qquad P(w)=Q(w)\quad(w\in V).
\]
Conversely, every such pair \((Q,v)\) defines an idempotent averaging operator. Thus the complete operator-rank generating polynomial is
\[
\boxed{\sum_{P}z^{\operatorname{rank}P}=1+\sum_{r=0}^{m}{m\brack r}_q q^{(m-r)(r+1)}z^{r+1}},
\]
where \({m\brack r}_q\) is the number of \(r\)-dimensional subspaces of \(\mathbb F_q^m\). Every integer rank from \(0\) to \(m+1\) occurs.

For fixed \(q\), let \(R_m\) be the rank of a uniformly random idempotent averaging operator and put \(S_m=R_m-1-\lfloor m/2\rfloor\). Define the finite positive constant
\[
\Theta_q=\sum_{s\in\mathbb Z}q^{-2s^2-s}=\sum_{s\in\mathbb Z}q^{-2s^2+s}.
\]
As \(m\to\infty\) through even values, \(S_m\) converges in total variation to the integer-valued law with masses \(q^{-2s^2-s}/\Theta_q\); through odd values it converges to the reflected law with masses \(q^{-2s^2+s}/\Theta_q\). In both cases the total-variation error is \(O_q(q^{-m/4})\). Consequently \(R_m/m\to 1/2\) in probability.

## Assumptions and scope

The ground field is any finite field of order \(q\), including even characteristic. The bracket is extended bilinearly from \([e,v]=v\), \([V,V]=0\), and \([x,y]=-[y,x]\); it is alternating also in characteristic two. The parameter \(m\) is any positive integer. Operators are **distinct labeled linear maps**, not conjugacy classes. Ranks are vector-space ranks over \(\mathbb F_q\). In the asymptotic statement \(q\) is fixed and \(m\) tends to infinity within the indicated parity.

## Proof

**1. Characterization of averaging projections.** For an idempotent linear map let \(H=\operatorname{im}P\) and \(K=\ker P\), so \(L_m=H\oplus K\). Expanding the averaging identity on \(H\oplus K\) gives the equivalent conditions
\[
[H,H]\subseteq H,\qquad [H,K]\subseteq K.
\]
For completeness, on \(h,h'\in H\) the averaging identity says \(P([h,h'])=[h,h']\), and on \(h\in H,k\in K\) it says \(P([h,k])=0\); bilinearity proves sufficiency.

**2. The image cannot lie in the derived ideal.** Assume \(H\ne0\) and \(H\subseteq V\). Because \(H+K=L_m\), choose \(k=ae+w\in K\) with \(a\ne0\). For \(0\ne h\in H\) we have \([h,k]=-ah\), which lies simultaneously in \(H\) and in \(K\) by the preceding criterion. This contradicts \(H\cap K=0\). Hence the projection of \(H\) onto \(L_m/V\) is nonzero.

**3. The kernel lies in the derived ideal.** Choose \(h=e+u\in H\), where \(u\in V\). The adjoint action \(\operatorname{ad}_h\) is zero on \(\mathbb F_qh\) and the identity on \(V\), so \(L_m=\mathbb F_qh\oplus V\) is its \(0,1\)-eigenspace decomposition. By step 1, \(K\) is invariant under this projection operator. Thus any \(k\in K\) decomposes as \(k=k_0+k_1\) with \(k_0\in K\cap\mathbb F_qh\) and \(k_1\in K\cap V\), since the spectral projections are \(I-\operatorname{ad}_h\) and \(\operatorname{ad}_h\). But \(K\cap\mathbb F_qh=0\), so \(K\subseteq V\). Every linear subspace of \(V\) is an ideal of \(L_m\); therefore \(K\) is an ideal. Since \(H\) is a subalgebra, \(P\) preserves the Lie bracket, proving the rigidity assertion.

**4. Parameterization and exact counts.** Because \(K\subseteq V\), the restriction \(Q=P|_V\) is a linear projection and \(P(e)=e+v\) for some \(v\in V\). Idempotency on \(e\) says \(Qv=0\). Conversely such a pair yields a Lie-algebra homomorphism: the sole nonzero defining brackets satisfy \([e+v,Qw]=Qw=P([e,w])\); the operator is idempotent because \(Qv=0\). Every Lie endomorphism is averaging, proving the converse. Fix \(r=\operatorname{rank}Q\). There are \({m\brack r}_q\) choices for \(W=\operatorname{im}Q\), then \(q^{r(m-r)}\) complementary kernels in \(V\), and finally \(q^{m-r}\) choices for \(v\in\ker Q\). Thus the rank-\(r+1\) count is exactly \({m\brack r}_q q^{(m-r)(r+1)}\). The zero map adds the rank-zero term; the identity is the sole rank-\(m+1\) map.

**5. The two parity limits.** Set \(D_j(q)=\prod_{i=1}^j(1-q^{-i})\) and \(D_\infty(q)=\prod_{i=1}^\infty(1-q^{-i})>0\). The Gaussian binomial identity gives
\[
{m\brack r}_q=q^{r(m-r)}\frac{D_m(q)}{D_r(q)D_{m-r}(q)}.
\]
The rank-\(r+1\) weight is therefore
\[
q^{(m-r)(2r+1)}\frac{D_m(q)}{D_r(q)D_{m-r}(q)}.
\]
For \(m=2k\), put \(r=k+s\); the exponent equals \(2k^2+k-2s^2-s\). For \(m=2k+1\) the exponent is \(2k^2+3k+1-2s^2+s\). For \(\lvert s\rvert\le m/4\), the product ratio equals \(D_\infty(q)^{-1}(1+O_q(q^{-m/4}))\), uniformly in \(s\). Over all admissible \(s\), the product ratio is bounded above by \(D_\infty(q)^{-2}\), and the tails \(\lvert s\rvert>m/4\) of either Gaussian weight are \(O_q(q^{-c m^2})\) for some \(c>0\). The zero operator has negligible relative weight, since the dominant nonzero term grows at least as \(q^{m^2/3}\) for all sufficiently large \(m\). Dividing by the common total weight proves the asserted total-variation limits and error bound. The tightness of \(S_m\) gives \(R_m/m\to1/2\).

## Verification

Run `python3 verify.py` using a standard Python installation. It exhaustively enumerates every matrix over \(\mathbb F_2\) in dimensions \(2,3,4\), every matrix over \(\mathbb F_3\) in dimensions \(2,3\), and every matrix over \(\mathbb F_4\) in dimensions \(2,3\). It tests idempotency and both averaging identities directly on basis pairs, computes each matrix rank by finite-field elimination, checks every accepted map is a Lie endomorphism, and compares the resulting histogram to the exact formula. The polynomial for dimension four over \(\mathbb F_2\) has coefficients \((1,8,112,56,1)\); the dimension-three \(\mathbb F_4\) polynomial has coefficients \((1,16,80,1)\). The successful run ends with `VERIFY_OK`. Finite enumeration verifies only the listed finite cases; the proof above covers all prime powers and all positive \(m\).

## Relationship to prior work

Laraiedh–Silvestrov (2023), §2.2, Proposition 2.24 (numbered Proposition 2.25 in the later published version), establishes the general characterization of idempotent averaging operators in terms of a subalgebra image and a kernel invariant under that image; **that general criterion is prior work**. Their classification sections instead treat homogeneous operators on \(q\)-deformed Witt-type Hom-Lie algebras, not the present finite scalar-affine family. Tang–Sheng–Wagemann (2023), §1.2 and §§2–4, develops the connection between averaging operators, relative Rota–Baxter operators, and their cohomology, rather than finite-field enumeration of projections. The present contribution is the specific rigidity of all averaging projections to Lie retracts on this family, the complete embedded rank counts, and the two reflected theta limits. The rigidity fails for general Lie algebras: on the three-dimensional Heisenberg algebra with \([x,y]=z\), projection onto \(\mathbb F_qz\) along \(\operatorname{span}\{x,y\}\) is averaging but does not preserve \([x,y]\).

## Limitations

The conclusion that every averaging projection is a Lie endomorphism uses the scalar adjoint action on the codimension-one abelian ideal; it need not hold for general almost-abelian Lie algebras with nonscalar action. The asymptotic statement fixes \(q\). The rank formula counts labeled operators, not isomorphism classes. The general idempotent-averaging criterion and Gaussian-binomial projection enumeration are established tools; only the specialized rigidity and refined rank/asymptotic assertions are assessed here. An unlocated comprehensive census of affine Lie retractions could imply the counting formula; the literature-priority comparison is not exhaustive.

## References

1. I. Laraiedh and S. Silvestrov, *Averaging operators on q-deformed Witt and q-deformed W(2,2) algebras*, first public preprint 2023-04-03, arXiv:2304.00662, §2.2 and §§3–4; https://arxiv.org/abs/2304.00662.
2. R. Tang, Y. Sheng and F. Wagemann, *From relative Rota-Baxter operators and relative averaging operators on Lie algebras to relative Rota-Baxter operators on Leibniz algebras: a uniform approach*, first public preprint 2023-06-24, arXiv:2306.13873, §§1–2 and §4; https://arxiv.org/abs/2306.13873.
