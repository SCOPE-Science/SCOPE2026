# No U-polarized K3^[2] fourfold carries two holomorphic Lagrangian fibrations along its two isotropic rays

## Context

Let $X$ be a projective irreducible holomorphic symplectic fourfold of
$K3^{[2]}$-type. Its second cohomology carries the Beauville–Bogomolov–Fujiki
form $q$ on
$L=U^3\oplus E_8(-1)^2\oplus\langle-2\rangle$.
Assume $NS(X)\cong U$ is spanned by primitive isotropic classes $f_1,f_2$
with $(f_1,f_2)=1$. The question is whether holomorphic Lagrangian
fibrations can occur along both isotropic rays on the same $X$.

## Definitions

- For $x=af_1+bf_2$ in $U$, $q(x)=2ab$.
- For $K3^{[2]}$-type, the relevant primitive wall classes have square $-2$,
  or square $-10$ with divisibility 2.
- If $\pi:X\to\mathbf P^2$ is a holomorphic Lagrangian fibration, then
  $F=\pi^*\mathcal O(1)$ is nef and $q(F)=0$.
- Embed $U$ as the first $U$-summand of $L$, set
  $F_1=e_1$, $F_2=f_1$, $\delta=F_1-F_2$, and $T=U^\perp$.

## Result

The universal two-fibration claim is false. For every projective
$K3^{[2]}$-type fourfold with $NS(X)\cong U$ as above, at most one of the
two primitive isotropic rays is nef. Consequently the same fourfold cannot
carry holomorphic Lagrangian fibrations along both rays.

For the first-summand embedding, a very general period with Picard lattice
exactly $U$ and a Kähler class in one of the two chambers gives a
lattice-polarized existence witness. Reflection in the $(-2)$ class
$\delta$ is an integral monodromy reflection exchanging the two isotropic
rays at the lattice level. No assertion that this $(-2)$ wall crossing is a
Mukai flop is needed for the obstruction.

## Proof / evidence

1. The class $\delta=f_1-f_2$ has $q(\delta)=-2$, is primitive, and has
   divisibility one because $(\delta,F_1)=-1$ and $(\delta,F_2)=1$.
   Hence $\delta$ is a wall class. The reflection
   $R_\delta(x)=x+(x,\delta)\delta$ is an integral involution, swaps
   $F_1$ and $F_2$, fixes $F_1+F_2$, and fixes $T$ pointwise.

2. In $U$, square $-2$ means $ab=-1$, so the only primitive such classes
   are $\pm\delta$. Square $-10$ means $ab=-5$; every primitive solution
   has coprime coefficients and therefore divisibility one in this
   unimodular $U$ summand. Thus there is no square-$-10$, divisibility-2
   wall in this copy of $U$.

   Moreover $(f_1,\delta)=-1$, $(f_2,\delta)=1$, and
   $q(f_1+f_2)=2>0$. Therefore $\delta^\perp$ crosses the interior of the
   positive cone and strictly separates the two isotropic boundary rays.
   A Kähler chamber lies on one side, and its nef closure contains at most
   one of the two isotropic rays.

3. A holomorphic Lagrangian fibration has nef isotropic pullback class.
   Since $q(af_1+bf_2)=2ab$, every isotropic class in $U$ lies on one of
   the two boundary rays. Step 2 therefore prevents both rays from
   supporting holomorphic fibrations on the same $X$.

4. For the first-summand embedding,
   $T\cong U^2\oplus E_8(-1)^2\oplus\langle-2\rangle$ has nonempty period
   domain. A very general period has Picard lattice exactly $U$. Taking
   $\kappa=2F_1+F_2$ gives $q(\kappa)=4$ and
   $(\kappa,\delta)=-1$. Period-map surjectivity and global
   Torelli/chamber realization provide a marked projective fourfold with
   Kähler cone the chamber containing $\kappa$. Its nef closure contains
   the $f_1$ ray and excludes the $f_2$ ray.

   The reflection $R_\delta$ is the monodromy reflection attached to the
   $(-2)$ class. The result uses only chamber separation and makes no
   Mukai-flop claim for this wall.

## Limitations

The argument invokes established wall-class, Kähler-cone, monodromy,
period-map and Torelli results. The exhibited fourfold comes from a
period/chamber existence argument rather than explicit equations. The
statement concerns holomorphic fibrations on one model, not rational
fibrations after birational modification.

## Reproducibility

Run `python3 artifacts/check_lattice.py` and
`python3 artifacts/check_embedding.py`. The archived outputs are
`artifacts/lattice_check.json` and `artifacts/embedding.json`.

## References

- E. Markman, *Prime exceptional divisors on holomorphic symplectic
  varieties and monodromy-reflections*, arXiv:0912.4981.
- G. Mongardi, *A note on the Kähler and Mori cones of hyperkähler
  manifolds*, arXiv:1307.0393.
- Amerik–Verbitsky on MBM classes and Kähler chambers.
- Matsushita and Hwang on holomorphic Lagrangian fibrations.
- Global Torelli and period-map results for irreducible holomorphic
  symplectic manifolds.
