# Quantitative Bézout stability forces Banach–Mazur proximity to a simplex

## Statement

Let \(K\subset\mathbb R^n\) be a full-dimensional convex body, \(n\ge 2\). For a unit vector \(v\), write \(\ell_K(v)\) for the length of a longest chord of \(K\) parallel to \(v\), and for \(0<s<\ell_K(v)\) put
\[
K_v^s:=K\cap(K-sv).
\]
Define the restricted chord-intersection Bézout constant
\[
 b_{\rm ch}(K):=
 \sup_{v\in S^{n-1}}\sup_{0<s<\ell_K(v)}
 \frac{V(K)\,V(K[n-2],K_v^s,[0,v])}
 {V(K[n-1],K_v^s)\,V(K[n-1],[0,v])}.
\]
Fenchel's mixed-volume inequality gives \(b_{\rm ch}(K)\le 2\), while letting \(s\downarrow0\) gives \(b_{\rm ch}(K)\ge1\). Langharst and Wang proved in 2026 that \(b_{\rm ch}(K)=1\) already forces \(K\) to be a simplex.

For \(c\ge1\), set
\[
 \lambda_n(c):=1-\bigl(1-c^{-(n-1)}\bigr)^{1/n}
\]
and
\[
 \Psi_n(c):=
 c^{-(n-1)}\lambda_n(c)^n.
\]
Then the following quantitative strengthening holds.

**Theorem.** If \(b_{\rm ch}(K)\le c\), then:

1. For every \(v\in S^{n-1}\),
   \[
   \frac{\ell_K(v)V(K[n-1],[0,v])}{V(K)}\ge \lambda_n(c).
   \]
   More precisely, if \(b_{\rm ch}(K;v)\) denotes the supremum in the definition of \(b_{\rm ch}\) with \(v\) fixed and
   \[
   q_K(v):=\frac{\ell_K(v)V(K[n-1],[0,v])}{V(K)},
   \]
   then
   \[
   b_{\rm ch}(K;v)
   \ge \bigl[1-(1-q_K(v))^n\bigr]^{-1/(n-1)}.
   \]

2. The difference body \(DK:=K+(-K)\) satisfies the near-equality estimate
   \[
   \boxed{
   \frac{V(DK)}{\binom{2n}{n}V(K)}\ge \Psi_n(c).
   }
   \]

3. Let \(d_\triangle(K)\) be the Banach–Mazur distance from \(K\) to the class of simplices, in the normalization used in the Rogers–Shephard stability theorem. Then
   \[
   \boxed{
   d_\triangle(K)
   \le 1+n^{50n^2}\bigl(1-\Psi_n(c)\bigr).
   }
   \]
   In particular, as \(\varepsilon\downarrow0\),
   \[
   b_{\rm ch}(K)\le1+\varepsilon
   \quad\Longrightarrow\quad
   d_\triangle(K)-1
   =O_n(\varepsilon^{1/n}),
   \]
   and more explicitly, for \(0\le\varepsilon\le1\),
   \[
   d_\triangle(K)-1
   \le n^{50n^2}
   \Bigl((n-1)+n(n-1)^{1/n}\Bigr)\varepsilon^{1/n}.
   \]

Thus approximate validity of only the special chord-intersection tests used in the recent characterization already forces quantitative affine proximity to a simplex.

There is also a relative-inradius consequence for the full two-body Bézout constant. Let \(b_2(K)\) be the smallest \(c\) such that
\[
 V(K)V(K[n-2],A,B)
 \le c\,V(K[n-1],A)V(K[n-1],B)
\]
for all convex bodies \(A,B\). If \(b_2(K)\le c\), then every full-dimensional convex body \(M\) satisfies
\[
 \boxed{
 \frac{r(K,M)V(K[n-1],M)}{V(K)}\ge\lambda_n(c),
 }
\]
where \(r(K,M)=\max\{t\ge0:z+tM\subset K\text{ for some }z\}\) is the relative inradius.

## Proof

### 1. A quantitative longest-chord estimate

