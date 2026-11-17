# Absolute-sum rigidity and exact lattice lifting constants for scalar–\(\ell_1\) extensions

## Finding

Let \(\nu\) be **any** normalized absolute norm on \(\mathbb R^2\): it satisfies \(\nu(s,t)=\nu(|s|,|t|)\) and \(\nu(1,0)=\nu(0,1)=1\). Give the real vector lattice
\[
A_\nu=\mathbb R\oplus\ell_1(\mathbb N),\qquad
\|(a,x)\|_{A_\nu}=\nu\bigl(|a|,\|x\|_1\bigr)
\]
its coordinatewise order. Define its **optimal lattice projective lifting constant** \(\kappa(A_\nu)\) as the infimum of numbers \(\lambda\ge1\) with this property: for every real Banach lattice \(Y\), closed lattice ideal \(J\), bounded lattice homomorphism \(T:A_\nu\to Y/J\), and \(\varepsilon>0\), there exists a lattice homomorphism \(\widetilde T:A_\nu\to Y\) lifting \(T\) with \(\|\widetilde T\|\le(\lambda+\varepsilon)\|T\|\). The zero map is understood to have a zero lift.

**Theorem (one geometric classification).** For every normalized absolute norm \(\nu\),
\[
\boxed{\ \kappa(A_\nu)=K_\nu:=\max_{s,t\ge0,\ s+t=1}\frac1{\nu(s,t)}\ }.
\]
Moreover, \(A_\nu\) is semiprojective in the sense of Kania–Niwiński (separable ambient Banach lattices, prescribed increasing ideal towers, and one stage supporting arbitrarily close-to-contractive lifts) **if and only if** \(\nu(s,t)=|s|+|t|\) for every \((s,t)\in\mathbb R^2\). Equivalently, semiprojectivity holds precisely when \(K_\nu=1\).

In particular, \(\kappa(\mathbb R\oplus_q\ell_1)=2^{1-1/q}\) for \(1\le q\le\infty\), and the sum is semiprojective exactly at \(q=1\). For the normalized absolute norms \(\nu_\theta(s,t)=(1-\theta)(|s|+|t|)+\theta\max\{|s|,|t|\}\), \(0\le\theta\le1\), the constants are exactly \(K_{\nu_\theta}=2/(2-\theta)\). Thus all possible optimal lifting constants \([1,2]\) occur, and even arbitrarily small nontrivial lattice renormings of \(\ell_1\) can destroy semiprojectivity.

## Assumptions and scope

All spaces and lattice homomorphisms are **real**. The norm \(\nu\) is any finite-dimensional absolute lattice norm with both coordinate vectors of norm one; it need not be symmetric under interchange of the two coordinates or strictly convex. The index set of the \(\ell_1\) component is countably infinite. The projective lifting constant tests all Banach lattices and closed lattice ideals; the semiprojectivity assertion tests separable ambient Banach lattices and sequential ideal towers, with the lifting stage independent of the permitted norm loss.

A normalized absolute norm satisfies
\[
\max\{s,t\}\le\nu(s,t)\le s+t\qquad(s,t\ge0),
\]
by lattice monotonicity and the triangle inequality. Hence \(1\le K_\nu\le2\), and the compact simplex maximization defining \(K_\nu\) is attained.

## Proof

**1. Upper bound by the ordinary projective \(\ell_1\) norm.** Write \(L=\mathbb R\oplus_1\ell_1(\mathbb N)\), lattice-isometric to \(\ell_1(\mathbb N_0)\). The formal coordinatewise lattice identities \(U:A_\nu\to L\) and \(V:L\to A_\nu\) have
\[
\|U\|=\sup_{(s,t)\ne(0,0),\ s,t\ge0}\frac{s+t}{\nu(s,t)}=K_\nu,
\qquad \|V\|=1.
\]
The last equality follows because \(\nu(s,t)\le s+t\), with equality on each coordinate axis. By the projectivity of countable \(\ell_1\) as a Banach lattice (de Pagter–Wickstead, Theorem 11.8), every lattice homomorphism \(T\circ V:L\to Y/J\) has, for each \(\delta>0\), a lattice-homomorphic lift \(W:L\to Y\) with \(\|W\|\le(1+\delta)\|T\circ V\|\). Then \(W\circ U\) lifts \(T\) and has norm at most \(K_\nu(1+\delta)\|T\|\). Thus \(\kappa(A_\nu)\le K_\nu\).

