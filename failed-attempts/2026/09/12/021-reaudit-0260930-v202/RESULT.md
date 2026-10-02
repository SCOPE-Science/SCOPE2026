# K2P single-triangle quarnet D12|34 does not have dimension 7: certified dimension at least 13

## Context

Exact dimensions of phylogenetic network varieties control parameter-count identifiability, degrees of freedom contributed by triangle interiors beyond displayed trees, and penalty terms in algebraic model selection. Dimension formulas for group-based level-1 networks established in the triangle-free setting do not settle the 3-cycle case for even-order state groups. The admitted target asked whether the Kimura two-parameter (K2P) Fourier phylogenetic variety of the named single-triangle quarnet D12|34 has Krull dimension exactly 7.

## Definitions and object

Let D12|34 be the binary semi-directed level-1 quarnet on taxa {1,2,3,4} with split 12|34, one 3-cycle, and hybrid leaf-child 1. Work in K2P Fourier coordinates over G = Z2 x Z2 with classes identity (0,0), transition (0,1), and transversions (1,0),(1,1), edge normalization a_e^0 = 1, per-edge parameters (t_e,s_e) = (transition,transversion), nine network edges rc, r4, ca, c3, ab, b2, ah, bh, h1, plus interior mixture parameter delta (keep b->h) versus 1-delta (keep a->h), for 19 parameters total.

There are 64 consistent Fourier patterns p=(g1,g2,g3,g4) with g1+g2+g3+g4=0. Put s=g1+g2. The corrected parametrization is

- M1(p) = bh(g1) h1(g1) b2(g2) c3(g3) r4(g4) ab(s) ca(s) rc(g4),
- M2(p) = ah(g1) h1(g1) ab(g2) b2(g2) c3(g3) r4(g4) ca(s) rc(g4),
- q(p) = delta M1(p) + (1-delta) M2(p).

The root-edge exponent is g1+g2+g3=-g4=g4 in Z2 x Z2. Each edge factor contributes t_e on a transition, s_e on a transversion, and 1 on the identity. The phylogenetic variety is the Zariski closure of the image of this polynomial map.

## Result

The K2P Fourier phylogenetic variety of D12|34 has Krull dimension at least 13. In particular, its dimension is not 7.

For the displayed tree obtained by keeping b->h, the corresponding K2P monomial image has dimension exactly 10.

## Proof / evidence

Evaluate at the explicit rational torus point t_e=(2+i)/3 and s_e=(1+i)/4, with i enumerating the nine edges in the order rc,r4,ca,c3,ab,b2,ah,bh,h1, and delta=1/5. Every edge parameter is nonzero.

1. **Network lower bound.** The exact 64x19 Jacobian over Q has rank 13 at this point. A nonzero 13x13 minor uses rows
   [1,2,4,5,8,10,16,20,24,32,36,40,44]
   and columns
   [t_rc,s_rc,t_ca,s_ca,t_c3,s_c3,t_ab,s_ab,t_b2,s_b2,t_ah,s_ah,t_bh].
   Its determinant is
   160576479/4194304 != 0.
   Hence the image variety has dimension at least 13.

2. **Displayed-tree dimension.** The displayed-tree map is monomial. Its 64-row exponent matrix in the 16 nonidentity edge-class coordinates has exact rank 10. The image dimension of a monomial map on the algebraic torus equals this exponent rank, so the displayed-tree K2P locus has dimension exactly 10. An exact torus-Jacobian computation independently gives rank 10.

Therefore 13>7, so the target assertion “Krull dimension exactly 7” is rigorously false.

## Correction relative to the earlier package

The earlier RESULT and verifier placed the root edge rc at exponent s=g1+g2. That is not the phylogenetic Fourier exponent for the rooted edge in this topology. The correct exponent is g1+g2+g3=g4. Recomputing from the corrected map changes the displayed 13x13 minor (its determinant is 160576479/4194304 rather than 160576479/2097152) but leaves the decisive rank lower bound 13 unchanged. The research conclusion therefore survives after repair.

## Limitations

Only the falsification of dimension 7 through the certified lower bound dim>=13 is proved here. The exact network dimension is not established because no matching algebraic upper bound is supplied. The certificate is for the stated K2P Fourier normalization with a_e^0=1 and uniform-root conventions; it does not establish analogous claims for JC, K3P, or other normalizations.

## Reproducibility

Run `python3 output/artifacts/verify_disproof.py`. The corrected stdlib-only script rebuilds the map with rc(g4), certifies the nonzero 13x13 minor above, verifies displayed-tree exponent rank 10, and prints `VERIFY_OK`.

## References

- E. Gross, R. Krone, S. Martin, *Dimensions of Level-1 Group-Based Phylogenetic Networks*, Bulletin of Mathematical Biology 86 (2024), arXiv:2307.15166.
- S. Cox, E. Gross, S. Martin, *Group-based phylogenetic models on 3-sunlet networks*, Bulletin of Mathematical Biology 87, 132 (2025), DOI 10.1007/s11538-025-01506-1. Their dimension theorem treats odd-order groups; the paper explicitly states that even-order groups remain open under their method.
