# Bounded radial Toeplitz symbols realize every U(n)-intertwiner for a logarithmic Fock weight

Let
\[
h(r)=
\begin{cases}
0,&0\le r\le 1,\\[2mm]
\frac12(\log r)^{3/2},&r>1,
\end{cases}
\]
and let \(\mathcal A_h(\mathbb C^n)\) be the radially weighted Fock space with density
\(e^{-2h(|z|)}\), for a fixed \(n\ge 1\).

For a bounded radial symbol \(\varphi(z)=a(|z|)\), Bdarneh's spectral formula gives
\[
T_\varphi|_{\mathcal P^m(\mathbb C^n)}
=\lambda_{\varphi,m}I,
\qquad
\lambda_{\varphi,m}
=
\frac{\int_0^\infty a(r)r^{2m+2n-1}e^{-2h(r)}\,dr}
{\int_0^\infty r^{2m+2n-1}e^{-2h(r)}\,dr}.
\]
Write
\[
\Lambda_n:L^\infty(0,\infty)\longrightarrow \ell^\infty(\mathbb N_0),
\qquad
\Lambda_n(a)=(\lambda_{\varphi,m})_{m\ge0}.
\]

## Theorem

For every \(n\ge1\), the map \(\Lambda_n\) is surjective. More strongly, it has a bounded
linear right inverse:
\[
\boxed{\exists\,R_n:\ell^\infty\to L^\infty(0,\infty)
\text{ bounded and linear such that }\Lambda_nR_n=I_{\ell^\infty}.}
\]

Consequently every bounded \(U(n)\)-intertwining operator on
\(\mathcal A_h(\mathbb C^n)\) is a single Toeplitz operator with a bounded radial symbol:
\[
\boxed{
\{T_\varphi:\varphi\in L^\infty(\mathbb C^n)^{U(n)}\}
=
\operatorname{End}_{U(n)}(\mathcal A_h(\mathbb C^n)).
}
\]
Under the homogeneous-degree decomposition, both sides are isometrically identified with
\(\ell^\infty(\mathbb N_0)\). Thus the set of bounded-radial-symbol Toeplitz operators is
already a \(C^*\)-algebra; no norm closure or algebra generation enlarges it. For \(n=1\),
this is the full diagonal masa relative to the normalized monomial basis.

## Proof

Set
\[
\alpha_m=2m+2n,\qquad
A_m=\int_0^\infty r^{\alpha_m-1}e^{-2h(r)}\,dr,
\qquad
k_m(r)=A_m^{-1}r^{\alpha_m-1}e^{-2h(r)}.
\]
Then \(k_m\ge0\) and \(\|k_m\|_{L^1}=1\), while
\[
(\Lambda_na)_m=\int_0^\infty a(r)k_m(r)\,dr.
\]

### 1. Asymptotically disjoint concentration windows

For \(r>1\), put \(u=\log r\). The exponent in the \(m\)-th moment becomes
\[
F_m(u)=\alpha_m u-u^{3/2},
\]
whose maximum occurs at
\[
u_m=\frac49\alpha_m^2.
\]
Let \(R_{-1}=0\) and, for \(m\ge0\),
\[
R_m=\exp\!\left[\frac49(\alpha_m+1)^2\right],
\qquad
E_m=[R_{m-1},R_m).
\]
For \(m\ge1\), the logarithmic endpoints of \(E_m\) are
\[
\frac49(\alpha_m-1)^2,\qquad \frac49(\alpha_m+1)^2.
\]

Write
\[
\delta_m=\int_{(0,\infty)\setminus E_m}k_m(r)\,dr.
\]
We claim that \(\delta_m\to0\). The argument is the same Laplace concentration mechanism
used in Bdarneh's one-dimensional alternating-symbol example, with
\(2m+2\) replaced by \(2m+2n\).

Indeed,
\[
F_m(u_m)=\frac4{27}\alpha_m^3,
\]
and at the two logarithmic endpoints one has
\[
F_m\!\left(\frac49(\alpha_m-1)^2\right)-F_m(u_m)
=-\frac4{27}(3\alpha_m-2),
\]
\[
F_m\!\left(\frac49(\alpha_m+1)^2\right)-F_m(u_m)
=-\frac4{27}(3\alpha_m+2).
\]
Moreover \(F_m'\ge1\) up to the lower endpoint and \(F_m'\le-1\) beyond the upper
endpoint. A unit interval around \(u_m\) gives
\[
A_m\ge e^{F_m(u_m)-1}
\]
for all sufficiently large \(m\). Hence the lower tail is bounded, up to a polynomial
factor in \(\alpha_m\), by
\[
\exp\!\left[-\frac4{27}(3\alpha_m-2)\right],
\]
and the upper tail by
\[
e\exp\!\left[-\frac4{27}(3\alpha_m+2)\right].
\]
The contribution of \(0<r<1\) is \(1/\alpha_m\), negligible compared with the same lower
bound for \(A_m\). Therefore \(\delta_m\to0\).

### 2. A compact perturbation of the identity on \(\ell^\infty\)

Define the isometric step-symbol embedding
\[
S:\ell^\infty\to L^\infty(0,\infty),
\qquad
S(a)(r)=a_m\quad(r\in E_m).
\]
Let
\[
T=\Lambda_nS:\ell^\infty\to\ell^\infty.
\]
For every \(a=(a_m)\in\ell^\infty\),
\[
|(Ta)_m-a_m|
=
\left|\int (S(a)-a_m)k_m\right|
\le 2\|a\|_\infty\delta_m.
\]
Thus \(K:=T-I\) maps the unit ball into sequences whose tails converge uniformly to zero.
If \(P_N\) denotes truncation to the first \(N\) coordinates, then \(P_NK\) is finite rank and
\[
\|K-P_NK\|\le 2\sup_{m>N}\delta_m\longrightarrow0.
\]
Hence \(K\) is compact and
\[
T=I+K
\]
is Fredholm. In particular \(\operatorname{ran}T\) is closed and has finite codimension in
\(\ell^\infty\).

