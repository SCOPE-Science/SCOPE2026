# Exponential collapse of negative type for rank-three finite Grassmann graphs

## Finding

Let \(q\ge2\) be a prime power and let \(n\ge6\). On the set \(\mathcal G_q(n,3)\) of all three-dimensional vector subspaces of \(\mathbb F_q^n\), define
\[
d(U,V)=3-\dim(U\cap V)\in\{0,1,2,3\}.
\]
For \(m\ge0\), put \([m]_q=(q^m-1)/(q-1)\). Introduce
\[
E=[3]_q,\qquad C=q^2[n-4]_q-E,\qquad A=(q+1)C+E,\qquad B=qC+E-1.
\]
Then \(C>0\), and there is exactly one \(\beta_{q,n}\in(0,1)\) satisfying
\[
\boxed{C-A2^{\beta_{q,n}}+B3^{\beta_{q,n}}=0.}
\]
For every real \(t>0\), the powered distance kernel \((d(U,V)^t)_{U,V}\) is conditionally negative semidefinite **if and only if** \(0<t\le\beta_{q,n}\). It is strictly conditionally negative definite for \(0<t<\beta_{q,n}\); at equality its mean-zero nullspace is exactly Grassmann harmonic degree two, of dimension \(\genfrac{[}{]}{0pt}{}{n}{2}_q-[n]_q\), and for \(t>\beta_{q,n}\) the kernel has a positive quadratic form on that harmonic space. Thus the metric \(d^{t/2}\) admits an isometric Hilbert embedding exactly for \(0<t\le\beta_{q,n}\).

For each fixed prime power \(q\), as \(n\to\infty\),
\[
\boxed{\lim_{n\to\infty}q^{n-2}\beta_{q,n}=\frac{q-1}{q\log3-(q+1)\log2}.}
\]
In contrast, for the ordinary three-subset Johnson space, its exchange distance is one-half squared Euclidean distance of indicator vectors and remains conditionally negative definite at exponent \(1\).

## Assumptions and scope

The finite-field order \(q\) may be even or odd, and \(n\ge6\) guarantees all four Grassmann harmonic sectors are present. Conditional negative semidefiniteness means \(\sum_{U,V}\overline{z_U}z_Vd(U,V)^t\le0\) for every complex coefficient vector with \(\sum_U z_U=0\). The all-zero diagonal is prescribed, including at exponent \(t=0\), which is not needed here. The parameter \(t\) is a real number, with no integrality restriction. Throughout, \(\genfrac{[}{]}{0pt}{}{a}{b}_q\) denotes the Gaussian binomial coefficient, with \(\genfrac{[}{]}{0pt}{}{a}{0}_q=1\).

## Proof

**1. Incidence and harmonic eigenvalues.** Let \(W_s\) be the inclusion matrix whose rows are indexed by three-subspaces \(U\) and columns by \(s\)-subspaces \(T\), with \(W_s(U,T)=\mathbf1_{\{T\subset U\}}\). Set \(H_s=W_sW_s^*\), so
\[
H_s(U,V)=\genfrac{[}{]}{0pt}{}{\dim(U\cap V)}{s}_q.
\]
The standard finite-field subspace-lattice up/down decomposition yields mutually orthogonal harmonic sectors \(\mathcal H_j\), \(0\le j\le3\), and the exact incidence eigenvalues
\[
H_s\big|_{\mathcal H_j}=\begin{cases}
q^{j(3-s)}\genfrac{[}{]}{0pt}{}{3-j}{s-j}_q\genfrac{[}{]}{0pt}{}{n-s-j}{3-s}_q I,&j\le s,\\
0,&j>s.
\end{cases}
\tag{1}
\]
For completeness, this follows by identifying \(W_s\) with the \(s\)-to-three divided up operator on the subspace lattice: up/down operators preserve each orthogonal symmetric Jordan chain, whose successive norm ratios are explicit Gaussian factors; multiplying their squared ratios gives (1). The chains indexed by rank \(j\) span \(\mathcal H_j\), which has dimension \(\genfrac{[}{]}{0pt}{}{n}{j}_q-\genfrac{[}{]}{0pt}{}{n}{j-1}_q\). The chain construction and its normalization are given in Srinivasan, arXiv:1304.6244v1, Theorem 1.2, equation (8); here the divided up operator counts each embedded \(s\)-subspace once.

The eigenvalues needed below are
\[
\begin{array}{c|ccc}
 &\mathcal H_1&\mathcal H_2&\mathcal H_3\\ \hline
H_1&q^2\genfrac{[}{]}{0pt}{}{n-2}{2}_q&0&0\\
H_2&q(q+1)[n-3]_q&q^2[n-4]_q&0.
\end{array}
\]

**2. Exact distance-power spectrum.** Write \(A_i(U,V)=\mathbf1_{\{d(U,V)=i\}}\) and \(J\) for the all-ones matrix. Counting common lines and planes gives the exact identities
\[
A_1=H_2-EI,\qquad A_2=H_1-(q+1)A_1-EI,\qquad A_3=J-I-A_1-A_2.
\]
For \(t>0\) put \(r=2^t\), \(s=3^t\), and define
\[
\alpha=1-(q+1)r+qs,\qquad \eta=r-s,\qquad \gamma=-s-E(\alpha+\eta).
\]
Then \(D_t=(d(U,V)^t)_{U,V}\) satisfies
\[
D_t=sJ+\alpha H_2+\eta H_1+\gamma I.
\]
By (1) its three mean-zero eigenvalues are
\[
\begin{aligned}
\mu_1&=\alpha q(q+1)[n-3]_q+\eta q^2\genfrac{[}{]}{0pt}{}{n-2}{2}_q+\gamma,\\
\mu_2&=\alpha q^2[n-4]_q+\gamma=C-A2^t+B3^t,\\
\mu_3&=\gamma.
\end{aligned}
\tag{2}
\]

