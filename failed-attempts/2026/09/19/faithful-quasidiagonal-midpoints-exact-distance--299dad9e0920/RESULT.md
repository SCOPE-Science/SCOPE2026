# Faithful quasidiagonal midpoints with an exact norm-distance profile

## Statement

Let \(A\) be the separable unital residually finite-dimensional \(C^*\)-algebra constructed by Mehdi Moradi in *Quasidiagonal traces need not form a face* (arXiv:2609.18793v1). Retain the complementary projections \(e^0,e^1\in A\), the coordinate traces \(\tau_m\), the ultralimit trace \(\tau_\infty\), the faithful trace
\[
\gamma=\sum_{m=0}^\infty 2^{-m-1}\tau_m,
\]
and the sector traces \(\mu_0,\mu_1\) from that construction. Thus
\[
e^0+e^1=1,\qquad
\mu_\varepsilon(e^\delta)=\delta_{\varepsilon\delta},
\qquad
\tau_\infty=\frac{\mu_0+\mu_1}{2}.
\]

Then both \(\tau_\infty\) and \(\gamma\) are quasidiagonal traces. For
\[
0\le c\le1,\qquad 0\le t\le1,
\]
define
\[
\omega_{c,t}
=(1-c)\gamma+c\bigl((1-t)\mu_0+t\mu_1\bigr).
\tag{1}
\]
The distance from \(\omega_{c,t}\) to the set \(T_{\mathrm{qd}}(A)\) of quasidiagonal tracial states is exactly
\[
\boxed{
\operatorname{dist}\bigl(\omega_{c,t},T_{\mathrm{qd}}(A)\bigr)
=c\,|2t-1|.
}
\tag{2}
\]

Consequently, for every \(0<c<1\):

1. every \(\omega_{c,t}\) is a faithful amenable tracial state;
2. the chord
   \[
   [\,\omega_{c,0},\omega_{c,1}\,]
   \]
   meets \(T_{\mathrm{qd}}(A)\) in exactly one point, its midpoint
   \[
   q_c:=\omega_{c,1/2}
   =(1-c)\gamma+c\tau_\infty;
   \tag{3}
   \]
3. \(q_c\) is a faithful quasidiagonal trace, while both endpoints are faithful, amenable, and non-quasidiagonal;
4. the two endpoints have the exact distance
   \[
   \operatorname{dist}(\omega_{c,0},T_{\mathrm{qd}}(A))
   =
   \operatorname{dist}(\omega_{c,1},T_{\mathrm{qd}}(A))
   =c.
   \tag{4}
   \]

Thus Moradi's example contains faithful non-quasidiagonal amenable traces at every prescribed norm distance \(c\in(0,1)\) from the quasidiagonal trace set, and each such pair can be chosen with a faithful quasidiagonal midpoint. The failure of the face property is therefore not merely asymmetric or boundary-supported: it persists on faithful trace chords with a sharp norm metric profile.

At \(c=1\), (2) also gives
\[
\operatorname{dist}(\mu_0,T_{\mathrm{qd}}(A))
=
\operatorname{dist}(\mu_1,T_{\mathrm{qd}}(A))
=1,
\qquad
T_{\mathrm{qd}}(A)\cap[\mu_0,\mu_1]
=
\left\{\frac{\mu_0+\mu_1}{2}\right\}.
\tag{5}
\]

## Proof

### 1. The weak-star closure used in Moradi's proof consists of quasidiagonal traces

Let \(\mathcal D\) be the normalized traces of finite direct sums of Moradi's coordinate representations \(\rho_m\), allowing repetitions, and let
\[
K=\overline{\mathcal D}^{\,w^*}\subseteq T(A).
\]
Moradi proves that \(K\) is convex, that \(\tau_\infty\in K\), and that
\(\gamma\in K\). His final diagonal approximation argument is written for the
particular trace
\[
\tau=\frac12(\tau_\infty+\gamma),
\]
but the argument applies verbatim to every element of \(K\).

