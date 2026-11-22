# Independent mathematical audit

## correctness

PASS

For every finite field F_q the elementary product bracket has coordinates (a d′-d a′, d f′-f d′, a e′-e a′+b f′-f b′). With (d,d′) nonzero the first two equations impose one independent nonzero functional each, contributing q^2(q^2-1); with both zero they contribute q^4 only when u=v=0. The final functional on (b,e,b′,e′) vanishes precisely when a=a′=f=f′=0. Accounting for q^2 central-entry choices gives F=q^5 M-q^7 1_(u=v=0)+q^8 1_(u=v=w=0) and all three claimed formulas. The adjoint coefficient matrix has ranks 0,1,2,3 in the stated cases d=0 or d !=0 and (a,f)=0 or not, with populations q, q(q^2-1), q^3(q^2+q-2), q^3(q-1)(q^2-1). No characteristic division is used. Independent SymPy identities show sum of target masses is q^12, rank populations q^6, and the rank-weighted zero fiber equals F(0). Independently reconstructed literal matrix products and finite-field elimination exhaust all 2^12 and 3^12 input pairs and all q^6 adjoint ranks for q=2,3. These finite checks corroborate, but do not establish, the universal proof.

## originality

FAIL

Decisive earlier published source contains EXACTLY the same three target-fiber polynomials, their multiplicities, surjectivity onto the derived ideal, the SAME four adjoint-rank multiplicities, and the identical commuting probability for precisely n_4(F_q) in every characteristic. The earlier work explicitly gives the rank distribution as a zero-fiber cross-check, so neither half of the assigned result is left over. The earlier source was first publicly committed on 2026-10-25 19:49:48 UTC, whereas the assigned source was first committed on 2026-11-08 19:36:16 UTC. The identical formulas are not merely related parameter choices; they have the same matrix algebra, bracket, target decomposition, finite-field domain, normalizations and conclusions.

## value

FAIL

The exact n_4 target-fiber distribution is a meaningful natural class-three Lie algebra invariant in isolation, but all three target strata, complete four-rank adjoint table, and normalized commuting probability already appear verbatim in the earlier full result for the same algebra and all q. No independently unknown structural lemma, new cutoff, or additional classification remains. Rearranging the direct counting proof and supplying more small-field computations is not an independent mathematical contribution; narrowing to only the rank table also fails because the earlier source states that exact table. No scientific repair survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
