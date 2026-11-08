# Sharp negative-type exponent of the rank-four symplectic dual polar metric

## Finding
Let \(q\ge2\) be a prime power. Let \(X_q\) consist of the maximal totally isotropic (Lagrangian) four-dimensional subspaces of a nondegenerate eight-dimensional symplectic vector space over \(\mathbb F_q\), and put \(d(U,V)=4-\dim(U\cap V)\). The **supremal negative-type exponent** \(\beta_q\) of this natural path metric is the unique number in \((0,1)\) satisfying
\[
-(q+1)(q^2+1)+q(q^2+1)(q^2+q+1)2^{\beta_q}
-q^3(q+1)(q^2+1)3^{\beta_q}+q^6 4^{\beta_q}=0.
\]
For every real \(t>0\), the powered distance matrix \((d(U,V)^t)_{U,V\in X_q}\) is conditionally negative semidefinite if and only if \(0<t\le\beta_q\). For \(0<t<\beta_q\) it is strictly conditionally negative definite. At \(t=\beta_q\), its mean-zero kernel is **exactly the fourth (last) primitive spectral component of the symplectic dual polar association scheme**; all other mean-zero spectral components remain negative. Equivalently, \(d^{t/2}\) admits an isometric Hilbert-space embedding exactly for \(0<t\le\beta_q\).

As \(q\) runs through growing prime powers,
\[
\boxed{\lim_{q\longrightarrow\infty}q^6\beta_q
=\frac1{\log(4/3)}.}
\]
The exponent thus tends to zero at the exact sixth-power rate in the field order. For illustration, \(\beta_2=0.1545203621597\ldots\), \(\beta_3=0.0104241433980\ldots\), and \(\beta_4=0.00144286903841\ldots\).

## Assumptions and scope
The field order \(q\) is any prime power, including characteristic two. The ambient symplectic form is nondegenerate and alternating, of Witt index four. Distinct vertices have distance one, two, three, or four, and the distance is the graph's shortest-path metric. We use the standard real conditional-negative-type convention: for real coefficients \((c_U)\) with \(\sum_U c_U=0\), one demands \(\sum_{U,V}c_Uc_V d(U,V)^t\le0\). Strictness means equality only for the zero vector of coefficients. At the endpoint, equality is characterized by the last primitive eigenspace; it is not claimed that this eigenspace is one-dimensional.

Let \([r]_q=(q^r-1)/(q-1)\). Denote by \(A_i\) the distance-\(i\) adjacency matrix for \(i=0,1,2,3,4\), so \(A_0=I\), and let \(E_j\), \(j=0,1,2,3,4\), be the primitive orthogonal spectral projectors in decreasing order of the eigenvalues of \(A_1\). Thus \(E_0\) projects onto constants and \(E_1+E_2+E_3+E_4=I-E_0\).

## Proof
**1. Known dual-polar spectral input and its normalization.** For the symplectic dual polar graph of rank four, the distance-regular intersection numbers are
\[
c_i=[i]_q,\qquad b_i=q^{i+1}[4-i]_q,\qquad a_i=(q-1)[i]_q,
\]
with \(b_4=0\), \(c_0=0\). The five eigenvalues of \(A_1\) are
\[
\theta_j=q[4-j]_q-[j]_q,\qquad 0\le j\le4.
\]
These are standard results from the dual-polar association scheme; their use is explicitly attributed to the cited literature. For each \(j\), define \(p_{0j}=1\), \(p_{1j}=\theta_j\), and recursively
\[
 p_{i+1,j}=\frac{(\theta_j-a_i)p_{ij}-b_{i-1}p_{i-1,j}}{c_{i+1}},\qquad i=1,2,3.
\]
The distance-regular identity \(A_1A_i=b_{i-1}A_{i-1}+a_iA_i+c_{i+1}A_{i+1}\) proves that \(A_iE_j=p_{ij}E_j\). Direct substitution yields the **complete nonconstant distance spectrum** (each displayed row lists the eigenvalues of \(A_1,A_2,A_3,A_4\) on \(E_j\)):
\[
\begin{array}{c|rrrr}
 j & A_1&A_2&A_3&A_4\\\hline
1&q^3+q^2+q-1&q(q-1)(q+1)(q^2+q+1)&q^3(q^3-q^2-q-1)&-q^6\\
2&q^2-1&-2q^2&-q^2(q^2-1)&q^4\\
3&-q^2-1&0&q^2(q^2+1)&-q^4\\
4&-(q+1)(q^2+1)&q(q^2+1)(q^2+q+1)&-q^3(q+1)(q^2+1)&q^6
\end{array}
\]
The omitted constant row is \(q(q+1)(q^2+1)\), \(q^3(q^2+1)(q^2+q+1)\), \(q^6(q+1)(q^2+1)\), and \(q^{10}\). All four nonconstant rows sum to \(-1\), as they must from \(\sum_{i=0}^4A_i=J\).

