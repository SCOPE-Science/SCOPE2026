# Independent mathematical audit

## correctness

PASS

Reconstructed the dual and the integral maps. A face cannot contain a disconnected triple, so the non-hub complex is X=sk_1(D)*sk_1(B); the hub link is (D_disc*sk_1(B_t)) disjoint union T_disc. In particular a missed neighbor can occur in the link only as an isolated vertex, and |B_t|=1 still gives a connected, contractible joined part. X is a 2-connected wedge of binom(a-2,2)binom(b-1,2) three-spheres; the link has t+1 components and its non-isolated part is a wedge of (a-2)binom(b-t-1,2) two-spheres. Nullhomotopy of the link inclusion gives the asserted dual wedge by the cone pushout. For successive dual inclusions the map on reduced link H_0 merges one isolated component and is a split surjection. On H_2 the map is the identity on the D factor tensored with the inclusion of complete-graph cycle lattices; the triangle basis obtained from a reference vertex in the smaller neighbor set exhibits a direct summand of the asserted codimension, also when that set has one or two vertices. In the natural relative sequence for (Y_t,X), H_1(Y_t) identifies with reduced link H_0 and H_3(Y_t) extends link H_2 by a fixed H_3(X). Thus the H_3 map is a primitive injection. Dualizing the free groups and applying natural combinatorial Alexander duality on a fixed ordered vertex set gives the stated original maps and degrees. The common H_3(X) contribution is positive, proving non-shellability of the pure original complex. The example (9,5,3,3) and (0,1,2,3) follows, including the last rank-zero kernel. The recorded artifacts/check_star.py and artifacts/check_maps.py checks cover 27 parameter choices and 54 degree/stage map-rank tests over F_2 only; the integral conclusions follow from the proof, not from those artifacts.

## originality

FAIL

A distinct indexed same-day record bf4d87cacd9e gives the same fixed-hub ordinary three-cut Alexander-dual wedge, integral original homology and both split persistence maps on the main domain a,b>=4, 0<=t<b. It adds the terminal stage t=b, while this frozen record adds b=3. This is demonstrated substantive overlap, not a conclusion that the other record came first or that the entire parameter domains are identical. The frozen record's central contribution is not established as distinct; b=3 is the same link calculation at a small endpoint (b=3,t=2 has a contractible joined link part), with no separate scientific motivation for an endpoint-only repair.

## value

PASS

As mathematics the full theorem isolates a natural contrast between localized and matching edge damage and determines integral maps, not only Betti numbers: it tracks exactly which ranks persist or appear at each spoke deletion. That is independently useful structural content, although the content is materially shared with the other indexed result. The b=3 parameter difference alone has no identified separate use sufficient for a repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
