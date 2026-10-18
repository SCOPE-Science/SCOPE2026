# The complete closed-ideal lattice above the compacts for triangular Calkin realizations

## Finding
Let \(V\) be any separable real or complex Banach space. Liu and Shen construct a separable Banach space \(X_V\) for which the quotient map
\[
q_V:\mathcal B(X_V)\longrightarrow \operatorname{Cal}(X_V)
\]
identifies the Calkin algebra with
\[
\mathfrak A(V^*)=\left\{\begin{pmatrix}\lambda&0\\ v&\mu\end{pmatrix}:\lambda,\mu\in\mathbb K,\ v\in V^*\right\},
\]
whose multiplication is
\[
(\lambda,v,\mu)(\lambda',v',\mu')=(\lambda\lambda',\,v\lambda'+\mu v',\,\mu\mu').
\]
Every closed two-sided ideal of \(\mathcal B(X_V)\) that contains \(\mathcal K(X_V)\) is exactly one of the following:

1. \(\mathcal J_W=q_V^{-1}(0\oplus W\oplus0)\), where \(W\) is an arbitrary closed linear subspace of \(V^*\);
2. \(\mathcal M_{\mu}=q_V^{-1}(\mathbb K\oplus V^*\oplus0)\);
3. \(\mathcal M_{\lambda}=q_V^{-1}(0\oplus V^*\oplus\mathbb K)\);
4. \(\mathcal B(X_V)\).

Thus \(\mathcal M_{\lambda}\) and \(\mathcal M_{\mu}\) are the only maximal proper closed two-sided ideals containing the compacts, and
\[
\mathcal M_{\lambda}\cap\mathcal M_{\mu}=\mathcal E(X_V).
\]
Moreover, \(W\mapsto\mathcal J_W\) is a lattice isomorphism from the closed-subspace lattice of \(V^*\) onto the interval \([\mathcal K(X_V),\mathcal E(X_V)]\).

## Assumptions and scope
The statement concerns the specific spaces \(X_V\) supplied by the triangular realization theorem of Liu--Shen, and only classifies closed two-sided ideals that contain \(\mathcal K(X_V)\). It makes no assertion about proper ideals lying strictly below the compact operators. The scalar field may be \(\mathbb R\) or \(\mathbb C\), and \(V\) may be the zero space.

The source theorem identifies \(\operatorname{Cal}(X_V)\) with \(\mathfrak A(V^*)\), identifies the Jacobson radical with the lower-left copy of \(V^*\), and identifies \(\mathcal E(X_V)/\mathcal K(X_V)\) with that radical. The source also records the subspace-to-ideal correspondence inside \([\mathcal K(X),\mathcal E(X)]\) for its universal choice \(V=\ell_1\). The classification above adds the remaining ideals above the radical and works for every separable coefficient space \(V\).

## Proof
Write
\[
e_0=(1,0,0),\qquad e_1=(0,0,1),\qquad R=0\oplus V^*\oplus0
\]
inside \(\mathfrak A(V^*)\). Let \(I\) be a closed two-sided ideal of \(\mathfrak A(V^*)\).

First suppose every element of \(I\) has both diagonal coordinates equal to zero. Then \(I\subseteq R\), so \(I=0\oplus W\oplus0\) for a closed linear subspace \(W\subseteq V^*\). Conversely every such subspace is a two-sided ideal, because direct multiplication gives
\[
(\lambda,v,\mu)(0,w,0)=(0,\mu w,0),\qquad
(0,w,0)(\lambda,v,\mu)=(0,w\lambda,0).
\]

Now suppose \(I\) contains \(a=(\lambda,v,\mu)\) with \(\lambda\ne0\). Then
\[
e_0ae_0=\lambda e_0,
\]
so \(e_0\in I\). For every \(r\in R\), one has \(re_0=r\); hence \(R\subseteq I\). If no element of \(I\) has nonzero \(\mu\)-coordinate, it follows that
\[
I=\mathbb K e_0\oplus R=\mathbb K\oplus V^*\oplus0.
\]
If some element of \(I\) has nonzero \(\mu\)-coordinate, the symmetric compression with \(e_1\) yields \(e_1\in I\), hence \(1=e_0+e_1\in I\) and \(I=\mathfrak A(V^*)\). The case in which a nonzero \(\mu\)-coordinate occurs but no nonzero \(\lambda\)-coordinate occurs is symmetric and gives \(I=0\oplus V^*\oplus\mathbb K\).

These cases exhaust all closed two-sided ideals of \(\mathfrak A(V^*)\). Since closed ideals of \(\mathcal B(X_V)\) containing \(\ker q_V=\mathcal K(X_V)\) correspond bijectively, by quotient and inverse image, to closed ideals of \(\operatorname{Cal}(X_V)\), the displayed list pulls back to the claimed list in \(\mathcal B(X_V)\).

Finally, Liu--Shen identify \(\mathcal E(X_V)/\mathcal K(X_V)\) with \(R\). Therefore the two codimension-one quotient ideals intersect in \(\mathcal E(X_V)\), and the ideals between the compacts and the inessential operators are precisely the \(\mathcal J_W\).

## Verification
The proof uses only the multiplication formula in the triangular Calkin algebra, the quotient correspondence for ideals containing the kernel, and the source identification of the inessential quotient with the radical. Each algebraic case can be checked by the two idempotent compressions \(e_0ae_0\) and \(e_1ae_1\). No finite experiment, enumeration, or unproved asymptotic step is used.

Boundary checks include \(V=\{0\}\), where the radical vanishes and the Calkin algebra is \(\mathbb K\oplus\mathbb K\), and one-dimensional \(V^*\), where the upper part of the lattice has the same diamond shape as the earlier Kania--Laustsen triangular example.

## Relationship to prior work
Liu--Shen, arXiv:2609.32334v1, prove the triangular realization for arbitrary separable \(V\), with square-zero radical isometric to \(V^*\), and prove \(\mathcal E(X_V)/\mathcal K(X_V)\cong V^*\). Their universal-ideal theorem explicitly records the closed-subspace lattice only in the interval \([\mathcal K(X),\mathcal E(X)]\) for the choice \(V=\ell_1\). The full list of closed ideals above the compacts for arbitrary \(V\), including the two and only two maximal ideals above the radical, is not stated in the inspected text.

Kania--Laustsen, arXiv:1507.01213, constructed an earlier Banach space whose closed-ideal lattice contains a one-dimensional triangular diamond: \(\{0\}\subset\mathcal K\subset\mathcal E\subset\mathcal M_1,\mathcal M_2\subset\mathcal B\). That result supplies the finite-dimensional prototype but does not cover the arbitrary dual radical \(V^*\) or the resulting full closed-subspace lattice.

Targeted searches for equivalent triangular-Calkin ideal classifications, arbitrary square-zero dual radicals, maximal-ideal formulations, and implication-level variants found no published result covering this statement.

## Limitations
The classification is relative to the triangular Calkin realization \(X_V\); it does not classify ideals below \(\mathcal K(X_V)\), nor does it assert that every Banach space with a Calkin algebra having two characters has this lattice. The algebraic derivation is short, so an equivalent formulation could exist under general triangular Banach-algebra terminology even though the application to the Liu--Shen realization was not located. No claim is made about approximate identities, generators, amenability, or finer geometry of the ideals.

## References
1. Rui Liu and Jie Shen, *Duals of separable Banach Spaces as Calkin Algebras and Universal Ideal Quotients*, arXiv:2609.32334v1, first submitted 2026-09-26. See Theorem 1.3 and Section 9.3.
2. Tomasz Kania and Niels Jakob Laustsen, *Ideal structure of the algebra of bounded operators acting on a Banach space*, arXiv:1507.01213, first submitted 2015-07-05.
