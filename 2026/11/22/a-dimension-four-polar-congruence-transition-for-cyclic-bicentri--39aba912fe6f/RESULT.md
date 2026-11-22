# A dimension-four polar-congruence transition for cyclic bicentric simplices

## Finding
For each integer \(n\ge3\) and each \(t>0\), let \(H=\{x\in\mathbb R^{n+1}:\sum_i x_i=0\}\), \(v_j=e_j-\mathbf1/(n+1)\), and \(W\subset H\) be the real first-frequency two-plane of the \((n+1)\)-point discrete Fourier transform. With \(P\) orthogonal projection onto \(W\), put \(T_t=P+t(I_H-P)\), \(N_t^2=(2+(n-2)t^2)/(n+1)\), and \(\Delta_t=\operatorname{conv}\{T_tv_j/N_t:0\le j\le n\}\). Here \(\Delta_t\) has unit circumradius, its centroid and its incenter coincide at the origin, and its inradius is \(h_t=[(2+(n-2)t^2)(2+(n-2)t^{-2})]^{-1/2}\), as established by Nour for \(0<t\le1\); the identities extend to every \(t>0\).

**Theorem (reciprocal polar-pair classification).** For every \(t>0\),
\[
 h_t\Delta_t^\circ=-\Delta_{1/t},
 \qquad \operatorname{vol}_n(\Delta_t)=\frac{\sqrt{n+1}}{n!}\,t^{n-2}\left(\frac{n+1}{2+(n-2)t^2}\right)^{n/2}.
\]
The two unit-circumradius, equal-inradius simplices \(\Delta_t\) and \(\Delta_{1/t}\) are Euclidean congruent if and only if \(t=1\) or \(n=4\). At \(n=4\), the congruence holds via the vertex permutation \(j\mapsto 2j\pmod5\), together with a Euclidean isometry, at every \(t>0\). For \(0<t<1\), their volumes satisfy
\[
\operatorname{vol}_3(\Delta_t)>\operatorname{vol}_3(\Delta_{1/t}),\qquad
\operatorname{vol}_4(\Delta_t)=\operatorname{vol}_4(\Delta_{1/t}),\qquad
\operatorname{vol}_n(\Delta_t)<\operatorname{vol}_n(\Delta_{1/t})\ (n\ge5).
\]
In particular, the volume ratio tends to infinity in dimension three, remains exactly one in dimension four, and tends to zero in every dimension at least five as \(t\downarrow0\). These are *family-specific* statements; no analogous classification for all bicentric simplices is asserted.

## Assumptions and scope
All geometry is Euclidean in the \(n\)-plane \(H\). Polarity is taken with respect to the origin and Euclidean unit ball: \(K^\circ=\{y:\langle y,x\rangle\le1\text{ for all }x\in K\}\). The coordinate indices run from \(0\) to \(n\); \(n\ge3\) is an integer and \(t>0\). The Fourier plane is \(W=\operatorname{span}\{q,s\}\) with \(q_j=\cos(2\pi j/(n+1))\) and \(s_j=\sin(2\pi j/(n+1))\). The source proves the geometry for \(0<t\le1\). Its proof uses only invertibility and the Fourier orthogonality identities, which remain valid for all positive \(t\); equivalently, one can reverify the displayed facet-normal equations directly for \(t>1\).

## Proof
Write \(m=n+1\), \(Q=I_H-P\). The regular simplex \(\operatorname{conv}\{v_j\}\) has volume \(\sqrt m/n!\): the Gram determinant of the \(n\) edge vectors \(e_j-e_0\) is \(m\). On \(H\), the operator \(T_t=P+tQ\) has eigenvalues \(1\) twice and \(t\) with multiplicity \(n-2\), so \(\det T_t=t^{n-2}\). Rescaling all transformed vertices by \(N_t^{-1}\) gives the asserted volume formula.

The unit outward facet normal opposite the \(j\)-th vertex is
\[
\nu_j(t)=-\frac{T_t^{-1}v_j}{L_t},\qquad
L_t^2=\frac{2+(n-2)t^{-2}}{m}.
\]
Indeed, \(\langle T_tv_i/N_t,\nu_j(t)\rangle=1/(mN_tL_t)=h_t\) for every \(i\ne j\), while the inner product is \(-n h_t\) when \(i=j\). Thus the defining inequalities are \(\langle x,\nu_j(t)\rangle\le h_t\). As \(T_t^{-1}=T_{1/t}\) and \(L_t=N_{1/t}\), we have \(\nu_j(t)=-u_j(1/t)\), where \(u_j(s)=T_sv_j/N_s\). Polarity gives \(h_t\Delta_t^\circ=\operatorname{conv}\{\nu_j(t)\}=-\Delta_{1/t}\). The equality \(h_t=h_{1/t}\) is immediate.

