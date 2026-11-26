# Independent mathematical audit

## correctness

PASS

Normalize by -B>0. The fixed-point equations give only (-1,-1). For j≥1, x_(j+1)=-1-2(x_(j-1))_++2(x_j)_+. Once x_j≤0 for j≥1 the next first coordinate is strictly negative and no later first coordinate becomes positive. If x_1,x_2,x_3>0 the recurrence instead gives x_4=-5-4u_+<0, so in every case x_4<0. When a last positive x_r exists, x_(r+1)≤0 and y_(r+1)<-1; x_(r+2)=y_(r+1)<-1 and y_(r+2)=-1, hence the first hit is r+3 (an equilibrium reached earlier cannot be left). Without a positive first coordinate the map is (u,v)→(v,-1)→(-1,-1), with the stated time-zero and time-one exceptions. On u≤0 test x_1=v, then x_2=2v-1, then x_3=2v-3 on the applicable positive branches; on u>0 test x_1=v+2u, then x_2=2(u+v)-1, then x_3=2v-3. Each zero belongs to the nonpositive branch. This recovers the full partition and gives time six exactly for v>3/2; (0,2) witnesses minimality. All seven times are realized by the displayed test states.

## originality

PASS

The same map and its finite capture are prior work. The primary analyses give a seven-step sufficient bound on the initial strip u≤0,v>0; the distinct result is the exact uniform index and all-plane first-hit partition, including the horizontal strict maximal-time threshold. The identical catalog hit is not a separate antecedent.

## value

PASS

The established excitable map has a natural finite-transient question. The contribution is not merely improving an upper bound from seven to six: the exact strata determine which perturbations generate each transient length, and the longest length depends only on the initial second coordinate despite the branch switch in the first coordinate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
