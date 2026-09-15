# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Essential spectral gap with a round circle in the limit set — disproof of the target

## 1. Target restated

Let $X=\Gamma\backslash\mathbb H^3$ be convex cocompact (torsion-free, so a
manifold) whose limit set $\Lambda_\Gamma\subset S^2$ contains a round circle.
The target asks whether there exist $C_0,\beta>0$ (depending on $X$ at most)
such that the cutoff resolvent
$$
R(\lambda)=(-\Delta-1-\lambda^2)^{-1}:
L^2_{\mathrm{comp}}(X)\to L^2_{\mathrm{loc}}(X),
$$
a priori holomorphic for $\Im\lambda>1$, continues holomorphically to
$$
\mathcal U=\{|\lambda|>C_0,\ \Im\lambda>-\beta\}
$$
and satisfies, for every compactly supported cutoff $\chi$,
$$
\|\chi R(\lambda)\chi\|\le C_{\chi,\epsilon}
|\lambda|^{-1-2\min(0,\Im\lambda)+\epsilon},
\qquad |\lambda|>C_0,\ \Im\lambda>-\beta.
$$

**Answer: No.** The claim is false as stated, already at the level of
holomorphic continuation, before any bound. The obstruction is structural:
under the standard definition of convex cocompact, closed (compact)
hyperbolic $3$-manifolds are admissible, their limit set is all of $S^2$
(hence contains every round circle), and their Laplacian has eigenvalues
tending to $+\infty$, producing real resolvent poles arbitrarily far out in
$\mathcal U$.

## 2. Counterexample class

Recall the standard Kleinian-group terminology (see e.g. Maskit,
Matsuzaki–Taniguchi, Kapovich):

- $\Gamma<\mathrm{PSL}(2,\mathbb C)$ is **convex cocompact** if it is
  finitely generated, has no parabolic elements, and the convex core of
  $M=\Gamma\backslash\mathbb H^3$ is compact. In particular every
  torsion-free **cocompact** lattice $\Gamma$ is convex cocompact, with
  convex core the whole compact manifold $X=\Gamma\backslash\mathbb H^3$.
- If $\Gamma$ is cocompact, its domain of discontinuity
  $\Omega(\Gamma)\subset S^2$ is empty; equivalently the limit set satisfies
  $\Lambda_\Gamma=S^2$. Indeed, a nonempty $\Omega$ would give boundary at
  infinity / ends, contradicting compactness of $\Gamma\backslash\mathbb H^3$.

Classical $3$-manifold theory gives existence of closed hyperbolic
$3$-manifolds: e.g. the Weeks manifold (Weeks 1985; rigor verified in
subsequent literature), or closed arithmetic examples via Borel's existence
of uniform lattices in $\mathrm{PSL}(2,\mathbb C)$, passed to a torsion-free
finite-index subgroup by Selberg's lemma. Fix any such torsion-free
cocompact $\Gamma$ and $X=\Gamma\backslash\mathbb H^3$ closed hyperbolic.
Then:

(i) $X$ is convex cocompact in the sense above;
(ii) $\Lambda_\Gamma=S^2$, which contains every round circle, so the
  target's hypothesis is satisfied in the strongest possible way.

Hence, if the target were true, such an $X$ would admit $C_0,\beta>0$ with
holomorphic continuation of $\chi R(\lambda)\chi$ to $\mathcal U$ for every
cutoff $\chi$.

## 3. Spectrum and poles

On a closed Riemannian manifold $X$, the (nonnegative) Laplacian $-\Delta$
with domain $H^2(X)$ is self-adjoint on $L^2(X)$, has compact resolvent by
Rellich compactness plus elliptic estimates, and hence infinite discrete
spectrum
$$
0=E_0<E_1\le E_2\le\cdots\to +\infty,
$$
with a complete orthonormal eigenbasis $\{\phi_j\}$,
$-\Delta\phi_j=E_j\phi_j$. This is standard elliptic/spectral theory.