The volume ratio \(R_n(s):=\operatorname{vol}_n(\Delta_{\sqrt s})/\operatorname{vol}_n(\Delta_{1/\sqrt s})\) is
\[
R_n(s)=s^{(n-4)/2}\left(\frac{2s+n-2}{2+(n-2)s}\right)^{n/2}.
\]
Direct logarithmic differentiation, with all denominators strictly positive, yields the exact identity
\[
 \frac{d}{ds}\log R_n(s)=\frac{(n-4)(n-2)(s-1)^2}{s(n+2s-2)((n-2)s+2)}.
\]
As \(R_n(1)=1\), the sign for \(0<s<1\) is positive if \(n=3\), zero if \(n=4\), and negative if \(n\ge5\). If \(t\ne1\) and \(n\ne4\), the unequal volumes forbid Euclidean congruence. Furthermore
\[
 R_n(t^2)\sim\left(\frac{n-2}{2}\right)^{n/2}t^{n-4}\quad(t\downarrow0),
\]
which gives the three limiting regimes.

When \(n=4\), \(m=5\) and \(Q\) is the second-frequency two-plane. Under the permutation \(j\mapsto2j\pmod5\), the first and second Fourier frequency planes interchange. Since \(N_{1/t}=N_t/t\), the vertex Gram matrix of \(\Delta_{1/t}\), after this permutation, equals that of \(\Delta_t\): the eigenvalue \(1/N_t^2\) on the first two-plane and \(t^2/N_t^2\) on the second two-plane are exchanged. A bijection of affinely spanning vertex sets preserving all pairwise distances extends to a Euclidean isometry, proving congruence.

## Verification
A standalone numerical checker (`check.py`) reconstructs the \(n+1\) vertices, both normal configurations, the dual facet identities, the volume formula via Gram determinants, and the dimension-four permutation congruence for integers \(3\le n\le12\) at five positive parameters. It passed. This is corroboration, not a substitute for the all-dimensional determinant, polarity, and derivative proof. The derivative factorization can additionally be checked by direct rational symbolic differentiation.

## Relationship to prior work
Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher* (arXiv:2611.14181v1, first public 2026-11-10), Section 3, supplies the Fourier deformation, normalization, facet normals, and common inradius for \(0<t\le1\). The result above does **not** claim that construction or the insphere/circumsphere coincidence as new. The new structural claims are exact reciprocal polar duality, the dimension-four congruence classification, and the opposite-volume ordering with a sharp dimension threshold and limiting ratio.

A previously indexed result titled *Sharp volume interval for concentric bicentric tetrahedra* gives a complete three-dimensional volume interval at fixed radii, and therefore dominates any bare assertion that three-dimensional concentric bicentric tetrahedra can have unequal volumes. The present theorem's novelty is **not** that assertion; it concerns an exact reciprocal-polar correspondence and a dimension-sensitive all-dimensional classification of this canonical Fourier family. The all-three-dimensional volume comparison may also be derivable from that published interval combined with its extremizers; it is included for the transparent full dimension-split statement, not independently promoted as a new theorem.

## Limitations
The theorem is restricted to Nour's one-parameter Fourier family and its positive reciprocal extension. It does not classify polar-congruent simplices outside that family or prove new universal insphere inequalities. Earlier specialized work on bicentric simplex polar duality and the closest historical three-dimensional volume theorem may contain related formulations; the novelty assessment is provisional pending independent literature review. Numerical sampling does not prove uniqueness outside the displayed family. No independent mathematical audit was performed.

## References
- C. Nour, *A counterexample to the strong version of the union of uniform closed balls conjecture in dimensions three and higher*, arXiv:2611.14181v1 (2026-11-10), https://arxiv.org/abs/2611.14181, particularly Lemma 3.1 and its proof.
- *Sharp volume interval for concentric bicentric tetrahedra*, published-finding corpus indexed record `2026/10/11/SCOPE-sharp-volume-interval-for-concentric-bicentric-tetrahedra--3c21c1faa6d8` (background/possible stronger three-dimensional coverage; full text not independently inspected).