**3. The sole obstruction.** For every \(q\ge2\) the number \(a_q=q\log3-(q+1)\log2\) is positive: it increases in \(q\), and at \(q=2\) equals \(\log(9/8)>0\). It follows that \(\alpha(0)=0\) and \(\alpha'(t)>0\) for all \(t\ge0\), hence \(\alpha>0\) for \(t>0\). Also \(\eta<0\) and \(\alpha+q\eta=1-2^t<0\).

Let \(h=q(q+1)+q^3[n-4]_q\), and \(\ell=q^2\genfrac{[}{]}{0pt}{}{n-2}{2}_q\). By Gaussian Pascal recursion with \(m=n-4\ge2\),
\[
\genfrac{[}{]}{0pt}{}{m+2}{2}_q
=\genfrac{[}{]}{0pt}{}{m+1}{2}_q+q^m[m+1]_q
>(q+1)+q^2[m]_q,
\]
so \(\ell>qh\). Therefore \(\mu_1-\mu_2=\alpha h+\eta\ell<0\). Likewise \(\mu_2-\mu_3=\alpha q^2[n-4]_q>0\). Thus \(\mu_2\) is strictly the largest mean-zero eigenvalue for every \(t>0\); all other harmonic sectors cannot determine the threshold.

Now \(C>0\) because already at \(n=6\), \(C=q^2(q+1)-(q^2+q+1)=q^3-q-1>0\). Moreover
\[
3B-2A=(q-2)C+E-3>0.
\]
Consequently \(B/A>2/3>\log2/\log3\), so \(\mu_2'(t)=B\log3\,3^t-A\log2\,2^t>0\) for all \(t\ge0\). Finally, \(\mu_2(0)=-1\) and \(\mu_2(1)=(q-1)C+E-3>0\). Hence (2) has a unique root \(\beta_{q,n}\in(0,1)\), with the asserted signs and nullspace. The finite-distance version of Schoenberg's theorem equates conditional negative definiteness of \(d^t\) with a squared Hilbert embedding of \(d^t\), proving the metric claim.

**4. Asymptotic.** For fixed \(q\), \(C\sim q^{n-2}/(q-1)\). The root identity rearranges as
\[
C\alpha(\beta_{q,n})=3^{\beta_{q,n}}-E(3^{\beta_{q,n}}-2^{\beta_{q,n}}).
\]
Since \(\alpha(t)>0\) for \(t>0\) and the right side is bounded for \(0<t<1\), necessarily \(\beta_{q,n}\to0\). Taylor expansion gives \(\alpha(t)=a_qt+O(t^2)\), and the right side is \(1+O(t)\); thus \(C\beta_{q,n}\to1/a_q\), which yields the displayed limit.

## Verification

Run the included `grassmann_check.py` with Python 3 and NumPy. It constructs all \(1\)-, \(2\)-, and \(3\)-dimensional subspaces of \(\mathbb F_2^6\) directly and verifies exact integer polynomial identities for both incidence Gram spectra, together with their traces and multiplicities. It separately checks existence and numerical location of the threshold for field orders \(2,3,4,5\) at five ambient dimensions each. The expected terminal line is `GRASSMANN_RANK_THREE_NEGATIVE_TYPE_CHECKS_PASS`. These computations corroborate (1)–(2) but are not used to extrapolate the theorem beyond verified parameters; all universal claims follow from the algebra above.

## Relationship to prior work

Srinivasan's subspace-lattice harmonic decomposition supplies the incidence singular values used in (1), and Marco–Parcet's Grassmann graph analysis develops the related Radon/q-Hahn machinery. Neither inspected paper states a power-negative-type threshold for this rank-three distance. The nonfield Johnson-graph analogue has a different incidence spectrum and, even at rank three, retains negative type at exponent \(1\). The new statement is the sharp power range, the unique critical harmonic degree, and the fixed-field exponential asymptotic—not the classical decomposition by itself.

## Limitations

No quantitative distortion assertion is made above the critical exponent, and the result does not classify the corresponding problem for rank greater than three. The existence of an earlier formulation via general association-scheme positivity or q-Hahn polynomials cannot be ruled out by the bounded literature comparison. The finite checker verifies only selected fields and dimensions; the full theorem rests on equation (1) and the inequalities proved here.

## References

- Murali K. Srinivasan, *The Goldman-Rota identity and the Grassmann scheme*, arXiv:1304.6244v1 (first publicly posted 2013-04-23), https://arxiv.org/abs/1304.6244.
- José Manuel Marco and Javier Parcet, *Laplacian operators and Radon transforms on Grassmann graphs*, arXiv:math/0404019 (2004 preprint), https://arxiv.org/abs/math/0404019.
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the AMS 44 (1938), 522–536 (classical Hilbert/negative-type correspondence).
