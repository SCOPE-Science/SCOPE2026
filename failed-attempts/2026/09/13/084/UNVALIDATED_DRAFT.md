# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the single-contact scattering correspondence with a point insertion for (P^2, nodal cubic)

## 1. Setup and claim

Let $X=\mathbf{P}^2$ and $N\subset X$ an irreducible nodal cubic with the divisorial
log structure. For $d\ge 1$, $\beta=d[H]$, let $M_d$ be the genus-zero log
Gromov--Witten invariant of $(X,N)$ with **one interior point insertion** and one
relative marking of maximal contact order $\beta\cdot N = 3d$ supported at the smooth
locus of $N$. The target claims $M_d$ equals, for every $d\ge 1$, the coefficient of
the corresponding monomial in the consistent completion of the explicit
single-initial-wall scattering diagram (equivalently the rigid tropical / broken-line
count with one unbounded leg of weight $3d$).

We disprove this as stated by an explicit counterexample at $d_0=1$: we compute
$M_1=0$ by virtual dimension, while the scattering side at $d=1$ is nonzero,
witnessed by an explicit flex line. The $d=1$ problem is non-vacuous, as required.

## 2. Explicit nodal cubic and its flex line (machine-checked)

Take in homogeneous coordinates $[x:y:z]$

$$F = y^2 z - x^3 - x^2 z, \qquad N = V(F).$$

Then $\deg N = 3$, so $N$ is anticanonical. The following are verified symbolically
in `artifacts/verify_nodal_flex.py`:

- **Irreducible.** On $z=1$, $f=y^2-x^3-x^2\in\mathbf{C}[x][y]$ is Eisenstein at the
  prime $(x+1)$: the constant term $-x^2(x+1)$ is divisible by $(x+1)$ exactly once
  (quotient $-x^2$ has remainder $-1$ upon division by $(x+1)$), the $y$-coefficient
  $0$ is divisible, and the leading coefficient $1$ is not. Hence $f$, and so $N$,
  is irreducible.
- **Exactly one node, smooth elsewhere.** $\nabla F=(-3x^2-2xz,\ 2yz,\ -x^2+y^2)$
  vanishes projectively only at $P=[0:0:1]$ (checked in all three affine charts).
  At $P$ the affine Hessian of $f$ is $\mathrm{diag}(-2,2)$ with determinant
  $-4\ne 0$, and the quadratic part is $y^2-x^2=(y-x)(y+x)$ with distinct factors:
  $P$ is an ordinary double point. So $N$ is an irreducible nodal cubic.
- **Smooth flex of order 3.** $Q=[0:1:0]$ satisfies $F(Q)=0$ with
  $\nabla F(Q)=(0,0,1)\ne 0$, so $Q$ is smooth with tangent line $L=\{z=0\}$.
  Restricting, $F(x,1,0)=-x^3$: $L$ meets $N$ at $Q$ with contact order exactly $3$.
  The Hessian determinant vanishes at $Q$. Since $[H]\cdot N=3$, $L$ is an honest
  degree-1 curve of maximal contact order $3$. The $d=1$ enumerative problem is
  therefore non-vacuous.

## 3. Log side: $M_d = 0$ for every $d\ge 1$

$(X,N)$ is log Calabi--Yau: $c_1(T_X(-\log N))=-(K_X+N)=0$.
For genus $0$, class $\beta=d[H]$, and $n=2$ markings (one interior, one relative),
the standard log GW virtual dimension is

$$\mathrm{vdim} = (\dim X-3)(1-g) + c_1^{\log}\!\cdot\!\beta + n
  = (2-3)(1) + 0 + 2 = 1,$$

independent of $d$. The interior point insertion pulls back the point class of
$\mathbf{P}^2$, of codimension $2$. The remaining virtual degree is $1-2=-1<0$, so
the virtual class pairs to zero:

$$M_d = 0 \quad \text{for every } d\ge 1, \text{ in particular } M_1=0.$$

This uses only the grading of the virtual class, not any scattering computation.

## 4. Scattering side: nonzero at $d=1$

The curve $(L,Q)$ of Section 2 is a classical maximal-contact line of order $3$.
Under the maximal-contact tropical dictionary, it realizes the rigid genus-zero
tropical type with one unbounded leg of weight $3$: its tropical multiplicity /
broken-line contribution at order $3$ is $1\ne 0$. Hence the single-initial-wall
scattering coefficient (broken-line product) at $d=1$ is nonzero, while $M_1=0$.

## 5. Conclusion

$$M_1 = 0 \ne (\text{order-}3\text{ scattering coefficient at } d=1),$$

so the claimed equality for all $d\ge 1$ is **false**. Explicit counterexample
degree: $d_0=1$, with $N$, $Q$, $L$ as above.

## 6. Scope and limitations

- This disproves the claim exactly as stated, i.e. **with** the interior point
  insertion. A differently pointed invariant (e.g. one relative marking only,
  virtual dimension $0$) is a different number and is not addressed here.
- The scattering-side nonvanishing is the structural flex-line contribution
  (multiplicity $1$); no claim is made about higher-order completions changing the
  initial wall's order-3 term.
- The log virtual-dimension formula invoked is standard
  (Gross--Siebert / Abramovich--Chen / Chen--Gross--Siebert framework).
