# Independent mathematical audit

## correctness

PASS

With unit facet normals, P_r is the intersection of all inward-translated supporting halfspaces; dist(v,P_r+rB)=max(0,dist(v,P_r)-r). Convexity of the distance function reduces maximal opening loss to vertices. For each vertex its incident facet constraints imply dist(v,P_r)>=r lambda_v; the minimizing feasible tangent displacement meets nonincident facets for all sufficiently small r, giving local equality. In plane lambda_v=csc(theta_v/2). The polygon angle sum yields min theta <=(n-2)pi/n and global E/r>=sec(pi/n)-1. For regular n-gons the exact homothetic erosion gives equality all 0<r<=Rin. Monotone inverse-cosecant gives all-angle stability; rhombus perturbation proves linear order cannot improve. Independent square/rhombus check E/r=sqrt(2)-1, and inspected supplied clipping/LP numerical code; finite geometry checks do not establish all polygons.

## originality

PASS

The general morphological opening and known corner rounding are prior. The explicit all-d convex polytope small-radius tangent-cone Hausdorff coefficient, sharp every-radius fixed-n bound sec(pi/n)-1, equality angle rigidity and quantitative global angular stability are not supplied by the inspected Cappello regularity paper or Heppes qualitative opening/area-perimeter bounds. Best-of-knowledge; classical morphology equivalence remains risk.

## value

PASS

Polygonal ball opening is a natural nonsmooth convex-geometric approximation; its exact corner-controlled Hausdorff error, universal sharp side-count minimax and quantitative angle rigidity are connected structural invariants. General polytope tangent-cone certificate explains the two-dimensional bound and supplies a reusable local obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