Since \(\operatorname{ran}T\subseteq\operatorname{ran}\Lambda_n\), the linear space
\(\operatorname{ran}\Lambda_n\) contains a closed finite-codimensional subspace. Therefore
\(\operatorname{ran}\Lambda_n\) itself is closed and finite-codimensional.

### 3. The preadjoint has trivial kernel

Define
\[
J:\ell^1\to L^1(0,\infty),
\qquad
Jc=\sum_{m\ge0}c_mk_m.
\]
Because \(\|k_m\|_1=1\), \(J\) is bounded, and under the canonical dualities
\[
J^*=\Lambda_n.
\]

We show that \(J\) is injective. Suppose \(Jc=0\). After dividing by the common positive
factor \(r^{2n-1}e^{-2h(r)}\), we obtain almost everywhere
\[
\sum_{m\ge0}\frac{c_m}{A_m}r^{2m}=0.
\]
Consider
\[
g(z)=\sum_{m\ge0}\frac{c_m}{A_m}z^m.
\]
This series is entire. Indeed, for any \(\rho>0\), choose \(R>\max\{1,\sqrt\rho\}\).
Continuity of \(h\) on \([R,R+1]\) gives a constant \(C_R>0\) such that
\[
A_m\ge C_RR^{2m}.
\]
Hence for \(|z|\le\rho\),
\[
\sum_m\left|\frac{c_m}{A_m}z^m\right|
\le C_R^{-1}\sum_m|c_m|\left(\frac{\rho}{R^2}\right)^m<\infty.
\]
Thus \(g\) is entire and \(g(r^2)=0\) for almost every \(r>0\). The identity theorem yields
\(g\equiv0\), so \(c_m=0\) for every \(m\). Therefore \(\ker J=\{0\}\).

### 4. Closed range forces surjectivity

We already know that \(\operatorname{ran}J^*=\operatorname{ran}\Lambda_n\) is norm closed.
By the Banach-space closed range theorem, \(\operatorname{ran}J\) is closed. Since \(J\) is
injective, its inverse on its range is bounded: for some \(C<\infty\),
\[
\|c\|_1\le C\|Jc\|_1.
\]
Given any \(b=(b_m)\in\ell^\infty\), define on \(\operatorname{ran}J\)
\[
F_b(Jc)=\sum_{m\ge0}b_mc_m.
\]
Then
\[
|F_b(Jc)|\le C\|b\|_\infty\|Jc\|_1.
\]
Hahn--Banach extends \(F_b\) to \(L^1(0,\infty)\), so it is represented by some
\(a\in L^\infty(0,\infty)\). Consequently
\[
(\Lambda_na)_m=\int a(r)k_m(r)\,dr=b_m
\]
for every \(m\). Thus \(\Lambda_n\) is onto.

Finally, the Fredholm map \(T=\Lambda_nS\) has finite-dimensional kernel and cokernel.
Choose bounded complements to both, invert \(T\) on a complement of its kernel, and choose
preimages under \(\Lambda_n\) for a basis of the finite-dimensional cokernel. Combining
these two pieces gives a bounded linear right inverse \(R_n\).

## Operator-algebra consequence

Bdarneh proves for every radial weight in the paper's class that
\[
\operatorname{End}_{U(n)}(\mathcal A_h(\mathbb C^n))
\cong\ell^\infty(\mathbb N_0),
\]
with the \(m\)-th coordinate acting on the homogeneous polynomial block
\(\mathcal P^m(\mathbb C^n)\), and that bounded radial Toeplitz operators have exactly the
moment eigenvalues used above. The theorem therefore upgrades the general strong-operator
density result, for this logarithmic weight, to exact equality by a single bounded-symbol
Toeplitz operator.

This is a maximal contrast with the classical Gaussian Fock space. There, bounded radial
symbols produce eigenvalue sequences whose norm closure is the proper algebra of bounded
sequences uniformly continuous for the square-root metric. Here the bounded-symbol
eigenvalue map itself already reaches all of \(\ell^\infty\).

## Relation to prior work

- Bdarneh (2026), arXiv:2609.20652v1, proves the radial moment formula, general
  strong-operator density of invariant Toeplitz operators, and for the logarithmic weight
  constructs one bounded radial symbol whose eigenvalues approach \((-1)^m\). The result
  above promotes that concentration mechanism to arbitrary bounded target sequences and
  exact surjectivity.
- Esmeral--Maximenko (2016) identify the norm-closed algebra generated by bounded radial
  symbols in the classical Gaussian Fock space with the square-root-uniformly-continuous
  sequence algebra; this is the contrasting restrictive bounded-symbol regime.
- Grudsky--Vasilevski (2002), Theorem 3.7, already shows that every bounded sequence can be
  prescribed in the classical Fock space if one allows their larger symbol class
  \(L^\infty_1(\mathbb R_+,e^{-r^2})\), whose symbols are explicitly unbounded in general.
  That result is not a bounded-symbol surjectivity theorem.

## Limitations

The theorem is specific to the logarithmic weight above and to \(U(n)\)-radial symbols. It
does not characterize which other radial weights have the same surjectivity property, does
not give the optimal norm of a bounded right inverse, and does not assert uniqueness of the
representing bounded symbol. It also does not treat the multi-parameter quasi-radial
eigenvalue maps associated with proper block subgroups of \(U(n)\).

Originality is to the best of our knowledge.
