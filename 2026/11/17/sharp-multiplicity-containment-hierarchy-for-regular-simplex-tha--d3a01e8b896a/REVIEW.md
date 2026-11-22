# Independent mathematical audit

## correctness

PASS

Writing x=ru, each Thales-ball constraint is r<=u.v_i. The simplex gauge equals d*r*(-min_i u.v_i). With I the m largest inner products and k the smallest, s_I=average v_i has norm sqrt((d+1-m)/(dm)), t_k=-v_k has norm 1 and s_I.t_k=1/d. The maximal product of two linear forms on the sphere is (||s_I||||t_k||+s_I.t_k)/2, yielding precisely the formula. Its unique positive top eigendirection aligns equal top m values, a unique bottom k, and exact m ball contacts, proving equality count and sharp lower-m condition. Sum v_i=0 implies U_(d+1)={0}. Direct source checker constructs all equality points for dimensions 2..11; reviewed its entire source and used analytic rank-two calculation for all d.

## originality

PASS

PASS best knowledge: multiplicity-superlevel external radial gauge with all equality points is not provided by earlier onefold diameter-ball covering, diameter-ball matching intersection, or simplex radial-facet overlaps. Related planar d=2,m=2 containment was already known and is not claimed in isolation.

## value

PASS

PASS: m-fold depth of a natural centroid-to-vertex diametral-ball arrangement, its sharp containment threshold and exact extremal contact classification provide a complete dimension-dependent geometric invariant, not a routine onefold-covering restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
