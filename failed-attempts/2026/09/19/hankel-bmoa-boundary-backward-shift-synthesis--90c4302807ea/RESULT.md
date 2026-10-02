# Backward-shift orbit synthesis has an exact Hankel--BMOA boundary

## Statement

Let \(H^2=H^2(\mathbb D)\), let \(S^*\) be the backward shift, and for
\(f(z)=\sum_{j\ge 0}\beta_j z^j\) put
\[
f^\sharp(z)=\overline{f(\overline z)}=\sum_{j\ge0}\overline{\beta_j}z^j.
\]
For \(g(z)=\sum_{k\ge0}\alpha_k z^k\in H^2\), define initially on analytic
polynomials
\[
L_g^0 f
   =\sum_{m\ge0}\langle (S^*)^m g,f^\sharp\rangle z^m.
\]
Then the \(m\)-th Taylor coefficient is
\[
\widehat{L_g^0 f}(m)=\sum_{j\ge0}\alpha_{m+j}\beta_j.
\]
Thus \(L_g^0\) is exactly the analytic Hankel operator with Hankel matrix
\[
(\alpha_{m+j})_{m,j\ge0}.
\]

Consequently, by the classical Nehari--Fefferman theorem,
\[
\boxed{L_g^0\text{ extends boundedly }H^2\to H^2
       \iff g\in \mathrm{BMOA}.}
\]
For a general \(g\in H^2\), the correct everywhere-free formulation is the
maximal Hankel domain
\[
\mathcal D_g
 =\left\{f=\sum_{j\ge0}\beta_jz^j\in H^2:
     \left(\sum_{j\ge0}\alpha_{m+j}\beta_j\right)_{m\ge0}\in\ell^2\right\}.
\]
The corresponding operator is closed and densely defined, and analytic
polynomials form a core. These domain facts are standard; they are included
only to state the sharp correction.

## Explicit counterexample

Take
\[
g(z)=f(z)=\sum_{n=0}^\infty (n+1)^{-2/3}z^n.
\]
Both \(f\) and \(g\) belong to \(H^2\), since
\[
\sum_{n\ge0}(n+1)^{-4/3}<\infty.
\]
If \(c_m\) is the formal \(m\)-th coefficient of \(L_g f\), then
\[
c_m
 =\sum_{j=0}^\infty
   (j+1)^{-2/3}(m+j+1)^{-2/3}.
\]
For \(m\ge1\), restricting the sum to \(0\le j\le m\) gives
\[
c_m
 \ge (m+1)(m+1)^{-2/3}(2m+1)^{-2/3}
 \ge C m^{-1/3}
\]
with an absolute constant \(C>0\). Hence
\[
\sum_{m\ge1}|c_m|^2
 \ge C^2\sum_{m\ge1}m^{-2/3}
 =\infty.
\]
Therefore
\[
f\notin\mathcal D_g,\qquad L_g f\notin H^2.
\]

More generally, for
\[
g_a=f_a=\sum_{n\ge0}(n+1)^{-a}z^n,
\qquad \frac12<a\le\frac34,
\]
one has \(f_a,g_a\in H^2\) and
\[
\widehat{L_{g_a}f_a}(m)\gtrsim m^{1-2a},
\]
so the output again fails to lie in \(H^2\). This supplies a continuum of
counterexamples, including the endpoint \(a=3/4\).

## Consequence for arXiv:2609.19311v1

Lemma 2.1 of Ferreira--do Carmo, *Projections and minimal invariant subspaces
in the Hardy space over the bidisk* (arXiv:2609.19311v1), asserts that the
same formula defines an operator \(L_g:H^2\to H^2\) for every \(g\in H^2\).
Its proof identifies
\[
L_g f=\sum_{j\ge0}\beta_j(S^*)^jg
\]
and then asserts that this orbit-synthesis map is bounded on \(\ell^2\).
The counterexample above shows that this assertion is false. The sharp
boundedness condition is \(g\in\mathrm{BMOA}\), not merely \(g\in H^2\).

This is not only a defect in the proof of the lemma. Proposition 2.2 uses
\(L_g(h)\), \(L_{P_m(u)}(h)\), and the series
\[
\sum_{j\ge0}h_j(T_z^*)^ju
\]
without establishing that the chosen vectors lie in the relevant maximal
domains or that the corresponding orbit-synthesis series converges. Hence
the proof of Proposition 2.2 does not follow from the stated hypotheses.