Indeed, because \(A\) is separable, fix a norm-dense sequence
\((a_j)\) in its unit ball. If \(\lambda\in K\), then for each \(j\) there is
a finite-dimensional unital representation
\[
\theta_j:A\to M_{N_j}
\]
whose normalized trace agrees with \(\lambda\) within \(1/j\) on
\(a_1,\ldots,a_j\). Density gives pointwise trace convergence on all of
\(A\). Since every \(\theta_j\) is a *-homomorphism, its multiplicativity
defect is zero. Hence \(\lambda\) is quasidiagonal.

Therefore
\[
\boxed{K\subseteq T_{\mathrm{qd}}(A),}
\tag{6}
\]
and in particular
\[
\tau_\infty,\gamma\in T_{\mathrm{qd}}(A).
\tag{7}
\]

This is an implicit strengthening of the approximation step in Moradi's
Lemma 3.1, not a new general quasidiagonality criterion.

### 2. The sector difference is a norm-one separator for all quasidiagonal traces

Set
\[
h=e^1-e^0=2e^1-1.
\tag{8}
\]
The projections \(e^0,e^1\) are complementary, so \(h=h^*\),
\(h^2=1\), and
\[
\|h\|=1.
\tag{9}
\]

Moradi's Theorem 4.1 says that every quasidiagonal tracial state
\(\nu\) on \(A\) gives equal mass to the two sectors:
\[
\nu(e^0)=\nu(e^1)=\frac12.
\]
Hence
\[
\boxed{\nu(h)=0\qquad(\nu\in T_{\mathrm{qd}}(A)).}
\tag{10}
\]

On the other hand, Lemma 3.2 gives
\[
\mu_0(h)=-1,\qquad \mu_1(h)=1.
\tag{11}
\]
Each coordinate trace satisfies
\(\tau_m(e^0)=\tau_m(e^1)=1/2\), so
\[
\gamma(h)=0.
\tag{12}
\]
Combining (1), (11), and (12),
\[
\omega_{c,t}(h)=c(2t-1).
\tag{13}
\]

Therefore, for every \(\nu\in T_{\mathrm{qd}}(A)\),
\[
\|\omega_{c,t}-\nu\|
\ge
|(\omega_{c,t}-\nu)(h)|
=
c|2t-1|.
\]
Taking the infimum gives
\[
\operatorname{dist}\bigl(\omega_{c,t},T_{\mathrm{qd}}(A)\bigr)
\ge c|2t-1|.
\tag{14}
\]

### 3. The quasidiagonal midpoint attains the lower bound

By (7) and convexity of \(K\),
\[
q_c=(1-c)\gamma+c\tau_\infty\in K\subseteq T_{\mathrm{qd}}(A).
\tag{15}
\]
Using \(\tau_\infty=(\mu_0+\mu_1)/2\),
\[
\omega_{c,t}-q_c
=
c\left(t-\frac12\right)(\mu_1-\mu_0).
\tag{16}
\]

The norm of \(\mu_1-\mu_0\) is exactly \(2\). The upper bound \(2\) is
automatic for the difference of two states, while (9) and (11) give
\[
\|\mu_1-\mu_0\|
\ge
|(\mu_1-\mu_0)(h)|
=2.
\tag{17}
\]
Consequently,
\[
\|\omega_{c,t}-q_c\|
=
2c\left|t-\frac12\right|
=
c|2t-1|.
\tag{18}
\]
Since \(q_c\) is quasidiagonal, (18) is an upper bound for the distance to
\(T_{\mathrm{qd}}(A)\). Together with (14), this proves (2).

The unique-intersection assertion follows immediately: for \(c>0\), the
right side of (2) vanishes exactly at \(t=1/2\).

### 4. Faithfulness and amenability

Moradi proves that \(\gamma\) is faithful. If \(0\le c<1\), then every
trace \(\omega_{c,t}\) contains the positive coefficient \(1-c\) of
\(\gamma\). Thus for \(a\in A_+\setminus\{0\}\),
\[
\omega_{c,t}(a)
\ge
(1-c)\gamma(a)>0,
\]
so every \(\omega_{c,t}\) is faithful.

