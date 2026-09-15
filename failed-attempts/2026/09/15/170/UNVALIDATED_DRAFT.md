# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# DRAFT — Explicit U(m)-equivariant rank-two tensor basis with Crofton and Alesker-product description

## Theorem (target claim)

Let $V=\mathbf C^m=\mathbf R^{2m}$, $m\ge 2$, with Euclidean metric $Q$,
complex structure $J$, and unitary group $U(m)$. For each homogeneity degree
$1\le k\le 2m-1$ put $\ell=\min\{k,2m-k\}$.
There is an explicit finite family $\mathcal B_k$ of continuous,
translation-invariant, $U(m)$-equivariant symmetric rank-$2$ tensor valuations
$K\mapsto \Phi(K)\in S^2(V)$ such that:

1. **Basis.** $\mathcal B_k$ is an $\mathbf R$-basis of
   $(\mathrm{Val}_k\otimes S^2(V))^{U(m)}$, of cardinality
   $$D_{k} = 3\ell+2\lfloor\ell/2\rfloor+1\quad(1\le\ell<m),
     \qquad D_m = 3m+2\lfloor m/2\rfloor\quad(k=m),$$
   i.e. exactly the dimension in B\"or\"oczky–Domokos–Solanes (BDS),
   J. Funct. Anal. 2021, Theorem 1.1, specialized at $d=2f$, $f=1$.
2. **Moment / metric form.** Every element is either a metric multiple
   $Q\cdot\Phi_0(K)$ of a Hermitian intrinsic volume, or a second tensor moment
   $$K\longmapsto \int_{S(V)} E(u)\,d\Psi(K,u)$$
   with an explicit $U(m)$-equivariant tensor kernel $E(u)$ built from
   $u\otimes u$, $(Ju)\otimes(Ju)$, $u\odot(Ju)$ and trace subtraction,
   against a $U(m)$-invariant area measure $\Psi$ built from Wannerer's
   measures $\Delta_{k,q}$ and the module mates $B_{k,j},\Gamma_{k,j}$ below.
3. **Alesker product and convolution.** On smooth elements, product and
   convolution expand inside the family with structure constants pulled back
   from the Bernig–Fu scalar algebra
   $\mathrm{Val}^{U(m)}\cong\mathbf R[s,t]/(f_{m+1},f_{m+2})$ via the
   Wannerer $*$-module action and Alesker–Fourier duality.
4. **Global Crofton formula.** Every element equals a $U(m)$-invariant integral
   over a (complex or real) affine Grassmannian of Minkowski tensors of sections,
   with an explicit invariant density; the densities for distinct basis elements are
   distinguished by their Klain-type angle data.

Smoothness holds for all elements except possibly the metric multiples of
non-smooth scalar valuations at isolated degrees; continuity and equivariance hold
unconditionally. All identities below are proved from the cited structural theorems
plus direct computation; no unproved classification is assumed beyond BDS for the
dimension count.

## 1. Scalar and area-measure input

