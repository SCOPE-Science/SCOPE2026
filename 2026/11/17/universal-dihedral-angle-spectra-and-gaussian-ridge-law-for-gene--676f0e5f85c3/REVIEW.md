# Independent mathematical audit

## correctness

PASS

The proof explicitly uses the previously published complete facet and vertex descriptions for generalized parking-function polytopes: lower normals -e_i and upper normals 1_S with all nonempty S except |S|=n−1 when b1=1. At a simple vertex, nested upper facets, all lower/lower pairs, disjoint upper/lower pairs, and the classical b1=1 exceptional full-upper/lower incidences exhaust codimension-2 ridges. For S⊊T, outward normal cosine sqrt(|S|/|T|) gives interior angle π−acos sqrt(s/t), while orthogonal pairs give right angles and exceptional inner product −1/sqrt(n) yields acute acos(1/sqrt(n). Subset enumeration counts nested upper incidences by 3^n−2^{n+1}+1, removing n(2^{n−1}−1) in classical case; all right and n acute counts match. Independent direct subset-pair enumerations for n=3..6 verified both regimes (n=4: nonclassical U=50,R=34,A=0; classical U=22,R=30,A=4). The dominant nested pairs equal a ternary assignment up to O(n(2/3)^n) in total variation; multinomial delta method on s/(s+t) at (1/3,1/3) yields variance 3/8 and angle derivative 1 at ratio 1/2, proving 3π/4 Gaussian limit. verify_angles.py source independently forms actual facet/vertex incidence and checks 18 finite cases; its floating affine ranks are corroboration, not an all-n proof.

## originality

PASS

Fresh best-of-knowledge primary-source and published-mathematics comparison of the exact final theorem, not a claim of exhaustive historical priority. Candidate takes known face lattice as input and proves new metric and random sampling statements; not identical to a prior enumerated angular table. Priority risk is close derivability from known data, especially for the finite angle formula.

## value

PASS

A full Euclidean ridge-angle multiset and its high-dimensional random-ridge limit are natural extrinsic metric invariants not captured merely by face counts. Uniformity over all remaining parking parameters, the sharp classical-only acute orbit and the explicit variance 3/8 give reusable geometric and probabilistic structure; the published combinatorial facet data are credited rather than relabeled as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