**2. A quotient tower with a universal sharp obstruction.** Let \(c\) be the real convergent-sequence lattice, and set
\[
B=c\oplus c_0,\qquad
\|(u,v)\|_B=\sup_{n\ge1}\bigl(|u_n|+|v_n|\bigr).
\]
This is a separable Banach lattice. Put \(I_m=\{(j,0):j\in c_0,\ j_n=0\text{ for }n>m\}\) for positive integers \(m\), and \(I=\overline{\bigcup_m I_m}=c_0\oplus\{0\}\). Each \(I_m\) and \(I\) is a closed lattice ideal. Denote the quotient maps by \(Q_m:B\to B/I_m\) and \(Q:B\to B/I\), and the canonical map \(B/I_m\to B/I\) by \(\pi_m\).

The map \(\Phi:B\to\mathbb R\oplus_\infty c_0\), \(\Phi(u,v)=(\lim_n u_n,v)\), induces an **isometric lattice isomorphism** \(\overline\Phi:B/I\to\mathbb R\oplus_\infty c_0\). To see the norm equality, any representative of \((a,v)\) has norm at least \(\max\{|a|,\|v\|_\infty\}\). Conversely, choose \(N\) such that \(|v_n|\le\delta\) for \(n>N\) and take the representative with first sequence \(u_n=0\) for \(n\le N\) and \(u_n=a\) for \(n>N\). Its norm is at most \(\max\{\|v\|_\infty,|a|+\delta\}\); let \(\delta\downarrow0\).

Define a lattice homomorphism \(T:A_\nu\to B/I\) by
\[
T(a,x)=\overline\Phi^{-1}(a,\iota x),
\]
where \(\iota:\ell_1\hookrightarrow c_0\) is the canonical coordinatewise inclusion. It is a contraction, since
\(\|T(a,x)\|=\max\{|a|,\|x\|_\infty\}\le\nu(|a|,\|x\|_1)\); in fact \(\|T\|=1\), by applying it to \((1,0)\).

Fix a stage \(m\) and suppose \(S:A_\nu\to B/I_m\) is **any** lattice-homomorphic lift, \(\pi_m S=T\). For positive \(s,t\), choose positive representatives in \(B\) of \(S(s,0)\) and \(S(0,t e_n)\), denoted \((u^{(s)},v^{(s)})\) and \((u^{(n)},v^{(n)})\). Such representatives exist because a positive quotient class is the modulus of a representative. Since their images in \(B/I\) are \((s,0)\) and \((0,t e_n)\), respectively,
\[
\lim_{j\to\infty}u^{(s)}_j=s,
\qquad v^{(s)}=0,
\qquad v^{(n)}=t e_n,
\qquad u^{(n)}_j\ge0.
\]
For every \(n>m\), subtracting elements of \(I_m\) does not change the \(n\)-th pair of coordinates. Positivity therefore yields
\[
\|S(s,t e_n)\|_{B/I_m}
\ge u^{(s)}_n+u^{(n)}_n+t
\ge u^{(s)}_n+t.
\]
As \(n\to\infty\), \(u^{(s)}_n\to s\), whereas \(\|(s,t e_n)\|_{A_\nu}=\nu(s,t)\). Hence every such \(S\) satisfies
\[
\|S\|\ge\frac{s+t}{\nu(s,t)}.
\]
Taking the supremum over \(s,t\ge0\) with \(s+t>0\) gives \(\|S\|\ge K_\nu\). For an ordinary quotient lift \(S:A_\nu\to B\), the same argument applies directly (or take the quotient to \(B/I_1\)); thus \(\kappa(A_\nu)\ge K_\nu\). Together with Step 1 this proves the exact formula. Furthermore, the explicit lattice homomorphism \(S_0:A_\nu\to B\), \(S_0(a,x)=((a,a,\ldots),\iota x)\), is a lift of \(T\), with \(\|S_0\|=K_\nu\): indeed \(\|S_0(a,x)\|=|a|+\|x\|_\infty\le |a|+\|x\|_1\), and this upper bound has supremum exactly \(K_\nu\) on inputs \((s,t e_n)\). Thus every individual stage has a lift \(Q_m S_0\) of norm exactly \(K_\nu\), matching the lower bound.

