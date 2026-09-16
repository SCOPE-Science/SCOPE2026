# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Rigidity of 4D shrinking ρ-Einstein solitons with half harmonic Weyl curvature

## The rho-deformed half-harmonic eigenvector lemma, with sharp degeneracy

**Setting (the target's exact objects).** Let $(M^4,g,f)$ satisfy the gradient
$\rho$-Einstein soliton equation

$$R_{ij}+\nabla_i\nabla_j f=(\rho R+\lambda)\,g_{ij},\qquad \lambda>0,$$

with fixed $\rho\notin\{1/4,1/6\}$. Let $W^\pm$ be the self-dual /
anti-self-dual parts of the Weyl tensor in dimension $4$ and
$\delta W^\pm=0$ the half-harmonic condition ($\delta=-\operatorname{div}$;
vanishing is convention-independent).

**Claim (proved here).**
At every point with $df\ne 0$, $\delta W^+=0$ (resp. $\delta W^-=0$) forces
$\nabla f$ to be an eigenvector of $\mathrm{Ric}$:

$$R_{1a}=0,\qquad \nabla R\parallel\nabla f,\qquad
e_1:=\nabla f/|\nabla f|,\ a\in\{2,3,4\}.$$

The constant $\rho=1/6$ is sharp for this implication: the operative test
factor is exactly $(\rho-1/6)$, which vanishes identically at $\rho=1/6$.
Together with the trace degeneracy at $\rho=1/4$, this explains both
exclusions in the target. The $\rho=0$ case recovers Lemma 2.4 of Wu–Wu–Wylie.

**Conventions.** We fix sign conventions so that the contracted second Bianchi
identity reads $\operatorname{div}\mathrm{Ric}=\tfrac12\,dR$ and the Hessian
commutation reads
$\nabla_i\nabla_j\nabla_k f-\nabla_j\nabla_i\nabla_k f=-R_{ijk}{}^{\ell}\nabla_\ell f$
in the notation below; equivalently, all identities are normalized by their
$\rho=0$ reductions, which are checked against Wu–Wu–Wylie Lemmas 2.2–2.4.
Only the *relative* coefficient $(\rho-1/6)$ between the $\rho$-correction and
the Riemannian $1/6$ term matters, and it is verified independently in
`output/artifacts/rho_eigenvector_check.py`.

## Lemma A (rho-soliton identities)

(i) **Trace.**
$R+\Delta f=4(\rho R+\lambda)$, i.e.
$\Delta f=(4\rho-1)R+4\lambda$.
The link between $\Delta f$ and $R$ degenerates at $\rho=1/4$.

(ii) **Contraction.** $\mathrm{Ric}(\nabla f)=c\,\nabla R$ with
$c=(1-6\rho)/2$.
*Proof.* Take the divergence of the soliton equation. With
$\operatorname{div}\mathrm{Ric}=\tfrac12 dR$ (contracted Bianchi, no soliton
input) and $\operatorname{div}\mathrm{Hess}\,f=d\Delta f+\mathrm{Ric}(\nabla f)$
(Hessian commutation), plus $d\Delta f=(4\rho-1)\,dR$ from (i):
$$\tfrac12 dR+(4\rho-1)\,dR+\mathrm{Ric}(\nabla f)=\rho\,dR,$$
so $\mathrm{Ric}(\nabla f)=(\rho-\tfrac12-4\rho+1)\,dR=(\tfrac12-3\rho)\,dR$.
At $\rho=0$ this is $\mathrm{Ric}(\nabla f)=\tfrac12\nabla R$ (Wu–Wu–Wylie
Lemma 2.2); the identity is vacuous at $\rho=1/6$.

(iii) **Drift scalar.**
$$\Delta_f R:=\Delta R-\langle\nabla f,\nabla R\rangle
=\frac{6\rho}{1-6\rho}\langle\nabla f,\nabla R\rangle
+\frac{2\big((\rho R+\lambda)R-|\mathrm{Ric}|^2\big)}{1-6\rho}.$$
*Proof.* Differentiate (ii) and trace:
$c\,\Delta R=\nabla_j(R_{jk}\nabla^k f)
=(\nabla_jR_{jk})\nabla^k f+R_{jk}\nabla^j\nabla^k f
=\tfrac12\langle dR,df\rangle+\langle\mathrm{Ric},
(\rho R+\lambda)g-\mathrm{Ric}\rangle$.
Divide by $c=(1-6\rho)/2$ and subtract $\langle dR,df\rangle$.
At $\rho=0$: $\Delta_fR=2\lambda R-2|\mathrm{Ric}|^2$ (their (5)).
Numerically verified in `output/artifacts/rho_soliton_identities.py`.

## Lemma B (rho-deformed $D$-tensor)

With $D^\rho_{jkl}:=2\nabla_iW_{ijkl}-W_{ijkl}\nabla^i f$,

$$D^\rho_{jkl}=\tfrac12(R_{jl}\nabla_kf-R_{jk}\nabla_lf)
+\frac{1-6\rho}{12}(\nabla_kR\,g_{jl}-\nabla_lR\,g_{jk})
-\frac{R}{6}(g_{jl}\nabla_kf-g_{jk}\nabla_lf),$$

and $D^{\rho,\pm}$ is given by halving each coefficient and adding the dual
(${}'$) copy, exactly as in Wu–Wu–Wylie Lemma 2.3.
*Proof.* Follow their Lemma 2.3 proof verbatim, tracking two changes:
$\nabla_iR_{ijkl}=R_{ijkl}\nabla^i f+\rho(\nabla_kR\,g_{jl}-\nabla_lR\,g_{jk})$
(soliton antisymmetrized), and
$R_{ijkl}\nabla^i f=W_{ijkl}\nabla^i f+\tfrac12(R_{jl}\nabla_kf-R_{jk}\nabla_lf)
+\tfrac{c}{2}(\nabla_kR\,g_{jl}-\nabla_lR\,g_{jk})
-\tfrac{R}{6}(g_{jl}\nabla_kf-g_{jk}\nabla_lf)$
with $c=(1-6\rho)/2$ from Lemma A(ii). Since
$2\operatorname{div}W=\operatorname{div}\mathrm{Rm}-\tfrac16\,dR\wedge g$
is purely Riemannian, subtracting gives the $dR\wedge g$ coefficient
$c/2+\rho-1/6=(1-6\rho)/12$. At $\rho=0$ this is $1/12$ (their formula).
Coefficient algebra verified in `output/artifacts/rho_eigenvector_check.py`.

## Theorem (eigenvector + sharpness)

*Proof.* Let $\delta W^\pm=0$, i.e. $\nabla_iW^\pm_{ijkl}=0$, and put
$e_1=\nabla f/|\nabla f|$ at a point with $df\ne0$.
From Lemma B's derivation, the $\pm$ equation reads

$$R_{ijkl}\nabla^i f+R_{ijk'l'}\nabla^i f
+\rho\big[(\wedge)+(\wedge)'\big]
=4\nabla_iW^\pm_{ijkl}+\tfrac16\big[(\wedge)+(\wedge)'\big],$$

where $(\wedge)=(\nabla_kR\,g_{jl}-\nabla_lR\,g_{jk})$ and $(\wedge)'$ is its
dual. Take $j=k=1$, $l\ne1$. Then $R_{i11l}\nabla^i f=|\nabla f|R_{111l}=0$
and likewise for the dual term, by antisymmetry in the first two slots.
Since $(1\,l\,1'\,l')$ is a permutation of $(1234)$, $1',l',k'\ne1$, so
$g_{1l'}=g_{1k'}=0$ and the dual brackets vanish; the unprimed bracket is
$-\nabla_lR$. With $\nabla W^\pm=0$:

$$-\rho\,\nabla_lR=-\tfrac16\,\nabla_lR,\qquad\text{i.e.}\quad
(\rho-\tfrac16)\,\nabla_lR=0,\quad l\ne1.$$

Hence for $\rho\ne1/6$: $\nabla_lR=0$ ($l\ne1$), so
$\nabla R\parallel e_1\parallel\nabla f$; by Lemma A(ii) with $c\ne0$,
$R_{1a}|\nabla f|=c\cdot0=0$. ∎

*Sharpness.* At $\rho=1/6$ the factor $(\rho-1/6)$ is identically zero, so
these test components yield no information; simultaneously $c=0$ empties
Lemma A(ii) and the drift formula (iii) blows up. The exclusion
$\rho=1/6$ is therefore sharp for this route (no counterexample at
$\rho=1/6$ is claimed).

## Proposition (computed: pointwise algebra does not suffice)

The Weyl symmetry constraints in dimension $4$ cut out a $10$-dimensional
space (SVD check). The $12$ half-harmonic linear conditions on the pair
$(W,D)$ have rank $6$ (nullity $7$ in the $13$-dimensional $(w,D)$ space);
each $D_a$ direction retains a nullspace component (projection residual
$0.931$). Hence pointwise $\delta W^\pm=0$ alone does **not** force $D=0$ or
full $\delta W=0$: the upgrade to the target's rigidity conclusion genuinely
requires the global argument (rho-Weitzenböck, maximum principle,
analyticity, rho-rigidity chain). Reproduced by
`output/artifacts/asd_linear_system.py`.

## Status of the full target (honest delimitation)

*Proved here:* Lemma A (all of (i)–(iii)), Lemma B, Theorem above,
Proposition above.
*Computed:* coefficient/degeneracy/drift checks; Weyl-dim-10 and rank-6
linear-algebra facts.
*Cited (not re-proved):* Wu–Wu–Wylie full $\rho=0$ classification
(arXiv:1410.7303; Calc. Var. 2018, doi:10.1007/s00526-018-1415-x); Cao–Chen
Bach-flat classification; Catino–Mastrolia–Monticelli fourth-order Weyl
result; Andrade–Borges–Reis 2025 Bach-flat $\rho$-soliton facts.
*Open (blocked within this pass):* the $\rho$-modified Weitzenböck identity
for $|W^\pm|$, nonnegativity of the resulting $\rho$-parameter algebraic
quantity $\phi_\rho$ (Timofte-type check as a function of $\rho$),
$R\ge0$/growth control for general $\rho$, and the terminal harmonic-Weyl
$\rho$-rigidity implication. No counterexample to the target was found; the
target is neither proved nor disproved here.

## References

- J.-Y. Wu, P. Wu, W. Wylie, *Gradient shrinking Ricci solitons of half
  harmonic Weyl curvature*, arXiv:1410.7303; doi:10.1007/s00526-018-1415-x.
- H.-D. Cao, Q. Chen, *On Bach-flat gradient shrinking Ricci solitons*,
  doi:10.1215/00127094-2147649.
- G. Catino, P. Mastrolia, D. Monticelli, *Gradient Ricci solitons with
  vanishing conditions on Weyl*, doi:10.1016/j.matpur.2016.10.007.
- M. Andrade, V. Borges, H. Reis, *On gradient $\rho$-Einstein solitons with
  Bach tensor radially nonnegative*, arXiv:2503.24337.
- B.-L. Chen (shrinking solitons have $R\ge0$); G. Huang (integral-pinched
  shrinking $\rho$-solitons, arXiv:1612.08512) — cited for the open remainder.
