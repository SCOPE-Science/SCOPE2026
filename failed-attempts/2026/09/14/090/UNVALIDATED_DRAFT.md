# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact rational neighborhoods beyond the endomorphism-ring bound

## Theorem (TARGET)

Let $p>3$ be prime, $\ell\ne p$ prime, and $E/\mathbf{F}_p$ supersingular
with $j=j(E)\notin\{0,1728\}$. Then $t=0$, $\pi^2=-p$ for Frobenius $\pi$,
and with $q_j\ge 1$ minimal write $\mathcal{O}=\mathrm{End}(E_{\bar\mathbf{F}_p})$
as the Ibukiyama order $\mathcal{O}(q_j)$ or $\mathcal{O}'(q_j)$.
Assume $\ell\nmid 2q_j$. Then:

1. **Dictionary (no bound).** $\mathcal{O}/\ell\mathcal{O}\cong M_2(\mathbf{F}_\ell)$;
   there are exactly $\ell+1$ left $\mathcal{O}$-ideals $I$ of norm $\ell$,
   in bijection with geometric subgroups $C\subset E[\ell]$
   (Deuring; $j\ne 0,1728$ gives trivial fiber from extra automorphisms).
2. **Fiber condition (necessary and sufficient).** For geometric $j'$,
   $s(j'):=\mathrm{mult}_{Y=j'}\Phi_\ell(j,Y)$ equals the number of norm-$\ell$
   left ideals $I$ with $j(\mathcal{O}_R(I))=j'$, where the $j$-invariant of
   a maximal order type is read off via Deuring (Hilbert-class data for the
   explicit orders $\mathcal{O}(q_j),\mathcal{O}'(q_j)$). Two ideals give the
   same target iff their right orders are $B$-conjugate. No inequality on
   $p,q_j,\ell$ is used: enumeration of the $\ell+1$ ideals and their right
   orders is a finite computation in the quaternion algebra.
3. **Frobenius action and $r$.** $C$ is Frobenius-stable iff its ideal class
   is fixed by $\pi$-conjugation. Hence
   $r(j'):=\#\{C\ \mathrm{rational}: j(E/C)=j'\}$ is the number of
   $\pi$-fixed ideals in the fiber over $j'$. Total rational kernels:
   $\sum_{j'}r(j')=1+\bigl(\frac{-p}{\ell}\bigr)\in\{0,2\}$, the fixed points
   of $\bar\pi\in M_2(\mathbf{F}_\ell)$ of characteristic polynomial
   $X^2+p$ acting on $\mathbf{P}^1(\mathbf{F}_\ell)$.
4. **Factorization.** The $\mathbf{F}_p$-roots of $\Phi_\ell(j,Y)$ are exactly
   the $j'$ with $r(j')>0$; non-rational roots occur in Frobenius orbits whose
   degrees are the orbit sizes on non-fixed fiber elements. Loops
   ($j'=j$) and collisions (distinct kernels, same $j'$) are counted by the
   fiber sizes $s(j')$ vs fixed points $r(j')$.

In particular $r_{E,\ell}$ and $s_{E,\ell}$ are determined explicitly from
$\mathcal{O}(q_j)$/$\mathcal{O}'(q_j)$ plus modular/Hilbert-class data, with
no hypothesis $p>q_j\ell^2$ or $p>4q_j\ell^2$. The old bound only served to
force unique small generators identifying right-order types; full ideal
enumeration replaces it.

## Proof sketch

- Trace: $E/\mathbf{F}_p$ supersingular, $p>3$ $\Rightarrow$ $t=0$ ($t=\pm p,
  \pm2p$ impossible by Hasse for $p>3$; $t=\pm p$ contradicts supersingularity
  parity). So $\pi^2=-p$.
- $\ell\nmid 2q_j$ keeps $\ell$ away from the discriminant of the Ibukiyama
  order, so $\mathcal{O}\otimes\mathbf{F}_\ell\cong M_2(\mathbf{F}_\ell)$ and
  norm-$\ell$ left ideals correspond to $\mathbf{F}_\ell$-lines: $\ell+1$.
- Deuring correspondence $I\leftrightarrow (E\to E/C)$ is unconditional;
  excluding $j=0,1728$ kills the extra-automorphism ambiguity, so
  $s(j')$ = fiber cardinality and $r(j')$ = fixed-point count.
- $\bar\pi$ has $\mathrm{tr}=0$, $\det=p$; fixed lines exist iff $-p$ is a
  quadratic residue mod $\ell$: count $1+(\frac{-p}{\ell})$.
- Factorization claim follows because $j(E/C)\in\mathbf{F}_p\iff C$ is
  Galois-stable, and $\Phi_\ell(j,j')=0\iff j'$ is some $j(E/C)$.

## Verified illustrating example (violates old bound)

$p=13$, $E:y^2=x^3+x+4$, $\ell=3$ (certificate `artifacts/example_check.py`):

- $\#E(\mathbf{F}_{13})=14$, trace $0$ (supersingular); $j=5\ne0,1728\equiv12$.
- Old bound needs $p>4q\ell^2\ge 36$: fails for every $q_j\ge1$ (so for the
  actual minimal $q_j$ too).
- $\psi_3$ has **no** $\mathbf{F}_{13}$ root $\Rightarrow$ 0 rational
  3-kernels $=1+(\frac{-13}{3})=1+(\frac{2}{3})=0$. ✓
- $\gcd(\psi_3,\psi_3')=1$ $\Rightarrow$ 4 distinct geometric 3-subgroups
  $=\ell+1$, all non-rational, forming Frobenius orbits of degree $>1$;
  $\Phi_3(5,Y)$ has no $\mathbf{F}_{13}$ root. ✓

## Limitations / scope

- Excludes $j=0,1728$ (extra automorphisms) and $\ell\mid 2q_j$ (non-split
  $\mathcal{O}/\ell\mathcal{O}$), as in the target statement.
- Uses standard Deuring/Tate/Ibukiyama inputs as black boxes; the novelty is
  removing the size bound via full fiber enumeration.
- Computation covers one violating example ($p=13,\ell=3$); general claim is
  proved deductively, not by exhaustion.