**3. Sharp semiprojectivity boundary.** If \(K_\nu>1\), the single contractive map \(T\) above has no lift of norm \(\le1+\varepsilon\) at **any** stage for \(0<\varepsilon<K_\nu-1\); hence \(A_\nu\) is not semiprojective. If \(K_\nu=1\), the triangle inequality \(\nu(s,t)\le s+t\), together with \((s+t)/\nu(s,t)\le1\), forces \(\nu(s,t)=s+t\) for every \(s,t\ge0\). Absoluteness makes \(\nu\) the \(\ell_1^2\) norm, so \(A_\nu=L\cong\ell_1\), which is \(1^+\)-projective and therefore semiprojective. This proves the equivalence.

**4. Explicit parameter families.** For \(\nu(s,t)=(s^q+t^q)^{1/q}\) on the positive quadrant with \(1\le q<\infty\), Hölder gives \(s+t\le2^{1-1/q}\nu(s,t)\), with equality at \(s=t>0\); at \(q=\infty\) the sharp ratio is two. For \(\nu_\theta\), if \(s+t=1\) then \(\nu_\theta(s,t)=1-\theta+\theta\max\{s,t\}\), minimized at \(s=t=1/2\), giving \(K_{\nu_\theta}=1/(1-\theta/2)=2/(2-\theta)\). All claimed consequences follow.

## Verification

The lower-bound witness is the explicit separable Banach lattice \(B=c\oplus c_0\) with the exact sequence of finite-coordinate ideals above; every step of the norm bound is uniform in the stage \(m\). The quotient norm is calculated in both directions, and the stage lower bound uses a fixed positive representative for \(S(s,0)\), allowing \(n\to\infty\). The proof checks both endpoint norms (\(\ell_1\) and \(\ell_\infty\)), the zero-coordinate cases, and nonsymmetric normalized absolute norms. No finite experiments or unpublished infinite-dimensional lemma is used. The sole external positive lifting premise is the established \(1^+\)-projectivity of countable \(\ell_1\), cited below.

## Relationship to prior work

Kania and Niwiński's *Semiprojective Banach lattices* (arXiv:2604.10624, first submitted 12 April 2026), especially Theorem 6.9 and Corollary 6.11 in the October 2026 revision, provides the separable quotient-tower obstruction and shows that \(\mathbb R\oplus_\infty\ell_1\) is not semiprojective and is \(2^+\)-projective. The present theorem makes the **sharp projectivity constant and semiprojectivity classification simultaneous for every normalized absolute norm**, not just the max-norm endpoint. The proof adapts their quotient model while retaining the full positive-pair ratio instead of a single endpoint test.

De Pagter and Wickstead's Theorem 11.8 supplies projectivity of countable \(\ell_1\) sums, used for the upper bound. Work on norm-attaining lattice homomorphisms under renorming investigates a different property and does not supply this lifting classification. No result here resolves whether arbitrary separable semiprojective Banach lattices must be \(1^+\)-projective or whether countable \(\ell_1\)-sums of arbitrary semiprojectives are semiprojective.

## Limitations

This is a classification **only** for the scalar-plus-countable-\(\ell_1\) absolute sums. It does not characterize general renormings of \(\ell_1\), higher-block absolute sums, or all semiprojective Banach lattices. Although relevant primary texts and research-record comparisons were inspected, publication priority under other terminology is not independently certified. The main lower-bound construction derives from the recent quotient-tower method and is acknowledged as such; the claim is the complete sharp absolute-norm classification, not the invention of the model.

## References

1. T. Kania and M. Niwiński, *Semiprojective Banach lattices*, arXiv:2604.10624v2, §6, Theorem 6.9 and Corollary 6.11, and §8 (2026). https://arxiv.org/abs/2604.10624
2. B. de Pagter and A. W. Wickstead, *Free and projective Banach lattices*, arXiv:1204.4282, Theorem 11.8; *Proc. R. Soc. Edinburgh Sect. A* 145 (2015), 105–143. https://arxiv.org/abs/1204.4282
3. E. Bilokopytov, E. García-Sánchez, D. de Hevia, G. Martínez-Cervantes and P. Tradacete, *Norm-attaining lattice homomorphisms and renormings of Banach lattices*, arXiv:2502.10165 (2025). https://arxiv.org/abs/2502.10165