Fix \(v\in S^{n-1}\), abbreviate \(\ell=\ell_K(v)\), \(K^s=K_v^s\), and let
\[
 P=V_{n-1}(P_{v^\perp}K),\qquad
 P_s=V_{n-1}(P_{v^\perp}K^s).
\]
The projection formula gives
\[
 V(K[n-1],[0,v])=\frac Pn.
\]
Write \(c_v=b_{\rm ch}(K;v)\). The defining inequality for \(c_v\), together with
\[
 K^s+[0,sv]\subset K,
\]
gives
\[
 V(K[n-2],K^s,[0,v])
 \le c_v\frac{P}{n}
 \left(1-\frac{Ps}{nV(K)}\right).
\]
Applying the projection formula once more and then the \((n-1)\)-dimensional Minkowski inequality yields
\[
 P_s\le
 c_v^{\,n-1}P
 \left(1-\frac{Ps}{nV(K)}\right)^{n-1}.
 \tag{1}
\]
The layer-cake identity along the direction \(v\) is
\[
 V(K)=\int_0^\ell P_s\,ds.
\]
Set
\[
 q=\frac{\ell P}{nV(K)}
 =\frac{\ell V(K[n-1],[0,v])}{V(K)}.
\]
Integrating (1) gives
\[
 1\le c_v^{\,n-1}\bigl[1-(1-q)^n\bigr].
 \tag{2}
\]
The standard inclusion
\[
 \left(1-\frac{s}{\ell}\right)K+z_s\subset K^s
\]
for a suitable translation \(z_s\) gives \(P_s\ge(1-s/\ell)^{n-1}P\); after integration this implies \(0<q\le1\). Hence (2) is equivalent to
\[
 q\ge1-\bigl(1-c_v^{-(n-1)}\bigr)^{1/n},
\]
which proves the first assertion and its directional refinement.

### 2. From the special Bézout tests to Rogers–Shephard near-equality

Let
\[
 g_K(x):=V(K\cap(K+x))
\]
be the covariogram. The same layer-cake identity gives, for \(0\le t\le\ell\),
\[
 g_K(-tv)=\int_t^\ell P_s\,ds.
\]
Using (1), now with any \(c\ge b_{\rm ch}(K)\), and writing \(t=r\ell\), one obtains
\[
 \frac{g_K(-r\ell v)}{V(K)}
 \le c^{n-1}
 \left[(1-qr)^n-(1-q)^n\right],
 \qquad 0\le r\le1.
 \tag{3}
\]
The radial function of the difference body \(DK\) in the direction \(-v\) is \(\ell_K(v)\). Since
\[
 \int_{\mathbb R^n}g_K(x)\,dx=V(K)^2,
\]
polar integration and (3) give
\[
 V(K)
 \le n c^{n-1}V(DK)\,I_n(q_*),
\]
where the directional lower bound permits \(q_*\ge\lambda_n(c)\), and
\[
 I_n(q)
 :=\int_0^1\left[(1-qr)^n-(1-q)^n\right]r^{n-1}\,dr.
\]
A one-variable calculation gives
\[
 I_n(q)
 =q\int_0^1 s^n(1-qs)^{n-1}\,ds
 =q^{-n}\int_0^q y^n(1-y)^{n-1}\,dy
 \le q^{-n}B(n+1,n).
\]
Since
\[
 nB(n+1,n)=\binom{2n}{n}^{-1},
\]
we obtain
\[
 V(K)
 \le
 \frac{c^{n-1}\lambda_n(c)^{-n}}{\binom{2n}{n}}V(DK),
\]
which rearranges to
\[
 \frac{V(DK)}{\binom{2n}{n}V(K)}
 \ge c^{-(n-1)}\lambda_n(c)^n
 =\Psi_n(c).
\]

### 3. Banach–Mazur stability

The Rogers–Shephard inequality says
\[
 V(DK)\le\binom{2n}{n}V(K),
\]
with equality exactly for simplices. Böröczky's quantitative stability theorem states that if
\[
 V(DK)=(1-\delta)\binom{2n}{n}V(K),
\]
then
\[
 d_\triangle(K)\le1+n^{50n^2}\delta.
\]
The preceding estimate gives
\[
 \delta\le1-\Psi_n(c),
\]
which proves the stated Banach–Mazur bound.

