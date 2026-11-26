# Independent mathematical audit

## correctness

PASS

Let x=aH/2>2, b=s/a and y=a²h1h2/4, so unordered positive allocations correspond one-to-one to 0<y<=x²/4. Nilpotent Cayley multiplication gives M=dI+vN, where d=(1−x+y)/(1+x+y) and v=2bx(1−y)/(1+x+y)². The point y=1 has M=−qI, q=(x−2)/(x+2)>0; y<1 gives d<−q. For y>1 the increasing diagonal satisfies −q<d<=q²<q. Then q²I−MᵀM has positive leading diagonal and determinant (q²−d²)²−q²v², so the exact condition for a norm at least q is |v|>=(q²−d²)/q. Factoring q²−d² gives the equivalent b>=2(x²−2y−2)/(x²−4). The right side strictly decreases from 2 on the feasible interval, proving strict superiority of y=1 to every alternative if b>=2 and strict improvement immediately to its right if b<2. The quadratic with sum H and product 4/a² gives the stated unequal positive pair and norm. At H=4/a, the equal-step nilpotent factors multiply to zero; this boundary does not obey the equivalence. For s=0 all products are scalar, which does not make the designated product allocation optimal.

## originality

PASS

The distinct claim is the global iff threshold and unique optimality of a particular positive real split at fixed total duration. It is not the existence of a cancellation pair, the Cayley-map formula, the dissipativity boundary alone, or a general statement about transient growth. The strongest indexed analogues share either the model or the method/constraint but do not, in their available statements, imply this threshold.

## value

PASS

The exact threshold identifies when norm reduction should use cancellation of the nilpotent term rather than push the scalar attenuation further. Eigenvalues alone miss this trade-off. The threshold coincides with the boundary for Euclidean dissipativity, includes rigidity at equality, and gives a sharp unequal-step damping benchmark for analyzing nonnormal integrators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
