# A sharp common-metric obstruction for rank-one \(2\)-partial isometries

## Finding
Let \(H\) be a complex Hilbert space of dimension at least two and \(T\in\mathcal B(H)\) have rank one and be nonzero. Set \(x=\|T\|^2\). An operator is called a \(2\)-partial isometry when \(T\beta_2(T)=0\), where \(\beta_2(T)=T^{*2}T^2-2T^*T+I\). Define the canonical reflexive generalized inverse
\[
S_T=2T^*-T^{*2}T.
\]
Here a *common metric* means one and the same equivalent Hilbert inner product on both the domain and the codomain of \(T\); equivalently, \(\langle h,k\rangle_G=\langle Gh,k\rangle\) for a bounded, strictly positive, boundedly invertible \(G\) on \(H\).

**Theorem.** Suppose \(T\) is a rank-one \(2\)-partial isometry. Then \(x\ge\frac12\), and \(S_T\) is the Moore--Penrose inverse of \(T\) with respect to some common metric **if and only if**
\[
\boxed{\ \|T\|^2<2\ }.
\]
For every \(\frac12<x<2\) with \(x\ne1\), the sharp minimal metric condition number is
\[
\boxed{\ \inf_{G:\ S_T=T^{\dagger_G}}\|G\|\,\|G^{-1}\|=\frac2{2-x}\ }.
\]
At the two degenerate parameters \(x=\frac12\) and \(x=1\), the minimum equals \(1\), because the original inner product works. This is a complete classification of rank-one \(2\)-partial isometries on any complex Hilbert space, finite- or infinite-dimensional.

In particular, on \(\mathbb C^2\) the exact matrices
\[
T=\begin{pmatrix}\sqrt7/2&0\\3/2&0\end{pmatrix},\qquad
S_T=\begin{pmatrix}-\sqrt7&3\\0&0\end{pmatrix}
\]
provide a negative answer already in dimension two to the common-inner-product Moore--Penrose question posed for this generalized inverse.

## Assumptions and scope
All operators act on a complex Hilbert space \(H\) of dimension at least two; rank-one means nonzero with one-dimensional range. The adjoint \(T^*\) is initially taken with respect to the given Hilbert structure. Changing to a common metric changes the adjoint used in the Moore--Penrose identities, but **does not** redefine the already constructed operator \(S_T\). The same metric is required for both Penrose selfadjointness identities. The condition-number assertion concerns \(G>0\) bounded and boundedly invertible, and does not make a claim about allowing two independently chosen domain/codomain metrics.

## Proof
Write \(T=\sqrt{x}\,u\otimes v^*\) with \(\|u\|=\|v\|=1\). Multiplication of \(T\) by a unimodular scalar multiplies \(S_T\) by its conjugate and changes neither \(S_TT\) nor \(TS_T\), so it does not affect common-metric Moore--Penrose equivalence. We may therefore write
\[
u=cv+sw,\qquad c,s\ge0,\qquad c^2+s^2=1,
\]
for some \(w\perp v\) of norm one. All ensuing operators vanish outside the relevant two-plane, except where the identity is explicitly present.

A direct rank-one calculation gives
\[
T^*T=xP_v,\qquad T^{*2}T^2=x^2c^2P_v,\qquad
\beta_2(T)=I+(x^2c^2-2x)P_v.
\]
Since \(T\ne0\), the \(2\)-partial-isometry equation \(T\beta_2(T)=0\) is equivalent to
\[
\boxed{x^2c^2=2x-1}.
\]
Consequently \(x\ge\frac12\), \(c^2=(2x-1)/x^2\), and \(s^2=(x-1)^2/x^2\). Conversely these formulas realize a rank-one \(2\)-partial isometry for every \(x\ge\frac12\): choose the indicated \(c,s\) and the above \(T\).

The inverse candidate and its two idempotent products are
\[
S_T=\sqrt{x}\,v\otimes((2-x)c\,v^*+2s\,w^*),\quad
P=S_TT=P_v,
\]
\[
Q=TS_T=x\begin{pmatrix}
(2-x)c^2&2cs\\(2-x)cs&2s^2
\end{pmatrix}_{(v,w)}.
\]
Thus \(P^2=P\), \(Q^2=Q\), \(TS_TT=T\), and \(S_TTS_T=S_T\). These are the first two Penrose identities without changing the metric. For the remaining two, a positive invertible \(G\) works precisely when
\[
GP=P^*G,\qquad GQ=Q^*G.
\]
The first condition requires \(Gv=g v\) with \(g=\langle Gv,v\rangle>0\). If \(cs>0\), testing the second condition on the ordered pair \((v,w)\) yields
\[
2g=(2-x)\langle Gw,w\rangle.
\]
Positivity therefore forces \(x<2\). Conversely, for every \(x<2\), the explicitly bounded positive definite metric
\[
\boxed{G=2I-xP_v}
\]
satisfies both equations (verify the two off-diagonal entries of \(GQ\) from the displayed matrix). This includes the degenerate cases \(c=0\) and \(s=0\). When \(cs=0\), the rank-one constraint forces \(x=\frac12\) or \(x=1\), respectively; in both cases \(P,Q\) are already orthogonal projections and \(G=I\) works. For \(x\ge2\), one has \(cs>0\), so the positivity contradiction is decisive.