**2. The last primitive component strictly dominates every other nonconstant component.** Put \(\lambda_j(t)=\sum_{i=1}^4 i^t p_{ij}\), and write the positive successive increments
\[
 u=2^t-1,\quad v=3^t-2^t,\quad w=4^t-3^t\qquad(t>0).
\]
The spectral table gives
\[
\begin{split}
\lambda_4-\lambda_1&=2q[3]_q u+2q^6w,\\
\lambda_4-\lambda_2&=q(q+1)\bigl((q+1)u-q(q^2+1)v+q^3(q-1)w\bigr),\\
\lambda_4-\lambda_3&=q(q^2+1)\bigl(u-q(q+1)v+q^3w\bigr).
\end{split}
\]
The first difference is positive. For the others set \(x=2^t>1\) and \(\alpha=\log_2 3\). Because \(3^5=243<256=2^8\), one has \(1<\alpha<8/5\). Write \(y=x^{\alpha-1}\). Then
\[
 \frac{w}{v}=\frac{x^2-x^\alpha}{x^\alpha-x}
 =\frac{y^{1/(\alpha-1)}-y}{y-1}
 >\frac{2-\alpha}{\alpha-1}>\frac23.
\]
The first strict inequality follows because the secant slope of the convex function \(y\mapsto y^{1/(\alpha-1)}\) exceeds its tangent slope at one. For \(q\ge3\),
\[
 \frac{q(q^2+1)}{q^3(q-1)}\le\frac59<\frac23,
 \qquad \frac{q(q+1)}{q^3}\le\frac49<\frac23.
\]
Thus the second and third differences are positive already from the \(w,v\) terms, without using \(u>0\).

For \(q=2\), divide the second and third differences by their positive prefactors. Their bracketed quantities become, respectively,
\[
 g_2(t)=8\,4^t-18\,3^t+13\,2^t-3,\qquad
 g_3(t)=8\,4^t-14\,3^t+7\,2^t-1.
\]
Take \(z=2^{t/5}-1>0\). From \(3^t\le 2^{8t/5}\), the first is bounded below by
\[
8(1+z)^{10}-18(1+z)^8+13(1+z)^5-3
=z(82z^2-14z+1)+485z^4+1021z^5+1176z^6+816z^7+342z^8+80z^9+8z^{10}>0.
\]
Here \(82z^2-14z+1>0\), since its discriminant is negative. Similarly,
\[
g_3(t)\ge 3z+38z^2+246z^3+735z^4+1239z^5+1288z^6+848z^7+346z^8+80z^9+8z^{10}>0.
\]
Consequently \(\lambda_4(t)>\lambda_j(t)\) for every \(t>0\) and \(j=1,2,3\), uniformly in every prime power \(q\ge2\).