For $\Im\lambda>1$ a direct check gives
$E_j-1-\lambda^2\ne 0$ for all $j$ (if $\lambda=a+ib$, $b>1$: either
$a\ne 0$ and $\Im(E_j-1-\lambda^2)=-2ab\ne 0$, or $a=0$ and
$E_j-1+b^2\ge b^2-1>0$), so $R(\lambda)$ is bounded on $L^2(X)$ and acts
diagonally:
$$
R(\lambda)\phi_j=(E_j-1-\lambda^2)^{-1}\phi_j,
\qquad \Im\lambda>1.
$$

Since $X$ is compact, $L^2_{\mathrm{comp}}(X)=L^2_{\mathrm{loc}}(X)=L^2(X)$,
and the constant function $\chi\equiv 1$ is an admissible compactly
supported smooth cutoff. For this $\chi$, $\chi R(\lambda)\chi=R(\lambda)$,
so the target's universal cutoff quantifier applies directly to $R$ itself.
(The only alternative reading, an existential cutoff, is trivialized by
$\chi=0$ and cannot be intended.)

## 4. Contradiction

Because $E_j\to+\infty$, all but finitely many eigenvalues satisfy
$E_j>1$. For each such $j$ put $\mu_j=\sqrt{E_j-1}>0$; then $\mu_j\to+\infty$
along the positive real axis. Suppose, toward contradiction, that for some
$C_0,\beta>0$ the operator family $F(\lambda)=\chi R(\lambda)\chi$ with
$\chi\equiv 1$ extended holomorphically from $\Im\lambda>1$ to all of
$\mathcal U=\{|\lambda|>C_0,\Im\lambda>-\beta\}$. Then for any fixed $j$ the
scalar function
$$
f_j(\lambda)=\langle\phi_j,F(\lambda)\phi_j\rangle_{L^2}
$$
would be holomorphic on $\mathcal U$, while agreeing with
$(E_j-1-\lambda^2)^{-1}$ on $\{\Im\lambda>1\}\cap\mathcal U$ (nonempty open).
By analytic continuation the two agree on $\mathcal U\setminus\{\pm\mu_j\}$,
but the right-hand side has a pole at $\lambda=\mu_j$. Choosing $j$ large
enough that $\mu_j>C_0$ (hence $\mu_j\in\mathcal U$ since
$\Im\mu_j=0>-\beta$), holomorphicity of $f_j$ on all of $\mathcal U$ is
impossible. Explicitly, $|f_j(\lambda)|\to\infty$ as
$\lambda\to\mu_j$ within $\mathcal U$.

Therefore no pair $(C_0,\beta)$ gives a holomorphic continuation to
$\mathcal U$, and a fortiori the claimed polynomial bound cannot hold on
$\mathcal U$. This refutes the target already for a single admissible $X$,
hence refutes the universal claim over the stated class, whether constants
are allowed to depend on $X$ or required to be uniform.

## 5. Remarks on scope

- The argument uses only: (a) cocompact implies convex cocompact with full
  limit set (standard Kleinian geometry); (b) existence of one closed
  hyperbolic $3$-manifold (classical); (c) discrete Laplacian spectrum
  $E_j\to\infty$ on closed manifolds (standard elliptic theory). No
  fractal-uncertainty, microlocal, or resonance-free-strip machinery is needed
  because the compact case short-circuits the problem.
- The natural repair is to exclude compact $X$ (e.g. require $X$ noncompact /
  infinite-volume, $\Lambda_\Gamma\ne S^2$), after which the question becomes
  the genuine open problem about gaps for Schottky-type or circle-containing
  infinite-volume examples. That repaired statement is not addressed here.
- Proof vs.\ computation: this is a deductive disproof; no numerical
  computation is required. No literature search was used beyond standard
  textbook facts cited above.

## 6. Conclusion

The target claim is **false**: a closed hyperbolic $3$-manifold $X$
satisfies the hypothesis ($\Lambda_\Gamma=S^2$ contains every round circle)
but its cutoff resolvent has infinitely many real poles tending to $+\infty$,
so no resonance-free strip $\{|\lambda|>C_0,\Im\lambda>-\beta\}$ with the
stated holomorphic continuation and bound exists. ∎