Quasidiagonal traces are amenable. Hence \(q_c\) is amenable. The set of
amenable traces is a face of the tracial state space. Since
\[
q_c=\frac12\omega_{c,0}+\frac12\omega_{c,1},
\tag{19}
\]
both endpoints are amenable. Every \(\omega_{c,t}\) is then a convex
combination of the endpoints, so the entire chord is amenable.

For \(0<c<1\), (2) shows that every point of the chord except its midpoint
is non-quasidiagonal. In particular the endpoints are faithful amenable
non-quasidiagonal traces at exact distance \(c\) from
\(T_{\mathrm{qd}}(A)\).

## Relation to Moradi's theorem

Moradi's stated Theorem 1.1 produces a faithful quasidiagonal trace with an
asymmetric decomposition
\[
\tau=\frac14\mu_1+\frac34\mu_2,
\qquad
\mu_1\notin T_{\mathrm{qd}}(A),
\]
which proves that quasidiagonal traces need not form a face. The body of the
paper separately constructs \(\tau_\infty,\gamma,\mu_0,\mu_1\), proves
\(\tau_\infty=(\mu_0+\mu_1)/2\), places \(\tau_\infty\) and \(\gamma\) in
the weak-star closure \(K\) of finite-dimensional representation traces,
and proves the universal sector-balance condition for quasidiagonal traces.

Combining those ingredients yields the stronger symmetric geometry above.
In particular, the same construction supplies:

- a quasidiagonal midpoint of two non-quasidiagonal traces;
- a faithful quasidiagonal midpoint of two faithful non-quasidiagonal
  traces;
- an exact norm-distance formula for the entire chord; and
- faithful amenable non-quasidiagonal traces at every distance
  \(c\in(0,1)\) from the quasidiagonal trace set.

The point is quantitative and geometric: the obstruction detected by the
sector unitary \(h=e^1-e^0\) is not merely enough to prove
non-quasidiagonality; together with the symmetric finite-dimensional
midpoint it computes the norm distance exactly.

## Limitations and originality boundary

This result concerns Moradi's specific 2026 RFD construction and does not
claim that arbitrary failures of the quasidiagonal-trace face property have
a symmetric chord, an exact distance formula, or faithful endpoints. It
does not characterize the whole set \(T_{\mathrm{qd}}(A)\); Theorem 4.1
only supplies the necessary sector-balance condition used here.

The diagonal observation \(K\subseteq T_{\mathrm{qd}}(A)\), the norm-two
distance of states supported on complementary projections, and the fact
that amenable traces form a face are standard or immediate ingredients and
are not claimed as new in isolation. The claimed contribution is their
synthesis inside Moradi's new example: the family (1), the exact distance
profile (2), the unique quasidiagonal midpoint on each chord, and the
faithful/amenable strengthening for every \(0<c<1\).

Originality is asserted only to the best of our knowledge. The full text of
arXiv:2609.18793v1 was inspected, including Lemmas 3.1--3.2, Theorem 4.1,
and the proof of Theorem 1.1. The paper explicitly notes that both
\(\mu_0\) and \(\mu_1\) are non-quasidiagonal, but it does not state a
midpoint theorem or a norm-distance result, and its stated main
decomposition is asymmetric. Searches for quasidiagonal traces together
with norm distance, midpoint decompositions, faithful non-quasidiagonal
components, affine hyperplanes, and equivalent trace-simplex terminology
did not locate this refinement.

The principal residual originality risk is that the elementary convex
geometry used here may have been recorded in older quasidiagonal-trace
literature in a general form. Brown's theory of amenable and
quasidiagonal traces and subsequent work were checked as background, but
older literature was not exhaustively searched for an abstract
``balanced projection + quasidiagonal midpoint'' lemma. Such a general
lemma would not by itself contain the specific faithful one-parameter
family extracted here from Moradi's 2026 construction.

## References

1. M. Moradi, *Quasidiagonal traces need not form a face*,
   arXiv:2609.18793v1 (2026).
   https://arxiv.org/abs/2609.18793
2. N. P. Brown, *Invariant means and finite representation theory of
   \(C^*\)-algebras*, Memoirs of the American Mathematical Society 184
   (2006), no. 865.
   https://doi.org/10.1090/memo/0865
