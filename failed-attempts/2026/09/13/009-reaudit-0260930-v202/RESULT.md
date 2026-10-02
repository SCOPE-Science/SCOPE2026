# Genus-two b1=2 SL2 Heegaard character-stack intersection: Lagrangian models and tangent cohomology

## Context
Let G=SL_2(C), let Σ be a closed oriented genus-two surface, and let H_+,H_- be genus-two handlebodies. Glue their boundaries by the separating Dehn twist about c=[a_1,b_1]. Let M=H_+∪_ΣH_- and W=Loc_G(M).

## Result
1. X=Loc_G(Σ) is a 0-shifted symplectic derived character stack, and the restriction maps Loc_G(H_±)→X carry the standard boundary Lagrangian structures. Their derived fiber product is W=Loc_G(M).
2. Killing the handlebody meridians b_1,b_2 makes c=[a_1,b_1] trivial, so the chosen separating twist does not change the resulting Heegaard presentation. Thus π_1(M)≅F_2 and H_*(M;Z)≅(Z,Z^2,Z^2,Z); topologically M is the genus-two double #^2(S^1×S^2).
3. At the trivial representation ρ, the tangent complex is T_ρW≃C^*(M;sl_2)[1]. Hence
   dim H^{-1}=3, dim H^0=6, dim H^1=6, dim H^2=3,
   its Euler/virtual dimension is -3+6-6+3=0, and Poincaré duality gives H^i(T_ρW)≅H^{1-i}(T_ρW)^∨.
4. The classical truncation of the representation stack is [G^2/G]. The tangent-cohomology dimensions above do not by themselves compute local Tor groups, a Tor amplitude, a Behrend value, or any loop-rotation invariant. No such identification is claimed here.

## Proof sketch
The mapping-stack and Lagrangian statements are the standard PTVV/Calaque boundary construction for oriented manifolds. Under the handlebody quotient, b_i=1 and therefore c=[a_1,b_1]=1; the separating twist becomes invisible in the induced presentation. Mayer–Vietoris gives Betti numbers (1,2,2,1). At the trivial local system, ad ρ is the constant three-dimensional local system sl_2, so H^j(M;ad ρ)≅H^j(M;C)⊗sl_2. The mapping-stack tangent formula T_ρLoc_G(M)≃C^*(M;ad ρ)[1] yields the displayed dimensions and duality.

## Reproducibility
`artifacts/verify_heegaard.py` checks the Mayer–Vietoris rank, the six-dimensional isotropic handlebody image in the twelve-dimensional Goldman space, and the tangent dimensions/virtual dimension. `artifacts/verify_heegaard.json` stores its expected exact output.

## Limitations
This is a local tangent calculation at the trivial representation. It does not compute derived local Tor groups or a Behrend/DT invariant, and it makes no claim about irreducible components or global enumerative geometry.

## References
- Pantev–Toën–Vaquié–Vezzosi, *Shifted Symplectic Structures*, arXiv:1111.3209.
- Calaque, *Lagrangian structures on mapping stacks and semi-classical TFTs*, arXiv:1306.3235.