For \(c=1+\varepsilon\),
\[
 1-\Psi_n(1+\varepsilon)
 =n(n-1)^{1/n}\varepsilon^{1/n}
 +O_n(\varepsilon^{2/n}).
\]
For \(0\le\varepsilon\le1\), the elementary estimates
\[
 1-(1+\varepsilon)^{-(n-1)}\le(n-1)\varepsilon
\]
and \(1-(1-x)^n\le nx\) give
\[
 1-\Psi_n(1+\varepsilon)
 \le\Bigl((n-1)+n(n-1)^{1/n}\Bigr)\varepsilon^{1/n}.
\]
This proves the explicit coarse modulus.

Equivalently, any body at a fixed Banach–Mazur distance from every simplex must violate at least one of the special chord-intersection Bézout tests by a definite amount:
\[
 b_{\rm ch}(K)-1
 \ge
 \left(
 \frac{d_\triangle(K)-1}
 {n^{50n^2}\bigl((n-1)+n(n-1)^{1/n}\bigr)}
 \right)^n
\]
whenever the right-hand side is in the range covered by the preceding estimate.

### 4. Relative-inradius stability for the full Bézout constant

Assume \(b_2(K)\le c\) and let \(M\) be full-dimensional. For
\[
 K_s:=K\ominus sM
 =\{x:x+sM\subset K\},
 \qquad 0\le s\le r(K,M),
\]
the same Aleksandrov–Fenchel/Minkowski argument used in the exact characterization, with the factor \(c\) retained, gives
\[
 V(K_s[n-1],M)
 \le
 c^{n-1}\frac{V(K[n-1],M)}{V(K)^{n-1}}
 \left(V(K)-sV(K[n-1],M)\right)^{n-1}.
\]
Integrating the inner-parallel-body identity and normalizing
\[
 \rho=\frac{r(K,M)V(K[n-1],M)}{V(K)}
\]
therefore gives
\[
 1\le c^{n-1}\bigl[1-(1-\rho)^n\bigr].
\]
Since \(0<\rho\le1\), this yields \(\rho\ge\lambda_n(c)\).

## Relation to prior work

Soprunov and Zvavitch introduced the mixed-volume Bézout inequality and conjectured that the sharp constant-one inequality characterizes simplices. Several subsequent papers established the conjecture for important subclasses or related formulations. Langharst and Wang proved the conjecture for all full-dimensional convex bodies in September 2026 and, crucially for the result above, showed that it is enough to test the special pairs \(A=[0,v]\), \(B=K\cap(K-sv)\). Their proof also gives exact longest-chord and relative-inradius characterizations.

The present result retains a constant \(c\ge1\) through those inequalities, converts it to an explicit deficit in the Rogers–Shephard difference-body inequality, and then invokes Böröczky's stability theorem to obtain Banach–Mazur proximity to a simplex. The Rogers–Shephard stability theorem itself is prior work; the claimed contribution here is the quantitative bridge from the restricted Bézout tests to Rogers–Shephard near-equality, together with the resulting explicit stability modulus and the corresponding quantitative chord and inradius bounds.

## Limitations

The exponent \(1/n\) and all displayed constants are not claimed to be optimal. The Banach–Mazur coefficient \(n^{50n^2}\) is inherited from the available Rogers–Shephard stability theorem and is very large. No converse quantitative estimate from Banach–Mazur proximity to \(b_{\rm ch}(K)-1\) is asserted beyond the contrapositive of the stated bound. The relative-inradius estimate uses the full two-body Bézout constant \(b_2(K)\), whereas the Banach–Mazur stability theorem needs only the restricted chord-intersection tests. Originality is asserted only to the best of our knowledge; differently formulated or not-yet-indexed work may contain related quantitative estimates.

## References

- D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380 (2026). https://arxiv.org/abs/2609.20380
- K. Böröczky Jr., *The stability of the Rogers–Shephard inequality and of some related inequalities*, Advances in Mathematics 190 (2005), 47–76. https://doi.org/10.1016/j.aim.2003.11.015
- I. Soprunov and A. Zvavitch, *Bezout Inequality for Mixed Volumes*, International Mathematics Research Notices 2016, 7230–7252. https://doi.org/10.1093/imrn/rnv390
- C. Saroglou, I. Soprunov and A. Zvavitch, *Characterization of Simplices via the Bezout Inequality for Mixed Volumes*, Proceedings of the American Mathematical Society 144 (2016), 5333–5340. https://doi.org/10.1090/proc/13149