**3. Unique crossing and endpoint.** Let
\[
 F_q(x)=q^6x^2-q^3(q+1)(q^2+1)x^{\alpha}
 +q(q^2+1)(q^2+q+1)x-(q+1)(q^2+1).
\]
Then \(\lambda_4(t)=F_q(2^t)\). Write \(B=q^3(q+1)(q^2+1)\), so \(B/q^6=(1+q^{-1})(1+q^{-2})\le15/8\). For every \(x\ge1\),
\[
 F_q''(x)=2q^6-B\alpha(\alpha-1)x^{\alpha-2}
 >2q^6-\frac{15}{8}\frac{24}{25}q^6=\frac15q^6>0.
\]
Moreover, since \(\alpha<8/5\),
\[
 F_q'(1)>2q^6-\frac85B+q(q^2+1)(q^2+q+1)
 =\frac{q(q+1)}5\left(q^2(2q-1)(q-2)+5\right)>0.
\]
Thus \(F_q\) increases strictly on \([1,\infty)\). The exact table gives \(F_q(1)=-1\), while
\[
 F_q(2)=(q-1)^3(q+1)(q^2+q+1)>0.
\]
There is therefore exactly one \(\beta_q\in(0,1)\) with \(\lambda_4(\beta_q)=0\). By step 2 the entire mean-zero spectral space is negative for \(0<t<\beta_q\), negative semidefinite with kernel \(E_4\) at \(t=\beta_q\), and has a positive eigenvalue for \(t>\beta_q\). This is precisely the claimed negative-type classification. The Hilbert-embedding equivalence follows from Schoenberg's finite negative-type criterion.

**4. Sixth-power asymptotic.** Directly from the formula,
\[
 \lambda_4'(0)=q^6\log(4/3)+O(q^5),\qquad
 \sup_{0\le t\le1}|\lambda_4''(t)|=O(q^6).
\]
The convexity bound from step 3 and \(\lambda_4(\beta_q)=0\) first show \(\beta_q=O(q^{-6})\). Taylor's theorem then gives
\[
 0=-1+\beta_q\{q^6\log(4/3)+O(q^5)\}+O(q^6\beta_q^2),
\]
which implies \(q^6\beta_q\to1/\log(4/3)\). All error estimates are uniform as \(q\to\infty\) through prime powers.

## Verification
The standalone program `verify.py` recomputes the full five-by-five eigenvalue table from the exact distance-regular three-term recurrence and compares it to independent closed-form expressions for eight field orders (including nonprime prime powers). It checks spectral ordering at several exponents, sum rules, and the total Lagrangian count. Separately, it constructs all \(2295\) Lagrangian four-subspaces of \(\mathbb F_2^8\) by exact binary symplectic transvections, verifies isotropy, recovers the layer sizes \(1,30,280,960,1024\), and checks the intersection numbers in representative layers. The reported output is `SYMPLECTIC_DUAL_POLAR_FOURTH_METRIC_PASS`. These are finite checks supporting, not replacing, the uniform symbolic argument.

## Relationship to prior work
The dual-polar scheme's incidence parameters, distance recursion, and basic spectrum are classical; see the discussion and references of Worawannotai's 2012 paper, especially Section 16. Murugan's 2011 general theorem gives the determinant-zero characterization of generalized roundness for vertex-transitive metrics. The present calculation **specializes that general principle and completes the nontrivial spectral comparison**: for this rank-four symplectic metric the final primitive component, not a priori distinguished by the general criterion, is uniquely critical for all prime powers and all positive exponents, with an explicit one-root equation and a sharp sixth-power asymptotic. No authorship or independent priority certification is claimed.

## Limitations
The theorem concerns symplectic dual-polar rank exactly four, not other ranks or the Hermitian/orthogonal polar families. It classifies negative type and Hilbert embeddability, not the multiplicities of the primitive spectral components. Historical priority remains uncertain despite targeted comparison with the cited spectral and generalized-roundness literature and searchable research records; a more general previously published theorem could subsume it. The numerical examples and finite graph enumeration do not constitute an independent proof of the entire prime-power family.

## References
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first posted 2011-12-23), particularly Sections 2–3. https://arxiv.org/abs/1112.5657
- C. Worawannotai, *Dual polar graphs, the quantum algebra U_q(sl_2), and Leonard systems of dual q-Krawtchouk type*, arXiv:1205.2144 (first posted 2012-05-10), especially Section 16. https://arxiv.org/abs/1205.2144
- A. E. Brouwer, A. M. Cohen and A. Neumaier, *Distance-Regular Graphs*, Springer (1989), Section 9.4, cited for classical scheme data through the source above. Date to day precision not established here.
