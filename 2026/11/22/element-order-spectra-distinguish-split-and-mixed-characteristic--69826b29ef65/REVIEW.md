# Independent mathematical audit

## correctness

PASS

The abelian unit group is the direct product of its elementary abelian principal units, 1+m, and the cyclic prime-to-p factor T of order q-1. For t in T of order ell>1, a=t(1+w) has 1-a invertible, so every translation part is conjugate away. The orders are ell when w=0 and p*ell otherwise. For t=1, the power formula (b,1+w)^n=(nb+binom(n,2)wb,1+nw) follows using w^2=0. At n=p the odd-characteristic binomial term vanishes, since p*m=0, leaving (pb,1). In characteristic p every nonidentity member of this sector has order p; in characteristic p^2, pb vanishes precisely on m since the map from F_q to m given by multiplication by p is nonzero and F_q-linear. Exactly (q-1)q^(2d) elements have order p^2. The counts exhaust |G|=q^(2d+1)(q-1). For the class-size comparison, fixing a leaves unit orbits on R/(1-a)R with each orbit multiplied in size by |(1-a)R|; these are one trivial quotient if 1-a is invertible, or zero, the units and the nonzero scalar lines of the radical in R or in R/F_q w otherwise. All sizes depend only on q,d. For degrees, the trivial additive character has stabilizer R^units; nontrivial characters factoring through F_q form one orbit of size q-1. For a nonzero radical character the principal units act transitively on its q extensions, because w acts by twisting with the residue character b mod m -> chi(wb). Scalar orbits of radical characters have size q-1. In the abelian semidirect product each stabilizer character yields one irrep of degree the orbit size, so the full degree multiset is likewise independent of characteristic. The displayed rings are local, have radical dimension d, and have characters p and p^2 respectively. An independent direct group multiplication run for p=3,d=2 in both models at /workspace/branches/e7e0aabb-3977-46bc-ae51-42c203d4dcdf/element_order_reproduction.py reproduced the listed coefficients and order 486; it is corroboration, not the general proof. The supplied verifier was not executed.

## originality

PASS

The class-size and degree coincidences are known consequences of the square-zero Borel data, and stronger order data already cover the principal-radical boundary omitted from the new claim. No inspected source was found to furnish the d>=2 all-parameter order distribution or its separation of the two families with matching classical multisets.

## value

PASS

Element order is a basic diagnostic for whether the affine group retains ring characteristic after the classical size and degree multisets have forgotten it. The result gives both a uniform exact distribution for the natural nonprincipal square-zero class and an explicit infinite family illustrating the extra discriminating power, not just the observation that translations in a mixed-characteristic ring can have order p^2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
