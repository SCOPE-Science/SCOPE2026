# Anticanonical positivity and core models of matrix-pencil Schubert surfaces

## Finding

Let \(Y_L\) be the normal Schubert surface of a two-dimensional complex matrix pencil \(L\). For each eigenvalue \(\lambda_i\) of its regular Kronecker component, write its **distinct** Jordan-block sizes as \(1\le k_{i,1}<\cdots<k_{i,h_i}\); their multiplicities do not enter the formulas. Put \(\kappa=\sum_i k_{i,h_i}\), with \(\kappa=0\) when there is no regular component.

**Theorem.** If the pencil is regular, then \(\kappa\ge2\), the anticanonical divisor of \(Y_L\) is nef and big, and
\[
(-K_{Y_L})^2=\frac{4\kappa}{\kappa-1}.
\]
It is ample if and only if \(h_i=1\) for every \(i\). Thus a regular pencil with two distinct Jordan-block sizes at any one eigenvalue produces a weak anticanonical surface that is not Fano.

If the pencil is singular, \(-K_{Y_L}\) is big and
\[
(-K_{Y_L})^2=9-\kappa.
\]
It is nef exactly when \(\kappa\le3\), and ample exactly when \(\kappa\le2\) and \(h_i=1\) for every eigenvalue \(\lambda_i\). For \(\kappa\ge3\), the Zariski decomposition of \(-K_{Y_L}\) is
\[
-K_{Y_L}=P+\frac{\kappa-3}{\kappa-1}C_\infty,
\qquad P^2=\frac{4\kappa}{\kappa-1},
\]
where \(C_\infty\) is the distinguished curve coming from the line at infinity. Here \(P\) is nef, big and semiample, with \(P\cdot C_\infty=0\); for \(\kappa=3\) the coefficient of \(C_\infty\) is zero. The anticanonical model for every singular pencil with \(\kappa\ge3\), and for every regular pencil, is isomorphic to the regular-pencil Schubert surface obtained by retaining **one Jordan block of maximal size at each eigenvalue**, with the same eigenvalues. This core surface has ample anticanonical divisor.

The term *nef and big* is used on these normal \(\mathbb Q\)-factorial quotient surfaces; when the divisor is not ample, this is the intended generalized weak-del-Pezzo condition.

## Assumptions and scope

Work over \(\mathbb C\). A matrix pencil is a two-dimensional linear subspace of rectangular matrices. The term *regular* means its generic member is square and invertible, whereas *singular* means otherwise in the Kronecker normal-form sense. The source proves the surface is normal with quotient singularities. Canonical divisors are \(\mathbb Q\)-Cartier, and their intersection products are defined on a smooth resolution.

The resolution described in [1, Theorem 3.2, Proposition 4.1 and Theorem 4.6] is the blow-up \(\pi:S\to\mathbb P^2\) of exactly \(\kappa\) successive (possibly infinitely near) points on the strict transform of the same line at infinity \(\ell_0\), forming one chain of length \(k_{i,h_i}\) over each distinct eigenvalue. Let \(H\) be the pullback of a line, \(E_{i,j}\) the *total-transform* exceptional basis, and \(\ell=H-\sum E_{i,j}\) the final strict transform of \(\ell_0\). The intersection form in this basis is \(H^2=1\), \(E_{i,j}^2=-1\), and all off-diagonal products vanish. The distinguished exceptional-chain curves have classes \(A_{i,j}=E_{i,j}-E_{i,j+1}\) for nonterminal \(j\), and \(A_{i,k_{i,h_i}}=E_{i,k_{i,h_i}}\).

The resolution morphism \(f:S\to Y_L\) contracts every \(A_{i,j}\) whose index \(j\) is *not* one of the Jordan-block sizes at its eigenvalue, and retains exactly the curves indexed by Jordan-block sizes. It also contracts \(\ell\) precisely for regular pencils; for singular pencils \(C_\infty=f(\ell)\) remains a curve. These statements are imported from [1], not independently new assertions.

## Proof

**Step 1 — canonical and intersection classes.** Adjunction for iterated point blow-ups gives
\[
-K_S=3H-\sum E_{i,j},\quad
\ell^2=1-\kappa,\quad
(-K_S)\cdot\ell=3-\kappa,\quad
(-K_S)^2=9-\kappa.
\]
For every nonterminal exceptional chain member, \((-K_S)\cdot A_{i,j}=0\); on each terminal exceptional curve it equals \(1\). The contracted nonterminal curves are \((-2)\)-curves, so their discrepancies vanish.

If the pencil is **regular**, the additional contracted curve \(\ell\) has discrepancy \((3-\kappa)/(\kappa-1)\). Indeed, writing \(K_S=f^*K_{Y_L}+a\ell\) plus the zero-discrepancy exceptional curves and intersecting with \(\ell\), we obtain \(a(1-\kappa)=\kappa-3\). Equivalently,
\[
 f^*(-K_{Y_L})
 =-K_S+\frac{3-\kappa}{\kappa-1}\ell
 =Q,
\quad Q=\frac{2}{\kappa-1}\left(\kappa H-\sum E_{i,j}\right).
\]
Hence \(Q^2=4\kappa/(\kappa-1)\) and \(Q\cdot\ell=0\). The same class \(Q\) will be useful in the singular case with \(\kappa\ge3\).