The paper's subsequent projection-rigidity chain passes through Proposition
2.2: Corollary 2.3 uses it directly; Lemma 2.5 reduces to Proposition 2.2;
Corollary 2.6 uses Lemma 2.5; and Theorem 2.7 uses Corollary 2.6. Therefore
these later conclusions are not established by the current argument.

This record does **not** claim that Proposition 2.2, Corollaries 2.3 and 2.6,
Lemma 2.5, or Theorem 2.7 are false. It establishes that the stated proof
route has a genuine domain/boundedness gap.

## The same synthesis gap in the 2024 precursor

The same authors' 2024 paper *On the Invariant Subspace Problem via Universal
Toeplitz Operators on the Hardy Space Over the Bidisk* contains the analogous
step in Lemma 15: from
\[
\|(t_\varphi^*)^n g\|\le \|g\|
\]
for an inner \(\varphi\), it concludes that
\[
\sum_{n\ge0}\beta_n(t_\varphi^*)^n g
\]
is defined for every \(\beta\in\ell^2\). Uniform boundedness of the individual
orbit vectors does not imply that the orbit is a Bessel sequence.

For the special inner function \(\varphi(z)=z\), take
\[
M=H^2(\mathbb D^2),\qquad
u(z,w)=g(z)
\]
with the explicit \(g\) above, and
\[
\beta_n=(n+1)^{-2/3}.
\]
Then \(\beta\in\ell^2\), but the claimed synthesis series is exactly the
non-\(H^2\) Hankel output above (in the \(w^0\) slice). Thus Lemma 15's
unrestricted \(\ell^2\)-synthesis assertion is also false as stated.

## Correct replacement

For the one-variable backward shift, the exact replacement is:
\[
\boxed{
\{(S^*)^j g:j\ge0\}\text{ admits bounded }\ell^2
\text{ synthesis}
\iff g\in\mathrm{BMOA}.
}
\]
Equivalently, the backward-shift orbit of \(g\) is a Bessel sequence exactly
for \(g\in\mathrm{BMOA}\).

For arbitrary \(g\in H^2\), one may still work with the canonical closed
Hankel operator on \(\mathcal D_g\), but every use of \(L_g(h)\) must then
verify \(h\in\mathcal D_g\). In the bidisk argument one must additionally
verify convergence of the vector-valued orbit synthesis used to construct an
element of \(M\). Scalar BMOA membership of a single slice alone does not
supply that vector-valued convergence.

## Prior literature and originality boundary

The Hankel-matrix identification and the equivalence
\[
\text{bounded Hankel operator}\iff \mathrm{BMOA}\text{ symbol}
\]
are classical and are **not** claimed as new. Nehari's 1957 theorem is the
classical bounded-Hankel input. Gérard--Pushnitski (2022) explicitly treat
Hankel symbols \(u\in H^2\), emphasize that such operators can be unbounded,
state the BMOA boundedness criterion, and prove that the maximal Hankel
operator is closed with polynomials as a core.

The contribution here is the paper-specific diagnosis: identifying the
operator in arXiv:2609.19311v1 with that classical Hankel operator, giving a
fully explicit \(H^2\)-counterexample to Lemma 2.1, locating the exact BMOA
boundary, and tracing the resulting gap through the paper's projection-rigidity
argument. The same explicit example also falsifies the unrestricted
orbit-synthesis step in Lemma 15 of the 2024 precursor.

Searches by the current arXiv identifier, title, lemma number, authors,
"Hankel", "BMOA", "correction", and "erratum" did not locate a public
correction of these specific statements. Originality is therefore asserted
only to the best of our knowledge.

## Limitations

This record does not disprove the projection-rigidity conclusions of
arXiv:2609.19311v1, and it does not settle the invariant subspace problem.
It does not classify vector-valued orbit synthesis for \(T_z^*\) on the bidisk.
The BMOA characterization itself is classical rather than a new theorem.

## References

1. M. dos Santos Ferreira and J. M. Ribeiro do Carmo, *Projections and minimal invariant subspaces in the Hardy space over the bidisk*, arXiv:2609.19311v1, 2026.
2. J. M. R. do Carmo and M. S. Ferreira, *On the Invariant Subspace Problem via Universal Toeplitz Operators on the Hardy Space Over the Bidisk*, Bull. Braz. Math. Soc. (N.S.) 55 (2024), Article 12; arXiv:2309.03427.
3. Z. Nehari, *On bounded bilinear forms*, Ann. of Math. (2) 65 (1957), 153--162. DOI: 10.2307/1969670.
4. P. Gérard and A. Pushnitski, *Unbounded Hankel operators and the flow of the cubic Szegő equation*, Invent. Math. (2022). DOI: 10.1007/s00222-022-01176-z.
