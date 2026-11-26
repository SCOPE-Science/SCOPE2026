# Independent mathematical audit

## correctness

PASS

Reconstructed over an arbitrary field of characteristic two. A^3=0 puts A^2 in the two-sided annihilator; noncommutativity needs at least two independent directions modulo A^2. Thus below dimension four only the three-dimensional, one-dimensional-square case can occur. For B=[[a,b],[c,d]], e=b+c≠0, multiplying by P=[[0,d/e],[a/e,1]] gives P^tB+BP=B, with no additional restriction on K or on det B. The projection onto the square is local: use that scaling derivation on the square and a central shear killing the square at each vector outside it. It violates Leibniz on a nonzero product of complement vectors. In the exhibited four-dimensional algebra det B=1; A²=Ann(A)=Kc and a hypothetical square-zero direct summand would sit inside the other summand's square. In the equation P^tB+BP=sB, entries (11),(21) kill p21,p32; (22),(23),(32) give p12=p23=s and p13=0; comparison of (13),(31) kills p23 and s. The remaining restrictions give a scalar diagonal and unrestricted p31. This gives exactly two quotient parameters and three independent central shears. The tests at y,z,y+z,x,x+y force precisely that quotient form even over F₂; locality also kills c. The two-local map is validated by extending prescribed values on two quotient vectors to a functional (homogeneity handles dependent inputs). Read verify.py and its saved transcript: the latter corroborates the 5/5 ranks over F₂,F₄,F₈ and 8,192,3584 lower-dimensional forms, but the replay of the displayed symbolic identities and pointwise argument above, not the finite script, is the proof for arbitrary fields. Uploaded code was inspected, not run. Its docstring's invocation name is stale; VERIFICATION.md gives the actual file name.

## originality

PASS

The bounded comparison supports the noncommutative characteristic-two two-step cutoff and the explicit witness, not novelty of the general derivation machinery or of the nonlinear two-local illustration.

## value

PASS

This gives the first possible noncommutative dimension within the stipulated characteristic-two two-step class, not just an isolated new multiplication table. The uniform smaller-dimension obstruction and the indecomposable witness identify why the familiar square-projection obstruction can stop working. The explicit small derivation space also gives a useful example separating rigidity for linear local maps from nonadditive 2-local maps. The conclusion is not a classification at dimension four or a claim outside A³=0.

The dated certificate retains the supplied scientific assessment, sources and limitations.