For nondegenerate \(\frac12<x<2\), \(x\ne1\), write \(h=\langle Gw,w\rangle>0\). The same identity gives \(h/g=2/(2-x)>1\). Since \(v\) is an eigenvector of \(G\) and \(\|G\|\ge h\), \(\|G^{-1}\|\ge1/g\), so every admissible \(G\) satisfies \(\|G\|\|G^{-1}\|\ge2/(2-x)\). The displayed \(G=2I-xP_v\) has precisely the two spectral values \(2-x\) and \(2\), attaining equality.

For the concrete matrix, a direct computation yields
\[
\beta_2(T)=\begin{pmatrix}0&0\\0&1\end{pmatrix},\quad
S_TT=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
TS_T=\begin{pmatrix}-7/2&3\sqrt7/2\\-3\sqrt7/2&9/2\end{pmatrix}.
\]
Any \(G>0\) making \(S_TT\) orthogonal must be diagonal in this basis. Making \(TS_T\) orthogonal would then equate a positive multiple of \(3\sqrt7/2\) with a negative multiple of \(3\sqrt7/2\), impossible. Hence the negative example is exact, not numerical.

## Verification
The standalone dependency-free `checker.py` recomputes \(T^{*2}T^2\), \(\beta_2(T)\), \(S_T\), \(S_TT\), and \(TS_T\) exactly over \(\mathbb Q(\sqrt7)\), verifies both reflexive-generalized-inverse identities and the opposite off-diagonal signs, and checks representative parameter values on both sides of the threshold. Run `python3 checker.py` from a directory containing this file. The universal assertions and optimality are proved above; finite diagnostics are not a substitute for those arguments.

## Relationship to prior work
Aouichaoui, Buchała and Garcia introduced the specific generalized inverse for \(m\)-partial isometries in their Lemma 2.8 and explicitly asked in Section 6, Question 6 whether, for \(m=2\), it can be a Moore--Penrose inverse in some inner product. Their results establish reflexive generalized-inverse identities but not a common-metric criterion. The theorem above resolves this question negatively in dimension two, and sharpens the answer to an exact rank-one norm threshold, including the best possible metric conditioning on the positive side.

The standard four Penrose equations and general weighted pseudoinverse theory allow two independently assigned positive weights, which is a different problem: requiring a *single* metric makes the two idempotents simultaneously selfadjoint and causes the obstruction. Earlier studies of \(m\)-partial isometries and semi-Hilbertian variants motivate the operator class; the displayed rank-one threshold is not presented as a consequence of their general theory.

## Limitations
The classification is for rank-one \(2\)-partial isometries, not arbitrary rank or higher \(m\). It prescribes one common positive-definite equivalent inner product, not separate weights on source and target. No assertion is made about a different generalized inverse of \(T\), since an ordinary Moore--Penrose inverse always exists for finite-rank \(T\). The literature comparison is based on the accessible source material described in the companion review; older work on simultaneous symmetrization of idempotents may imply parts of the argument. Independent historical-priority assessment has not been performed.

## References
1. M. A. Aouichaoui, M. Buchała, S. R. Garcia, *On \(m\)-partial isometries: spectra, weighted shifts, and similarity*, arXiv:2606.12865 (first publicly posted June 11, 2026), especially Lemma 2.8 and Section 6, Question 6.
2. A. Saddi, O. A. Mahmoud Sid Ahmed, *\(m\)-partial isometries on Hilbert spaces*, International Journal of Functional Analysis, Operator Theory and Applications **2** (2010), 67–83.
3. A. Saddi, F. Mahmoudi, *\((A,m)\)-partial isometries in semi-Hilbertian spaces*, Linear and Multilinear Algebra **71** (2023), 1640–1656, first online April 27, 2022.
4. D. S. Djordjević et al., *Unified approach to the reverse order rule for generalized inverses*, on weighted Moore--Penrose equations; consulted for background on the distinction between common and independent weights.