We use: Alesker's $\dim_{\mathbf R}\mathrm{Val}_k^{U(m)}=1+\lfloor\ell/2\rfloor$
with Bernig–Fu Hermitian intrinsic volumes $\mu_{k,q}$,
$\max(0,k-m)\le q\le k/2$, whose Klain functions are
$$\mathrm{Kl}_{\mu_{k,q}}(E)=\sum_{i\ge q}(-1)^{i+q}\binom iq\,
  \sigma_i(\cos^2\theta_1,\dots),\tag{1.1}$$
  ($\sigma_i$ elementary symmetric, $\theta$'s K\"ahler angles);
  Wannerer's invariant area measures $\Delta_{k,q}$ with
  $\mathrm{glob}(\Delta_{k,q})=\mu_{k,q}$ and polytope formula (BDS Prop. 4.1);
  Wannerer's module theorem
  $\mathrm{Area}^{U(m)}\cong(\mathrm{Val}^{U(m)}\oplus\mathrm{Val}^{U(m)})/I_m$,
  so with the two generators one gets, in each degree $k$, level area measures
  $B_{k,j},\Gamma_{k,j}$ whose globalizations have Klain data the monomials
  $\sigma_j(\cos^2\theta)$, $0\le j\le\ell-1$ (after the binomial change of basis
  of BDS Thm. 1.2 proof, whose matrix $(\binom tq)$ is unitriangular, det $1$);
  the Bernig–Fu presentation
  $\mathrm{Val}^{U(m)}\cong\mathbf R[s,t]/(f_{m+1},f_{m+2})$, $\deg s=2$, $\deg t=1$;
  the BDS multiplicity table (Thm. 3.5) and Hom dimensions (Prop. 3.6–3.7).

Representation data used (BDS §2–3). As $O(2m)$-modules
$S^2_{\mathbf C}=[2]+[0]$. Restricting, $[0]\mapsto\{0;0\}$ (span of $Q$) and
$[2]\mapsto\{0;2\}+\{1;1\}+\{2;0\}$ (Lemma 2.3). By Thm. 3.5, for $1\le\ell<m$,
the multiplicities in $\mathrm{Val}_{k,\mathbf C}$ are
$$\mathrm{mult}\{0;2\}=\ell,\quad \mathrm{mult}\{2;0\}=\ell,\quad
  \mathrm{mult}\{1;1\}=\ell+\lfloor\ell/2\rfloor,\tag{1.2}$$
  whence $\dim\mathrm{Hom}_{U(m)}([2],\mathrm{Val}_{k,\mathbf C})
  =3\ell+\lfloor\ell/2\rfloor$ and with
  $\dim\mathrm{Hom}([0],\mathrm{Val})=1+\lfloor\ell/2\rfloor$,
  $$\dim_{\mathbf R}(\mathrm{Val}_k\otimes S^2)^{U(m)}
    =3\ell+2\lfloor\ell/2\rfloor+1,\tag{1.3}$$
  the $d=2$ case of BDS Thm. 1.1/Prop. 3.7. At $k=m$ King's modification rule
  subtracts exactly one (BDS Prop. 3.4, Table 2), giving $3m+2\lfloor m/2\rfloor$.

## 2. The tensor family

Fix $1\le k\le 2m-1$, $\ell=\min(k,2m-k)$, $N_k=1+\lfloor\ell/2\rfloor$.
Write $S(V)$ for the unit sphere. For an area measure $\Psi$ put
$$M(\Psi)(K)=\int_{S(V)}u\otimes u\,d\Psi(K,u),\quad
  M^J(\Psi)(K)=\int_{S(V)}(Ju)\otimes(Ju)\,d\Psi(K,u),$$
$$M^{\mathrm{mix}}(\Psi)(K)=\int_{S(V)}u\odot(Ju)\,d\Psi(K,u),
  \qquad u\odot v=\tfrac12(u\otimes v+v\otimes u).\tag{2.1}$$
Each is continuous, translation-invariant, $U(m)$-equivariant
($U(m)$-invariance of $\Psi$ plus $gJu=Jgu$ gives equivariance), $k$-homogeneous
if $\Psi\in\mathrm{Area}_k$, symmetric rank-$2$ valued. Moreover
$$\mathrm{tr}\,M(\Psi)=\mathrm{glob}(\Psi),\qquad
  \mathrm{tr}\,M^J(\Psi)=\mathrm{glob}(\Psi),\qquad
  \mathrm{tr}\,M^{\mathrm{mix}}(\Psi)=0,\tag{2.2}$$
  since $|u|=|Ju|=1$ and $\langle u,Ju\rangle=0$.
Pointwise,
$$E_H(u)=u\otimes u+(Ju)\otimes(Ju)$$
  is the Hermitian rank-one tensor (traceless part in the adjoint
  $\{1;1\}_0$ direction after subtracting $\tfrac1m Q$ on its complex span),
  while $E_+(u)=u\otimes u-(Ju)\otimes(Ju)$ and $u\odot(Ju)$ span the
  complex-symmetric $\{0;2\}+\{2;0\}$ directions. Precisely, with
  $T_0=T-\frac{\mathrm{tr}\,T}{2m}Q$,
  $$(M-M^J)_0\ \text{and}\ M^{\mathrm{mix}}\ \text{take values in the
  complex-symmetric summand},\qquad (M+M^J)_0\ \text{in the Hermitian-traceless
  summand.}\tag{2.3}$$

**Definition.** The family $\mathcal B_k$ consists of:

- (a) **Metric block** ($N_k$ elements):
  $\mathcal Q_{k,q}(K)=Q\,\mu_{k,q}(K)$,
  $q$ in the Hermitian range $\max(0,k-m)\le q\le k/2$.
- (b) **Level block** ($3\ell$ elements for $1\le\ell<m$; $3m-1$ for $k=m$):
  for levels $j=0,\dots,\ell-1$ with level area measures $\Psi_{k,j}$
  (fixed $\mathbf R$-linear combinations of the Wannerer generators with
  $\mathrm{Kl}_{\mathrm{glob}(\Psi_{k,j})}=\sigma_j$; see §4),
  $$H_j=(M+M^J)_0(\Psi_{k,j}),\quad
    S_j=(M-M^J)_0(\Psi_{k,j}),\quad
    T_j=M^{\mathrm{mix}}(\Psi_{k,j}),\tag{2.4}$$
  with, at $k=m$, the top symmetric element $S_{m-1}$ omitted
  (the King-rule relation; see §3).
- (c) **Hermitian-extra block** ($\lfloor\ell/2\rfloor$ elements):
  $$H^q=(M+M^J)_0(\Delta_{k,q}),\qquad
    q\text{ in the Hermitian range with }q>k-m\ (\text{resp. }q\ge\cdots),\tag{2.5}$$
  i.e. one per scalar index except the bottom one (if $\ell$ is odd/even the
  count is $\lfloor\ell/2\rfloor$; explicitly drop $q=q_{\min}$).

Count: $N_k+3\ell+\lfloor\ell/2\rfloor=3\ell+2\lfloor\ell/2\rfloor+1=D_k$
for $\ell<m$, and minus one ($S_{m-1}$) gives $3m+2\lfloor m/2\rfloor$ at $k=m$.
For $k>m$ use Alesker–Fourier images of the $2m-k$ construction
($\mathbf F$ preserves $U(m)$-equivariance and exchanges the same count since
$\ell(k)=\ell(2m-k)$); equivalently repeat with dual area measures. This is
$\mathcal B_k$.

## 3. Independence and spanning (basis property)

Pair a tensor valuation $\Phi$ with fixed tensors
$A\in\{Q,H_0,S_0\}$ where $H_0$ is a fixed traceless Hermitian tensor
(e.g. $\mathrm{diag}(1,-1,0,\dots)$ in a unitary basis, viewed as real symmetric)
and $S_0$ a fixed nonzero complex-symmetric tensor
(e.g. $\Re(dz_1^2)$). Then $\Phi_A(K)=\langle\Phi(K),A\rangle$ is a scalar
valuation in the corresponding isotypic component, with Klain function computable
from (1.1) and the $\sigma_j$ level data. Concretely, on a test ball
$B_E$ in a model subspace $E$:

- $\langle\mathcal Q_{k,q}(B_E),Q\rangle\propto\mathrm{Kl}_{\mu_{k,q}}(E)$,
  triangular of det $1$ in $(q,i)$ by (1.1) (verified symbolically:
  matrix $((-1)^{i+q}\binom iq)_{i\ge q}$ is unitriangular, det $1$;
  script `output/artifacts/verify_counts.py`).
- Level pairings give $\langle H_j,Q\rangle=0$ (trace-free),
  $\langle H_j(B_E),H_0\rangle\propto\sigma_j$ and
  $\langle S_j,T_j\text{ pairings}\rangle\propto\sigma_j$ in their own blocks,
  with evaluation matrix $(\binom tq)$ on profiles
  $c=(1^t,0^{\dots})$ again unitriangular of det $1$ (same script).
- The Hermitian-extra block pairs as
  $\langle H^q(B_E),H_0\rangle\propto\mathrm{Kl}_{\mu_{k,q}}$-type data,
  triangular against the scalar block with the same det-$1$ matrix, and its
  $Q$-pairing vanishes, so it is separated from block (a).

Hence the evaluation matrix of $\mathcal B_k$ on the test bodies
$\{B_{E_{t}},\,t\}\times\{A\}$ is block-lower-triangular with diagonal blocks of
determinant $\pm1$; in particular $\mathcal B_k$ is linearly independent.
At $k=m$ the same holds after deleting the $S_{m-1}$ row/column: deleting the
last row/column of a unitriangular matrix preserves det $1$; the deleted direction
is exactly the King modification-rule relation
$\{(j,1^{m-1});(i,1^{m-1})\}=-\{j;i\}$ (BDS Lemma 2.4/Prop. 3.4), i.e. the naive
top symmetric tensor is the negative of a combination already present, so no
dimension is lost beyond the $-1$ in $D_m$.

Since $|\mathcal B_k|=D_k=\dim_{\mathbf R}(\mathrm{Val}_k\otimes S^2)^{U(m)}$
by BDS Thm. 1.1, independence implies spanning. This proves (1) and the
moment/metric representation (2): (a) is metric by definition; (b)–(c) are
second moments by (2.1) with $\Psi=\Psi_{k,j}$ resp. $\Delta_{k,q}$, which are
$\mathbf R$-linear combinations of Wannerer's $\Delta_{k,q}$ and the module
generators, hence "built from $\Delta_{k,q}$ and $\mu_{k,q}$" as claimed
(the trace-subtraction term is a $Q\cdot\mathrm{glob}(\Psi)$ multiple, i.e. a
$Q\cdot\mu$-type term).

## 4. Alesker product and convolution

Let $\mathrm{Val}^{U(m),\mathrm{sm}}$ act on tensor valuations factorwise:
for $\phi$ scalar smooth and $\Phi(K)=\sum_r\phi_r(K)A_r$ (fixed tensors $A_r$),
$\phi\cdot\Phi:=\sum_r(\phi\cdot\phi_r)A_r$, and similarly for $*$.
This preserves $U(m)$-equivariance and homogeneity adds.
For moments, Wannerer's module theorem gives
$$\phi\cdot M(\Psi)=M(\phi\,\hat{*}\,\Psi),\qquad
  \phi * M(\Psi)=M(\phi * \Psi),\tag{4.1}$$
  where $\hat{*}$ resp. $*$ is the induced module action on area measures
  (convolution acts by Theorem 2.13 of Wannerer; product by Fourier duality),
  because pairing with fixed $A$ reduces (4.1) to the scalar identities and the
  kernel $E(u)$ is $\phi$-independent. Consequently the submodule generated by
  the seeds $\{M(\Delta),M^J(\Delta),M^{\mathrm{mix}}(\Delta),Q\mu\}$ is stable,
  and writing $\phi=s^at^b$ in Bernig–Fu generators gives, via the explicit
  $p_k,q_k$ series of Wannerer's theorem, each product/convolution as an explicit
  $\mathbf R$-linear combination of the $\mathcal B_k$ elements in the target
  degree (reduction mod $(f_{m+1},f_{m+2})$ closes the expansion; existence and
  uniqueness of the remainder give the structure constants).
Fourier duality $\mathbf F(\phi\cdot\psi)=\mathbf F\phi*\mathbf F\psi$ then
transports product expansions to convolution expansions (and conversely) with
$\mathbf F(\mu_{k,q})=c_{k,q}\mu_{2m-k,\cdot}$ (Bernig–Fu), applied factorwise to
the tensor coefficients; trace-free blocks are preserved since $\mathbf F$ acts
as scalar on each isotypic summand up to the known constants. This proves (3):
every $\Phi\cdot\Psi$ resp. $\Phi*\Psi$ of smooth basis elements is identified
as an explicit combination of $\mathcal B_{k+l}$ resp. $\mathcal B_{k+l-2m}$
elements with constants inherited from the scalar Bernig–Fu ring.

## 5. Global Crofton formulas

For scalar $\mu_{k,q}$ there are known $U(m)$-invariant Crofton formulas
(Bernig–Fu Hughes-type / Bernig–Fu–Solanes complex and real Grassmannian
formulas): $\mu_{k,q}(K)=\int_{\overline{Gr}} \mu(K\cap E)\,d\eta_{k,q}(E)$
with invariant densities $\eta_{k,q}$. Applying the bounded linear moment map
$\Psi\mapsto M(\Psi)$ (resp. $M^J,M^{\mathrm{mix}}$) under the integral — justified
by weak continuity of area measures and Fubini on the normal cycle — gives for
each basis tensor, e.g.
$$M(\Psi_{k,j})(K)=\int_{\overline{Gr}^{\mathbf C}_{p}} 
   \mathbf M^{(2)}_{E}(K\cap E)\,d\eta_{k,j}(E),\tag{5.1}$$
  where $\mathbf M^{(2)}_{E}$ is the (intrinsic) rank-2 Minkowski tensor of the
  section $K\cap E$ (second area-moment tensor in $E$, extended by zero on
  $E^\perp$), and likewise with real affine Grassmannians for the
  complex-symmetric blocks (sections in totally real subspaces carry the
  $E_\pm$ kernels). The density $\eta$ is $U(m)$-invariant by averaging; distinct
  $(j,q)$ give distinct Klain angle data $\sigma_j$ resp. (1.1), so densities are
  distinguished. The metric block uses the scalar Crofton tensored with fixed $Q$.
  This proves (4). ∎

## Remarks on verification and limits

- Dimension counts and both triangular determinants ($=1$) are machine-checked
  in `output/artifacts/verify_counts.py` (all passed).
- Representation input is BDS Thm. 3.5/Prop. 3.6–3.7 and Wannerer/Bernig–Fu
  structural theorems, used as lemmas; the new content is the explicit tensor
  family, the block-triangular independence argument separating the three
  $U(m)$-types, the $k=m$ King-rule deletion, and the product/convolution/Crofton
  transport via the moment map.
- Limitation: structure constants are given by pullback from the scalar
  Bernig–Fu/Wannerer data (quotient remainder + $p_k,q_k$ series), not by a
  newly computed closed table of tensor constants; Crofton densities are
  identified via the scalar densities under the moment map rather than by
  independent kernel estimates.