**Step 2 — positivity against every curve.** For any irreducible curve \(\Gamma\) on \(S\) other than \(\ell\) or an exceptional-chain curve, its image in \(\mathbb P^2\) has positive degree \(d\) and successive multiplicities \(m_{i,j}\). Because the original plane curve does not contain \(\ell_0\), the intersection of its final strict transform with \(\ell\) yields the elementary infinitely-near Bézout inequality
\[
 d-\sum_{i,j}m_{i,j}\ge0.
\]
Consequently,
\[
 (-K_S)\cdot\Gamma=3d-\sum m_{i,j}\ge2d>0,
\]
and, when \(\kappa\ge2\),
\[
 Q\cdot\Gamma
 =\frac{2}{\kappa-1}\left(\kappa d-\sum m_{i,j}\right)
 \ge2d>0.
\]
On nonterminal exceptional curves \(Q\) has intersection zero, and on terminal exceptional curves intersection \(2/(\kappa-1)>0\); it vanishes on \(\ell\). Thus \(Q\) is nef and big, with precisely these null curves. In the regular case, after disregarding curves contracted by \(f\), its null curves are exactly the retained non-maximal Jordan-size curves. The Nakai–Moishezon criterion for normal projective surfaces establishes the regular-pencil ampleness criterion.

**Step 3 — singular pencils.** Here \(f\) only contracts zero-discrepancy \((-2)\)-curves, so \(f^*(-K_{Y_L})=-K_S\), giving square \(9-\kappa\). The distinguished curve \(\ell\) is not contracted. By Step 2 all other curves have nonnegative anticanonical intersection, while \((-K_S)\cdot\ell=3-\kappa\). Thus \(-K_{Y_L}\) is nef precisely when \(\kappa\le3\), and ample precisely when \(\kappa\le2\) with no retained intermediate \((-2)\)-curve. Bigness for every \(\kappa\) follows from \(-K_S=2H+\ell\): \(2H\) is big and nef, \(\ell\) effective, so \(-K_S\) and hence \(-K_{Y_L}\) are big. In particular a negative value of \((-K_{Y_L})^2\) when \(\kappa>9\) does not contradict bigness, because the divisor has a fixed negative part.

For \(\kappa\ge3\), rearrangement of Step 1 gives
\[
-K_S=Q+\frac{\kappa-3}{\kappa-1}\ell.
\]
The coefficient is nonnegative, \(Q\) is nef, \(\ell\) has negative self-intersection, and \(Q\cdot\ell=0\). Therefore this is the Zariski decomposition on \(S\), and it descends under the crepant \(f\) to the formula on \(Y_L\). The positive part is big and its square is as stated.

**Step 4 — the anticanonical core.** Construct a **regular square pencil** with, at each eigenvalue, a *single* Jordan block of maximal size \(k_{i,h_i}\). Its blow-up resolution is the same \(S\) (the clusters depend only on the eigenvalues and their maximal lengths). By [1, Proposition 4.1], the morphism to this core surface contracts \(\ell\) and **every nonterminal** \(A_{i,j}\), but retains every terminal curve. Since the core has one block size at each eigenvalue, Step 2 proves its \(-K\) ample. Its anticanonical divisor pulls back to \(Q\). The Stein factorization/uniqueness of the contraction of the negative-definite null configuration shows that the morphism defined by sufficiently divisible positive-part sections is exactly this core contraction. For regular \(Y_L\), this is its anticanonical model; for singular \(Y_L\) with \(\kappa\ge3\), it is the anticanonical model of its Zariski positive part. This identifies the model as an abstract normal surface, not the original Plücker embedding.

The cases \(\kappa=0,1\) in the singular branch require no expression involving \(1/(\kappa-1)\): Step 3 alone proves their assertions.

## Verification

The accompanying `verify.py` performs exact rational intersection-form calculations on \(2014\) sample Kronecker-size patterns (all compositions and retained-size subsets through total maximal length \(7\), with up to four eigenvalues), and checks both pencil types. It verifies squares, discrepancy corrections, intersections with chain curves, null-curve classification and the Zariski positive-part formula. It does **not** enumerate all irreducible plane curves; the infinite positivity assertion rests instead on the Bézout argument in Step 2. Run `python3 verify.py` with the Python standard library.

## Relationship to prior work

The geometric resolution, the exceptional-curve dictionary, the normality/quotient-singularity result and the distinction between regular and singular pencil types are due to [1], especially Theorem 3.2 and Section 4. Those are explicitly used as premises. The new statement is the *global* canonical-positivity classification, both self-intersection formulas, the singular Zariski decomposition for all maximal block sums, and identification of the anticanonical core that forgets intermediate distinct block sizes. In particular, [1] exhibits a Hirzebruch surface of type \(\mathbb F_2\) for a special pencil, but does not formulate the present classification of all Jordan-size patterns. General Fano results about classical flag-variety Schubert subvarieties concern different objects and do not imply the statement here without the blow-up curve analysis.

## Limitations

This theorem only concerns complex **two-dimensional** matrix pencils and the abstract normal Schubert surfaces. It does not classify higher-dimensional matrix spaces, embeddings of anticanonical models, singularity baskets beyond those in [1], or positive characteristic. It relies on the cited resolution and its contraction dictionary. Historical originality relative to unpublished work or alternate terminology remains to be checked independently. No external independent mathematical validation has been performed.

## References

[1] Vincenzo Galgano, Fulvio Gesmundo and Hanieh Keneshlou, *Schubert compactifications of matrix pencils*, arXiv:2610.07164 (first submitted 2026-10-05), especially Theorem 3.2, Proposition 3.7, Proposition 4.1, Proposition 4.5, and Theorem 4.6. https://arxiv.org/abs/2610.07164
